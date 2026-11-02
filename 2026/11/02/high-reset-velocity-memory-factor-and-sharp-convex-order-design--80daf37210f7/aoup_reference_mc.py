import numpy as np

def check(r, v0, n=5000, seed=20261027):
    D=1.; Dv=0.8; tau=1.25; d=0.7
    rng=np.random.default_rng(seed+int(r)*17+int((v0+2)*11))
    dt=d/(2*np.sqrt(D*r)*360)
    x=np.full(n,d);v=np.full(n,v0);exponent=np.full(n,-d*v0/(2*D));active=np.ones(n,dtype=bool)
    for j in range(1200):
        ids=np.flatnonzero(active)
        if not len(ids): break
        oldx=x[ids]; oldv=v[ids]
        dWv=rng.normal(size=len(ids))*np.sqrt(dt)
        dv=-oldv/tau*dt+np.sqrt(2*Dv)/tau*dWv
        newx=oldx-2*np.sqrt(D*r)*dt+np.sqrt(2*D*dt)*rng.normal(size=len(ids))
        f=np.clip(oldx/np.maximum(oldx-newx,1e-300),0,1)
        inside=newx>0
        frac=np.where(inside,1,f)
        exponent[ids] += -(oldx*dv*frac)/(2*D)-(oldv**2*dt*frac)/(4*D)
        x[ids]=np.maximum(newx,0); v[ids]=oldv+dv
        active[ids[~inside]]=False
    if active.any(): print('uncompleted',r,v0,active.sum())
    z=np.exp(exponent)
    return z.mean(),z.std(ddof=1)/np.sqrt(n)

if __name__=='__main__':
 for r in (25.,100.,400.):
  for v0 in (-1.,0.,1.):
   z,se=check(r,v0)
   print('r',r,'v0',v0,'MC-ratio',round(z,6),'SE',round(se,6),'limit',round(np.exp(-0.7*v0/2),6))
