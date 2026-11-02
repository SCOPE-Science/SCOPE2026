"""Exact-rational independent checks of two-defect normal-mode thresholds.

Python 3 standard library only. This is a finite diagnostic, not a proof
of the statements quantified over all chain lengths.
"""
from fractions import Fraction as F
from math import isqrt


def laplacian_entry(n, i, j):
    if i == j:
        return F(1 if i in (0, n - 1) else 2)
    return F(-1 if abs(i - j) == 1 else 0)


def green_entry(n, i, j):
    # Zero-indexed inverse of 4I minus the free-boundary path Laplacian.
    a, b = min(i, j) + 1, max(i, j) + 1
    return F((-1) ** (i + j) * (2*a-1) * (2*(n-b)+1), 4*n)


def rank2_positive_count(n, a, b, contrast):
    aa = green_entry(n, a, a)
    bb = green_entry(n, b, b)
    ab = green_entry(n, a, b)
    t = F(1, 4) / contrast
    determinant = (aa-t)*(bb-t)-ab*ab
    trace = aa+bb-2*t
    if determinant < 0:
        return 1
    if determinant > 0:
        return 2 if trace > 0 else 0
    return None  # An exact band-edge mode: skip generic inertia check.


def direct_inertia(n, a, b, contrast):
    # Symmetric tridiagonal H = L - 4M. LDL signs independently count
    # its positive eigenvalues (Sylvester inertia, with nonzero pivots).
    previous = None
    positives = 0
    for i in range(n):
        d = F((1 if i in (0, n-1) else 2)-4)
        if i in (a, b):
            d += 4*contrast
        if previous is not None:
            if previous == 0:
                return None
            d -= 1/previous
        if d == 0:
            return None
        positives += int(d > 0)
        previous = d
    return positives


def test_inverse(n):
    for i in range(n):
        for k in range(n):
            value = sum((4*int(i == j) - laplacian_entry(n, i, j)) *
                        green_entry(n, j, k) for j in range(n))
            assert value == int(i == k), (n,i,k,value)


def test_geometric_bound(n, a, b):
    # Exact bound beta_min <= n/8 checked without square roots:
    # the smaller eigenvalue is <= Rayleigh quotient (1,-sgn G_ab).
    u = F(2*a+1, 2*n) # zero-indexed a -> 1-indexed a+1
    v = F(2*(n-(b+1))+1, 2*n)
    s = u+v
    assert 0 < s < 1
    aa = green_entry(n,a,a)
    bb = green_entry(n,b,b)
    ab = abs(green_entry(n,a,b))
    rq = (aa+bb-2*ab)/2
    assert rq == F(n,2)*s*(1-s)
    assert rq <= F(n,8)


def run():
    inv = 0
    for n in range(3,19):
        test_inverse(n)
        inv += n*n
    tests = 0
    skipped = 0
    geometry = 0
    deltas = [F(1,101),F(3,17),F(23,61),F(47,89),F(5,7),F(89,101)]
    for n in range(3,35):
        for a in range(n-1):
            for b in range(a+1,n):
                test_geometric_bound(n,a,b); geometry+=1
                for delta in deltas:
                    predicted = rank2_positive_count(n,a,b,delta)
                    actual = direct_inertia(n,a,b,delta)
                    if predicted is None or actual is None:
                        skipped += 1
                        continue
                    assert actual == predicted, (n,a,b,delta,actual,predicted)
                    tests += 1
    # Exact sharpness witness for every n=2 mod 4: quarter placements.
    sharpness = 0
    for n in range(6,103,4):
        a = (n+2)//4 - 1
        b = (3*n+2)//4 - 1
        aa = green_entry(n,a,a)
        bb = green_entry(n,b,b)
        ab = abs(green_entry(n,a,b))
        assert aa == bb
        assert aa-ab == F(n,8)
        assert F(1,4)/(aa-ab) == F(2,n)
        sharpness += 1
    print('PASS: exact Green inverse entries:',inv)
    print('PASS: exact geometric Rayleigh checks:',geometry)
    print('PASS: rank-two vs full-system inertia:',tests)
    print('Skipped singular-pivot/equality diagnostics:',skipped)
    print('PASS: sharp quarter-site witnesses:',sharpness)

if __name__=='__main__':
    run()
