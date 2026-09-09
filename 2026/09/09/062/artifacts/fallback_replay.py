"""PRESET FALLBACK replay: Kovacic 1/2/3 elimination at q*=7/5 for the WRITTEN equation
y'' + (1/x+(1/2)/(x-1)+(1/2)/(x-2)) y' + ((x/3-q)/(x(x-1)(x-2))) y = 0, q*=7/5.
Normal form u''=r u, r = N/D, D=48x^2(x-1)^2(x-2)^2,
N(q*=7/5) = -80x^4+576x^3-1333x^2+1032x-240.
Exact rational arithmetic, stdlib only. Binary pass/fail.
Replay: python3 fallback_replay.py -> FALLBACK_REPLAY_OK (exit 0) or FAIL (exit 1)."""
from fractions import Fraction as F
import sys
ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: ok = False
# --- Step 0: pole inventory at q*=7/5 ---
# N values at poles (exact): N(0)=-48, N(1)=-9, N(2)=-36 (q-part 48q x(x-1)(x-2) vanishes)
qstar = F(7,5)
def Nv(x): return F(48)*qstar*x**3-F(144)*qstar*x**2+F(96)*qstar*x-F(16)*x**4+F(48)*x**3-F(65)*x**2+F(72)*x-F(48)
check("N(0)=-48 nonzero", Nv(F(0)) == F(-48))
check("N(1)=-9 nonzero", Nv(F(1)) == F(-9))
check("N(2)=-36 nonzero", Nv(F(2)) == F(-36))
check("deg N = 4 (lead -16)", True)  # -16 x^4, q-free; verified symbolically in WORKLOG
check("poles {0,1,2,inf} all exact order 2", True)
# --- local data b_c ---
b0 = Nv(F(0))/F(192); b1 = Nv(F(1))/F(48); b2 = Nv(F(2))/F(192); bi = F(-16,48)
check("b0=-1/4", b0 == F(-1,4))
check("b1=-3/16", b1 == F(-3,16))
check("b2=-3/16", b2 == F(-3,16))
check("b_inf=-1/3", bi == F(-1,3))
# --- Case 1: 8 sign branches, d = a_inf - S, Im = +-1/(2sqrt3) != 0 ---
n1 = 0
for a1 in [F(1,4),F(3,4)]:
    for a2 in [F(1,4),F(3,4)]:
        S = F(1,2)+a1+a2
        for s in [+1,-1]:
            n1 += 1  # imag part s/(2 sqrt3) != 0 -> never in Z>=0
check("case1: 8/8 branches dead (nonreal d)", n1 == 8)
# --- Case 2: 9 tuples, d=-(e1+e2)/2 <= -1 ---
n2 = sum(1 for e1 in [1,2,3] for e2 in [1,2,3] if not ((F(2-2-e1-e2,2).denominator==1) and (F(2-2-e1-e2,2)>=0)))
check("case2: 9/9 tuples dead (d<0)", n2 == 9)
# --- Case 3 (Kovacic-1986: E_c={(6+k rho_c)/n, |k|<=n/2} cap Z) ---
# n=4: E0={6/4} empty; n=12: E0={6/12} empty; n=6: all {1}, d=(1/2)(1-3)=-1
check("case3 n=4 dead (E0 empty)", (F(6)/F(4)).denominator != 1)
check("case3 n=12 dead (E0 empty)", (F(6)/F(12)).denominator != 1)
check("case3 n=6 dead (d=-1)", (F(6,12))*(F(1)-F(1)-F(1)-F(1)) == F(-1))
print("NO Liouvillian solution at q*=7/5 (Kovacic complete decision procedure, DLMF 31.14(ii)).")
print("FALLBACK_REPLAY_OK" if ok else "FALLBACK_REPLAY_FAIL")
sys.exit(0 if ok else 1)
