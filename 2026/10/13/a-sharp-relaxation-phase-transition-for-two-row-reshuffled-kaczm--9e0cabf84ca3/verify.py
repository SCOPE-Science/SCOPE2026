#!/usr/bin/env python3
"""Independent-by-construction algebraic checks of the stated finite matrix identities."""
from fractions import Fraction as F
from math import sqrt
import sympy as sp

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in (0,1)) for j in (0,1)] for i in (0,1)]
def tr(A): return A[0][0]+A[1][1]
def det(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def T(A): return [[A[j][i] for j in (0,1)] for i in (0,1)]
def gr(A): return mm(T(A),A)
def add(A,B): return [[A[i][j]+B[i][j] for j in (0,1)] for i in (0,1)]

tests=0
for t in [F(1,11),F(1,3),F(1,2),F(2,3),F(3,4),F(7,8)]:
    c=(1-t*t)/(1+t*t)
    s=2*t/(1+t*t)
    a=(F(1),F(0)); b=(c,s)
    for w in [F(-1,2),F(0),F(1,5),F(1),F(7,6),F(4,3),F(9,5),F(2),F(5,2)]:
        def op(v): return [[(F(1) if i==j else F(0))-w*v[i]*v[j] for j in (0,1)] for i in (0,1)]
        U,V=op(a),op(b)
        S=add(gr(mm(U,V)),gr(mm(V,U)))
        Q=[[v/F(2) for v in row] for row in S]
        scalar=c*c*w*w*(w-2)*(w-2)+2*(w-1)*(w-1)
        delta=c*w*(w-2)*(c*c*w*w-2*w+2)
        assert tr(Q)==scalar
        assert tr(Q)**2-4*det(Q)==delta**2
        tests+=2

c,w,u,t=sp.symbols('c w u t', real=True)
S=c*c*w*w*(2-w)**2+2*(w-1)**2
D=c*w*(w-2)*(c*c*w*w-2*w+2)
Qfirst=(S+D)/2
Qsecond=(S-D)/2
Fpoly=2*c*c*w**3-3*c*c*w*w+3*c*w*w-4*c*w+2*w-2
Gpoly=2*c*c*w**3-3*c*c*w*w-3*c*w*w+4*c*w+2*w-2
assert sp.expand(sp.diff(Qfirst,w)-(1+c)*Gpoly)==0
assert sp.expand(sp.diff(Qsecond,w)-(1-c)*Fpoly)==0
assert sp.expand(Gpoly.subs(w,1+u)-((1-c)*(c+2*u-3*c*u*u)+2*c*c*u**3))==0
assert sp.factor(Fpoly.subs({w:1+t*t/2,c:t/(1+t*t/2)})-t*(t**3+sp.Rational(3,2)*t*t-1))==0

root=sp.nroots(2*t**3+3*t*t-2,maxsteps=300)[0]
# Select the positive real root independently of output ordering.
roots=[complex(z) for z in sp.nroots(2*t**3+3*t*t-2,maxsteps=300)]
root=next(z.real for z in roots if abs(z.imag)<1e-10 and z.real>0)
crit=root/(1+root*root/2)
assert .5511124055<crit<.5511124056
for cc in (.05,.25,.5,.6,.8,.99):
    def Fval(x): return float(Fpoly.subs({c:cc,w:x}))
    left,right=1.,2.
    for k in range(65):
        mid=(left+right)/2
        if Fval(mid)<0:left=mid
        else:right=mid
    station=(left+right)/2
    crossover=2/(1+sqrt(1-2*cc*cc)) if 2*cc*cc<1 else None
    optimum=crossover if cc<=crit else station
    def risk(x):
        SS=cc*cc*x*x*(2-x)**2+2*(x-1)**2
        DD=cc*x*(x-2)*(cc*cc*x*x-2*x+2)
        return (SS+abs(DD))/2
    for h in (-.0001,-.00001,.00001,.0001):
        assert risk(optimum)<=risk(optimum+h)+1e-11
    assert risk(optimum)<risk(1)
print('PASS',tests,'exact rational Gram invariants, 4 symbolic polynomial checks, 6 optimum checks')
