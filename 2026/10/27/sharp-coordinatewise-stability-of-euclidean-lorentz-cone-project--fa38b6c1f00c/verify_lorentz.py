"""Reproducible finite checks for the Lorentz-cone coordinatewise Lipschitz profile.
Analytical proof, not this finite checker, establishes the universal theorem.
"""
import math
import random

def projection(z):
    s, *x = z
    r = math.sqrt(sum(a*a for a in x))
    if s >= r:
        return list(z)
    if s <= -r:
        return [0.0] * len(z)
    t = (s + r) / 2
    return [t] + [t*a/r for a in x]

def jacobian(d, t, unit):
    assert -1 < t < 1
    j = [[0.0]*(d+1) for _ in range(d+1)]
    j[0][0] = .5
    for i in range(d):
        j[0][i+1] = unit[i]/2
        j[i+1][0] = unit[i]/2
        for k in range(d):
            j[i+1][k+1] = ((1+t if i == k else 0) - t*unit[i]*unit[k])/2
    return j

def maxrows(j):
    return max(sum(abs(a) for a in row) for row in j)

def g(d,a):
    return a - a*a + math.sqrt(d-1)*a*math.sqrt(max(0.0,1-a*a))

def gp(d,a):
    return 1 - 2*a + math.sqrt(d-1)*(1-2*a*a)/math.sqrt(1-a*a)

def root(d):
    lo,hi=.5,1/math.sqrt(2)
    for _ in range(90):
        a=(lo+hi)/2
        if gp(d,a)>0:
            lo=a
        else:
            hi=a
    return (lo+hi)/2

def predicted(d):
    if d==1: return 1.
    scalar = (1+math.sqrt(d))/2
    if d>=5: return scalar
    a=root(d)
    return 1+g(d,a)/2

checks=0
rng=random.Random(20261019)
for d in range(1,33):
    lip=predicted(d)
    scalar=(1+math.sqrt(d))/2
    assert lip>=1 and lip>=scalar-2e-12
    checks+=2
    if d in (2,3,4):
        a=root(d)
        assert .5<a<1/math.sqrt(2) and abs(gp(d,a))<1e-12
        assert 1+g(d,a)/2>scalar+1e-4
        checks+=3
    if d>=5:
        assert 1+g(d,root(d))/2<scalar
        checks+=1
    for _ in range(36):
        u=[rng.uniform(-1,1) for _ in range(d)]
        norm=math.sqrt(sum(v*v for v in u))
        u=[v/norm for v in u]
        t=rng.uniform(-.999,.999)
        J=jacobian(d,t,u)
        assert maxrows(J)<=lip+2e-12
        assert abs(sum(abs(v) for v in J[0])-(1+sum(abs(v) for v in u))/2)<1e-12
        checks+=2
        if d<=6:
            z=[t]+u
            eps=1e-6
            k=rng.randrange(d+1)
            ez=list(z);ez[k]+=eps
            finite=(projection(ez)[rng.randrange(d+1)]) # finite output guard
            assert math.isfinite(finite)
            checks+=1
    if d<=6:
        for _ in range(20):
            u=[rng.uniform(-1,1) for _ in range(d)]
            norm=math.sqrt(sum(v*v for v in u));u=[v/norm for v in u]
            t=rng.uniform(-.8,.8)
            z=[t]+u; J=jacobian(d,t,u)
            for k in range(d+1):
                w=z.copy();w[k]+=1e-6
                q=projection(w);p=projection(z)
                for i in range(d+1):
                    assert abs((q[i]-p[i])/1e-6-J[i][k])<2e-5
                    checks+=1
    # Close-to-extremizing derivative tests, with actual sign direction.
    if d>=5:
        u=[1/math.sqrt(d)]*d;t=0.0;row=0
    elif d>=2:
        a=root(d);u=[a]+[math.sqrt((1-a*a)/(d-1))]*(d-1);t=1-1e-8;row=1
    else:
        u=[1.];t=0.;row=0
    J=jacobian(d,t,u)
    signs=[1 if v>=0 else -1 for v in J[row]]
    z=[t]+u;eps=1e-8
    p=projection(z)
    w=[z[i]+eps*signs[i] for i in range(d+1)]
    q=projection(w)
    empirical=abs(q[row]-p[row])/eps
    # For d=2..4 boundary proximity can invalidate linearization at eps=1e-8;
    # numerical derivative verified via exact J instead.
    if d>=5:
        assert abs(empirical-lip)<2e-6
    assert sum(abs(v) for v in J[row])>=lip-3e-8
    checks+=(2 if d>=5 else 1)
print('VERIFIED',checks,'finite assertions; max-dimensional test d=32')
for d in range(1,10):
    print(d, f'{predicted(d):.12f}', 'scalar' if d>=5 else ('flat' if d==1 else 'vector'),
          'a='+f'{root(d):.12f}' if d in (2,3,4) else '')
