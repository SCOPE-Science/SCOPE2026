#!/usr/bin/env python3
"""Finite checks for the negative-type spectrum of generalized-quadrangle Levi graphs.

Requires Python >=3.9, standard library only. This is not an infinite proof.
"""
from collections import deque
from itertools import product
from math import exp, log, sqrt


def proj(v, q):
    for a in v:
        if a % q:
            z = pow(a, -1, q)
            return tuple((z * b) % q for b in v)
    raise ValueError('zero vector')


def form(v, w, q):
    return (v[0]*w[2] - v[2]*w[0] + v[1]*w[3] - v[3]*w[1]) % q


def gq(q):
    assert q in (2,3,5,7) and all(q % k for k in range(2,int(sqrt(q))+1))
    pts = sorted({proj(v,q) for v in product(range(q), repeat=4) if any(v)})
    index = {p:i for i,p in enumerate(pts)}
    lines = set()
    for i,v in enumerate(pts):
        for w in pts[i+1:]:
            if form(v,w,q) == 0:
                line = frozenset([index[w]] + [index[proj(tuple((v[k]+t*w[k])%q for k in range(4)),q)] for t in range(q)])
                if len(line) == q+1:
                    lines.add(line)
    lines = sorted(lines,key=lambda s:tuple(sorted(s)))
    a = len(pts)
    assert a == (q+1)*(q*q+1) and len(lines) == a
    nbr = [set() for _ in range(2*a)]
    for j,line in enumerate(lines):
        for i in line:
            nbr[i].add(a+j); nbr[a+j].add(i)
    assert all(len(r)==q+1 for r in nbr)
    return nbr


def distances(nbr):
    out=[]
    for s in range(len(nbr)):
        d = [-1]*len(nbr);d[s]=0
        que=deque([s])
        while que:
            v=que.popleft()
            for w in nbr[v]:
                if d[w]<0:
                    d[w]=d[v]+1; que.append(w)
        assert min(d)==0 and max(d)==4
        out.append(d)
    return out


def F(q,p):
    return -(q+1) + q*(q+1)*2**p - q*q*(q+1)*3**p + q**3*4**p


def root(q):
    lo=0.; hi=log(1+1/q)/log(2)
    assert F(q,lo)<0<F(q,hi)
    for _ in range(70):
        mid=(hi+lo)/2
        if F(q,mid)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def spectral_eigs(q,p):
    def e(l):
        b2=l*l-(q+1)
        b3=l*(l*l-2*q-1)
        b4=(l**4-(3*q+1)*l*l+q*(q+1))/(q+1)
        return l+2**p*b2+3**p*b3+4**p*b4
    return [e(-(q+1)),e(-sqrt(2*q)),e(0),e(sqrt(2*q)),e(q+1)]


def verify(q):
    nbr=gq(q)
    dist=distances(nbr)
    n=len(nbr)
    layer=[1,q+1,q*(q+1),q*q*(q+1),q**3]
    assert sum(layer)==n
    assert all([row.count(k) for k in range(5)] == layer for row in dist)
    recs=0
    for i in range(n):
        for j in range(n):
            dij=dist[i][j]
            s2=sum(dist[k][j]==2 for k in nbr[i])
            s3=sum(dist[k][j]==3 for k in nbr[i])
            assert s2 == q*(dij==1)+(dij==3)
            assert s3 == q*(dij==2)+(q+1)*(dij==4)
            recs+=2
    p=root(q)
    eig=spectral_eigs(q,p)
    assert abs(eig[0])<1e-8
    assert max(eig[1:4])<-0.02
    assert eig[4]>0
    # The point/line bipartition vector is a direct eigenvector of D_p.
    half=n//2
    signs=[1]*half+[-1]*half
    for i in range(n):
        value=sum((dist[i][j]**p if i!=j else 0)*signs[j] for j in range(n))
        assert abs(value-eig[0]*signs[i])<1e-8
    # A perturbation on either side of p must change the sign of the mode.
    assert F(q,p*.9)<0 and F(q,min(1,p*1.1))>0
    return n,recs,p


def main():
    checks=0
    for q in (2,3,5):
        n,recs,p=verify(q)
        checks+=recs
        print(f'GQ({q},{q}): {n} vertices, p-critical={p:.12f}, recurrence_checks={recs}')
    for q in range(2,200):
        p=root(q)
        assert 0<p<log(1+1/q)/log(2)
        eig=spectral_eigs(q,p*.999)
        assert all(x<0 for x in eig[:4]),(q,eig)
    print(f'CHECK_OK exact_graph_recurrence_entries={checks} scalar_orders=2..199')

if __name__=='__main__':
    main()
