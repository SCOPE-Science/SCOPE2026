#!/usr/bin/env python3
"""Exact finite chain verification for symmetric-group conjugacy quotients.

Only the Python standard library is required. The algorithm enumerates all
integer partitions, hence all conjugacy classes, in each requested symmetric
group. All arithmetic is exact.
"""
from functools import lru_cache

@lru_cache(None)
def partitions(total, bound=None):
    """Partitions in decreasing order, including ones (fixed points)."""
    if bound is None:
        bound = total
    if total == 0:
        return ((),)
    return tuple((k,) + rest
                 for k in range(min(bound, total), 0, -1)
                 for rest in partitions(total - k, k))

@lru_cache(None)
def prime_divisors(value):
    found = []
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            found.append(factor)
            while value % factor == 0:
                value //= factor
        factor += 1
    if value > 1:
        found.append(value)
    return tuple(found)

def support_primes(partition):
    return tuple(sorted({p for length in partition
                         for p in prime_divisors(length)}))

def remove_p_component(partition, p):
    """Cycle type of the p'-part; each L-cycle gives p^v cycles of L/p^v."""
    result = []
    for original in partition:
        remaining = original
        multiplicity = 1
        while remaining % p == 0:
            remaining //= p
            multiplicity *= p
        result.extend([remaining] * multiplicity)
    return tuple(sorted(result, reverse=True))

def chain_bases(n):
    by_dimension = {0: [], 1: [], 2: [], 3: []}
    for part in partitions(n):
        count = len(support_primes(part))
        if count:
            assert count <= 4
            by_dimension[count - 1].append(part)
    return by_dimension

def boundary_matrix(bases, dim):
    columns = bases[dim]
    index = {part: row for row, part in enumerate(bases[dim - 1])}
    a = [[0] * len(columns) for _ in range(len(index))]
    for col, part in enumerate(columns):
        for sign_index, p in enumerate(support_primes(part)):
            face = remove_p_component(part, p)
            assert sum(face) == sum(part)
            assert len(support_primes(face)) == dim
            a[index[face]][col] += (-1) ** sign_index
    return a

def rank_mod(a, prime):
    rows = len(a)
    cols = len(a[0]) if rows else 0
    b = [[x % prime for x in row] for row in a]
    pivot_rows = []
    row = 0
    for col in range(cols):
        pivot = next((i for i in range(row, rows) if b[i][col]), None)
        if pivot is None:
            continue
        b[row], b[pivot] = b[pivot], b[row]
        pivot_rows.append((row, col))
        inv = pow(b[row][col], -1, prime)
        b[row] = [(x * inv) % prime for x in b[row]]
        for i in range(row + 1, rows):
            coeff = b[i][col]
            if coeff:
                b[i] = [(x - coeff * y) % prime
                        for x, y in zip(b[i], b[row])]
        row += 1
        if row == rows:
            break
    return row, pivot_rows

def free_edge_peeling(a, triangle_count):
    """Eliminate triangles forced to have coefficient zero in any 2-cycle."""
    remaining = set(range(triangle_count))
    batches = []
    while remaining:
        exposed = set()
        for row in a:
            incident = [j for j in remaining if row[j] != 0]
            if len(incident) == 1:
                exposed.add(incident[0])
        if not exposed:
            break
        remaining.difference_update(exposed)
        batches.append(len(exposed))
    return batches, remaining

def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]

def verify():
    print('Exact conjugacy-orbit chain-complex check, n=1,...,15')
    print('n : (C0,C1,C2,C3) : rank(d2 mod 101) : rank(d2 mod 103)')
    for n in range(1, 16):
        bases = chain_bases(n)
        d2 = boundary_matrix(bases, 2)
        # For small n with no 1-cells there are no 2-cells either.
        r101, pivots101 = rank_mod(d2, 101)
        r103, pivots103 = rank_mod(d2, 103)
        d1 = boundary_matrix(bases, 1) if bases[1] else [[0] * 0 for _ in bases[0]]
        for j in range(len(bases[2])):
            col = [d2[i][j] for i in range(len(d2))]
            assert all(x == 0 for x in matvec(d1, col))
        dims = tuple(len(bases[k]) for k in (0, 1, 2, 3))
        peel_batches, survivors = free_edge_peeling(d2, len(bases[2]))
        print(f'{n:2d} : {dims} : {r101} : {r103} : peel={peel_batches} : residual={len(survivors)}')
        if n < 15:
            assert r101 == len(bases[2]), (n, r101, len(bases[2]))
            assert len(survivors) == 0
        else:
            assert dims == (40, 111, 24, 0)
            assert len(survivors) == 4
            assert {bases[2][i] for i in survivors} == {
                (5,3,2,1,1,1,1,1), (7,3,2,1,1,1),
                (7,5,2,1), (7,5,3)}
            assert r101 == 23 and r103 == 23
            cells = [
                (5, 3, 2, 1, 1, 1, 1, 1),
                (7, 3, 2, 1, 1, 1),
                (7, 5, 2, 1),
                (7, 5, 3),
            ]
            coefficients = [1, -1, 1, -1]
            cycle = [0] * len(bases[2])
            for part, coefficient in zip(cells, coefficients):
                cycle[bases[2].index(part)] = coefficient
            assert matvec(d2, cycle) == [0] * len(d2)
            print('n=15: primitive four-triangle cycle boundary = 0')
            print('n=15: nonzero entries =', [
                (cells[i], coefficients[i]) for i in range(4)])
            print('n=15: the 23 pivot columns are', [i for _, i in pivots101])
    print('PASS: integral H_2=0 for 1<=n<=14, H_2=Z for n=15.')

if __name__ == '__main__':
    verify()
