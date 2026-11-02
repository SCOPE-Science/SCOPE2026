#!/usr/bin/env python3
"""Deterministic checks for a rectangular half-turn flat three-manifold theorem."""
import math, random
from fractions import Fraction
rng=random.Random(16033)


def qcap(a,h): return min(a*a,4*h*h)-h*h

def Fq(q,a,b):
    assert 0<a<=b
    if q<=0:return 0.
    A=a/2.;B=b/2.
    if q>=A*A+B*B:return 1.
    r=math.sqrt(q)
    if r<=A: area=math.pi*q/4
    elif r<=B:area=(A*math.sqrt(q-A*A)+q*math.asin(A/r))/2
    else:
        def H(v):return (v*math.sqrt(q-v*v)+q*math.asin(v/r))/2
        area=H(A)+H(B)-math.pi*q/4
    return area/(A*B)


def analytic_length(x,y,a,b,h):
    dx=min((2*x)%a,a-(2*x)%a)
    dy=min((2*y)%b,b-(2*y)%b)
    return min(a,2*h,math.sqrt(h*h+dx*dx+dy*dy))


def brute_length(x,y,z,a,b,h):
    best=math.inf
    for m in range(-2,3):
      for n in range(-2,3):
        for k in range(-2,3):
          if k%2==0:
            dx=m*a;dy=n*b;dz=k*h
          else:
            dx=m*a-2*x;dy=n*b-2*y;dz=k*h
          if m==n==k==0:continue
          d=math.sqrt(dx*dx+dy*dy+dz*dz)
          best=min(best,d)
    return best

for a,b,h in [(.8,1.0,.1),(1.,1.,.35),(1.,1.,.5),(1.,1.,.9),
              (1.,1.2,.3),(1.,math.sqrt(2),.5),(1.,1.6,.5),
              (1.,2.1,.9),(1.,4.,2.),(2.,3.,1.2),(2.,3.,3.)]:
 for j in range(160):
  x=rng.random()*a;y=rng.random()*b;z=rng.random()*h
  assert abs(analytic_length(x,y,a,b,h)-brute_length(x,y,z,a,b,h))<1e-10,(a,b,h,x,y)
print('GROUP_ORBIT_MINIMUM_INDEPENDENT_RECONSTRUCTION_PASSED 1760')

# The exact rational identity for the untruncated spatial variance.
assert Fraction(1,80)-Fraction(1,12)**2==Fraction(1,180)
assert Fraction(2,180)==Fraction(1,90)
print('EXACT_FOURTH_MOMENT_AND_VARIANCE_CONSTANT_PASSED')

# Analytic CDF versus independently sampled deck points.
for a,b,h in [(1,1,.18),(1,1,.5),(1,1,.91),(1,1.2,.6),
              (1,1.5,.5),(1,2,.49),(2,3,.8),(1,1,1.4)]:
 vals=[analytic_length(rng.random()*a,rng.random()*b,a,b,h) for _ in range(16000)]
 cap=min(a,2*h)
 for t in [h*.9, h*1.1, (h+cap)/2, cap-.02, cap+.02]:
  if t<cap:expected=Fq(t*t-h*h,a,b)
  else:expected=1.
  got=sum(v<=t for v in vals)/len(vals)
  assert abs(got-expected)<.026,(a,b,h,t,got,expected)
print('CDF_PIECEWISE_INDEPENDENT_SAMPLING_PASSED 40')

# Exact geometric area identity checked against independent midpoint-grid counts.
for a,b in [(1,1),(1,1.1),(1,1.5),(1,2),(1,3)]:
 for q in [.02,.14,.27,.52,.83,1.4]:
  N=180
  count=sum(1 for i in range(N) for j in range(N)
         if ((i+.5)*a/(2*N))**2+((j+.5)*b/(2*N))**2<=q)
  got=count/N**2
  expect=Fq(q,a,b)
  assert abs(got-expect)<.006,(a,b,q,got,expect)
print('INDEPENDENT_RECTANGLE_QUARTER_DISK_AREA_PASSED 30')

# Verify the sharp plateau geometry and uniqueness for anisotropic cells.
def v_grid(a,b,h,N=130):
 q=qcap(a,h)
 vals=[min((i+.5)**2*a*a/(4*N*N)+(j+.5)**2*b*b/(4*N*N),q)
       for i in range(N) for j in range(N)]
 m=sum(vals)/len(vals)
 return sum((v-m)**2 for v in vals)/len(vals)

for a,b in [(1,1),(1,1.3),(1,math.sqrt(2)),(1,1.7),(1,3)]:
 upper=(a**4+b**4)/180
 center=v_grid(a,b,a/2)
 assert center<=upper+2e-5
 if b/a<math.sqrt(2)-1e-9:
  lo=math.sqrt(a*a+b*b)/(2*math.sqrt(3))
  hi=math.sqrt(3*a*a-b*b)/2
  assert abs(v_grid(a,b,(lo+hi)/2)-upper)<2e-5
 elif b/a>math.sqrt(2)+1e-9:
  assert center<upper-1e-4,(a,b,center,upper)
 for h in [.1*a,.3*a,.7*a,.95*a,1.1*a]:
  assert v_grid(a,b,h)<=center+2e-5,(a,b,h)
print('OPTIMIZER_PHASE_DIAGRAM_AND_SHARP_VARIANCE_PASSED')
print('ALL_CHECKS_PASSED')
