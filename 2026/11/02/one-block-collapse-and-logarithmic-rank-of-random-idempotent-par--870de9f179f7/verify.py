#!/usr/bin/env python3
"""Independent checks of the collapse law for idempotent partition-preserving maps.

Usage: python verify.py
Standard-library only. The finite check enumerates maps as arrays, not via the
factorization used in the formula.
"""
from itertools import product
from collections import Counter
from math import comb, log, exp, lgamma


def h(c, m):
    return sum(comb(m, k) * k ** (c * m - k) for k in range(1, m + 1))


def predicted(r, m):
    counts = Counter()
    for ch in product(range(r), repeat=r):
        if any(ch[ch[i]] != ch[i] for i in range(r)):
            continue
        basins = Counter(ch)
        roots = tuple(j for j in range(r) if ch[j] == j)
        count = 1
        for j in roots:
            count *= h(basins[j], m)
        counts[len(roots)] += count
    return counts


def independent_bruteforce(r, m):
    n = r * m
    counts = Counter()
    rank_counts = Counter()
    for ch in product(range(r), repeat=r):
        # For each character, map each point in block i into block ch[i].
        target_lists = [range(ch[i] * m, (ch[i]+1) * m) for i in range(r)]
        for blockmaps in product(*(product(t, repeat=m) for t in target_lists)):
            f = sum((tuple(t) for t in blockmaps), ())
            if all(f[f[x]] == f[x] for x in range(n)):
                roots = sum(ch[i] == i for i in range(r))
                counts[roots] += 1
                rank_counts[(roots, len(set(f)))] += 1
    return counts, rank_counts


def rank_formula_constant(r, m, k):
    return r * comb(m, k) * k**(r*m-k)


def main():
    cases = ((1,1),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2))
    for r,m in cases:
        predicted_by_roots = predicted(r,m)
        brute, ranks = independent_bruteforce(r,m)
        assert predicted_by_roots == brute, (r,m,predicted_by_roots,brute)
        for k in range(1,m+1):
            assert ranks[(1,k)] == rank_formula_constant(r,m,k), (r,m,k)
        assert sum(brute.values()) == sum(predicted_by_roots.values())
        if r == 2:
            assert predicted_by_roots[1] == 2*h(2,m)
            assert predicted_by_roots[2] == h(1,m)**2
        print(f'BRUTE_OK blocks={r} block_size={m} count={sum(brute.values())} rank_one_character={brute[1]}')
    # Check that all top idempotent characters agree with the multinomial formula.
    for r in range(2, 7):
        for m in range(1, 6):
            got = predicted(r,m)
            assert got[1] == r*h(r,m)
            assert sum(got.values()) >= got[1]
    print('EXACT_CHARACTER_FORMULA_OK')

    # Verify the logarithmic large-deviation trend and dominant rank using
    # stable log-sum-exp arithmetic; this is a numerical sanity check, not proof.
    def log_h(c,m):
        logs = [lgamma(m+1)-lgamma(k+1)-lgamma(m-k+1)
                +(c*m-k)*log(k) for k in range(1,m+1)]
        maxi = max(logs)
        return maxi + log(sum(exp(z-maxi) for z in logs)), 1+max(range(m), key=logs.__getitem__)
    for r in (2,3,4):
        for m in (250,1000,5000):
            a, mode = log_h(r,m)
            b, _ = log_h(r-1,m)
            c, _ = log_h(1,m)
            assert mode > 0 and mode <= m
            # Finite-m rate need not already equal limiting rate.
            print(f'ASYMPTOTIC_SANITY r={r} m={m} '+
                  f'scaled_mode={mode*log(m)/m:.7f} '+
                  f'log_two_root_to_one_root_per_m={(b+c-a)/m:.7f}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
