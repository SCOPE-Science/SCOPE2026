#!/usr/bin/env python3
"""Exact rational checks of a two-group critical SAIRS Lyapunov identity.

This checks algebra on one example. The theorem for every group count
is established by the mathematical proof, not by finite sampling.
"""
from fractions import Fraction as F

B=((F(2),F(1)),(F(1),F(2)))
n=2
mu=nu=gamma=alpha=delta_a=delta_i=F(1)
s=F(2,3)
kappa=mu+nu+gamma
d_a=alpha+delta_a+mu
d_i=delta_i+mu
K=tuple(tuple(s*(B[i][j]+alpha*B[i][j]/d_i)/d_a for j in range(n)) for i in range(n))
assert K==((F(2,3),F(1,3)),(F(1,3),F(2,3)))
assert all(sum(K[j][i] for j in range(n))==1 for i in range(n))
assert K[0][0]-K[0][1]==F(1,3)  # second eigenvalue, hence spectral radius one
p=(F(1),F(1))
q=tuple(sum(p[j]*s*B[j][i]/d_i for j in range(n)) for i in range(n))
assert q==(F(1),F(1))
assert all(sum(p[j]*s*B[j][i] for j in range(n))-p[i]*d_a+alpha*q[i]==0 for i in range(n))
assert all(sum(p[j]*s*B[j][i] for j in range(n))-q[i]*d_i==0 for i in range(n))
S=(F(3,4),F(1,2))
A=(F(1,10),F(1,5))
I=(F(1,20),F(1,10))
R=tuple(F(1)-S[i]-A[i]-I[i] for i in range(n))
assert all(z>=0 for z in R)
f=tuple(sum(B[i][j]*(A[j]+I[j]) for j in range(n)) for i in range(n))
assert f==(F(3,5),F(3,4))
e=tuple(S[i]-s for i in range(n))
edot=tuple(-kappa*e[i]-S[i]*f[i]-gamma*(A[i]+I[i]) for i in range(n))
Adot=tuple(S[i]*f[i]-d_a*A[i] for i in range(n))
Idot=tuple(alpha*A[i]-d_i*I[i] for i in range(n))
Wdot=sum(p[i]*Adot[i]+q[i]*Idot[i] for i in range(n))
assert Wdot==sum(p[i]*e[i]*f[i] for i in range(n))
Hdot=sum(p[i]*edot[i] for i in range(n) if e[i]>0)
Vdot=Wdot+Hdot
right=(sum(p[i]*e[i]*f[i] for i in range(n) if e[i]<0)
       -sum(p[i]*(s*f[i]+kappa*e[i]+gamma*(A[i]+I[i])) for i in range(n) if e[i]>0))
assert (Wdot,Hdot,Vdot,right)==(F(-3,40),F(-17,20),F(-37,40),F(-37,40))
assert Vdot==right<0
# At the nonsmooth boundary e_i=0, e_i' is nonpositive.
assert -s*f[0]-gamma*(A[0]+I[0])<0
print('CHECK_OK')
