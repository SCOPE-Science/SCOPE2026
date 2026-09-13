"""Full 8-member ring-1 certificate (fixed u=(1,0)): for each n in ring1, certify
sup_{a in [0,1/4]} Re[A_n(a)] <= -0.0075 (hence |A_n| >= 0.0075, I(a) >= 5.6e-5).

Same engine as interval_proof.py (Taylor J=3 + exact Stokes triangle FT), with
per-member exact k* and beta. Frozen members (beta=0): A constant, one interval.
Imag parts: certified enclosed (printed) but only Re sup is needed for |A| bound.
Saves certify_ring1_results.json with per-member sup bounds.
Run: python3 certify_ring1.py
"""
import sys, json
from mpmath import iv, mp, mpf
mp.dps = 40
from math import comb, factorial as f_
import math as _m

S2 = iv.sqrt(2)
R = 1/iv.sqrt(2-S2)
s2h = S2/2
VOL = 2*S2*(R**2)

V = []
for m in range(8):
    ang = iv.pi/8 + m*iv.pi/4
    V.append((R*iv.cos(ang), R*iv.sin(ang)))

def Kint(w):
    wb = max(abs(float(w.a)), abs(float(w.b)))
    if wb < 0.5:
        ii = iv.mpc(0, 1)
        tot = iv.mpf('0'); term = iv.mpf('1')
        for n_ in range(14):
            tot += term/iv.mpf(str(f_(n_+1)))
            term = term*(ii*w)
        rem = (wb**14)/_m.factorial(15)*_m.e**wb
        return tot + iv.mpf([-1,1])*rem
    return (iv.exp(iv.mpc(0,1)*w)-1)/(iv.mpc(0,1)*w)

def FT_triangle(Qx, Qy, ax, ay, bx, by):
    ii = iv.mpc(0,1)
    det = abs(ax*by - ay*bx)
    A = 2*iv.pi*(Qx*ax + Qy*ay)
    B = 2*iv.pi*(Qx*bx + Qy*by)
    Bb = max(abs(float(B.a)), abs(float(B.b)))
    Ab = max(abs(float(A.a)), abs(float(A.b)))
    if Bb < 0.5 and Ab < 0.5:
        tot = iv.mpf('0')
        for m_ in range(16):
            for n_ in range(16):
                tot += ((ii*B)**m_)*((ii*A)**n_)/iv.mpf(str(f_(n_)*f_(n_+m_+2)))
        tail = ((_m.e**Bb)*(_m.e**Ab))*(Bb**16+Ab**16)*4
        return det*(tot + iv.mpf([-1,1])*tail)
    if Bb < 0.5:
        A, B = B, A
    eB = iv.exp(ii*B)
    return det*(eB*Kint(A-B)/(ii*B) - Kint(A)/(ii*B))

def F0(Qx, Qy):
    tot = iv.mpf('0')
    for m in range(8):
        (ax, ay), (bx, by) = V[m], V[(m+1) % 8]
        tot += FT_triangle(Qx, Qy, ax, ay, bx, by)
    return tot

from fractions import Fraction
def sinpow_coeffs(j):
    c = {}
    for r in range(j+1):
        p = j - 2*r
        c[p] = c.get(p, Fraction(0)) + Fraction(((-1)**r)*comb(j, r), 2**j)
    return c
COEFFS = {0: {0: Fraction(1)}, 1: sinpow_coeffs(1), 2: sinpow_coeffs(2), 3: sinpow_coeffs(3)}

def Mj(j, kSx, kSy):
    C = COEFFS[j]
    tot = iv.mpf('0')
    for p, cp in C.items():
        for q, cq in C.items():
            coeff = float(cp*cq)
            tot += iv.mpf(str(coeff))*F0(kSx + iv.mpf(str(p)), kSy + iv.mpf(str(q)))
    return tot

RING1 = [(3,-2,0,2),(-3,2,0,-2),(0,2,-3,2),(0,-2,3,-2),
         (2,-3,2,0),(-2,3,-2,0),(2,0,-2,3),(-2,0,2,-3)]

