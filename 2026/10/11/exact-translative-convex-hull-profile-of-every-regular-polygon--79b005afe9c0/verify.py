#!/usr/bin/env python3
import math

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    pts=sorted(set((round(x,15),round(y,15)) for x,y in points))
    if len(pts)<=1:
        return pts
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=1e-13:
            lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=1e-13:
            up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]

def regular(m):
    return [(math.cos(2*math.pi*k/m),math.sin(2*math.pi*k/m)) for k in range(m)]

def central_symmetral(P):
    return hull([((p[0]-q[0])/2,(p[1]-q[1])/2) for p in P for q in P])

def support(P,u):
    return max(x*u[0]+y*u[1] for x,y in P)

def width(P,u):
    vals=[x*u[0]+y*u[1] for x,y in P]
    return max(vals)-min(vals)

def radial(P,u):
    # Intersect the ray t*u, t>=0, with every polygon edge and keep
    # the nearest positive boundary intersection.
    cand=[]
    n=len(P)
    for i in range(n):
        a=P[i]; b=P[(i+1)%n]
        ex=b[0]-a[0]; ey=b[1]-a[1]
        den=ex*u[1]-ey*u[0]
        if abs(den)<1e-14:
            continue
        sseg=-(a[0]*u[1]-a[1]*u[0])/den
        if -1e-12 <= sseg <= 1+1e-12:
            x=a[0]+sseg*ex; y=a[1]+sseg*ey
            t=x*u[0]+y*u[1]
            # collinearity is automatic up to numerical error.
            if t>=-1e-12:
                cand.append(max(0.0,t))
    assert cand
    pos=[x for x in cand if x>1e-12]
    assert pos
    return min(pos)

def formula(m):
    if m%2:
        return 1+8*math.cos(math.pi/(2*m))**3/(m*math.sin(2*math.pi/m))
    if m%4==2:
        return 1+4/(m*math.sin(math.pi/m))
    return 1+8/(m*math.sin(2*math.pi/m))

def area_regular(m):
    return 0.5*m*math.sin(2*math.pi/m)

max_err=0.0
const_err=0.0
for m in range(3,41):
    P=regular(m)
    D=central_symmetral(P)
    vals=[]
    angles=[2*math.pi*(j+0.37)/7200 for j in range(7200)]
    # Include all vertex directions exactly so the nonconstant 4k branch
    # is tested at its analytic maxima rather than only near them.
    angles.extend(2*math.pi*k/m for k in range(m))
    for th in angles:
        u=(math.cos(th),math.sin(th))
        up=(-u[1],u[0])
        # d_P=2*rho_D and w_P=w_D.
        vals.append(2*radial(D,u)*width(P,up))
    numeric=1+max(vals)/area_regular(m)
    max_err=max(max_err,abs(numeric-formula(m)))
    if m%4:
        const_err=max(const_err,max(vals)-min(vals))
    else:
        expected_lo=4*math.cos(math.pi/m)**2
        expected_hi=4.0
        assert min(vals)>=expected_lo-2e-6
        assert max(vals)<=expected_hi+2e-6

assert max_err < 2e-6, max_err
assert const_err < 2e-11, const_err
assert abs(formula(3)-3)<1e-14
assert abs(formula(4)-3)<1e-14
assert abs(formula(5)-(10+math.sqrt(5))/5)<1e-14

print("VERIFY_OK")
print("all_m_3_to_40_profile = passed")
print("small_published_values = passed")
print("max_formula_error = %.3e" % max_err)
print("max_constant_branch_spread = %.3e" % const_err)
