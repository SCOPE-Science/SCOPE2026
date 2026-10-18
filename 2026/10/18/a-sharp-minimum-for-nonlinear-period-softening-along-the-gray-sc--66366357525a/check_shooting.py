from scipy.integrate import solve_ivp
from scipy.optimize import root
import numpy as np

def data(F,k):
 c=F+k; disc=F*F-4*F*c*c
 if disc<=0: raise ValueError('no equilibrium')
 v=(F+np.sqrt(disc))/(2*c)
 u=c/v
 J=np.array([[-F-v*v,-2*u*v],[v*v,2*u*v-c]])
 l=np.linalg.eigvals(J)
 return u,v,np.max(l.imag)

def trial(t,r):
 k=t*t/(1+t)**4; Fh=t*k
 _,v_h,om_h=data(Fh,k)
 Th=2*np.pi/om_h
 Lre=(3*t-1)/(8*(1-t)); coeff=(9*t*t+6*t+5)*(1+t)**3/(24*t*t*(1-t)**2)
 # radial: eigen growth tau~-(F-Fh)/t and tau+g_r r²=0 => F-Fh ~t*g_r*r²
 target=Fh+t*Lre*r*r
 def calc(v):
  F,T=v
  try:
   u0,v0,_=data(F,k); V=v0+r; U=(F+k)/V
   sol=solve_ivp(lambda tt,yy: [F*(1-yy[0])-yy[0]*yy[1]**2,yy[0]*yy[1]**2-(F+k)*yy[1]],(0,T),(U,V),rtol=8e-12,atol=5e-14,method='DOP853',max_step=Th/100)
   u1,v1=sol.y[:,-1]
   return np.array([(v1-V)/r,(u1-U)/r]);
  except ValueError: return np.array([1e4,1e4])
 sol=root(calc,[target,Th*(1+coeff*r*r)],tol=1e-9)
 if not sol.success and np.linalg.norm(sol.fun)>1e-6:print('bad',sol.message,sol.fun)
 F,T=sol.x
 _,_,om=data(F,k)
 obs=(T*om/(2*np.pi)-1)/r**2
 print(f't={t}, r={r}, F0={Fh:.10g}, F={F:.10g}, T={T:.10g}, om={om:.10g}, coefficient_th={coeff:.10g}, observed={obs:.10g}, ratio={obs/coeff:.7f}, success={sol.success}, error={np.linalg.norm(sol.fun):.1e}')
for t in [.25,.5]:
 for r in [.012,.008,.005,.003]:trial(t,r)
