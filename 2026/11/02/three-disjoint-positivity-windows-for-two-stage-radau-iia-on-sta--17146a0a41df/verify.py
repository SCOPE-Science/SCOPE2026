#!/usr/bin/env python3
"""Exact algebra and small-matrix replay for the star diffusion theorem.
Requires Python 3 and SymPy. This checks identities and examples; the proof
of the all-parameter root and sign classification is in RESULT.md.
"""
import sympy as S

checks=0
def eq(x,y):
    global checks
    assert S.cancel(x-y)==0,(x,y)
    checks+=1

def test(t):
    global checks
    assert bool(t),t
    checks+=1

h,m,x = S.symbols('h m x', positive=True)
r=lambda z:(6-2*z)/(z*z+4*z+6)
a,b=r(h),r((m+1)*h)
Da=h*h+4*h+6
Db=(m+1)**2*h*h+4*(m+1)*h+6
F=(m+1)*h**4+(-2*m*m+2*m+10)*h**3+(6*m*m+4*m+16)*h**2+(24*m+12)*h+36
H=(1+m*b)/(m+1)
T=(1-b)/(m+1)
D=(m+b+(m*m-1)*a)/(m*(m+1))
E=(m+b-(m+1)*a)/(m*(m+1))
eq(H,((m+1)*h*h+(4-2*m)*h+6)/Db)
eq(T,h*((m+1)*h+6)/Db)
eq(D,F/(Da*Db))
eq(E,h*h*((m+1)*h*h+(6*m+12)*h+18)/(Da*Db))
eq(H+m*T,1)
eq(T+D+(m-1)*E,1)
eq(S.diff(r(x),x),2*(x*x-6*x-18)/(x*x+4*x+6)**2)
eq(r(3+3*S.sqrt(3)),(5-3*S.sqrt(3))/2)
eq(F.subs(h,8),-4*(160*m*m-1392*m-2593))
eq(S.limit(F.subs(h,3+x/m)/m,m,S.oo),243-18*x)
eq(S.limit(F.subs(h,2*m+x)/m**4,m,S.oo),8*(x+7))

# Rational exact full Laplacian evaluation in representative safe/unsafe regimes.
for mm in (2,3,5,10,11,12):
    n=mm+1
    L=S.zeros(n,n)
    for j in range(1,n):
        L[0,0]+=1;L[j,j]+=1;L[0,j]=-1;L[j,0]=-1
    for hh in (S.Rational(1,4), S.Rational(1,2), S.Rational(3,4),
               S.Integer(2),S.Integer(3),S.Integer(8),S.Integer(16)):
        W=hh*L
        P=(6*S.eye(n)-2*W)*(W*W+4*W+6*S.eye(n)).inv()
        hv=S.cancel(H.subs({m:mm,h:hh}))
        tv=S.cancel(T.subs({m:mm,h:hh}))
        dv=S.cancel(D.subs({m:mm,h:hh}))
        ev=S.cancel(E.subs({m:mm,h:hh}))
        for i in range(n):
            eq(sum(P[i,j] for j in range(n)),S.Integer(1))
            for j in range(n):
                expect=hv if i==j==0 else (tv if i==0 or j==0 else (dv if i==j else ev))
                eq(P[i,j],expect)
        test(tv>0);test(ev>0)
        if mm<=10: test(hv>0 and dv>0)

# Witnesses for two different failure mechanisms at the first failing size.
for hh in (S.Rational(3,4),S.Integer(8)):
    if hh<S.Integer(2): test(S.factor(H.subs({m:11,h:hh}))<0)
    else: test(S.factor(D.subs({m:11,h:hh}))<0)
test(S.factor(F.subs({m:11,h:8}))<0)
test(S.factor(F.subs({m:10,h:8}))>0)
for mm in (11,12,20,100):
    poly=S.Poly(F.subs(m,mm),h)
    test(poly.count_roots(0,S.oo)==2)
    test(S.factor(F.subs({m:mm,h:8}))<0)
    disc=mm*mm-10*mm-2
    test(disc>0)
    left=(mm-2-S.sqrt(disc))/(mm+1)
    right=(mm-2+S.sqrt(disc))/(mm+1)
    test(0<left<right<2)
print('PASS',checks,'exact symbolic/rational/root assertions')
