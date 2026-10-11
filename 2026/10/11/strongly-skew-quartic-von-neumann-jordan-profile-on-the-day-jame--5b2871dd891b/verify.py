import math

V=[(1.0,0.0),(1.0,1.0),(0.0,1.0),(-1.0,0.0),(-1.0,-1.0),(0.0,-1.0)]

def N(z):
    x,y=z
    return max(abs(x),abs(y),abs(x-y))

def poly(r):
    return r**3+2*r**2-2

lo,hi=0.0,1.0
for _ in range(100):
    mid=(lo+hi)/2
    if poly(mid)<0: lo=mid
    else: hi=mid
rho=(lo+hi)/2

def envelope(r,t):
    vals=[]
    for x in V:
        for y in V:
            a=N((x[0]+r*t*y[0],x[1]+r*t*y[1]))
            b=N((r*x[0]-t*y[0],r*x[1]-t*y[1]))
            vals.append(a**4+b**4)
    return max(vals)

def formula_env(r,t):
    return max(1+(r+t)**4,(1+r*t)**4+max(r,t)**4)

vertex_checks=0
for ir in range(1,121):
    r=rho*ir/120
    for it in range(241):
        t=it/240
        assert abs(envelope(r,t)-formula_env(r,t))<2e-10
        vertex_checks+=1

def h(r,t):
    return t**3*(1-(1+r*t)**-3)-r

def root_t(r):
    if abs(r-rho)<1e-12:
        return 1.0
    lo=r
    hi=1.0
    assert h(r,lo)<0 and h(r,hi)>0
    for _ in range(100):
        mid=(lo+hi)/2
        if h(r,mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2

profile_checks=0
for ir in range(1,101):
    r=rho*ir/100
    tr=root_t(r)
    exact=((1+r*tr)**4+tr**4)/(4*(1+r**4)*(1+tr**4))
    best=0.0
    for it in range(20001):
        t=it/20000
        val=envelope(r,t)/(4*(1+r**4)*(1+t**4))
        best=max(best,val)
    assert exact+3e-8>=best
    assert abs(h(r,tr))<2e-12 or abs(tr-1)<2e-12
    profile_checks+=1

assert abs(poly(rho))<2e-14
print(f"VERIFY_OK rho={rho:.15f} vertex_checks={vertex_checks} profile_checks={profile_checks} branches=2")
