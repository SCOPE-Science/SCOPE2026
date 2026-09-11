"""Verify the elementary complete INTEGRAL-point determination for
C4: y^2 = x^5 - 5x^3 + 4x^2 + x - 1, i.e. f(x) = (x-1)*g(x),
g(x) = x^4 + x^3 - 4x^2 + 1.

Checks (exact integer arithmetic only):
 1. f = (x-1)*g identity; disc = 1957 = 19*103 (nonzero -> smooth affine model).
 2. Sandwich identities: 4g - A^2 = -(x-2)(x-6) [A=2x^2+x-4];
    B^2 - 4g = 5x^2-6x+5, disc -64 [B=2x^2+x-3];
    4g - A2^2 = 3x^2+10x-21 [A2=2x^2+x-5];
    B2^2 - 4g = (x-2)(x-6) [B2=A].
 3. Coprimality: g(x) = (x-1)*q(x) - 1, so gcd(x-1, g(x)) = 1 for integer x.
 4. Key values: g(-3), g(-2..6), f(-3..6); between-squares exclusions;
    monotonicity witnesses M(2), M(-3), M'(signs) with M = 4x^2+3x-8.
Run: python3 verify_integral.py  -> prints VERIFY_OK on success.
"""
import math

def g(x): return x**4 + x**3 - 4*x**2 + 1
def f(x): return x**5 - 5*x**3 + 4*x**2 + x - 1
def A(x): return 2*x*x + x - 4
def B(x): return 2*x*x + x - 3
def A2(x): return 2*x*x + x - 5

ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: ok = False

def bareiss_det(A):
    A = [row[:] for row in A]; n = len(A); prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            s = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if s is None: return 0
            A[k], A[s] = A[s], A[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
    return A[n - 1][n - 1]

# 0. EXACT discriminant of f via Bareiss on the 9x9 Sylvester matrix of (f, f').
fC = [1, 0, -5, 4, 1, -1]   # x^5 .. x^0
fpC = [5, 0, -15, 8, 1]     # x^4 .. x^0
N = 9
S = [[0] * N for _ in range(N)]
for i in range(4):
    for j, c in enumerate(fC): S[i][i + j] += c
for i in range(5):
    for j, c in enumerate(fpC): S[4 + i][i + j] += c
res = bareiss_det(S)
check("Res(f,f') = 1957 (exact Bareiss)", res == 1957)
check("disc(f) = 1957 = 19*103 != 0 (smooth)", res == 19 * 103 and res != 0)

# 1. identity f=(x-1)g for a range + coefficient check via expansion at 7 points
# (degree <=5 identity verified on 7 distinct nodes => holds identically)
check("factor identity on -3..6", all(f(x) == (x-1)*g(x) for x in range(-3, 7)))
# discriminant of f verified in sympy session as 1957 (recorded); re-verify resultant-free:
# skip recompute here; identity (x-1)g recorded with g(1)=-1:
check("g(1)=-1", g(1) == -1)

# 2. sandwich identities on -10..10
check("4g-A^2 == -(x-2)(x-6)", all(4*g(x)-A(x)**2 == -(x-2)*(x-6) for x in range(-10, 11)))
check("B^2-4g == 5x^2-6x+5", all(B(x)**2-4*g(x) == 5*x*x-6*x+5 for x in range(-10, 11)))
check("4g-A2^2 == 3x^2+10x-21", all(4*g(x)-A2(x)**2 == 3*x*x+10*x-21 for x in range(-10, 11)))
d = 36 - 4*5*5
check("disc(5x^2-6x+5)=-64", d == -64)
check("5x^2-6x+5>0 on -10..10", all(5*x*x-6*x+5 > 0 for x in range(-10, 11)))
check("3x^2+10x-21>0 at x>=2 sample", all(3*x*x+10*x-21 > 0 for x in [2,3,4,5,6,100]))

# 3. coprimality: g(x)+1 divisible by (x-1) with quotient q; check q exact on samples
def q(x): return (g(x)+1)//(x-1) if x != 1 else 4  # g'(1)=4*1+3-8+... g'(x)=4x^3+3x^2-8x -> g'(1)=-1? limit q(1)=(g(x)+1)/(x-1)|_{x=1}
# verify divisibility for samples
check("x-1 | g+1 on samples", all((g(x)+1) % (x-1) == 0 for x in range(-10, 11) if x != 1))
# hence any common divisor of (x-1) and g(x) divides 1:
check("gcd samples = 1", all(math.gcd(x-1, g(x)) == 1 for x in range(-10, 11) if x != 1))

# 4a. values
check("g(-3)=19", g(-3) == 19)
check("g(2)=9", g(2) == 9)
check("g(6)=1369=37^2", g(6) == 1369 == 37**2)
check("f values -3..6", [f(x) for x in range(-3,7)] == [-76,21,6,-1,0,9,146,771,2604,6845])
check("f(6) strictly between 82^2,83^2", 82**2 < f(6) < 83**2)
check("21 nonsquare", 16 < 21 < 25)
check("6 nonsquare", 4 < 6 < 9)
check("f(-3)<0, f(0)<0", f(-3) < 0 and f(0) < 0)
# 4b. monotonicity witnesses: M(x)=4x^2+3x-8; M(2)=14; M(-3)=19; M'=8x+3
def M(x): return 4*x*x+3*x-8
check("M(2)=14", M(2) == 14)
check("M(-3)=19", M(-3) == 19)
# M'>0 for x>=0 (8x+3>0); M'<0... M'=8x+3<0 for x<=-1: so M decreasing on (-inf,-3], M(x)>=M(-3)=19 there
check("M(-4)>=19 (decreasing check sample)", M(-4) == 64-12-8 == 44 and M(-4) >= 19)
# 4c. sandwich strictness: for integer x in {3,4,5}: A^2<4g<B^2
for x in [3,4,5]:
    check(f"x={x}: A^2<4g<B^2", A(x)**2 < 4*g(x) < B(x)**2)
# x=6: equality below, strict above
check("x=6: 4g==A^2<B^2", 4*g(6) == A(6)**2 and A(6)**2 < B(6)**2)
# x>6 sample: A2^2<4g<A^2 (B2=A): check x=7..20
check("x=7..20: A2^2<4g<A^2", all(A2(x)**2 < 4*g(x) < A(x)**2 for x in range(7, 21)))
# nonsquare consequence: no square strictly between consecutive squares
def nonsquare_between(m2, v, M2):
    r = math.isqrt(v)
    return r*r != v
check("g(3),g(4),g(5) nonsquare", all(math.isqrt(g(x))**2 != g(x) for x in [3,4,5]))

print("VERIFY_OK" if ok else "VERIFY_FAIL")
