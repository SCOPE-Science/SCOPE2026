#!/usr/bin/env python3
"""Standalone finite tests for the single-edit binary sum-channel theorem.
No external packages. Exhaustive small-parameter checks and an explicit length-eight code.
"""
from itertools import product, combinations

CODE8 = (0, 7, 25, 42, 63, 85, 90, 99, 109, 112,
         142, 147, 161, 182, 184, 194, 201, 220, 228, 251)


def d(x, y):
    return (x ^ y).bit_count()


def par(x):
    return x.bit_count() % 2


def type_l_sphere(x, ell, n):
    """All outputs after at most one row-level insertion/deletion/substitution.
    A mixed-length tuple is unambiguous because every row retains its index.
    Input x encodes ell data rows as n-bit binary integers.
    """
    rows = tuple(''.join(str((x[i*n+j] & 1)) for j in range(n))
                 for i in range(ell))
    parity = ''.join(str(sum(int(rows[i][j]) for i in range(ell)) % 2)
                     for j in range(n))
    output = rows + (parity,)
    s = {output}
    for r, row in enumerate(output):
        for j in range(n):
            w = list(output)
            w[r] = row[:j] + str(1 - int(row[j])) + row[j+1:]
            s.add(tuple(w))
            w = list(output)
            w[r] = row[:j] + row[j+1:]
            s.add(tuple(w))
        for j in range(n+1):
            for b in '01':
                w = list(output)
                w[r] = row[:j] + b + row[j:]
                s.add(tuple(w))
    return s


def col_int(bits, ell, n, col):
    return sum(bits[r*n + col] << r for r in range(ell))


def conflicts(x, y, ell, n):
    delta = [d(col_int(x, ell, n, k), col_int(y, ell, n, k))
             for k in range(n)]
    return sum(t != 0 for t in delta) == 1 and any(t in (1, 2) for t in delta)


def max_classical(ell):
    """Exact branch-and-bound maximum independent set on the Hamming<=2 graph."""
    size = 1 << ell
    neighbors = [sum(1 << j for j in range(size) if d(i, j) >= 3)
                 for i in range(size)]
    best = []
    def search(chosen, avail):
        nonlocal best
        if len(chosen) + avail.bit_count() <= len(best):
            return
        if avail == 0:
            if len(chosen) > len(best):
                best = chosen[:]
            return
        xbit = avail & -avail
        x = xbit.bit_length() - 1
        search(chosen + [x], avail & neighbors[x])
        search(chosen, avail ^ xbit)
    search([], (1 << size) - 1)
    return best


def rowpar_code(ell, n, classical):
    cset = set(classical)
    return [bits for bits in product((0, 1), repeat=ell*n)
            if sum((sum(bits[r*n:r*n+n]) % 2) << r
                   for r in range(ell)) in cset]


def check():
    assert len(CODE8) == 20 and len(set(CODE8)) == 20
    assert min(d(a, b) for a, b in combinations(CODE8, 2)) == 3
    print('A(8,3) witness: 20 binary words, minimum Hamming distance 3')
    print('A(8,3) optimality is literature-sourced, not computationally proved here')
    for ell in range(1, 5):
        classical = max_classical(ell)
        print('A_2({},3) = {} (complete branch-and-bound)'.format(ell, len(classical)))
        for n in (1, 2):
            inputs = list(product((0, 1), repeat=ell*n))
            spheres = [type_l_sphere(x, ell, n) for x in inputs]
            # Independently test exact confusability against the claimed
            # single-column radius-two adjacency rule.
            for i in range(len(inputs)):
                for j in range(i+1, len(inputs)):
                    actual = not spheres[i].isdisjoint(spheres[j])
                    expected = conflicts(inputs[i], inputs[j], ell, n)
                    assert actual == expected, (ell,n,i,j,actual,expected)
            optcode = rowpar_code(ell, n, classical)
            assert len(optcode) == len(classical) * (1 << (ell*(n-1)))
            assert len({parbits for parbits in optcode}) == len(optcode)
            sphere_by_word = {w:type_l_sphere(w, ell, n) for w in optcode}
            for a,b in combinations(optcode,2):
                assert sphere_by_word[a].isdisjoint(sphere_by_word[b])
            print('SID full-ball check: ell={} n={} matrices={} code={}'
                  .format(ell, n, len(inputs), len(optcode)))
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
