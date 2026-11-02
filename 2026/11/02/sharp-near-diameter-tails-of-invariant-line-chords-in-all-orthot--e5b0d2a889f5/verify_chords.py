import numpy as np,math
from scipy.stats import qmc
from scipy.special import gamma

def tail_qmc(a,eps,m=18,delta=.8):
 a=np.array(a,float);d=len(a);A=np.linalg.norm(a); ell=2*A-eps
 L=0.5+d*delta*eps; pts=qmc.Sobol(d-1,scramble=True,seed=325).random_base2(m)
 coords=np.concatenate([np.zeros((len(pts),1)), np.sort(pts,axis=1),np.ones((len(pts),1))],axis=1)
 ys=L*np.diff(coords,axis=1)-delta*eps
 v=a/(2*A*A) - ys/a
 q=a/A
 norm=np.sqrt(1+eps**2*(v*v).sum(axis=1))
 u=(q[None,:]+eps*v)/norm[:,None]
 b=2*a[None,:]-ell*u
 valid=np.all(b>0,axis=1)
 pos=np.maximum(b,0)
 # each i prod b_j other indices
 f=np.zeros(len(pts))
 for i in range(d):
  f+=u[:,i]*np.prod(pos[:,np.arange(d)!=i],axis=1)
 f*=valid
 f*=eps**(d-1)*(1+eps**2*(v*v).sum(axis=1))**(-d/2)*A/np.prod(a)
 num=2**d/(2*math.pi**(d/2)/gamma(d/2))*f.mean()*L**(d-1)/math.factorial(d-1)
 den=2**(d-1)*np.prod(a)*np.sum(1/a)*gamma(d/2)/(math.sqrt(math.pi)*gamma((d+1)/2))
 return num/den

def pred(a):
 a=np.array(a,float);d=len(a);A=np.linalg.norm(a)
 return 2**(1-d)*A**(d+1)*gamma((d+1)/2)/(math.pi**((d-1)/2)*math.factorial(2*d-2)*np.prod(a)**3*np.sum(1/a))
if __name__=='__main__':
 for a in [[1,1,1,1],[1,1,1,1,1],[1,2,1,3]]:
  for eps in [.1,.05,.025]:
   val=tail_qmc(a,eps);C=pred(a)
   print(a,eps,'tail',val,'ratio',val/(C*eps**(2*len(a)-2)),flush=True)
