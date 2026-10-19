import sympy as S
z,d,L,g,h,v,G,al,t=S.symbols('z d L g h v G al t', positive=True)
u=g+h;q=1-t;D=d+L
J=S.Matrix([[-D,-(G+g*q),-(G+h*v*q/al)], [L,g*q-u,h*v*q/al],[0,al,-v]])
p=S.Poly((z*S.eye(3)-J).det(),z)
A1=D+h+v+g*t
A2=d*(h+v)+L*(u+v+G)+(d*g+v*u)*t
A3=L*(v*u+G*(al+v))+d*v*u*t
for k,expected in [(2,A1),(1,A2),(0,A3)]:
 diff=S.factor(p.coeff_monomial(z**k)-expected)
 print('coefficient',k,diff)
 assert diff==0
Delta0=S.expand((A1*A2-A3).subs(t,0));print('delta0 factor',S.factor(Delta0))
# Bound at t=0: a1 a2 >= a1 L(G+u); a1 >=d+L+v>=G+v since d=mu+nu+G, and u>=al. But does this imply comparison?
# compare a1*(G+u) - (v*u + G*(al+v))
print('a1 core difference at t=0',S.factor((A1*(G+u)-(v*u+G*(al+v))).subs(t,0)))
# independent numeric eigs
import numpy as np
for mu,nu,gamma,alpha,dA,dI,betaA,betaI in [(1,15,1,3,0.1,0.2,50,30),(.1,8,10,6,.05,1,150,10),(1,0,1,2,3,4,20,10)]:
 u0=alpha+dA+mu;v0=dI+mu;d0=mu+nu+gamma
 B=betaA+alpha*betaI/v0;s=u0/B
 if (mu+gamma)<=d0*s:continue
 a=(mu+gamma-d0*s)/(u0+gamma*(1+alpha/v0));I=alpha*a/v0; lamb=betaA*a+betaI*I
 W=np.array([[0,.5,.5],[.5,0,.5],[.5,.5,0]])
 M=np.zeros((9,9))
 for i in range(3):
  M[i,i]=-(d0+lamb)
  M[i,3+i]=-gamma;M[i,6+i]=-gamma
  for j in range(3):
   M[i,3+j]-=s*betaA*W[i,j]
   M[i,6+j]-=s*betaI*W[i,j]
  M[3+i,i]=lamb;M[3+i,3+i]=-u0;M[6+i,3+i]=alpha;M[6+i,6+i]=-v0
  for j in range(3): M[3+i,3+j]+=s*betaA*W[i,j];M[3+i,6+j]+=s*betaI*W[i,j]
 print('numeric max real eigenvalue',np.linalg.eigvals(M).real.max())
 assert np.linalg.eigvals(M).real.max()<0
