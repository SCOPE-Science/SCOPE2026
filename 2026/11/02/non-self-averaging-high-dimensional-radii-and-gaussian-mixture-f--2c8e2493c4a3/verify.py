#!/usr/bin/env python3
"""Standalone reproducibility checks for the stationary radial limit theorem.
Uses only the Python standard library.  Finite tests support, not replace, proof.
"""
from fractions import Fraction as F
import random, math

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

# Two independent expressions for the fourth moment: the GEM decomposition
# and the stationary Markov generator (in dimensionless units).
for alpha in [F(1, 3), F(1, 2), F(1), F(3, 2), F(2), F(4), F(10)]:
    s1 = 1/(alpha+1)
    s2 = (alpha+6)/((alpha+1)*(alpha+2)*(alpha+3))
    t4 = 6/((alpha+1)*(alpha+2)*(alpha+3))
    cross = alpha/((alpha+1)*(alpha+2)*(alpha+3))
    ev2 = 2/((alpha+1)*(alpha+2))
    er2 = alpha/(alpha+2)
    ev4 = 24/((alpha+1)*(alpha+2)*(alpha+3)*(alpha+4))
    er4 = alpha/(alpha+4)
    ev2r2 = 2*alpha/((alpha+2)*(alpha+3)*(alpha+4))
    check(ev2/(1-er2) == s1, 'GEM first moment')
    check((ev4+2*ev2r2*s1)/(1-er4) == s2, 'GEM second homozygosity moment')
    check(ev4/(1-er4) == t4, 'GEM fourth-weight moment')
    check(s2-t4 == cross, 'off-diagonal GEM moment')
    check(s2-s1*s1 == 2*alpha/((alpha+1)**2*(alpha+2)*(alpha+3)), 'nonzero variance')
    for d in [1, 2, 3, 4, 7, 16, 128]:
        d=F(d)
        fourth_generator = (alpha+6+2*alpha/d)/((alpha+1)*(alpha+2)*(alpha+3))
        fourth_sphere = s2 + 2*cross/d
        check(fourth_generator == fourth_sphere, 'generator vs spheres 4th moment')
        check(fourth_sphere-s1*s1 == (s2-s1*s1)+2*cross/d, 'exact radial variance')
        check(d * (fourth_generator-s2) == 2*cross, 'sharp mean-square fluctuation constant')
    check((s2 + cross) - s1*s1 == alpha/((alpha+1)**2*(alpha+2)), 'd=2 beta law crosscheck')

# Exact edge squeeze. For alpha=1 the probability of any GEM weight
# exceeding 1-delta is -log(1-delta) for delta<1/2.
for j in range(2, 20):
    epsilon = 2.0**(-j)
    lower_delta = epsilon/2
    upper_delta = (1-math.sqrt(1-2*epsilon))/2
    lower = -math.log1p(-lower_delta)
    upper = -math.log1p(-upper_delta)
    check(lower <= upper, 'edge event squeeze')
    check(lower/(epsilon/2) >= 1, 'lower leading constant')
    check(upper/(epsilon/2) > 1, 'upper leading constant')
    if j >= 11:
        check(abs(upper/(epsilon/2)-1) < 3*epsilon, 'asymptotic leading constant')

rng = random.Random(20261027)
def stick(alpha, cutoff=2e-12):
    pieces=[]
    rem=1.0
    while rem>cutoff:
        v=1-rng.random()**(1.0/alpha)
        w=rem*v
        pieces.append(w)
        rem *= 1-v
        if len(pieces)>10000:
            raise RuntimeError('unexpected stick length')
    # Since rem <= cutoff, omitted contribution to squared radius is <=2*cutoff.
    return pieces

def radial_sq(d, weights):
    z=[0.0]*d
    for w in weights:
        u=[rng.gauss(0,1) for _ in range(d)]
        inv=1/math.sqrt(sum(t*t for t in u))
        for k in range(d): z[k]+=w*u[k]*inv
    return sum(v*v for v in z)

alpha=1.7
for d,n in [(2,3000),(12,2000),(64,900)]:
    qq=[radial_sq(d,stick(alpha)) for _ in range(n)]
    mean=sum(qq)/n
    var=sum((x-mean)**2 for x in qq)/n
    expected_mean=1/(alpha+1)
    expected_var=2*alpha/((alpha+1)**2*(alpha+2)*(alpha+3))*(1+(alpha+1)/d)
    check(abs(mean-expected_mean)<0.035,'direct stochastic stationary radial mean')
    check(abs(var-expected_var)<0.020,'direct stochastic stationary radial variance')

# Independent fixed-weight conditional sphere fluctuations.
weights=[.45,.30,.20,.05]
d=256
n=1900
s=sum(w*w for w in weights)
t=sum(w**4 for w in weights)
delta=[]
for _ in range(n): delta.append(math.sqrt(d)*(radial_sq(d,weights)-s))
avg=sum(delta)/n
var=sum((v-avg)**2 for v in delta)/n
check(abs(avg)<0.045,'conditional CLT centered')
check(abs(var-2*(s*s-t))<0.033,'conditional Gaussian-mixture variance')
print('PASS:',checks,'finite exact/numeric assertions')
