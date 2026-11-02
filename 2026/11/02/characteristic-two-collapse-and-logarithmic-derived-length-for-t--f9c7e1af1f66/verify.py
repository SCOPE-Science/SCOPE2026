#!/usr/bin/env python3
"""Finite-prime-field verification of derivation derived-series formulas.

Standard library only. Derivations are found by solving differentiated
presentation relations, without assuming their predicted coordinate form.
"""

def rref(rows, prime, cols):
    mat = [[int(v) % prime for v in row] for row in rows]
    rank, pivots = 0, []
    for col in range(cols):
        pivot = next((j for j in range(rank, len(mat)) if mat[j][col]), None)
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        scalar = pow(mat[rank][col], -1, prime)
        mat[rank] = [(z * scalar) % prime for z in mat[rank]]
        for j in range(len(mat)):
            if j != rank and mat[j][col]:
                factor = mat[j][col]
                mat[j] = [(a - factor * b) % prime for a, b in zip(mat[j], mat[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(mat):
            break
    return mat[:rank], pivots

def nullspace(rows, prime, cols):
    mat, pivots = rref(rows, prime, cols)
    ans = []
    for free in range(cols):
        if free in pivots:
            continue
        vec = [0] * cols
        vec[free] = 1
        for i, col in enumerate(pivots):
            vec[col] = (-mat[i][free]) % prime
        ans.append(vec)
    return ans

def check(lengths, prime):
    m = len(lengths)
    assert m >= 2 and min(lengths) >= 3
    monomials = [(-1, 0)] + [(i, power) for i, length in enumerate(lengths)
                                 for power in range(1, length)]
    n = len(monomials)
    index = {u: k for k, u in enumerate(monomials)}
    def multiply_indices(a, b):
        i, v = monomials[a]
        j, w = monomials[b]
        if i == -1: return b
        if j == -1: return a
        if i != j or v + w >= lengths[i]: return None
        return index[i, v + w]
    product = [[multiply_indices(i,j) for j in range(n)] for i in range(n)]
    def times(u, v):
        out = [0] * n
        for i, a in enumerate(u):
            if not a: continue
            for j, b in enumerate(v):
                if not b or product[i][j] is None: continue
                at = product[i][j]
                out[at] = (out[at] + a*b) % prime
        return out
    standard = [[int(i == j) for i in range(n)] for j in range(n)]
    x_indices = [index[i, 1] for i in range(m)]
    # A derivation is determined by the unknown vectors D(x_i).
    # Solve all differentiated defining relations with no assumed form.
    equations = []
    for i in range(m):
        for j in range(i+1, m):
            for out_idx in range(n):
                row = [0] * (m*n)
                for h in range(n):
                    z = product[h][x_indices[j]]
                    if z == out_idx: row[i*n+h] += 1
                    z = product[x_indices[i]][h]
                    if z == out_idx: row[j*n+h] += 1
                equations.append(row)
    for i, length in enumerate(lengths):
        h0 = index[i, length-1]
        for out_idx in range(n):
            row = [0] * (m*n)
            for h in range(n):
                if product[h0][h] == out_idx:
                    row[i*n+h] += length
            equations.append(row)
    generators = nullspace(equations, prime, m*n)
    expected = sum(length - 1 for length in lengths) + m*(m-1)
    assert len(generators) == expected, (lengths, prime, 'dimension')
    matrices = []
    for vector in generators:
        images = [vector[i*n:(i+1)*n] for i in range(m)]
        M = [[0]*n for _ in range(n)]
        for col, (i, power) in enumerate(monomials):
            if i == -1: continue
            source = 0 if power == 1 else index[i, power-1]
            img = times(standard[source], images[i])
            for row in range(n):
                M[row][col] = power * img[row] % prime
        for a in range(n):
            for b in range(n):
                lhs = [0]*n if product[a][b] is None else [M[row][product[a][b]] for row in range(n)]
                ua = [M[row][a] for row in range(n)]
                ub = [M[row][b] for row in range(n)]
                xa, xb = times(ua,standard[b]),times(standard[a],ub)
                assert lhs == [(u+v)%prime for u,v in zip(xa,xb)]
        matrices.append(M)
    def bracket(A,B):
        return [[sum(A[i][h]*B[h][j]-B[i][h]*A[h][j] for h in range(n)) % prime
                 for j in range(n)] for i in range(n)]
    dims = [len(matrices)]
    current = matrices
    while current:
        brackets = [sum(bracket(A,B),[]) for k,A in enumerate(current) for B in current[k+1:]]
        if not brackets:
            dims.append(0)
            break
        indep, pivots = rref(brackets, prime, n*n)
        dims.append(len(indep))
        current = [[row[h*n:(h+1)*n] for h in range(n)] for row in indep]
    if prime == 2:
        target = [expected, m*(m-1) + sum((length-1)//2 for length in lengths),0]
    else:
        target = [expected, m*(m-1) + sum(length-2 for length in lengths)]
        power = 4
        while True:
            next_dim = sum(max(0,length-power) for length in lengths)
            target.append(next_dim)
            if next_dim == 0: break
            power *= 2
    assert dims == target, (lengths,prime,dims,target)
    print('CHECK_OK',lengths,prime,tuple(dims))

if __name__ == '__main__':
    for p in (2,3,5):
        for lengths in ((3,5),(4,7),(3,9),(3,4,6)):
            check(lengths,p)
    print('VERIFY_OK')
