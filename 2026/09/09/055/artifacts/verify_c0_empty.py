#!/usr/bin/env python3
"""Verifier: C0: y^2 = x^6+3x^4-5x^2+7 has NO integral points (C0(Z) = empty).

Stdlib-only. Checks:
  (A) exact mod-4 exhaustion: f(x) in {2,3} mod 4 for all residues, never a square {0,1};
  (B) discriminant of f != 0 via exact Bareiss determinant of Sylvester matrix
      (smooth affine curve; genus-2 degree-6 model);
  (C) brute-force cross-check |x| <= LIM finds no solutions.
Exit 0 + print VERIFY_OK iff all pass.
"""
import math

def f_int(x: int) -> int:
    return x**6 + 3*x**4 - 5*x**2 + 7

def check_mod4():
    squares = {(y*y) % 4 for y in range(4)}
    assert squares == {0, 1}, squares
    table = {}
    for r in range(4):
        table[r] = f_int(r) % 4
    # exact expected values: even -> 3, odd -> 2
    assert table == {0: 3, 1: 2, 2: 3, 3: 2}, table
    for r, v in table.items():
        assert v not in squares, (r, v)
    return table

def poly_coeffs_desc(coeffs_asc):
    # strip leading zeros, return descending list
    c = list(coeffs_asc)
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c[::-1]

def sylvester(a_desc, b_desc):
    m = len(a_desc) - 1  # deg a
    n = len(b_desc) - 1  # deg b
    N = m + n
    M = [[0]*N for _ in range(N)]
    for i in range(n):
        for j, c in enumerate(a_desc):
            M[i][i+j] = c
    for i in range(m):
        for j, c in enumerate(b_desc):
            M[n+i][i+j] = c
    return M

def bareiss_det(M):
    N = len(M)
    A = [row[:] for row in M]
    prev = 1
    for k in range(N-1):
        # partial pivot (exact): find nonzero pivot row
        if A[k][k] == 0:
            piv = -1
            for i in range(k+1, N):
                if A[i][k] != 0:
                    piv = i
                    break
            if piv == -1:
                return 0
            A[k], A[piv] = A[piv], A[k]
        for i in range(k+1, N):
            for j in range(k+1, N):
                A[i][j] = (A[i][j]*A[k][k] - A[i][k]*A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
        if prev == 0:
            return 0
    return A[N-1][N-1]

def check_discriminant():
    # f = x^6+3x^4-5x^2+7 ; f' = 6x^5+12x^3-10x
    a_desc = [1, 0, 3, 0, -5, 0, 7]   # deg 6
    b_desc = [6, 0, 12, 0, -10, 0]    # deg 5
    M = sylvester(a_desc, b_desc)
    assert len(M) == 11 and all(len(r) == 11 for r in M)
    res = bareiss_det(M)
    # |disc(f)| = |Res(f,f')| / lc(f); Sylvester row-ordering fixes only the sign,
    # so assert the absolute value (cross-checked against sympy: disc = -4714544128).
    disc_abs = abs(res)
    assert res != 0 and disc_abs != 0
    assert disc_abs == 4714544128, res
    disc = -4714544128  # sympy convention value
    return disc

def check_bruteforce(lim=50000):
    found = []
    for x in range(-lim, lim+1):
        v = f_int(x)
        r = math.isqrt(v)
        if r*r == v:
            found.append(x)
    assert found == [], found
    return lim

def check_mod8_mod16():
    # supplementary witnesses (not needed for proof)
    f8 = sorted({f_int(x) % 8 for x in range(8)})
    q8 = sorted({(y*y) % 8 for y in range(8)})
    f16 = sorted({f_int(x) % 16 for x in range(16)})
    q16 = sorted({(y*y) % 16 for y in range(16)})
    assert f8 == [3, 6, 7], f8
    assert q8 == [0, 1, 4], q8
    assert f16 == [3, 6, 7], f16
    assert q16 == [0, 1, 4, 9], q16
    assert set(f8).isdisjoint(q8) and set(f16).isdisjoint(q16)
    return f8, f16

if __name__ == "__main__":
    t = check_mod4()
    print("mod4 table:", t, " squares mod4: {0,1}  -> no overlap OK")
    d = check_discriminant()
    print("disc(f) =", d, " != 0 OK")
    f8, f16 = check_mod8_mod16()
    print("mod8 f-values:", f8, " mod16 f-values:", f16, " OK")
    lim = check_bruteforce(50000)
    print(f"brute force |x| <= {lim}: no solutions OK")
    print("VERIFY_OK")
