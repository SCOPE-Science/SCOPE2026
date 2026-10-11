#!/usr/bin/env python3
"""Independent diagnostics for finite-moment inversion of orthotope shadows.
Python 3 standard library only. Finite quadrature checks supplement the proof.
"""
import math
import random
from itertools import product

PI = math.pi
COEFF3 = 3 * (4 - PI) / (8 * PI)

def legendre_rule(n):
    out = []
    for j in range(1, n + 1):
        z = math.cos(PI * (j - .25) / (n + .5))
        for _ in range(30):
            a, b = 1., z
            for k in range(2, n + 1):
                a, b = b, ((2 * k - 1) * z * b - (k - 1) * a) / k
            pp = n * (z * b - a) / (z * z - 1)
            v = z - b / pp
            if abs(v - z) < 2e-15:
                z = v
                break
            z = v
        w = 2 / ((1 - z * z) * pp * pp)
        out.append((.5 * (z + 1), .5 * w))
    return out

def moments(area_triplet):
    a, b, c = area_triplet
    e1 = a + b + c
    e2 = a * b + b * c + c * a
    e3 = a * b * c
    return (e1 / 2,
            e1 ** 2 / 3 - 2 * (PI - 2) / (3 * PI) * e2,
            e1 ** 3 / 4 - 3 * e1 * e2 / 8 + COEFF3 * e3)

def inversion(m):
    m1, m2, m3 = m
    e1 = 2 * m1
    e2 = (e1 * e1 - 3 * m2) * PI / (2 * (PI - 2))
    e3 = (m3 - e1 ** 3 / 4 + 3 * e1 * e2 / 8) / COEFF3
    p = e2 - e1 * e1 / 3
    q = -2 * e1 ** 3 / 27 + e1 * e2 / 3 - e3
    if p > -1e-11:
        return (e1 / 3,) * 3
    arg = (3 * q / (2 * p)) * math.sqrt(-3 / p)
    theta = math.acos(max(-1., min(1., arg))) / 3
    amp = 2 * math.sqrt(-p / 3)
    return tuple(sorted(e1 / 3 + amp * math.cos(theta - 2 * PI * j / 3)
                        for j in range(3)))

def sides_from_faces(x):
    a, b, c = x
    return tuple(sorted((math.sqrt(b * c / a), math.sqrt(a * c / b), math.sqrt(a * b / c))))

