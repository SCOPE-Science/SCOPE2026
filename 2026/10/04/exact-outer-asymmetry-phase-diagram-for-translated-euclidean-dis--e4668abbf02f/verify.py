from math import cos, sin, sqrt, pi

def poly_threshold(a):
    return 4*a**6 + 7*a**4 - 2*a**2 - 1

def threshold():
    lo, hi = 0.0, 1.0
    for _ in range(120):
        mid = (lo + hi)/2
        if poly_threshold(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2

A0 = threshold()

def ystar(a):
    return (3*a**4 + 18*a*a - 5 - (1-a*a)*sqrt(9*a**4 - 2*a*a + 57))/(16*a*a)

def closed(a):
    if a == 0:
        return 0.0
    pref = 8*a*(1-a*a)**1.5/pi
    if a <= A0:
        return pref*(1+a*a)
    y = ystar(a)
    return pref*sqrt((1-y)*((1+a*a)**2 - 4*a*a*y)/(1-a*a*y)**4)

def raw_outer(a, t):
    # Boundary point x=(a+cos t,sin t), outward normal n=(cos t,sin t),
    # positively oriented tangent v=(-sin t,cos t).
    u = cos(t)
    s = sin(t)
    disc = sqrt(max(0.0, 1-a*a*u*u))
    bx = -2*disc*s
    by =  2*disc*u

    L = 1+a*a+2*a*u
    lam = (1-a*a)/L
    px = -lam*(a+u)
    py = -lam*s

    # Unit outward normal at p, because p lies on the translated unit circle.
    upx = px-a
    upy = py
    norm = sqrt(upx*upx+upy*upy)
    upx /= norm
    upy /= norm
    vpx, vpy = -upy, upx
    discp = sqrt(max(0.0, 1-a*a*upx*upx))
    bpx = 2*discp*vpx
    bpy = 2*discp*vpy
    return abs(bx*bpy-by*bpx)/pi

samples = [0.1, 0.3, 1/sqrt(3), 0.65, 0.68, 0.69, 0.75, 0.85, 0.95]
N = 120000
for a in samples:
    brute = 0.0
    for j in range(N):
        t = 2*pi*j/N
        brute = max(brute, raw_outer(a,t))
    assert abs(brute-closed(a)) < 2e-8, (a, brute, closed(a))

assert abs(A0-0.6833726274004417) < 5e-15
assert poly_threshold(1/sqrt(3)) < 0
family_max = 64*sqrt(2)/(27*pi)
assert abs(closed(1/sqrt(3))-family_max) < 2e-15

# High-branch witness: z^2=y*, converted back by u=(z-a)/(1-a*z).
for a in (0.70,0.80,0.90):
    z = sqrt(ystar(a))
    u = (z-a)/(1-a*z)
    t = __import__("math").acos(u)
    assert abs(raw_outer(a,t)-closed(a)) < 3e-14

print("VERIFY_OK translated-disk outer asymmetry phase diagram")
