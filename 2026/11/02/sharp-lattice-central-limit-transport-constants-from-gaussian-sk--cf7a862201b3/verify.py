"""Deterministic numerical checks of lattice CLT transport constants.
All mathematical limits are established analytically in RESULT.md.
"""
import numpy as np
from scipy.stats import norm, binom
from scipy.special import ndtri

checks=0

def check(statement, explanation):
    global checks
    if not statement:
        raise AssertionError(explanation)
    checks += 1

def binomial_w2_scaled(n,p):
    k=np.arange(n+1)
    probabilities=binom.pmf(k,n,p)
    cumulative=np.cumsum(probabilities)
    cumulative[-1]=1.0
    cuts=ndtri(np.clip(cumulative[:-1],1.e-299,1-1.e-15))
    heights=np.r_[norm.pdf(cuts),0.0]
    lo=np.r_[0.0,heights[:-1]]
    normalized=(k-n*p)/np.sqrt(n*p*(1-p))
    cross=float(np.dot(normalized,lo-heights))
    return n*(2-2*cross)

def limit_w2_binomial(p):
    return (1/12+(1-2*p)**2/18)/(p*(1-p))

for p in (0.2,0.3,0.5,0.7):
    target=limit_w2_binomial(p)
    values=[binomial_w2_scaled(n,p) for n in (200,500,1200)]
    print(f'p={p:.2f}, nW2² at n=200,500,1200: {values}, predicted {target:.12f}')
    check(abs(values[-1]-target)<0.003,'W2 asymptotic accuracy')
    check(abs(values[-1]-target)<abs(values[0]-target),'W2 convergence to asymptotic')
    for v in values:
        check(v>0,'W2 positive')

# Exact symbolic identity for the quadratic limiting constant.
import sympy as sp
gamma,c=sp.symbols('gamma c',real=True)
z,u=sp.symbols('z u',real=True)
expr=sp.integrate((gamma*(z*z-1)/6+u)**2,(u,-c/2,c/2))/c
mean=sp.integrate(expr*sp.exp(-z*z/2)/sp.sqrt(2*sp.pi),(z,-sp.oo,sp.oo))
check(sp.simplify(mean-(c*c/12+gamma*gamma/18))==0,'symbolic quadratic limit')
print('symbolic Gaussian-uniform mixture verified:',sp.simplify(mean))
print('PASS',checks,'assertions')
