"""Reproducibility checks for a boundary 2-by-2 conditional-Poisson law.
Only standard Python libraries are required; numerical checks do not prove limits.
"""
import math
from fractions import Fraction

checks = 0

def verify(condition, description):
    global checks
    assert condition, description
    checks += 1

def legendre(n, x):
    if n == 0:
        return Fraction(1)
    p0, p1 = Fraction(1), x
    for j in range(1, n):
        p0, p1 = p1, ((2*j+1)*x*p1-j*p0)/(j+1)
    return p1

def exact_law(n, z):
    w = Fraction(z, n*n)
    unnormalized = [Fraction(math.comb(n,k)**2)*w**k for k in range(n+1)]
    total = sum(unnormalized)
    p = [a/total for a in unnormalized]
    return p, total, w

for n in range(1, 10):
    for z in (Fraction(1,3), Fraction(1), Fraction(7,2)):
        p, total, w = exact_law(n, z)
        if w != 1:
            verify(total == (1-w)**n * legendre(n, (1+w)/(1-w)), 'Legendre generating identity')
        e = sum(k*p[k] for k in range(n+1))
        e2 = sum(k*k*p[k] for k in range(n+1))
        var = e2-e*e
        verify(e2 == z/Fraction(n*n)*sum((n-k)**2*p[k] for k in range(n+1)), 'exact score')
        verify(var <= e, 'Poisson-binomial variance bound')
        mu = math.sqrt(float(z))
        k0 = n*mu/(n+mu)
        if mu < n:
            verify(-1e-10 <= k0-float(e) <= 1+1e-10,'mean squeeze')
        for k in range(n):
            verify(p[k+1]*Fraction((k+1)**2) == p[k]*Fraction(z,(n*n)) * (n-k)**2, 'mass ratio')

# Stable log-sum-exp enumeration of both finite-size and Bessel reference laws.
def log_normalized(log_weights):
    high = max(log_weights)
    weights = [math.exp(a-high) for a in log_weights]
    total = sum(weights)
    return [a/total for a in weights]

def tv_distance(n, mu):
    end = max(n, int(mu+30*math.sqrt(mu)+100))
    bs, qs = [], []
    for k in range(end+1):
        logb = 2*k*math.log(mu)-2*math.lgamma(k+1)
        bs.append(logb)
        if k<=n:
            hlog = 2*(math.lgamma(n+1)-math.lgamma(n-k+1)-k*math.log(n))
            qs.append(logb+hlog)
        else:
            qs.append(float('-inf'))
    bp,qp=log_normalized(bs),log_normalized(qs)
    return 0.5*sum(abs(x-y) for x,y in zip(bp,qp))

print('Exact combinatorial and moment assertions:', checks)
for c in (0.125, 1.0, 4.0):
    predicted = math.erf(c**0.75/2) # 2Phi(c^(.75)/sqrt(2))-1 = erf(c^(.75)/2)
    arr = []
    for n in (1000,4000,16000):
        mu = c**0.5*n**(2/3)
        val = tv_distance(n,mu)
        arr.append((n, round(val,7)))
    print('c=',c, 'prediction=',round(predicted,7), 'finite=',arr)
    verify(abs(arr[-1][1]-predicted)<0.08,'crossover numerical tolerance')
for n in (2000,8000):
    mu=n**0.8
    print('supercritical n=',n,'mu=',round(mu,3),'TV=',round(tv_distance(n,mu),6))
print('Total assertions:', checks)
