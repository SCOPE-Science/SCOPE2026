from fractions import Fraction as F

def rho_c(d,m):
    return 1-2*d+m

def kappa(d,m):
    return (1+m)/(1+2*d)

def xstar(d,m):
    return (1+3*d+m*d)/(1+m)

def profile(d,m,x):
    s=abs(x)
    xs=xstar(d,m)
    if s<=d:
        return 1-(d-m/F(2))/(1+d-s)
    if s<1+d:
        return F(1)
    if s<=xs:
        return F(1,2)/(s-d)
    return (2+m)/(2*(s+1+d))

# step function represented by half-open intervals [a,b) with constant value
def val(segments,t):
    for a,b,v in segments:
        if a < t < b or (t==a and a!=b):
            return v
    return F(0)

def integral_on(segments,L,R):
    z=F(0)
    for a,b,v in segments:
        lo=max(L,a); hi=min(R,b)
        if hi>lo:
            z += (hi-lo)*v
    return z

def maxavg(segments,x):
    # For a step function, between endpoint-crossing radii the numerator is affine,
    # hence N(r)/(2r) is monotone or constant. It suffices to inspect critical radii,
    # plus the r->0 local limit.
    bps=sorted(set([a for a,b,v in segments]+[b for a,b,v in segments]))
    rs=sorted(set(abs(q-x) for q in bps if abs(q-x)>0))
    vals=[]
    # one-sided local limit at the center, where defined
    tinyvals=[]
    for a,b,v in segments:
        if a < x < b:
            tinyvals.append(v)
    if tinyvals:
        vals.extend(tinyvals)
    for r in rs:
        vals.append(integral_on(segments,x-r,x+r)/(2*r))
    return max(vals) if vals else F(0)

def make_F(d,hsegs):
    return [
        (-1-d,-d,F(1)),
        *hsegs,
        (d,1+d,F(1)),
    ]

# Algebraic identities, checked on representative exact rationals.
for d,m in [(F(1,4),F(1,16)),(F(1,3),F(1,9)),(F(2,5),F(1,5))]:
    rc=rho_c(d,m)
    kap=kappa(d,m)
    xs=xstar(d,m)
    assert 0 < rc < 1
    assert m/(2*d) <= rc
    assert rc <= kap < 1
    assert kap-rc == 2*d*(2*d-m)/(1+2*d)
    assert xs-(1+d) == (2*d-m)/(1+m)

# Exact step-function checks for d=1/4, m=1/16.
d=F(1,4); m=F(1,16); rc=rho_c(d,m)
h_examples=[
    [(-d,d,m/(2*d))],
    [(-d,-F(1,8),F(0)),(-F(1,8),F(0),F(1,8)),(F(0),F(1,8),F(1,4)),(F(1,8),d,F(1,8))],
    [(-d,-F(1,8),F(3,8)),(-F(1,8),F(0),F(1,8)),(F(0),F(1,8),F(0)),(F(1,8),d,F(0))],
]
for h in h_examples:
    mass=sum((b-a)*v for a,b,v in h)
    assert mass==m
    assert max(v for a,b,v in h)<=rc
    seg=make_F(d,h)
    for x in [F(-2),F(-5,4),F(-1),F(-1,4),F(0),F(1,4),F(1),F(5,4),F(3,2),F(2)]:
        assert maxavg(seg,x)==profile(d,m,x), (h,x,maxavg(seg,x),profile(d,m,x))

# Above-threshold witness at the tower boundary.
rho=F(3,4)
assert rho>rc
a=F(1,32)
c=(m-rho*a)/(2*d-a)
assert 0<=c<=rho
h1=[(-d,d-a,c),(d-a,d,rho)]
assert sum((b-a)*v for a,b,v in h1)==m
seg1=make_F(d,h1)
safe=profile(d,m,d)
witness=F(1,2)*(1+rho)
assert witness>safe
assert maxavg(seg1,d)>=witness

print("VERIFY_OK")
print("rho_c =", rc)
print("safe_boundary_value =", safe)
print("above_threshold_boundary_value >=", witness)
