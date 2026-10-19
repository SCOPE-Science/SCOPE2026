"""Reproduce finite sanity checks for the analytic open-hypercycle theorem.
All global assertions rely on the proof, not numerical sampling.
"""
from fractions import Fraction as F
from math import e, exp, log

# For n=3, exact replicator derivative and q bound on an interior grid.
checks = 0
for i in range(1, 18):
    for j in range(1, 19-i):
        k = 19-i-j
        if k <= 0:
            continue
        p = (F(i,19),F(j,19),F(k,19))
        q = p[0]*p[1]+p[1]*p[2]+p[2]*p[0]
        dp = tuple(p[a]*(p[(a-1)%3]-q) for a in range(3))
        assert sum(dp) == 0
        assert sum(dp[a]/p[a] for a in range(3)) == 1-3*q
        assert q <= F(1,3)
        assert q <= p[1]+p[2]
        checks += 1
assert checks > 100

# Parameter example d=1/20, gamma=1: two positive radial roots.
d = 1/20
gamma = 1.0
f = lambda z: z*exp(-gamma*z)-3*d
assert f(0) < 0 and f(1) > 0 and f(20) < 0

def bisect(a,b):
    assert f(a)*f(b) < 0
    for _ in range(100):
        m = (a+b)/2
        if f(a)*f(m) <= 0:
            b = m
        else:
            a = m
    return (a+b)/2
small,large = bisect(0,1),bisect(1,20)
assert 0 < small < 1 < large
assert abs(f(small)) < 1e-14 and abs(f(large)) < 1e-14
assert 1-gamma*small > 0 and 1-gamma*large < 0

eps=(d*gamma*e/2)*exp(-2/(d*gamma))
T=2/(d*gamma)
assert abs(eps*exp(T)-d*gamma*e/2) < 1e-14
assert eps > 0
print(f'PASS: {checks} exact simplex cases; radial roots {small:.12g},{large:.12g}; positive wedge aperture {eps:.5e}')
