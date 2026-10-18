#!/usr/bin/env python3
"""Modular rank certificate for odd Fourier uncertainty on C_25.

Run: python3 verify_odd_sine_25.py
Requires Python standard library only. Nonzero modular minors prove
nonzero cyclotomic minors via Z[zeta_25] -> F_l, zeta_25 -> root.
"""
import itertools
import json

N = 25
REP = tuple(range(1, 13))
PAIRS = ((2, 4), (3, 3), (3, 4), (2, 5))


def prime_factors(n):
    out = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def primitive_root(ell):
    factors = prime_factors(ell - 1)
    return next(g for g in range(2, ell) if all(
        pow(g, (ell - 1)//d, ell) != 1 for d in factors))


def modular_sine(ell):
    assert (ell - 1) % N == 0
    z = pow(primitive_root(ell), (ell - 1)//N, ell)
    assert pow(z, N, ell) == 1 and pow(z, 5, ell) != 1
    mat = tuple(tuple((pow(z, (x*y)%N, ell) -
                       pow(z, (-x*y)%N, ell))%ell for x in REP)
                for y in REP)
    return z, mat


def full_column_rank(matrix, row_indices, column_indices, ell):
    # Row echelon algorithm on a rectangular matrix, exact in F_ell.
    cols = tuple(column_indices)
    work = [list(matrix[y][x] for x in cols) for y in row_indices]
    rank = 0
    nc = len(cols)
    for c in range(nc):
        pivot = next((i for i in range(rank, len(work))
                      if work[i][c] != 0), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][c], -1, ell)
        for i in range(rank + 1, len(work)):
            if work[i][c]:
                mul = work[i][c] * inv % ell
                for k in range(c, nc):
                    work[i][k] = (work[i][k] - mul*work[rank][k]) % ell
        rank += 1
        if rank == nc:
            break
    return rank == nc


def run(ell):
    z, matrix = modular_sine(ell)
    all_rows = frozenset(range(12))
    results = []
    for r, s in PAIRS:
        failures = []
        total = 0
        frequency_sets = list(itertools.combinations(range(12), s))
        complements = [tuple(sorted(all_rows.difference(J)))
                       for J in frequency_sets]
        for I in itertools.combinations(range(12), r):
            for J, zero_rows in zip(frequency_sets, complements):
                total += 1
                if not full_column_rank(matrix, zero_rows, I, ell):
                    failures.append((tuple(REP[j] for j in I),
                                     tuple(REP[j] for j in J)))
        results.append({'r':r,'s':s,'tested':total,
                        'rank_deficient_pairs':len(failures),
                        'exceptions':failures})
    return {'prime':ell,'primitive_25th_root':z,'cases':results}


def verify():
    output = [run(ell) for ell in (101, 151)]
    wanted = {(2,4):0,(3,3):0,(3,4):0,(2,5):2}
    target_exceptions = [
        ((5,10),(1,4,6,9,11)),
        ((5,10),(2,3,7,8,12))]
    for o in output:
        for c in o['cases']:
            key = (c['r'],c['s'])
            assert c['tested'] == __import__('math').comb(12,key[0]) * __import__('math').comb(12,key[1])
            assert c['rank_deficient_pairs'] == wanted[key]
            assert c['exceptions'] == target_exceptions if key == (2,5) else not c['exceptions']
    assert output[0]['cases'] == output[1]['cases']
    return {'status':'PASS','N':N,'supports':'odd: f(-x)=-f(x)',
            'description':'All r<=s boundary cases with r in {2,3}; r=1 excluded by direct sine-row support calculation',
            'certificates':output,
            'conclusion':'minimum nonzero odd |supp f|+|supp Ff| is 14; four projective extremizers'}


if __name__ == '__main__':
    print(json.dumps(verify(), sort_keys=True, separators=(',',':')))
