import math, numpy as np
from scipy.integrate import solve_ivp

def ode(t,y,a,b):
 u,v=y
 return -b*math.exp(-b*t)*v-a*math.exp(-(a+b)*t)*u,-a*math.exp(-a*t)*u-b*math.exp(-(a+b)*t)*v

def mc(n,a,b,t,reps=10000):
 rng=np.random.default_rng(1773)
 rates=np.tile([a,b],n//2)
 f=np.zeros(2)
 for z in range(reps):
  clock=rng.exponential(scale=1/rates)
  busy=np.zeros(n,dtype=bool)
  for j in np.argsort(clock):
   if clock[j]>t:break
   idx=((j,j+1,j+2))
   idx=tuple(x%n for x in idx)
   if not any(busy[x] for x in idx):
    for x in idx:busy[x]=True
  f[0]+=not any(busy[x] for x in (0,1,2))
  f[1]+=not any(busy[x] for x in (1,2,3))
 return f/reps
for a,b in [(1,1),(1,.5),(2,1)]:
 for t in [.2,.9,1.7]:
  sol=solve_ivp(lambda t,y:ode(t,y,a,b),(0,t),[1,1],atol=1e-13,rtol=1e-12)
  u,v=sol.y[:,-1]
  theory=np.array([math.exp(-a*t)*u*u,math.exp(-b*t)*v*v])
  obs=mc(100,a,b,t,3000)
  print(a,b,t,obs,theory)
  assert max(abs(obs-theory))<.032
print('PASS transient checks 18')
