import numpy as np
from scipy.linalg import expm
from scipy.special import lambertw

def qfun(b,lmb,t):
 mu=np.sqrt(complex(lmb*lmb-b*b))
 if abs(mu)<1e-12:return np.exp(-lmb*t)*(1+lmb*t)
 return np.exp(-lmb*t)*(np.cosh(mu*t)+lmb*np.sinh(mu*t)/mu)

def formula(n,h,th,lmb,t):
 kk=np.arange(n); p=np.zeros(n,dtype=complex)
 E0=2*h*np.cos(th)*np.cos(2*np.pi*kk/n)
 E1=2*h*np.sin(th)*np.sin(2*np.pi*kk/n)
 for k in kk:
  for l in kk:
   weight=np.exp(-1j*(E0[k]-E0[l])*t)*qfun(E1[k]-E1[l],lmb,t)/n**2
   p+=weight*np.exp(2j*np.pi*(k-l)*np.arange(n)/n)
 return p.real

def direct(n,h,th,lmb,t):
 S=np.roll(np.eye(n),1,axis=0).astype(complex)
 Hp=h*(np.exp(1j*th)*S+np.exp(-1j*th)*S.conj().T)
 Hm=h*(np.exp(-1j*th)*S+np.exp(1j*th)*S.conj().T)
 i=np.eye(n)
 def comm(H):return -1j*(np.kron(i,H)-np.kron(H.T,i))
 nn=n*n
 L=np.block([[comm(Hp)-lmb*np.eye(nn),lmb*np.eye(nn)],[lmb*np.eye(nn),comm(Hm)-lmb*np.eye(nn)]])
 ini=np.zeros(2*nn,complex);ini[0]=ini[nn]=0.5
 state=expm(L*t)@ini
 return np.real(np.diag((state[:nn]+state[nn:]).reshape((n,n),order='F')))

count=0;err=0
for n in (3,4,5,6,7,8):
 for th in (0.38,np.pi/2,2.0):
  for t in (.4,2.7,8.0):
   a=formula(n,.73,th,.8,t);b=direct(n,.73,th,.8,t)
   err=max(err,float(np.max(abs(a-b))));assert np.allclose(a,b,atol=1e-10),(n,th,t,a,b)
   count+=1
 print('n',n,'last analytic',np.round(formula(n,.73,th,.8,150),5))
print('dense',count,'maxerr',err)
for n in (4,6,8,10):
 f=2 if n%4==0 else 0
 asympt=np.ones(n)*(1/n-f/n**2)
 for x in (0,n//2):asympt[x]+=(-1)**x/n
 p=formula(n,.73,np.pi/2,.8,150)
 print('limit',n,asympt,'maxerr',np.max(abs(asympt-p)))
 assert np.allclose(asympt,p,atol=1e-12)
for n in (3,5,7,9,11,13,15):
 d=np.array([np.sin(2*np.pi*k/n) for k in range(n)])
 empirical=min(abs(d[i]-d[j]) for i in range(n) for j in range(i))
 closed=2*np.sin(np.pi/(2*n))*np.sin(np.pi/n)
 assert abs(empirical-closed)<1e-12
 print('delta',n,empirical,closed)
for n in (51,101,201,401,801):
 h=.73;theta=.75;lamb=.8
 b=4*abs(h*np.sin(theta))*np.sin(np.pi/(2*n))*np.sin(np.pi/n)
 gap=b*b/(lamb+np.sqrt(lamb*lamb-b*b))
 constant=2*np.pi**4*h*h*np.sin(theta)**2/lamb
 print('quartic',n,gap*n**4/constant)
 assert abs(gap*n**4/constant-1)<.006
