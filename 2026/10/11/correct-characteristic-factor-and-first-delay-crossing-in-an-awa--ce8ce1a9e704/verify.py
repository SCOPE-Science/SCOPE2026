#!/usr/bin/env python3
import math, cmath
r=40.0; beta=0.0025; m=0.2; mu=0.01; d1=0.1; d2=0.1; c=0.6; p=0.6; gamma=0.02; lam=0.1
C=c+mu; G=gamma+mu; L=lam+mu+d1
v=C*G*L/(c*p*gamma)
def f(I): return v*I + mu*v*math.exp(m*I)/beta-r
lo,hi=0.0,50.0
for _ in range(200):
    mid=(lo+hi)/2
    if f(mid)>0: hi=mid
    else: lo=mid
I=(lo+hi)/2
S=v*math.exp(m*I)/beta
E=G*L*I/(c*p*gamma); Q=L*I/(p*gamma); J=lam*I/(d2+mu)
u=beta*math.exp(-m*I)*I
p1=C+G+L+mu+u
p2=C*G+C*L+G*L+(mu+u)*(C+G+L)
p3=(mu+u)*(C*G+C*L+G*L)
p4=C*G*L*u
q1=C*G*L*m*I; q0=mu*q1
coef=[1.0,p1*p1-2*p2,p2*p2+2*p4-2*p1*p3,p3*p3-2*p2*p4-q1*q1,p4*p4-q0*q0]
assert [x>0 for x in coef[:3]]==[True,True,True] and coef[3]<0 and coef[4]<0
z=0.0044253010286742922574; theta=math.sqrt(z)
def poly(z): return sum(coef[k]*z**(4-k) for k in range(5))
assert abs(poly(z))<1e-15
R1=p1*theta**3-p3*theta; R2=-theta**4+p2*theta**2-p4
den=q1*q1*theta*theta+q0*q0
co=(q1*theta*R1+q0*R2)/den; si=(-q0*R1+q1*theta*R2)/den
phase=math.atan2(si,co); tau=phase/theta
assert abs(tau-18.59248621759530)<1e-10
xi=1j*theta
def F(x,t): return x**4+p1*x**3+p2*x**2+p3*x+p4+cmath.exp(-x*t)*(q1*x+q0)
assert abs(F(xi,tau))<1e-12
D2=p1*p2-(p3+q1)
D3=p1*p2*(p3+q1)-(p3+q1)**2-p1*p1*(p4+q0)
assert min(p1,p2,p3+q1,p4+q0,D2,D3)>0
D=4*xi**3+3*p1*xi**2+2*p2*xi+p3+cmath.exp(-xi*tau)*(q1-tau*(q1*xi+q0))
dxdt=xi*cmath.exp(-xi*tau)*(q1*xi+q0)/D
assert dxdt.real>0 and abs(dxdt.real-0.001262757946267497)<1e-12
# equilibrium residuals for the five coupled equations
inc=beta*math.exp(-m*I)*S*I
res=[r-inc-mu*S,inc-C*E,c*E-G*Q,p*gamma*Q-L*I,lam*I-(d2+mu)*J]
assert max(map(abs,res))<1e-10
print('VERIFY_OK')
print('I*',repr(I))
print('tau*',repr(tau))
print('theta*',repr(theta))
print('Re(dxi/dtau)',repr(dxdt.real))
