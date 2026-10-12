#!/usr/bin/env python3
"""Exact symbolic verification of a two-sampling Kaczmarz phase diagram.

Run: python verify.py
Requires: sympy (only for symbolic polynomial algebra).
"""
from itertools import permutations, product
from fractions import Fraction
import sympy as s

h, t, sigma = s.symbols('h t sigma', positive=True, real=True)
U = [s.Matrix([1,0]), s.Matrix([-s.Rational(1,2),s.sqrt(3)/2]),
     s.Matrix([-s.Rational(1,2),-s.sqrt(3)/2])]
I = s.eye(2)
AA = [I-h*u*u.T for u in U]
assert sum(U,s.zeros(2,1)) == s.zeros(2,1)
assert s.simplify(sum((u*u.T for u in U),s.zeros(2,2))) == 3*I/2

pairs=[]
for pi in permutations(range(3)):
    M,v=I,s.zeros(2,1)
    for ix in pi:
        M=AA[ix]*M
        v=AA[ix]*v+h*U[ix]
    pairs.append((M,v))
Emtm=s.simplify(sum((M.T*M for M,v in pairs),s.zeros(2,2))/6)
Emtv=s.simplify(sum((M.T*v for M,v in pairs),s.zeros(2,1))/6)
Ev2=s.simplify(sum(((v.T*v)[0] for M,v in pairs),s.Integer(0))/6)
c=1-3*h+3*h*h-h**3+h**6/32
p=h**4*(h*h+6*h+12)/16
q=1-h+h*h/2
b=q**3
di=h*h*(1+q+q*q)
assert s.simplify(Emtm-c*I)==s.zeros(2,2)
assert Emtv==s.zeros(2,1)
assert s.expand(Ev2-p)==0
assert s.factor(c-b)==-3*h*h*(h-2)**4/32
P4=3*h**4-22*h**3+28*h*h-48*h+48
P3=h**3+2*h*h+6*h-12
Q=h**4+2*h**3+4*h*h-24*h+48
assert s.factor(p-di)==-h*h*P4/16
assert s.factor(1-c-h*(2-h)*Q/32)==0
Vrr=s.factor(p/(1-c))
Viid=s.factor(di/(1-b))
assert s.factor(Viid-2*h/(2-h))==0
assert s.factor(Vrr-Viid+8*h*P3/((h-2)*Q))==0
assert s.cancel((1+t)**4*P4.subs(h,2*t/(1+t)) -
                (-64*t**4-48*t**3+112*t*t+96*t+48))==0
assert s.cancel((1+t)**4*Q.subs(h,2*t/(1+t)) -
                (48*t**4+96*t**3+160*t*t+144*t+48))==0
assert P4.subs(h,s.Rational(59,50))>0
assert P4.subs(h,s.Rational(119,100))<0
assert P3.subs(h,s.Rational(121,100))<0
assert P3.subs(h,s.Rational(61,50))>0
# Direct 27 equiprobable IID paths; independent of moment recursion.
for hh in [s.Rational(1,4),s.Rational(2,3),s.Rational(1),s.Rational(6,5),s.Rational(3,2),s.Rational(15,8)]:
    AA0=[z.subs(h,hh) for z in AA]
    UU=[hh*u for u in U]
    for initial in [s.Matrix([0,0]),s.Matrix([1,-2])]:
        E_rr=s.Integer(0)
        for pi in permutations(range(3)):
            x=initial
            for j in pi:x=AA0[j]*x+UU[j]
            E_rr+=(x.T*x)[0]/6
        E_iid=s.Integer(0)
        for pi in __import__('itertools').product(range(3),repeat=3):
            x=initial
            for j in pi:x=AA0[j]*x+UU[j]
            E_iid+=(x.T*x)[0]/27
        assert s.simplify(E_rr-(c.subs(h,hh)*(initial.T*initial)[0]+p.subs(h,hh)))==0
        assert s.simplify(E_iid-(b.subs(h,hh)*(initial.T*initial)[0]+di.subs(h,hh)))==0
# A witnessed finite-horizon reversal at h=6/5, x0=0.
H=s.Rational(6,5)
c0,b0,p0,di0=[s.factor(v.subs(h,H)) for v in (c,b,p,di)]
first=p0-di0
second=p0*(1+c0)-di0*(1+b0)
assert first==s.Rational(1512,15625) and second<0
# Independent two-epoch enumeration in a rational basis (second coordinate is sqrt(3) times stored coefficient).
UV = ((Fraction(1),Fraction(0)),(Fraction(-1,2),Fraction(1,2)),(Fraction(-1,2),Fraction(-1,2)))
HF=Fraction(6,5)
def path_sq(indices, xx):
    a,b=xx
    for j in indices:
        ua,ub=UV[j]
        alpha=HF*(1-ua*a-3*ub*b)
        a+=alpha*ua
        b+=alpha*ub
    return a*a+3*b*b
for xx in ((Fraction(0),Fraction(0)),(Fraction(1),Fraction(-2))):
    rr=sum((path_sq(pi+pj,xx) for pi,pj in product(permutations(range(3)),repeat=2)),Fraction(0))/36
    iid=sum((path_sq(indices,xx) for indices in product(range(3),repeat=6)),Fraction(0))/729
    n0=xx[0]**2+3*xx[1]**2
    assert rr==Fraction(s.factor(p0*(1+c0)+c0**2*n0))
    assert iid==Fraction(s.factor(di0*(1+b0)+b0**2*n0))
print('VERIFY_OK 6-permutation exact moment identities; 12 direct enumeration settings (396 paths); 1530 two-epoch paths; polynomial certificates; one-to-two epoch reversal')
print('h=6/5 first RR-IID:',first,'second:',second)
print('unique roots approximately:',s.nroots(P4,maxsteps=100)[0],s.nroots(P3,maxsteps=100)[0])
