#!/usr/bin/env python3
import cmath
import math

TOL = 2e-9

def source_coeffs(eps, j):
    w = cmath.exp(2j * math.pi * j / 5)
    A = w**4 + w**3 + (2*eps-1)*w**2 - 12*w + (2*eps-1)
    B = (-2*eps-6)*(w**4+w**3) + (4-12*eps)*w**2 + (36-4*eps)*w + (4-12*eps)
    C = 8*(eps-1)*(w+1)**2
    return w, A, B, C

def peval(coef, y):
    z = 0j
    for a in coef:
        z = z*y + a
    return z

def pder(coef, y):
    n = len(coef)-1
    return peval([coef[i]*(n-i) for i in range(n)], y)

def assert_close(z, tol=TOL):
    if abs(z) > tol:
        raise AssertionError(f"residual {z!r} exceeds {tol}")

def full_displayed_lhs(k, j):
    w = cmath.exp(2j * math.pi * j / 5)
    s = math.sin(k)
    c = math.cos(k)
    return (
        w*k**6*s**6
        + k**4*s**4*(w**4+w**3+2*w**2*c-w**2-12*w*c**2+2*c-1)
        + k**2*s**2*(
            w**4*(5*s**2-2*c-6)
            + w**3*(5*s**2-2*c-6)
            + w**2*(18*c*s**2-5*s**2-12*c+4)
            + w*(54*s**4-88*s**2-4*c+36)
            + 18*c*s**2-5*s**2-12*c+4
        )
        + w**4*(3*s**4-4*c*s**2)
        + w**3*(3*s**4-4*c*s**2)
        + w**2*(54*c*s**4-3*s**4-48*c*s**2+8*s**2+8*c-8)
        + 4*w*(27*s**6-51*s**4-2*c*s**2+28*s**2+4*c-4)
        + 54*c*s**4-3*s**4-48*c*s**2+8*s**2+8*c-8
    )

def phase_real(k, j):
    w = cmath.exp(2j * math.pi * j / 5)
    z = full_displayed_lhs(k, j)/w
    if abs(z.imag) > 2e-7*(1+abs(z.real)):
        raise AssertionError("displayed sector expression did not reduce to a real phase")
    return z.real

def bisect(a, b, j, steps=80):
    fa = phase_real(a, j)
    fb = phase_real(b, j)
    if fa*fb > 0:
        raise AssertionError("root not bracketed")
    for _ in range(steps):
        m = (a+b)/2
        fm = phase_real(m, j)
        if fa*fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a+b)/2

sqrt5 = math.sqrt(5.0)
roots = {}
for j in range(5):
    roots[(1,j)] = [8.0] if j == 0 else [5.0, 8.0]
roots[(-1,0)] = [4.0, 6-2*sqrt5, 6+2*sqrt5]
for j in (1,4):
    roots[(-1,j)] = [1.0, 4.0, 6+2*sqrt5]
for j in (2,3):
    roots[(-1,j)] = [1.0, 4.0, 6-2*sqrt5]

# Verify roots and simplicity directly in the source-derived cubic coefficients.
for (eps,j), ys in roots.items():
    coef = source_coeffs(eps,j)
    for y in ys:
        assert_close(peval(coef,y), 2e-8)
        if abs(pder(coef,y)) < 1e-6:
            raise AssertionError(f"non-simple claimed root eps={eps}, j={j}, y={y}")

# Verify the explicit factor families independently via coefficient identities.
def coeff_from_roots(rs):
    c=[1.0]
    for r in rs:
        nc=[0.0]*(len(c)+1)
        for i,a in enumerate(c):
            nc[i]+=a
            nc[i+1]-=a*r
        c=nc
    return c

def normalized_coeffs(eps,j):
    w,A,B,C=source_coeffs(eps,j)
    return [1.0, A/w, B/w, C/w]

factor_roots = {
    (1,0): [0.0,0.0,8.0],
    (-1,0): [4.0,6-2*sqrt5,6+2*sqrt5],
}
for j in range(1,5):
    factor_roots[(1,j)] = [0.0,5.0,8.0]
for j in (1,4): factor_roots[(-1,j)] = [1.0,4.0,6+2*sqrt5]
for j in (2,3): factor_roots[(-1,j)] = [1.0,4.0,6-2*sqrt5]

for key,rs in factor_roots.items():
    got=normalized_coeffs(*key)
    want=coeff_from_roots(rs)
    for a,b in zip(got,want):
        assert_close(a-b, 3e-8)

# The source's displayed asymptotic expression evaluated at k=N+c/N
# has O(N^-2) residual at every claimed nonzero constant.
for (eps,j),ys in roots.items():
    parity = 0 if eps == 1 else 1
    for y in ys:
        c0=math.sqrt(y)
        vals=[]
        for base in (100,200,400):
            n=base+parity
            N=n*math.pi
            vals.append(abs(full_displayed_lhs(N+c0/N,j)))
        if not (vals[0] > 3*vals[1] and vals[1] > 3*vals[2]):
            raise AssertionError((eps,j,c0,vals))

# Representative finite-index roots of the displayed sector expression converge
# to the predicted positive scaled offsets.
checks=[
    (200,1,math.sqrt(5.0)),
    (200,1,math.sqrt(8.0)),
    (201,1,1.0),
    (201,1,2.0),
    (201,1,sqrt5+1),
    (201,2,sqrt5-1),
]
for n,j,c0 in checks:
    N=n*math.pi
    r=bisect(N+(c0-0.08)/N, N+(c0+0.08)/N, j)
    scaled=(r-N)*N
    if abs(scaled-c0)>8e-5:
        raise AssertionError((n,j,c0,scaled))

print("VERIFY_OK")
print("even nonzero union:", [math.sqrt(5.0), 2*math.sqrt(2.0)])
print("odd nonzero union:", [1.0, sqrt5-1, 2.0, sqrt5+1])
