#!/usr/bin/env python3
"""Reproduce symbolic flip identities and two high-precision local examples."""
import sympy as sp
import mpmath as mp

A, R, K, y, x = sp.symbols('A R K y x', positive=True)
f = y * sp.exp((R-K*y**A-A*y)/A)
subs = {R: x+A*y, K: x/y**A}
assert sp.simplify(sp.diff(f,y).subs(subs).subs(x,2-y)+1) == 0
assert sp.simplify(sp.diff(f,y,2).subs(subs).subs(x,2-y)
                   +(A-1)*(2-y)/y) == 0
assert sp.simplify(sp.diff(f,y,3).subs(subs).subs(x,2-y)
                   -(4+(5-A)*(A-1)*(2-y))/y**2) == 0
T = sp.symbols('T', real=True)
a2 = -T/(2*y)
a3 = (4+(5-A)*T)/(6*y**2)
Q = 3*T**2+2*(5-A)*T+8
assert sp.simplify(a2**2+a3-Q/(12*y**2)) == 0
# Implicit fixed point derivative at the flip where K*y**A+ A*y=R and x+y=2.
dy_dK = -y**A/(A*(K*y**(A-1)+1))
assert sp.simplify((A-1)*dy_dK.subs(K,(2-y)/y**A)
                   +(A-1)*y**(A+1)/(2*A)) == 0
assert sp.simplify(sp.discriminant(Q,T) - 4*((A-5)**2-24)) == 0
for alpha, t, expected_sign in [(sp.Integer(2),sp.Integer(1),1),
                                (sp.Integer(10),sp.Rational(5,3),-1)]:
    r = 2*alpha-t
    yy = sp.factor((r-2)/(alpha-1))
    xx = sp.factor(t/(alpha-1))
    kk = xx/yy**alpha
    assert 2<r<2*alpha and xx>0 and yy>0 and kk>0
    assert xx+yy == 2 and xx+alpha*yy == r
    qval = sp.factor(Q.subs({A:alpha,T:t}))
    assert sp.sign(qval)==expected_sign
    fconcrete = f.subs({A:alpha,R:r,K:kk})
    assert all(sp.simplify(sp.diff(fconcrete,y,j).subs(y,yy)-v)==0
               for j,v in [(1,-1),(2,-t/yy),
                           (3,(4+(5-alpha)*t)/yy**2)])
# Numerical illustrations only; general existence and flip type follow from proof.
mp.mp.dps = 70
for alpha,t,factor,want_attraction in [(2,mp.mpf(1),mp.mpf('1.0001'),True),
                                       (10,mp.mpf(5)/3,mp.mpf('0.999999'),False)]:
    r=2*alpha-t
    yc=(r-2)/(alpha-1)
    xc=t/(alpha-1)
    kc=xc/yc**alpha
    k=kc*factor
    root=mp.findroot(lambda z:k*z**alpha+alpha*z-r,(yc*mp.mpf('.99'),yc*mp.mpf('1.01')))
    F=lambda z:z*mp.exp((r-k*z**alpha-alpha*z)/alpha)
    Fprime=lambda z:mp.exp((r-k*z**alpha-alpha*z)/alpha)*(1-k*z**alpha-z)
    initial_guess= root-mp.mpf('.006')
    lo=mp.findroot(lambda z:F(F(z))-z,(initial_guess,initial_guess+mp.mpf('1e-5')))
    hi=F(lo)
    assert lo>0 and hi>0 and lo<root<hi
    assert abs(F(hi)-lo)<mp.mpf('1e-45')
    mult=Fprime(lo)*Fprime(hi)
    assert (abs(mult)<1)==want_attraction
print('VERIFY_OK: general symbolic identities, rational criticality examples, and two local cycle checks')
