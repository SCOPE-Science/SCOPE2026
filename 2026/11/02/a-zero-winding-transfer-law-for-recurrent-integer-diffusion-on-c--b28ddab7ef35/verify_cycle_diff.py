#!/usr/bin/env python3
"""Finite replay for recurrent integer diffusion on labelled cycles.

No third-party dependencies. The algebraic argument in RESULT.md, not this
finite replay, supplies the theorem for all cycle lengths.
"""
from collections import defaultdict
from itertools import product

ALPHABET = (-1, 0, 1)
STATES = tuple(product(ALPHABET, repeat=2))
INDEX = {s: i for i, s in enumerate(STATES)}


def edges():
    ans = []
    for (a, b), i in INDEX.items():
        for c in ALPHABET:
            j = INDEX[(b, c)]
            if b == 0:
                if a + c == 0:
                    ans.append((i, j, 0))
            else:
                bound = 1 - b * (a + c)
                for q in range(1, bound + 1):
                    ans.append((i, j, b * q))
    return ans


def transfer_count(n):
    ee = edges()
    ans = 0
    for start in range(9):
        dp = {(start, 0): 1}
        for _ in range(n):
            nxt = defaultdict(int)
            for (j, weight), multiplicity in dp.items():
                for a, b, d in ee:
                    if a == j:
                        nxt[(b, weight + d)] += multiplicity
            dp = nxt
        ans += dp.get((start, 0), 0)
    return ans


def diffusion(x):
    n = len(x)
    return tuple(x[i] + (x[(i-1) % n] > x[i]) - (x[(i-1) % n] < x[i])
                 + (x[(i+1) % n] > x[i]) - (x[(i+1) % n] < x[i])
                 for i in range(n))


def independent_direct_count(n):
    count = 0
    maxgap = 0
    examples = []
    for epart in product(range(-3, 4), repeat=n-1):
        elast = -sum(epart)
        if not -3 <= elast <= 3:
            continue
        e = epart + (elast,)
        x = [0]
        for d in epart:
            x.append(x[-1] + d)
        x = tuple(x)
        y = diffusion(x)
        if diffusion(y) == x:
            count += 1
            gap = max(map(abs, e))
            if gap > maxgap:
                maxgap = gap
                examples = [e]
    return count, maxgap, examples


def run():
    expected = {3: 19, 4: 47, 5: 171, 6: 517, 7: 1793, 8: 5927,
                9: 20287, 10: 69307, 11: 238283, 12: 823865}
    for n in range(3, 13):
        cnt = transfer_count(n)
        assert cnt == expected[n], (n, cnt, expected[n])
        assert cnt % 2 == 1
        if n <= 8:
            direct, gap, examples = independent_direct_count(n)
            assert direct == cnt, (n, direct, cnt)
            assert gap == (2 if n == 3 else 3)
            print(f"n={n}, transfer={cnt}, direct={direct}, primitive_orbits={(cnt-1)//2}, gap={gap}")
        else:
            print(f"n={n}, transfer={cnt}, primitive_orbits={(cnt-1)//2}")
    print("CYCLE_DIFFUSION_ALL_CHECKS_PASSED")


if __name__ == '__main__':
    run()

# Sharpness witnesses use the sign-gradient update, not only the transfer test.
def sharp_witness_checks():
    for n in range(4, 21):
        if n % 2 == 0:
            e = (-3, 3) + (-1, 1) * (n // 2 - 1)
        else:
            e = (-3, 1, 0, -1, 3) + (-1, 1) * ((n - 5) // 2)
        assert len(e) == n and sum(e) == 0
        x = [0]
        for v in e[:-1]:
            x.append(x[-1] + v)
        assert diffusion(diffusion(tuple(x))) == tuple(x)
        assert diffusion(tuple(x)) != tuple(x)
        assert max(map(abs, e)) == 3
    e = (-2, 0, 2)
    x = (0, -2, -2)
    assert diffusion(diffusion(x)) == x and diffusion(x) != x
    print('SHARP_GAP_WITNESSES_PASSED n=3..20')

sharp_witness_checks()
