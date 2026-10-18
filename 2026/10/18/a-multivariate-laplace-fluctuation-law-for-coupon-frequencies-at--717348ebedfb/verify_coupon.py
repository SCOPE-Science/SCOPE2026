#!/usr/bin/env python3
"""Reproducible numerical checks for coupon-completion occupancy fluctuations.
No data files, networking, or nonstandard packages are required.
"""
import math, random, statistics
from fractions import Fraction


def harmonic(n):
    return sum(Fraction(1, k) for k in range(1, n+1))

# Exact algebraic check of E[N_1]=H_n via a Beta integral: for n>=2
# E[N_1] = 1 + n(n-1) int_0^1 u(1-u)^(n-2)(-log u) du.
# Expanding and using int_0^1 u^(j+1)(-log u)du = 1/(j+2)^2.
for n in range(2, 16):
    val = Fraction(1)
    for j in range(n-1):
        val += Fraction(n*(n-1)*(-1)**j*math.comb(n-2,j), (j+2)**2)
    assert val == harmonic(n), (n,val,harmonic(n))
print('Exact rational singleton mean = harmonic number checked for n=2..15.')

# n=3 all distinct at the stopping step iff N_1=3: probability 3!/3^3.
# The Beta-multinomial formula gives 3*int_0^1 u^2(log u)^2du=2/9.
assert Fraction(3*2, 3**3) == Fraction(math.factorial(3), 3**3)
print('Exact n=3 event P(N_1=3)=2/9 checked.')

rng = random.Random(934187)

def direct(n):
    a = [0]*n
    missing = n
    w = 0
    while missing:
        j = rng.randrange(n)
        if a[j] == 0: missing -= 1
        a[j] += 1
        w += 1
    return w,[sum(v == r for v in a) for r in (1,2)]

m=25000
n=12
out=[direct(n) for _ in range(m)]
assert abs(statistics.mean(x[1][0] for x in out)-float(harmonic(n)))<0.10
assert abs(statistics.mean(x[0] for x in out)-n*float(harmonic(n)))<0.35
print('Direct discrete simulation: n=12, trials=25000, means',round(statistics.mean(x[1][0] for x in out),5),round(statistics.mean(x[0] for x in out),5))

# Draw U=min_i Uniform_i via U=1-(1-V)^(1/n); V uniform.
# Given U, the n-1 non-last counts have multinomial cell probabilities
# q_r=(-log(U))^r*U/[r!*(1-U)]. Sequential binomial sampling
# is implemented by direct categorical draws only for manageable n.

def conditionally_sample(n,rmax):
    e=-math.log(1-rng.random())
    # P(U>u)=(1-u)^n, and e=-n*log(1-U).
    u=-math.expm1(-e/n)
    t=-math.log(u)
    q=[u*t**r/(math.factorial(r)*(1-u)) for r in range(1,rmax+1)]
    counts=[0]*rmax
    # sampling via categorical choice; independent n-1 trials
    for _ in range(n-1):
        v=rng.random()
        for r,p in enumerate(q):
            v-=p
            if v<0:
                counts[r]+=1
                break
    counts[0]+=1
    return t, counts

n=350
m=3000
sample=[conditionally_sample(n,2) for _ in range(m)]
means=[statistics.mean(x[1][i] for x in sample) for i in (0,1)]
print('Conditional multinomial simulation: n=350, trials=3000, counts r=1,2 means',*[round(z,3) for z in means])
print('Gumbel-centered and Gaussian-mixture scaling are analytic; finite simulations are not proof.')
