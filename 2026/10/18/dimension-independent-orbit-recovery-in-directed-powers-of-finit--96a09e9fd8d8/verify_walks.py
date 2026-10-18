#!/usr/bin/env python3
"""Independent exact-walk-polynomial test of orbit separation for uniform chain products."""
from itertools import combinations_with_replacement
from collections import defaultdict
from math import comb, factorial


def truncated_egf(levels, r):
    count = [1] + [0] * r
    for v in levels:
        nxt = [0] * (r + 1)
        for t in range(r + 1):
            nxt[t] = sum(comb(t,j) * count[t-j] for j in range(min(t,v)+1))
        count = nxt
    return tuple(count)


def test(m, d):
    seen = {}
    r = (m + 1) // 2
    for x in combinations_with_replacement(range(m + 1), d):
        down = truncated_egf(x, r)
        up = truncated_egf(tuple(m - t for t in x), r)
        key = (down, up)
        assert key not in seen, (m, d, x, seen.get(key))
        seen[key] = x
    assert len(seen) == comb(m+d, d)
    return len(seen)


def main():
    cases = profiles = 0
    for m in range(1, 15):
        for d in range(1, 9):
            if comb(m+d, d)>5000:
                continue
            profiles += test(m,d)
            cases += 1
    for m in range(1, 30):
        r = (m + 1) // 2
        if r > 1:
            prev = {}
            for x in range(m + 1):
                key = (truncated_egf((x,),r-1),
                       truncated_egf((m-x,),r-1))
                prev.setdefault(key, []).append(x)
            assert any(len(v)>1 for v in prev.values()), (m,r)
        else:
            assert m<=2
    print('WALK_POLYNOMIAL_INJECTIVITY_PASS', 'configurations', cases,
          'profiles_tested', profiles, 'single_chain_sharpness_m_up_to',29)


if __name__ == '__main__':
    main()
