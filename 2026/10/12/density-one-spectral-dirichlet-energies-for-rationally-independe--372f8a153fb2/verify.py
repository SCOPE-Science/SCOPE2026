#!/usr/bin/env python3
"""Symbolic cell-secular reconstruction at a single-edge Dirichlet momentum.

Dependency: sympy. This checks an algebraic proof step, not the
infinite equidistribution theorem (whose proof is in RESULT.md).
"""
import math
import sympy as S

k,z,w,p,q=S.symbols('k z w p q',nonzero=True)
I=S.I
T=S.symbols('T',nonzero=True)  # exp(i*k*a/2), at k*a=m*pi
u=S.Matrix(S.symbols('a0:6'))
Aplus,Aminus,Bplus,Bminus,Cplus,Cminus=u
p1=Aplus*T+Aminus/T; dp1=I*k*(Aplus*T-Aminus/T)
p2=Bplus+Bminus; dp2=I*k*(Bplus-Bminus)
p3=Cplus+Cminus; dp3=I*k*(Cplus-Cminus)
f1=Aplus/T+Aminus*T; df1=I*k*(Aplus/T-Aminus*T)
f2=(Bplus*z+Bminus/z)*p; df2=I*k*(Bplus*z-Bminus/z)*p
f3=(Cplus*w+Cminus/w)*q; df3=I*k*(Cplus*w-Cminus/w)*q
fs=[-p2-p1-I*(dp2+dp1),
    -p3-p2+I*(-dp3+dp2),
    -p1-p3+I*(dp1+dp3),
    -f2-f1+I*(df2+df1),
    -f3-f2+I*(df3-df2),
    -f1-f3-I*(df1+df3)]
M=S.Matrix([[S.expand(f).coeff(x) for x in u] for f in fs])
sb=(z-1/z)/(2*I); sc=(w-1/w)/(2*I)
c1=(q+1/q)/2; c2=(p+1/p)/2
sbc=(z*w-1/(z*w))/(2*I)
# The direct vertex matrix uses interchanged names for the two Bloch
# coordinates relative to equation (19); their independent ranges agree.
for Tvalue, epsilon in [(I,-1),(-I,-1),(-S.Integer(1),1),(S.Integer(1),1)]:
    det=S.factor(M.subs(T,Tvalue).det(method='domain-ge'))
    F=(k*k-1)*(sb*c1+sc*c2)-epsilon*(k*k+1)*sbc
    assert S.cancel(det-64*I*k*k*p*q*F)==0

a=1.0
b=.5+math.sqrt(2)/1000
c=.5+math.sqrt(3)/1000
kp=math.pi
r=((kp*kp+1)/(kp*kp-1)
  * math.sin(math.pi*(math.sqrt(2)+math.sqrt(3))/1000)
  / (math.cos(math.pi*math.sqrt(2)/1000)+math.cos(math.pi*math.sqrt(3)/1000)))
assert 0<r<.017
th=math.acos(r)
res=(kp*kp-1)*(math.sin(kp*b)*math.cos(th)+math.sin(kp*c)*math.cos(th))
res+=(kp*kp+1)*math.sin(kp*(b+c))
assert abs(res)<1e-11
assert (kp*kp+1)*abs(math.sin((b+c)*kp)) < (kp*kp-1)*(abs(math.sin(b*kp))+abs(math.sin(c*kp)))
print('VERIFY_OK exact_determinant_identity irrational_witness strict_membership')
