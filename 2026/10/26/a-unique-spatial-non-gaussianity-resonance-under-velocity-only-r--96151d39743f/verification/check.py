#!/usr/bin/env python3
"""Independent finite symbolic algebra checks for a velocity-reset oscillator.

This script verifies rational moment identities only. Existence, uniqueness and
all-rate global optimization are proved separately in the mathematical text.
"""
import sympy as s

x,v=s.symbols('x v')
k,g,r,T=s.symbols('k g r T', positive=True)

def generator(f):
    return s.expand(v*s.diff(f,x)+(-k*x-g*v)*s.diff(f,v)+g*T*s.diff(f,v,2)+r*(f.subs(v,0)-f))

def solve_degree(n,prior):
    mon=[(i,n-i) for i in range(n+1)]
    a=s.zeros(len(mon)); rhs=s.zeros(len(mon),1)
    for row,(i,j) in enumerate(mon):
        polynomial=generator(x**i*v**j)
        p=s.Poly(polynomial,x,v)
        for col,(ii,jj) in enumerate(mon):
            a[row,col]=p.coeff_monomial(x**ii*v**jj)
        for (ii,jj),expected in prior.items():
            rhs[row]-=p.coeff_monomial(x**ii*v**jj)*expected
    assert s.factor(a.det())!=0
    ans=a.inv()*rhs
    return dict(zip(mon,[s.factor(t) for t in ans]))

second=solve_degree(2,{(0,0):s.S.One})
fourth=solve_degree(4,second)
D=r**3+9*g*r**2+(26*g**2+10*k)*r+24*g**3+32*g*k
assert s.factor(second[(2,0)]-2*g*T/(k*(2*g+r)))==0
assert s.factor(second[(0,2)]-2*g*T/(2*g+r))==0
assert s.factor(second[(1,1)])==0
m40=12*g**2*T**2*(12*g**2+7*g*r+16*k+r**2)/(k**2*(2*g+r)*D)
m04=24*g**2*T**2*(6*g**2+5*g*r+8*k+r**2)/((2*g+r)*D)
assert s.factor(fourth[(4,0)]-m40)==0
assert s.factor(fourth[(0,4)]-m04)==0
assert s.factor(fourth[(3,1)])==0
assert s.factor(fourth[(1,3)]-12*g**2*T**2*r/((2*g+r)*D))==0
assert s.factor(fourth[(2,2)]-4*g**2*T**2*(12*g**2+7*g*r+16*k+r**2)/(k*(2*g+r)*D))==0
ax=s.factor(fourth[(4,0)]/(3*second[(2,0)]**2)-1)
av=s.factor(fourth[(0,4)]/(3*second[(0,2)]**2)-1)
assert s.factor(ax-6*k*r/D)==0
assert s.factor(av-r*(r**2+5*g*r+6*g**2+6*k)/D)==0
assert s.factor(s.diff(ax,r)-6*k*(24*g**3+32*g*k-9*g*r**2-2*r**3)/D**2)==0
assert s.limit(av,r,s.oo)==1
assert s.limit(ax,r,s.oo)==0
assert s.limit(ax,r,0)==0
assert s.limit(ax/r,r,0)==6*k/(24*g**3+32*g*k)
# independent stationarity check at rational parameter points
for kg,gg,rr,tt in [(1,1,1,1),(2,3,s.Rational(5,2),7),(s.Rational(5,3),s.Rational(7,4),4,s.Rational(2,5)),(9,2,8,3)]:
    data={k:kg,g:gg,r:rr,T:tt}
    mom={**second,**fourth,(0,0):s.S.One}
    for n in (2,4):
        for i in range(n+1):
            j=n-i
            check=s.Poly(generator(x**i*v**j),x,v)
            z=sum(s.factor(coef*mom[exps]) for exps,coef in check.terms())
            assert s.factor(z.subs(data))==0
print('PASS: full degree-two/four generator systems and four exact-rational specializations')
