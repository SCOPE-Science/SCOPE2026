"""Independent arithmetic checks for rhombic-dodecahedron section perimeters.
Run: python verify_candidate_perimeter.py (Python 3 standard library only).
"""
import itertools
import math
import random

SQRT2=math.sqrt(2.0)
V_CUBE=list(itertools.product((-1.0,1.0), repeat=3))
EDGES=[(v,tuple(2.0*v[i] if j==i else 0.0 for j in range(3))) for v in V_CUBE for i in range(3)]

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(x):return math.sqrt(dot(x,x))
def hull2(points):
    points=sorted(set(points))
    def cross2(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    bot=[]
    for p in points:
        while len(bot)>1 and cross2(bot[-2],bot[-1],p)<=0:bot.pop()
        bot.append(p)
    top=[]
    for p in reversed(points):
        while len(top)>1 and cross2(top[-2],top[-1],p)<=0:top.pop()
        top.append(p)
    return bot[:-1]+top[:-1]

def perimeter_polygon(points):
    h=hull2(points)
    return sum(math.dist(p,h[(i+1)%len(h)]) for i,p in enumerate(h)),len(h)

def direct(n):
    n=tuple(v/norm(n) for v in n)
    e=(0,0,1) if abs(n[2])<.9 else (1,0,0)
    ex=cross(n,e);ex=tuple(v/norm(ex) for v in ex)
    ey=cross(n,ex)
    pts=[]
    for v,w in EDGES:
        sv=dot(n,v);sw=dot(n,w)
        if sv*sw<0:
            p=tuple((sw*v[i]-sv*w[i])/(sw-sv) for i in range(3))
            pts.append((dot(ex,p),dot(ey,p)))
    return perimeter_polygon(pts)

def exact(n):
    a,b,c=sorted(map(abs,n),reverse=True)
    S=a+b+c
    if a<=b+c:
        return 4/S*(math.sqrt(2*a*a+(b+c)**2)+math.sqrt(2*b*b+(a+c)**2)+math.sqrt(2*c*c+(a+b)**2))
    d=a+b-c;e=a-b+c
    return (4*math.sqrt(2*a*a+(b+c)**2)/S
     +8*b*math.sqrt((a+b)**2+2*c*c)/(d*S)
     +4*(a-b-c)*math.sqrt(2*a*a+(b-c)**2)/(d*e)
     +8*c*math.sqrt((a+c)**2+2*b*b)/(e*S))

def projection_perimeter(n):
    n=tuple(v/norm(n) for v in n)
    tet=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
    return 2*sum(math.sqrt(max(0.0,3-dot(v,n)**2)) for v in tet)

def check():
    rng=random.Random(21931017)
    counts=[0,0]; worst=0.0;worst_stability=0.0
    for i in range(3200):
        n=[rng.uniform(-2,2) for _ in range(3)]
        if norm(n)<.01:continue
        p,k=direct(n)
        q=exact(n)
        worst=max(worst,abs(p-q))
        assert abs(p-q)<2e-9,(n,p,q)
        counts[{6:0,8:1}[k]]+=1
        nunit=tuple(v/norm(n) for v in n)
        Q=sum(nunit[a]**2*nunit[b]**2 for a in range(3) for b in range(a+1,3))
        # The strong Jensen estimate is an analytic bound, checked numerically here.
        assert 8*SQRT2-p>=4/(3*math.sqrt(3))*Q-1e-10
        assert p<=projection_perimeter(n)+1e-10
        worst_stability=max(worst_stability,4/(3*math.sqrt(3))*Q-(8*SQRT2-p))
    assert counts[0]>300 and counts[1]>300,counts
    assert abs(exact([1,1,1])-4*math.sqrt(6))<1e-12
    assert abs(exact([1,0,0])-8*SQRT2)<1e-12
    assert abs(exact([1,1,0])-(4+4*math.sqrt(3)))<1e-12
    # Near-coordinate cusp, all sign/order chambers, two scales.
    for p,q in [(1,0),(0,1),(2**-.5,2**-.5),(.6,.8),(-.8,.6)]:
        for t in [1e-4,1e-5,1e-6]:
            n=(math.sqrt(1-t*t),t*p,t*q)
            delta=8*SQRT2-exact(n)
            leading=8*(SQRT2-1)*(abs(p)+abs(q))*t
            assert abs(delta-leading)<350*t*t,(p,q,t,delta,leading)
    print('EXACT_DIRECTIONAL_FORMULAS_VS_INDEPENDENT_EDGE_HULL_OK',counts,'max_error',worst)
    print('SHARP_UPPER_BOUND_AND_TETRAHEDRAL_FRAME_STABILITY_OK')
    print('SIX_SECTOR_EXACT_ENDPOINTS_AND_AXIS_CUSP_OK')
    print('ALL_RHOMBIC_DODECAHEDRON_PERIMETER_CHECKS_OK')
if __name__=='__main__':check()
