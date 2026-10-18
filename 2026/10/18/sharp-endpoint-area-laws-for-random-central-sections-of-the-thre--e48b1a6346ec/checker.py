"""Independent finite checks for central three-cube section-area endpoint laws."""
import itertools
import math
import random

ROOT2 = math.sqrt(2.0)
VERTS = list(itertools.product((-1.0, 1.0), repeat=3))
EDGES = [(v,w) for v,w in itertools.combinations(VERTS,2) if sum(v[i]!=w[i] for i in range(3))==1]


def section_polygon_area(normal):
    z = normal
    x = (1.0,0.0,0.0) if abs(z[0])<0.8 else (0.0,1.0,0.0)
    dot = sum(x[i]*z[i] for i in range(3))
    e = [x[i]-dot*z[i] for i in range(3)]
    ne = math.sqrt(sum(v*v for v in e)); e = [v/ne for v in e]
    f = [z[1]*e[2]-z[2]*e[1], z[2]*e[0]-z[0]*e[2], z[0]*e[1]-z[1]*e[0]]
    pts = set()
    for v,w in EDGES:
        dv = sum(z[i]*v[i] for i in range(3)); dw = sum(z[i]*w[i] for i in range(3))
        if dv*dw > 0.0: continue
        t = dv/(dv-dw) if abs(dv-dw)>1e-13 else 0.0
        if t<0 or t>1: continue
        p = [v[i]+t*(w[i]-v[i]) for i in range(3)]
        pts.add((round(sum(e[i]*p[i] for i in range(3)),12),round(sum(f[i]*p[i] for i in range(3)),12)))
    pts=sorted(pts)
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    hull=lo[:-1]+hi[:-1]
    return abs(sum(hull[i][0]*hull[(i+1)%len(hull)][1]-hull[(i+1)%len(hull)][0]*hull[i][1] for i in range(len(hull))))/2


def formula(normal):
    a,b,c = sorted((abs(v) for v in normal),reverse=True)
    if a<=0: raise ValueError('zero normal')
    if c < 1e-14 or b+c<=a: return 4.0/a
    return 4.0/a-(b+c-a)**2/(a*b*c)


def unit(v):
    n=math.sqrt(sum(x*x for x in v)); return [x/n for x in v]


def check():
    rng=random.Random(2397)
    cases=400
    maxerr=0.0
    for _ in range(cases):
        v=unit([rng.gauss(0,1) for _ in range(3)])
        err=abs(formula(v)-section_polygon_area(v))
        maxerr=max(maxerr,err)
        assert err<2e-8,(v,err)
    for v in ((1,0,0),(1,1,0),(1,1,1)):
        p=unit(v)
        assert abs(formula(p)-section_polygon_area(p))<2e-8
    assert abs(formula(unit((1,0,0)))-4.0)<1e-12
    assert abs(formula(unit((1,1,0)))-4*ROOT2)<1e-12
    def loc(t,s):
        r=math.sqrt(1-t*t-s*s)
        return [r/ROOT2+t/ROOT2,r/ROOT2-t/ROOT2,s]
    for t0,s0 in ((.13,.05),(.02,.16),(-.09,.12),(.10,-.2),(-.2,-.03)):
        p=abs(t0);q=abs(s0)
        D=4*ROOT2*p+ (2*(q-ROOT2*p)**2/q if q>ROOT2*p else 0.0)
        for k in (0.01,0.003,0.001):
            t,s=k*t0,k*s0
            actual=4*ROOT2-formula(loc(t,s))
            assert abs(actual/k-D)<1.0*k, (t0,s0,k,actual/k,D)
    # Independent numerical integration of the 1-homogeneous deficit's unit sublevel.
    N=120000
    pmax=1/(4*ROOT2)
    I=(pmax/N)*sum((1+math.sqrt(max(0,1-32*(pmax*(j+.5)/N)**2)))/4 for j in range(N))
    area=(4+math.pi)/(64*ROOT2)
    assert abs(I-area)<1e-8,(I,area)
    upper=12*4*area/(4*math.pi)
    assert abs(upper-3*(4+math.pi)/(16*math.pi*ROOT2))<1e-12
    print('PASS', cases, 'independent edge-intersection polygon comparisons, max error',maxerr)
    print('PASS endpoint/tangent formulas, quadrature and sharp tail coefficient',upper)

if __name__=='__main__': check()
