#!/usr/bin/env python3
"""Exact symbolic verification of the two-facet-apex volume-product profile.
Requires Python 3 and SymPy; run: python verify_profile.py.
This script is supplementary to the elementary integral and polygon proofs.
"""
from itertools import product
import sympy as S

t, u, v, z = S.symbols('t u v z', positive=True)
R = S.Rational

def equal(a,b):
    assert S.cancel(a-b)==0, (a,b)

def orient(a,b,c):
    return S.expand((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))

def prove_nonnegative(expr, regime):
    expr=S.expand(expr)
    if not expr: return
    degree=S.Poly(expr,t).degree()
    if regime=='low':
        # Projective map z>=0 -> 0<=t<=2.
        f=S.cancel((1+z)**degree * expr.subs(t,2*z/(1+z)))
    else:
        # Shift z>=0 -> t>=2.
        f=S.expand(expr.subs(t,z+2))
    p=S.Poly(f,z)
    assert all(c>=0 for c in p.all_coeffs()), (regime, expr, f)

def area(vertices):
    return S.expand(sum(orient((0,0),vertices[i],vertices[(i+1)%len(vertices)])
                        for i in range(len(vertices)))/2)

H=[(-1,-1),(1,-1),(1+t,1),(1,1+t),(-1,1)]
D=[(a[0]-b[0],a[1]-b[1]) for a,b in product(H,repeat=2)]
low=[(-t-2,-2),(-2,-t-2),(0,-t-2),(2,-2),(t+2,0),
     (t+2,2),(2,t+2),(0,t+2),(-2,2),(-t-2,0)]
high=[(-t-2,-2),(-2,-t-2),(0,-t-2),(t,-t),(t+2,0),
      (t+2,2),(2,t+2),(0,t+2),(-t,t),(-t-2,0)]
for poly,regime in [(low,'low'),(high,'high')]:
    for c in poly:
        assert any(S.cancel(c[0]-d[0])==0 and S.cancel(c[1]-d[1])==0
                   for d in D),c
    # Convex polygon: each of the 25 generating differences lies on
    # the interior side of EVERY proposed counterclockwise edge.
    for i in range(len(poly)):
        a,b=poly[i],poly[(i+1)%len(poly)]
        for c in D: prove_nonnegative(orient(a,b,c),regime)
equal(area(H),4+2*t+t*t/2)
equal(area(low),16+12*t+t*t)
equal(area(high),8+12*t+3*t*t)

A=area(H)
# Fiber identity from x1=p+q, x2=p-q and mixed area with [-1,1]^2.
Vlow=S.factor(R(2,3)*A+R(1,3)*area(low)+8+R(8,3)*t)
Vhigh=S.factor(R(2,3)*A+R(1,3)*area(high)+8+R(8,3)*t)
equal(Vlow,16+8*t+R(2,3)*t*t)
equal(Vhigh,R(4,3)*(t*t+6*t+10))

v0=2/(t+2); a=(t+2)/2

def dbl(expr,lo,hi,left,right):
    return S.factor(S.integrate(S.integrate(expr,(u,lo,hi)),(v,left,right)))

I1=dbl((1-u)*(2-(t+4)*u/2-t*v/2),v,(4-t*v)/(t+4),0,v0)
I0=dbl((1-v)*(2-a*(u+v)),0,v,0,v0)
Ilo=dbl((1-v)*(2-a*(u+v)),0,4/(t+2)-v,v0,1)
Elo=dbl((1-v)*((2-t)*v/2-a*u),0,(2-t)*v/(t+2),0,1)
Ihi=dbl((1-v)*(2-a*(u+v)),0,4/(t+2)-v,v0,2/t)
Ehi=dbl((1-v)*((t-2)*v/2-a*u),0,(t-2)*v/(t+2),0,2/t)
equal(I1,4*(2*t*t+9*t+8)/(3*(t+2)**2*(t+4)**2))
equal(I0,(6*t+5)/(3*(t+2)**3))
equal(Ilo,t*t*(t*t-8*t+24)/(48*(t+2)**3))
equal(Elo,(t-2)**2/(48*(t+2)))
equal(Ihi,4*(3*t**4-6*t**3-2*t*t+16*t-12)/(3*t**4*(t+2)**3))
equal(Ehi,(t-2)**2*(2*t-3)/(3*t**4*(t+2)))
Wlow=S.factor(2*(I1+I0+Ilo-Elo))
Whigh=S.factor(2*(I1+I0+Ihi-Ehi))
equal(Wlow,-(t**5+4*t**4-44*t**3-272*t*t-464*t-256)/(3*(t+2)**3*(t+4)**2))
equal(Whigh,8*(3*t**6+26*t**5+80*t**4+72*t**3-88*t*t-64*t+128)/(3*t**3*(t+2)**3*(t+4)**2))
equal(Whigh-Wlow,(t-2)**4/(3*t**3*(t+2)))

Qlow=S.factor(Vlow*Wlow)
Qhigh=S.factor(Vhigh*Whigh)
BASE=R(32,3)
Nlow=1920+2752*t+1136*t*t+32*t**3-76*t**4-16*t**5-t**6
Nhigh=t**7+19*t**6+106*t**5+188*t**4-128*t**3-568*t*t+64*t+640
equal(Qlow-BASE,2*t*Nlow/(9*(t+2)**3*(t+4)**2))
equal(Qhigh-BASE,64*Nhigh/(9*t**3*(t+2)**3*(t+4)**2))
# Both polynomials are strictly positive in their own chambers.
# The low inequality uses t<=2 to dominate the three negative terms.
equal(Nlow-(1920+2752*t+688*t*t+32*t**3),
      t*t*(448-76*t*t-16*t**3-t**4))
prove_nonnegative(t*t*(448-76*t*t-16*t**3-t**4),'low')
prove_nonnegative(Nhigh,'high')
for W,V in [(Wlow,Vlow),(Whigh,Vhigh)]:
    equal(W.subs(t,2),R(79,216))
    equal(V.subs(t,2),R(104,3))
equal(Qlow.subs(t,2),R(1027,81))
equal(Qhigh.subs(t,2),R(1027,81))
equal(S.diff(Qlow,t).subs(t,2),-R(433,972))
equal(S.diff(Qhigh,t).subs(t,2),R(515,972))
equal(S.limit(Qlow,t,0,dir='+'),BASE)
equal(S.limit(Qhigh,t,S.oo),BASE)
print('TWO_APEX_4D_EXACT_PROFILE_OK')
