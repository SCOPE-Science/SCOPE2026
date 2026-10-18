"""Reproduce algebraic and finite-matrix checks for the universal-hub pinning theorem.

Run with Python 3 plus sympy, numpy, scipy. Finite tests supplement the proof.
"""
from fractions import Fraction
import math
import random
import sympy as s
import numpy as np
from scipy.optimize import minimize_scalar

checks = 0

def eq(left, right):
    global checks
    assert s.simplify(left-right) == 0, (left,right)
    checks += 1

def ok(test):
    global checks
    assert bool(test)
    checks += 1

m,y,B,u=s.symbols('m y B u', positive=True)
x=B-2*m*y
F=(2*m-2)/(m+1+y)+1/(2*m+1+y) + (2*m+x+1+y)/((2*m+x)*(1+y)-2*m)
P=y+2-4*m*(m-1)*y/(m+1+y)**2-2*m*y/(2*m+1+y)**2
D_boundary=s.factor(s.diff(F,y).subs(y,B/(2*m)))
eq(D_boundary, P.subs(y,B/(2*m))/(2*m*(B/(2*m))))
eq(s.diff(F,y).subs(y,0), -1-4*m/B-(2*m-2)/(m+1)**2-1/(2*m+1)**2)

N=s.cancel(P*(m+1+y)**2*(2*m+1+y)**2)
poly=s.Poly(N,y)
coeffs=[1,6*(m+1),9*m*m+32*m+14,-2*(2*m**3-28*m*m-29*m-8),-12*m**4+34*m**3+73*m*m+44*m+9,2*(m+1)**2*(2*m+1)**2]
for k,c in zip(range(5,-1,-1),coeffs):eq(poly.coeff_monomial(y**k),c)
H=980*m**5-6516*m**4-13437*m**3-10314*m*m-3645*m-486
eq(P.subs(y,m/3),-H/(3*(4*m+3)**2*(7*m+3)**2))
shift_H=s.Poly(s.expand(H.subs(m,u+9)),u)
for i in range(6):ok(shift_H.nth(i)>0)
shift_C=s.Poly(s.expand((-coeffs[4]).subs(m,u+9)),u)
for i in range(5):ok(shift_C.nth(i)>0)

# Uniform strict positivity for dimensions m=2,...,8.  For fixed y>0,
# m(m-1)/(m+1+y)^2 increases with m; 2m/(2m+1+y)^2
# never exceeds 1/[4(1+y)]. The resulting quartic is positive.
G=y+2-224*y/(y+9)**2-y/(4*(1+y))
Q=4*y**4+83*y**3-366*y*y+139*y+648
eq(G,Q/(4*(1+y)*(y+9)**2))

def bernstein_coefficients(f,L,R,n=4):
    t=s.symbols('t')
    fp=s.Poly(s.expand(f.subs(y,L+(R-L)*t)),t)
    aa=[fp.nth(i) for i in range(n+1)]
    return [s.simplify(sum(aa[j]*s.binomial(k,j)/s.binomial(n,j) for j in range(k+1))) for k in range(n+1)]

b0=bernstein_coefficients(Q,0,2)
b1=bernstein_coefficients(Q,2,3)
ok(b0==[648,s.Rational(1435,2),543,s.Rational(581,2),190])
ok(b1==[190,s.Rational(559,4),s.Rational(255,2),182,336])
for coeff in b0+b1:ok(coeff>0)
# For y >= 3, Q is a polynomial with strictly positive coefficients in y-3.
z=s.symbols('z')
qshift=s.Poly(s.expand(Q.subs(y,3+z)),z)
ok([qshift.nth(i) for i in range(5)]==[336,616,597,131,4])

# Two-root / asymptotic certificates, purely symbolic.
low_lim=s.limit(P,m,s.oo)
eq(low_lim,2-3*y)
z=s.symbols('z',positive=True)
high_lim=s.limit(P.subs(y,m*z)/m,m,s.oo)
eq(high_lim,z*(1-4/(1+z)**2))

# Exact sign witnesses, including the first reentrant case.
mm=9
def Pr(mm,yy):
    return yy+2-Fraction(4*mm*(mm-1),1)*yy/(mm+1+yy)**2 -Fraction(2*mm,1)*yy/(2*mm+1+yy)**2
ok(Pr(9,Fraction(3,1))==-Fraction(9161,40898))
for budget,expect in [(1,1),(54,-1),(200,1)]:
    v=Pr(9,Fraction(budget,18))
    ok((v>0)-(v<0)==expect)

# Direct construction of K_1 join K_{m,m}; independently check spectral trace.
def lap(mm):
    n=2*mm+1
    L=np.zeros((n,n))
    for i in range(1,n):
        L[0,0]+=1.;L[i,i]+=1.;L[0,i]-=1.;L[i,0]-=1.
    for i in range(1,mm+1):
        for j in range(mm+1,2*mm+1):
            L[i,i]+=1.;L[j,j]+=1.;L[i,j]-=1.;L[j,i]-=1.
    return L

def ff(mm,bb,yy):
    xx=bb-2*mm*yy
    return (2*mm-2)/(mm+1+yy)+1/(2*mm+1+yy)+(2*mm+xx+1+yy)/((2*mm+xx)*(1+yy)-2*mm)

rng=random.Random(345)
for mm in [2,3,4,5,8,9,10,15,21]:
    L=lap(mm)
    ok(np.linalg.norm(L-L.T)<1e-13)
    for bb in [0.2,1.,5.,25.,54.,125.,2*mm*mm]:
        for f in [0.,.05,.2,.5,.9,1.]:
            yy=f*bb/(2*mm)
            xx=bb-2*mm*yy
            arr=np.array([xx]+[yy]*(2*mm))
            A=L+np.diag(arr)
            val=np.trace(np.linalg.inv(A))
            ok(abs(val-ff(mm,bb,yy))<1e-8*max(1.,abs(val)))
        ymax=bb/(2*mm)
        sol=minimize_scalar(lambda yy:ff(mm,bb,yy),bounds=(0.,ymax),method='bounded',options={'xatol':1e-12})
        at_boundary=float(Pr(mm,Fraction(str(bb))/Fraction(2*mm)))<=0
        if at_boundary:
            ok(ff(mm,bb,ymax)<=sol.fun+1e-8)
        else:
            ok(sol.x < ymax+1e-7)
            ok(sol.fun < ff(mm,bb,ymax)+1e-5)
        best=min(sol.fun,ff(mm,bb,ymax))
        if mm<=10:
            for k in range(8):
                a=np.array([rng.expovariate(1.) for _ in range(2*mm+1)])
                a=bb*a/a.sum()
                test=float(np.trace(np.linalg.inv(L+np.diag(a))))
                ok(test>=best-1e-7*max(1,best))

print('PASS:',checks,'algebraic and matrix assertions')
