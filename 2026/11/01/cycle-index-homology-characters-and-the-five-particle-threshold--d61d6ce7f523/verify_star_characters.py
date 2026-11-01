"""Reproduce finite arm-permutation Euler/Lefschetz checks for star configuration spaces.

Requires only Python 3.10+; exact integer arithmetic, no external packages.
This corroborates finite instances, not a proof of the uniform theorem.
"""
from itertools import combinations, permutations
from math import factorial, comb
from functools import lru_cache
from collections import Counter


def cycle_lengths(p):
    seen = set()
    result = []
    for a in range(len(p)):
        if a in seen:
            continue
        b = a
        ell = 0
        while b not in seen:
            seen.add(b)
            ell += 1
            b = p[b]
        result.append(ell)
    return result


def proposed_euler_trace(m, n, p):
    lengths = cycle_lengths(p)
    c1 = lengths.count(1)
    series = [1] + [0] * n
    for ell in lengths:
        # Each cycle supplies one geometric factor (1-t^ell)^(-1).
        for j in range(ell, n + 1):
            series[j] += series[j - ell]
    return series[n] + (1-c1) * series[n - 1]


def cubical_cells(m, n):
    # Subdivide each star arm into n edges; canonical Abrams model.
    choices = [('v', -1, 0)]
    choices += [('v', a, j) for a in range(m) for j in range(1, n + 1)]
    choices += [('e', a, j) for a in range(m) for j in range(1, n + 1)]
    supports = {('v', -1, 0): 1}
    for a in range(m):
        for j in range(1, n + 1):
            tip = 1 + a * n + j - 1
            supports[('v', a, j)] = 1 << tip
            other = 0 if j == 1 else tip - 1
            supports[('e', a, j)] = (1 << tip) | (1 << other)
    cells = []
    for items in combinations(choices, n):
        used = 0
        for item in items:
            footprint = supports[item]
            if used & footprint:
                break
            used |= footprint
        else:
            cells.append(items)
    return cells


def signed_fixed_cell_euler(cells, p):
    total = 0
    for C in cells:
        Cset = set(C)
        moved = {(typ, p[a] if a >= 0 else -1, j) for typ, a, j in C}
        if moved != Cset:
            continue
        edges = sorted(item for item in C if item[0] == 'e')
        transported = [('e', p[a], j) for _, a, j in edges]
        perm = [edges.index(item) for item in transported]
        inversion = sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i+1, len(perm)))
        total += (-1)**(len(edges) + inversion)
    return total


@lru_cache(None)
def bounded_partitions(m, n):
    if n == 0:
        return 1
    if n < 0 or m == 0:
        return 0
    return bounded_partitions(m-1, n) + bounded_partitions(m, n-m)


def trivial_multiplicity(m, n):
    return 1-bounded_partitions(m,n)-bounded_partitions(m,n-1) + sum(bounded_partitions(m-1,j) for j in range(n))


def main():
    configs = [(3,3), (3,4), (4,3), (4,4), (3,5)]
    checks = 0
    for m, n in configs:
        cubical = cubical_cells(m, n)
        seen = set()
        for p in permutations(range(m)):
            direct = signed_fixed_cell_euler(cubical, p)
            formula = proposed_euler_trace(m, n, p)
            if direct != formula:
                raise AssertionError((m, n, p, direct, formula))
            checks += 1
            seen.add(tuple(sorted(cycle_lengths(p))))
        ident = tuple(range(m))
        expected_b1 = 1-comb(n+m-1,m-1)+(m-1)*comb(n+m-2,m-1)
        assert proposed_euler_trace(m, n, ident) == 1-expected_b1
        print(f'm={m} n={n} cells={len(cubical)} permutations={factorial(m)} conjugacy_classes={len(seen)} b1={expected_b1}')
    for m in range(3, 7):
        group = list(permutations(range(m)))
        for n in range(1, 8):
            averaged = sum(1-proposed_euler_trace(m,n,p) for p in group)
            assert averaged % len(group) == 0, (m,n,averaged)
            assert averaged // len(group) == trivial_multiplicity(m,n), (m,n,averaged)
        print(f'm={m} Burnside_averages_verified_n1..7=7')
    for m in range(3, 9):
        values = [trivial_multiplicity(m,n) for n in range(1, 10)]
        assert values[:5] == [0,0,0,0,1], (m,values)
        print('m=',m,' invariant_multiplicities_n1..9=',','.join(map(str,values)),sep='')
    print(f'EXACT_SIGNED_CELL_CHECKS={checks}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
