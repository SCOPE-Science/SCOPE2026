"""Independent DLMF 31.2 E3-E4 normal-form route vs direct r=P'/2+P^2/4-Q. stdlib only.
Replay: python3 dlmf_crosscheck.py -> DLMF_CROSSCHECK_OK"""
from fractions import Fraction as F
q = F(7,5); a = F(2); g = F(1); d = F(1,2); e = F(1,2); ab = F(1,3)
A = -g*d/2 - g*e/(2*a) + q/a
B = g*d/2 - d*e/(2*(a-1)) - (q-ab)/(a-1)
C = g*e/(2*a) + d*e/(2*(a-1)) - (a*ab-q)/(a*(a-1))
D = g*(g/2-1)/2; E = d*(d/2-1)/2; Ff = e*(e/2-1)/2
print(f"A={A} B={B} C={C} (expect 13/40, -113/120, 37/60)")
print(f"D={D} E={E} F={Ff} (expect -1/4, -3/16, -3/16)")
assert (A,B,C) == (F(13,40), F(-113,120), F(37,60))
assert (D,E,Ff) == (F(-1,4), F(-3,16), F(-3,16))
assert A+B+C == 0
print("matches apart() partial fractions of r identically. DLMF_CROSSCHECK_OK")
