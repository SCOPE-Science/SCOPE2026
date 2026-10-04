from math import acos, asin, cos, sin, pi, sqrt

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def vertex(n, rho, j):
    th = 2*pi*j/n
    return (sin(rho)*cos(th), sin(rho)*sin(th), cos(rho))

def dist(a,b):
    z = max(-1.0, min(1.0, dot(a,b)))
    return acos(z)

def profile(n, omega):
    c = cos(pi/(2*n))
    rho = asin(sin(omega/2)/c)
    asym = 1/(2*c-1)
    from_def = sin(rho)/(2*sin(omega/2)-sin(rho))
    return rho, asym, from_def

for n in range(3, 64, 2):
    for omega in (0.05, 0.3, 0.8, 1.2, pi/2):
        rho, asym, from_def = profile(n, omega)
        assert 0 < rho < omega <= pi/2 + 1e-15
        V = [vertex(n,rho,j) for j in range(n)]
        # Farthest vertex distance is omega.
        maxd = max(dist(V[i],V[j]) for i in range(n) for j in range(i+1,n))
        assert abs(maxd-omega) < 3e-12, (n,omega,maxd)
        # Regular-vertex vector average is cos(rho) times the axis.
        avg = tuple(sum(v[k] for v in V)/n for k in range(3))
        assert abs(avg[0]) < 2e-14 and abs(avg[1]) < 2e-14 and abs(avg[2]-cos(rho)) < 2e-14
        # The Hou--Jin expression cancels the width exactly.
        assert abs(asym-from_def) < 3e-13
        # A sampled boundary of B(o,omega-rho) lies in every radius-omega disk.
        rr = omega-rho
        for q in range(73):
            th = 2*pi*q/73
            x = (sin(rr)*cos(th), sin(rr)*sin(th), cos(rr))
            for v in V:
                assert dist(x,v) <= omega + 2e-12

# Triangle endpoint and monotonicity along odd n.
rho, a3, _ = profile(3, 0.9)
assert abs(a3-(1+sqrt(3))/2) < 2e-14
vals = [profile(n,0.9)[1] for n in range(3,101,2)]
assert all(vals[i] > vals[i+1] for i in range(len(vals)-1))

# Asymptotic coefficients.
for n in (1001, 2001, 4001):
    a = profile(n,0.7)[1]
    approx4 = 1 + pi*pi/(4*n*n) + 11*pi**4/(192*n**4)
    assert abs(a-approx4) < 2e-18 + 5/n**6

print("VERIFY_OK spherical Reuleaux asymmetry profile")
