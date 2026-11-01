#!/usr/bin/env python3
"""Independent finite-field and intersection-algebra checks of a rank-three dual-polar kernel theorem.

Needs Python 3 and NumPy. Numeric spectral diagonalization is supplementary;
proof for all prime powers is supplied separately.
"""
import itertools
import math
import numpy as np


def binary_basis(rows):
    """Canonical reduced binary row-echelon basis of integer-bit rows."""
    v = list(rows)
    k = 0
    for j in range(5, -1, -1):
        t = next((a for a in range(k, len(v)) if v[a] & (1 << j)), None)
        if t is None:
            continue
        v[k], v[t] = v[t], v[k]
        for a in range(len(v)):
            if a != k and (v[a] & (1 << j)):
                v[a] ^= v[k]
        k += 1
        if k == len(v):
            break
    return tuple(v[:k])


def omega(a, b):
    x, y = a & 7, a >> 3
    xx, yy = b & 7, b >> 3
    return ((x & yy).bit_count() + (y & xx).bit_count()) % 2


def lagrangian_subspaces_F2_6():
    subs = set()
    for triple in itertools.combinations(range(1, 64), 3):
        r = binary_basis(triple)
        if len(r) == 3 and all(omega(r[i], r[j]) == 0
                               for i in range(3) for j in range(i+1, 3)):
            subs.add(r)
    return sorted(subs)


def graph_arrays_q2():
    subs = lagrangian_subspaces_F2_6()
    N = len(subs)
    assert N == 135, N
    A = [np.zeros((N,N),dtype=np.int64) for _ in range(4)]
    for a in range(N):
        A[0][a,a] = 1
        for b in range(a+1,N):
            dist = len(binary_basis(subs[a]+subs[b]))-3
            assert 1 <= dist <= 3
            A[dist][a,b] = A[dist][b,a] = 1
    for i,want in enumerate([1,14,56,64]):
        assert (A[i].sum(axis=1) == want).all(), (i,A[i].sum(axis=1))
    assert np.array_equal(sum(A),np.ones((N,N),dtype=np.int64))
    assert np.array_equal(A[1] @ A[1], 14*A[0]+A[1]+3*A[2])
    assert np.array_equal(A[1] @ A[2], 12*A[1]+3*A[2]+7*A[3])
    assert np.array_equal(A[1] @ A[3], 8*A[2]+7*A[3])
    eig = np.linalg.eigvalsh(A[1].astype(float))
    for eigen,mult in [(14,1),(5,35),(-1,84),(-7,15)]:
        assert np.count_nonzero(abs(eig-eigen)<1e-7)==mult,(eigen,mult,eig)
    alpha = bisection(2)
    D = A[1].astype(float) + (2**alpha)*A[2] + (3**alpha)*A[3]
    e = np.linalg.eigvalsh(D)
    assert np.count_nonzero(abs(e)<1e-7)==84
    assert np.count_nonzero(e< -1e-7)==50
    assert np.count_nonzero(e>1e-7)==1
    return N, alpha


def bisection(q):
    lo,hi = 0.0,1.0
    for _ in range(85):
        m=(lo+hi)/2
        if q*q*(3**m-2**m)>1:
            hi=m
        else:
            lo=m
    return (lo+hi)/2


def algebra_tests():
    for q in [2,3,4,5,7,8,9,11,16,25,32,64,101]:
        S=q*q+q+1
        k=q*S
        B=np.array([[0,k,0,0],
                    [1,q-1,q*q*(q+1),0],
                    [0,q+1,q*q-1,q**3],
                    [0,0,S,q**3-1]],dtype=np.float64)
        roots=np.linalg.eigvals(B)
        for v in [k,q*q+q-1,-1,-S]:
            assert min(abs(x-v) for x in roots)<1e-5,(q,v,roots)
        V=(q+1)*(q*q+1)*(q**3+1)
        mult=[1,q*(q*q+1)*S//2,q*q*(q**4+q*q+1),
              q*(q*q+1)*(q*q-q+1)//2]
        assert sum(mult)==V,(q,V,mult)
        alpha=bisection(q)
        assert 0<alpha<1 and q*q*(3**alpha-2**alpha)>1-1e-10
        assert 2**alpha < 1 + 1/q
        for p in [0,alpha/3,2*alpha/3,alpha]:
            L1=(q*q+q-1)+q*(q*q-q-1)*2**p-q**3*3**p
            L3=-S+q*S*2**p-q**3*3**p
            L2=-1+q*q*(3**p-2**p)
            assert L1< -1e-7 and L3< -1e-7 and L2<1e-7,(q,p,L1,L2,L3)
        assert V-1-mult[2]==q*(q*q+1)**2
    print('ALGEBRA_CHECK_OK q=2,...,101')


if __name__=='__main__':
    algebra_tests()
    N,p=graph_arrays_q2()
    print('FULL_GF2_GRAPH_CHECK_OK',N,format(p,'.12f'))
    print('CHECK_OK')
