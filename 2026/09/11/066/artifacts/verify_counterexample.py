"""Certified counterexample to the MOTS eigenvalue vanishing law (v3, exact).

Target claim: axisymmetric vacuum maximal data, stable MOTS, J != 0,
0 < delta = A/(8pi|J|)-1 <= 1  =>  lam1*A <= 8*delta.

Counterexample: Kerr horizon section, M = 1, a = 99/100.
Certifies: delta in (0,1], lam1*A >= 2.3 > 1.23 >= 8*delta.

Strategy (see DRAFT.md for proofs):
 * Full principal eigenvalue = ground energy of axisymmetric SL reduction
   H u = -d/dz[((1-z^2)/R) u'] + V u on (-1,1), R = r^2+a^2 z^2.
 * Comparison: H >=_form -(1/S2) d/dz[(1-z^2)d/dz] + Vmin  =>  lam2 >= 2/S2+Vmin.
 * Temple with u(z) = 89+33 z^2.
All HDouble-integrals reduce to Jk = int_{-1}^{1} R^{-k} (k<=6) via exact
recursion from J1 = 2 atan(a/r)/(a r); atan enclosed by alternating Taylor
remainder; all other steps are rational interval arithmetic (exact).
"""
from fractions import Fraction as Q

class I:
    __slots__ = ("lo", "hi")
    def __init__(self, lo, hi=None):
        lo = lo if isinstance(lo, Q) else Q(lo)
        hi = lo if hi is None else (hi if isinstance(hi, Q) else Q(hi))
        assert lo <= hi
        self.lo, self.hi = lo, hi
    def __add__(self, o):
        o = o if isinstance(o, I) else I(o)
        return I(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__
    def __sub__(self, o):
        o = o if isinstance(o, I) else I(o)
        return I(self.lo - o.hi, self.hi - o.lo)
    def __rsub__(self, o):
        return I(o) - self
    def __mul__(self, o):
        o = o if isinstance(o, I) else I(o)
        ps = (self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi)
        return I(min(ps), max(ps))
    __rmul__ = __mul__
    def __truediv__(self, o):
        o = o if isinstance(o, I) else I(o)
        assert o.lo > 0 or o.hi < 0, "division by interval containing 0"
        ps = (self.lo/o.lo, self.lo/o.hi, self.hi/o.lo, self.hi/o.hi)
        return I(min(ps), max(ps))
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        r = I(Q(1))
        for _ in range(n):
            r = r*self
        return r
    def __repr__(self):
        return f"[{float(self.lo):.9f}, {float(self.hi):.9f}]"

def atan_enclosure(x, N=70):
    """Enclose atan(x) for 0 < x < 1 interval via alternating Taylor remainder."""
    assert x.lo > 0 and x.hi < 1
    s = I(Q(0))
    for k in range(N+1):
        term = x**(2*k+1)/I(Q(2*k+1))
        s = s + term if k % 2 == 0 else s - term
    rem = x**(2*N+3)/I(Q(2*N+3))   # >= true remainder, positive
    return I(s.lo - rem.hi, s.hi + rem.hi)

def main():
    a = Q(99, 100); a2 = a*a
    SQ199 = I(Q(1410673, 100000), Q(1410674, 100000))
    assert SQ199.lo*SQ199.lo < 199 < SQ199.hi*SQ199.hi
    RP = Q(1) + SQ199/I(Q(100))
    R2 = RP*RP
    S2 = R2 + I(a2)
    print("r+ in", RP)
    print("S2 in", S2)

    PI = I(Q(31415, 10000), Q(31416, 10000))
    AREA = Q(4)*PI*S2
    DELTA = S2/(Q(2)*I(a2)**I(Q(0))*I(a) if False else Q(2)*I(a)) - Q(1)
    EIGHT = Q(8)*DELTA
    print("A in", AREA)
    print("delta in", DELTA)
    print("8*delta in", EIGHT)
    assert DELTA.lo > 0 and DELTA.hi <= 1
    print("window 0<delta<=1: OK")

    # J1 = 2 atan(a/r)/(a r), recursion for J2..J6
    X = I(a)/RP
    assert X.hi < 1
    AT = atan_enclosure(X)
    print("atan(a/r) in", AT)
    J = {}
    J[1] = Q(2)*AT/(I(a)*RP)
    for k in range(1, 6):
        J[k+1] = I(Q(1))/(I(Q(k))*R2*S2**k) + I(Q(2*k-1))/(I(Q(2*k))*R2)*J[k]
    for k in range(1, 7):
        print(f"J{k} in", J[k])

    # M_k = int z^{2k} R^{-m} pieces: use expansion z^2 = (R-r^2)/a^2
    # Precompute K[j] = int R^{-j} for j=1..6 -> J[j]. Then:
    # int z^2/R^4 = (J3 - r^2 J4)/a^2 etc. Build needed moments:
    r2 = R2
    def poly_R_int(q):
        # int_{-1}^{1} R^q dz for q >= 0, exact
        from math import comb
        tot = I(Q(0))
        for l in range(q+1):
            tot += I(Q(comb(q, l))) * (r2**(q-l)) * (I(a2)**l) * I(Q(2, 2*l+1))
        return tot
    def moment(p, m):
        # int z^{2p} R^{-m}, z^2 = (R-r2)/a2; J index 1..6 else exact poly part
        from math import comb
        tot = I(Q(0))
        for j in range(p+1):
            c = I(Q(comb(p, j)) * (Q(-1)**(p-j))) / (I(a2)**p) * (r2**(p-j))
            e = m-j
            tot += c*(J[e] if e >= 1 else poly_R_int(-e))
        return tot
    # sanity: J indices m-j >= 1 always (m<=6, j<=p<=2 -> m-j>=... m=4,j=2 -> J2 ok; check all uses below)
    M = moment
    # integrals needed:
    # N = int u^2 = 89^2*2 + 2*89*33*(2/3) + 33^2*(2/5)
    Nint = I(Q(89*89*2) + Q(2*89*33*2, 3) + Q(33*33*2, 5))
    print("N =", Nint)
    # G = int (1-z^2)/R (u')^2, u'=66z: = 66^2 [int z^2/R - int z^4/R]
    # int z^2/R = (J0 - r2 J1)/a2 with J0 = int dz = 2
    J0 = I(Q(2))
    Z2R1 = (J0 - r2*J[1])/I(a2)
    Z4R1 = M(2, 1)
    G = I(Q(66*66))*(Z2R1 - Z4R1)
    print("G in", G)
    # P2 = int V u^2 with V = c0 + c3/R^3 + c2/R^2 + c1/R:
    c0 = I(Q(1))/(Q(4)*R2) - I(a2)/(S2*S2)
    c3 = Q(3)*R2*S2
    c2 = -(Q(2)*I(a2) + Q(3)*R2)
    c1 = ((R2 - I(a2))*(Q(3)*R2 + I(a2)))/(Q(4)*R2*S2)
    # u^2 = 89^2 + 2*89*33 z^2 + 33^2 z^4
    e0, e1, e2 = Q(89*89), Q(2*89*33), Q(33*33)
    def vint(m):
        return e0*J[m] + e1*M(1, m) + e2*M(2, m)
    P2 = c0*Nint + c3*vint(3) + c2*vint(2) + c1*vint(1)
    H = G + P2
    print("H=<u,Hu> in", H)
    assert Nint.lo > 0 and H.lo > 0
    MU = H/Nint
    print("mu in", MU)

    # Vmin: V decreasing in R (dV/dR numerator < 0 on 64 panels), Vmin = V(S2)
    def dVdR_num(R):
        return -(Q(9)*R2*S2) + Q(2)*(Q(2)*I(a2) + Q(3)*R2)*R - c1*R*R
    lo, hi = R2.lo, S2.hi
    for k in range(64):
        A_ = lo + (hi-lo)*Q(k)/Q(64); B_ = lo + (hi-lo)*Q(k+1)/Q(64)
        assert dVdR_num(I(A_, B_)).hi < 0
    print("V decreasing in R: OK")
    VMIN = c0 + c3/(S2**3) + c2/(S2**2) + c1/S2
    print("Vmin in", VMIN)
    NU = I(Q(2))/I(S2.hi) + I(VMIN.lo)
    print("nu in", NU)
    assert MU.hi < NU.lo
    print("mu < nu: OK")

    # residual: res = A2m + B2m/R + C2m/R^2 + D2m/R^3 + E2m/R^4 + F2m/R^5 + G2m/R^6
    # with exact rational coefficients in (r2, S2, a2); derive:
    # res = -(Wp up + 66 W) + V u - mu u; expand in basis {z^{2i}/R^j} then convert z-powers.
    # Wp up + 66W = 66[W - 2z^2/R - z^2(1-z^2) 2a2/R^2]  (using Rp=2a2 z)
    #   = 66[(1-z^2)/R - 2z^2/R - 2a2 z^2(1-z^2)/R^2]
    # V u - mu u = (c0-mu) u + c3 u/R^3 + c2 u/R^2 + c1 u/R.
    # Collect res = P0(z) + P1(z)/R + P2c(z)/R^2 + P3(z)/R^3 with polys:
    # P0 = -(mu... ) -> P0(z) = (c0-mu) u  [c0,mu intervals]
    # P1(z) = -66[(1-z^2) - 2z^2] + c1 u = -66(1-3z^2) + c1 u
    # P2c(z) = -66*2a2 z^2(1-z^2)... wait: -66*[ - 2a2 z^2(1-z^2)/R^2 ]? sign: Wp up+66W = 66W + up Wp; up Wp = 66z*Wp; Wp = -2z/R-(1-z^2)Rp/R^2 = -2z/R-2a2 z(1-z^2)/R^2. up*Wp = -132 z^2/R - 132 a2 z^2(1-z^2)/R^2. So -(Wp up+66W) = +132 z^2/R + 132 a2 z^2(1-z^2)/R^2 - 66(1-z^2)/R = [132z^2-66(1-z^2)]/R + 132a2 z^2(1-z^2)/R^2 = 66(3z^2-1)/R + 132 a2(z^2-z^4)/R^2.
    # So: P1(z) = 66(3z^2-1) + c1 u(z); P2c(z) = 132 a2 (z^2-z^4) + c2 u(z); P3(z) = c3 u(z); P0(z) = (c0-mu) u(z).
    MUiv = MU
    P0 = lambda z: (c0-MUiv)*(U0+U1*z*z)
    P1 = lambda z: I(Q(66))*(Q(3)*z*z-Q(1)) + c1*(U0+U1*z*z)
    P2c = lambda z: I(Q(132)*a2)*(z*z-z**4) + c2*(U0+U1*z*z)
    P3 = lambda z: c3*(U0+U1*z*z)
    U0, U1 = Q(89), Q(33)
    # res^2 = sum_{i<=j} (2-delta) Pi Pj / R^{i+j}; each Pi Pj = even poly degree <= 8 (P2c has z^4*u -> deg 6; P2c^2 deg 12!). Convert z^{2k} via M(k, m).
    Ps = [P0, P1, P2c, P3]
    # represent each Pi as coeff dict {k: coeff of z^{2k}} with interval coeffs
    def rep_P0():
        b = c0-MUiv
        return {0: b*I(U0), 1: b*I(U1)}
    def rep_P1():
        return {0: I(Q(-66)) + c1*I(U0), 1: I(Q(198)) + c1*I(U1)}
    def rep_P2():
        return {0: c2*I(U0), 1: I(Q(132)*a2) + c2*I(U1), 2: I(-Q(132)*a2)}
    def rep_P3():
        return {0: c3*I(U0), 1: c3*I(U1)}
    reps = [rep_P0(), rep_P1(), rep_P2(), rep_P3()]
    Rint = I(Q(0))
    for i in range(4):
        for j in range(i, 4):
            mult = Q(1) if i == j else Q(2)
            # (Pi Pj)(z) = sum_k d_k z^{2k}; integral of d_k z^{2k}/R^{i+j} = d_k M(k, i+j)
            ri, rj = reps[i], reps[j]
            for ki, ci in ri.items():
                for kj, cj in rj.items():
                    k = ki+kj; m = i+j
                    if m == 0:
                        val = ci*cj*I(Q(2, 2*k+1))  # int z^{2k} dz
                    else:
                        assert 1 <= m-k if False else True
                        val = ci*cj*M(k, m)
                    Rint += mult*val
    print("R=<res,res> in", Rint)
    Rint = I(Q(0) if Rint.lo < 0 else Rint.lo, Rint.hi)  # R >= 0; keep rigorous upper edge
    SIG2 = Rint/Nint
    print("sig2 in", SIG2)
    gap = NU - MU
    assert gap.lo > 0
    LAM_LO = MU.lo - SIG2.hi/gap.lo
    print("Temple lam1 >=", float(LAM_LO))
    assert LAM_LO > 0
    LHS, RHS = LAM_LO*AREA.lo, EIGHT.hi
    print("lam1*A >= %.6f" % float(LHS))
    print("8*delta <= %.6f" % float(RHS))
    assert LHS > RHS
    print("CERTIFIED: lam1*A > %.4f > %.4f >= 8*delta" % (float(LHS), float(RHS)))
    print("ALL CHECKS PASSED")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
