"""Brute-force enumeration cross-checks for commuting idempotent set maps.

No external packages.  Computes the root-fibre formula and directly
enumerates both total functions for n<=5, comparing their full rank profiles.
"""
from collections import defaultdict
from itertools import product
from math import comb, factorial


def rooted_profile(m):
    result = defaultdict(int)
    for p in range(m):
        for q in range(m - p):
            r = m - 1 - p - q
            multinomial = factorial(m - 1) // (factorial(p) * factorial(q) * factorial(r))
            result[(1, p + 1, q + 1)] += m * multinomial * ((p + 1) * (q + 1)) ** r
    return dict(result)


def rank_profiles(N):
    rooted = [None] + [rooted_profile(m) for m in range(1, N + 1)]
    total = [{(0, 0, 0): 1}]
    for n in range(1, N + 1):
        current = defaultdict(int)
        for m in range(1, n + 1):
            ways = comb(n - 1, m - 1)
            for (ct, fa, gb), s in rooted[m].items():
                for (oldct, oldfa, oldgb), v in total[n - m].items():
                    current[(ct + oldct, fa + oldfa, gb + oldgb)] += ways * s * v
        total.append(dict(current))
    return total


def brute_profile(n):
    idem = [f for f in product(range(n), repeat=n) if all(f[f[i]] == f[i] for i in range(n))]
    out = defaultdict(int)
    for f in idem:
        af = sum(f[i] == i for i in range(n))
        for g in idem:
            if not all(f[g[i]] == g[f[i]] for i in range(n)):
                continue
            bg = sum(g[i] == i for i in range(n))
            t = sum(f[i] == i and g[i] == i for i in range(n))
            out[(t, af, bg)] += 1
    return dict(out)


def main():
    N = 10
    profiles = rank_profiles(N)
    total = [sum(d.values()) for d in profiles]
    expected = [1, 1, 7, 58, 601, 7616, 113989, 1963060, 38178193, 826879312, 19727279461]
    assert total == expected, (total, expected)
    for n in range(1, 6):
        brute = brute_profile(n)
        assert brute == profiles[n], (n, brute, profiles[n])
        assert all(t <= a and t <= b for t, a, b in profiles[n])
        print(f"n={n}: {len(profiles[n])} rank classes; total={total[n]}, verified")
    print("FULL_PROFILE_CHECK_OK")
    print("counts n=0..10:", total)


if __name__ == '__main__':
    main()
