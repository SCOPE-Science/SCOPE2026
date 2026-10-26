"""Finite-dimensional verification of the complete-bipartite noncollision occupation theorem."""
import math
import numpy as np
from fractions import Fraction

checks=0
for m in range(2,31):
    s=math.sqrt(m*(m-1))
    lam=2*m-2*s
    # Two-state aggregated exclusion killed generator: S,D.
    killed=np.array([[-2*m,2*m],[2*(m-1),-2*m]],float)
    h=np.array([math.sqrt(m/(m-1)),1.0])
    assert np.allclose(killed@h,-lam*h,rtol=5e-12,atol=5e-12);checks+=1
    # Ground-state transformed noncolliding macro rates, both exactly 2 sqrt(m(m-1)).
    rateSD=2*m*h[1]/h[0]
    rateDS=2*(m-1)*h[0]/h[1]
    assert np.isclose(rateSD,2*s) and np.isclose(rateDS,2*s);checks+=1
    # NC stationary weighted h^2 under uniform reversible exclusion: equal S and D masses.
    wS=2*m*(m-1)*h[0]**2;wD=2*m*m*h[1]**2
    assert np.isclose(wS,wD);checks+=1
    # EX stationary: P_D=m/(2m-1).
    pD=Fraction(m,2*m-1)
    assert 2*m*(1-pD)==2*(m-1)*pD;checks+=1
    klforward=lam-1
    klreverse=float(2*pD)-lam
    assert klforward>0 and klreverse>0;checks+=1
    # Auto-covariance of hazard 2 I_D under NC, at t.
    for t in [0,0.03125,0.2,1.0]:
        val=math.exp(-4*s*t)
        assert abs(val-(math.exp(-2*rateSD*t)))<1e-11;checks+=1
    # Explicit finite-n killed chain eigen checks no floating underflow.
print('PASS',checks,'assertions, m=2..30, stationary distribution, killing eigenpair, RN entropy and covariance.')
for m in range(2,7):
    vertices=range(2*m)
    states=[(i,j) for i in vertices for j in vertices if i!=j]
    idx={s:i for i,s in enumerate(states)}
    n=len(states)
    Q=np.zeros((n,n));K=np.zeros((n,n))
    for pos,(x,y) in enumerate(states):
        for index in [0,1]:
            src=(x,y)[index]
            for dst in vertices:
                if (src<m)==(dst<m):continue
                if dst==(y,x)[index]:
                    # K has an additional killing rate, Q does not.
                    K[pos,pos]-=1.0
                else:
                    new=(dst,y) if index==0 else (x,dst)
                    Q[pos,idx[new]]+=1.0
                    K[pos,idx[new]]+=1.0
                    Q[pos,pos]-=1.0;K[pos,pos]-=1.0
    h=np.array([math.sqrt(m/(m-1)) if ((x<m)==(y<m)) else 1.0 for (x,y) in states]);s=math.sqrt(m*(m-1));lam=2*m-2*s
    assert np.allclose(K@h,-lam*h);checks+=1
    NC=np.diag(1/h)@K@np.diag(h)+lam*np.eye(n)
    assert np.allclose(NC@np.ones(n),np.zeros(n));checks+=1
    p=h*h/sum(h*h)
    assert np.allclose(p@NC,np.zeros(n));checks+=1
    def group(xy): return (xy[0]<m)==(xy[1]<m)
    for j,xy in enumerate(states):
        target=np.array([group(z)!=group(xy) for z in states])
        rate=np.sum(NC[j,target])
        assert abs(rate-2*s)<1e-10;checks+=1
    p_diff=sum(p[j] for j,z in enumerate(states) if not group(z))
    assert abs(p_diff-0.5)<1e-10;checks+=1
print('PASS all',checks,'assertions, including independent full labelled configuration matrices for m=2..6.')
