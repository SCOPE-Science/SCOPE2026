"""Inductive-system audit + upper-bound chain (exact integer arithmetic).

The admitted target data: A_j = M_{N_j}(C(X_j)), X_j = (S^2)^{t_j},
phi_j: A_j -> A_{j+1} diagonal with total multiplicity 4 =
3 coordinate-projection eigenvalue maps + 1 point evaluation.

Certifies (stdlib only):
 (1) Recursion closure: t_{j+1} = 3 t_j + 2 with t_1 = 2 gives t_j = 3^j - 1
     (closed form verified j=1..12); hence D_j = 2 t_j = 2(3^j - 1).
 (2) Covering-dimension product rule used: dim((S^2)^t) = 2t (finite CW
     product; each S^2 dim 2). Recorded as cited topology; arithmetic
     consequence D_j tabulated exactly.
 (3) Matrix-size recursion N_{j+1} = 4 N_j, N_1 = 2 -> N_j = 2*4^{j-1}
     verified j=1..12.
 (4) Multiplicity split: 3 coordinate + 1 point-eval = 4 total; coordinate
     fraction 3/4, point fraction 1/4. Point-eval count per step = 1 > 0,
     consistent with generic-density simplicity hypothesis (flagged).
 (5) Homogeneous upper-bound values u_j = D_j/(2 N_j) = (3^j-1)/2^{2j-1}:
     u_1 = 1, u_2 = 1, u_3 = 13/16 <= 1 (target upper half at stage 3);
     strictly decreasing for j >= 2; u_j -> 0 geometrically (x3/4 steps).
 (6) Limit-chain reading: min_{j<=J} u_j decreases: J=3 -> 13/16; J=5 ->
     121/256; J=8 -> 205/1024. So the liminf route gives rc(V) <= 13/16
     already at stage 3, sharpening along the system (mod cited liminf
     lemma + homogeneous estimate, both flagged in WORKLOG L5).

Prints VERIFY_OK.
"""
from fractions import Fraction

def main():
    # (1) recursion vs closed form
    print("(1) t recursion vs closed form:")
    t = 2
    for j in range(1, 13):
        assert t == 3**j - 1, (j, t)
        print(f"  j={j}: t={t} OK")
        t = 3 * t + 2
    # (2) D table
    print("(2) covering dimensions D_j = 2 t_j:")
    for j in range(1, 9):
        tj = 3**j - 1
        Dj = 2 * tj
        assert Dj == 2 * (3**j - 1)
        print(f"  j={j}: D={Dj}")
    print("  product rule dim((S^2)^t)=2t [cited topology] OK")
    # (3) matrix sizes
    print("(3) matrix-size recursion:")
    N = 2
    for j in range(1, 13):
        assert N == 2 * (4 ** (j - 1)), j
        print(f"  j={j}: N={N}")
        N = 4 * N
    print("  N_{j+1}=4N_j OK")
    # (4) multiplicity split
    print("(4) multiplicity split:")
    coord, pt, tot = 3, 1, 4
    assert coord + pt == tot
    assert Fraction(coord, tot) == Fraction(3, 4)
    assert pt > 0
    print(f"  {coord} coordinate + {pt} point-eval = {tot}; "
          "point count >0 consistent with density hypothesis [flagged] OK")
    # (5) upper-bound values
    print("(5) homogeneous bounds u_j = D_j/(2N_j):")
    prev = None
    for j in range(1, 13):
        D = 2 * (3**j - 1)
        N = 2 * (4 ** (j - 1))
        u = Fraction(D, 2 * N)
        assert u == Fraction(3**j - 1, 2**(2 * j - 1)), j
        flag = ""
        if j >= 3:
            assert u < prev, j
            flag = "(decreasing OK)"
        print(f"  j={j}: u={u}~{float(u):.6f} {flag}")
        prev = u
    assert Fraction(3**3 - 1, 2**5) == Fraction(13, 16) <= 1
    print("  u_3=13/16<=1 (target upper half at stage 3) OK")
    # (6) running minima
    print("(6) running minima min_{j<=J} u_j:")
    runmin = None
    for j in range(1, 11):
        D = 2 * (3**j - 1)
        N = 2 * (4 ** (j - 1))
        u = Fraction(D, 2 * N)
        runmin = u if runmin is None else min(runmin, u)
        if j in (3, 5, 8, 10):
            print(f"  J={j}: min={runmin}")
    assert runmin == Fraction(2 * (3**10 - 1), 2 * 2 * 4**9)
    print("  liminf route sharpens: 13/16 -> ... -> 7381/65536 OK")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
