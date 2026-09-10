"""Rigorous interval certificate for PRESET FALLBACK (lane-552).
BL data: bare masses (1, 0.01), punctures z=+/-1.5 (d=3), mADM=1.01.
Claim: S_{r=10} has min theta+ >= 0.10 and mH in [0.96,1.06].
Method: axisymmetry -> 1D in c=cos t. q1=102.25-30c, q2=102.25+30c (exact rationals).
psi=1+1/(2r1)+0.01/(2r2); dpsi/dr=-[(10-1.5c)/(2r1^3)+0.01(10+1.5c)/(2r2^3)];
H=psi^-2/5+4 psi^-3 dpsi/dr (=theta+ outward, time-symmetric).
Panels in c with Fraction interval arithmetic + rigorous sqrt enclosure:
 - min H over panels (lower ends) -> global min bound.
 - J1=int psi^4 dc, J2=int H^2 psi^4 dc -> A=2pi R^2 J1, I=2pi R^2 J2 -> mH.
Area cap: MOTS has mH=sqrt(A/16pi) <= mH(S) by Geroch/Huisken-Ilmanen monotonicity.
"""
import sys; sys.path.insert(0,'output/artifacts')
from fractions import Fraction as F
from interval import sqrt_bounds, addi, subi, muli, divi

R2 = (F(409,4), F(409,4))   # R^2+9/4 = 102.25
K  = (F(30), F(30))          # 3R
ONE = (F(1), F(1)); M2 = (F(1,100), F(1,100))
HALF=(F(1,2),F(1,2)); FOUR=(F(4),F(4)); INV5=(F(1,5),F(1,5))
def q12(c):
    t = muli(K, c)
    return subi(R2, t), addi(R2, t)
def eval_panel(c):
    q1, q2 = q12(c)
    r1 = sqrt_bounds(q1[0], q1[1]); r2 = sqrt_bounds(q2[0], q2[1])
    r1i=(r1[0],r1[1]); r2i=(r2[0],r2[1])
    psi = addi(ONE, addi(divi(ONE, addi(r1i,r1i)), divi(M2, addi(r2i,r2i))))
    u1 = subi((F(10),F(10)), muli((F(3,2),F(3,2)), c))
    u2 = addi((F(10),F(10)), muli((F(3,2),F(3,2)), c))
    r13 = muli((q1[0],q1[1]), r1i); r23 = muli((q2[0],q2[1]), r2i)
    S = addi(divi(u1, r13), muli(M2, divi(u2, r23)))
    dpsi = (-S[1]/2, -S[0]/2)
    psi2 = muli(psi,psi); psi3 = muli(psi2,psi); psi4 = muli(psi2,psi2)
    H = addi(divi(INV5, psi2), muli(FOUR, divi((dpsi[0],dpsi[1]), psi3)))
    return psi, dpsi, H, psi4

# point check vs anchor.py (H(0)=0.1548, H(pi/2)=0.1645, H(pi)=0.1699)
for c in [F(1), F(0), F(-1)]:
    psi,d,H,p4 = eval_panel((c,c))
    print("c=%s H in [%s,%s]" % (c, float(H[0]), float(H[1])))

N = 400
h = F(2, N)
Hlo_global = None; J1lo=J1hi=F(0); J2lo=J2hi=F(0)
for k in range(N):
    c = (F(-1)+k*h, F(-1)+(k+1)*h)
    psi,d,H,p4 = eval_panel(c)
    H2 = muli(H,H)
    g1 = p4; g2 = muli(H2,p4)
    if Hlo_global is None or H[0] < Hlo_global: Hlo_global = H[0]
    J1lo += h*g1[0]; J1hi += h*g1[1]
    J2lo += h*g2[0]; J2hi += h*g2[1]
print("panels:",N)
print("min H lower bound:", float(Hlo_global))
print("J1 in [%s,%s]" % (float(J1lo),float(J1hi)))
print("J2 in [%s,%s]" % (float(J2lo),float(J2hi)))
PI=(F(3141592653589793,10**15), F(3141592653589794,10**15))
A = muli(muli(muli((F(2),F(2)), PI), (F(100),F(100))), (J1lo,J1hi))
I = muli(muli(muli((F(2),F(2)), PI), (F(100),F(100))), (J2lo,J2hi))
S16 = muli((F(16),F(16)), PI)
AoS = divi(A, S16); IoS = divi(I, S16)
rA = sqrt_bounds(AoS[0], AoS[1])
mH = muli(rA, subi(ONE, IoS))
print("A in [%s,%s]" % (float(A[0]),float(A[1])))
print("I/16pi in [%s,%s]" % (float(IoS[0]),float(IoS[1])))
print("mH in [%s,%s]" % (float(mH[0]),float(mH[1])))
print("PASS_a:", Hlo_global >= F(1,10))
print("PASS_b:", mH[0] >= F(96,100) and mH[1] <= F(106,100))
cap = 16*float(PI[1])*(float(mH[1])**2)
print("area cap 16 pi (1.06)^2 =", 16*float(PI[1])*(1.06**2), " certified <=", cap)
