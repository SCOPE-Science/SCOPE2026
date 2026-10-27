"""Reproducible numerical and exact checks for staircase information identities.
Standard library only; this is not a proof of asymptotic statements.
"""
from fractions import Fraction
from math import log, sqrt, exp
from random import Random


def minimum_expectation(p, i):
    return (1-(1-p)**(i+1))/Fraction(i+1)


def mean_jumps(p, n):
    return sum(minimum_expectation(p, i) for i in range(n))


def explicit_mean_jumps(p, n):
    return sum((1-(1-p)**j)/Fraction(j) for j in range(1, n+1))


def exact_second_moment(p, i):
    # 2 integral_0^p y (1-y)^i dy
    q = 1-p
    return 2*(Fraction(1, (i+1)*(i+2))-q**(i+1)/Fraction(i+1)+q**(i+2)/Fraction(i+2))


def stationary_score_expectation(p, x):
    # Jump conditional density p dy, stay atom probability 1-p*x
    return (p*x)/p - (1-p*x)*x/(1-p*x)


def score_conditional_second(p, x):
    return (p*x)/p**2 + (1-p*x)*x**2/(1-p*x)**2


def info_increment(p, x):
    return x/(p*(1-p*x))


def test_exact():
    checks = 0
    for p in [Fraction(1,5), Fraction(2,5), Fraction(3,4)]:
        for n in range(1, 15):
            assert mean_jumps(p,n) == explicit_mean_jumps(p,n)
            checks += 1
        for i in range(0, 15):
            assert Fraction(0) <= exact_second_moment(p,i) <= Fraction(2, (i+1)*(i+2))
            checks += 1
        for x in [Fraction(1,7), Fraction(1,2), Fraction(6,7),Fraction(1)]:
            assert stationary_score_expectation(p,x)==0
            assert score_conditional_second(p,x)==info_increment(p,x)
            checks += 2
    return checks


def simulate(p, n, reps=120):
    rng=Random(73921+n)
    means=[]; scores=[]; informations=[]
    for _ in range(reps):
        x=1.0; count=0; score=0.0; info=0.0
        for i in range(n):
            prob=p*x
            info+=x/(p*(1-prob))
            if rng.random()<prob:
                # conditional jump magnitude uniform on (0,x)
                x*=rng.random()
                score+=1/p
                count+=1
            else:
                score-=x/(1-prob)
        means.append(count); scores.append(score*p/sqrt(log(n))); informations.append(info*p*p/log(n))
    return (n, sum(means)/reps, sum(scores)/reps, sum(z*z for z in scores)/reps, sum(informations)/reps)


if __name__=='__main__':
    nchecks=test_exact()
    print('PASS exact rational identities:',nchecks)
    for row in [simulate(.4,n) for n in (2000,12000)]:
        print('n, mean jumps, normalized score mean, normalized score second moment, normalized bracket mean:',tuple(round(float(z),4) for z in row))
    print('Finite simulations do not establish the distributional limits.')
