#!/usr/bin/env python3
import math

def q(x): return 4.0*sum(math.sinh(t/2.0)**2 for t in x)
def radii(d,e): return 2*math.asinh(math.sqrt(e)/2), 2*math.sqrt(d)*math.asinh(math.sqrt(e)/(2*math.sqrt(d)))
def support(v,e):
    a=[abs(t) for t in v]
    def p(lam): return [math.asinh(t/(2*lam)) if t else 0.0 for t in a]
    lo,hi=1e-12,1.0
    while q(p(hi))>e: hi*=2
    for _ in range(160):
        mid=(lo+hi)/2
        if q(p(mid))>e: lo=mid
        else: hi=mid
    x=p((lo+hi)/2)
    return sum(t*y for t,y in zip(a,x))
def close(a,b): return abs(a-b)<=3e-10*max(1,abs(a),abs(b))
cases=0
for d in range(2,9):
  for e in (.01,.1,1.,10.,100.):
    r0,r1=radii(d,e)
    assert close(q([r0]+[0.]*(d-1)),e)
    assert close(q([r1/math.sqrt(d)]*d),e)
    assert close(support([1.]+[0.]*(d-1),e),r0)
    assert close(support([1/math.sqrt(d)]*d,e),r1)
    v=[1.,.5]+[0.]*(d-2); n=math.sqrt(1.25); h=support(v,e)/n
    assert r0<h<r1
    cases+=1
print(f'VERIFY_OK cases={cases}')
