#!/usr/bin/env python3
"""Exhaustive exact audit of reverse-complement greedy assembly of DNA dimers.

No external dependencies. Run: python3 verify.py
"""
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb

ALPHABET = "ACGT"
COMPLEMENT = dict(zip(ALPHABET, "TGCA"))


def reverse_complement(word):
    return "".join(COMPLEMENT[c] for c in reversed(word))


def canonical(word):
    return min(word, reverse_complement(word))


REPRESENTATIVES = tuple(sorted({canonical(a + b) for a in ALPHABET for b in ALPHABET}))
assert REPRESENTATIVES == ("AA", "AC", "AG", "AT", "CA", "CC", "CG", "GA", "GC", "TA")


def overlap(a, b):
    """Proper suffix/prefix overlap: each contributor has a nonempty remainder."""
    for k in range(min(len(a), len(b)) - 1, 0, -1):
        if a[-k:] == b[:k]:
            return k
    return 0


def possible_greedy_successors(state):
    best_overlap = -1
    successors = set()
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            x, y = state[i], state[j]
            for u in (x, reverse_complement(x)):
                for v in (y, reverse_complement(y)):
                    for a, b in ((u, v), (v, u)):
                        t = overlap(a, b)
                        if t < best_overlap:
                            continue
                        if t > best_overlap:
                            best_overlap = t
                            successors.clear()
                        joined = canonical(a + b[t:])
                        rem = state[:i] + state[i + 1:j] + state[j + 1:] + (joined,)
                        successors.add(tuple(sorted(rem)))
    return successors


@lru_cache(None)
def longest_greedy(state):
    if len(state) == 1:
        return len(state[0])
    return max(longest_greedy(t) for t in possible_greedy_successors(state))


def optimal_length(representatives):
    """Exact oriented Hamiltonian path DP on labeled representative classes."""
    n = len(representatives)
    variants = [(s, reverse_complement(s)) for s in representatives]
    dp = {(1 << i, i, j): 2 for i in range(n) for j in (0, 1)}
    for mask in range(1, 1 << n):
        for i in range(n):
            if not mask & (1 << i):
                continue
            for orient in (0, 1):
                old = dp.get((mask, i, orient))
                if old is None:
                    continue
                for j in range(n):
                    if mask & (1 << j):
                        continue
                    for orient2 in (0, 1):
                        cost = old + 2 - overlap(variants[i][orient], variants[j][orient2])
                        key = (mask | (1 << j), j, orient2)
                        dp[key] = min(cost, dp.get(key, 1000))
    full = (1 << n) - 1
    return min(dp[full, i, j] for i in range(n) for j in (0, 1))


def brute_opt_small(words):
    """Independent direct permutation enumeration for at most four reads."""
    best = 999
    for ordering in permutations(words):
        for bits in product((0, 1), repeat=len(words)):
            seq = [s if bit == 0 else reverse_complement(s) for s, bit in zip(ordering, bits)]
            total = 2 + sum(2 - overlap(a, b) for a, b in zip(seq, seq[1:]))
            best = min(best, total)
    return best


def brute_greedy_small(state):
    """Independent explicit recursion without memoization, for up to three reads."""
    if len(state) == 1:
        return len(state[0])
    all_choices = []
    for i, j in combinations(range(len(state)), 2):
        for a in (state[i], reverse_complement(state[i])):
            for b in (state[j], reverse_complement(state[j])):
                for u, v in ((a, b), (b, a)):
                    ol = overlap(u, v)
                    others = [state[h] for h in range(len(state)) if h != i and h != j]
                    others.append(canonical(u + v[ol:]))
                    all_choices.append((ol, tuple(sorted(others))))
    top = max(z[0] for z in all_choices)
    return max(brute_greedy_small(st) for k, st in all_choices if k == top)


def main():
    by_n = []
    total_bad = 0
    maximum_ratio = (1, 1)
    for n in range(1, 11):
        bad = 0
        best = (1, 1)
        witness = None
        for subset in combinations(REPRESENTATIVES, n):
            result = longest_greedy(tuple(subset))
            exact = optimal_length(subset)
            assert result >= exact
            assert result - exact <= 1, (subset, result, exact)
            if n <= 4:
                assert exact == brute_opt_small(subset)
            if n <= 3:
                assert result == brute_greedy_small(tuple(subset))
            if result > exact:
                bad += 1
            if result * best[1] > exact * best[0]:
                best = (result, exact)
                witness = subset
            if result * maximum_ratio[1] > exact * maximum_ratio[0]:
                maximum_ratio = (result, exact)
        assert n == 1 or len(list(combinations(REPRESENTATIVES, n))) == comb(10, n)
        by_n.append((n, comb(10, n), bad, best[0], best[1], witness))
        total_bad += bad
    assert [r[2] for r in by_n] == [0, 0, 16, 55, 78, 69, 40, 17, 6, 1]
    assert [(r[3], r[4]) for r in by_n] == [
        (1, 1), (1, 1), (5, 4), (6, 5), (7, 6), (8, 7),
        (9, 8), (10, 9), (11, 10), (12, 11)
    ]
    assert maximum_ratio == (5, 4)
    assert total_bad == 282
    assert sum(row[1] for row in by_n) == 1023
    assert longest_greedy(("AA", "AC", "CA")) == 5
    assert optimal_length(("AA", "AC", "CA")) == 4
    assert all(any(x in "AACA" for x in (s, reverse_complement(s))) for s in ("AA", "AC", "CA"))
    # Explicit legal worst tie: GT+TG -> GTG; AA attaches with zero overlap.
    assert reverse_complement("AC") == "GT" and reverse_complement("CA") == "TG"
    assert overlap("GT", "TG") == 1
    assert max(overlap(a, b) for a in ("GTG", reverse_complement("GTG"))
               for b in ("AA", reverse_complement("AA"))) == 0
    assert max(overlap(b, a) for a in ("GTG", reverse_complement("GTG"))
               for b in ("AA", reverse_complement("AA"))) == 0
    print("representative_classes=", ",".join(REPRESENTATIVES), sep="")
    print("n subsets nonoptimal worst_greedy/opt")
    for n, total, bad, g, o, _ in by_n:
        print(n, total, bad, f"{g}/{o}")
    print("total_inputs=1023")
    print("nonoptimal_inputs=282")
    print("global_worst_ratio=5/4")
    print("max_additive_excess=1")
    print("canonical_witness=AA,AC,CA;opt=AACA;bad_greedy=GTGAA")
    print("greedy_memo_states=", longest_greedy.cache_info().currsize, sep="")
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
