"""Independent finite-mixing and small-transmissibility threshold checks.

Run with `python verify_threshold.py`; standard library only.
"""
from math import exp, log, sqrt, isclose
from fractions import Fraction
from itertools import product


def mixing(p, h):
    return [[(1-h)*(1-p)+h, (1-h)*p],
            [(1-h)*(1-p), (1-h)*p+h]]


def radius2(m):
    trace = m[0][0]+m[1][1]
    det = m[0][0]*m[1][1]-m[0][1]*m[1][0]
    return (trace+sqrt(max(0.0, trace*trace-4*det)))/2


def finite_radius(p, h, susceptibility, infectivity, t):
    mix = mixing(p,h)
    rates = [[1, infectivity], [susceptibility, susceptibility*infectivity]]
    return radius2([[mix[i][j]*(1-exp(-rates[i][j]*t)) for j in range(2)] for i in range(2)])


def leading_radius(p, h, susceptibility, infectivity):
    mix = mixing(p,h)
    rates = [[1, infectivity], [susceptibility, susceptibility*infectivity]]
    return radius2([[mix[i][j]*rates[i][j] for j in range(2)] for i in range(2)])


def exact_threshold(kappa, p, h, susceptibility, infectivity):
    lo, hi = 0., 1.
    while kappa*finite_radius(p,h,susceptibility,infectivity,hi)<1:
        hi *=2
    for _ in range(85):
        mid=(lo+hi)/2
        if kappa*finite_radius(p,h,susceptibility,infectivity,mid)<1: lo=mid
        else: hi=mid
    return (lo+hi)/2

checks=0
for p,h,aa,ii in product((.1,.4,.8), (0.,.2,.6,.9,1.), (1.,1.3,2.), (1.,1.5,3.)):
    alpha=aa*ii
    a=1-p+alpha*p
    b=p+alpha*(1-p)
    theta=a+b*h
    r=(theta+sqrt(max(0.,theta*theta-4*alpha*h)))/2
    assert isclose(r,leading_radius(p,h,aa,ii),rel_tol=1e-12,abs_tol=1e-12)
    assert 1-1e-12 <=theta/r<=2+1e-12
    if h>0: assert theta/r>1+1e-10 or (alpha==1 and h>0)
    for kappa in (20,100,400):
        t=exact_threshold(kappa,p,h,aa,ii)
        assert abs(kappa*finite_radius(p,h,aa,ii,t)-1)<3e-12
        assert t>1/(kappa*theta)
        if kappa==400:
            assert abs(kappa*t*r-1)<0.012
        checks+=4
    if alpha==1:
        for kappa in (10,100):
            t=exact_threshold(kappa,p,h,aa,ii)
            assert isclose(t,-log(1-1/kappa),rel_tol=1e-11)
            checks+=1
# Exact polynomial identities over rationals; avoids relying on eigensolver.
for p,h,alpha in product((Fraction(1,3),Fraction(2,5)),(Fraction(0),Fraction(1,4),Fraction(3,4),Fraction(1)),(Fraction(1),Fraction(3),Fraction(5))):
    pi=mixing(p,h)
    determinant=pi[0][0]*pi[1][1]-pi[0][1]*pi[1][0]
    a=1-p+alpha*p; b=p+alpha*(1-p)
    assert determinant==h
    assert a*b-alpha==p*(1-p)*(alpha-1)**2
    assert pi[0][0]+alpha*pi[1][1]==a+b*h
    checks+=3
# Source neutral-case approximation predicts supercriticality at this value;
# the original linearized multitype kernel remains subcritical.
for kappa in (2,10,100,10000):
    t=3/(4*kappa)
    assert kappa*(1+1)*t>1
    assert kappa*finite_radius(.4,1.,1.,1.,t)<1
    checks+=2
print(f"PASS {checks} comparisons; exact rational identities, 405 model-grid parameter sets, and critical roots checked")

# Independent regression of the finite-excess-degree near-segregation crossover.
def crossover_weight(p,q,tau):
    return (q-tau+sqrt((q-tau)**2+4*p*q*tau))/2

for kappa,p,tau,s in product((2.,6.,30.),(.2,.65),(0.,.3,1.,3.,8.),(.25,.7)):
    t0=log(kappa/(kappa-1)); q0=(kappa-1)*t0
    g=crossover_weight(p,q0,tau)
    assert p*q0-1e-14<=g<=q0+1e-14
    for delta in (.004,.002):
        actual=exact_threshold(kappa,p,1-tau*delta,(1+delta)**s,(1+delta)**(1-s))
        predicted=t0-delta*g/(kappa-1)
        assert abs(actual-predicted)<10*delta*delta
        checks+=2

# At any fixed nonmaximal assortativity, the first-order derivative is -p*t0.
for kappa,p,h,s in product((2.,6.,30.),(.2,.65),(0.,.3,.8),(.25,.7)):
    t0=log(kappa/(kappa-1)); delta=1e-5
    actual=exact_threshold(kappa,p,h,(1+delta)**s,(1+delta)**(1-s))
    assert abs((actual-t0)/delta+p*t0)<4e-4
    checks+=1
print(f"PASS extended; total checks {checks}, crossover scaling and fixed-h limits")
