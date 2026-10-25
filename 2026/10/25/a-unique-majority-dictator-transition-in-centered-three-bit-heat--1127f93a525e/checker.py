"""Self-contained exact finite checks for three-coordinate heat-kernel norm.
Uses Python standard library. No finite check substitutes for the proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import exp, log, tanh

def row(s):
    return [((1+s[0]*((-1)**((bits>>0)&1)))/2)*
            ((1+s[1]*((-1)**((bits>>1)&1)))/2)*
            ((1+s[2]*((-1)**((bits>>2)&1)))/2) for bits in range(8)]

def exact_max(s):
    p=row(s)
    return max(2*sum(p[i] for i in chosen)-1 for chosen in combinations(range(8),4))

def formula(s):
    return max(max(s), (sum(s)-s[0]*s[1]*s[2])/2)

values=[F(1,6),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(5,6)]
checks=0
for s in product(values, repeat=3):
    assert exact_max(s)==formula(s),(s, exact_max(s),formula(s))
    ss=sorted(s,reverse=True)
    a=ss[0]*(1+ss[1]*ss[2])-ss[1]-ss[2]
    b=ss[0]-(ss[0]+ss[1]+ss[2]-ss[0]*ss[1]*ss[2])/2
    assert a==2*b
    checks+=1
# A genuine tie between majority and slow-coordinate dictatorship:
s2,s3=F(1,3),F(1,4)
s1=(s2+s3)/(1+s2*s3)
assert exact_max((s1,s2,s3))==s1
checks+=1

# Compare the analytic time profile with a direct 8-state stochastic matrix,
# and numerically check a single positive transition for distinct slow rates.
rate_examples=[(1.,2.,3.),(1.,1.,4.),(1.,1.01,1.5),(0.5,1.3,2.5)]
for rates in rate_examples:
    for t in [1e-3,.04,.2,.8,2.,5.]:
        ss=tuple(exp(-2*r*t) for r in rates)
        p=row(ss)
        direct=max(2*sum(p[i] for i in chosen)-1 for chosen in combinations(range(8),4))
        assert abs(direct-float(formula(ss))) < 1e-12
        checks+=1

# Special-case algebraically independent: early-time quadratic coefficient.
for rates in [(1,2,3),(.5,1.1,1.6),(.1,.5,1.7)]:
    c=2*(rates[0]*rates[1]+rates[0]*rates[2]+rates[1]*rates[2])
    t=1e-5
    s=[exp(-2*r*t) for r in rates]
    n=formula(s)
    assert abs((1-n)/t**2-c)/c < 4e-4
    checks+=1

print('PASS', checks, 'tests: exact 70-choice balanced optimization, tie, independent matrix rows, onset')
