#!/usr/bin/env python3
"""Reproduce fourth-order stationary moments and polynomial sign certificates.

Dependencies: Python 3.10+ and SymPy 1.12+.
"""
from fractions import Fraction
import sympy as S

k, u = S.symbols('k u', positive=True)
H = (4*k+3)*(k+u+u**2)**2*(9*k+3*u+u**2)*(k+2+3*u+u**2)
Pc = -9*k**2+(26*u**2+68*u+51)*k+3*u**4+24*u**3+72*u**2+69*u+18
Px = (12-9*u)*k**2+(33+119*u+112*u**2+26*u**3)*k+18+69*u+102*u**2+72*u**3+24*u**4+3*u**5
Pv = -9*k**3+(-18+16*u+26*u**2)*k**2+(6*u+10*u**2+4*u**3+3*u**4)*k+6*u**2+9*u**3+3*u**4

# Independently reconstruct stationary monomial equations from the Markov generator.
# A=E[x**i*v**j] and B=E[x**i*v**j*sigma].
M = {(0,0,0):S.Integer(1),(0,0,1):S.Integer(0)}
for d in range(1,5):
    inds=[(i,d-i,0) for i in range(d+1)]+[(i,d-1-i,1) for i in range(d)]
    sym={z:S.Symbol('m_%d_%d_%d'%z) for z in inds}
    def val(i,j,s):
        if i<0 or j<0:return S.Integer(0)
        return sym.get((i,j,s),M.get((i,j,s),S.Integer(0)))
    eqs=[]
    for i,j,s in inds:
        eqs.append(i*val(i-1,j+1,s)-j*val(i,j,s)-j*k*val(i+1,j-1,s)+j*val(i,j-1,1-s)-s*u*val(i,j,s))
    sol=S.solve(eqs,list(sym.values()),dict=True)
    assert len(sol)==1, (d,'rank mismatch')
    for z,q in sym.items(): M[z]=S.factor(sol[0][q])

assert S.factor(M[2,0,0]-(u+1)/(k*(k+u+u**2)))==0
assert S.factor(M[0,2,0]-u/(k+u+u**2))==0
assert S.factor(M[1,1,0])==0
cross=S.factor(M[2,2,0]-M[2,0,0]*M[0,2,0])
kurt_x=S.factor(M[4,0,0]-3*M[2,0,0]**2)
kurt_v=S.factor(M[0,4,0]-3*M[0,2,0]**2)
assert S.factor(cross+2*u*Pc/H)==0
assert S.factor(kurt_x+6*Px/(k*H))==0
assert S.factor(kurt_v+6*u*Pv/H)==0
print('EXACT: second/fourth moment identities and covariance factorization pass')

# Remainders on the cross-covariance zero set Pc=0.
Rv=-(1532*k*u**3+5888*k*u**2+7911*k*u+3681*k+156*u**5+1428*u**4+5319*u**3+8502*u**2+5697*u+1242)/S.Integer(9)
Rx=(236*k*u**2+476*k*u+303*k+12*u**4+96*u**3+387*u**2+429*u+126)/S.Integer(3)
assert S.factor(S.rem(Pv,Pc,k)-Rv)==0
assert S.factor(S.rem(Px,Pc,k)-Rx)==0
assert S.factor(Pc.subs(k,6)-3*u*(u**3+8*u**2+76*u+159))==0
print('EXACT: positive-coefficient remainder and threshold-6 certificates pass')

B=26*u**2+68*u+51
C=3*u**4+24*u**3+72*u**2+69*u+18
kc=(B+S.sqrt(B**2+36*C))/18
assert S.simplify(Pc.subs(k,kc))==0
assert S.limit(kc,u,0,dir='+')==6
assert S.limit(kc/u**2,u,S.oo)==3
assert S.series(kc,u,0,2).removeO()==6+S.Rational(159,19)*u
print('EXACT: unique quadratic threshold, small- and large-rate limits pass')

n=0
for uv in [S.Rational(1,10),S.Rational(1,2),S.Integer(1),S.Rational(4,3),S.Integer(2),S.Integer(4),S.Integer(10)]:
    for kv in [S.Rational(1,10),S.Integer(1),S.Integer(3),S.Integer(6),S.Integer(10),S.Integer(20),S.Integer(50),S.Integer(500)]:
        substitution={k:kv,u:uv}
        for expr,formula in [(cross,-2*u*Pc/H),(kurt_x,-6*Px/(k*H)),(kurt_v,-6*u*Pv/H)]:
            assert S.cancel(expr.subs(substitution)-formula.subs(substitution))==0
            n+=1
    ccv=S.N(kc.subs(u,uv),40)
    polyv=S.Poly(Pv.subs(u,uv),k)
    roots_v=S.polys.polytools.intervals(polyv,eps=S.Rational(1,10**10))
    positives_v=[(a,b) for (a,b),mult in roots_v if b>0 and a>=0]
    assert len(positives_v)==1
    assert S.N(positives_v[0][1],30)<ccv
    if uv>S.Rational(4,3):
        roots_x=S.polys.polytools.intervals(S.Poly(Px.subs(u,uv),k),eps=S.Rational(1,10**10))
        positives_x=[(a,b) for (a,b),mult in roots_x if b>0 and a>=0]
        assert len(positives_x)==1
        assert ccv<S.N(positives_x[0][0],30)
    else:
        assert all(c>=0 for c in S.Poly(Px.subs(u,uv),k).all_coeffs())
print(f'EXACT: {n} rational parameter checks and threshold orderings pass')
print('TOTAL: 168 rational moment substitutions plus 7 threshold-order tests, all passed')
