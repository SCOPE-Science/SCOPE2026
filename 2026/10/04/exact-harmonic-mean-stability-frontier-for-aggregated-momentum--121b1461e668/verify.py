from fractions import Fraction
import cmath
import math
import random

def poly_mul(a, b):
    out = [0 for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def poly_add(a, b):
    n = max(len(a), len(b))
    out = [0 for _ in range(n)]
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return out

def char_poly(betas, s):
    # Ascending coefficients.
    prod = [1]
    for b in betas:
        prod = poly_mul(prod, [-b, 1])
    p = poly_mul(prod, [-1, 1])
    qsum = [0]
    for i in range(len(betas)):
        q = [1]
        for j, b in enumerate(betas):
            if i != j:
                q = poly_mul(q, [-b, 1])
        qsum = poly_add(qsum, q)
    term = poly_mul(qsum, [0, s/len(betas)])
    return poly_add(p, term)

def peval(coeff, z):
    acc = 0
    for c in reversed(coeff):
        acc = acc*z + c
    return acc

def durand_kerner(coeff, maxit=4000, tol=1e-13):
    # Monic polynomial, ascending coefficients.
    n = len(coeff)-1
    lead = coeff[-1]
    c = [complex(x/lead) for x in coeff]
    radius = 1.2
    roots = [radius*cmath.exp(2j*math.pi*k/n) for k in range(n)]
    for _ in range(maxit):
        nxt = []
        err = 0.0
        for i, z in enumerate(roots):
            den = 1+0j
            for j, w in enumerate(roots):
                if i != j:
                    den *= (z-w)
            if abs(den) < 1e-20:
                den += 1e-20
            zn = z - peval(c, z)/den
            err = max(err, abs(zn-z))
            nxt.append(zn)
        roots = nxt
        if err < tol:
            return roots
    raise RuntimeError("root solver did not converge")

def sstar(betas):
    return 2*len(betas)/sum(1/(1+b) for b in betas)

# Exact rational P(-1) identity.
for betas in [
    [Fraction(0), Fraction(9,10), Fraction(99,100)],
    [Fraction(1,5), Fraction(2,5)],
    [Fraction(1,3), Fraction(1,3), Fraction(4,5)],
]:
    K = len(betas)
    ss = Fraction(2*K, 1) / sum(Fraction(1,1)/(1+b) for b in betas)
    p = char_poly(betas, ss)
    val = peval(p, Fraction(-1))
    assert val == 0

# Unit-circle phase identity.
for _ in range(200):
    betas = [random.random()*0.999 for _ in range(random.randint(1,5))]
    theta = random.uniform(0.02, math.pi-0.02)
    z = cmath.exp(1j*theta)
    H = sum(z/(z-b) for b in betas)
    lhs = ((1-z)*H.conjugate()).imag
    Dsum = sum((1-b)/(1-2*b*math.cos(theta)+b*b) for b in betas)
    rhs = -math.sin(theta)*Dsum
    assert abs(lhs-rhs) < 2e-12

# Root check around the sharp boundary.
tests = [
    [0.0, 0.9, 0.99],
    [0.2, 0.7],
    [0.1, 0.2, 0.8, 0.95],
    [0.0, 0.9, 0.99, 0.999],
]
for betas in tests:
    ss = sstar(betas)
    for frac in (0.1, 0.5, 0.99):
        roots = durand_kerner(char_poly(betas, frac*ss))
        assert max(abs(r) for r in roots) < 1-1e-8
    roots = durand_kerner(char_poly(betas, ss))
    assert min(abs(r+1) for r in roots) < 1e-8
    roots = durand_kerner(char_poly(betas, 1.01*ss))
    assert max(abs(r) for r in roots) > 1+1e-5

# Default-vector constants and harmonic-mean bounds.
v3 = [0.0, 0.9, 0.99]
v4 = [0.0, 0.9, 0.99, 0.999]
assert abs(sstar(v3) - 2.957371920219007) < 1e-14
assert abs(sstar(v4) - 3.1632074969779493) < 1e-14
for betas in tests:
    ss = sstar(betas)
    assert 2*(1+min(betas)) <= ss + 1e-14
    assert ss <= 2*(1+max(betas)) + 1e-14

# Geometric damping family tends toward 4.
def geo(K, a):
    return [1-a**i for i in range(K)]
assert sstar(geo(1000, 0.1)) > 3.99
assert sstar(geo(1000, 0.5)) > 3.98

print("verification passed")
