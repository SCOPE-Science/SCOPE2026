import numpy as np
rng=np.random.default_rng(314159)
r=.7;gamma=1.3;v=2.;rho=1.4
N=250000

def run(durations, initx=None, initvel=None, resets=False):
 xs=np.zeros(len(durations)) if initx is None else initx.copy()
 signs=rng.choice([-1.,1.],size=len(durations)) if initvel is None else initvel.copy()
 # Simulate flips in each time chunk via vectorized event times, only on active remaining intervals
 remain=durations.copy();mask=remain>1e-12
 while np.any(mask):
  ids=np.flatnonzero(mask); events=rng.exponential(1/gamma,len(ids)); seg=np.minimum(events,remain[ids]);xs[ids]+=v*signs[ids]*seg; remain[ids]-=seg; flip=events<seg+1e-13
  signs[ids[flip]]*=-1;mask=remain>1e-12
 return xs,signs
age=rng.exponential(1/r,N)
x0,vel0=run(age)
for t in (.2,1.,2.):
 # future restart via sample whole reset clocks individually: approximation by per path while loop
 xf=x0.copy();vf=vel0.copy();remain=np.full(N,t)
 while np.any(remain>1e-12):
  ids=np.flatnonzero(remain>1e-12)
  dtreset=rng.exponential(1/r,len(ids))
  duration=np.minimum(dtreset,remain[ids]); y,s=run(duration,xf[ids],vf[ids]);xf[ids]=y;vf[ids]=s;remain[ids]-=duration
  didreset=dtreset<duration+1e-13
  xf[ids[didreset]]=0;vf[ids[didreset]]=rng.choice([-1.,1.],size=np.count_nonzero(didreset))
 est=rho*np.mean(np.maximum(np.minimum(x0,xf),0));se=rho*np.std(np.maximum(np.minimum(x0,xf),0))/np.sqrt(N)
 print('t',t,'MC C',est,'SE',se)

# Independent inversion of the theoretical covariance transform.
import mpmath as mp
mp.mp.dps=35
rr=mp.mpf(str(r)); gg=mp.mpf(str(gamma)); vv=mp.mpf(str(v)); rh=mp.mpf(str(rho))
ll=mp.sqrt(rr*(rr+2*gg))/vv

def transform(s):
    z=s+rr
    k=mp.sqrt(z*(z+2*gg))/vv
    a=(z+2*gg)/(2*vv**2*k)
    return rh/ll**2*((ll/2)*a*(1/k+1/(k+ll))+(rr/(4*vv**2))*(1/k-1/(k+ll))) + rh*rr/(4*s*z*(ll+k))

# New independent regenerative simulations and transform inversion are compared
# within five empirical standard errors, with finite-sample standard errors printed.
rng=np.random.default_rng(314159)
age=rng.exponential(1/r,N)
x0,vel0=run(age)
for t in (.2,1.,2.):
    xf=x0.copy();vf=vel0.copy();remain=np.full(N,t)
    while np.any(remain>1e-12):
        ids=np.flatnonzero(remain>1e-12)
        dtreset=rng.exponential(1/r,len(ids))
        duration=np.minimum(dtreset,remain[ids])
        y,s=run(duration,xf[ids],vf[ids]);xf[ids]=y;vf[ids]=s;remain[ids]-=duration
        didreset=dtreset<duration+1e-13
        xf[ids[didreset]]=0;vf[ids[didreset]]=rng.choice([-1.,1.],size=np.count_nonzero(didreset))
    observations=rho*np.maximum(np.minimum(x0,xf),0)
    estimated=observations.mean()
    stderr=observations.std(ddof=1)/np.sqrt(N)
    theoretical=float(mp.invertlaplace(transform,t,method='dehoog'))
    assert abs(estimated-theoretical)<5*stderr+0.001,(t,estimated,theoretical,stderr)
    print('verified',t,estimated,theoretical,stderr)
assert abs(float(mp.limit(lambda z: z*transform(z),0))-float(rh/(8*ll)))<1e-9
print('All covariance-transform checks passed.')
