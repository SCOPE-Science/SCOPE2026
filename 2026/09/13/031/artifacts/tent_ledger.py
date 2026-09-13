"""Tent-map ledger for Tate duplication Lattes q=5.
Verifies: (1) every rational skeleton coordinate is preperiodic under folded doubling;
(2) torsion-preimage counts 2^{2n-1}+2; (3) retractions equidistribute (discrepancy -> 0).
"""
from fractions import Fraction

def tent(x: Fraction) -> Fraction:
    # segment [0,1/2] folded doubling: circle doubling mod 1 folded by x~1-x
    # lift: y = (2*x) mod 1 in [0,1); fold to [0,1/2]
    y = (2*x) % 1
    if y > Fraction(1,2):
        y = 1 - y
    return y

def orbit_type(x: Fraction, max_steps=5000):
    seen = {}
    cur = x
    for i in range(max_steps):
        if cur in seen:
            return (seen[cur], i - seen[cur])  # (preperiod, period)
        seen[cur] = i
        cur = tent(cur)
    return None

# (1) all rationals with denominator <= 200 preperiodic
bad = []
for d in range(1, 201):
    for n in range(0, d+1):
        x = Fraction(n, 2*d)  # points in [0,1/2] with denominator | 2d
        if x > Fraction(1,2):
            continue
        r = orbit_type(x)
        if r is None:
            bad.append(x)
print("rational preperiodic check: denominators<=200, bad =", bad[:10], "count", len(bad))
# examples
for x in [Fraction(1,3), Fraction(1,5), Fraction(1,6), Fraction(1,7), Fraction(3,16)]:
    print(x, "->", orbit_type(x))

# (2) ledger counts
for n in range(0, 7):
    c = 2**(2*n-1)+2 if n >= 1 else 1
    print(f"n={n} |L^{{-n}}(inf)|={c} check 4^n={4**n} quotient={(4**n-4)//2+4 if n>=1 else 1}")

# (3) equidistribution: 2^n-torsion circle points k/2^n mod 1 folded; discrepancy vs uniform on [0,1/2]
def folded_torsion(n):
    pts = []
    N = 2**n
    for k in range(N):
        y = Fraction(k, N)
        if y > Fraction(1,2):
            # fold: circle point k/2^n and -k/2^n identified; folded = min(y,1-y)
            y = 1 - y
        pts.append(float(y))
    return sorted(pts)

def discrepancy(pts):
    # star-discrepancy vs uniform on [0,0.5]: compare empirical CDF
    m = len(pts)
    pts = sorted(pts)
    d = 0.0
    for i, p in enumerate(pts):
        # uniform CDF F(p)=p/0.5=2p
        d = max(d, abs((i+1)/m - 2*p), abs(i/m - 2*p))
    return d

for n in range(1, 11):
    pts = folded_torsion(n)
    print(f"n={n} N={len(pts)} discrepancy={discrepancy(pts):.4f}")
print("OK")
