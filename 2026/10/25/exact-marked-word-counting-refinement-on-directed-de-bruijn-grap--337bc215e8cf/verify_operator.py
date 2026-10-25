#!/usr/bin/env python3
"""Independent adjacency-operator checks of coordinate recovery identities."""
from itertools import product


def verify(q, length, root):
    words = tuple(product(range(q), repeat=length))
    index = {w: i for i, w in enumerate(words)}
    out = [tuple(index[w[1:] + (a,)] for a in range(q)) for w in words]
    inc = [[] for _ in words]
    for i, targets in enumerate(out):
        for j in targets:
            inc[j].append(i)

    def A(v):
        return [sum(v[j] for j in targets) for targets in out]

    def T(v):
        return [sum(v[j] for j in targets) for targets in inc]

    point = [int(w == root) for w in words]
    for i in range(length):
        v = point[:]
        for _ in range(i):
            v = T(v)
        for _ in range(length - 1):
            v = A(v)
        for j in range(length):
            u = v[:]
            for _ in range(length - 1 - j):
                u = T(u)
            factor = q ** (i + length - 1 - j)
            want = [factor * int(w[j] == root[i]) for w in words]
            assert u == want, (q, length, root, i, j)


def main():
    configurations = 0
    identities = 0
    for q in range(1, 5):
        for length in range(1, 6):
            if q ** length > 128:
                continue
            for root in product(range(q), repeat=length):
                verify(q, length, root)
                configurations += 1
                identities += length ** 2
            print(f'q={q}, length={length}, roots={q ** length}, identities_per_root={length ** 2}: PASS')
    print(f'TOTAL configurations={configurations}, verified_coordinate_identities={identities}')
    print('VERIFY_OPERATORS_OK')


if __name__ == '__main__':
    main()
