"""Numerical diagnostics for the analytic global-boundedness theorem.

The proof is given in RESULT.md. These finite checks do not certify
all states or all parameters.
"""
from fractions import Fraction
from math import tanh, sqrt, e
from random import Random

M = ((Fraction(17, 10), Fraction(-1)),
     (Fraction(1), Fraction(17, 10)))
b = (Fraction(-3, 10), Fraction(3, 10))
assert M[0][0] == M[1][1] == Fraction(17, 10)
assert M[0][1] == -M[1][0]
assert M[0][0] - abs(M[0][1]) - max(abs(b[0]), abs(b[1])) == Fraction(2, 5)
assert M[0][0]**2 + M[1][0]**2 == Fraction(389, 100)
S = sqrt(2)*(sqrt(389)+3)/10


def update(x, T, alpha):
    t0, t1 = tanh(alpha*x[0]), tanh(alpha*x[1])
    return ((1-T)*x[0]+T*(1.7*t0-t1-0.3),
            (1-T)*x[1]+T*(t0+1.7*t1+0.3))


def norm(x):
    return sqrt(x[0]**2 + x[1]**2)


rng = Random(836451)
checks = 0
for alpha in (0.1, 0.5, 1.0, 3.0, 10.0):
    H = 2*S
    B = 68/(5*e*alpha)+H**2
    rho = 5*(B+1)/8
    R = rho+H
    for _ in range(70):
        v = (rng.uniform(-1000,1000),rng.uniform(-1000,1000))
        f = update(v, 2, alpha)
        rad = norm(v)
        if rad >= rho:
            assert norm(f)**2 - rad**2 <= -1+1e-7*max(1, rad), (alpha, v)
        if rad <= R:
            assert norm(f) <= R+1e-8
        checks += 1
for T in (0.01,0.4,1.0,1.8,1.99):
    C=T*S
    q=abs(1-T)
    R=C/(1-q)+1
    for _ in range(100):
        v = (rng.uniform(-R,R),rng.uniform(-R,R))
        v = (v[0]*min(1,R/max(1e-9,norm(v))),v[1]*min(1,R/max(1e-9,norm(v))))
        assert norm(update(v,T,1.2)) <= R+1e-8
        checks += 1
for T in (2.001,2.1,2.3,3.5):
    C=T*S
    Re=2*C/(T-2)
    for _ in range(50):
        alpha=rng.uniform(0.01,20)
        a=rng.uniform(-3.14,3.14)
        v=(2*Re*a,2*Re)
        assert norm(update(v,T,alpha)) >= T/2*norm(v)-1e-8
        checks += 1
print(f'{checks} deterministic finite checks passed; analytic proof is separate.')
