"""Monte Carlo sanity check of stationary correlations, using Euler-Maruyama with actual resets."""
import numpy as np
from verify import analytic
rng=np.random.default_rng(7843)
g,r=3.,1.7
h=0.005
n=28000
x=np.zeros(n);q=np.zeros(n)
obs={0.0:None, 0.25:None,1.0:None,3.0:None}
t0=45.0
checkpoints={int(round((t0+t)/h)):t for t in obs}
for k in range(max(checkpoints)+1):
    if k in checkpoints:obs[checkpoints[k]]=x.copy()
    xold=x.copy()
    x +=(-xold+q)*h+np.sqrt(2*h)*rng.standard_normal(n)
    q +=(xold-q)*(h/g)+np.sqrt(2*h/g)*rng.standard_normal(n)
    x[rng.random(n)<r*h]=0.
xx=obs[0.]
for t in [0.,.25,1.,3.]:
    c=float(np.mean(xx*obs[t]));truth=analytic(g,r,t)[6]
    print(f't={t:.2f}: simulation={c:.7f}, theorem={truth:.7f}, absolute_error={abs(c-truth):.7f}')
    assert abs(c-truth)<0.040, (t,c,truth)
print('PASS stationary trajectory correlation check')
