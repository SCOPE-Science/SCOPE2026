#!/usr/bin/env python3
"""Independent finite checks of a binary word transition/universality theorem.

Uses only Python's standard library. Finite verification corroborates the
all-length proofs; it does not establish them by itself.
"""
from collections import Counter
from itertools import combinations, product
from fractions import Fraction
from math import comb


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def arch_index(word):
    seen = set()
    k = 0
    for letter in word:
        seen.add(letter)
        if len(seen) == 2:
            k += 1
            seen.clear()
    return k


def direct_index(word):
    subs = {""}
    for symbol in word:
        subs |= {s + symbol for s in tuple(subs)}
    result = 0
    while all("".join(p) in subs for p in product("01", repeat=result + 1)):
        result += 1
    return result


def graph_matching_index(word):
    # Standard matching DP, not the greedy arch algorithm.
    edges = [a != b for a, b in zip(word, word[1:])]
    a, b = 0, 0
    # a: optimum on vertices so far; b: optimum one vertex earlier.
    for present in edges:
        a, b = max(a, b + (1 if present else -10**6)), a
    return a


def binomial_joint(n, t, k):
    if n == 0:
        return int(t == 0 and k == 0)
    if k == 0:
        return 2 * int(t == 0)
    return 2 * (choose(k - 1, t - k) * choose(n - k, k)
                + choose(k - 1, t - k - 1) * choose(n - k - 1, k))


def conditional_mean(n, t):
    if n == 1:
        assert t == 0
        return Fraction(0)
    m = n - 1
    return (m - t + 1) * sum((Fraction(choose(t, r), choose(m, r))
                              for r in range(1, t + 1, 2)), Fraction(0))


def transfer_poly(max_n):
    # States: P = pending incomplete arch; E = just completed an arch.
    # Track coefficient histograms indexed by (transition count, arch count).
    out = [Counter({(0, 0): 1})]
    pending = Counter({(0, 0): 2})
    ended = Counter()
    out.append(pending.copy())
    for n in range(2, max_n + 1):
        np = Counter()
        ne = Counter()
        for (t, k), num in pending.items():
            np[t, k] += num  # same symbol, still pending
            ne[t + 1, k + 1] += num  # opposite, arch closes
        for (t, k), num in ended.items():
            np[t, k] += num  # next symbol same as last
            np[t + 1, k] += num  # next symbol opposite
        pending, ended = np, ne
        out.append(pending + ended)
    return out


def check():
    # Direct scattered-subsequence definition, graph matching DP and arch count.
    for n in range(0, 11):
        for w in product('01', repeat=n):
            k = arch_index(w)
            assert k == direct_index(w) == graph_matching_index(w), (n, w)

    # Every indexed word through length 16, with exact two-parameter counts.
    for n in range(1, 17):
        observed = Counter()
        for w in product('01', repeat=n):
            t = sum(a != b for a, b in zip(w, w[1:]))
            observed[t, arch_index(w)] += 1
        assert sum(observed.values()) == 2**n
        for t in range(n):
            assert sum(observed[t, k] for k in range(n // 2 + 1)) == 2*choose(n-1,t)
            if t:
                admissible = [k for k in range(n//2+1) if observed[t,k]]
                assert admissible == list(range((t+1)//2, min(t,n//2)+1))
            for k in range(n//2+1):
                assert observed[t,k] == binomial_joint(n,t,k), (n,t,k)

    # DP transition implementation checks binomial coefficients through n=90.
    transfer = transfer_poly(90)
    for n, hist in enumerate(transfer):
        for t in range(max(1, n)):
            for k in range(n // 2 + 1):
                assert hist[t,k] == binomial_joint(n,t,k), ('transfer',n,t,k)
        assert sum(hist.values()) == 2**n
    # Independent enumeration of transition-edge subsets for conditional means.
    for m in range(1, 12):
        for t in range(m + 1):
            total = 0
            for positions in combinations(range(m), t):
                last = -2
                k = 0
                for i in positions:
                    if i > last + 1:
                        last = i
                        k += 1
                total += k
            assert Fraction(total, choose(m, t)) == conditional_mean(m+1,t)

    print('TRANSITION_MATCHING_UNIVERSALITY_PASS direct_n<=10 words_n<=16 transfer_n<=90 means_m<=11')

if __name__ == '__main__':
    check()
