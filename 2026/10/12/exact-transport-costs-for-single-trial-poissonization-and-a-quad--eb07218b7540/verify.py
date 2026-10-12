"""Numerical diagnostics for exact costs of a categorical trial and its Poissonization.

Requirements: Python 3.10+, scipy, numpy, sympy. These finite checks do not
replace the all-dimensional analytic argument in RESULT.md.
"""
from itertools import product
from math import exp, factorial
import numpy as np
from scipy.optimize import linprog
import sympy as sp


def poisson_tail(lam, k):
    return 1-exp(-lam)*sum(lam**j/factorial(j) for j in range(k))


def poissonized_moment(d, cut=32):
    lam=1/d
    emax=sum(1-(1-poisson_tail(lam,k))**d for k in range(1,cut+1))
    return 2+1/d-2*emax


def lp_discrete(d, trunc):
    # Condition each Pois(1/d) variate on {0,...,trunc}.
    x=np.arange(trunc+1)
    masses=np.array([(1/d)**j/factorial(j) for j in x], dtype=float)
    masses/=masses.sum()
    support=np.array(list(product(x,repeat=d)),dtype=float)
    b=np.prod(np.array([masses[v.astype(int)] for v in support]),axis=1)
    n=len(support)
    costs=np.array([1+np.sum(support**2,axis=1)-2*support[:,i] for i in range(d)])
    # Variables z_{i,y}. Row/column marginals fixed exactly.
    A=np.zeros((d+n,d*n))
    for i in range(d):
        A[i, i*n:(i+1)*n]=1.
        A[d:, i*n:(i+1)*n]=np.eye(n)
    target=np.concatenate([np.full(d,1/d), b])
    answer=linprog(costs.ravel(),A_eq=A,b_eq=target,bounds=(0,None),method='highs')
    assert answer.success,answer.message
    optimum=answer.fun
    max_based=1+np.dot(b,np.sum(support**2,axis=1))-2*np.dot(b,np.max(support,axis=1))
    assert abs(optimum-max_based)<5e-6,(optimum,max_based)
    return optimum

for d in (1,2,3,5,10,30,100,300):
    a=poissonized_moment(d)
    assert a>2/exp(1)-2e-11,(d,a)
    print('d',d,'W2_squared',format(a,'.13f'),'d2_correction',round((a-2/exp(1))*d*d,9))

for d,trunc in ((1,7),(2,5),(3,3)):
    x=lp_discrete(d,trunc)
    a=poissonized_moment(d)
    assert abs(x-a)<0.016,(d,x,a)
    print('lp_check',d,trunc,round(x,12),round(a,12))

z=sp.symbols('z',positive=True)
# P(M>=2): 1-[exp(-z)(1+z)]**(1/z), and P(M>=3).
two=1-sp.exp((-z+sp.log(1+z))/z)
three=1-sp.exp((-z+sp.log(1+z+z**2/2))/z)
assert sp.series(two,z,0,3).removeO().expand()==z/2-sp.Rational(11,24)*z**2
assert sp.series(three,z,0,3).removeO().expand()==z**2/6
assert 2*(sp.Rational(11,24)-sp.Rational(1,6))==sp.Rational(7,12)
print('VERIFY_OK')
