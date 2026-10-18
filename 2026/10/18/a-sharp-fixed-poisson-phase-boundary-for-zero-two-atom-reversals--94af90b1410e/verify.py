"""Exact-arithmetic checks for Poisson-plus-Bernoulli zero/two atom comparisons.

The executable tests finite instances only. The uniform statements require
and receive the analytic arguments in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def ratio(lam, probabilities):
    odds = [p / (1-p) for p in probabilities]
    return lam*lam/2 + lam*sum(odds,F(0)) + sum((odds[i]*odds[j] for i in range(len(odds)) for j in range(i+1,len(odds))),F(0))


def critical_mean(lam):
    c = 1-lam*lam/2
    return c/(lam+c)


checks = 0
for denom in (6,8,10):
    choices = [F(i,denom) for i in range(denom)]
    for m in (1,2,3,4):
        for ps in product(choices,repeat=m):
            alpha = sum(ps,F(0))
            if alpha >= 1 or alpha == 0:
                continue
            g = (1-alpha)/(2-alpha)
            tests = [F(0),g/2,g,g+F(1,7),F(1),F(5,4)]
            for lam in tests:
                actual = ratio(lam,ps)
                envelope = lam*lam/2 + lam*alpha/(1-alpha)
                if lam >= g:
                    assert actual <= envelope, (ps,lam,actual,envelope)
                    if lam > g and sum(p>0 for p in ps)>1:
                        assert actual < envelope
                    if lam == g:
                        assert (actual==envelope)==(sum(p>0 for p in ps)<=2)
                checks += 1

for denom in (4,6,8,10,12):
    for a in range(1,denom):
        alpha=F(a,denom)
        g=(1-alpha)/(2-alpha)
        x=alpha/3
        y=alpha-x
        assert ratio(g/2,[x,y]) > ratio(g/2,[alpha])
        assert ratio(g,[x,y]) == ratio(g,[alpha])
        checks += 2

for lam in (F(1,10),F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(7,5)):
    if lam*lam>=2:continue
    alpha=critical_mean(lam)
    assert 0<alpha<1
    assert ratio(lam,[alpha])==F(1)
    assert lam > (1-alpha)/(2-alpha)
    for smaller in (F(0),alpha/4,alpha/2,alpha*F(9,10)):
        assert ratio(lam,[smaller])<1
    for greater in (alpha+(1-alpha)/10,alpha+(1-alpha)/2):
        assert ratio(lam,[greater])>1
    checks+=9

# Exact rational version of the pair-merging identity, with other coins.
for den in (11,13):
    for i in range(1,den-1):
        for j in range(1,den-i):
            x,y=F(i,den),F(j,den)
            delta=(x/(1-x))*(y/(1-y))*(2-x-y)/(1-x-y)
            assert (x+y)/(1-x-y)-x/(1-x)-y/(1-y)==delta
            checks+=1

print(f"PASS: {checks} exact rational assertions; finite checks supplement analytic proof")