def numeric_moments(areas, rule):
    u, v = areas[0], areas[1]
    zcoef = areas[2]
    out = [0., 0., 0.]
    for t, wt in rule:
        r = math.sqrt(1 - t * t)
        for z, wz in rule:
            phi = PI * z / 2
            f = r * (u * math.cos(phi) + v * math.sin(phi)) + zcoef * t
            w = wt * wz
            ff = f
            for k in range(3):
                out[k] += w * ff
                ff *= f
    return tuple(out)

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def proj_area_by_hull(sides, normal):
    n=normal
    pivot=(0.,0.,1.) if abs(n[2])<.8 else (0.,1.,0.)
    e1=cross(n,pivot); s=norm(e1);e1=tuple(x/s for x in e1)
    e2=cross(n,e1)
    pts=[]
    for eps in product((-1.,1.),repeat=3):
        p=tuple(eps[i]*sides[i]/2 for i in range(3))
        pts.append((dot(p,e1),dot(p,e2)))
    pts=sorted(set(pts))
    def cr(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]; hi=[]
    for p in pts:
        while len(lo)>=2 and cr(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi)>=2 and cr(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    h=lo[:-1]+hi[:-1]
    return .5*abs(sum(h[i][0]*h[(i+1)%len(h)][1]-h[i][1]*h[(i+1)%len(h)][0] for i in range(len(h))))

def higher_dim_tests():
    checks=0
    rng=random.Random(97113)
    for d in range(2,9):
        raw=[1.]+[2**(k/2)*math.gamma((k+1)/2)/math.sqrt(math.pi)
                   for k in range(1,d+1)]
        kappa=[0.]*(d+1)
        for k in range(1,d+1):
            kappa[k]=raw[k]-sum(math.comb(k-1,j-1)*kappa[j]*raw[k-j]
                                    for j in range(1,k))
            assert abs(kappa[k])>1e-10,(d,k,kappa[k]);checks+=1
        for trial in range(8):
            q=[rng.uniform(.75,1.25) for _ in range(d)]
            cumul=[0.]+[kappa[k]*sum(x**k for x in q) for k in range(1,d+1)]
            h=[1.]+[0.]*d
            for k in range(1,d+1):
                h[k]=sum(math.comb(k-1,j-1)*cumul[j]*h[k-j]
                           for j in range(1,k+1))
            observed=[1.]+[h[k]/(2**(k/2)*math.gamma((d+k)/2)/math.gamma(d/2))
                          for k in range(1,d+1)]
            recovered_h=[1.]+[observed[k]*(2**(k/2)*math.gamma((d+k)/2)/math.gamma(d/2))
                              for k in range(1,d+1)]
            K=[0.]*(d+1);e=[1.]+[0.]*d
            for k in range(1,d+1):
                K[k]=recovered_h[k]-sum(math.comb(k-1,j-1)*K[j]*recovered_h[k-j]
                                       for j in range(1,k))
                pp=K[k]/kappa[k]
                assert abs(pp-sum(x**k for x in q))<1e-5;checks+=1
                e[k]=sum((-1)**(j-1)*e[k-j]*K[j]/kappa[j] for j in range(1,k+1))/k
            for x in q:
                residual=sum((-1)**j*e[j]*x**(d-j) for j in range(d+1))
                assert abs(residual)<1e-4,(d,trial,residual)
                checks+=1
    return checks

def main():
    rng=random.Random(827194)
    rule=legendre_rule(128)
    nchecks=0
    for a,b,c in [(1,1,1),(1,2,3),(.4,1.1,3.2),(2,4,5)]+[
       (math.exp(rng.uniform(-.9,.9)),math.exp(rng.uniform(-.9,.9)),math.exp(rng.uniform(-.9,.9))) for _ in range(14)]:
        coeff=(b*c,a*c,a*b)
        ana=moments(coeff)
        numeric=numeric_moments(coeff,rule)
        for x,y in zip(ana,numeric):
            assert abs(x-y)<4e-6*max(1,abs(x)),(coeff,ana,numeric)
            nchecks+=1
        inv=inversion(ana)
        for x,y in zip(inv,sorted(coeff)):
            assert abs(x-y)<1e-5*max(1,x),(coeff,inv)
            nchecks+=1
        srec=sides_from_faces(inv)
        for x,y in zip(srec,sorted((a,b,c))):
            assert abs(x-y)<1e-5*max(1,x),(coeff,srec)
            nchecks+=1
        for k in range(4):
            v=[rng.gauss(0,1) for _ in range(3)]; l=norm(v);v=tuple(x/l for x in v)
            direct=proj_area_by_hull((a,b,c),v)
            formula=coeff[0]*abs(v[0])+coeff[1]*abs(v[1])+coeff[2]*abs(v[2])
            assert abs(formula-direct)<1e-11*max(1,formula)
            nchecks+=1
    x=(1.,2.,3.)
    z=1/math.sqrt(3);y=(2+z,2+z,2-2*z)
    aa=moments(x);bb=moments(y)
    assert abs(aa[0]-bb[0])<1e-12 and abs(aa[1]-bb[1])<1e-12
    assert abs(aa[2]-bb[2])>1e-5
    nchecks+=3
    last=None
    for eps in (.2,.1,.05):
        x=(1-eps,1.,1+eps);z=eps/math.sqrt(3)
        y=(1-z,1-z,1+2*z)
        mx,my=moments(x),moments(y)
        assert abs(mx[0]-my[0])<1e-13 and abs(mx[1]-my[1])<1e-13
        delta=abs(mx[2]-my[2]);expected=COEFF3*2*eps**3/(3*math.sqrt(3))
        assert math.isclose(delta,expected,rel_tol=1e-9)
        dist=max(abs(a-b) for a,b in zip(sides_from_faces(x),sides_from_faces(y)))
        assert .3*eps<dist<2*eps
        if last:
            assert abs(delta/last[0]-(eps/last[1])**3)<1e-9
        last=(delta,eps)
        nchecks+=4
    nchecks+=higher_dim_tests()
    print('VERIFY_OK',nchecks,'checks; all-d moment-cumulant identities, quadrature, direct hull, inversion, sharpness')

if __name__=='__main__':main()
