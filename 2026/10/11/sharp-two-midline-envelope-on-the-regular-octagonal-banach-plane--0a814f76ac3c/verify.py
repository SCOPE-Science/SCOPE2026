import math

SQ2 = math.sqrt(2.0)
R = SQ2 - 1.0
B = R * R
C = 2.0 * SQ2 - 1.0
TOL = 2e-9

def N(v):
    s, t = v
    return max(abs(s), abs(t), (abs(s) + abs(t)) / SQ2)

V = [
    (1.0, R), (R, 1.0), (-R, 1.0), (-1.0, R),
    (-1.0, -R), (-R, -1.0), (R, -1.0), (1.0, -R)
]

def seg_intersection(p1, p2, q1, q2):
    dx1, dy1 = p2[0]-p1[0], p2[1]-p1[1]
    dx2, dy2 = q2[0]-q1[0], q2[1]-q1[1]
    det = dx1*(-dy2) - dy1*(-dx2)
    if abs(det) < 1e-12:
        return None
    bx, by = q1[0]-p1[0], q1[1]-p1[1]
    s = (bx*(-dy2) - by*(-dx2)) / det
    u = (dx1*by - dy1*bx) / det
    if -TOL <= s <= 1.0+TOL and -TOL <= u <= 1.0+TOL:
        return (p1[0] + s*dx1, p1[1] + s*dy1)
    return None

def unique(points):
    out = []
    for p in points:
        if not any((p[0]-q[0])**2 + (p[1]-q[1])**2 < 1e-14 for q in out):
            out.append(p)
    return out

def feasible_intersections(a):
    x = (1.0, a)
    shifted = [(x[0]-v[0], x[1]-v[1]) for v in V]
    pts = []
    for i in range(8):
        p1, p2 = V[i], V[(i+1) % 8]
        for j in range(8):
            q1, q2 = shifted[j], shifted[(j+1) % 8]
            z = seg_intersection(p1, p2, q1, q2)
            if z is not None and abs(N(z)-1.0) < 2e-8 and abs(N((x[0]-z[0], x[1]-z[1]))-1.0) < 2e-8:
                pts.append(z)
    return unique(pts)

def canonical_z(a):
    if a <= -B + 1e-12:
        return (R-a, 1.0+a)
    if a <= B + 1e-12:
        return ((1.0-a)/2.0, (1.0+2.0*R+a)/2.0)
    return (1.0-R-a, 1.0)

branch_checks = 0
intersection_checks = 0

for k in range(2001):
    a = -R + 2.0*R*k/2000.0
    x = (1.0, a)
    z = canonical_z(a)
    w = (x[0]-z[0], x[1]-z[1])
    assert abs(N(x)-1.0) < TOL
    assert abs(N(z)-1.0) < TOL
    assert abs(N(w)-1.0) < TOL

    A = N((2.0*x[0]-z[0], 2.0*x[1]-z[1]))
    D = N((x[0]+z[0], x[1]+z[1]))
    assert A <= C + TOL and D <= C + TOL

    if a <= -B + 1e-12:
        assert abs(A-C) < 2e-8
        assert abs(D-(SQ2-a)) < 2e-8
    elif a <= B + 1e-12:
        assert abs(A-(2.0+R-a)/SQ2) < 2e-8
        assert abs(D-(2.0+R+a)/SQ2) < 2e-8
    else:
        assert abs(A-(SQ2+a)) < 2e-8
        assert abs(D-C) < 2e-8
    branch_checks += 1

for k in range(401):
    a = -R + 2.0*R*k/400.0
    x = (1.0, a)
    z = canonical_z(a)
    w = (x[0]-z[0], x[1]-z[1])
    pts = feasible_intersections(a)
    assert len(pts) == 2
    for p in pts:
        assert any((p[0]-q[0])**2 + (p[1]-q[1])**2 < 2e-13 for q in (z, w))
    intersection_checks += 1

x = (1.0, -R)
y = (B, -1.0)
assert abs(N(x)-1.0) < TOL
assert abs(N(y)-1.0) < TOL
assert abs(N((x[0]-y[0], x[1]-y[1]))-1.0) < TOL
A = N((x[0]+y[0], x[1]+y[1]))
D = N((2.0*x[0]-y[0], 2.0*x[1]-y[1]))
assert abs(A-C) < 2e-8 and abs(D-C) < 2e-8

M1 = (A + D) / 2.0
M2 = (A*A + D*D) / 2.0
M3 = (math.sqrt(A) + math.sqrt(D)) / 2.0
assert abs(M1-C) < 2e-8
assert abs(M2-(9.0-4.0*SQ2)) < 2e-8
assert abs(M3-math.sqrt(C)) < 2e-8

print(
    "VERIFY_OK "
    f"branch_checks={branch_checks} "
    f"edge_intersections={intersection_checks} "
    f"M1={M1:.15f} M2={M2:.15f} M3={M3:.15f}"
)
