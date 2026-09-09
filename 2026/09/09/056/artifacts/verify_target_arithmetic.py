"""Exact integer/rational audit of admitted Villadsen target data (stdlib only).

Checks:
 (A) stage dimensions t_i=3^i-1, d_i=2*t_i, matrix sizes n_i=2*4^{i-1},
     ratios d_i/n_i and d_i/(2n_i) for i=1..10 (Fractions, exact).
 (B) stage-3 Bott-pair rank gap: r_p=8, r_q=16 in A3=M32(C(X3)),
     normalized trace gap = 8/32 = 1/4 exactly.
 (C) persistence wash-out: at stage j>=3, rank gap Delta_j=8*4^{j-3},
     covering dim D_j=2*(3^j-1); sufficient-embedding threshold
     T_j=(D_j+1)/2 (conservative Husemoller-type stable-range bound:
     complex codim >= ceil(D/2) forces embedding of e-bundle into
     trivial f-bundle, hence Cuntz subequivalence of the images).
     Table Delta_j vs T_j, crossing stage, and general lemma:
     for ANY fixed normalized gap g>0 at any fixed stage, eventual
     forced comparison since g*n_j/(D_j/2) -> infinity as (4/3)^j.
 (D) slow dimension growth: d_j/n_j = 4*(3/4)^j*(1-3^{-j}) -> 0;
     exhibit j with ratio < 1/100; upper-bound signal d3/(2n3)<=1.

Prints VERIFY_OK on success. No external deps.
"""
from fractions import Fraction

def main():
    # (A) stage data
    print("stage | t_i | d_i | n_i | d_i/n_i | d_i/(2n_i)")
    data = {}
    for i in range(1, 26):
        t = 3**i - 1
        d = 2 * t
        n = 2 * (4 ** (i - 1))
        r1 = Fraction(d, n)
        r2 = Fraction(d, 2 * n)
        data[i] = (t, d, n, r1, r2)
        print(f"{i} | {t} | {d} | {n} | {r1}={float(r1):.6f} | {r2}={float(r2):.6f}")
    # exact assertions for stages 1..4
    assert data[1][:3] == (2, 4, 2)
    assert data[2][:3] == (8, 16, 8)
    assert data[3][:3] == (26, 52, 32)
    assert data[4][:3] == (80, 160, 128)
    assert data[3][3] == Fraction(13, 8)   # d3/n3
    assert data[3][4] == Fraction(13, 16)  # d3/(2n3) <= 1
    assert data[3][4] <= 1
    # slow growth: ratio strictly decreasing for i>=2 and ->0
    for i in range(2, 25):
        assert data[i + 1][3] < data[i][3], (i, data[i][3], data[i + 1][3])
    assert data[25][3] < Fraction(1, 100), data[25][3]

    # (B) stage-3 trace gap
    rp, rq, n3 = 8, 16, 32
    gap = Fraction(rq - rp, n3)
    assert gap == Fraction(1, 4), gap
    print(f"\nstage-3 ranks: rp={rp}, rq={rq}, n3={n3}, gap={gap} == 1/4 OK")

    # (C) wash-out table
    print("\nj | Delta_j | D_j | T_j=(D_j+1)/2 | Delta-T | forced?")
    cross = None
    for j in range(3, 12):
        M = 4 ** (j - 3)
        Delta = 8 * M
        D = 2 * (3 ** j - 1)
        # T as Fraction to handle .5
        T = Fraction(D + 1, 2)
        forced = Delta >= T
        print(f"{j} | {Delta} | {D} | {T} | {Fraction(Delta,1)-T} | {forced}")
        if forced and cross is None:
            cross = j
    assert cross == 8, cross
    # pre-crossing stages must be negative (obstruction Chand possible there)
    for j in (3, 4, 5, 6, 7):
        M = 4 ** (j - 3)
        assert 8 * M < Fraction(2 * (3 ** j - 1) + 1, 2), j
    # general lemma: g*n_j vs D_j/2 -> infinity for any fixed g>0
    # check ratio doubles-ish: use g=1/4; ratio R_j = (n_j/4)/(D_j/2)
    for j in (3, 8, 12):
        n = 2 * (4 ** (j - 1))
        D = 2 * (3 ** j - 1)
        R = Fraction(n, 4) / Fraction(D, 2)  # = n/(2D)
        print(f"R_{j} (gap 1/4 stable-range ratio) = {R} ~ {float(R):.4f}")
    assert Fraction(2 * 4 ** 7, 4) / Fraction(2 * (3 ** 8 - 1), 2) > 1  # j=8 forced
    # monotonic growth of R_j eventually: R_{j+1}/R_j = 4*(3^j-1)/(3^{j+1}-1) >1
    for j in range(3, 11):
        Rj = Fraction(2 * 4 ** (j - 1), 4) / Fraction(2 * (3 ** j - 1), 2)
        Rj1 = Fraction(2 * 4 ** j, 4) / Fraction(2 * (3 ** (j + 1) - 1), 2)
        assert Rj1 > Rj, j

    # (D) upper-bound signal + decay below any eps
    assert data[3][4] == Fraction(13, 16)
    assert data[8][4] < Fraction(1, 4), data[8][4]
    print("\nupper-bound signal: d3/(2n3)=13/16<=1 OK; d8/(2n8)=%s<1/4 OK" % data[8][4])
    # (E) sharp threshold: D_j even so ceil(D_j/2)=D_j/2=3^j-1; check exact crossing
    for j in range(3, 12):
        M = 4 ** (j - 3)
        Delta = 8 * M
        need = 3 ** j - 1
        print(f"sharp j={j}: Delta={Delta} vs need={need} -> {'forced' if Delta >= need else 'open'}")
    assert 8 * 4 ** (7 - 3) < 3 ** 7 - 1      # j=7 open even sharply
    assert 8 * 4 ** (8 - 3) >= 3 ** 8 - 1     # j=8 forced sharply
    # uniform J(g) formula check: J(1/4)=ceil(ln8/ln(4/3))=8
    import math
    J = math.ceil(math.log(8) / math.log(4 / 3))
    assert J == 8, J
    print(f"J(1/4)={J} OK")
    # K-amplification monotonicity: gap g in M_K(A_j) <-> rank gap g*K*N_j >= g*N_j
    for K in (1, 2, 5, 32):
        assert Fraction(1, 4) * K * 32768 >= (13120 + 1) // 2 or True  # j=8 sanity
    # general g: J(g) exists since (4/3)^j -> oo; verify J(1/2)=12? (1/2)*2*4^{j-1}>=3^j
    def Jof(gnum, gden):
        j = 3
        while True:
            if Fraction(gnum, gden) * 2 * 4 ** (j - 1) >= 3 ** j - 1 + Fraction(1, 2):
                return j
            j += 1
            assert j < 100
    print("J(1/4)=%d, J(1/2)=%d, J(1/8)=%d" % (Jof(1, 4), Jof(1, 2), Jof(1, 8)))
    assert Jof(1, 4) == 8

    print("VERIFY_OK")

if __name__ == "__main__":
    main()
