#!/usr/bin/env python3
"""Numerical checks for priced alternating-cycle spectral-gap theorem.
Requires numpy. Analytic theorem is proved separately; these checks are finite tests only.
"""
import math, cmath, random
import numpy as np

def candidate(m,c,d):
    alpha=math.pi/m
    r=math.cos(alpha)
    den=c+d+2*r*math.sqrt(c*d)
    x=(1+r*math.sqrt(d/c))/(m*den)
    y=(1+r*math.sqrt(c/d))/(m*den)
    gap=2*math.sin(alpha)**2/(m*den)
    return x,y,gap

def laplacian(weights):
    n=len(weights)
    L=np.zeros((n,n))
    for i,w in enumerate(weights):
        j=(i+1)%n
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    return L

def test():
    rng=random.Random(64352026)
    exact=0; spectral=0; dual=0; feasible=0
    # Exact rational checks for C6 with c=1,d=4: x=2/21,y=5/84,gap=1/14.
    from fractions import Fraction as Q
    x=Q(2,21); y=Q(5,84); g=Q(1,14)
    assert 3*(x+4*y)==1
    assert (x+y-g)**2 == x*x+y*y-x*y
    exact+=2
    for m in range(2,17):
      n=2*m
      for c,d in ((1.,1.),(1.,4.),(9.,1.),(.2,7.),(15.,.007)):
        x,y,gap=candidate(m,c,d)
        w=[x if i%2==0 else y for i in range(n)]
        assert abs(m*(c*x+d*y)-1)<4.e-13
        spec=np.linalg.eigvalsh(laplacian(w))
        assert abs(spec[1]-gap)<1.e-10*max(1,gap), (m,c,d,spec[1],gap)
        spectral+=1
        alpha=math.pi/m
        rho=math.cos(alpha)
        den=c+d+2*rho*math.sqrt(c*d)
        u=math.asin(math.sqrt(c)*math.sin(alpha)/math.sqrt(den))
        v=alpha-u
        assert 0<u<alpha and v>0
        z=np.array([cmath.exp(1j*((i//2)*2*alpha+(2*u if i%2 else 0))) for i in range(n)])
        assert abs(sum(z))<1e-12*n
        assert np.linalg.norm(laplacian(w)@z-gap*z)<5e-10
        norm2=float(np.vdot(z,z).real)
        for i in range(n):
          length2=abs(z[i]-z[(i+1)%n])**2
          target=4*math.sin(alpha)**2*(c if i%2==0 else d)/den
          assert abs(length2-target)<4e-12
          dual+=1
        rng_cost=sum((c if i%2==0 else d)*r for i,r in enumerate(w))
        assert abs(rng_cost-1)<5e-13
        for rep in range(8):
          rand=[rng.expovariate(1) for _ in range(n)]
          scale=sum((c if i%2==0 else d)*r for i,r in enumerate(rand))
          rand=[r/scale for r in rand]
          val=float(np.linalg.eigvalsh(laplacian(rand))[1])
          bound=sum(rand[i]*abs(z[i]-z[(i+1)%n])**2 for i in range(n))/norm2
          assert val<=gap+1e-10 and abs(bound-gap)<5e-12, (m,c,d,val,gap,bound)
          feasible+=1
    print(f'VERIFY_OK {exact} exact-rational relations, {spectral} eigenspectra/eigenvector cases, {dual} dual edge chords, {feasible} nonuniform feasible allocations; finite checks do not certify all sizes.')
if __name__=='__main__':test()
