#!/usr/bin/env python3
"""Independent finite tests for the three-scale Gaussian Fourier-zero multiplicity theorem."""
import math
import cmath
import sympy as sp
import mpmath as mp
mp.mp.dps = 40

def mu(a):
    return mp.pi*(1-a)/(2*(1+a))

def norm(a):
    return (4*a)**mp.mpf('0.25')/mp.sqrt(1+a)

def direct_bargmann_gaussian(a,z):
    pref = mp.power(2,mp.mpf('0.25'))*mp.power(2*a,mp.mpf('0.25'))
    f=lambda t:mp.exp(-mp.pi*(a+1)*t*t+2*mp.pi*t*z-mp.pi*z*z/2)
    return pref*mp.quad(f,[-mp.inf,mp.inf])

for a in [mp.mpf('0.3333333333333333333333333333333'),mp.mpf('1'),mp.mpf('1.666666666666666666666666667'),mp.mpf('3')]:
    for z in [mp.mpc('0.25','0.33'), mp.mpc('-0.4','0.18')]:
        prediction=norm(a)*mp.exp(mu(a)*z*z)
        err=abs(direct_bargmann_gaussian(a,z)-prediction)
        assert err<mp.mpf('1e-32'),(a,z,err)
print('GAUSSIAN_BARGMANN_TESTS=8 max_error<1e-32')

x=sp.symbols('x')
models=[(1,2,sp.Rational(1),sp.Rational(2),sp.Rational(1)),
        (1,4,sp.Rational(1),sp.Rational(1),sp.Rational(27,256)),
        (1,3,sp.Rational(1),sp.Rational(1),sp.Rational(1)),
        (1,2,sp.Rational(1),sp.Rational(1),sp.Rational(1))]
for p,q,A,B,C in models:
    polynomial=A+B*x**p+C*x**q
    fact=sp.factor(polynomial)
    roots=sp.polys.polytools.intervals(polynomial,eps=sp.Rational(1,10**8)) if q<=4 else []
    gcd=sp.gcd(polynomial,sp.diff(polynomial,x))
    condition=(p%2==1 and q%2==0 and (sp.Rational(A*q,B*(q-p)))**q == (sp.Rational(A*p,C*(q-p)))**p)
    has_multiple=sp.degree(gcd)>0
    assert condition==has_multiple,(p,q,condition,has_multiple)
    print('MODEL',p,q,'polynomial',fact,'multiple',has_multiple,'gcd',gcd)

# Verify exact double zeros and second-derivative rigidity for resonance p/q=1/4.
alpha=mp.pi/8;beta=mp.pi/2;A=B=mp.mpf(1);C=mp.mpf(27)/256
xstar=mp.log(mp.mpf(4)/3)/alpha
for j in [-3,-2,-1,0,1,2,3]:
    w=xstar+1j*mp.pi*4*(2*j+1)/beta
    f=A+B*mp.exp(alpha*w)+C*mp.exp(beta*w)
    df=B*alpha*mp.exp(alpha*w)+C*beta*mp.exp(beta*w)
    ddf=B*alpha**2*mp.exp(alpha*w)+C*beta**2*mp.exp(beta*w)
    assert abs(f)<mp.mpf('1e-35') and abs(df)<mp.mpf('1e-35')
    assert abs(ddf-A*alpha*beta)<mp.mpf('1e-35')
print('RESONANT_DOUBLE_ZEROS=7 second_derivative_identity=PASS')

# Algebraic rational-root count using exact polynomial roots and their periods.
def zero_counts(p,q,A,B,C,alpha,beta,R):
    pol=sp.Poly(A+B*x**p+C*x**q,x)
    import numpy as np
    rr=np.roots([float(v) for v in pol.all_coeffs()])
    # Numerical repeated roots can split, so use the exact gcd and factorization to obtain multiplicities.
    sqfree=sp.sqf_list(pol)[1]
    ww=[]
    for factor,mult in sqfree:
        coeff=[complex(sp.N(v,40)) for v in factor.all_coeffs()]
        rr2=np.roots(coeff)
        for root in rr2:
            logroot=cmath.log(root)
            for k in range(-max(50,int(beta*R*R/(2*math.pi*q))+20), max(50,int(beta*R*R/(2*math.pi*q))+20)+1):
                w=(q/beta)*(logroot+2j*math.pi*k)
                if abs(w)<=R*R*(1+1e-10):ww.append(mult)
    return (2*sum(ww),2*len(ww))

for p,q,A,B,C in [(1,2,1,2,1),(1,4,1,1,sp.Rational(27,256)),(1,2,1,1,1)]:
    alpha=float(mp.pi*p/8); beta=alpha*q/p
    for R in [10,20,40]:
        counted,distinct=zero_counts(p,q,A,B,C,alpha,beta,R)
        base=2*beta/math.pi*R*R
        multiple=(p%2==1 and q%2==0 and abs((A*q/(B*(q-p)))**q-(A*p/(C*(q-p)))**p)<1e-9)
        estimate=base*(1-(1/q if multiple else 0))
        assert abs(counted-base)<20 and abs(distinct-estimate)<20,(p,q,R,counted,distinct,base,estimate)
        print('COUNT',p,q,'R',R,'total',counted,'distinct',distinct,'main',round(base,3),'distinct_main',round(estimate,3))
print('ALL_CHECKS_PASSED')
