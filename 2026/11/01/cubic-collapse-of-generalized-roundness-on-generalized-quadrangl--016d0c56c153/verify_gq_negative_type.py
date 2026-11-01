#!/usr/bin/env python3
"""Independent finite-case checks for powered-distance negative type on GQ incidence graphs.

Requires Python >=3.9, numpy, scipy. Finite checks corroborate, rather than prove,
statements concerning all generalized quadrangles of equal order.
"""
from itertools import product
from collections import deque
from math import log
import numpy as np
from scipy.optimize import brentq


def normalized(vector, q):
    for v in vector:
        if v % q:
            inv = pow(int(v), -1, q)
            return tuple((z*inv) % q for z in vector)
    raise ValueError('zero vector')


def symplectic(a, b, q):
    return (a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2]) % q


def incidence_W(q):
    """Construct W(q) from totally isotropic lines in F_q^4, q prime."""
    points = sorted({normalized(a, q) for a in product(range(q),repeat=4) if any(a)})
    loc = {p:i for i,p in enumerate(points)}
    lines = set()
    for i, a in enumerate(points):
        for b in points[i+1:]:
            if symplectic(a,b,q):
                continue
            line = frozenset(loc[normalized([(s*a[j]+t*b[j]) % q for j in range(4)], q)]
                             for s,t in product(range(q),repeat=2) if s or t)
            assert len(line)==q+1
            lines.add(line)
    lines = sorted(lines,key=lambda s:tuple(sorted(s)))
    B=np.array([[int(i in line) for line in lines] for i in range(len(points))],dtype=np.int64)
    assert B.shape==((q+1)*(q*q+1),)*2
    return B


def graph_distances(B):
    v=B.shape[0]
    adj=[[] for _ in range(2*v)]
    for i,j in zip(*B.nonzero()):
        adj[i].append(v+j); adj[v+j].append(i)
    D=np.full((2*v,2*v),-1,dtype=np.int64)
    for src in range(2*v):
        D[src,src]=0
        todo=deque([src])
        while todo:
            u=todo.popleft()
            for w in adj[u]:
                if D[src,w]<0:
                    D[src,w]=D[src,u]+1
                    todo.append(w)
    assert (D>=0).all()
    return D


def threshold_function(p,q):
    return q**3*4.**p-q*q*(q+1)*3.**p+q*(q+1)*2.**p-(q+1)


def check(q):
    B=incidence_W(q)
    v=len(B); N=2*v
    A=B@B.T-(q+1)*np.eye(v,dtype=np.int64)
    Al=B.T@B-(q+1)*np.eye(v,dtype=np.int64)
    eye=np.eye(v,dtype=np.int64); one=np.ones((v,v),dtype=np.int64)
    assert (B.sum(axis=0)==q+1).all() and (B.sum(axis=1)==q+1).all()
    assert (np.diag(A)==0).all() and ((A==0)|(A==1)).all()
    assert (np.diag(Al)==0).all() and ((Al==0)|(Al==1)).all()
    assert np.array_equal(A@A,q*(q+1)*eye+(q-1)*A+(q+1)*(one-eye-A))
    assert np.array_equal(Al@Al,q*(q+1)*eye+(q-1)*Al+(q+1)*(one-eye-Al))
    D=graph_distances(B)
    # Compare every one of the N^2 BFS distances with the independent incidence formulas.
    expected=np.zeros((N,N),dtype=np.int64)
    expected[:v,:v]=2*A+4*(one-eye-A)
    expected[v:,v:]=2*Al+4*(one-eye-Al)
    expected[:v,v:]=B+3*(one-B)
    expected[v:,:v]=expected[:v,v:].T
    assert np.array_equal(D,expected)
    root=brentq(lambda p:threshold_function(p,q),0,1,xtol=1e-14)
    p0=log(1+1/q)/log(2)
    assert 0<root<p0
    f=q*(q+1)**2//2; g=q*(q*q+1)//2
    assert 1+2*f+2*g==N-1
    def predicted_eigenvalues(p):
        x=2**p; y=3**p; z=4**p
        r=(q-1)*x-q*z
        s=q*z-(q+1)*x
        return sorted([threshold_function(p,q)]+[r-(y-1)*(2*q)**.5]*f+
                      [r+(y-1)*(2*q)**.5]*f+[s]*(2*g))
    # Independent full matrix power and projected Gram at three p-values.
    H=np.eye(N)-np.ones((N,N))/N
    for p in [root/2,root,root+(p0-root)/2]:
        P=D.astype(float)**p
        P[D==0]=0.
        projected=H@P@H
        actual=np.linalg.eigvalsh(projected)
        predicted=predicted_eigenvalues(p)
        # Projected spectrum includes one extra zero eigenvalue.
        target=sorted(predicted+[0.])
        assert np.max(np.abs(actual-target))<1e-8, (q,p,np.max(np.abs(actual-target)))
        if p<root-1e-9:assert actual[-1]<1e-8 and actual[-2]<-1e-5
        if abs(p-root)<1e-9:
            assert abs(actual[-1])<1e-8 and abs(actual[-2])<1e-8 and actual[-3]<-1e-5
        if p>root+1e-9:assert actual[-1]>1e-5
    print(f'CASE_OK q={q} vertices={N} exact_bfs_distances={N*N} '
          f'harmonic_multiplicities={f},{g} exponent={root:.12f} '
          f'critical_Hilbert_dimension={N-2}')


def main():
    for q in [2,3,5]:
        check(q)
    A=log(4/3)
    B=log(3/2)
    for q in [11,31,101,301]:
        root=brentq(lambda p:threshold_function(p,q),0,min(1.,20./q**3),xtol=1e-16)
        leading=1/(A*q**3)+B/(A*A*q**4)
        assert abs(root-leading)<10./q**5
    print('ASYMPTOTIC_OK exponent_order=q_inverse_cubed')
    print('ALL_GQ_NEGATIVE_TYPE_CHECKS_OK')


if __name__=='__main__':
    main()
