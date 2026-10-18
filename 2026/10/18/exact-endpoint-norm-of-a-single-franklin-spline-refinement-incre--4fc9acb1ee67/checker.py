"""Standalone exact and finite-section checks for one-knot spline refinement."""
from fractions import Fraction
import math
import numpy as np
import sympy as sp
from scipy.linalg import solve_banded

S = sp.sqrt(3)
T, U, X = sp.symbols('t u x', real=True)
Q = 2-S
C0 = (1-(S-1)*T)/2
C1 = (2-S+(S-1)*T)/2
D = sp.Rational(1,2)+(S-1)*T*(1-T)
E = (S+2*(S-1)*T*(1-T))/12
L = (S-1)/2 + T*(C0**2+D**2)/(2*(C0+D)) + (1-T)*(C1**2+D**2)/(2*(C1+D))
N = (96*S-144)*U**3+(84*S-96)*U**2+(135-57*S)*U+12*(S-1)
F = (48*S-80)*U**3+(60-28*S)*U**2+(6+4*S)*U+6*(S-1)
P = (1760*S-3040)*U**4+(3216-1840*S)*U**3+(634*S-1062)*U**2+(636-356*S)*U+(94*S-159)
D0 = (-40+24*S)*U**3+(30-14*S)*U**2+(3+2*S)*U+3*(S-1)
checks = 0

def ck(cond, why):
    global checks
    assert bool(cond), why
    checks += 1

def iszero(expr):
    return sp.simplify(sp.radsimp(sp.factor(expr))) == 0

# Exact equations independently connecting the Gram inverse and refinement vector.
for expression,label in [
    (4*(-Q)+1+Q**2,'Gram recurrence'),
    ((sp.Rational(2,3))*S+2*(sp.Rational(1,6))*(-S*Q)-1,'Gram inverse diagonal'),
    (C0 - S*((2-T)-Q*(1+T))/6,'left coefficient'),
    (C1 - S*((1+T)-Q*(2-T))/6,'right coefficient'),
    (1-(1-T)*C0-T*C1-D,'new vertex'),
    (sp.Rational(1,3)-((2-T)*C0+(1+T)*C1)/6-E,'orthogonal energy'),
    ((C0+C1)*(1+Q**2)/(2*(1-Q**2))-(S-1)/2,'geometric tail'),
    (sp.together(D*L/E-N.subs(U,T*(1-T))/F.subs(U,T*(1-T))),'reduced rational norm'),
    (sp.together(sp.diff(N,U)*F-N*sp.diff(F,U)-12*P),'polynomial derivative'),
    (sp.together(F-2*D0),'derivative denominator'),
    (N.subs(U,0)-2*F.subs(U,0),'endpoint lower'),
    (sp.together(N.subs(U,sp.Rational(1,4))/F.subs(U,sp.Rational(1,4))-(sp.Rational(27,26)+45*S/52)),'midpoint upper'),
]:
    ck(iszero(expression),label)

# Positivity of all coefficients of derivative numerator P, so monotonic for every u>=0.
for expr in sp.Poly(P,U).all_coeffs()+sp.Poly(D0,U).all_coeffs():
    ck(float(expr.evalf(30))>0,'positive coefficient')

# Independent symmetric finite-section Gram inversion, piecewise geometry, and endpoint norm.
for frac in [Fraction(1,1000),Fraction(1,100),Fraction(1,10),Fraction(1,5),Fraction(1,4),Fraction(2,5),Fraction(1,2),Fraction(3,5),Fraction(3,4),Fraction(9,10),Fraction(99,100),Fraction(999,1000)]:
    t=float(frac); q=2-math.sqrt(3)
    c0=float(C0.subs(T,sp.Rational(frac.numerator,frac.denominator)))
    c1=float(C1.subs(T,sp.Rational(frac.numerator,frac.denominator)))
    d=float(D.subs(T,sp.Rational(frac.numerator,frac.denominator)))
    energy=float(E.subs(T,sp.Rational(frac.numerator,frac.denominator)))
    norm=float((N/F).subs(U,t*(1-t)))
    length=float(L.subs(T,sp.Rational(frac.numerator,frac.denominator)))
    ck(d>max(c0,c1),'maximum attained at inserted knot')
    ck(abs(d*length/energy-norm)<2e-12,'geometric and rational norm')
    ck(2<norm<2.538,'sharp bound')
    width=61
    ab=np.zeros((3,width)); ab[1,:]=2/3; ab[0,1:]=1/6; ab[2,:-1]=1/6
    b=np.zeros(width); b[29]=(2-t)/6; b[30]=(1+t)/6
    c=solve_banded((1,1),ab,b)
    ck(abs(c[29]-c0)<1e-13,'finite Gram left middle')
    ck(abs(c[30]-c1)<1e-13,'finite Gram right middle')
    for offset in range(-15,16):
        j=29+offset
        ex=(c0*((-q)**(-offset)) if offset<=0 else c1*((-q)**(offset-1)))
        ck(abs(c[j]-ex)<2e-12,'finite Gram inverse geometric tail')
    # Norm square and absolute integral calculated independently by cellwise integration.
    x=[float(k) for k in range(-25,27)]+[t]
    x.sort()
    def val(xx):
        k=math.floor(xx)
        def coef(j):return c0*((-q)**(-j)) if j<=0 else c1*((-q)**(j-1))
        if xx==t:return d
        return -((k+1-xx)*coef(k)+(xx-k)*coef(k+1))
    signed=[];sq=[]
    for a,bx in zip(x[:-1],x[1:]):
        aa=val(a);bb=val(bx);w=bx-a
        signed.append(w*((aa*aa+bb*bb)/(2*(abs(aa)+abs(bb))) if aa*bb<0 else (abs(aa)+abs(bb))/2))
        sq.append(w*(aa*aa+aa*bb+bb*bb)/3)
    ck(abs(sum(signed)-length)<1e-12,'independent cellwise L1')
    ck(abs(sum(sq)-energy)<1e-12,'independent cellwise L2')
    ck(abs(d*sum(signed)/sum(sq)-norm)<1e-10,'independent numerical rank-one norm')

for z in range(101):
    u=z/400
    val=float((N/F).subs(U,u))
    ck(val>=1.9999999999 and val<=2.537352,'entire rational profile bound sample')
print(f'PASS: {checks} assertions (exact symbolic identities, positivity, finite-section inverse, independent integrals).')
