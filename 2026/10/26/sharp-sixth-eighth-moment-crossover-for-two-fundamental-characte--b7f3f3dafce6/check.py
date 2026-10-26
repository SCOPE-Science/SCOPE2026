"""Standalone exact Weyl-constant-term verification for USp(4) character moments.
Run: python3 check.py.  Only the Python standard library is required.
"""
from collections import defaultdict
from math import comb, cos, pi, sqrt, isclose


def product(f, g):
    out = defaultdict(int)
    for (i, j), a in f.items():
        for (k, l), b in g.items():
            out[(i+k, j+l)] += a*b
    return {k: v for k, v in out.items() if v}


def power(f, n):
    out = {(0, 0): 1}
    for _ in range(n):
        out = product(out, f)
    return out


A = {(1, 0): 1, (-1, 0): 1, (0, 1): 1, (0, -1): 1}
B = {(0, 0): 1, (1, 1): 1, (1, -1): 1, (-1, 1): 1, (-1, -1): 1}
ROOTS = ((2, 0), (0, 2), (1, 1), (1, -1))
W = {(0, 0): 1}
for r, s in ROOTS:
    W = product(W, {(0, 0): 2, (r, s): -1, (-r, -s): -1})
assert W.get((0, 0)) == 8


def moment(n, k):
    coeff = product(product(power(A, n-k), power(B, k)), W).get((0, 0), 0)
    assert coeff % 8 == 0, (n, k, coeff)
    return coeff//8


EXPECTED = {
    0: [1],
    2: [1, 0, 1],
    4: [3, 0, 2, 0, 3],
    6: [14, 0, 11, 0, 10, 0, 15],
    8: [84, 0, 75, 0, 73, 0, 75, 0, 105],
}
for n, row in EXPECTED.items():
    assert [moment(n, k) for k in range(n+1)] == row


def moment_complex(a, b, m):
    mu = EXPECTED[2*m]
    return sum(comb(m, i)*comb(m, j) *
               a**(m-i)*b**i * a.conjugate()**(m-j)*b.conjugate()**j *
               mu[i+j] for i in range(m+1) for j in range(m+1)).real


def aligned(p, m):
    q = 1-p
    return sum(comb(2*m, 2*j)*EXPECTED[2*m][2*j] *
               p**(m-j)*q**j for j in range(m+1))


def H6(p):
    return 14*p**3 + 165*p**2*(1-p) + 150*p*(1-p)**2 + 15*(1-p)**3


def H8(p):
    q=1-p
    return 84*p**4+2100*p**3*q+5110*p**2*q**2+2100*p*q**3+105*q**4


for k in range(1001):
    p = k/1000
    assert isclose(aligned(p, 3), H6(p), abs_tol=1e-8)
    assert isclose(aligned(p, 4), H8(p), abs_tol=1e-7)

p6 = (sqrt(365)-15)/8
h = lambda p: 157*p**3-240*p**2-40*p+60
lo, hi = 0.0, 1.0
for i in range(90):
    mid=(lo+hi)/2
    if h(mid)>0: lo=mid
    else: hi=mid
p8 = (lo+hi)/2
assert 0.5 < p6 < 0.52
assert 0.49 < p8 < 0.5
assert p8 < p6
assert h(0.5) == -3/8
assert isclose(h(p8), 0.0, abs_tol=1e-12)
assert isclose(H6(p6), 43.019700544257629, abs_tol=1e-11)
assert isclose(H8(p8), 593.6996346023551, abs_tol=1e-10)


def quadrature(a, b, m, N=64):
    total = 0.0
    for j in range(N):
        theta=2*pi*j/N
        z=2*cos(theta)
        for k in range(N):
            phi=2*pi*k/N
            x=z+2*cos(phi)
            y=1+4*cos(theta)*cos(phi)
            density=(2-2*cos(2*theta))*(2-2*cos(2*phi)) * \
                (2-2*cos(theta+phi))*(2-2*cos(theta-phi))/8
            total += abs(a*x+b*y)**(2*m)*density
    return total/(N*N)

for m in (3,4):
    for a,b in ((1+0j, 0j), (0j,1+0j), (0.3+0.4j, -0.7+0.25j),
                (sqrt(.3)+0j, -sqrt(.7)+0j)):
        exact = moment_complex(a,b,m)
        numeric = quadrature(a,b,m)
        assert isclose(exact,numeric,rel_tol=1e-10,abs_tol=1e-8), (m,a,b,exact,numeric)
        assert exact <= (abs(a)**2+abs(b)**2)**m * (H6(p6) if m==3 else H8(p8))+1e-9

print('PASS: exact Weyl moment tables (degrees 0,2,4,6,8);')
print('polynomial formulas, unique critical points, crossover signs;')
print('and independent 64x64 torus quadrature for 8 complex tests.')
print('p6=',repr(p6),'K6=',repr(H6(p6)))
print('p8=',repr(p8),'K8=',repr(H8(p8)))
