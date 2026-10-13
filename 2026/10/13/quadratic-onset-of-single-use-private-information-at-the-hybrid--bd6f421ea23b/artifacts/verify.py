import math


def F(a):
    return (1.0-a*a)*math.atanh(a)-a**3


def h(x):
    return -x*math.log(x)-(1.0-x)*math.log(1.0-x)


def Delta(p,z):
    a=1.0-2.0*p
    k=1.0-a*a
    r=math.sqrt(a*a+k*z*z)
    return h((1.0+a*z)/2.0)-h((1.0+r)/2.0)


def dDelta(p,z):
    a=1.0-2.0*p
    k=1.0-a*a
    r=math.sqrt(a*a+k*z*z)
    return -a*math.atanh(a*z)+k*z*math.atanh(r)/r


def root_bisect(lo,hi,steps=180):
    assert F(lo)>0.0 and F(hi)<0.0
    for _ in range(steps):
        mid=(lo+hi)/2.0
        if F(mid)>0.0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0


def contact_point(p):
    # dDelta is negative just to the right of zero below threshold.
    lo=1e-14
    hi=0.25
    assert dDelta(p,lo)<0.0
    while dDelta(p,hi)<=0.0:
        hi*=1.5
        assert hi<0.99
    for _ in range(120):
        mid=(lo+hi)/2.0
        if dDelta(p,mid)<0.0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0


a_star=root_bisect(0.75,0.76)
p_star=(1.0-a_star)/2.0
Fp=1.0-3.0*a_star*a_star-2.0*a_star*math.atanh(a_star)
N=3.0-6.0*a_star*a_star+3.0*a_star**4-2.0*a_star**6
K=6.0*Fp*Fp/N
L=math.sqrt(-12.0*a_star*Fp/N)

assert 0.12412024820043 < p_star < 0.12412024820046
assert N>0.0 and Fp<0.0
assert abs(K-136.236236139043)<1e-9
assert abs(L-9.72830498723646)<1e-10

for delta in (1e-5,2e-5,5e-5):
    p=p_star-delta
    z=contact_point(p)
    gap=Delta(p,0.0)-Delta(p,z)
    assert gap>0.0
    assert abs(gap/(delta*delta)-K)/K < 0.002
    assert abs(z/math.sqrt(delta)-L)/L < 0.002

# Cross-check against the source's finite-grid single-use value at p=0.124102.
delta=p_star-0.124102
prediction=K*delta*delta
assert abs(prediction-4.514e-8) < 3e-10

print('a_star=%.16g' % a_star)
print('p_star=%.16g' % p_star)
print('K=%.16g' % K)
print('L=%.16g' % L)
print('VERIFY_OK')
