"""Verify J_t transverse Mahler computations for target claim (stdlib only)."""
from fractions import Fraction
import math

def A_of(t):
    # t as Fraction; A = vol(J_t)/32
    s = Fraction(0)
    for j in range(1, 6):
        from math import comb
        c = comb(5, j) * (j ** 5)
        term = Fraction(c, 120) / (1 + (5 - j) * t)
        if (5 - j) % 2 == 1:
            s -= term
        else:
            s += term
    return s / ((1 + 5 * t) ** 5)

def B_of(t):
    return 120*t**5+600*t**4+600*t**3+200*t**2+25*t+1

def R_of(t):
    return A_of(t)*B_of(t)

# checks
print("A(0) =", A_of(Fraction(0)), "B(0) =", B_of(Fraction(0)), "R(0) =", R_of(Fraction(0)))
assert A_of(Fraction(0)) == 1 and B_of(Fraction(0)) == 1

# one-sided derivative via small rational h
h = Fraction(1, 10**6)
dR = (R_of(h) - 1) / h
print("difference quotient R(h)/h at h=1e-6:", float(dR))
assert dR > Fraction(9) and dR < Fraction(11), "R'(0) should be ~10"

# second: exact derivative R'(0) = A'(0)+B'(0); A'(0)=-15, B'(0)=25
# verify numerically
dA = (A_of(h)-1)/h
dB = (B_of(h)-1)/h
print("dA ~", float(dA), " dB ~", float(dB))
assert dA > Fraction(-16) and dA < Fraction(-14)
assert dB > Fraction(24) and dB < Fraction(26)

# Hanner_5 vertex counts by recursion: H_n = H_k x_1 H_{n-k} (l1-sum) or x_infty (product)
# V(l1) = V1+V2, V(linf) = V1*V2. Base V(H_1)=2.
def hanner_vertices(n):
    if n == 1:
        return {2}
    out = set()
    for k in range(1, n):
        for a in hanner_vertices(k):
            for b in hanner_vertices(n-k):
                out.add(a+b)
                out.add(a*b)
    # dedupe by symmetry k<->n-k automatically in set
    return out

for n in range(1, 6):
    print(f"Hanner_{n} vertex counts:", sorted(hanner_vertices(n)))
assert 242 not in hanner_vertices(5), "J_t (242 vertices) is non-Hanner"

# J_t vertex count (t>0): support-pattern vertices c*1_S, c=1/(1+t|S|):
# total nonzero = sum_{m=1..5} C(5,m)2^m = 3^5-1 = 242.
# axial (m=1): 10 x e_i/(1+t); diagonal (m=5): 32 x (+-1)/(1+5t) are
# two of the five support patterns. Verify they satisfy f_t=1.
def ft(x, t):
    return max(abs(v) for v in x) + t*sum(abs(v) for v in x)
t = 0.1
for i in range(5):
    x = [0.0]*5; x[i] = 1/(1+t)
    assert abs(ft(x, t)-1) < 1e-12
x = [1/(1+5*t)]*5
assert abs(ft(x, t)-1) < 1e-12
print("vertex feasibility OK")

# exact R(t) table + transverse check vs delta<=5t upper bound:
# need R(t)-1 >= kappa*25*t^2 with kappa=1/16, i.e. >= (25/16) t^2, on [0, 0.01]
print("\nt, R(t), (R-1)/t^2:")
for num in [0, 1, 2, 5, 10, 25, 50, 100, 250]:
    tt = Fraction(num, 10000)  # 0..0.025
    r = R_of(tt)
    gap = r - 1
    print(f"{float(tt):.4f}  R={float(r):.8f}  gap={float(gap):.6e}", end="")
    if tt > 0:
        print(f"  gap/t^2={float(gap/(tt*tt)):.4f}  (need>=1.5625)", end="")
        assert gap/(tt*tt) >= Fraction(25,16), f"fails at t={tt}"
    print()

# cross-check vol(Q_t) by Monte Carlo-free Riemann check in 2D analogue? Instead
# verify polar formula R_t={y>=0: sum(y_i-t)_+<=1} at t=0 gives simplex vol 1/120.
# General formula vol = sum_k C(5,k) t^{5-k}/k! ; check k=5 term=1/120 at t=0. OK by construction.
# Independent numeric check: midpoint Riemann sum for vol(J_t) in positive orthant at t=0.1
t = 0.1
N = 60
hstep = 1.0/N
count = 0
tot = 0
for multi in range(N**5):
    # too big (60^5); use coarser: N=12
    break
N = 12
hstep = 1.0/N
inside = 0
for i1 in range(N):
    for i2 in range(N):
        for i3 in range(N):
            for i4 in range(N):
                for i5 in range(N):
                    x = [(i+0.5)*hstep for i in (i1,i2,i3,i4,i5)]
                    if max(x)+t*sum(x) <= 1:
                        inside += 1
riem = inside*(hstep**5)
exact = float(A_of(Fraction(1,10)))
print(f"\nRiemann vol(Q_0.1)={riem:.5f} exact={exact:.5f}")
assert abs(riem-exact) < 0.02
print("Riemann cross-check OK")

# independent numeric check of polar positive part via Riemann
N = 14
hstep = 2.0/N
inside = 0
for i1 in range(N):
    for i2 in range(N):
        for i3 in range(N):
            for i4 in range(N):
                for i5 in range(N):
                    y = [(i+0.5)*hstep for i in (i1,i2,i3,i4,i5)]
                    if sum(max(v-t,0) for v in y) <= 1:
                        inside += 1
riem = inside*(hstep**5)
exact = float(B_of(Fraction(1,10))/120)
print(f"Riemann vol(R_0.1)={riem:.5f} exact={exact:.5f}")
assert abs(riem-exact) < 0.05
print("Polar Riemann cross-check OK")

# proved BM upper bound only: d(J_t,C)-1 <= 5t by the sandwich
# (1/(1+5t))C subset J_t subset C. Volume-ratio quantities below are
# reference only, NOT BM lower bounds.
for num in [1, 5, 10]:
    tt = Fraction(num, 1000)
    a = A_of(tt)
    lb = float(a) ** (-0.2) - 1
    print(f"t={float(tt)}: volume-ratio quantity (NOT a BM lower bound) q={lb:.6f}; proved BM upper 5t={float(5*tt)}")
    assert lb > 0

print("\nVERIFY_OK")
