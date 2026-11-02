"""Finite diagnostics for scalar operator-mean cycles; not a substitute for the proof."""
import math, cmath, random

random.seed(230427)
def f_ar(t,l): return 1-l+l*t
def f_geo(t,l): return t**l
def f_har(t,l): return 1/(1-l+l/t)
def f_mix(t,l):
    # A nonsymmetric Kubo--Ando mean with derivative 1/2 at 1.
    assert l==0.5
    return .4*f_har(t,.2)+.6*f_har(t,.7)
def step(w,l,f):
    m=len(w)
    return [w[(j+1)%m]*f(w[j]/w[(j+1)%m],l) for j in range(m)]
def spread(w): return max(w)-min(w)
def eig_abs(m,l,r): return abs(l+(1-l)*cmath.exp(2j*math.pi*r/m))
checks=0
for m in range(2,17):
 for l in [.15,.25,.5,.7,.9]:
    rho=math.sqrt(1-4*l*(1-l)*math.sin(math.pi/m)**2)
    assert abs(rho-max(eig_abs(m,l,r) for r in range(1,m)))<1e-12
    checks+=1
    for f in [f_ar,f_geo,f_har]+([f_mix] if l==.5 else []):
     for case in range(12):
      w=[math.exp(random.uniform(-1,1)) for _ in range(m)]
      old=spread(w)
      for k in range(9):
       nw=step(w,l,f)
       assert min(w)-1e-13<=min(nw) and max(nw)<=max(w)+1e-13
       assert spread(nw)<=old+1e-12
       checks+=2
       w=nw;old=spread(w)
     # Numerical derivative at consensus against the predicted circulant Jacobian.
     eps=1e-5
     v=[math.cos(2*math.pi*j/m)+.37*math.sin(4*math.pi*j/m) for j in range(m)]
     w=[math.exp(eps*x) for x in v]
     transformed=step(w,l,f)
     for j in range(m):
      linear=l*v[j]+(1-l)*v[(j+1)%m]
      assert abs(math.log(transformed[j])/eps-linear)<1.3e-5
      checks+=1
# Check the non-symmetric 2-cycle does not collapse in one step,
# while its derivative vanishes.
w=[1.0,2.0]
nw=step(w,.5,f_mix)
assert abs(nw[0]-nw[1])>1e-5
checks+=1
print('FINITE_CHECKS_PASS',checks)
