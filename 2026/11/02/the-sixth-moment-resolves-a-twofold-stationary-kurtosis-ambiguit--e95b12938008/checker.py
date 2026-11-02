#!/usr/bin/env python3
"""Exact reproducibility of stationary moment inversion for Brownian-reset drive."""
import sympy as S
b,c=S.symbols('b c', positive=True)
M={(0,0):S.Integer(1)}
# Normalize r=D=1 and mu=1/b; all even moments scale as (D/r)^n.
for n in range(1,7):
    for p in range(n+1):
        q=n-p
        if n%2:
            M[p,q]=S.Integer(0)
            continue
        above=p*M.get((p-1,q+1),S.Integer(0)) if p else S.Integer(0)
        diffusion=q*(q-1)*M.get((p,q-2),S.Integer(0)) if q>1 else S.Integer(0)
        M[p,q]=S.factor((above+diffusion)/(p/b+(1 if q>0 else 0)))
P=lambda z:z**6+61*z**5+2393*z**4+12443*z**3+22614*z**2+16344*z+4320
p=lambda z:z**2+19*z+12
q=lambda z:(z+2)*(z+3)
Q=lambda z:(z+2)**2*(z+3)**2*(z+4)*(z+5)
expect2=2*b**2/(1+b)
expect4=12*b**4*p(b)/((1+b)**2*q(b))
expect6=120*b**6*P(b)/((1+b)**3*Q(b))
for d,expected in [(2,expect2),(4,expect4),(6,expect6)]:
    assert S.factor(M[d,0]-expected)==0, d
K=lambda z:p(z)/q(z)
H=lambda z:P(z)/Q(z)
psi=3*(9-b)/(7*b+3)
assert S.factor((p(b)*q(c)-p(c)*q(b))+2*(b-c)*(7*b*c+3*b+3*c-27))==0
assert S.factor(S.diff(K(b),b)+2*(7*b**2+6*b-27)/q(b)**2)==0
assert S.factor(K(b)-2-b*(9-b)/q(b))==0
assert S.factor(K(b)-K(psi))==0
assert S.factor(psi.subs(b,psi)-b)==0
R=357*b**6+2030*b**5-436986*b**4-2517506*b**3-4533183*b**2-2618136*b-449280
den=11*(b+2)**2*(b+3)**2*(b+4)*(b+5)*(16*b+21)*(25*b+39)
assert S.factor(H(b)-H(psi)+2*(7*b**2+6*b-27)*R/den)==0
assert 357*81+2030*9==47187 and 47187<436986
for x in [S.Rational(1,10),S.Rational(1,2),S.Rational(1),S.Rational(2),S.Rational(4),S.Rational(17,2)]:
    y=S.factor(psi.subs(b,x))
    assert x>0 and y>0 and x!=y
    assert S.factor(K(x)-K(y))==0
    assert S.factor(H(x)-H(y))!=0
    v=S.Rational(7,3)
    sb=v*(1+x)/(2*x**2);sc=v*(1+y)/(2*y**2)
    assert S.factor((expect2.subs(b,x)*sb)-(expect2.subs(b,y)*sc))==0
    assert S.factor((expect4.subs(b,x)*sb**2)-(expect4.subs(b,y)*sc**2))==0
    assert S.factor((expect6.subs(b,x)*sb**3)-(expect6.subs(b,y)*sc**3))!=0
print('PASS: independent stationary generator recurrence, exact moment formulas, involution, derivative, sixth-ratio factorization, polynomial sign bound, and rational indistinguishable-pair certificates.')
