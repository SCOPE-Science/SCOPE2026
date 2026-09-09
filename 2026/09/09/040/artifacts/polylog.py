"""Polynomial exclusion log: no 9-direction function in four exhaustive families over F_13.

A Redei-type blocking set of size 22 in PG(2,13) would require a function
f : F_13 -> F_13 determining exactly N = 9 directions (slopes). This script
exhaustively checks four families and asserts N = 9 never occurs:

  A0. ALL monomials a*x^e (1 <= a <= 12, 0 <= e <= 12); scaling f -> a*f sends
      each secant slope s to a*s (bijection), so N is preserved (representative
      x^e suffices; all a are checked explicitly);
  A. ALL binomials a*x^e + b*x^j (1 <= a,b <= 12, 0 <= j < e <= 12);
  B. ALL trinomials x^e + a*x^j + b*x^k, monic (scaling f -> a*f permutes
     slopes, so monic covers all), 0 <= k < j < e <= 12;
  C. ALL polynomials of degree <= 6 via normalized representatives
     x^d + c_{d-1} x^{d-1} + ... + c_2 x^2 (d <= 6): every polynomial is
     a*f + m*x + c with f normalized, and f -> a*f + m*x + c sends each secant
     slope s to a*s + m (bijection), hence preserves the direction count N.

Consequence (computed, replayable): any N = 9 function over F_13 -- if one
exists at all -- has >= 4 nonzero terms and degree >= 7.

Usage: python3 polylog.py  (stdlib only; ~1-3 minutes)
Exit 0 with PASS lines iff all assertions hold.
"""
import sys
import time

P = 13
PAIRS = [(x, y) for x in range(P) for y in range(x + 1, P)]
INV = {d: pow(d, -1, P) for d in range(1, P)}


def ndir(f):
    D = set()
    for x, y in PAIRS:
        D.add(((f[x] - f[y]) * INV[(x - y) % P]) % P)
    return len(D)


def polyval(coeffs, x):
    # coeffs: dict exp -> coeff
    s = 0
    for e, c in coeffs.items():
        s += c * pow(x, e, P)
    return s % P


def main():
    t0 = time.time()
    # ---- Family A0: all monomials a*x^e ----
    seenA0, n9A0, tableA0 = set(), 0, {}
    for e in range(0, 13):
        for a in range(1, 13):
            f = [(a * pow(x, e, P)) % P for x in range(P)]
            n = ndir(f)
            seenA0.add(n)
            tableA0.setdefault(e, set()).add(n)
            if n == 9:
                n9A0 += 1
    print(f"A0 monomials: N-values={sorted(seenA0)} N=9 count={n9A0} "
          f"-> {'PASS' if n9A0 == 0 else 'FAIL'}")
    print(f"  12-case table (e: N): "
          f"{ {e: sorted(v) for e, v in sorted(tableA0.items())} }")
    # ---- Family A: all binomials ----
    seenA, n9A = set(), 0
    for e in range(1, 13):
        for j in range(0, e):
            for a in range(1, 13):
                for b in range(1, 13):
                    f = [(a * pow(x, e, P) + b * pow(x, j, P)) % P
                         for x in range(P)]
                    n = ndir(f)
                    seenA.add(n)
                    if n == 9:
                        n9A += 1
    print(f"A binomials: N-values={sorted(seenA)} N=9 count={n9A} "
          f"-> {'PASS' if n9A == 0 else 'FAIL'}")
    # ---- Family B: all monic trinomials ----
    seenB, n9B = set(), 0
    for e in range(2, 13):
        for j in range(1, e):
            for k in range(0, j):
                for a in range(1, 13):
                    for b in range(1, 13):
                        f = [(pow(x, e, P) + a * pow(x, j, P)
                              + b * pow(x, k, P)) % P for x in range(P)]
                        n = ndir(f)
                        seenB.add(n)
                        if n == 9:
                            n9B += 1
    print(f"B trinomials: N-values={sorted(seenB)} N=9 count={n9B} "
          f"-> {'PASS' if n9B == 0 else 'FAIL'}")
    # ---- Family C: all normalized deg<=6 ----
    seenC, n9C = set(), 0
    # degrees 0,1: constant (N=0: single value, no secants... define via code),
    # linear (N=1). Handle d>=2 uniformly; add d<2 by hand.
    seenC.add(1)  # linear functions determine 1 direction
    import itertools
    for d in range(2, 7):
        for co in itertools.product(range(P), repeat=d - 1):
            # f = x^d + co[0] x^{d-1} + ... + co[d-2] x^2
            f = []
            for x in range(P):
                v = pow(x, d, P)
                for i, c in enumerate(co):
                    v += c * pow(x, d - 1 - i, P)
                f.append(v % P)
            n = ndir(f)
            seenC.add(n)
            if n == 9:
                n9C += 1
                print("  UNEXPECTED N=9 deg", d, co)
    print(f"C deg<=6 normalized: N-values={sorted(seenC)} N=9 count={n9C} "
          f"-> {'PASS' if n9C == 0 else 'FAIL'}")
    # ---- control: known witnesses attain N=8,10,11 ----
    for nm, co, want in [("W21", {7: 1}, 8), ("W23", {9: 1, 5: 1}, 10),
                         ("W24", {7: 1, 3: 2}, 11)]:
        got = ndir([polyval(co, x) for x in range(P)])
        flag = "OK" if got == want else "MISMATCH"
        print(f"  control {nm}: N={got} (want {want}) [{flag}]")
        assert got == want
    dt = time.time() - t0
    allok = (n9A0 == 0 and n9A == 0 and n9B == 0 and n9C == 0)
    print(f"OVERALL: {'PASS' if allok else 'FAIL'} ({dt:.1f}s)")
    print(f"  12-case monomial table (e: N): "
          f"{ {e: sorted(v) for e, v in sorted(tableA0.items())} }")
    print("CONCLUSION: no 9-direction function among all monomials, all "
          "binomials, all trinomials, or any polynomial of degree <= 6 over "
          "F_13; a Redei-type size-22 blocking set would need >= 4 terms, "
          "deg >= 7.")
    sys.exit(0 if allok else 1)


if __name__ == "__main__":
    main()
