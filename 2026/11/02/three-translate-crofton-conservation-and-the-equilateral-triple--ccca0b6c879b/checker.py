#!/usr/bin/env python3
"""Independent numerical checks of the three-translate line-incidence formulas.
No external packages are required. All checks are finite corroboration; proofs
in RESULT.md establish claims over continuous angle and offset domains.
"""
import math

PI = math.pi

def width_projection(poly, u):
    v = [x*u[0]+y*u[1] for x,y in poly]
    return min(v),max(v)

def exactly_k_lengths(intervals):
    endpoints = sorted(x for a,b in intervals for x in (a,b))
    lengths = [0.0]*4
    for a,b in zip(endpoints,endpoints[1:]):
        m=(a+b)*.5
        k=sum(aa<=m<=bb for aa,bb in intervals)
        lengths[k]+=b-a
    return lengths[1:4]

def circumference(vertices):
    return sum(math.hypot(x-u,y-v) for (x,y),(u,v) in zip(vertices,vertices[1:]+vertices[:1]))

def B(q):
    if q<=1:
        return 2*(q*math.asin(q)+math.sqrt(max(0.,1-q*q))-1)
    return PI*q-2

def T(q):
    if q<=math.sqrt(3)/2:
        return 0.
    if q<=1:
        return 6*(q*(PI/6-math.acos(q))+math.sqrt(max(0.,1-q*q))-.5)
    return PI*q-3

def integration_polygon(name,poly,centers,N=9000):
    ans=[0.0,0.0,0.0]
    maxerr=0.0
    for i in range(N):
        th=PI*(i+.5)/N
        u=(math.cos(th),math.sin(th))
        a,b=width_projection(poly,u)
        shifts=[x*u[0]+y*u[1] for x,y in centers]
        intervals=[(a+v,b+v) for v in shifts]
        ll=exactly_k_lengths(intervals)
        r=max(shifts)-min(shifts)
        goal=[r,r,b-a-r]
        maxerr=max(maxerr,max(abs(x-y) for x,y in zip(ll,goal)))
        for j in range(3):ans[j]+=ll[j]*PI/N
    # If center triangle isn't counterclockwise, perimeter is unaffected.
    Ptriangle=circumference(centers)
    Pbody=circumference(poly)
    target=[Ptriangle,Ptriangle,Pbody-Ptriangle]
    error=max(abs(a-b) for a,b in zip(ans,target))
    assert maxerr<2e-12,(name,'pointwise failure',maxerr)
    assert error<3e-5,(name,'integral mismatch',ans,target,error)
    print(name,'integral=',[round(x,10) for x in ans],
          'theory=',[round(x,10) for x in target], 'max_error=',error)

def integration_disks(q,N=16000):
    c=[(0.,0.),(1.,0.),(.5,math.sqrt(3)/2)]
    ans=[0.0,0.0,0.0]
    for i in range(N):
        th=PI*(i+.5)/N
        ux,uy=math.cos(th),math.sin(th)
        shifts=[x*ux+y*uy for x,y in c]
        intervals=[(v-q/2,v+q/2) for v in shifts]
        ll=exactly_k_lengths(intervals)
        for j in range(3): ans[j]+=ll[j]*PI/N
    b=B(q);t=T(q)
    target=[3*PI*q-6*b+3*t, 3*b-3*t, t]
    error=max(abs(a-b) for a,b in zip(ans,target))
    assert error<4e-6,(q,ans,target,error)
    print('three disks q=',q,'measure=',[round(x,9) for x in ans],
          'formula=',[round(x,9) for x in target], 'max_error=',error)

if __name__=='__main__':
    rectangle=[(-2.,-1.),(2.,-1.),(2.,1.),(-2.,1.)]
    triangle=[(-2.,-1.),(2.,-1.),(.1,2.)]
    ellipse_poly=[(2.0*math.cos(2*PI*j/160), math.sin(2*PI*j/160)) for j in range(160)]
    centers=[(0.,0.),(.55,.06),(.12,.36)]
    for name,poly in [('noncentrally symmetric triangle',triangle),('rectangle',rectangle),('160-gon ellipse',ellipse_poly)]:
        integration_polygon(name,poly,centers)
    for q in [.45,.75,math.sqrt(3)/2,.88,.96,1.,1.2,2.]:
        integration_disks(q)
    q0=math.sqrt(3)/2
    lim=6/(3+PI*math.sqrt(3)/2)
    import decimal
    decimal.getcontext().prec=48
    print('Predicted normalized quadratic onset coefficient',lim)
    print('ALL CHECKS PASSED')
