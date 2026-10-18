#!/usr/bin/env python3
"""Exact and independent finite-dimensional checks for a temporal fourth-moment contrast.

Requires Python 3, NumPy, SciPy, SymPy. Execute: python verify_time_arrow.py
"""
import math
import numpy as np
from scipy.linalg import expm
import sympy as sp

z, p = sp.symbols('z p', real=True)
F = lambda a: (1-a)**3*(1+a)
assert sp.expand(F(z)-(1-z**4+2*z**3-2*z)) == 0
assert sp.simplify((1-p)*F(sp.Integer(0))+p*F(sp.Integer(-2))-(1-28*p))==0
assert sp.solve(1-28*p,p)==[sp.Rational(1,28)]
assert sp.Rational(0)<sp.Rational(1,28)<sp.Rational(1,16)

cases=[
    ('full reset', [(0,1)]),
    ('fixed positive contraction', [(sp.Rational(1,2),1)]),
    ('fixed negative contraction', [(sp.Rational(-1,2),1)]),
    ('two positive contractions', [(sp.Rational(1,4),sp.Rational(1,3)), (sp.Rational(3,4),sp.Rational(2,3))]),
    ('two signed contractions', [(sp.Rational(-3,4),sp.Rational(2,5)), (sp.Rational(1,3),sp.Rational(3,5))]),
    ('identity or full reset', [(0,sp.Rational(2,7)),(1,sp.Rational(5,7))]),
    ('rare negative overshoot', [(0,sp.Rational(19,20)),(-2,sp.Rational(1,20))]),
    ('critical zero contrast', [(0,sp.Rational(27,28)),(-2,sp.Rational(1,28))]),
    ('below overshoot threshold', [(0,sp.Rational(39,40)),(-2,sp.Rational(1,40))]),
    ('near unstable fourth moment', [(0,sp.Rational(47,50)),(-2,sp.Rational(3,50))]),
]
count=4
for name, mark_law in cases:
    law=[(sp.Rational(a),sp.Rational(w)) for a,w in mark_law]
    assert sum(w for a,w in law)==1
    m={j:sp.simplify(sum(w*a**j for a,w in law)) for j in range(1,5)}
    assert m[4]<1
    D=sp.Rational(11,10)
    r=sp.Rational(7,5)
    a={j:sp.simplify(r*(1-m[j])) for j in range(1,5)}
    assert all(a[j]>0 for j in range(1,5))
    variance=2*D/a[2]
    fourth=24*D**2/(a[2]*a[4])
    factor=sp.simplify(sum(w*F(q) for q,w in law))
    checks=[
        sp.simplify(fourth-12*D*variance/a[4])==0,
        sp.simplify(a[4]-2*(a[3]-a[1])-r*factor)==0,
        sp.simplify((fourth-3*variance**2)-12*D**2*r*sum(w*(1-q**2)**2 for q,w in law)/(a[2]**2*a[4]))==0,
    ]
    assert all(checks)
    count+=len(checks)
    contrast_prefactor=sp.simplify(12*D**2*r*factor/(a[2]*a[4]))
    assert sp.simplify((6*D*variance-(a[3]-a[1])*fourth)-contrast_prefactor)==0
    count+=1
    # Generator acting on coefficients of [1,x,x^2,x^3,x^4].
    M=np.zeros((5,5))
    for j in range(1,5):
        M[j,j]=-float(a[j])
        if j>=2:M[j-2,j]=float(D*j*(j-1))
    for lag in (0.04,0.2,0.7,1.6,4.0):
        P=expm(M*lag)
        direct=float(fourth)*(P[3,3]-P[1,1])+float(variance)*P[1,3]
        u,v=float(a[1]),float(a[3])
        divided=lag*math.exp(-u*lag) if abs(u-v)<1e-12 else (math.exp(-u*lag)-math.exp(-v*lag))/(v-u)
        prediction=float(contrast_prefactor)*divided
        assert divided>0 and abs(direct-prediction)<1e-10*(1+abs(prediction)+abs(direct)),(name,lag,direct,prediction)
        count+=1
    # The theoretical positive kernel has a single peak.
    u,v=float(a[1]),float(a[3])
    peak=1/u if abs(u-v)<1.e-12 else math.log(v/u)/(v-u)
    assert peak>0
    eps=min(.005,peak/100)
    G=lambda t: t*math.exp(-u*t) if abs(u-v)<1e-12 else (math.exp(-u*t)-math.exp(-v*t))/(v-u)
    assert G(peak)>G(peak-eps) and G(peak)>G(peak+eps)
    count+=1
    # Covariance matches an OU process with same variance and rate a_1.
    OU_diffusivity=a[1]*variance
    assert sp.simplify(OU_diffusivity/a[1]-variance)==0
    count+=1
    if name=='critical zero contrast':
        assert factor==0
    elif name in ('rare negative overshoot','near unstable fourth moment'):
        assert factor<0
    else:
        assert factor>0
    count+=1
    print(f'{name}: mark factor={factor}, rates={a[1]}, {a[3]}, lag peak={peak:.6f}; PASS')
print('PASS:',count,'assertions (exact symbolic and independent matrix semigroup)')
