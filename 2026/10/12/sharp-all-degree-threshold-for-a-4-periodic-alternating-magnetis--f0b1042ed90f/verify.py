from fractions import Fraction
from math import exp, log, sinh, sqrt


def F(v, theta, k):
    return v**(k+1) - (theta+1)*v**k + (theta+1)*v - 1.0


def Ak(t,k):
    return sinh((k+1)*t)/sinh((k-1)*t)


def root_t(theta,k):
    target=theta+1.0
    lo=0.0; hi=1.0
    while Ak(hi,k) <= target:
        hi*=2.0
    for _ in range(160):
        mid=(lo+hi)/2
        if Ak(mid,k) < target: lo=mid
        else: hi=mid
    return (lo+hi)/2

# Exact critical derivatives and threshold identity, k=2..100.
for k in range(2,101):
    th=Fraction(2,k-1)
    a=th+1
    fp=Fraction(k+1)-a*k+a
    fpp=Fraction(k*(k+1))-a*k*(k-1)
    fppp=Fraction(k*(k-1)*(k+1))-a*k*(k-1)*(k-2)
    assert fp == 0
    assert fpp == 0
    assert fppp == k*(k+1)
    assert a == Fraction(k+1,k-1)

# Reconstruct representative positive branches and the source system.
cases=0
for k in (2,3,4,7,20):
    thc=2.0/(k-1)
    for delta in (1e-4, 0.02, 0.3):
        theta=thc+delta
        t=root_t(theta,k)
        for sgn in (-1,1):
            tt=sgn*t
            v=exp(2*tt)
            u=1.0; w=v
            den=theta+u**k+w**k
            rhsu=(theta*u**k+v**k+1.0)/den
            rhsv=(u**k+theta*v**k+w**k)/den
            rhsw=(1.0+v**k+theta*w**k)/den
            assert abs(u-rhsu) < 2e-10
            assert abs(v-rhsv) < 2e-10
            assert abs(w-rhsw) < 2e-10
            assert abs(F(v,theta,k)) < 5e-8
            assert abs(F(1.0/v,theta,k)) < 5e-8
        cases += 1

# Check the derived onset coefficient against small deltas; this is corroborative only.
for k in (2,3,4,7,20):
    thc=2.0/(k-1)
    A=sqrt(6.0*k*(k-1)/(k+1))
    for delta in (1e-8, 1e-7, 1e-6):
        t=root_t(thc+delta,k)
        logr=2*k*t
        rel=abs(logr/(A*sqrt(delta))-1.0)
        assert rel < 2e-4, (k,delta,rel)

# k=2 matches the source's theta=2 onset for this branch.
assert Fraction(2,2-1) == 2
print(f'VERIFY_OK exact_k=2..100 branch_cases={cases} onset_cases=15')
