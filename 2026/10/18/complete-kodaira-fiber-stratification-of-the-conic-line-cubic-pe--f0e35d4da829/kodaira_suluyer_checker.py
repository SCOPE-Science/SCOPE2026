"""Exact symbolic identities for the Kodaira-fiber classification of a cubic pencil.
Run: python kodaira_suluyer_checker.py  (requires SymPy).
"""
import sympy as s
u,t,a=s.symbols('u t a')
P=s.expand((u-a)*(u**2+1)+t*(u-1)*(u**2-u+1))
L=(1+t)*u-(a+t)
H=s.expand(-s.discriminant(P,u))
expected=s.expand(3*t**4+(10*a+10)*t**3+(59*a*a-70*a+59)*t*t+
    (28*a**3-4*a*a-4*a+28)*t+4*a**4+8*a*a+4)
assert s.expand(H-expected)==0
assert s.factor(s.resultant(P,L,u))==t*(a-1)*(t+a)*(t+1)
assert s.factor(s.discriminant(s.expand(P*L),u)) == s.factor(-t**2*(a-1)**2*(t+a)**2*(t+1)**2*H)
assert s.factor(s.discriminant(H,t))==512*(a-1)**4*(a*a-a+1)*(71*a*a-196*a+71)**3
assert s.factor(H.subs(t,0))==4*(a*a+1)**2
assert s.factor(H.subs(t,-1))==(a-2)**2*(4*a*a-12*a+7)
assert s.factor(H.subs(t,-a))==(2*a-1)**2*(7*a*a-12*a+4)
exceptional=[a*a+1,a-2,2*a-1,4*a*a-12*a+7,7*a*a-12*a+4,71*a*a-196*a+71,a*a-a+1,a,a-1]
assert all(s.resultant(f,g,a)!=0 for i,f in enumerate(exceptional) for g in exceptional[:i])
M=(a+2*t)**2-3*(1+t)*(1+2*t)
N=(a+2*t)**3-27*(1+t)**2*(a+t)
assert s.factor(s.resultant(M,N,t))==-27*(a-2)**3*(a-1)*(71*a*a-196*a+71)
for r in [s.sqrt(3),-s.sqrt(3)]:
    aa=s.Rational(98,71)+s.Rational(39,71)*r
    tt=-s.Rational(52,71)-s.Rational(12,71)*r
    uu=-2-r
    pol=s.factor(P.subs({a:aa,t:tt}),extension=True)
    assert s.simplify(pol - (1+tt)*(u-uu)**3)==0
    assert s.simplify(L.subs({a:aa,t:tt,u:uu}))!=0
    assert s.simplify(H.subs({a:aa,t:tt}))==0
    assert s.simplify(s.diff(H,t).subs({a:aa,t:tt}))==0
    assert s.simplify(s.diff(H,t,2).subs({a:aa,t:tt}))!=0
print('SULUYER_KODAIRA_DISCRIMINANT_EXACT_OK')
