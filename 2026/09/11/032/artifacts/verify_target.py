"""Exact verification for lane-738 TARGET (stdlib only, exact integer arithmetic).

Checks:
 (A) Norm identities: 4|nu_j(n)|^2 == 10*F(2n-1)*F(2n+1)*F(2n+3) for j=1..4,
     for n = 2..27 (13 even + 13 odd values => Vandermonde certificate, see DRAFT).
 (B) Distance identities for z-differences (10 consecutive values n=2..11).
 (C) Mass-ratio bound: (cmax/R)^2 = 4/(F(2n-1)F(2n+1)) <= 2/5 < 0.633^2,
     hence M >= 4 - 2*0.633 = 2.734 > 1.1 (disc-average lemma, see DRAFT).
 (D) Arc bound: Fibonacci step lemma F(m+1)<=2F(m), F(m+2)<=3F(m) (m>=2) gives
     F(2n+3)^2/(F(2n-1)F(2n+1)) <= 27, so (chord/R^{1/3})^6 <= 400*27 = 10800
     <= 4.71^6 (exact integer check below); arc <= (pi/2)*chord < 15 R^{1/3}.
 (E) Integrality: F(3n), F(3n+3) even; N_n integer (one of F(2n-1),F(2n+1),F(2n+3) even).
"""
from fractions import Fraction

def fib(k):
    assert k >= 0
    x, y = 0, 1
    for _ in range(k):
        x, y = y, x + y
    return x

def Z(n):
    return [(-2*fib(n-1), 2*fib(n+2)), (-fib(n-2), fib(n+1)),
            (fib(n-1), -fib(n+2)), (fib(n), -fib(n+3))]

def base(n):
    assert fib(3*n) % 2 == 0 and fib(3*n+3) % 2 == 0
    return (fib(3*n+3)//2, fib(3*n)//2)

# (A) norm identities, 26 consecutive n = 13 per parity
for n in range(2, 28):
    A, B = base(n)
    s = 1 if n % 2 == 0 else -1
    N = 0
    for (zx, zy) in Z(n):
        q = (A + s*zx)**2 + (B + s*zy)**2
        N = q if N == 0 else N
        assert q == N, f"norm mismatch n={n}"
    assert 4*N == 10*fib(2*n-1)*fib(2*n+1)*fib(2*n+3), f"R identity fail n={n}"
print("A: norm identities n=2..27 OK")

# (B) distance identities, n=2..11
expect = {(0,1): (10, -1), (0,2): (18, 1), (0,3): (10, 3),
          (1,2): (2, 3), (1,3): (10, 1), (2,3): (2, -1)}
for n in range(2, 12):
    z = Z(n)
    for (i, j), (c, k) in expect.items():
        q = (z[i][0]-z[j][0])**2 + (z[i][1]-z[j][1])**2
        assert q == c*fib(2*n+k), f"dist fail n={n} pair={(i,j)}: {q} vs {c*fib(2*n+k)}"
print("B: distance identities n=2..11 OK")

# (C) mass bound: F(2n-1)F(2n+1) >= F3*F5 = 10, increasing
for n in range(2, 28):
    assert fib(2*n-1)*fib(2*n+1) >= 10
assert Fraction(633, 1000)**2 > Fraction(2, 5), "sqrt(2/5) < 0.633"
assert 4 - 2*Fraction(633, 1000) > Fraction(11, 10), "M >= 2.734 > 1.1"
print("C: mass bound M >= 2.734 > 1.1 for all n>=2 OK")

# (D) arc bound
# step lemma instances + ratio spot-checks
for m in range(2, 60):
    assert fib(m-1) <= fib(m) and fib(m+1) <= 2*fib(m) and fib(m+2) <= 3*fib(m)
for n in range(2, 28):
    r = Fraction(fib(2*n+3)**2, fib(2*n-1)*fib(2*n+1))
    assert r <= 27, f"ratio fail n={n}: {r}"
assert 471**6 >= 10800 * 100**6, "4.71^6 >= 10800"
assert Fraction(22, 7) < Fraction(315, 100), "pi < 3.15 usable"
assert Fraction(315, 200)*Fraction(471, 100) < 15, "(pi/2)*4.71 < 15"
print("D: chord <= 4.71 R^{1/3}, arc <= 15 R^{1/3} OK")

# (E) parity/integrality
assert [fib(m) % 2 for m in range(12)] == [0,1,1,0,1,1,0,1,1,0,1,1]
for n in range(2, 28):
    assert (5*fib(2*n-1)*fib(2*n+1)*fib(2*n+3)) % 2 == 0, f"N integer fail n={n}"
print("E: parity/integrality OK")
print("VERIFY_OK")
