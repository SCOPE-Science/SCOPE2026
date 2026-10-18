"""Exact finite checks for monic triple-product collisions (no dependencies)."""
from collections import Counter
from itertools import product
from math import comb


def count_matrices(rows, cols):
    assert sum(rows) == sum(cols)
    count = 0
    for a in range(min(rows[0], cols[0]) + 1):
        for b in range(min(rows[0] - a, cols[1]) + 1):
            c = rows[0] - a - b
            if c > cols[2]:
                continue
            for u in range(min(rows[1], cols[0] - a) + 1):
                for v in range(min(rows[1] - u, cols[1] - b) + 1):
                    w = rows[1] - u - v
                    i, j, k = cols[0] - a - u, cols[1] - b - v, cols[2] - c - w
                    if i >= 0 and j >= 0 and k >= 0 and i + j + k == rows[2]:
                        count += 1
    return count


def pol_mul(a, b, p):
    res = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            res[i + j] = (res[i + j] + v*w) % p
    return tuple(res)


def direct_count(p, d):
    fs = [v + (1,) for v in product(range(p), repeat=d)]
    pairs = [pol_mul(a, b, p) for a in fs for b in fs]
    freq = Counter()
    for ab in pairs:
        for c in fs:
            freq[pol_mul(ab, c, p)] += 1
    return sum(z*z for z in freq.values())


def main():
    for d in range(1, 11):
        M = count_matrices((d,)*3, (d,)*3)
        N = count_matrices((d,d-1,d-1), (d,d-1,d-1))
        expected_M = (d+1)*(d+2)*(d*d+3*d+4)//8
        expected_N = d*(d+1)*(d+2)*(3*d+1)//24
        assert M == expected_M and N == expected_N, (d,M,N)
        assert 9*N == 3*d*(d+1)*(d+2)*(3*d+1)//8
    print('PASS: ten exact 3-by-3 contingency counts, both formulas.')
    rows = [(2,1),(3,1),(5,1),(7,1),(11,1),
            (2,2),(3,2),(5,2),(7,2),(2,3),(3,3),(2,4)]
    for p,d in rows:
        value = direct_count(p,d)
        M = (d+1)*(d+2)*(d*d+3*d+4)//8
        N = d*(d+1)*(d+2)*(3*d+1)//24
        A,B = M,-9*N
        remainder = value - (A*p**(3*d) + B*p**(3*d-1))
        if d==1:
            assert value == 6*p**3-9*p**2+4*p, (p,value)
        assert value>0
        print(f'p={p}, d={d}, exact={value}, main={A*p**(3*d)}, '
              f'correction={B*p**(3*d-1)}, residual={remainder}')
    print('PASS: all direct collisions; for d=1 the full cubic polynomial agrees.')
    print('NOTE: finite checks are not a proof of all-q asymptotics.')


if __name__ == '__main__':
    main()
