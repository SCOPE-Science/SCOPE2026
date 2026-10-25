"""Independent finite-dimensional and numerical checks for a Gaussian width law.

Requires Python >=3.9; uses only the standard library. The finite checks
corroborate closed formulas and do not prove an infinite-dimensional limit.
"""
import itertools
import math
import random

phi = lambda x: math.exp(-x*x/2) / math.sqrt(2*math.pi)
Phi = lambda x: (1.0+math.erf(x/math.sqrt(2)))/2.0
f = lambda x: abs(x)*Phi(abs(x)) + phi(abs(x)) + phi(0)

def halfnormal_integral(fn, endpoint=11.0, subintervals=120000):
    n = subintervals
    step = endpoint/n
    accum = 2*phi(0)*fn(0) + 2*phi(endpoint)*fn(endpoint)
    for i in range(1,n):
        x = i*step
        accum += (4 if i%2 else 2)*2*phi(x)*fn(x)
    return step*accum/3

mu=(1+math.sqrt(2))/math.sqrt(math.pi)
sigma2=(14*math.pi+12*math.sqrt(3)-30*math.sqrt(2)-21)/(24*math.pi)
expect_f2=(6*math.sqrt(3)+12*math.sqrt(2)+7*math.pi+30)/(12*math.pi)
checks = [
    (lambda t: t*t*Phi(t)**2, 7/12+(1+1/math.sqrt(3))/(2*math.pi)),
    (lambda t: phi(t)**2, 1/(2*math.pi*math.sqrt(3))),
    (lambda t: t*Phi(t)*phi(t), (1+1/math.sqrt(3))/(4*math.pi)),
    (lambda t: t*Phi(t), (1+math.sqrt(2))/(2*math.sqrt(math.pi))),
    (lambda t: phi(t), 1/(2*math.sqrt(math.pi))),
    (lambda t: f(t), mu),
    (lambda t: f(t)**2, expect_f2),
    (lambda t: (t*t-1)*f(t), mu/2),
]
for integrand, value in checks:
    observed=halfnormal_integral(integrand)
    assert abs(observed-value)<5e-9,(observed,value)
assert abs(expect_f2-9*mu**2/8-sigma2)<1e-12 and sigma2>0

rng=random.Random(172903)
comparisons=0
for n in range(2,7):
    V=set()
    for k in range(1,n+1):
        V.update(itertools.permutations([1]*k+list(range(k+1,n+1))))
    for sample in range(64):
        g=[rng.gauss(0,1) for _ in range(n)]
        direct=max(sum(a*b for a,b in zip(v,g)) for v in V)
        formula=sum(g)+sum(max(0,g[i],g[j]) for i in range(n) for j in range(i+1,n))
        assert abs(direct-formula)<1e-9,(n,sample,direct,formula)
        hminus=-sum(g)+sum(max(0,-g[i],-g[j]) for i in range(n) for j in range(i+1,n))
        width=sum(max(0,g[i],g[j])-min(0,g[i],g[j]) for i in range(n) for j in range(i+1,n))
        assert abs(direct+hminus-width)<1e-9
        comparisons+=1
print('VERIFY_OK gaussian_integrals=8 support_comparisons=',comparisons,'variance=',sigma2)
