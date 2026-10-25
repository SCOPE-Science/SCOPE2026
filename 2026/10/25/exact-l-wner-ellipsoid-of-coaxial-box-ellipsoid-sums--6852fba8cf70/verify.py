"""Reproducible diagnostics for Löwner ellipsoids of coaxial box--ellipsoid sums.

Run: python3 verify.py. Universal correctness is established by the proof, not by sampling.
"""
import itertools
import math
import random


def solve(a, b):
    """Return kappa, unique positive contact offsets, optimal semiaxes."""
    d = len(a)
    assert d >= 2 and len(b) == d and all(t > 0 for t in a + b)
    def offsets(k):
        return [2*k*w*w/(math.sqrt(x*x+4*k*w*w)+x) for x,w in zip(a,b)]
    lo,hi=0.0,1.0
    while sum((v/w)**2 for v,w in zip(offsets(hi),b)) < 1:
        hi *= 2
    for _ in range(110):
        mid=(lo+hi)/2
        if sum((v/w)**2 for v,w in zip(offsets(mid),b)) < 1:
            lo=mid
        else:
            hi=mid
    k=(lo+hi)/2
    q=offsets(k)
    return k,q,[math.sqrt(d)*(v+w) for v,w in zip(a,q)]


def diagnostic():
    rng=random.Random(209487)
    trials=0
    for d in range(2,9):
        for _ in range(30):
            a=[10**rng.uniform(-0.9,0.9) for _ in range(d)]
            b=[10**rng.uniform(-0.9,0.9) for _ in range(d)]
            k,q,A=solve(a,b)
            assert abs(sum((v/w)**2 for v,w in zip(q,b))-1)<1.e-11
            assert all(abs(v*(x+v)/(w*w)-k)<1.e-9*max(1,k)
                       for x,v,w in zip(a,q,b))
            for eps in itertools.product((-1,1),repeat=d):
                p=[e*(v+t) for e,v,t in zip(eps,a,q)]
                assert abs(sum((v/w)**2 for v,w in zip(p,A))-1)<1.e-12
            for _ in range(70):
                z=[rng.gauss(0,1) for _ in range(d)]
                norm=math.sqrt(sum(t*t for t in z))
                frac=rng.random()
                y=[frac*t*w/norm for t,w in zip(z,b)]
                x=[rng.uniform(-v,v)+w for v,w in zip(a,y)]
                assert sum((v/w)**2 for v,w in zip(x,A))<=1+1.e-11
                t=[abs(v) for v in y]
                lhs=1-sum((v+w)**2/(d*(v+u)**2) for v,w,u in zip(a,t,q))
                rhs=(1-sum((w/v)**2 for w,v in zip(t,b)))/(d*k)
                rhs+=sum(v*(w-u)**2/(d*k*z*z*(v+u))
                         for v,w,u,z in zip(a,t,q,b))
                assert abs(lhs-rhs)<1.e-9*max(1,abs(lhs),abs(rhs))
                trials+=1
            for _ in range(70):
                direction=[rng.gauss(0,1) for _ in range(d)]
                u=[t/math.sqrt(sum(v*v for v in direction)) for t in direction]
                hK=sum(v*abs(t) for v,t in zip(a,u))
                hK+=math.sqrt(sum((v*t)**2 for v,t in zip(b,u)))
                hE=math.sqrt(sum((v*t)**2 for v,t in zip(A,u)))
                assert hE+1.e-11>=hK
                trials+=1
    for d in range(2,12):
        a=[2.0]*d; b=[1.75]*d
        _,q,A=solve(a,b)
        assert all(abs(v-(2*math.sqrt(d)+1.75))<1.e-10 for v in A)
    print('PASS:',trials,'numeric support/containment/identity tests;',
          'all sign contacts verified for 210 independent parameters')

if __name__=='__main__':
    diagnostic()
