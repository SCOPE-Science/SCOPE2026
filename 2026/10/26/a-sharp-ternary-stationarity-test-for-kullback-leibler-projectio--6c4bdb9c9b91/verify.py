"""Reproducible rational checks for ternary moment-projection rigidity.

These finite checks are consistency tests; the theorem for every positive
reference and target distribution is established by an analytic proof.
"""
from fractions import Fraction as F
from itertools import product


def h_kl(u):
    return 1-u


def hp_kl(u):
    return -F(1)


def h_chi(u):
    return (1-u*u)/2


def hp_chi(u):
    return -u


def stationary_sum(lam, mu, h):
    xs = (-1, 0, 1)
    mean = lam[2]-lam[0]
    assert sum(lam) == sum(mu) == 1
    assert mu[2]-mu[0] == mean
    return sum(l*(x-mean)*h(p/l) for x,l,p in zip(xs,lam,mu))


def derivative_comparison(s,t,h,hprime):
    x=1+t/s
    y=1-2*t/(1-2*s)
    # derivative at epsilon=0 of stationary_sum for the tilted reference
    return (2*s-1)*(h(x)-h(y))+(t/s)*hprime(x)


def dchi(mu,q):
    return sum((p-z)**2/(2*z) for p,z in zip(mu,q))


def perturbed_reference(s,eps,t):
    lam=(s+eps/2,1-2*s,s-eps/2)
    mu=(lam[0]+t,lam[1]-2*t,lam[2]+t)
    assert all(z>0 for z in lam+mu)
    return lam,mu


count=0
for s in [F(1,12),F(1,8),F(1,6),F(1,5),F(1,4),F(1,3),F(2,5)]:
    for k in [F(1,10),F(1,5),F(1,3),F(1,2),F(4,5)]:
        t=k*(1-2*s)/2
        if not 0<t<(1-2*s)/2: continue
        assert derivative_comparison(s,t,h_kl,hp_kl)==0
        for eps in [F(-1,10),F(-1,20),F(0),F(1,20),F(1,10)]:
            if abs(eps)>=2*s:continue
            lam,mu=perturbed_reference(s,eps,t)
            assert stationary_sum(lam,mu,h_kl)==0
            count+=1
print('KL exact rational stationarity tests:',count)

count2=0
for x in [F(101,100),F(5,4),F(3,2),F(2),F(3),F(5),F(10)]:
    for y in [F(1,20),F(1,5),F(1,3),F(1,2),F(3,4),F(9,10),F(99,100)]:
        s=(1-y)/(2*(x-y));t=s*(x-1)
        assert 0<s<F(1,2) and 0<t<(1-2*s)/2
        assert x==1+t/s and y==1-2*t/(1-2*s)
        assert derivative_comparison(s,t,h_kl,hp_kl)==0
        count2+=1
print('Exact ternary parameter realization tests:',count2)

lam,mu=perturbed_reference(F(1,4),F(1,10),F(1,16))
assert lam==(F(3,10),F(1,2),F(1,5))
assert mu==(F(29,80),F(3,8),F(21,80))
stat=stationary_sum(lam,mu,h_chi)
assert stat==F(-33,5120)
mean=lam[2]-lam[0]
h=F(1,10000)
qplus=tuple(l*(1+h*(x-mean)) for x,l in zip((-1,0,1),lam))
qminus=tuple(l*(1-h*(x-mean)) for x,l in zip((-1,0,1),lam))
assert sum(qplus)==sum(qminus)==1
central=(dchi(mu,qplus)-dchi(mu,qminus))/(2*h)
assert abs(central-stat)<F(1,1000000)
print('Pearson counterexample directional derivative:',stat)
print('Finite-difference consistency error:',abs(central-stat))
print('All checks PASSED; analytic proof remains essential.')
