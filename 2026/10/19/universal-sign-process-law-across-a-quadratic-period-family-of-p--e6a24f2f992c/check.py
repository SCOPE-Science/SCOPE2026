#!/usr/bin/env python3
"""Independent arithmetic and high-precision checks for a periodic planar map."""
from math import gcd
import mpmath as mp
import sympy as sp


def exact_checks():
    Avals=[(3,sp.Integer(1)),(4,sp.sqrt(2)),(5,(1+sp.sqrt(5))/2),(6,sp.sqrt(3))]
    for n,a in Avals:
        A=sp.Matrix([[a,-1],[1,0]])
        assert all(sp.simplify(z)==0 for z in (A**n+sp.eye(2)))
        x=sp.Integer(0); y=sp.Integer(1)
        for k in range(n*n):
            if k==n*n-n:
                assert sp.simplify(x)==0 and sp.simplify(y+1)==0
            # Exact sign is resolved numerically only after algebraic simplification.
            xx=sp.simplify(x)
            if xx==0: u=0
            elif float(sp.N(xx,30))>1e-20:u=1
            elif float(sp.N(xx,30))< -1e-20:u=-1
            else:raise ValueError(('ambiguous exact sign',n,k,xx))
            x,y=sp.simplify(a*u*x-y),x
        assert sp.simplify(x)==0 and sp.simplify(y-1)==0


def modular_checks():
    for n in range(3,150):
        q=n*n;p=n-1
        assert gcd(p,q)==1
        for k in range(q):
            d=(p*k)%q
            hit=sum(0<= (j+d)%q<n for j in range(n))
            prediction=max(0,n-d)+max(0,n-(q-d))
            assert hit==prediction,(n,k,hit,prediction)
        assert sum(0<= (j+p)%q<n for j in range(n))==1
        assert sum(0<= (j+2*p)%q<n for j in range(n))==0
        assert sum(0<= (j+(n+1)*p)%q<n for j in range(n))==n-1


def angular_checks():
    mp.mp.dps=110
    for n in range(3,11):
        q=n*n;p=n-1
        a=2*mp.cos(mp.pi/n)
        x=mp.mpf(0);y=mp.mpf(1)
        rays=[]
        for k in range(q):
            if abs(x)<mp.mpf('1e-75'):x=mp.mpf(0)
            if abs(y)<mp.mpf('1e-75'):y=mp.mpf(0)
            if k==q-n:assert x==0 and abs(y+1)<mp.mpf('1e-75')
            angle=mp.atan2(y,x)%(2*mp.pi)
            rays.append((angle,k))
            x,y=a*abs(x)-y,x
        assert abs(x)<mp.mpf('1e-70') and abs(y-1)<mp.mpf('1e-70')
        ranks={k:i for i,(_,k) in enumerate(sorted(rays))}
        assert len(set(str(t[0])[:65] for t in rays))==q
        assert all((ranks[(k+1)%q]-ranks[k])%q==p for k in range(q)),n
        sorted_rays=sorted(rays)
        indices=[]
        for i in range(q):
            t1=sorted_rays[i][0];t2=sorted_rays[(i+1)%q][0]
            if i==q-1:t2+=2*mp.pi
            angle=(t1+t2)/2
            if mp.cos(angle)<0:indices.append(i)
        assert len(indices)==n,(n,indices)
        assert set(indices)==set((ranks[0]+t)%q for t in range(n)),(n,indices,ranks[0])
        # Distinct time-series samples are cyclic rotations of a unique mechanical word.
        bits=[]
        for i in range(q):
            bits.append([int((i+p*t)%q in indices) for t in range(q)])
        assert len({tuple(s) for s in bits})==q
        for lag in range(q):
            empirical=sum(s[0] and s[lag] for s in bits)
            d=(p*lag)%q
            predicted=max(0,n-d)+max(0,n-(q-d))
            assert empirical==predicted,(n,lag)
    print('VERIFY_OK: algebraic branch matrices, exact modular counts, high-precision boundary rays and sectors')

if __name__=='__main__':
    exact_checks();modular_checks();angular_checks()
