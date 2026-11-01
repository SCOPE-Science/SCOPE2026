"""Reproducible finite checks of a shifted-cube hyperplane-section formula.
Only numerical checks; the accompanying proof establishes universal assertions.
"""
import math
import random
from itertools import product


def formula(n, t):
    assert n >= 3 and 0 <= t <= 1
    r = math.sqrt(n - 1)
    a = math.atan((1 - t)/r) + math.atan((1 + t)/r)
    def f(v):
        return math.atan(1/math.sqrt(n - 2 + v*v))
    return 2**(n - 1)/math.pi * (a + (n - 1)*(f(1-t) + f(1+t)))


def independent_edge_angle_sum(n,t):
    # Independent oriented-vector angle calculation over every cube edge.
    val = 0.0
    for j in range(n):
        for fixed in product((-1.0,1.0),repeat=n-1):
            v=list(fixed);v.insert(j,1.0)
            w=list(fixed);w.insert(j,-1.0)
            v[0]-=t;w[0]-=t
            dot=sum(a*b for a,b in zip(v,w))
            la=math.sqrt(sum(a*a for a in v))
            lb=math.sqrt(sum(b*b for b in w))
            val+=math.acos(max(-1.0,min(1.0,dot/(la*lb))))/math.pi
    return val


def independent_gaussian_mc(n,t,samples=25000):
    # Normalizing the Gaussian normals is unnecessary: only signs matter.
    rng=random.Random(24569 + n*100 + round(100*t))
    score=0
    for _ in range(samples):
        g=[rng.gauss(0,1) for i in range(n)]
        threshold=t*g[0]
        for j in range(n):
            fixed_sum=sum(abs(g[k]) for k in range(n) if k!=j)
            # For small n, explicitly enumerate all signs; no reliance on formula.
            for signs in product((-1,1),repeat=n-1):
                z=sum(s*g[k] for s,k in zip(signs,(i for i in range(n) if i!=j)))
                if abs(z-threshold)<abs(g[j]):score+=1
    return score/samples


def main():
    checks=0
    for n in (3,4,5,6,7):
        for t in (0.,.1,.3,.5,.7,.95,1.):
            f=formula(n,t)
            a=independent_edge_angle_sum(n,t)
            assert abs(f-a)<1e-10,(n,t,f,a)
            checks+=1
        assert all(formula(n,i/100)>formula(n,(i+1)/100) for i in range(100))
        checks+=100
        assert abs(formula(n,0)-2**n*n/math.pi*math.asin(1/math.sqrt(n)))<1e-11
        checks+=1
    for n,t in ((3,0.),(3,.5),(3,1.),(4,.25),(4,.8),(5,.5)):
        empirical=independent_gaussian_mc(n,t,25000)
        exact=formula(n,t)
        assert abs(empirical-exact)<.14,(n,t,empirical,exact)
        checks+=1
    # Exact rational positivity check for the comparison polynomial at sample integers.
    for c in range(2,21):
        for j in range(101):
            t=j/100
            expression=c**3+2*c*c-2*c-4+(6*c+6)*t*t-3*c*t**4-2*t**6
            assert expression>0
            checks+=1
    for n in (50,100,200,500):
        for t in (.1,.4,.8,1.):
            lhs=math.pi*math.sqrt(n)/2**(n-1)*(formula(n,0)-formula(n,t)) if n<500 else 0
            if n<500:
                assert abs(lhs-t*t)<.05,(n,t,lhs)
                checks+=1
    print('PASS',checks,'deterministic checks; MC uses independent normal sign events.')

if __name__=='__main__':main()
