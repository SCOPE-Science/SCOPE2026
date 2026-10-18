#!/usr/bin/env python3
"""Independent finite-dimensional checks for magnetic Grover walks on complete bipartite graphs.

The walk and spectral prediction are each built from their definitions.
Run: python verify.py (requires numpy, sympy).
"""
import math
import numpy as np
import sympy as sp


def walk(m, n, beta):
    assert m >= 2 and n >= 2
    vertices = range(m + n)
    arcs = [(i, m + j) for i in range(m) for j in range(n)]
    arcs += [(m + j, i) for j in range(n) for i in range(m)]
    at = {a: k for k, a in enumerate(arcs)}
    dim = len(arcs)
    d = np.zeros((m + n, dim), dtype=complex)
    for k, (a, b) in enumerate(arcs):
        d[a, k] = 1.0 / math.sqrt(n if a < m else m)
    S = np.zeros((dim, dim), dtype=complex)
    for k, (a, b) in enumerate(arcs):
        phase = beta if (a, b) == (0, m) else (-beta if (a, b) == (m, 0) else 0.0)
        S[k, at[(b, a)]] = np.exp(1j * phase)
    C = 2 * (d.conj().T @ d) - np.eye(dim)
    U = S @ C
    return U, d, S


def prediction(m, n, beta):
    t = 4 * math.sqrt((m - 1) * (n - 1)) / (m * n) * abs(math.sin(beta / 2))
    theta = 0.5 * math.asin(min(1.0, t))
    special = [np.exp(1j * (j * math.pi / 2 + sig * theta)) for j in range(4) for sig in (1, -1)]
    pinned = [1.0, -1.0] * (m*n-m-n) + [1j, -1j] * (m+n-4)
    return theta, np.asarray(special + pinned)


def unitary_maxdiff(a, b):
    return float(np.max(np.abs(a - b)))


def eigen_multiset_error(a, b):
    """Permutation-free assignment by greedy nearest neighbor, safe here since gaps > tolerance."""
    rem = list(np.asarray(b, dtype=complex))
    err = 0.0
    for x in np.asarray(a, dtype=complex):
        idx = int(np.argmin([abs(x-y) for y in rem]))
        err = max(err, abs(x-rem.pop(idx)))
    return err


def run():
    z, x, y, m, n, s = sp.symbols('z x y m n s', real=True)
    fact = (z**4-1)**2 + 64*x*z**4
    target = z**8 - 2*(1-32*x)*z**4 + 1
    assert sp.expand(fact-target) == 0
    # Nonzero singular-value product for an m-by-n single-edge twist.
    assert sp.expand((x+y)**2-(x-y)**2-4*x*y) == 0
    # Exact characteristic polynomials, with the magnetic phase kept as an indeterminate.
    phase = sp.Symbol('u', nonzero=True)
    zsym = sp.Symbol('z')
    for M, N in ((2,2), (2,3), (3,3)):
        edges = [(i, M+j) for i in range(M) for j in range(N)]
        arcs = edges + [(v,u0) for u0,v in edges]
        ai = {arc: ix for ix,arc in enumerate(arcs)}
        d = sp.zeros(M+N,2*M*N)
        for ix,(u0,v) in enumerate(arcs):
            d[u0,ix]=1/sp.sqrt(N if u0<M else M)
        flip=sp.zeros(2*M*N)
        for ix,(u0,v) in enumerate(arcs):
            phase_factor = phase if (u0,v)==(0,M) else 1/phase if (u0,v)==(M,0) else 1
            flip[ix,ai[(v,u0)]]=phase_factor
        matrix=flip*(2*d.T*d-sp.eye(2*M*N))
        observed=matrix.charpoly(zsym).as_expr()
        A=sp.Rational((M-1)*(N-1),(M*N)**2)
        expected=(zsym**2-1)**(M*N-M-N)*(zsym**2+1)**(M+N-4)*(
            (zsym**4-1)**2+16*A*(2-phase-1/phase)*zsym**4)
        assert sp.simplify(observed-expected)==0
    cases = [(2,2,0),(2,2,math.pi/3),(2,2,math.pi),
             (2,3,0.21),(2,3,2.0),(3,3,1.1),(3,4,0.8),
             (4,5,math.pi),(5,6,2*math.pi/7),(6,7,0.43)]
    numcheck = 5
    for m, n, beta in cases:
        U, d, S = walk(m,n,beta)
        size = 2*m*n
        assert U.shape==(size,size)
        assert unitary_maxdiff(U.conj().T@U, np.eye(size))<2e-13
        assert unitary_maxdiff(S@S, np.eye(size))<1e-14
        numcheck += 2
        theta, roots= prediction(m,n,beta)
        actual = np.linalg.eigvals(U)
        # Hungarian assignment is robust to repeated/eigenvalue degeneracy.
        from scipy.optimize import linear_sum_assignment
        cost = np.abs(actual[:,None]-roots[None,:]); ii,jj=linear_sum_assignment(cost)
        assert max(cost[ii,jj]) < 1e-9, (m,n,beta,max(cost[ii,jj]))
        numcheck += 1
        for k in (1,2,3,5):
            R=np.linalg.matrix_power(U,4*k)-np.eye(size)
            wantop=2*abs(math.sin(2*k*theta))
            wantfro=32*math.sin(2*k*theta)**2
            assert abs(np.linalg.norm(R,2)-wantop)<3e-10
            assert abs(np.linalg.norm(R,'fro')**2-wantfro)<3e-10
            numcheck += 2
        actualtr=np.trace(np.linalg.matrix_power(U,4))
        assert abs(actualtr-(size-8+8*math.cos(4*theta)))<2e-10
        numcheck += 1
    # A deliberately rational spectral angle within accessible magnetic range.
    m,n,p,q=3,4,1,17
    theta=p*math.pi/q
    amp=math.sin(2*theta)*m*n/(4*math.sqrt((m-1)*(n-1)))
    beta=2*math.asin(amp)
    U,_,_=walk(m,n,beta)
    t=4*q//math.gcd(q,2)
    assert np.linalg.norm(np.linalg.matrix_power(U,t)-np.eye(2*m*n),2)<1e-10
    for t0 in range(1,t):
        assert np.linalg.norm(np.linalg.matrix_power(U,t0)-np.eye(2*m*n),2)>1e-5
    numcheck += t
    print('PASS:',numcheck,'independent symbolic/matrix/period checks; rational period=',t)

if __name__=='__main__':
    run()
