"""Chiral slope-equation analysis for t12533 (exact rational arithmetic).
IIS Thm 1.3 (+/--type, n+n'!=0, v3!=0): m/(n+n') = C0 = 6033/323.
Scope: |H1| = |m| <= 30, r=m/n != s=m/n'.
Also: Varvarezos opposite-sign exclusion (L-space knot): r*s<0 impossible.
Also: IIS Cor 1.6: |(n+n')/m| < 1 for any chiral pair.
O(K) = |num/(4 v3)| = 12066/323 ~ 37.36; Thm 1.10(i-c) needs O(K) <= 52/3
and therefore does NOT fire -- the exclusion rests on the Diophantine +
Varvarezos route, not on (i-c). (An earlier draft stated this backwards;
AUDIT REPAIR corrected it.)
"""
from fractions import Fraction as F

a2, a4 = 52, 681
v3 = F(323, 4)
C0 = F(7*a2*a2 - a2 - 10*a4, 8*v3)
print("C0 = m/(n+n') =", C0, "=", float(C0))
O = abs(F(7*a2*a2 - a2 - 10*a4, 1) / (4*v3))
print("O(K) =", O, "=", float(O))

# In lowest terms C0 = 6033/323; 323 = 17*19 prime factors.
# m/(n+n') = 6033/323 with |m|<=30: since gcd(6033,323)=1 (check), m must be
# multiple of 6033 -> no solutions with 0<|m|<=30 except possibly n+n'=0 case.
import math
print("gcd(6033,323) =", math.gcd(6033, 323))
print("323 factors: 17*19 =", 17*19)
print("6033/17 =", 6033/17, " 6033/19 =", 6033/19)

# Enumerate: for each m in 1..30, each n,n' with r!=s, check equation.
sols = []
for m in range(1, 31):
    for n in range(-30, 31):
        for np in range(-30, 31):
            if n == 0 or np == 0:
                continue
            if n == np:
                continue  # r==s excluded (need r!=s); same (m,n)=(m,n') identical slope
            if n + np == 0:
                continue  # 00-type handled separately
            if F(m, n + np) == C0:
                sols.append((m, n, np))
print("solutions with 1<=m<=30, |n|,|n'|<=30, n!=n':", sols)

# n+n' = 0 case: Thm 1.3 does not apply (00-type); for L-space non-amphicheiral knot,
# 00-type impossible by v3!=0 (IIS Thm 1.1: 00-type => v3=v5=0; here v3=323/4 != 0).
print("v3 =", v3, "!= 0 -> 00-type (n+n'=0) excluded by IIS Thm 1.1.")
# Also 00-type => amphicheiral by Conj; t12533 asymmetric -> excluded anyway.

# Same-sign restriction: Varvarezos Thm 1.8 kills opposite-sign for L-space knots.
# So remaining candidates must have n,n' same sign (m>0). Our sols list is empty regardless.

# Cor 1.6 check: |(n+n')/m|<1 necessary. With C0: (n+n')/m = 323/6033 ~ 0.0535 <1 OK consistent.
print("(n+n')/m = 323/6033 =", float(F(323, 6033)), "< 1 OK (necessary condition satisfiable)")

# O(K) thresholds (Thm 1.10): O(K) = 12066/323 ~ 37.36.
# (i-c) requires O(K) <= |8 a2|/d(K) = 52/3 ~ 17.33: FALSE, so (i-c) does NOT
# fire and contributes nothing. The exclusion rests on the Thm 1.3 Diophantine
# (no in-scope solutions, shown above) + Varvarezos (opposite-sign) + v3 (00-type).
d = 24
print("(i-c): |8 a2|/d =", F(8*a2, d), "=", float(F(8*a2, d)), "; O(K) =", float(O))
print("O(K) <= |8a2|/d ?", O <= F(8*a2, d), "-> (i-c) does NOT fire; no exclusion from it.")

# (ii): v3!=0 and max(nu,nu-mirror)=0? max=12 !=0 -> no.
# (iii): v3=0? No.
print()
print("=== CONCLUSION (AUDIT-REPAIRED) ===")
print("Same-sign: IIS Thm 1.3 forces m/(n+n') = C0 = 6033/323; gcd=1 so 6033|m;")
print("  no solutions with 0<|m|<=30 (enumerated above: []).")
print("Opposite-sign: Varvarezos Thm 1.8 (nontrivial L-space knot).")
print("00-type: v3=323/4 != 0 (IIS Thm 1.1).")
print("Thm 1.10(i-c) does NOT fire (O(K)=12066/323 > 52/3) and is not used.")
print("No Floer d-sum is claimed. Walker equation not asserted.")
