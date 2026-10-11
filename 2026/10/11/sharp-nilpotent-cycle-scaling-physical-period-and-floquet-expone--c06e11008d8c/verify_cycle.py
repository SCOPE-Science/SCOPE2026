"""Reproducible numerical diagnostics for a near-zero nilpotent limit cycle.

No numerical experiment establishes the asymptotic theorem; see analytic proof.
Requires only Python 3 standard library. Run: python3 verify_cycle.py
"""
from math import gamma, sqrt, exp

def beta(a,b): return gamma(a)*gamma(b)/gamma(a+b)

i1=beta(.75,1.5)/4

i3=beta(.25,2.5)/4
rho=sqrt(2*i1/i3)
t0=sqrt(2)*beta(.25,.5)/rho
j0=2*sqrt(2)*rho**3*i3

def rhs(v,d):
 x,y,q=v
 return (y,-x**3+d*(y**3-x*x*y),d*(3*y*y-x*x))

def step(v,h,d):
 a=rhs(v,d)
 b=rhs(tuple(v[i]+h*a[i]/2 for i in range(3)),d)
 c=rhs(tuple(v[i]+h*b[i]/2 for i in range(3)),d)
 e=rhs(tuple(v[i]+h*c[i] for i in range(3)),d)
 return tuple(v[i]+h*(a[i]+2*b[i]+2*c[i]+e[i])/6 for i in range(3))

def passage(r,d,h=.002):
 v=(r,0.,0.)
 t=0.
 for k in range(12000):
  w=step(v,h,d)
  if v[1]>0 and w[1]<=0:
   low,high=0.,h
   for _ in range(28):
    mid=(low+high)/2
    if step(v,mid,d)[1]>0:low=mid
    else:high=mid
   frac=(low+high)/2
   crossing=step(v,frac,d)
   return crossing[0]-r,t+frac,crossing[2]
  v=w;t+=h
 raise RuntimeError('return not located')

def root(d):
 lo,hi=.7,.9
 f_lo=passage(lo,d)[0]; f_hi=passage(hi,d)[0]
 assert (f_lo*d<0 and f_hi*d>0),(d,f_lo,f_hi)
 for _ in range(28):
  mid=(lo+hi)/2
  if passage(mid,d)[0]*d <0:lo=mid
  else:hi=mid
 return (lo+hi)/2

assert .799 <rho<.801
assert 9.27<t0<9.28
assert 1.08<j0<1.09
for d in (.16,.08,.04):
 r=root(d)
 _,t,lm=passage(r,d)
 rm=root(-d)
 _,tm,lmm=passage(rm,-d)
 print('d=',d,'R=',round(r,9),'T=',round(t,9),'logmult=',round(lm,9),
       'R(-d)=',round(rm,9),'T(-d)=',round(tm,9))
 assert abs(r-rm)<1e-6
 assert abs(t-tm)<1e-5
 assert abs(lm+lmm)<1e-5
 assert abs(r-rho)<.03*d*d
 assert abs(t-t0)<.14*d*d
 assert abs(lm/d-j0)<.04*d*d
print('CHECK_OK')
