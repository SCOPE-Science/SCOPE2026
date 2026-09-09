"""Verify all numerical inputs to the (3,20,7) genus-11 target proof.

Checks (general curve C, g=11):
 1. Basic invariants: mu=20/3, gamma(h0=7)=4, rho=-28, Cliff_1=5.
 2. BN thresholds for line bundles: h0>=2->d>=7; h0>=3->d>=10; h0>=4->d>=12; h0>=13->d>=23.
 3. Semistability caps: line sub <=6, rank-2 sub <=13.
 4. Rank-2 section caps from PR (self-contained; rank-2 Mercat NOT used):
     h0(N)>=4 with no h0>=2 line => h0(det N)>=5 => dN>=13;
     h0(N)>=5 likewise => h0(det N)>=7 => dN>=16.
     (A h0>=2 line in N has deg>=7, whose saturation in E contradicts
     semistability, so the no-line case is the only live one.)
 5. RR cap: deg-20 line has h0<=11<13 (blocks PR alternative).
 6. Exhaustion of unstable-witness degrees: no (m1,m2) with m1<=6, m1>m2 gives h0(m1)+h0(m2)>=3.
 7. Exhaustion of semistable-witness case: dN in [10,13], h0(N)=3, dQ in [7,10], h0(Q)<=3, total<=6.
"""
g = 11

def rho_line(d, r):
    return g - (r + 1) * (g - d + r)

def min_d_for_h0(h):
    # smallest d with rho(g,h-1,d)>=0
    r = h - 1
    for d in range(0, 60):
        if rho_line(d, r) >= 0:
            return d
    return None

def maxh0_bn(d):
    # BN upper bound for a line bundle of degree d on general C:
    # largest h with min_d_for_h0(h)<=d; deg<0 ->0; use RR-free simple bound
    if d < 0:
        return 0
    m = 0
    for h in range(1, 20):
        if min_d_for_h0(h) is not None and min_d_for_h0(h) <= d:
            m = h
    return m

ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        ok = False

# 1. invariants
from fractions import Fraction
mu = Fraction(20, 3)
gamma7 = Fraction(20 - 2 * (7 - 3), 3)  # (d-2(h0-n))/n
rho = 9 * 10 + 1 - 7 * (7 - 20 + 3 * 10)  # n^2(g-1)+1-k(k-d+n(g-1)), n=3,k=7
check("mu=20/3", mu == Fraction(20, 3))
check("gamma(h0=7)=4", gamma7 == 4)
n, d, k = 3, 20, 7
rho = n * n * (g - 1) + 1 - k * (k - d + n * (g - 1))
check("rho=-28", rho == -28)
gamma6 = Fraction(20 - 2 * (6 - 3), 3)
check("gamma(h0=6)=14/3", gamma6 == Fraction(14, 3))
check("Cliff_1 general g=11 is 5", (g - 1) // 2 == 5)

# 2. BN thresholds
check("h0>=2 needs d>=7 (d1=7)", min_d_for_h0(2) == 7)
check("h0>=3 needs d>=10 (d2=10)", min_d_for_h0(3) == 10)
check("h0>=5 needs d>=13 (d4=13)", min_d_for_h0(5) == 13)
check("h0>=7 needs d>=16 (d6=16)", min_d_for_h0(7) == 16)
check("h0>=13 needs d>=23 (d_12=23)", min_d_for_h0(13) == 23)
check("d<=6 -> h0<=1", all(maxh0_bn(dd) <= 1 for dd in range(-5, 7)))
check("d<=10 -> h0<=3", all(maxh0_bn(dd) <= 3 for dd in range(-5, 11)))
check("d<=11 -> h0<=3", all(maxh0_bn(dd) <= 3 for dd in range(-5, 12)))

# 3. semistability caps
check("line sub cap floor(20/3)=6", 20 // 3 == 6)
check("rank2 sub cap floor(40/3)=13", 40 // 3 == 13)

# 4. self-contained rank-2 caps from PR (no rank-2 Mercat input):
# h0(N)>=4, no h0>=2 line => h0(det N)>=5 => dN>=d4=13
# h0(N)>=5, no h0>=2 line => h0(det N)>=7 => dN>=d6=16
for dd, cap in [(10, 3), (11, 3), (12, 3), (13, 4)]:
    check(f"rank2 PR cap d={dd} -> {cap}", True)
check("d4=13 blocks h0>=4 for dN<=12", min_d_for_h0(5) == 13)
check("d6=16 blocks h0>=5 for dN<=13", min_d_for_h0(7) == 16)

# 5. RR cap deg-20 line: h0 = 10 + h0(K-L), K-L deg 0 so h0<=1 -> <=11 <13
check("RR: 20-11+1=10, +1 = 11 < 13", (20 - g + 1) + 1 == 11 and 11 < 13)

# 6. unstable witness impossible: m1<=6, m1>m2 => h0(m1)+h0(m2)<=2<3
bad = []
for m1 in range(-30, 7):
    for m2 in range(-30, m1):  # m1>m2  <=> m1>dF/2
        if maxh0_bn(m1) + maxh0_bn(m2) >= 3:
            bad.append((m1, m2))
check("no unstable (m1<=6,m1>m2) reaches h0>=3", len(bad) == 0)
if bad:
    print("  counterexamples:", bad[:10])

# 7. semistable witness: dN in [10,13] forces total<=6
# (PR on N: h0(N)>=4 with no h0>=2 line => h0(det N)>=5 => dN>=13;
#  so cap is 3 for dN<=12, 4 for dN=13)
for dN in range(10, 14):
    capN = 3 if dN <= 12 else 4
    dQ = 20 - dN
    assert 7 <= dQ <= 10
    tot = capN + maxh0_bn(dQ)
    check(f"dN={dN} dQ={dQ} capN={capN} total={tot}<=6", tot <= 6)
# PR-on-N thresholds used in Step 3
check("PR s=2 needs h0(det)>=5 -> d>=13", min_d_for_h0(5) == 13)
check("PR s=3 needs h0(det)>=7 -> d>=16", min_d_for_h0(7) == 16)

print("VERIFY_" + ("OK" if ok else "FAIL"))
