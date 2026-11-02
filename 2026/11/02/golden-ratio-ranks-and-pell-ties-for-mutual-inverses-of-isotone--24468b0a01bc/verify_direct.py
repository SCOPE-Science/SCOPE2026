#!/usr/bin/env python3
"""Direct semigroup multiplication verification of the rank-stratified inverse-pair law."""
from itertools import combinations_with_replacement
from math import comb


def compose(f, g):
    return tuple(f[g[i]] for i in range(len(f)))


def direct_counts(n):
    maps = list(combinations_with_replacement(range(n), n))
    ans = [0] * (n + 1)
    for f in maps:
        r = len(set(f))
        for g in maps:
            if len(set(g)) != r:
                continue
            if compose(compose(f, g), f) == f and compose(compose(g, f), g) == g:
                ans[r] += 1
    return ans[1:]


def compositions(n, r):
    if r == 1:
        yield (n,)
    else:
        for a in range(1, n-r+2):
            for sub in compositions(n-a, r-1):
                yield (a,) + sub


def incidence_count(n, r):
    ans = 0
    for sizes in compositions(n, r):
        weight = 1
        for a in sizes:
            weight *= a
        ans += weight
    return ans


def main():
    for n in range(1, 7):
        obs = direct_counts(n)
        expected = [comb(n+r-1, 2*r-1)**2 for r in range(1, n+1)]
        assert obs == expected, (n, obs, expected)
        incidence = [incidence_count(n, r) for r in range(1, n+1)]
        assert [a*a for a in incidence] == obs
        print(f'n={n} inverse_pair_ranks={obs} total={sum(obs)}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
