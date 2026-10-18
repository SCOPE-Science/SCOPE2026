#!/usr/bin/env python3
"""Independent finite checks of six scattered-subsequence avoidance formulas.

Only the Python standard library is needed. This is finite corroboration;
the general classification is established by the run-decomposition proof.
"""

from collections import defaultdict
from itertools import product

PATTERNS = ("aabb", "abab", "abba", "baab", "baba", "bbaa")


def formula(pattern, A, B, K):
    if A == 0 or B == 0:
        return int(K == 0)
    if not 0 <= K <= A * B:
        return 0
    if pattern in ("baba", "bbaa"):
        K = A * B - K
    if pattern in ("abba", "baab"):
        return 1
    if pattern in ("abab", "baba"):
        if K == 0:
            return 1
        return sum(1 for j in range(1, A + 1)
                   if K % j == 0 and 1 <= K // j <= B)
    if pattern in ("aabb", "bbaa"):
        return int(K <= B) + sum(
            1 for i in range(B) for r in range(1, A)
            if K == B - i + r)
    raise ValueError(pattern)


def dynamic_counts(pattern, A, B):
    """DP for the greedy subsequence automaton, independent of run forms."""
    # key=(used-a, used-b, ab-count, matched-pattern-prefix)
    states = {(0, 0, 0, 0): 1}
    for _ in range(A + B):
        nxt = defaultdict(int)
        for (a, b, k, s), multiplicity in states.items():
            if a < A:
                ns = s + (pattern[s] == "a")
                if ns < len(pattern):
                    nxt[(a + 1, b, k, ns)] += multiplicity
            if b < B:
                ns = s + (pattern[s] == "b")
                if ns < len(pattern):
                    nxt[(a, b + 1, k + a, ns)] += multiplicity
        states = nxt
    out = defaultdict(int)
    for (a, b, k, _s), v in states.items():
        assert (a, b) == (A, B)
        out[k] += v
    return out


def has_subsequence(word, pattern):
    s = 0
    for letter in word:
        if letter == pattern[s]:
            s += 1
            if s == len(pattern):
                return True
    return False


def direct_counts(pattern, A, B):
    """Enumerate whole words and independently compute ab from a scan."""
    out = defaultdict(int)
    for tup in product("ab", repeat=A + B):
        if tup.count("a") != A:
            continue
        if has_subsequence(tup, pattern):
            continue
        na = k = 0
        for c in tup:
            if c == "a":
                na += 1
            else:
                k += na
        out[k] += 1
    return out


def main():
    dp_cells = brute_cells = 0
    for A in range(0, 15):
        for B in range(0, 15):
            for p in PATTERNS:
                got = dynamic_counts(p, A, B)
                for k in range(A * B + 1):
                    expected = formula(p, A, B, k)
                    assert got[k] == expected, (p, A, B, k, got[k], expected)
                    dp_cells += 1
                if A + B <= 11:
                    brute = direct_counts(p, A, B)
                    for k in range(A * B + 1):
                        assert brute[k] == got[k], (p, A, B, k)
                        brute_cells += 1
    print("PASS: all six patterns, 0 <= A,B <= 14, every 0 <= K <= AB")
    print(f"PASS: {dp_cells} DP-versus-formula cells")
    print(f"PASS: {brute_cells} direct-enumeration-versus-DP cells (A+B <= 11)")
    print("All tests exact integer arithmetic; no infinite-range inference from tests.")


if __name__ == "__main__":
    main()
