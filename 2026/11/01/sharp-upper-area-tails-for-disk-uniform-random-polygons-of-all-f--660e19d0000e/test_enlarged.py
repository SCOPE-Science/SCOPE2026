import numpy as np,math
from scipy.special import gamma

def run(n,e,N=450000,boost=3):
 rng=np.random.default_rng(12001+int(100000*e)+n)
 m=n-1;a=math.sin(2*math.pi/n);b=a/4
 scale=e*(1+boost*np.sqrt(e))
 t=rng.beta(m/2,n+1,N)
 directions=rng.normal(size=(N,m));directions/=np.linalg.norm(directions,axis=1)[:,None]
 y=directions*np.sqrt(scale*t)[:,None]
 z=(y+(1/math.sqrt(n)-1)*y.mean(axis=1,keepdims=True))/math.sqrt(b)
 angles=np.column_stack((z,-z.sum(axis=1)))+2*math.pi/n
 shares=rng.dirichlet(np.ones(n),size=N)
 uu=shares*((scale/a)*(1-t)*rng.beta(n,1,N))[:,None]
 rr=1-uu
 A=.5*np.sum(rr*np.roll(rr,-1,axis=1)*np.sin(angles),axis=1)
 d=n*a/2-A
 w=(angles[:,-1]/(2*math.pi/n))*np.prod(rr,axis=1)
 q=(scale/e)**((3*n-1)/2)*np.mean((d<e)*w)
 stderr=(scale/e)**((3*n-1)/2)*np.std((d<e)*w)/np.sqrt(N)
 return q,stderr,float(np.mean(d<e)),float(np.max(angles)),float(np.min(angles))
for n in (3,4):
 for e in (.2,.14,.1,.05,.02,.01,.003,.001):
  x=run(n,e)
  print('n',n,'eps',e,'ratio %.5f +- %.5f acceptance %.3f minangle %.3f'%(x[0],x[1],x[2],x[4]))
