"""Finite reproducibility checks for distance-two-shell dephasing on hypercubes.

The exact infinite-family argument is in RESULT.md; these checks test its
finite Fourier ranks, radial eigenmodes, and finite Lindblad semigroups.
"""
from itertools import combinations
from math import comb, isqrt, cos


def rank_mod(matrix, modulus=1000003):
    a = [[z % modulus for z in row] for row in matrix]
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, modulus)
        a[row][col:] = [(x * inv) % modulus for x in a[row][col:]]
        for i in range(row + 1, len(a)):
            if a[i][col]:
                f = a[i][col]
                a[i][col:] = [(a[i][j] - f * a[row][j]) % modulus
                                  for j in range(col, len(a[0]))]
        row += 1
        if row == len(a):
            break
    return row


def dimension_bright(d):
    return (d + 1) + (d - 1) * (d - 1 - int(d % 2 == 0)) \
        + (d - 3) * d * (d - 3) // 2 - 2 * int(isqrt(d) ** 2 == d)


def expected_rank(d, k):
    return int((d - 2 * k) ** 2 != d) \
        + (d - 1) * int(1 <= k <= d - 1 and 2 * k != d) \
        + d * (d - 3) // 2 * int(2 <= k <= d - 2)


def mask(indices):
    return sum(1 << j for j in indices)


def krawtchouk(d, k, j):
    return sum((-1) ** r * comb(j, r) * comb(d-j, k-r)
               for r in range(max(0, k-d+j), min(k, j) + 1))


def check_ranks():
    cases = 0
    for d in range(4, 10):
        monitors = [mask(c) for c in combinations(range(d), 2)]
        ranks = []
        for k in range(d + 1):
            cols = [mask(c) for c in combinations(range(d), k)]
            m = [[-1 if (t & s).bit_count() % 2 else 1 for s in cols]
                 for t in monitors]
            got = rank_mod(m)
            assert got == expected_rank(d, k), (d, k, got)
            ranks.append(got)
            cases += 1
        assert sum(ranks) == dimension_bright(d)
    return cases


def check_radial():
    cases = 0
    for d in (4, 9, 16, 25):
        s = isqrt(d)
        for k in ((d-s)//2, (d+s)//2):
            q = [krawtchouk(d, k, j) for j in range(d+1)]
            assert q[2] == 0
            for j in range(d+1):
                neighbor = (j * q[j-1] if j else 0) \
                    + ((d-j) * q[j+1] if j<d else 0)
                assert neighbor == (d-2*k) * q[j]
                cases += 1
    return cases


def check_physical():
    import numpy as np
    from scipy.sparse import csr_matrix, identity, kron, diags
    from scipy.sparse.linalg import expm_multiply
    cases = 0
    for d, t, tolerance in ((4, 130., 2e-4), (5, 150., 1e-3)):
        n = 1 << d
        edges = [(x, x ^ (1 << j)) for x in range(n) for j in range(d)]
        h = csr_matrix((np.ones(len(edges)),
                        ([x for x,y in edges], [y for x,y in edges])),
                       shape=(n,n),dtype=np.complex128)
        ident = identity(n,format='csr',dtype=np.complex128)
        sites = {mask(c) for c in combinations(range(d),2)}
        weights = [1. if x in sites else 0. for x in range(n)]
        # Column-major vectorization of the density matrix.
        decay = [-0.5*(weights[x]+weights[y]) if x!=y else 0.
                 for y in range(n) for x in range(n)]
        liouvillian = -1j*(kron(ident,h)-kron(h,ident))+diags(decay)
        initial = np.zeros(n*n,dtype=np.complex128)
        initial[0] = 1.
        rho = expm_multiply(t*liouvillian,initial).reshape((n,n),order='F')
        assert abs(np.trace(rho)-1.)<2e-9
        a = (comb(d,(d-isqrt(d))//2)/2**d) if isqrt(d)**2==d else 0.
        b = dimension_bright(d)
        predicted = (1-2*a)**2/b + 4*a*a*cos(isqrt(d)*t)**2
        assert abs(rho[0,0].real-predicted)<tolerance, (d,rho[0,0],predicted)
        assert abs(rho[0,0].imag)<2e-9
        cases += 1
    return cases


if __name__ == '__main__':
    rank_cases = check_ranks()
    radial_cases = check_radial()
    physical_cases = check_physical()
    print(f'VERIFY_OK rank_cases={rank_cases} radial_cases={radial_cases} physical_cases={physical_cases}')
