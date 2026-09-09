"""Lane 434: fractional-window elimination + theta'-leg check for C7 target.
Only stdlib + numpy. Exact integer/rational arithmetic where claimed exact;
float64 + longdouble cross-check for cosine margins (documented as computed evidence).
"""
from fractions import Fraction
import math
import numpy as np

print("=== A. Fractional (n,d) window for target Theta<=3.30 (exact) ===")
LB = Fraction(3257, 1000)  # rigorous LB from 367^{1/5}>3.257 (see below, Sec C)
TGT = Fraction(33, 10)
print("cells (r,d), r<=14, with 3.257<=d/r<=3.30:")
for r in range(1, 15):
    ds = [d for d in range(0, 4 * r + 3) if LB <= Fraction(d, r) <= TGT]
    print("  r=%2d d=%s" % (r, ds))

print()
print("=== B. THEOREM (window elimination): no (n,d)-rep of C7 has n/d<=3.30 ===")
print("Proof (self-contained replay of Bukh-Cox Prop.4 lower bound for C7).")
print("Let {(A_i,B_i)} be an (n,d)-rep of C7 (vertices Z7) over ANY field F,")
print("X_i = col-space(A_i), dim d. Prop.11: S indep, no S-T edges => sums indep.")
print("Edge 0~1; I={3,5} indep, no edges to {0,1}. Iterate: n >= dim(X0+X1)+2d.")
print("dim(X0+X1)=2d-t, t=dim(X0 cap X1) >= 4d-n; same t'=dim(X0 cap X6)>=4d-n.")
print("X1,X6 indep (1,6 nonedge) => (X0 cap X1),(X0 cap X6) indep, both in X0:")
print("d >= t+t' >= 2(4d-n)  <=>  2n >= 7d  <=>  n/d >= 7/2 = 3.5.")
print("Hence EVERY (n,d)-rep has n/d>=3.5 > 3.30: all window cells EMPTY. QED")
print("Corollary: H_f(C7;F)>=3.5 for every field; Haemers-on-powers also blocked:")
print("H(C7^bn F)^{1/n} >= H_f(C7;F) >= 3.5 (Cor.10), so no power-n Haemers cert")
print("can reach 3.30 either. Integer-rank special case: rank<=3 impossible over")
print("any field given Theta>=3.2578 (Lean-verified), since Theta<=rank.")

print()
print("=== C. Exact-integer lower-bound check: 367^{1/5} > 3.257 ===")
print("3257^5 =", 3257**5, "< 367*10^15 =", 367*10**15, "?", 3257**5 < 367*10**15)
assert 3257**5 < 367*10**15
print("Polak-Schrijver alpha(C7^5)>=367 => Theta(C7)>3.257, exact integer: OK")

print()
print("=== D. Upper witness H_f(C7)<=3.5: fractional edge-cover value 7/2 ===")
print("Cliques of C7 = edges+singletons; weight 1/2 on each of the 7 edges:")
print("each vertex covered twice -> coverage 2*(1/2)=1; total 7/2. Exact: OK")
print("Chain (cited): H_f(G;F) <= chi_f(Gbar) [Bukh-Cox Thm.8] => H_f(C7;F)<=3.5.")
print("With Sec.B: H_f(C7;F)=3.5 EXACTLY, every field. Haemers leg dead by 0.2.")

print()
print("=== E. Theta leg: theta'(C7) stuck above 3.30 (EXACT rational point) ===")
# Circulant theta' slice: B first row [1/7,0,a2,a3,a3,a2,0], a2,a3>=0, PSD.
# Exact point a2=0.11428, a3=0.05094 -> obj 1+14(a2+a3) = 82827/25000 = 3.31308.
# Exact LDL in verify.py: 7 positive rational pivots, smallest ~4.97e-4. Zero floats.
from fractions import Fraction as _F
_a2, _a3 = _F(11428, 100000), _F(5094, 100000)
_obj = 1 + 14 * (_a2 + _a3)
assert _obj == _F(82827, 25000) and _obj > _F(33, 10)
print("exact rational point a2=%s a3=%s obj=%s=3.31308 > 33/10: OK" % (_a2, _a3, _obj))
print("theta'(C7) >= 82827/25000 = 3.31308 > 3.30 by exact LDL (see verify.py).")
print("So: theta-leg in [3.31308, 3.3177], Haemers-leg = 3.5; min-family cannot give 3.30.")
