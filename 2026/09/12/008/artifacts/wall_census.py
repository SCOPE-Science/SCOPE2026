"""Exact rational wall census for the conic-ideal projection class on a GM threefold.

Setup: X ordinary GM threefold, H^3 = 10, H^2 = 10 L, H.L = 1.
Truncated Chern vector convention: (r, c, d, e) = ch0=r, ch1=c*H,
ch2=d*L, ch3=e*P. Todd: td = 1 + H/2 + (17/6) L + 1 P.
chi(A,B) = int_X( ch(A)^vee * ch(B) * td ).
Tilt data at beta=0: Im = 10*c, Re = 5*a^2*r - d, mu = -Re/Im.
"""
from fractions import Fraction as F

def mul(a, b):
    r1, c1, d1, e1 = a
    r2, c2, d2, e2 = b
    return (r1*r2, r1*c2 + c1*r2,
            r1*d2 + r2*d1 + 10*c1*c2,
            r1*e2 + r2*e1 + c1*d2 + c2*d1)

def chi(a, b):
    r1, c1, d1, e1 = a
    av = (r1, -c1, d1, -e1)
    rp, cp, dp, ep = mul(av, b)
    return rp*1 + cp*F(17, 6) + dp*F(1, 2) + ep

def Delta(a):
    r, c, d, e = a
    return (10*c)**2 - 20*r*d

O = (1, 0, 0, 0)
E = (2, -1, 1, F(1, 3))        # U_X, exceptional bundle
Edual = (2, 1, 1, F(-1, 3))    # U_X^vee
IC = (1, 0, -2, 0)             # ideal of smooth conic
G = (-1, 1, -3, F(-1, 3))      # [I_C] - [E] = -b1 + b2

print("chi(O,IC) =", chi(O, IC), "| chi(E,IC) =", chi(E, IC))
print("[G] = IC - E =", (G[0], G[1], G[2], G[3]))
print("chi(G,G) =", chi(G, G), " Delta(G) =", Delta(G))
print("Im(G) =", 10*G[1], " Re(G)(a) = 5 a^2 r - d =", -5, "*a^2 +3")
print("chi(Edual,G) =", chi(Edual, G))
print()
print("Rank-two cF=1 subobject walls: slope equality <=> Re(Q)=0,",
      "Q = G - F, rQ=-3, dQ=-3-dF => a^2 = (dF+3)/15")
for dF in range(-3, 3):
    a2 = F(dF + 3, 15)
    D = 100 - 40*dF
    print(f"dF={dF:+d}  a^2={a2} (~{float(a2)**0.5:.4f})  "
          f"Delta(F)={D}  BG-ok={D >= 0}")
print()
print("Im-gap: subobject F of G in Coh^0 has Im(F)=10*cF; no integer",
      "cF gives 0 < Im(F) < Im(G)=10. Destabilizers need cF=1 or Im=0.")
print("CONCLUSION: six BG-admissible integer walls incl. dF=1,2 ABOVE a=1/2;",
      "formal emptiness above 1/2 is false; Li bound / Hom checks required.")
