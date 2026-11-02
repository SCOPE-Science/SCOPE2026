#!/usr/bin/env python3
"""Independent finite exact checks for a clique-bouquet heat-variation theorem.

Run with Python 3, standard library only. Finite tests do not replace the
proof for arbitrary clique sizes and arbitrary real-valued input.
"""
from fractions import Fraction
from itertools import product
from random import Random
from math import exp


def graph(ks):
    n=1+sum(ks)
    edges=[]
    start=1
    for k in ks:
        vertices=(0,)+tuple(range(start,start+k))
        for a in range(len(vertices)):
            for b in range(a+1,len(vertices)):
                edges.append((vertices[a],vertices[b]))
        start+=k
    return n,edges


def laplacian_action(z, n, edges):
    out=[0]*n
    for u,v in edges:
        x=z[u]-z[v]
        out[u]+=x;out[v]-=x
    return out


def variation(z, edges):
    return sum(abs(z[u]-z[v]) for u,v in edges)


def directional(z,n,edges):
    dz=[-a for a in laplacian_action(z,n,edges)]
    total=0
    for u,v in edges:
        a=z[u]-z[v];b=dz[u]-dz[v]
        total+=abs(b) if a==0 else (b if a>0 else -b)
    return total


def indicator_from_counts(ks,xs):
    z=[0]
    for k,x in zip(ks,xs):z += [1]*x+[0]*(k-x)
    return z


def symbolic_J(ks,xs):
    return sum(x*(k+1-x) for k,x in zip(ks,xs))


def symbolic_D(ks,xs):
    K=sum(ks);X=sum(xs)
    return X*(K-2*X)-sum((k*k+3*k+1)*x-(k+3)*x*x for k,x in zip(ks,xs))


def check_cut_profiles():
    profiles=cuts=extreme=0
    # Independent direct edge counts vs symbolic formula, and upper bound.
    for m in range(1,5):
        for ks in product(range(1,5),repeat=m):
            if sum(ks)>10:continue
            profiles+=1
            n,edges=graph(ks)
            K=sum(ks);kmin=min(ks);mu=K-2*kmin-1
            witness=indicator_from_counts(ks,[kmin if k==kmin and i==ks.index(kmin) else 0 for i,k in enumerate(ks)])
            assert directional(witness,n,edges)==mu*variation(witness,edges)
            extreme+=1
            for xs in product(*(range(k+1) for k in ks)):
                z=indicator_from_counts(ks,xs)
                J=variation(z,edges);D=directional(z,n,edges)
                assert J==symbolic_J(ks,xs),(ks,xs,J)
                assert D==symbolic_D(ks,xs),(ks,xs,D)
                assert D<=mu*J,(ks,xs,D,mu,J)
                cuts+=1
    return profiles,cuts,extreme


def check_coarea():
    rng=Random(200713)
    trials=0
    for ks in ((1,2),(2,2),(1,3),(1,1,2),(2,2,2),(1,1,1,1),(2,3),(1,1,1)):
        n,edges=graph(ks);mu=sum(ks)-2*min(ks)-1
        for _ in range(1200):
            z=[rng.randrange(-7,8) for v in range(n)]
            J=variation(z,edges);D=directional(z,n,edges)
            assert D<=mu*J,(ks,z,D,mu,J)
            vals=sorted(set(z))
            coarea=0;coarea_d=0
            for v,nextv in zip(vals,vals[1:]):
                delta=nextv-v
                s=[int(u>=nextv) for u in z]
                coarea+=delta*variation(s,edges)
                coarea_d+=delta*directional(s,n,edges)
            assert J==coarea and D<=coarea_d,(ks,z,J,coarea,D,coarea_d)
            trials+=1
    return trials


def check_heat():
    # Explicit Euler at tiny time tests predicted logarithmic norm.
    rng=Random(177)
    checked=0
    for ks in ((1,1),(1,2),(2,2),(2,3),(1,1,1),(1,1,2),(2,2,2),(3,3,3),(1,1,1,1)):
        n,edges=graph(ks);mu=sum(ks)-2*min(ks)-1
        for _ in range(400):
            z=[rng.randrange(-5,6) for v in range(n)]
            J=variation(z,edges)
            if J==0:continue
            dt=1e-6
            l=laplacian_action(z,n,edges)
            nxt=[x-dt*y for x,y in zip(z,l)]
            # Forward Euler can have O(dt^2) overshoot where heat wouldn't.
            # Use first-order comparison tolerance bounded independently of sizes.
            assert variation(nxt,edges) <= (1+mu*dt)*J+1e-8
            checked+=1
    return checked

if __name__=='__main__':
    a,b,c=check_cut_profiles()
    d=check_coarea()
    e=check_heat()
    print('PASS exact profiles',a,'direct cut formula/inequalities',b,'critical witnesses',c)
    print('PASS random integer coarea + generator inequality',d)
    print('PASS first-order numerical heat step diagnostics',e)
