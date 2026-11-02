"""Reproducibility checks for weighted polygon-boundary random hulls.

Uses Python standard library only. Numerical checks supplement, and do not
replace, the exact geometric and probabilistic arguments in RESULT.md.
"""
import math
import random
from math import comb


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def hull(points):
    pts = sorted(set(tuple(p) for p in points))
    if len(pts) <= 1:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross((lower[-1][0]-lower[-2][0], lower[-1][1]-lower[-2][1]), (p[0]-lower[-1][0], p[1]-lower[-1][1])) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross((upper[-1][0]-upper[-2][0], upper[-1][1]-upper[-2][1]), (p[0]-upper[-1][0], p[1]-upper[-1][1])) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def area(poly):
    return abs(sum(cross(p, q) for p, q in zip(poly, poly[1:] + poly[:1])))/2 if len(poly) >= 3 else 0.0


def coeffs(poly):
    m = len(poly)
    edges = [(poly[(i+1)%m][0]-poly[i][0], poly[(i+1)%m][1]-poly[i][1]) for i in range(m)]
    return [cross(edges[(i-1)%m], edges[i])/2 for i in range(m)]


def leading(c, w):
    m = len(c)
    return sum(c[i]/(w[(i-1)%m]*w[i]) for i in range(m))


def gradient(c, w):
    m = len(c)
    return [-(c[i]/w[(i-1)%m] + c[(i+1)%m]/w[(i+1)%m])/w[i]**2 for i in range(m)]


def exact_mixed_nearest_moment(n, a, b):
    numerator = 1-(1-a)**(n+2)-(1-b)**(n+2)+(1-a-b)**(n+2)
    return numerator/(a*b*(n+1)*(n+2))


def polynomial_moment(n, a, b):
    total = 0.0
    for j in range(n+1):
        for k in range(n+1-j):
            total += comb(n, j)*comb(n-j, k)*(-a)**j*(-b)**k/((j+1)*(k+1))
    return total


def run():
    rng = random.Random(20261025)
    polys = [
      [(0.,0.),(2.,0.),(.8,1.7)],
      [(0.,0.),(2.,0.),(2.,1.),(0.,1.)],
      [(0.,0.),(2.,0.),(2.4,1.),(1.5,2.1),(-.4,1.2)],
      [(0.,0.),(2.,0.),(1.75,1.1),(-.2,.85)],
    ]
    for poly in polys:
        m = len(poly)
        c = coeffs(poly)
        assert min(c) > 0
        edges = [(poly[(i+1)%m][0]-poly[i][0], poly[(i+1)%m][1]-poly[i][1]) for i in range(m)]
        for _ in range(75):
            parameters = [sorted(rng.random() for __ in range(6)) for i in range(m)]
            samples = [(poly[i][0]+t*edges[i][0], poly[i][1]+t*edges[i][1]) for i in range(m) for t in parameters[i]]
            missing = area(poly) - area(hull(samples))
            corner = sum(c[i]*(1-parameters[(i-1)%m][-1])*parameters[i][0] for i in range(m))
            assert abs(missing-corner) < 1e-9, (missing, corner)
    print('GEOMETRIC_IDENTITY_PASSED')

    for n in range(1,9):
        for a,b in [(.12,.24),(.23,.42),(.33,.1)]:
            x = exact_mixed_nearest_moment(n,a,b)
            y = polynomial_moment(n,a,b)
            assert abs(x-y) < 1e-9, (n,a,b,x,y)
    print('EXACT_MIXED_MOMENTS_PASSED')

    for poly in polys:
        c=coeffs(poly);m=len(c);w=[1/m]*m
        g=gradient(c,w)
        for i in range(m):
            d=[0.]*m; j=(i+1)%m; d[i]=1;d[j]=-1
            h=1e-6
            p=[w[k]+h*d[k] for k in range(m)]
            q=[w[k]-h*d[k] for k in range(m)]
            fd=(leading(c,p)-leading(c,q))/(2*h)
            pred=sum(g[k]*d[k] for k in range(m))
            assert abs(fd-pred) < 1e-4, (fd,pred)
    triangle=polys[0]
    assert max(coeffs(triangle))-min(coeffs(triangle)) < 1e-12
    para=polys[1]
    assert max(coeffs(para))-min(coeffs(para)) < 1e-12
    quad=polys[3];c=coeffs(quad);w=[.25]*4
    g=gradient(c,w); center=sum(g)/4
    direction=[-(v-center) for v in g]
    norm=max(abs(v) for v in direction)
    w_new=[w[i]+0.001*direction[i]/norm for i in range(4)]
    assert leading(c,w_new) < leading(c,w)
    print('OPTIMIZATION_AND_PARITY_TESTS_PASSED')

    c=coeffs(polys[2]);m=len(c);w=[.1,.15,.3,.2,.25]
    theoretical_mean=leading(c,w)
    theoretical_var=3*sum((c[i]/(w[(i-1)%m]*w[i]))**2 for i in range(m))
    samples=[]
    for _ in range(40000):
        s=sum(c[i]/(w[(i-1)%m]*w[i])*rng.expovariate(1)*rng.expovariate(1) for i in range(m))
        samples.append(s)
    sample_mean=sum(samples)/len(samples)
    sample_var=sum((s-sample_mean)**2 for s in samples)/len(samples)
    assert abs(sample_mean/theoretical_mean-1)<.025
    assert abs(sample_var/theoretical_var-1)<.12
    print('LIMITING_MEAN_VARIANCE_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    run()
