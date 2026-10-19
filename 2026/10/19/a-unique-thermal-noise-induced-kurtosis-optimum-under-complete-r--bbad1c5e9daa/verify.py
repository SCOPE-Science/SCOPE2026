"""Independent algebraic and integral checks for stationary kurtosis in a completely reset active-force Langevin process.

Dependencies: Python 3, sympy, scipy, numpy. No remote access or external data.
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

k,h,u=sp.symbols('k h u',positive=True)
terms=((2,1,0),(-3,0,0),(4,0,1),(-1,0,2)) # coefficient, power of u, exponential damping

def expectation(poly_terms):
    return sp.factor(sum(c*k*sp.factorial(n)/(k+j)**(n+1)
                         for c,n,j in poly_terms))

def times(a,b):
    return tuple((ca*cb,na+nb,ja+jb)
                 for ca,na,ja in a for cb,nb,jb in b)

mg=expectation(terms)
mg2=expectation(times(terms,terms))
ug=expectation(tuple((c,n+1,j) for c,n,j in terms))
mu=sp.factor(h/k+mg)
nu=sp.factor(2*h*h/k**2+2*h*ug+mg2)
K=sp.factor(3*nu/mu**2-3)
Kclaim=3+24*k*(2*h*k**3+17*h*k**2+45*h*k+36*h+36*k+72)/((k+3)*(k+4)*(h*(k+1)*(k+2)+4)**2)
assert sp.factor(K-Kclaim)==0
P=h**2*(4*k**7+65*k**6+419*k**5+1337*k**4+2077*k**3+1026*k**2-864*k-864) +h*(128*k**5+1096*k**4+2948*k**3+1692*k**2-3456*k-3456)-720*k**2-3456*k-3456
assert sp.factor(sp.diff(K,k)+24*P/((k+3)**2*(k+4)**2*(h*(k+1)*(k+2)+4)**3))==0
assert sp.factor(K.subs(h,0)-(3+24*k*(36*k+72)/((k+3)*(k+4)*16)))==0
assert sp.limit(K.subs(h,0),k,sp.oo)==57
assert sp.factor(sp.limit(K,k,0,dir='+')-3)==0

assert sp.factor(sp.limit(K,k,sp.oo)-3)==0
# Positivity of the negative thermal derivative, verified via polynomial coefficients.
neg_h=sp.cancel(-sp.diff(K,h))
num_h, den_h = sp.fraction(sp.factor(neg_h))
assert all(c>0 for c in sp.Poly(num_h,k,h).coeffs())
assert den_h.subs({k:1,h:1})>0
P0=sp.Poly(P,k)
coeffs=P0.all_coeffs()
# A symbolic all-h certificate for the sole Descartes sign change: the only
# variable-sign coefficient is the k^2 term. The first five are positive
# polynomials in h; the last two are negative polynomials in h.
for cp in coeffs[:5]:
    assert all(c>=0 for c in sp.Poly(cp,h).all_coeffs()) and any(c>0 for c in sp.Poly(cp,h).all_coeffs())
for cp in coeffs[-2:]:
    assert all(c>=0 for c in sp.Poly(-cp,h).all_coeffs()) and any(c>0 for c in sp.Poly(-cp,h).all_coeffs())
assert sp.factor(P.subs(k,0)+864*(h+2)**2)==0
for ht in [sp.Rational(1,1000),sp.Rational(1,10),sp.Integer(1),sp.Integer(10)]:
    cc=list(sp.Poly(P.subs(h,ht),k).all_coeffs())
    assert cc[:5]==[x for x in cc[:5] if x>0]
    assert cc[-2]<0 and cc[-1]<0
    assert sum(1 for a,b in zip(cc,cc[1:]) if a*b<0)==1

def kval(kt,ht):
    return float(Kclaim.subs({k:kt,h:ht}))

for ht in (0,0.02,0.3,1.0,20.0):
    for kt in (0.25,1,3,15):
        def g(x): return 2*x-3+4*np.exp(-x)-np.exp(-2*x)
        def v(x): return ht*x+g(x)
        # For small x, g computed with cancellation; integration handles finite small values.
        e1=quad(lambda x:kt*np.exp(-kt*x)*v(x),0,np.inf,epsabs=1e-11)[0]
        e2=quad(lambda x:kt*np.exp(-kt*x)*v(x)**2,0,np.inf,epsabs=1e-10)[0]
        quadK=3*e2/e1**2-3
        err=abs(quadK-kval(kt,ht))
        assert err<2e-7,(kt,ht,quadK,kval(kt,ht),err)

pf=sp.lambdify((k,h),P,'numpy')
for ht in (0.0001,0.01,0.1,1,10,100):
    star=brentq(lambda kt:pf(kt,ht),0.001,1e5)
    assert pf(star*0.99,ht)<0 and pf(star*1.01,ht)>0
    print(f'h={ht:<10} optimum k={star:.10f}, maximum excess kurtosis={kval(star,ht):.10f}')

# Three stochastic age-mixture Monte Carlo corroborations, all independently generated.
rg=np.random.default_rng(20261015)
for ht,kt in [(0.3,1.0),(1.0,1.17),(10.0,0.74)]:
    ages=rg.exponential(scale=1/kt,size=1500000)
    vv=ht*ages+2*ages-3+4*np.exp(-ages)-np.exp(-2*ages)
    assert vv.min()>-1e-8
    x=np.sqrt(np.maximum(vv,0))*rg.standard_normal(len(ages))
    estimate=np.mean(x**4)/np.mean(x**2)**2-3
    target=kval(kt,ht)
    assert abs(estimate-target)<0.18,(ht,kt,estimate,target)
    print(f'age-mixture Monte Carlo h={ht}, k={kt}: {estimate:.5f} vs exact {target:.5f}')
print('PASS: renewal moments, derivative, uniqueness sign certificates, 20 quadratures, and 3 simulated checks')
