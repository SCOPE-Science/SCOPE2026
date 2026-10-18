#!/usr/bin/env python3
"""Independent exact edge enumeration and stochastic integration for central sections."""
from itertools import combinations, product
from math import acos, pi, sqrt
from random import Random


def graph(kind, p, q):
    assert 0 < p < q or (kind == 'mid' and p == q)
    edges = set()
    def add(a, b):
        a, b = tuple(a), tuple(b)
        assert a != b
        edges.add(tuple(sorted((a, b))))
    for i in range(3):
        j, k = [z for z in range(3) if z != i]
        for sign in (-1, 1):
            if kind in ('lo', 'mid'):
                ring = [(-1,j), (-1,k), (1,j), (1,k)]
                for n in range(4):
                    a = [0]*3; b = [0]*3
                    a[i] = b[i] = sign*q
                    val, idx = ring[n]; a[idx] = val*p
                    val, idx = ring[(n+1)%4]; b[idx] = val*p
                    add(a, b)
            else:
                for sj,sk in product((-1,1), repeat=2):
                    a = [0]*3; b = [0]*3
                    a[i] = b[i] = sign*q
                    a[j] = sj*q; a[k] = sk*p
                    b[j] = sj*p; b[k] = sk*q
                    add(a, b)
    if kind == 'lo':
        for i,j in combinations(range(3), 2):
            for si,sj in product((-1,1), repeat=2):
                a=[0]*3;b=[0]*3
                a[i]=si*q; a[j]=sj*p
                b[i]=si*p; b[j]=sj*q
                add(a,b)
    elif kind == 'hi':
        for k in range(3):
            i,j=[z for z in range(3) if z!=k]
            for si,sj in product((-1,1), repeat=2):
                a=[0]*3;b=[0]*3
                a[i]=b[i]=si*q; a[j]=b[j]=sj*q
                a[k]=-p;b[k]=p
                add(a,b)
    return sorted(edges)


def counts(kind, p, q, normal):
    a,b,c = sorted((abs(x) for x in normal), reverse=True)
    assert a>b>c>0
    if kind=='lo':
        return 4+2*(c*q>b*p)+2*(b*q<a*p)+2*(c*q<a*p)
    if kind=='hi':
        return (4+2*(a*q<b*q+c*p)
                  +2*(a*q>b*p+c*q and a*p<(b+c)*q)
                  +2*(b*q>a*p+c*q))
    return 8


def crossings(edges, normal):
    def dot(v): return sum(v[i]*normal[i] for i in range(3))
    values = [dot(v) for edge in edges for v in edge]
    if any(v==0 for v in values): return None
    return sum(dot(v)*dot(w)<0 for v,w in edges)


def angle_mean(kind,s):
    if kind=='lo':
        return (24*acos(1/(1+s*s))+12*acos(2*s/(1+s*s)))/pi
    if kind=='hi':
        return (12*acos((2-s*s)/(2+s*s))+24*acos((1+2*s)/(2+s*s)))/pi
    return 8.0


def run():
    tested=0
    for kind in ('lo','mid','hi'):
        for p,q in ((1,9),(1,4),(1,2),(3,4),(8,9)) if kind!='mid' else ((1,1),):
            edges=graph(kind,p,q)
            assert len(edges) == (24 if kind=='mid' else 36)
            vertices={v for e in edges for v in e}
            assert len(vertices)==(12 if kind=='mid' else 24)
            for a in range(3,25):
                for b in range(2,a):
                    for c in range(1,b):
                        normal=(a,b,c)
                        observed=crossings(edges,normal)
                        if observed is None: continue
                        predicted=counts(kind,p,q,normal)
                        assert observed == predicted, (kind,p,q,normal,observed,predicted)
                        tested+=1
    assert tested > 10000
    # Every listed count is realized by an open normal cone, at all tested rational scales.
    for p,q in ((1,100),(1,7),(1,2),(7,8),(99,100)):
        s=p/q
        eps=s*(1-s)/100
        small=(1+eps,1,1-eps)
        assert counts('lo',p,q,small)==6
        assert counts('lo',p,q,(2/s,1,s/2))==8
        assert counts('lo',p,q,(2/s,1,(1+s)/2))==10
        assert counts('hi',p,q,(10/s,1,.5))==4
        assert counts('hi',p,q,small)==6
        a=(1+1/s)/2
        c=min((a-1)/(2*s),(1-s)/4,0.25)
        assert counts('hi',p,q,(a,1,c))==8
        delta=s*(1-s)/10
        assert counts('hi',p,q,(1+delta,1,(1-s)/2))==10
    # Gaussian normals are rotationally invariant; probability is an angular ratio.
    rng=Random(19022)
    checks=[]
    for kind,s in (('lo',.25),('lo',.5),('lo',.75),('hi',.25),('hi',.5),('hi',.75)):
        p,q=int(s*4),4
        edges=graph(kind,p,q)
        n=18000
        score=0
        for _ in range(n):
            u=tuple(rng.gauss(0,1) for i in range(3))
            score+=crossings(edges,u)
        empirical=score/n
        target=angle_mean(kind,s)
        assert abs(empirical-target)<.11,(kind,s,empirical,target)
        checks.append((kind,s,round(empirical,5),round(target,5)))
    print('EXACT_SECTION_CHAMBERS_OK',tested,'positive cones and symbolic edge sets OK')
    print('HAAR_EXPECTATION_MC_OK', checks)
if __name__=='__main__':run()
