import math
import random

def add(x,y):
    return [a+b for a,b in zip(x,y)]

def sub(x,y):
    return [a-b for a,b in zip(x,y)]

def scale(a,x):
    return [a*t for t in x]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def norm(x):
    return math.sqrt(dot(x,x))

def proj_ball(z,c,r):
    v=sub(z,c)
    d=norm(v)
    if d <= r:
        return z[:]
    return add(c, scale(r/d, v))

def proj_two(z,a,r,b,R):
    n=len(z)
    if norm(sub(z,a)) <= r and norm(sub(z,b)) <= R:
        return z[:], "inside"
    pa=proj_ball(z,a,r)
    if norm(sub(pa,b)) <= R + 1e-13:
        return pa, "a"
    pb=proj_ball(z,b,R)
    if norm(sub(pb,a)) <= r + 1e-13:
        return pb, "b"
    if n == 1:
        raise AssertionError("one-dimensional fallback should be exhaustive")
    dvec=sub(b,a)
    D=norm(dvec)
    assert D > 0.0
    e=scale(1.0/D,dvec)
    s=(r*r-R*R+D*D)/(2.0*D)
    c=add(a,scale(s,e))
    rho2=r*r-s*s
    assert rho2 > -1e-12
    rho=math.sqrt(max(0.0,rho2))
    zc=sub(z,c)
    w=sub(zc,scale(dot(zc,e),e))
    nw=norm(w)
    assert rho > 0.0 and nw > 1e-14
    return add(c,scale(rho/nw,w)), "both"

def dykstra(z,a,r,b,R,steps=20000,tol=1e-13):
    x=z[:]
    p=[0.0]*len(z)
    q=[0.0]*len(z)
    for _ in range(steps):
        xp=add(x,p)
        y=proj_ball(xp,a,r)
        p=sub(xp,y)
        yq=add(y,q)
        xn=proj_ball(yq,b,R)
        q=sub(yq,xn)
        if norm(sub(xn,x)) <= tol*(1.0+norm(x)):
            x=xn
            break
        x=xn
    return x

# Deterministic branches.
cases=[
    ([0.0,0.0],[0.0,0.0],2.0,[1.0,0.0],2.0),
    ([5.0,0.0],[0.0,0.0],2.0,[1.0,0.0],2.0),
    ([-5.0,0.0],[0.0,0.0],2.0,[1.0,0.0],2.0),
    ([0.5,4.0],[0.0,0.0],1.0,[1.0,0.0],1.0),
]
seen=set()
for z,a,r,b,R in cases:
    p,branch=proj_two(z,a,r,b,R)
    q=dykstra(z,a,r,b,R)
    seen.add(branch)
    assert norm(sub(p,q)) < 2e-8
    assert norm(sub(p,a)) <= r+2e-10
    assert norm(sub(p,b)) <= R+2e-10
assert "both" in seen

rng=random.Random(73491)
branches={}
for n in [2,3,5,8]:
    for _ in range(250):
        a=[rng.uniform(-1.0,1.0) for _ in range(n)]
        direction=[rng.gauss(0.0,1.0) for _ in range(n)]
        nd=norm(direction)
        direction=scale(1.0/nd,direction)
        r=rng.uniform(0.4,2.0)
        R=rng.uniform(0.4,2.0)
        low=abs(r-R)+0.05
        high=r+R-0.05
        if low >= high:
            continue
        D=rng.uniform(low,high)
        b=add(a,scale(D,direction))
        z=[rng.uniform(-4.0,4.0) for _ in range(n)]
        p,branch=proj_two(z,a,r,b,R)
        q=dykstra(z,a,r,b,R)
        branches[branch]=branches.get(branch,0)+1
        assert norm(sub(p,a)) <= r+3e-9
        assert norm(sub(p,b)) <= R+3e-9
        assert norm(sub(p,q)) < 3e-7

# Concentric/containment cases must reduce to a single-ball branch.
for n in [1,2,4]:
    a=[0.0]*n
    b=[0.0]*n
    z=[3.0]+[0.2]*(n-1)
    p,branch=proj_two(z,a,2.0,b,1.0)
    assert branch in ("b","inside")
    assert norm(sub(p,b)) <= 1.0+1e-12

print("VERIFY_OK", branches)
