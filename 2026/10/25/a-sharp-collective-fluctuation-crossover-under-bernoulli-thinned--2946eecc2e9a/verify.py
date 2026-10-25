"""Independent checks for the Bernoulli-thinned common-reset Brownian gas.
Run with Python 3: python verify.py. No third-party dependencies.
"""
from fractions import Fraction as F
from math import exp, sqrt, log
from random import Random

count = 0

def check(condition, message):
    global count
    if not condition:
        raise AssertionError(message)
    count += 1

for q in [F(1), F(1,2), F(1,4), F(1,10), F(7,8)]:
    v = q/(2-q)
    # Generator: 0=2D-rq E[X^2], 0=12D E[X^2]-rq E[X^4].
    D, r = F(3,2), F(5,3)
    e2 = 2*D/(r*q)
    e4 = 12*D*e2/(r*q)
    joint = 4*D*e2/(r*q*(2-q))
    check(2*D-r*q*e2 == 0, 'second stationary moment')
    check(12*D*e2-r*q*e4 == 0, 'fourth stationary moment')
    check(4*D*e2-r*q*(2-q)*joint == 0, 'cross stationary moment')
    check((r*q/(2*D))**2*(e4-e2**2) == 5, 'marginal square variance')
    check((r*q/(2*D))**2*(joint-e2**2) == v, 'pair square covariance')
    for n in [1,2,3,8,19,100]:
        exact = F(5,n)+(1-F(1,n))*v
        other = v+(5-v)/n
        check(exact==other, 'finite-size variance identity')
    for k in [1,2,3,4,5]:
        # iid Exp(1) perpetuity with geometric weights: cumulant k.
        from math import factorial
        cumulant = F(factorial(k-1))*q**k/(1-(1-q)**k)
        check(cumulant>0, 'positive perpetuity cumulant')

# Brownian generator eigenfunction test for the stationary two-particle CF.
for q in [F(1),F(1,2),F(1,5)]:
    for k2,l2 in [(F(0),F(0)),(F(1),F(0)),(F(1,2),F(2))]:
        D,r=F(1),F(2)
        a = r*q/(r*q+D*k2)
        b = r*q/(r*q+D*l2)
        joint = r*(q*(1-q)*(a+b)+q*q)/(D*(k2+l2)+r*q*(2-q))
        # Stationarity: diffusion + partial resets of either/both.
        check((D*(k2+l2)+r*q*(2-q))*joint == r*(q*(1-q)*(a+b)+q*q), 'characteristic equation')
        if l2==0:
            check(joint==a,'marginal characteristic function')

# Truncated series variance and Laplace product at q=1/4.
q=F(1,4)
weights=[q*(1-q)**j for j in range(200)]
check(abs(float(sum(weights))-1)<1e-15,'weight normalization')
check(abs(float(sum(x*x for x in weights))-float(q/(2-q)))<1e-15,'weighted variance')

rng=Random(417)
q=.25
reps=5000
vals=[]
for _ in range(reps):
    w=q
    v=0.0
    for k in range(115):
        v += w*(-log(max(rng.random(),1e-15)))
        w *= 1-q
    vals.append(v)
mean=sum(vals)/reps
var=sum((x-mean)**2 for x in vals)/reps
check(abs(mean-1)<.04, 'perpetuity simulated mean sanity check')
check(abs(var-q/(2-q))<.03, 'perpetuity simulated variance sanity check')
print(f'PASS {count} exact and numerical checks; Monte Carlo mean={mean:.4f}, variance={var:.4f}')
