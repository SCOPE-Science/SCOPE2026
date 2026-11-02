"""Reproduce analytic geometric and contact identities for crossing-cylinder ellipsoids.

No finite sampling is claimed to establish global containment or optimality; these
follow from the independent algebraic proof and contact-moment certificates.
"""
import math
import random


def parameters(a, b):
    assert a >= b > 0
    t = (a/b)**2
    x = t / (math.sqrt(t*t-t+1) + t - 1)  # cancellation-resistant
    A = a*a*(1+x)/x
    B = b*b*(1+x)
    C = b*b*(2-x)
    return x, A, B, C


def check(a, b, trials=1000):
    x, A, B, C = parameters(a, b)
    t = (a/b)**2
    assert .5-1e-13 < x <= 1+1e-13
    assert math.isclose(t*(2*x-1), x*(2-x), rel_tol=1e-12, abs_tol=3e-9)
    assert math.isclose(a*a/A+b*b/B, 1, rel_tol=2e-12)
    assert math.isclose((a*a-b*b)/A+b*b/C, 1, rel_tol=2e-12)
    w0, w1 = (1+x)/3, (2-x)/3
    assert math.isclose(w0+w1, 1, rel_tol=1e-12)
    cov = [w0*a*a/A+w1*(a*a-b*b)/A, w0*b*b/B, w1*b*b/C]
    assert all(math.isclose(v, 1/3, rel_tol=2e-12) for v in cov), cov
    ratio2 = A*B*C/(a*a*b**4)
    assert math.isclose(ratio2, (1+x)**2*(2-x)/x, rel_tol=2e-12)
    for _ in range(trials):
        z = random.uniform(-b,b)
        sx = math.sqrt(max(0,a*a-z*z))
        sy = math.sqrt(max(0,b*b-z*z))
        xx = random.uniform(-sx,sx)
        yy = random.uniform(-sy,sy)
        assert xx*xx/A+yy*yy/B+z*z/C <= 1+4e-12
        g=[random.gauss(0,1) for k in range(3)]
        norm=math.sqrt(sum(v*v for v in g))
        xx, yy, z = a*g[0]/norm,b*g[1]/norm,b*g[2]/norm
        assert xx*xx+z*z<=a*a+4e-12
        assert yy*yy+z*z<=b*b+4e-12
    return (x, math.sqrt(ratio2), cov)


if __name__ == '__main__':
    random.seed(10959)
    ratios=[1, 1.00001, 1.05, 1.25, 2, 4, 20, 200]
    result=[]
    for r in ratios:
        x, ratio, cov=check(r,1.0,3000)
        result.append(ratio)
        print(f'a/b={r:8.5f} x={x:.12f}  L/J={ratio:.12f} contact_var={cov}')
    assert all(z>y for y,z in zip(result,result[1:]))
    assert math.isclose(result[0],2.0,abs_tol=1e-12)
    assert result[-1]<3*math.sqrt(3)/2
    print('PASS: contact algebra, analytic ratio, finite point checks, strict sampled monotonicity.')
