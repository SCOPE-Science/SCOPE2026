"""Reproducible supplementary checks for sections of products of Euclidean balls.
Requirements: Python 3, sympy and mpmath. Infinite-dimensional or analytic
claims are established in the accompanying mathematical proof, not by sampling.
"""
import math
from fractions import Fraction
import sympy as S
import mpmath as mp

p,q,t,v=S.symbols('p q t v', real=True)
poly=S.expand((1-v*v)*(1-(t-v)**2))
exact=S.integrate(poly,(v,t-1,1),conds='none')
assert S.simplify(exact+(t-2)**3*(t*t+6*t+4)/30)==0
assert S.simplify(exact.subs(t,0)-S.Rational(16,15))==0
assert S.simplify(exact.subs(t,2))==0

# Exact nonzero leading logarithm coefficients, in unnormalized a=b=1,
# for dimensions (2,2), (2,4), and (4,4).
def kappa(k):
    return S.pi**(S.Rational(k,2))/S.gamma(S.Rational(k,2)+1)

def predicted_log(m,n):
    p=S.Rational(m-1,2); q=S.Rational(n-1,2); j=p+q+1
    c=kappa(m-1)*kappa(n-1)*2**(p+q)
    if j%2==0:
        return S.simplify(j),S.simplify(-2*c*S.binomial(q,j))
    assert p!=q
    return S.simplify(j+1),S.simplify(c*S.binomial(q,j)*(q-p)*j/(j+1))
for m,n,order,coef in [(2,2,2,2),(2,4,4,-S.pi/2),(4,4,4,-2*S.pi**2/3)]:
    got=predicted_log(m,n)
    assert got==(order,coef),(m,n,got)

mp.mp.dps=48
def section(m,n,x):
    pm=mp.mpf(m-1)/2;qn=mp.mpf(n-1)/2
    km=mp.pi**(mp.mpf(m-1)/2)/mp.gamma(mp.mpf(m-1)/2+1)
    kn=mp.pi**(mp.mpf(n-1)/2)/mp.gamma(mp.mpf(n-1)/2+1)
    lo=max(mp.mpf(-1),x-1);hi=min(mp.mpf(1),x+1)
    if lo>=hi:return mp.mpf(0)
    f=lambda z: max(mp.mpf(0),1-z*z)**pm*max(mp.mpf(0),1-(x-z)**2)**qn
    return km*kn*mp.quad(f,[lo,(lo+hi)/2,hi])

# In symmetric profiles, lower Taylor terms are even powers; estimate the
# next-order logarithmic slope after subtracting the polynomial Taylor jet.
def fit_coefficient(m,n,order,points):
    es=[mp.mpf(z) for z in points]
    ys=[section(m,n,e)-section(m,n,0) for e in es]
    exponents=[2*j for j in range(1,order//2)]
    A=mp.matrix([[e**j for j in exponents]+[e**order*mp.log(e),e**order] for e in es])
    sol=mp.lu_solve(A,mp.matrix(ys))
    return sol[len(exponents)]
# The asymptotic fitting is a *sanity check*, not a rigorous error certificate.
for m,n,order,target in [(2,2,2,mp.mpf(2)),(2,4,4,-mp.pi/2),(4,4,4,-2*mp.pi**2/3)]:
    est=fit_coefficient(m,n,order,['0.004','0.003','0.002','0.0015'][:order//2+2])
    assert abs(est-target)<mp.mpf('0.035'), (m,n,est,target)
print('VERIFY_OK exact_polynomial=1 exact_log_coefficients=3 numerical_log_profiles=3')
