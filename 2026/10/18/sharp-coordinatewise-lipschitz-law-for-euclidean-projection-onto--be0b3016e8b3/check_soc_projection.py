"""Deterministic supporting checks for the sharp coordinate norm of Lorentz-cone projection.

Run with Python 3.9+ without external packages. The proof of the global
inequality and dimension cutoff is analytic; these finite tests cannot
establish those infinite/universal assertions.
"""
import math
import random
from fractions import Fraction


def projection(v):
    t, *z = v
    r = math.sqrt(sum(y*y for y in z))
    if t >= r:
        return list(v)
    if t <= -r:
        return [0.0] * len(v)
    return [(t+r)/2.0] + [(1+t/r)*y/2.0 for y in z]


def derivative(t, z):
    r = math.sqrt(sum(y*y for y in z))
    assert r > 0 and -r < t < r
    u = [y/r for y in z]
    s = t/r
    d = len(z)
    return [[0.5] + [0.5*u[j] for j in range(d)]] + [
        [0.5*u[i]] + [0.5*((1.0+s)*(1.0 if i == j else 0.0)-s*u[i]*u[j]) for j in range(d)]
        for i in range(d)
    ]


def row_max(A):
    return max(sum(abs(x) for x in row) for row in A)


def scalar(d, a):
    return (2.0+a-a*a + a*math.sqrt(d-1.0)*math.sqrt(max(0.0,1.0-a*a)))/2.0


def optimal_a(d):
    if d == 1:
        return 1.0
    def deriv(a):
        return 1-2*a + math.sqrt(d-1)*(1-2*a*a)/math.sqrt(1-a*a)
    lo, hi = 0.0, 1.0 - 1e-14
    assert deriv(lo)>0 and deriv(hi)<0
    for _ in range(120):
        mid=(lo+hi)/2
        if deriv(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def test():
    assert Fraction(89,40)**2 < Fraction(5)
    rng = random.Random(262041)
    checks=0
    for d in range(1, 16):
        Ltime=(1+math.sqrt(d))/2
        if d==1:
            Lspace=1
        else:
            a=optimal_a(d)
            Lspace=scalar(d,a)
            assert (Lspace>Ltime)==(d<=4)
            if d>=5:
                assert Ltime>Lspace
            checks+=2
        L=max(Ltime,Lspace)
        for sample in range(80):
            z=[rng.uniform(-1,1) for _ in range(d)]
            r=math.sqrt(sum(y*y for y in z))
            assert r>0
            s=rng.uniform(-0.95,0.95)
            t=s*r
            J=derivative(t,z)
            assert row_max(J)<=L+3e-12
            for i in range(d+1):
                assert abs(sum(abs(J[i][j]) for j in range(d+1))-sum(abs(J[j][i]) for j in range(d+1)))<1e-12
                checks+=1
            h=1e-6*max(1,r)
            for j in range(d+1):
                plus=[t]+z; minus=[t]+z
                plus[j]+=h; minus[j]-=h
                fplus=projection(plus); fminus=projection(minus)
                for i in range(d+1):
                    approx=(fplus[i]-fminus[i])/(2*h)
                    assert abs(approx-J[i][j])<1e-6, (d, s,i,j,approx,J[i][j])
                    checks+=1
        if d>=2:
            a=optimal_a(d)
            u=[a]+[math.sqrt((1-a*a)/(d-1))]*(d-1)
            for s in [0.99,0.999,0.999999]:
                J=derivative(s,u)
                spatialrow=sum(abs(v) for v in J[1])
                assert spatialrow>=Lspace-(1-s)*10
                checks+=1
            u=[1/math.sqrt(d)]*d
            J=derivative(0,u)
            assert abs(sum(abs(x) for x in J[0])-Ltime)<1e-12
            checks+=1
    print('OK',checks,'assertion groups')
    for d in range(1,10):
        a=optimal_a(d)
        print('spatial_dimension',d,'coordinate_lipschitz',format(max((1+math.sqrt(d))/2,scalar(d,a)) if d>1 else 1,'.10f'), 'dominant', 'spatial' if 2<=d<=4 else ('time' if d>=5 else 'equal'))

if __name__=='__main__':
    test()
