from math import cos, sin, pi, hypot, sqrt

def pts(n, R=1.0):
    return [(R*cos(2*pi*j/n), R*sin(2*pi*j/n)) for j in range(n)]

def dist(P, Q):
    return hypot(P[0]-Q[0], P[1]-Q[1])

def brute_gap(n, R=1.0):
    P = pts(n, R)
    best = -1.0
    best_sep = None
    for i in range(n):
        for j in range(i+1, n):
            hd = 2.0*min(max(dist(P[i], P[z]), dist(P[j], P[z])) for z in range(n))
            ld = hd - dist(P[i], P[j])
            if ld > best + 1e-12:
                best = ld
                best_sep = min((j-i) % n, (i-j) % n)
    return best, best_sep

def compact_formula(n, R=1.0):
    t = pi/n
    k = max(k for k in range(1, n//2 + 1) if k % 2 == 1)
    m = (k-1)//2
    return 4*R*sin((m+1)*t) - 2*R*sin(k*t), k

def residue_formula(n, R=1.0):
    t = pi/n
    r = n % 4
    if r == 0:
        return 2*R*(sqrt(2)-cos(t))
    if r == 1:
        return R*(2*sqrt(2)*(cos(t/4)-sin(t/4)) - 2*cos(3*t/2))
    if r == 2:
        return R*(2*sqrt(2)*(cos(t/2)+sin(t/2)) - 2)
    return R*(2*sqrt(2)*(cos(t/4)+sin(t/4)) - 2*cos(t/2))

for n in range(3, 81):
    b, sep = brute_gap(n)
    f, k = compact_formula(n)
    g = residue_formula(n)
    assert abs(b-f) < 2e-11, (n, b, f)
    assert abs(f-g) < 2e-11, (n, f, g)
    assert sep == k, (n, sep, k)

# Check convergence to the circle gap and the predicted leading residue-class errors.
circle = 2*(sqrt(2)-1)
for r, lead in [(0, None), (1, -sqrt(2)/2), (2, sqrt(2)), (3, sqrt(2)/2)]:
    n = 4000 + r
    while n % 4 != r:
        n += 1
    t = pi/n
    err = residue_formula(n) - circle
    if r == 0:
        assert abs(err/(t*t) - 1.0) < 2e-4
    else:
        assert abs(err/t - lead) < 2e-3

print("VERIFY_OK regular-polygon convexity gap n=3..80")
