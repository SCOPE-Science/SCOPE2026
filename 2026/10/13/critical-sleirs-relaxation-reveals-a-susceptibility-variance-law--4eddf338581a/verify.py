#!/usr/bin/env python3
from fractions import Fraction as F
from scipy.integrate import solve_ivp

rho=F(1,2);mu=F(1);sigma=F(1);delta=F(1);gamma=F(1)
alpha=F(5,3); beta=F(1)
a=delta+mu;b=gamma+mu;r=sigma+mu
h=delta/b;k=1+h
A=rho*alpha+(1-rho)*beta
B=rho*alpha*alpha+(1-rho)*beta*beta
G=sigma*gamma*h/r
H=1+(A/b)*h
K=k*(k*B-G*A)/(mu*H)
assert A*k == a
assert (A,B,G,H,K)==(F(4,3),F(17,9),F(1,4),F(4,3),F(45,16))
es=rho*(k*alpha-G)/mu
el=(1-rho)*(k*beta-G)/mu
pred=(1/K,h/K,(gamma*h/r)/K,es/K,el/K)
assert pred == (F(16,45),F(8,45),F(4,45),F(2,5),F(2,9))
assert B==A*A+rho*(1-rho)*(alpha-beta)**2
# positive dispersion effect at fixed A
assert k*k*rho*(1-rho)/(mu*H) > 0

def fun(t,y):
    S,L,E,I,R=y
    z=E+I
    return [float(mu*rho)+float(sigma*rho)*R-float(alpha)*S*z-float(mu)*S,
            float(mu*(1-rho))+float(sigma*(1-rho))*R-float(beta)*L*z-float(mu)*L,
            (float(alpha)*S+float(beta)*L)*z-float(a)*E,
            float(delta)*E-float(b)*I,
            float(gamma)*I-float(r)*R]

T=100000.0
sol=solve_ivp(fun,(0.0,T),[.44,.38,.09,.06,.03],rtol=8e-11,atol=5e-13,max_step=50.0)
assert sol.success
S,L,E,I,R=sol.y[:,-1]
got=(T*E,T*I,T*R,T*(float(rho)-S),T*(float(1-rho)-L))
for value,target in zip(got,pred):
    assert abs(value/float(target)-1) < .01,(got,pred)
assert abs(S+L+E+I+R-1)<1e-9
# Symbolic certificate for the exact Lyapunov derivative (all parameters free).
import sympy as sym
Sx,Lx,Ex,Ix,Rx,mux,rhox,deltax,gammax,sigmax,alphax,betax = sym.symbols(
    'Sx Lx Ex Ix Rx mux rhox deltax gammax sigmax alphax betax',
    real=True, nonzero=True)
Ax = rhox*alphax+(1-rhox)*betax
bx = gammax+mux
fSx = mux*rhox+sigmax*rhox*Rx-alphax*Sx*(Ex+Ix)-mux*Sx
fLx = mux*(1-rhox)+sigmax*(1-rhox)*Rx-betax*Lx*(Ex+Ix)-mux*Lx
fEx = (alphax*Sx+betax*Lx)*(Ex+Ix)-(deltax+mux)*Ex
fIx = deltax*Ex-bx*Ix
derivative=(1-rhox/Sx)*fSx+(1-(1-rhox)/Lx)*fLx+fEx+(Ax/bx)*fIx
predicted=(-mux*(Sx-rhox)**2/Sx -mux*(Lx-(1-rhox))**2/Lx
           +sigmax*Rx*(1-rhox**2/Sx-(1-rhox)**2/Lx)
           +(Ax*(1+deltax/bx)-(deltax+mux))*Ex)
assert sym.simplify(derivative-predicted)==0

print('VERIFY_OK')
print('K',K,'targets',pred,'observed',got)
