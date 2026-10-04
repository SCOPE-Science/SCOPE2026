import math

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    pts=sorted(set((float(x),float(y)) for x,y in points))
    if len(pts)<=1:
        return pts
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:
            lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:
            hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]
                   -poly[(i+1)%len(poly)][0]*poly[i][1]
                   for i in range(len(poly)))/2.0)

def parameters(m,q,R=1.0):
    alpha=math.pi/m
    mu=math.cos(alpha)/math.cos(q*alpha)
    delta=R*R*(math.cos(alpha)**2*math.tan(q*alpha)
               -q*math.sin(alpha)*math.cos(alpha))
    return mu,delta

for m in range(3,61):
    admissible=[q for q in range(3,m,2) if q < m/2]
    assert len(admissible)==(m-3)//4
    P=[(math.cos(2*math.pi*j/m),math.sin(2*math.pi*j/m)) for j in range(m)]
    AP=area(P)
    previous_mu=1.0
    previous_delta=0.0
    for q in admissible:
        mu,delta=parameters(m,q)
        assert mu>previous_mu and delta>previous_delta
        previous_mu,previous_delta=mu,delta

        # A vertex of the predicted homothetic level.
        x=(mu,0.0)
        direct=area(hull(P+[x]))-AP
        assert abs(direct-delta) < 2e-11*(1+delta), (m,q,direct,delta)

        # The convex-hull area is constant along the predicted level edge.
        v0=(mu,0.0)
        v1=(mu*math.cos(2*math.pi/m),mu*math.sin(2*math.pi/m))
        for t in (0.0,0.2,0.5,0.8,1.0):
            y=((1-t)*v0[0]+t*v1[0],(1-t)*v0[1]+t*v1[1])
            level=area(hull(P+[y]))-AP
            assert abs(level-delta) < 3e-11*(1+delta), (m,q,t,level,delta)

print("VERIFY_OK regular polygon illumination spectrum m=3..60")
