import math

def boundary_point(delta, m):
    assert 0 < delta <= 2 and 0 <= m <= 1
    if m <= delta/2:
        return (1-delta/4-m*m/(3*delta), 2*m/(3*delta))
    return (1-math.sqrt(2*delta*m)/3, 1-math.sqrt(2*delta/m)/3)

def area_formula(delta):
    if delta <= 2:
        return 4 - 44*delta/27 + (8*delta/9)*math.log(delta/2)
    eta=4-delta
    lam=eta/delta
    return lam*lam*area_formula(eta)

def numerical_cap_barycenter(delta, m, N=250000):
    # Direction proportional to (1,m). Integrate vertical fibers of the exact cap.
    # The threshold in unnormalised support coordinates is chosen from the analytic cap geometry.
    if m <= delta/2:
        # trapezoid: x >= 1-delta/2-m*y
        sy=sx=area=0.0
        dy=2/N
        for j in range(N):
            y=-1+(j+0.5)*dy
            xl=1-delta/2-m*y
            w=1-xl
            area += w*dy
            sx += 0.5*(1-xl*xl)*dy
            sy += y*w*dy
        return sx/area, sy/area, area
    # triangle: x + m y >= 1+m-d, d=sqrt(2 delta m)
    d=math.sqrt(2*delta*m)
    y0=1-d/m
    sy=sx=area=0.0
    dy=(1-y0)/N
    for j in range(N):
        y=y0+(j+0.5)*dy
        xl=1+(m*(1-y)-d)
        w=1-xl
        area += w*dy
        sx += 0.5*(1-xl*xl)*dy
        sy += y*w*dy
    return sx/area, sy/area, area

def polygon_area_from_boundary(delta, N=5000):
    octant=[boundary_point(delta, j/N) for j in range(N+1)]
    pts=[]
    for x,y in octant:
        pts.extend([(x,y),(y,x),(-y,x),(-x,y),(-x,-y),(-y,-x),(y,-x),(x,-y)])
    pts=sorted(set((round(x,14),round(y,14)) for x,y in pts), key=lambda p: math.atan2(p[1],p[0]))
    s=0.0
    for i,p in enumerate(pts):
        q=pts[(i+1)%len(pts)]
        s += p[0]*q[1]-p[1]*q[0]
    return abs(s)/2

for delta in (0.1, 0.5, 1.0, 2.0):
    for m in (0.0, min(delta/4,1.0), min(delta/2,1.0), (min(delta/2,1.0)+1)/2, 1.0):
        if m==0 and delta/2 < 0: continue
        x,y=boundary_point(delta,m)
        xn,yn,a=numerical_cap_barycenter(delta,m,N=12000)
        assert abs(a-delta) < 3e-8, (delta,m,a)
        assert abs(x-xn) < 3e-7 and abs(y-yn) < 3e-7, (delta,m,(x,y),(xn,yn))
        if m <= delta/2:
            assert abs(x-(1-delta/4-3*delta*y*y/4)) < 1e-12
        else:
            assert abs((1-x)*(1-y)-2*delta/9) < 1e-12
    an=polygon_area_from_boundary(delta, N=2500)
    af=area_formula(delta)
    assert abs(an-af) < 2e-6, (delta,an,af)

for delta in (2.2, 3.0, 3.8):
    eta=4-delta
    lam=eta/delta
    assert abs(area_formula(delta)-lam*lam*area_formula(eta)) < 1e-14

print('VERIFY_OK square Ulam body boundary and area')
