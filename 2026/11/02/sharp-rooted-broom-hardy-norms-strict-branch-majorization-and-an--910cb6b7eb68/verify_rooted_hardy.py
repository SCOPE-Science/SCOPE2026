"""Standalone numerical cross-checks for rooted metric-broom Hardy norms.

Requires Python 3.9+ standard library only. Analytical assertions of the theorem
are proven independently in its accompanying mathematical text.
"""
import math
import random


def root(a, branches):
    assert a > 0 and len(branches) >= 2 and min(branches) > 0
    hi = min(math.pi/(2*a), *(math.pi/(2*b) for b in branches))
    lo = 0.0
    for _ in range(90):
        k = (lo+hi)/2
        f = 1/math.tan(a*k) - sum(math.tan(k*b) for b in branches)
        if f > 0: lo=k
        else: hi=k
    return (lo+hi)/2


def hnorm(a,branches):return 1/root(a,branches)


def energy_ratio(a,branches,k):
    t=k*a
    I=a/2-math.sin(2*t)/(4*k)
    E=k*k*(a/2+math.sin(2*t)/(4*k))
    for b in branches:
        v=math.sin(t)/math.cos(k*b)
        I+=v*v*(b/2+math.sin(2*k*b)/(4*k))
        E+=v*v*k*k*(b/2-math.sin(2*k*b)/(4*k))
    return E/I

rng=random.Random(52124)
cases=0
for m in range(2,9):
    for _ in range(36):
        a=0.1+rng.random()*3
        branches=[0.08+rng.random()*2 for _ in range(m)]
        k=root(a,branches)
        assert abs(energy_ratio(a,branches,k)-k*k) < 1e-10*max(1,k*k)
        B=sum(branches)
        equal=[B/m]*m
        assert hnorm(a,equal)<=hnorm(a,branches)+2e-12
        assert hnorm(a,branches)< 2*(a+B)/math.pi+1e-9
        # One Robin Hood transfer makes unequal lengths more balanced.
        i=max(range(m),key=lambda j:branches[j])
        j=min(range(m),key=lambda j:branches[j])
        if branches[i]-branches[j] > 1e-6:
            x=min((branches[i]-branches[j])/4,0.001)
            balanced=branches[:];balanced[i]-=x; balanced[j]+=x
            assert hnorm(a,balanced)<hnorm(a,branches)+3e-12
        cases+=1
print('POSITIVE_GROUND_STATE_ENERGY_AND_MAJORIZATION_OK',cases)

stable=0
for m in (2,3,5,10):
    a=0.3+0.37*m
    B=0.75+0.17*m
    b=B/m
    k0=root(a,[b]*m)
    D=a/(math.sin(k0*a)**2)+m*b/(math.cos(k0*b)**2)
    C=(1/math.cos(k0*b)**2)*math.tan(k0*b)/D
    eps=3e-4*b
    bs=[b+eps,b-eps]+[b]*(m-2)
    obs=(hnorm(a,bs)-hnorm(a,[b]*m))/(2*eps*eps)
    assert abs(obs/C-1)<0.004, (m,C,obs)
    stable+=1
print('QUADRATIC_EQUAL_BRANCH_STABILITY_OK',stable)

limit=0
for a,B in ((1.,2.),(0.25,4.),(3.,0.7)):
    lo=0.;hi=math.pi/(2*a)
    for _ in range(90):
        k=(lo+hi)/2
        if 1/math.tan(a*k)>B*k:lo=k
        else:hi=k
    kinf=(lo+hi)/2
    D=a/(math.sin(kinf*a)**2)+B
    coeff=kinf*B**3/(3*D)
    for m in (100,200,400):
        val=hnorm(a,[B/m]*m)
        assert abs((val-1/kinf)*m*m/coeff-1)<0.02
        limit+=1
print('INFINITE_BRANCH_ENDPOINT_MASS_ASYMPTOTIC_OK',limit)
print('ALL_ROOTED_METRIC_TREE_HARDY_CHECKS_OK')
