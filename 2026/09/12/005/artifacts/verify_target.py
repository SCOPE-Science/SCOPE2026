"""Verify GM line-ideal projection class and beta=-1/2 tilt-wall exclusion.

Ordinary GM threefold X: H^3=10, Pic=Z*H, -K_X=H, H.c2=24.
Line L: H.L=1, chi(O_L)=1. ch(E)=(2,-H,L,1/3P) for g=6.
Checks:
 1. chi(O,I_L)=0, chi(E,I_L)=2 via HRR -> [pr(I_L)]_{<=2}=(-3,2H,-3L).
 2. Primitivity, Delta(M)=220, (-2)-class in N(Ku).
 3. beta=-1/2 Im quantization: Im(E)=10n1+5n0 in 5Z; total=5 -> no
    decomposition into two positive-Im factors -> no numerical wall,
    no strictly semistable object. Brute-force corroboration + BG bounds.
 4. Line/conic separation: conic lift (-1,1,-2) vs line (-3,2,-3).
"""
from fractions import Fraction as Q

H3 = 10
HL = 1  # H.L

def chi_E_IL():
    # ch(E^vee)=(2,H,L,-1/3P), ch(I_L)=(1,0,-L,-1/2P)
    # td1=H/2, td2=17/6 L (since (H^2+c2)/12=(10L+24L)/12), td3=P
    # P3 = A0B3 + (A1.B2) + (A2.B1) + A3B0 with A1.B2 = H.(-L) = -1 pt
    P3 = Q(-1) + Q(-1) + Q(0) + Q(-1, 3)  # 2*(-1/2) + H.(-L) + L.0 + (-1/3)*1
    assert P3 == Q(-7, 3), P3
    # P2=A0B2+A1B1+A2B0 = 2(-L)+0+L = -L ; P2.td1 = -L.H/2 = -1/2
    p2t1 = Q(-1, 2)
    # P1 = H ; P1.td2 = H.(17/6 L) = 17/6
    p1t2 = Q(17, 6)
    # P0.td3 = 2*1 = 2
    chi = P3 + p2t1 + p1t2 + Q(2)
    return chi

chi = chi_E_IL()
print("chi(E,I_L) =", chi)
assert chi == 2
chi_O = 1 - 1  # chi(O_X)-chi(O_L)
print("chi(O,I_L) =", chi_O)
assert chi_O == 0

# Projected truncated class: [I_L] - 2[E] - 0[O]
m0, m1, m2 = 1 - 2*2, 0 - 2*(-1), -1 - 2*1
print("projected (m0,m1,m2) =", (m0, m1, m2))
assert (m0, m1, m2) == (-3, 2, -3)

import math
print("primitive gcd(|-3|,|2|) =", math.gcd(3, 2))
assert math.gcd(3, 2) == 1

DeltaM = (H3*m1)**2 - 2*(H3*m0)*m2
print("Delta(M) =", DeltaM)
assert DeltaM == 220

# Euler pairing check: M_Euler Gram for g=6: [[-2,-3],[-3,-5]], u=-3v+2w
a, b = -3, 2
G = [[-2, -3], [-3, -5]]
Av = G[0][0]*a + G[0][1]*b
Bv = G[1][0]*a + G[1][1]*b
print("chi(u,u) =", a*Av + b*Bv)
assert a*Av + b*Bv == -2

BETA = Q(-1, 2)
def Im(n0, n1):
    return H3*n1 - BETA*H3*n0  # =10n1+5n0
print("Im(M) =", Im(m0, m1))
assert Im(m0, m1) == 5

# Brute force: search subobject Chern vectors in a wide box for a numerical
# wall at beta=-1/2 with both factors in Coh^beta (Im>0), BG on both,
# Delta<=Delta(M), and slope equality with alpha^2>0.
sols = []
R = 30
for n0 in range(-R, R+1):
    for n1 in range(-R, R+1):
        ie = Im(n0, n1)
        iff = Im(m0, m1) - ie
        if not (ie > 0 and iff > 0):
            continue
        for n2 in range(-R, R+1):
            f0, f1, f2 = m0-n0, m1-n1, m2-n2
            dE = (H3*n1)**2 - 2*(H3*n0)*n2
            dF = (H3*f1)**2 - 2*(H3*f0)*f2
            if dE < 0 or dF < 0 or dE > DeltaM or dF > DeltaM:
                continue
            sols.append((n0, n1, n2))
print("both-Im-positive BG-compatible candidates in box:", sols)
assert sols == []

# Show the wall equation would force the excluded case: with 2n1+n0=1,
# alpha^2 = (n2+5n1+5n0/4-13/4)/(5(n0+3)); record a few formal values to
# log the numerical wall W2 shape (all have quotient Im 0 -> not walls).
print("formal W2 samples (n0=2k+1,n1=-k; quotient Im=0, hence no wall):")
for k in [-1, 0, 1, 2]:
    n0, n1 = 2*k+1, -k
    for n2 in [-3, 0, 5]:
        num = Q(n2) + 5*n1 + Q(5*n0, 4) - Q(13, 4)
        den = 5*(n0+3)
        print(f"  k={k} (n0,n1,n2)={(n0,n1,n2)} formal alpha^2={num}/{den}={num/den}")

# Conic separation: [pr(I_C)] = -v+w -> (m0,m1,m2)=(-1,1,-2), (-1)-class
c0, c1, c2 = -1, 1, -2
print("conic Im =", Im(c0, c1), " Delta(conic) =", (H3*c1)**2-2*(H3*c0)*c2)
assert (c0, c1, c2) != (m0, m1, m2)
av, bv = -1, 1
print("conic chi =", av*(G[0][0]*av+G[0][1]*bv)+bv*(G[1][0]*av+G[1][1]*bv))
print("VERIFY_OK")
