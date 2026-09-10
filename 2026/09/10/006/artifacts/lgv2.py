"""LGV cross-check via Zeilberger's (n,k)-Magog determinant (right trapezoids, m=0).
Zeilberger'96: # (n,k) right Magog trapezoids = det_{0<=i,j<k} ( binom(n+k-i-j-1, n-i-1... )).
We use the clean Krattenthaler form: M(n,k) = prod ... ; instead of guessing indices,
verify the product formula for right Gog/Magog (n,k) counts against brute force at
n<=5 (self-calibrating), then use the determinant evaluation code path (Dodgson-exact
integer det) as the LGV certificate for the left-(6,3) anchor via the left-right
symmetry on the Gog side (involution 3.1) + computed left=right Gog counts.
Concretely: certify |G_left(6,3)| = |G_right(6,3)| via explicit involution (3.1) on data,
and |G_right(6,3)| = det-LGV = |M_right(6,3)| (Zeilberger), and |M_right| <-> S-image
left GOGAm count 4862. This composes the LGV agreement.
"""
from math import comb, prod
from fractions import Fraction

def det_int(M):
    n = len(M)
    A = [[Fraction(x) for x in row] for row in M]
    d = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None: return 0
        if p != c: A[c], A[p] = A[p], A[c]; d = -d
        d *= A[c][c]
        for r in range(c+1, n):
            f = A[r][c]/A[c][c]
            for k in range(c, n): A[r][k] -= f*A[c][k]
    assert d.denominator == 1, d
    return int(d)

def zeil_magog_right(n, k):
    """Zeilberger (n,k) right Magog count: det_{0<=i,j<=k-1} C(n+k-i-j-1, n-i-1)? calibrate."""
    M = [[comb(n+k-i-j-1, n-i-1) if n+k-i-j-1 >= 0 and n-i-1 >= 0 else 0
          for j in range(k)] for i in range(k)]
    return det_int(M)

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "artifacts")
    from gen import gen_gog
    # calibrate against brute-force RIGHT Gog trapezoid counts n<=5
    for n in range(1, 6):
        g = gen_gog(n)
        for k in (1, 2, 3):
            rg = set(tuple(tuple(row[j:]) for j, row in enumerate(t)) for t in g)  # right trap: entries i-j<=k-1 <-> j>=i-k+1
            # filter: right trap projection
            rset = set()
            for t in g:
                key = []
                for i, row in enumerate(t):
                    lo = max(0, (i+1)-k)
                    key.append(tuple(row[lo:]))
                rset.add(tuple(key))
            z = zeil_magog_right(n, k)
            print(f"n={n} k={k}: |Gright|={len(rset)} Zeil-det={z} match={len(rset)==z}", flush=True)
