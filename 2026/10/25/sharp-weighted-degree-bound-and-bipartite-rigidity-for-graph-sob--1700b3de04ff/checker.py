"""Reproducible numerical tests of sharp finite-graph clipping bounds.

Requires NumPy and SciPy; finite tests are diagnostics, not substitutes for the proof.
"""
from itertools import combinations
import numpy as np
from scipy.linalg import eigh


def laplacian(n, edges):
    L = np.zeros((n, n), dtype=float)
    for i, j, w in edges:
        assert i != j and w > 0
        L[i, i] += w
        L[j, j] += w
        L[i, j] -= w
        L[j, i] -= w
    return L


def mask_modulus(A, mask):
    d = np.array([(mask >> i) & 1 for i in range(A.shape[0])], dtype=float)
    DAD = d[:, None] * A * d[None, :]
    return float(np.sqrt(max(0.0, eigh(DAD, A, eigvals_only=True)[-1])))


def rho_modulus(A, mask):
    n = len(A)
    I = [i for i in range(n) if (mask >> i) & 1]
    J = [j for j in range(n) if not ((mask >> j) & 1)]
    if not I or not J:
        return float(bool(I))
    X = A[np.ix_(I, I)]
    Y = A[np.ix_(J, J)]
    B = -A[np.ix_(I, J)]
    # rho^2 is the top generalized eigenvalue of B Y^-1 B^T against X.
    rho2 = max(0.0, eigh(B @ np.linalg.solve(Y, B.T), X, eigvals_only=True)[-1])
    return float(1.0 / np.sqrt(1.0 - rho2))


def edges_cycle(n, weight=1):
    assert n >= 3
    return [(i, (i+1) % n, weight) for i in range(n)]


def edges_complete_bipartite(p, q, weight=1):
    return [(i, p+j, weight) for i in range(p) for j in range(q)]


def run():
    total_masks = 0
    for n, edges in [
        (2, [(0, 1, 2)]),
        (3, edges_cycle(3)),
        (4, edges_cycle(4)),
        (5, edges_cycle(5)),
        (6, edges_cycle(6)),
        (7, edges_cycle(7)),
        (8, edges_cycle(8)),
        (6, edges_complete_bipartite(3, 3)),
        (7, edges_complete_bipartite(3, 4)),
        (6, [(0,1,.5), (1,2,2.), (2,3,.75), (3,4,3.), (4,5,1.5), (5,0,1.)]),
    ]:
        L = laplacian(n, edges)
        degree = np.diag(L)
        D = float(degree.max())
        for gamma in [.125, .7, 2.3, 10.0]:
            A = np.eye(n) + gamma*L
            bound = (1.0+gamma*D)/np.sqrt(1.0+2.0*gamma*D)
            observed = 0.
            for mask in range(1 << n):
                norm1 = mask_modulus(A, mask)
                norm2 = rho_modulus(A, mask)
                assert np.isclose(norm1, norm2, atol=4.e-11, rtol=4.e-11), (n,gamma,mask,norm1,norm2)
                assert norm1 <= bound+4.e-11, (n,gamma,mask,norm1,bound)
                observed = max(norm1, observed)
                total_masks += 1
            bip_reg = n in (2,4,6,8) and ((n in (4,6,8) and edges == edges_cycle(n)) or (n==6 and edges == edges_complete_bipartite(3,3)) or n==2)
            if bip_reg:
                assert abs(observed-bound) < 4.e-11, (n,gamma,observed,bound)
            if n in (3,5,7) and edges == edges_cycle(n):
                assert observed < bound-1.e-6, (n,gamma,observed,bound)
    star_cases = 0
    for n in [1,2,3,4,6,8,12]:
        edges = [(0,j,1.0) for j in range(1,n+1)]
        L = laplacian(n+1,edges)
        for gamma in [.1,.7,2.,5.]:
            A = np.eye(n+1)+gamma*L
            observed = max(rho_modulus(A,mask) for mask in range(1<<(n+1)))
            exact = np.sqrt(1.+n*gamma**2/(1.+(n+1)*gamma))
            assert np.isclose(observed,exact,rtol=1.e-10,atol=1.e-10),(n,gamma,observed,exact)
            star_cases += 1
    print('PASS:', total_masks, 'mask comparisons and', star_cases, 'exact-star regressions; weighted degree and equality rigidity')


if __name__ == '__main__':
    run()
