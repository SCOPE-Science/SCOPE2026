import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq
from math import pi,exp,log
T=1.0; d1=0.78; d2=0.75
beta=lambda t:2.2+0.3*np.sin(2*pi*t)
mu=lambda t:0.4+0.05*np.sin(2*pi*t)
b=lambda t:0.6+0.1*np.cos(2*pi*t)
alpha=lambda t:1.3+0.2*np.sin(2*pi*t)
xi=lambda t:0.8+0.1*np.cos(2*pi*t)
κ=d1/d2
R=d2*np.exp(quad(b,0,T)[0]); assert R>1
q0=log(κ)-quad(lambda t:mu(t)+b(t),0,T)[0]
qinf=log(κ)+quad(lambda t:beta(t)-mu(t)-b(t),0,T)[0]
assert q0<0<qinf

def scalar(r0,ret=False):
  def fun(t,v):
    r=v[0];h=beta(t)*r/(r+alpha(t))-mu(t)-b(t)
    dr=r*h
    dv=beta(t)*alpha(t)/(r+alpha(t))**2
    return [dr,v[1]* (h+r*dv), np.exp(0.6*t+0.1/(2*pi)*np.sin(2*pi*t))*xi(t)*(1+r)]
  sol=solve_ivp(fun,[0,T],[r0,1.0,0.0],rtol=1e-11,atol=1e-13,dense_output=True)
  return sol.y[:,-1], sol
rstar=brentq(lambda r:κ*scalar(r)[0][0]-r,0.001,100)
arr,sol=scalar(rstar);print('r*',rstar,'rT',arr[0], 'Q0,Qinf',q0,qinf)
assert abs(κ*arr[0]-rstar)<1e-9
H=arr[2]; ystar=(R-1)/H; xstar=rstar*ystar
lambda_u=κ*arr[1];lambda_s=1/R
print('y* x*',ystar,xstar,'eigs',lambda_s,lambda_u,'R',R)
assert lambda_u>1 and 0<lambda_s<1

def full(x0,y0):
  def fun(t,v):
    x,y=v;xyp=x+alpha(t)*y
    return [x*(beta(t)*x/xyp-mu(t)-xi(t)*(x+y)),y*(b(t)-xi(t)*(x+y))]
  f=solve_ivp(fun,[0,T],[x0,y0],rtol=1e-11,atol=1e-13)
  return np.array([d1,d2])*f.y[:,-1]
vstar=np.array([xstar,ystar]);assert np.linalg.norm(full(*vstar)-vstar)<1e-9
h=1e-5
jac=np.column_stack([(full(*(vstar+h*np.eye(2)[i]))-full(*(vstar-h*np.eye(2)[i])))/(2*h) for i in range(2)])
eigs=np.linalg.eigvals(jac);print('numerical eigs',eigs,'jac=',jac)
assert max(abs(np.sort(eigs)-np.sort([lambda_s,lambda_u])))<1e-6
for r0,expected in [(rstar/2,'y'),(2*rstar,'x')]:
  yy=1.0;rr=r0
  for _ in range(200):
    out,sol=scalar(rr); Hn=out[2]; ynext=R*yy/(1+Hn*yy);rr=κ*out[0];yy=ynext
    if rr>1e20 or rr<1e-20:break
  if expected=='y':assert rr<rstar
  else:assert rr>rstar
print('ALL TESTS PASSED')
