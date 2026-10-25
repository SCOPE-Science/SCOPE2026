import math
import numpy as np
from scipy.integrate import quad

def mu(y): return (math.pi/2)*abs(math.sin(2*math.pi*y))
def periodic_ker(t):
 u=t%1
 return 2*math.pi**2*(u*u-u+1/6)
def direct(N,g):
 Y=np.arange(N)/N
 K=np.array([[1+g*periodic_ker(a-b) for b in Y] for a in Y])
 kap=np.array([quad(lambda y: (1+g*periodic_ker(a-y))*mu(y),0,1,epsabs=5e-12,points=sorted(set([a,.5])),limit=160)[0] for a in Y])
 return np.linalg.solve(K,kap)
def formula(N,g):
 x=math.pi/N
 a=x*x/3
 d=1-x/math.tan(x)
 y=np.arange(N)/N
 B=np.array([quad(lambda t: max(0,1-N*min(abs((v-t)%1),abs((t-v)%1)))*mu(t),0,1,epsabs=1e-12,points=sorted(set([v%1,(v+1/N)%1,(v-1/N)%1,.5])),limit=160)[0] for v in y])
 return B-g*d/(N*(1+g*a)),B
n=0
for N in [4,6,8,10,12]:
 x=math.pi/N; B=.5-N/(4*math.pi)*math.sin(2*x); a=x*x/3;d=1-x/math.tan(x)
 G=N*B/(d-N*a*B)
 for g in [0.25,1,G*.95,G,G*1.05,100]:
  w=direct(N,g);v,b=formula(N,g)
  assert np.max(abs(w-v))<1e-8,(N,g,w,v)
  assert abs(min(b)-b[0])<1e-8
  if abs(g-G)>1e-7: assert (min(w)>=0)==(g<G)
  n+=1
 print('N',N,'gamma frontier',format(G,'.12g'),'first weight',format(float(B),'.12g'))
print('PASS',n,'independently assembled kernel-integration matrix tests')
