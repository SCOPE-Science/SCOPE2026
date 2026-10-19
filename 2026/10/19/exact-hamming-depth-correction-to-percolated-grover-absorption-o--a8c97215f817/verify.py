"""Reproduction checks for sink-shell absorption in percolated hypercubes.

Run: python verify.py
Requires Python 3 with numpy and scipy.
The exact formula uses Fraction. Independent numerical resistance is obtained
from sparse graph Laplacian systems, and the Q3 dynamics uses averaged
coin/per-edge swap channels without spectral-projector shortcuts.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import splu


def B(d, h):
    if h == d + 1:
        return Fraction(0)
    assert 1 <= h <= d
    return Fraction(sum(math.comb(d, j) for j in range(h, d + 1)),
                    (2**d)*d*math.comb(d - 1, h - 1))


def resistance(d, k):
    assert d >= 3 and 1 <= k < d
    correction = (k*(B(d, k)-B(d, k+1))**2
                  + 4*B(d, k+1)**2
                  + (d-k-1)*(B(d, k+1)-B(d, k+2))**2)
    return 2*B(d, 1) + (Fraction(d-1, 1)
                         / (Fraction(d-2, 1)+Fraction(1, 2**(d-1))))*correction


def independent_resistance(d, k):
    num = (1 << d) - 1
    rows, cols, values = [], [], []
    deg = np.zeros(num)
    for vertex in range(1, num+1):
        for j in range(d):
            nbr = vertex ^ (1 << j)
            if nbr > vertex:
                a,b = vertex-1,nbr-1
                deg[a] += 1
                deg[b] += 1
                rows.extend((a,b))
                cols.extend((b,a))
                values.extend((-1.0,-1.0))
    rows.extend(range(num)); cols.extend(range(num)); values.extend(deg)
    L = csc_matrix((values,(rows,cols)),shape=(num,num))
    a = (1 << k)-1
    b = a | (1 << k)
    rhs = np.zeros(num-1)
    if a < num: rhs[a-1] = 1
    if b < num: rhs[b-1] = -1
    return float(rhs @ splu(L[:-1,:-1]).solve(rhs))


def quantum_channel_survival(d,k,p,steps=600):
    n = 1 << d
    size = n*d
    G = 2*np.ones((d,d))/d-np.eye(d)
    C = np.kron(np.eye(n),G)
    pairs = [(v*d+j,(v^(1<<j))*d+j)
             for v in range(n) for j in range(d) if v < (v^(1<<j))]
    vec = np.zeros(size)
    vec[((1<<k)-1)*d+k] = 1
    rho = np.outer(vec,vec)
    for _ in range(steps):
        rho = C@rho@C
        for a,b in pairs:
            perm = np.arange(size)
            perm[a], perm[b] = perm[b], perm[a]
            rho = (1-p)*rho + p*rho[np.ix_(perm,perm)]
        rho[:d,:]=0;rho[:,:d]=0
    return float(np.trace(rho))


def main():
    comparisons=0
    worst=0.0
    for d in range(3,9):
        for k in range(1,d):
            got = independent_resistance(d,k)
            expected = float(resistance(d,k))
            discrepancy=abs(got-expected)
            assert discrepancy < 2e-12,(d,k,discrepancy)
            worst=max(worst,discrepancy)
            comparisons+=1
    print('Independent electrical-network checks:',comparisons,'maximum error',worst)
    for k in (1,2):
        for p in (0.4,0.7):
            got=quantum_channel_survival(3,k,p)
            expected=(1-float(resistance(3,k)))/2
            discrepancy=abs(got-expected)
            assert discrepancy < 1e-10,(k,p,discrepancy)
            worst=max(worst,discrepancy)
            comparisons+=1
    print('Total independent checks:',comparisons,'maximum absolute error',worst)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
