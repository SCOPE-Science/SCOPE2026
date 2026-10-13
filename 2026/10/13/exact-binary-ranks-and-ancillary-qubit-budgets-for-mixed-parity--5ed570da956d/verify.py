#!/usr/bin/env python3
"""Direct exact binary-rank checks for heterogeneous clique Cartesian products.
Only the Python standard library is required. Finite tests complement the general proof.
"""
from itertools import product
from math import prod


def predicted_nullity(sizes):
    ev = [q for q in sizes if q % 2 == 0]
    od = [q for q in sizes if q % 2 == 1]
    Q, H = prod(ev), prod(q-2 for q in ev)
    P, R = prod(od), prod(q-2 for q in od)
    numerator = (Q + H) * (P + ((-1)**len(sizes)) * R)
    assert numerator % 4 == 0, (sizes, numerator)
    return numerator // 4


def adjacency_rows(sizes):
    vertices = list(product(*(range(q) for q in sizes)))
    index = {v: i for i,v in enumerate(vertices)}
    rows = []
    for v in vertices:
        bits = 0
        for k,q in enumerate(sizes):
            for value in range(q):
                if value == v[k]:
                    continue
                dest = v[:k] + (value,) + v[k+1:]
                bits |= 1 << index[dest]
        rows.append(bits)
    return rows


def rank_mod_two(rows):
    basis = {}
    for original in rows:
        x = original
        while x:
            j = x.bit_length()-1
            if j in basis:
                x ^= basis[j]
            else:
                basis[j] = x
                break
    return len(basis)


def main():
    counts = {'all':0, 'mixed_parity':0, 'odd_only':0, 'even_only':0, 'max_N':0}
    examples = [((2,3), 2), ((2,3,5), 6), ((2,2,3), 2), ((3,4), 6)]
    for qs, expect in examples:
        assert predicted_nullity(qs) == expect, (qs, predicted_nullity(qs), expect)
    for d in range(1,6):
        for sizes in product(range(2,7), repeat=d):
            N = prod(sizes)
            if N > 350:
                continue
            nu = predicted_nullity(sizes)
            assert (N - nu) % 2 == 0
            rk = rank_mod_two(adjacency_rows(sizes))
            assert N-rk == nu, (sizes,N,rk,nu)
            counts['all'] += 1
            counts['max_N'] = max(counts['max_N'],N)
            if any(q%2==0 for q in sizes) and any(q%2==1 for q in sizes):
                counts['mixed_parity'] += 1
            elif all(q%2==0 for q in sizes):
                counts['even_only'] += 1
            else:
                counts['odd_only'] += 1
    print('VERIFY_OK', ' '.join(f'{k}={v}' for k,v in counts.items()))


if __name__ == '__main__':
    main()
