#!/usr/bin/env python3
import sympy as sp
n,R,a,q,t=sp.symbols('n R a q t', positive=True)
k=(n-1)/n
d=(n-2)/n
kh=k*d
A=R-1
B=(1-t)*A/k+t*A/d
z=(1-(1-q)*(B+1)/R)/(a+R)
P=(1-t)*A/k
T=t*A/kh
cp=P/z
ct=T/z**2
y=(B+1)/R
tau=R/(n-2)
x=R*y/tau
E=[
 sp.simplify(tau*x-1-cp*z-k*ct*z**2),
 sp.simplify(tau*x*(n-2)-cp*k*x*z-x-ct*kh*x*z**2),
 sp.simplify(2*tau*x-2*y-2*cp*k*y*z-2*ct*kh*y*z**2),
 sp.simplify(-a*z+cp*(k*y*z-k*z**2-z)+(q*y-z)+ct*kh*y*z**2-ct*k*z**2-ct*kh*z**3),
]
assert all(e==0 for e in E), E
zp=sp.simplify(z.subs(t,0)); zt=sp.simplify(z.subs(t,1))
cpstar=sp.simplify(A/(k*zp)); ctstar=sp.simplify(A/(kh*zt**2))
Fp=(R*(n*q-1)+(1-q))/(n*R)
Ft=(n-1)/(n**2*(n-2))*((R*(n*q-2)+2*(1-q))/R)**2
assert sp.simplify(cpstar-(a+R)*A/Fp)==0
assert sp.simplify(ctstar-(a+R)**2*A/Ft)==0
r=sp.symbols('r', positive=True)
D=1-t+t*r
lhs=(1-t)/D+t*r**2/D**2
rhs=1-t*(1-t)*r*(1-r)/D**2
assert sp.simplify(lhs-rhs)==0
qmint=2*A/(R*n-2)
assert sp.simplify(zt.subs(q,qmint))==0
# Exact rational check at Figure 5(b) parameters.
vals={n:sp.Integer(5),R:sp.Rational(21,10),a:sp.Integer(1),q:sp.Rational(3,5),t:sp.Rational(1,2)}
qmin_num=sp.simplify(qmint.subs(vals))
assert qmin_num==sp.Rational(22,85) and vals[q]>qmin_num
zp_num=sp.simplify(zp.subs(vals)); zt_num=sp.simplify(zt.subs(vals))
r_num=sp.simplify(zt_num/zp_num)
D_num=sp.simplify((1-t+t*r).subs({t:vals[t],r:r_num}))
S_num=sp.simplify(((1-t)/D+t*r**2/D**2).subs({t:vals[t],r:r_num}))
assert 0<r_num<1 and S_num<1
print('VERIFY_OK')
print('q_min_t =', qmin_num)
print('z_p =', zp_num, 'z_t =', zt_num, 'r =', r_num)
print('midpoint normalized threshold sum =', S_num)
