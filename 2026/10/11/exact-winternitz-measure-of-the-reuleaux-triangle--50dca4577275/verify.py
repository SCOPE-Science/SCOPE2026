import math

SQ3 = math.sqrt(3.0)
centers = [
    (0.0, 1.0/SQ3),
    (-0.5, -1.0/(2.0*SQ3)),
    (0.5, -1.0/(2.0*SQ3)),
]

def radial(phi):
    ux, uy = math.cos(phi), math.sin(phi)
    # Along x = r u, membership in each unit disk is
    # r^2 - 2(c.u)r + |c|^2 - 1 <= 0.
    # Starting at r=0, the exit radius is the smaller positive upper root
    # across the three disks.
    bounds = []
    for cx, cy in centers:
        dot = cx*ux + cy*uy
        c2 = cx*cx + cy*cy
        disc = dot*dot + 1.0 - c2
        assert disc > 0
        bounds.append(dot + math.sqrt(disc))
    return min(bounds)

def simpson(f, a, b, n=12000):
    assert n % 2 == 0
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1,n):
        s += (4 if i % 2 else 2)*f(a+i*h)
    return s*h/3.0

def half_area(theta):
    return 0.5*simpson(lambda p: radial(p)**2, theta, theta+math.pi, 12000)

A0 = (math.pi-math.sqrt(3.0))/2.0
s0 = (math.acos(1.0/(2.0*math.sqrt(3.0)))
      - math.pi/6.0
      - (math.sqrt(11.0)+math.sqrt(3.0))/12.0)
depth = s0/A0
ratio = (A0-s0)/s0

assert abs(half_area(0.0)-s0) < 2e-10
assert abs(half_area(math.pi/6.0)-A0/2.0) < 2e-10

vals = [half_area((math.pi/6.0)*j/100.0) for j in range(101)]
assert all(vals[i+1] >= vals[i]-2e-10 for i in range(100))

x0 = math.sqrt(33.0)/6.0 - 0.5
def prim(t):
    return 0.5*(t*math.sqrt(1.0-t*t)+math.asin(t))
direct = 2.0*(-x0/(2.0*math.sqrt(3.0)) + prim(x0+0.5)-prim(0.5))
assert abs(direct-s0) < 2e-15

assert abs(A0-0.704770923010458) < 2e-15
assert abs(depth-0.4733904338011144) < 2e-15
assert abs(ratio-1.112421224844882) < 3e-15

# Directly verify the analytic c-difference formula on the fundamental interval.
Rc = 1.0/math.sqrt(3.0)
def c(phi):
    return Rc*math.cos(phi-7.0*math.pi/6.0)
for j in range(101):
    th = (math.pi/6.0)*j/100.0
    lhs = c(th+math.pi/3.0)-c(th)
    rhs = math.sin(th)/math.sqrt(3.0)
    assert abs(lhs-rhs) < 2e-15

print("VERIFY_OK")
print("area =", A0)
print("small_half =", s0)
print("depth =", depth)
print("ratio =", ratio)
