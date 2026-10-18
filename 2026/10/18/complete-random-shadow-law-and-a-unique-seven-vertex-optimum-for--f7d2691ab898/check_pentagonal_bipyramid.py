"""Independent finite checks for the exact random silhouette law of pentagonal bipyramids.

Requires only Python 3's standard library. Numerical tests support, but do not
replace, the proof of the all-height laws and uniqueness theorem.
"""
import math
import random

PI = math.pi
R = math.cos(PI / 5)
SINES = [math.sin(k * PI / 10) for k in range(1, 6)]
BASE = [(math.cos(2*j*PI/5), math.sin(2*j*PI/5), 0.0) for j in range(5)]


def law(h):
    lam = h / math.hypot(R, h)
    s = [0.0] + [math.asin(lam * a) for a in SINES]
    j = [s[k] - s[k-1] for k in range(1, 6)]
    c = 10 / PI
    p = {4: c*j[4], 7: c*(j[1]-j[2]),
         6: c*(j[0]-j[1]+j[2]-j[3])}
    p[5] = 1 - p[4] - p[6] - p[7]
    assert abs(sum(p.values())-1) < 1e-13
    assert min(p.values()) > -1e-13
    return p


def derivative(lam):
    a, b, c = SINES[:3]
    return 2*b/math.sqrt(1-(lam*b)**2) - a/math.sqrt(1-(lam*a)**2) - c/math.sqrt(1-(lam*c)**2)


def determinant(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def hull_count(points):
    pts = sorted(points)
    lower = []
    for pt in pts:
        while len(lower) > 1 and determinant(lower[-2], lower[-1], pt) <= 1e-12:
            lower.pop()
        lower.append(pt)
    upper = []
    for pt in reversed(pts):
        while len(upper) > 1 and determinant(upper[-2], upper[-1], pt) <= 1e-12:
            upper.pop()
        upper.append(pt)
    return len(lower) + len(upper) - 2


def direct_orthographic_shadow_count(h, u):
    ux,uy,uz = u
    a = math.hypot(ux, uy)
    e = (-uy/a, ux/a, 0.)
    f = (-ux*uz/a, -uy*uz/a, a)
    vertices = BASE + [(0.,0.,h),(0.,0.,-h)]
    polygon = [(sum(v[i]*e[i] for i in range(3)),
                sum(v[i]*f[i] for i in range(3))) for v in vertices]
    return hull_count(polygon)


def wedge_prediction(h,u):
    ux,uy,uz=u
    t=h*math.hypot(ux,uy)/uz
    phi=math.atan2(uy,ux)
    cs=[t*math.cos(phi - (2*j+1)*PI/5) for j in range(5)]
    kp=sum(x>R for x in cs)
    km=sum(x<-R for x in cs)
    return 5+(2-kp if kp else 0)+(2-km if km else 0)


def check():
    rng = random.Random(161082)
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid=(lo+hi)/2
        if derivative(mid)>0: lo=mid
        else: hi=mid
    lm=(lo+hi)/2
    hm=R*lm/math.sqrt(1-lm*lm)
    assert .67129 < lm < .67130
    assert .73271 < hm < .73273
    assert .08958 < law(hm)[7] < .08960
    for h in [0.08, (math.sqrt(5)-1)/2, hm, 1.0, 3.0, 20.0]:
        counts={n:0 for n in range(4,8)}
        trials=40000
        for _ in range(trials):
            phi=2*PI*rng.random()
            z=0.000001+(1-0.000001)*rng.random()
            u=(math.sqrt(1-z*z)*math.cos(phi), math.sqrt(1-z*z)*math.sin(phi), z)
            n1=wedge_prediction(h,u)
            n2=direct_orthographic_shadow_count(h,u)
            assert n1==n2, (h,u,n1,n2)
            assert n1 in counts
            counts[n1]+=1
        expected=law(h)
        assert all(abs(counts[n]/trials-expected[n]) < .015 for n in counts),(h,counts,expected)
        print('SHADOW_HULL_AND_FREQUENCY_OK h=',round(h,9),'trials=',trials,'law=',expected)
    assert derivative(0)>0 and derivative(1)<0
    assert derivative(lm-1e-4)>0 and derivative(lm+1e-4)<0
    hj=(math.sqrt(5)-1)/2
    assert derivative(hj/math.hypot(R,hj))>0
    print('UNIQUE_HEIGHT_NUMERIC_CHECK_OK',lm,hm,law(hm)[7])
    print('PENTAGONAL_BIPYRAMID_SILHOUETTE_OK')

if __name__=='__main__':
    check()
