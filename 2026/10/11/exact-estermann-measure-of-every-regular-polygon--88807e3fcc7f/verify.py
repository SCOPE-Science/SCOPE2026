import math

EPS = 1e-9

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    pts=sorted(set((round(x,14),round(y,14)) for x,y in points))
    if len(pts)<=1:
        return pts
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=1e-12:
            lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=1e-12:
            up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]

def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly))))/2

for n in range(3,102):
    P=[(math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n)) for j in range(n)]
    A=area(P)
    H=hull(P+[(-x,-y) for x,y in P])
    ratio=A/area(H)
    expected=1.0 if n%2==0 else math.cos(math.pi/n)
    expected_vertices=n if n%2==0 else 2*n
    assert len(H)==expected_vertices,(n,len(H),expected_vertices)
    assert abs(ratio-expected)<2e-10,(n,ratio,expected)

assert abs(math.cos(math.pi/3)-0.5)<EPS
print('VERIFY_OK')
print('triangle =', math.cos(math.pi/3))
print('pentagon =', math.cos(math.pi/5))
print('n=101 =', math.cos(math.pi/101))