def kp_beta_ks(nvec):
    n1,n2,n3,n4 = (iv.mpf(str(v)) for v in nvec)
    # rows: v1=(1/2,0), v2=(s/2,s/2), v3=(0,1/2), v4=(-s/2,s/2); dual-internal rows half of e*:
    # v1*=(1/2,0), v2*=(-s/2,s/2), v3*=(0,-1/2), v4*=(s/2,s/2)
    kx = n1/2 + n2*(s2h/2) + n4*(-s2h/2)
    ky = n2*(s2h/2) + n3/2 + n4*(s2h/2)
    ksx = n1/2 + n2*(-s2h/2) + n4*(s2h/2)
    ksy = n2*(s2h/2) + n3*(-iv.mpf('0.5')) + n4*(s2h/2)
    return kx, ksx, ksy

def num(x):
    """Robust upper float of an iv endpoint (mpf or degenerate mpi)."""
    try:
        return float(x)
    except ValueError:
        return float(x.a)

results = {}
allpass = True
for nvec in RING1:
    kx, kSx, kSy = kp_beta_ks(nvec)
    beta = kx  # u=(1,0)
    betamax = max(abs(float(beta.a)), abs(float(beta.b)))
    frozen = betamax == 0.0
    M = {j: Mj(j, kSx, kSy) for j in range(4)}
    C_ = 2*_m.pi*betamax*0.25
    rem3 = float(VOL.b)*C_**4/_m.factorial(4)*1.05
    agrid = [0.0] if frozen else [i*0.025 for i in range(11)]
    worst = -1e9
    detail = []
    ii = iv.mpc(0, 1)
    rng = [(0.0, 0.0)] if frozen else [(agrid[i], agrid[i+1]) for i in range(len(agrid)-1)]
    for (alo, ahi) in rng:
        amid = iv.mpf(str((alo+ahi)/2)); hw = iv.mpf(str((ahi-alo)/2))
        Qm = iv.mpf('0'); Lp = iv.mpf('0')
        for j in range(4):
            cj = (2*iv.pi*ii*beta)**j/iv.mpf(str(f_(j)))*M[j]
            Qm += cj*(amid**j)
            if j >= 1:
                Lp += abs(cj)*j*(iv.mpf(str(ahi))**(j-1))
        ReQ = iv.re(Qm)
        ub = ReQ.b + (Lp*hw).b + rem3
        ubf = num(ub)
        worst = max(worst, ubf)
        detail.append([alo, ahi, num(ReQ.a), num(ReQ.b), num((Lp*hw).b), ubf])
    status = "PASS" if worst < -0.0075 else "FAIL"
    if worst >= -0.0075: allpass = False
    results[str(nvec)] = {"supRe": worst, "rem3": rem3,
                          "M0re": [num(iv.re(M[0]).a), num(iv.re(M[0]).b)],
                          "status": status, "detail": detail}
    print(f"n={nvec}: beta in [{num(beta.a):+.6f},{num(beta.b):+.6f}] "
          f"M0~[{num(iv.re(M[0]).a):+.6f},{num(iv.re(M[0]).b):+.6f}] rem3={rem3:.2e} supRe={worst:.6f} [{status}]"
          + (" (frozen)" if frozen else ""))
    # imag sanity: print Im box at a=0.25
    Qe = sum((2*iv.pi*ii*beta)**j/iv.mpf(str(f_(j)))*M[j]*(iv.mpf('0.25')**j) for j in range(4))
    print(f"    A(0.25) in Re[{num(iv.re(Qe).a):+.6f},{num(iv.re(Qe).b):+.6f}] "
          f"Im[{num(iv.im(Qe).a):+.6f},{num(iv.im(Qe).b):+.6f}] (+-R {rem3:.1e})")

with open("certify_ring1_results.json", "w") as fh:
    json.dump(results, fh, indent=1)
print("ALL PASS" if allpass else "SOME FAILED")
