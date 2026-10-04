import math

Q=[(-1.0,-1.0),(1.0,-1.0),(1.0,1.0),(-1.0,1.0)]

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    pts=sorted(set((round(x,14),round(y,14)) for x,y in points))
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:
            lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0:
            up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]

def perimeter(poly):
    return sum(math.hypot(poly[(i+1)%len(poly)][0]-poly[i][0],
                          poly[(i+1)%len(poly)][1]-poly[i][1])
               for i in range(len(poly)))

def excess(x,y):
    return perimeter(hull(Q+[(x,y)]))-8.0

def area_formula(delta):
    c=math.pi*delta
    a=1.0+c/2.0
    b=math.sqrt(a*a-1.0)
    alpha=a+1.0
    beta=math.sqrt(alpha*alpha-2.0)
    return 4.0+4.0*a*b*math.asin(1.0/a)+4.0*alpha*beta*math.asin(b*b/(math.sqrt(2.0)*a*alpha))

for delta in (0.001,0.01,0.1,1.0,5.0):
    c=math.pi*delta
    a=1.0+c/2.0
    b=math.sqrt(a*a-1.0)
    alpha=a+1.0
    beta=math.sqrt(alpha*alpha-2.0)
    for j in range(41):
        y=-1.0+2.0*j/40.0
        x=1.0+b*math.sqrt(max(0.0,1.0-y*y/(a*a)))
        assert abs(excess(x,y)-c)<2e-10
    p0=b*b/(math.sqrt(2.0)*a)
    for j in range(41):
        p=-p0+2.0*p0*j/40.0
        q=beta*math.sqrt(max(0.0,1.0-p*p/(alpha*alpha)))
        x=(q+p)/math.sqrt(2.0)
        y=(q-p)/math.sqrt(2.0)
        assert x>=1.0-2e-12 and y>=1.0-2e-12
        assert abs(excess(x,y)-c)<2e-10
    d=b*b/a
    x,y=1.0+d,1.0
    p=(x-y)/math.sqrt(2.0); q=(x+y)/math.sqrt(2.0)
    assert abs((x-1.0)**2/(b*b)+y*y/(a*a)-1.0)<2e-12
    assert abs(p*p/(alpha*alpha)+q*q/(beta*beta)-1.0)<2e-12

def numerical_area(delta,ntheta=2048):
    c=math.pi*delta
    total=0.0
    for k in range(ntheta):
        theta=2.0*math.pi*(k+0.5)/ntheta
        ux,uy=math.cos(theta),math.sin(theta)
        lo,hi=0.0,2.0
        while excess(hi*ux,hi*uy)<c:
            hi*=2.0
        for _ in range(52):
            mid=(lo+hi)/2.0
            if excess(mid*ux,mid*uy)<=c: lo=mid
            else: hi=mid
        total+=lo*lo
    return math.pi*total/ntheta

for delta in (0.01,0.1,1.0,5.0):
    assert abs(area_formula(delta)-numerical_area(delta))<2e-6

for delta in (1e-3,3e-4,1e-4,3e-5):
    exact=area_formula(delta)-4.0
    approx=(2.0*math.pi**1.5*delta**0.5
            +(5.0/4.0)*math.pi**2.5*delta**1.5
            -(2.0/3.0)*math.pi**2*delta**2)
    assert abs(exact-approx)<20.0*delta**2.5

print("VERIFY_OK square separation-body area profile")
