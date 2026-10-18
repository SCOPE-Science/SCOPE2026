#!/usr/bin/env python3
"""Recompute integral cellular homology of unordered triples on bouquets.

Self-contained finite exact check. Each nonnegative weak composition encodes
an unordered configuration's occupied oriented loop interiors, with or
without the central wedge vertex. Differential formed by signed endpoint
incidence (interior collisions are collapsed).
"""
from itertools import combinations, product
from math import comb


def weak_compositions(total, slots):
    if slots == 0:
        return [()] if total == 0 else []
    if slots == 1:
        return [(total,)]
    return [(first,) + rest for first in range(total+1)
            for rest in weak_compositions(total-first, slots-1)]


def cell_complex(beta, particles):
    top = weak_compositions(particles, beta)
    lower = weak_compositions(particles-1, beta)
    bottom_index = {m: k for k,m in enumerate(lower)}
    matrix = [[0]*len(top) for _ in lower]
    # Build incidence contributions from physical oriented boundary facets.
    for k, m in enumerate(top):
        pos = 0
        for i, count in enumerate(m):
            if count:
                target = m[:i] + (count-1,) + m[i+1:]
                row = bottom_index[target]
                # Last coordinate tends to the right-hand circle endpoint (plus);
                # first coordinate tends to the left-hand endpoint (minus).
                matrix[row][k] += (-1)**(pos + count - 1) - (-1)**pos
            pos += count
    return top, lower, matrix


def alternate_incidence(beta, particles):
    # Independent oriented labels following the deletion formula for a rose:
    # remove first label with sign +, last label with sign -;
    # when the missing label is j, the vertex cell has signed orientation
    # (-1)^(j-1) relative to the ordered remaining particle coordinates.
    top = weak_compositions(particles, beta)
    bottom = weak_compositions(particles-1, beta)
    index = {m:k for k,m in enumerate(bottom)}
    mat = [[0]*len(top) for _ in bottom]
    for col, m in enumerate(top):
        blocks = []
        next_label = 1
        for count in m:
            blocks.append(tuple(range(next_label, next_label+count)))
            next_label += count
        for i, block in enumerate(blocks):
            if not block:
                continue
            to = list(m)
            to[i] -= 1
            row = index[tuple(to)]
            mat[row][col] += (-1)**(block[0]-1)
            mat[row][col] -= (-1)**(block[-1]-1)
    return mat


def integral_diagonal_form(matrix):
    """Check and reduce this matrix to a diagonal by integer column moves.

    For 3 particles every nonzero column has exactly one nonzero entry
    of absolute value 2. This routine verifies that property from computed
    raw cells, does not assume it when building incidence coefficients.
    """
    if not matrix:
        return [], 0
    nr = len(matrix)
    nc = len(matrix[0])
    cols = [[matrix[r][c] for r in range(nr)] for c in range(nc)]
    row_representative = {}
    for c, vec in enumerate(cols):
        nz = [(i,x) for i,x in enumerate(vec) if x]
        assert len(nz) <= 1, ('non-diagonal column', c,nz)
        if not nz:
            continue
        i, x = nz[0]
        assert abs(x) == 2, ('unexpected divisor', i,c,x)
        if i not in row_representative:
            row_representative[i] = c
        else:
            rep = row_representative[i]
            q, rem = divmod(x, cols[rep][i])
            assert rem == 0
            cols[c] = [vec[r] - q*cols[rep][r] for r in range(nr)]
            assert not any(cols[c]), ('nonzero remainder', c)
    # These exact integer unimodular column operations yield diagonal 2's.
    for row, rep in row_representative.items():
        assert abs(cols[rep][row]) == 2
    for c in range(nc):
        if c not in row_representative.values():
            assert not any(cols[c])
    return [2]*len(row_representative), len(row_representative)


def rank_modp(matrix,p):
    a = [[x % p for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0]); r = 0
    for c in range(cols):
        pivot = next((i for i in range(r,rows) if a[i][c]),None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c],-1,p)
        for j in range(c,cols): a[r][j] = a[r][j]*inv%p
        for i in range(rows):
            if i != r and a[i][c]:
                k = a[i][c]
                for j in range(c,cols): a[i][j] = (a[i][j] - k*a[r][j]) % p
        r += 1
        if r == rows: break
    return r


def test():
    verified = 0
    for beta in range(1,16):
        tops, bottoms, d = cell_complex(beta,3)
        alt = alternate_incidence(beta,3)
        assert all(d[i][j] == -alt[i][j]
                   for i in range(len(bottoms)) for j in range(len(tops)))
        assert len(tops) == comb(beta+2,3)
        assert len(bottoms) == comb(beta+1,2)
        factors, rank = integral_diagonal_form(d)
        assert rank == comb(beta,2)
        assert rank_modp(d,3) == rank
        assert rank_modp(d,5) == rank
        assert rank_modp(d,7) == rank
        assert rank_modp(d,2) == 0
        free_H3 = len(tops) - rank
        free_H2 = len(bottoms) - rank
        tors_H2 = len(factors)
        assert free_H3 == beta*(beta*beta+5)//6
        assert free_H2 == beta
        assert tors_H2 == comb(beta,2)
        # Known independently: for two particles, Smith diagonal contains beta 2s.
        top2, lower2, d2 = cell_complex(beta,2)
        fact2, rank2 = integral_diagonal_form(d2)
        assert len(fact2) == beta and rank2 == beta
        assert len(top2) - rank2 == comb(beta,2)
        assert len(lower2) - rank2 == 0
        verified += 1
        print(f'b={beta:2d}: C3={len(tops):4d}, C2={len(bottoms):3d}, '
              f'Smith2={len(factors):2d}, BM3=Z^{free_H3}, '
              f'BM2=Z^{free_H2}+(Z/2)^{tors_H2}')
    assert cell_complex(0,3) == ([],[],[])
    print('VERIFIED_ROSE_MODELS:', verified, 'FOR PARTICLES 3 AND 2; TREE CASE = ZERO; ALL_CHECKS_OK')

if __name__=='__main__': test()
