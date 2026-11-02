"""Reproducible checks for the one-dimensional active exclusion mean-field ring.

Requires only Python 3 standard library.  Checks are finite consistency tests,
not a proof of the theorem for arbitrary parameters or ring sizes.
"""
import cmath
import math
import random

checks = 0

def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def rhs(p, wa, wt, wr):
    n = len(p)
    occ = [u[0] + u[1] for u in p]
    out = [[0j, 0j] for _ in range(n)]
    for i in range(n):
        for a, direction in enumerate((1, -1)):
            im = (i - direction) % n
            ip = (i + direction) % n
            active = wa * (p[im][a]*(1-occ[i]) - p[i][a]*(1-occ[ip]))
            thermal = 0j
            for step in (-1, 1):
                thermal += p[(i-step)%n][a]*(1-occ[i]) - p[i][a]*(1-occ[(i+step)%n])
            out[i][a] = active + wt*thermal + wr*(p[i][1-a]-p[i][a])
    return out


def symbol(k, phi, wa, wt, wr):
    q = 1-math.cos(k)
    t = wa+2*wt
    return ((-t*q, -1j*wa*(1-phi)*math.sin(k)),
            (-1j*wa*(1-2*phi)*math.sin(k), -2*wr-(1-phi)*t*q))


def finite_activity_expression(n, phi, wa, wt, wr):
    s2 = math.sin(math.pi/n)**2
    return ((1-phi)*(2*phi*(1-s2)-1)*wa**2
            -(wr+4*(1-phi)*wt*s2)*wa
            -2*wr*wt-4*(1-phi)*wt**2*s2)


def threshold(n, phi, wt, wr):
    s2 = math.sin(math.pi/n)**2
    c = (1-phi)*(2*phi*(1-s2)-1)
    if c <= 0:
        return math.inf
    ell = wr+4*(1-phi)*wt*s2
    h = 2*wr*wt+4*(1-phi)*wt**2*s2
    return (ell+math.sqrt(ell*ell+4*c*h))/(2*c)


def max_real_nonconstant(n, phi, wa, wt, wr):
    largest = -math.inf
    for m in range(1,n):
        k = 2*math.pi*m/n
        a=symbol(k,phi,wa,wt,wr)
        tr=a[0][0]+a[1][1]
        det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
        roots = ((tr+cmath.sqrt(tr*tr-4*det))/2,
                 (tr-cmath.sqrt(tr*tr-4*det))/2)
        largest=max(largest,roots[0].real,roots[1].real)
    return largest


def assert_close(u, v, tol=2e-6):
    require(abs(u-v)<=tol*(1+abs(v)), f"Mismatch: {u} vs {v}")


# Independent direct derivative of the nonlinear N-site equation.
for n in (3,4,5,6,8,11,15):
    for phi,wa,wt,wr in ((0.12,0.5,0.4,1.4),
                         (0.57,8.0,0.0,1.0),
                         (0.9,60.0,0.2,1.0)):
        for m in range(1,n):
            k=2*math.pi*m/n
            j=symbol(k,phi,wa,wt,wr)
            for c in (0,1):
                eps=1e-8
                delta=[(0.5*cmath.exp(1j*k*i)*(1 if c==0 else 1),
                        0.5*cmath.exp(1j*k*i)*(1 if c==0 else -1))
                       for i in range(n)]
                p=[(phi/2+eps*u,phi/2+eps*v) for u,v in delta]
                vals=rhs(p,wa,wt,wr)
                predicted = (j[0][c],j[1][c])
                assert_close((vals[0][0]+vals[0][1])/eps,predicted[0])
                assert_close((vals[0][0]-vals[0][1])/eps,predicted[1])

# Check the closed determinant and trace identities mode by mode.
rng=random.Random(20261028)
for _ in range(120):
    n=rng.randint(3,35)
    phi=rng.uniform(.02,.98)
    wa=10**rng.uniform(-1,3)
    wt=10**rng.uniform(-2,2) if rng.random()<.6 else 0.0
    wr=10**rng.uniform(-2,1)
    for m in range(1,n):
        k=2*math.pi*m/n
        q=1-math.cos(k)
        j=symbol(k,phi,wa,wt,wr)
        tr=j[0][0]+j[1][1]
        det=j[0][0]*j[1][1]-j[0][1]*j[1][0]
        t=wa+2*wt
        det_formula=q*(2*(wr*t-wa*wa*(1-phi)*(2*phi-1))
                       +q*(1-phi)*(t*t+wa*wa*(2*phi-1)))
        assert_close(tr,-2*wr-(2-phi)*t*q,1e-10)
        assert_close(det,det_formula,1e-10)
    criterion=finite_activity_expression(n,phi,wa,wt,wr)
    growth=max_real_nonconstant(n,phi,wa,wt,wr)
    if abs(criterion)>1e-7*(1+wa**2+wt**2):
        require((growth>0)==(criterion>0),
                f"Instability mismatch N={n}, parameters={(phi,wa,wt,wr)}")

# No ring with 3 or 4 sites becomes linearly unstable at any finite activity.
for n in (3,4):
    for phi in (.02,.5,.75,.9,.999):
        for wa in (.01,1,100,1e5):
            for wt in (0,1,100):
                require(not (finite_activity_expression(n,phi,wa,wt,1)>0),
                        f"Small-ring counterexample: {n}, {phi}, {wa}, {wt}")
                require(max_real_nonconstant(n,phi,wa,wt,1)<1e-7,
                        "Small ring unexpectedly unstable")

# N=5 is attainable only above the exact density boundary 3-sqrt(5).
phi5=3-math.sqrt(5)
assert_close(phi5,1/(2*math.cos(math.pi/5)**2),1e-14)
for phi in (0.65,phi5-1e-4,phi5,phi5+1e-4,0.9):
    crit=threshold(5,phi,0,1)
    if phi<=phi5:
        require(math.isinf(crit) or crit>1e14, "Unexpected five-site instability")
    else:
        require(math.isfinite(crit) and crit>0,"No positive five-site threshold")
        require(max_real_nonconstant(5,phi,crit*.9,0,1)<1e-8,"Below threshold unstable")
        require(max_real_nonconstant(5,phi,crit*1.1,0,1)>1e-8,"Above threshold stable")

# Exact activity onset and strict threshold ordering for representative parameters.
for n in (5,6,8,12,30):
    for phi in (.65,.8,.95):
        for wt in (0,1.5,10.0):
            r=threshold(n,phi,wt,1)
            if math.isfinite(r):
                assert_close(finite_activity_expression(n,phi,r,wt,1),0,1e-7)
                require(finite_activity_expression(n,phi,r*1.01,wt,1)>0,"Upper side")
                require(finite_activity_expression(n,phi,r*.99,wt,1)<0,"Lower side")

print(f"PASS {checks} deterministic consistency assertions")
