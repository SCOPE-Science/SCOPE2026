"""Exhaustive Case-1/Case-2 branch enumeration, exact rationals + symbolic imag. stdlib only.
Replay: python3 case12_enumeration.py -> CASE12_ENUM_OK"""
from fractions import Fraction as F
print("== Case 1: all sign branches ==")
print("a0 = 1/2 (sole value, rho0=0); a1,a2 in {1/4,3/4}; a_inf = (1+s*i/sqrt3)/2, s=+-1")
n_branch = 0
for a1 in [F(1,4), F(3,4)]:
    for a2 in [F(1,4), F(3,4)]:
        S = F(1,2) + a1 + a2
        for s in [+1, -1]:
            # d = a_inf - S = (1/2 - S) + s*i/(2*sqrt3); imag != 0 always
            re = F(1,2) - S
            print(f"  a1={a1} a2={a2} s={s:+d}: Re(d)={re}, Im(d)=s/(2*sqrt3)!=0 -> NOT in Z>=0")
            n_branch += 1
print(f"{n_branch} branches, all dead. CASE 1 EXHAUSTED.")
print("== Case 2: all e-tuples ==")
print("E0={2}, E1=E2={2+k/2,k=0,+-2}={1,2,3}, Einf={2} (k=0,+-2; nonreal k!=0 terms)")
n = 0
for e1 in [1,2,3]:
    for e2 in [1,2,3]:
        d = F(2-2-e1-e2, 2)
        ok = (d.denominator == 1 and d >= 0)
        print(f"  e1={e1} e2={e2}: d={d} admissible? {ok}")
        assert not ok
        n += 1
print(f"{n} tuples, all dead. CASE 2 EXHAUSTED.")
print("CASE12_ENUM_OK")
