#!/usr/bin/env python3
"""Finite rational and numerical diagnostics for weighted unicyclic phase dynamics.
Checks are not substitutes for the infinite-parameter proof.
"""
import math
import random
import numpy as np
import sympy as sp

def case(n, path_weights, attachments):
    # n odd; edges directed i -> i+1, and extra trees each (parent,new,weight)
    assert n%2==1 and n>=3 and len(path_weights)==n-1
    N=n+len(attachments)
    ed=[(i,i+1,sp.Rational(a)) for i,a in enumerate(path_weights)]+[(a,b,sp.Rational(w)) for a,b,w in attachments]
    assert len(ed)==N-1
    B=sp.zeros(N,N-1)
    for j,(u,v,weight) in enumerate(ed): B[u,j]=1;B[v,j]=-1
    K=B.T*B
    D=sp.diag(*[w for _,_,w in ed])
    c=sp.Matrix([1]*(n-1)+[0]*len(attachments))
    v=D.inv()*c
    A=(c.T*v)[0]
    B3=sum(v[i]**3 for i in range(n-1))
    wc=1/A
    H=D-wc*c*c.T
    Q=(v.T*K.inv()*v)[0]
    gamma=sp.factor((A**3-B3)/(3*Q))
    # Explicit critical projection against cubic vector
    cubic=sp.Matrix([(-D[i,i]*v[i]**3+wc*A**3*c[i])/6 for i in range(N-1)])
    assert sp.simplify((v.T*cubic)[0]-(A**3-B3)/6)==0
    assert H*v==sp.zeros(N-1,1)
    assert H.rank()==N-2
    assert gamma>0
    # Chord inequality: sampled torus points and all weights below threshold
    rng=random.Random(107+n+N)
    aw=np.array([float(w) for _,_,w in ed]); cs=np.array(c,dtype=float).reshape(-1)
    for k in range(3000):
        z=np.array([rng.uniform(-math.pi,math.pi) for _ in ed]); S=float(cs@z)
        lhs=float(np.sum(aw*(1-np.cos(z))))
        rhs=(1-math.cos(S))/float(A)
        assert lhs+2e-12>=rhs, (n,N,k,lhs,rhs)
    # Infinitesimally above the threshold, the origin has one unstable edge direction.
    heval=np.array(H,float); eig=np.linalg.eigvalsh(heval)
    assert eig[0]>-1e-9 and eig[1]>1e-8
    Hup=np.array(D-(wc+sp.Rational(1,10000))*c*c.T,float)
    eigup=np.linalg.eigvalsh(Hup)
    assert eigup[0]<-1e-10 and eigup[1]>0
    return dict(n=n,N=N,A=A,B3=B3,wc=wc,Q=Q,gamma=gamma,K=np.array(K,float),D=np.array(D,float),c=cs,v=np.array(v,float).reshape(-1),aw=aw)

def local_critical_iter(ca):
    # For a fixed small perturbation, the tail of n*t_n^2 tends to 1/gamma.
    K,D,c,v,A=ca['K'],ca['D'],ca['c'],ca['v'],float(ca['A'])
    h=.025
    w=1/A
    z=.16*v/max(abs(v))
    q=float(ca['Q']);lv=np.linalg.solve(K,v)/q
    N=160000
    ratios=[]
    for k in range(1,N+1):
        grad=np.diag(D)*np.sin(z)-w*c*math.sin(c@z)
        z-=h*K@grad
        if k in [20000,80000,160000]:
            t=float(lv@z)
            ratios.append((k,(1/t**2)/k, h*float(ca['gamma'])))
    # Asymptotic is slow, use a broad band, trend as n increases.
    for _,approx,expect in ratios:
        assert abs(approx/expect-1)<.26, (ca['n'],ratios)
    return ratios

def main():
    cases=[
        case(3,[1,1],[]),
        case(5,[1,1,1,1],[]),
        case(5,[1,2,sp.Rational(3,2),3],[(0,5,sp.Rational(2,3)),(2,6,5),(6,7,2)]),
        case(7,[1,2,3,4,5,6],[(0,7,1),(3,8,2)]),
    ]
    for ca in cases:
        print('GRAPH',ca['n'],ca['N'],'threshold',ca['wc'],'Q',ca['Q'],'gamma/h',ca['gamma'])
    assert cases[0]['gamma']==sp.Rational(1,1) # m=2 => coefficient 4*(1)/(4)=1
    assert cases[1]['gamma']==2 # m=4 => coefficient 4*3/6 =2
    # Attached trees alter Q only; the critical threshold persists for equal cycle weights.
    bare=case(5,[1]*4,[])
    attached=case(5,[1]*4,[(0,5,1),(2,6,7),(0,7,2),(2,8,4)])
    assert bare['wc']==attached['wc']==sp.Rational(1,4)
    assert attached['Q']>bare['Q']
    assert attached['gamma']<bare['gamma']
    print('ATTACH',bare['Q'],attached['Q'],bare['gamma'],attached['gamma'])
    for ca in [cases[0],cases[1],cases[2]]:
        print('RELAX',ca['n'],ca['N'],local_critical_iter(ca))
    print('VERIFICATION_OK')

if __name__=='__main__': main()
