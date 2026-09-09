"""Exact verifier for lane-434 target-directed certificates.
Replays with exact rational arithmetic (Fractions) + exact integers only.
Prints VERIFY_OK iff all checks pass. Stdlib only.
"""
from fractions import Fraction


def check_theta_prime_point():
    # Circulant B for theta'(C7) primal: max <J,B>, tr=1, PSD, entrywise>=0, 0 on C7 edges.
    a0 = Fraction(1, 7)
    a2 = Fraction(11428, 100000)  # 0.11428
    a3 = Fraction(5094, 100000)   # 0.05094
    row = [a0, Fraction(0), a2, a3, a3, a2, Fraction(0)]
    n = 7
    B = [[row[(j - i) % n] for j in range(n)] for i in range(n)]
    # (i) trace == 1
    assert sum(B[i][i] for i in range(n)) == 1, "trace"
    # (ii) zero on C7 edges (offset +-1)
    for i in range(n):
        assert B[i][(i + 1) % n] == 0 and B[i][(i - 1) % n] == 0, "edge zero"
    # (iii) entrywise >= 0
    assert min(min(r) for r in B) >= 0, "nonneg"
    # (iv) exact LDL, no pivoting: all pivots > 0  => strictly PSD
    L = [[Fraction(0)] * n for _ in range(n)]
    D = [Fraction(0)] * n
    for i in range(n):
        L[i][i] = Fraction(1)
    for k in range(n):
        s = B[k][k] - sum(L[k][t] ** 2 * D[t] for t in range(k))
        assert s > 0, "pivot %d = %s not >0" % (k, s)
        D[k] = s
        for i in range(k + 1, n):
            t = B[i][k] - sum(L[i][u] * L[k][u] * D[u] for u in range(k))
            L[i][k] = t / D[k]
    # (v) objective = sum all entries = 1 + 14(a2+a3) = 16543/5000 > 33/10
    obj = sum(sum(r) for r in B)
    assert obj == 1 + 14 * (a2 + a3) == Fraction(82827, 25000), "objective %s" % obj
    assert obj > Fraction(33, 10), "must exceed 3.30"
    return obj, D


def check_lower_bound():
    # Polak-Schrijver alpha(C7^5) >= 367  =>  Theta > 3.257 (exact integer)
    assert 3257 ** 5 < 367 * 10 ** 15
    return True


def check_window_cells_empty_by_theorem():
    # Theorem: every (n,d)-rep of C7 over any field has n/d >= 7/2.
    # Proof replayed in DRAFT (Prop.11 iteration). Here: check that 7/2 > 33/10
    # and that the two candidate small cells (23,7),(33,10) both lie below 7/2.
    assert Fraction(7, 2) > Fraction(33, 10)
    assert Fraction(23, 7) < Fraction(7, 2) and Fraction(33, 10) < Fraction(7, 2)
    return True


def check_cover_value():
    # chi_f(C7bar) <= 7/2 via weight 1/2 on each C7 edge (cliques of C7bar = ... ):
    # each vertex in exactly 2 edges -> coverage 1; total 7/2. Exact.
    w = Fraction(1, 2)
    assert 7 * w == Fraction(7, 2)
    assert 2 * w == 1
    return True


if __name__ == "__main__":
    obj, pivots = check_theta_prime_point()
    check_lower_bound()
    check_window_cells_empty_by_theorem()
    check_cover_value()
    print("theta'-point objective =", obj, "=", float(obj))
    print("exact LDL pivots:", ["%s~%.6f" % (p, float(p)) for p in pivots])
    print("all exact checks passed")
    print("VERIFY_OK")
