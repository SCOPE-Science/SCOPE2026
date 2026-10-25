"""Independent numerical checks of the elliptic-section diameter formulas.

Only the Python standard library is required. Finite computations supplement,
not replace, the analytic arguments in RESULT.md.
"""
import math
import random


def simpson(f, lo, hi, n=12000):
    assert n % 2 == 0
    step = (hi - lo) / n
    total = f(lo) + f(hi)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(lo + j * step)
    return total * step / 3


def section_cdf(radius, a, b, c):
    if radius <= b:
        return 0.0
    if radius >= a:
        return 1.0
    alpha = radius**-2 - a**-2
    beta = b**-2 - radius**-2
    gamma = c**-2 - radius**-2
    def missing(phi):
        h = math.cos(phi)**2 / beta + math.sin(phi)**2 / gamma
        z = alpha * h
        return math.sqrt(z / (1 + z))
    return 1 - 2 / math.pi * simpson(missing, 0, math.pi / 2)


def upper_coefficient(a, b, c):
    d = b**-2 - a**-2
    modulus_squared = 1 - d / (c**-2 - a**-2)
    ell_e = simpson(lambda x: math.sqrt(1 - modulus_squared * math.sin(x)**2),
                    0, math.pi / 2)
    return 2 / math.pi * math.sqrt(2 / (a**3 * d)) * ell_e


def direct_ellipsoid_radius(n, a, b, c):
    nx, ny, nz = n
    if abs(nz) < 0.8:
        u = (ny, -nx, 0.0)
    else:
        u = (0.0, nz, -ny)
    norm = math.sqrt(sum(x*x for x in u))
    u = tuple(x / norm for x in u)
    v = (ny*u[2]-nz*u[1], nz*u[0]-nx*u[2], nx*u[1]-ny*u[0])
    q = (1 / a**2, 1 / b**2, 1 / c**2)
    f = sum(qi * ui*ui for qi, ui in zip(q, u))
    g = sum(qi * vi*vi for qi, vi in zip(q, v))
    h = sum(qi * ui*vi for qi, ui, vi in zip(q, u, v))
    lam = (f+g-math.sqrt((f-g)**2+4*h*h))/2
    return 1 / math.sqrt(lam)


def run():
    a,b,c = 4.,2.,1.
    rng = random.Random(20261018)
    thresholds = (2.2,2.5,3.,3.5,3.8)
    counts = [0] * len(thresholds)
    total = 90000
    for _ in range(total):
        n = [rng.gauss(0,1) for j in range(3)]
        norm = math.sqrt(sum(v*v for v in n))
        n = tuple(v/norm for v in n)
        R = direct_ellipsoid_radius(n,a,b,c)
        for j,r in enumerate(thresholds):
            counts[j] += R <= r
            q1,q2,q3 = a**-2,b**-2,c**-2
            t=r**-2
            alpha,beta,gamma = t-q1,q2-t,q3-t
            cone = (n[0]**2 > alpha*(n[1]**2/beta+n[2]**2/gamma))
            if (R <= r) != cone:
                raise AssertionError('Secular cone vs direct eigenvalue criterion')
    for r,count in zip(thresholds,counts):
        f = section_cdf(r,a,b,c)
        empirical = count/total
        assert abs(f-empirical)<0.01, (r,f,empirical)
    for r in thresholds:
        z=(r**-2-a**-2)/(b**-2-a**-2)
        low=1-math.sqrt(z)
        high=1-2/math.pi*math.asin(math.sqrt(z))
        vals=[section_cdf(r,a,b,x) for x in (0.01,0.5,1.0,1.5,1.99,2.0)]
        assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))
        assert abs(vals[-1]-low)<1e-10
        assert abs(vals[0]-high)<0.001
    L=upper_coefficient(a,b,c)
    for h in (0.02,0.004,0.0006):
        y=(1-section_cdf(a-h,a,b,c))/math.sqrt(h)
        assert abs(y-L) < 0.006, (h,y,L)
    for c0 in (0.25,0.5,1.0,1.5,2.0):
        assert section_cdf(2.8,a,b,c0)<1
        assert upper_coefficient(a,b,c0)>0
    print('TRIAXIAL_SECTION_CHECK_OK','orientations='+str(total),
          'thresholds='+str(len(thresholds)),
          'upper_coefficient='+str(round(L,12)))

if __name__=='__main__':
    run()
