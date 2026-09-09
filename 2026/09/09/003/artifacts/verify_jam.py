#!/usr/bin/env python3
"""Exact jammed-backbone certificate for N=31 equal circles in the square.

Object: committed Packomania csq31 coordinates (31 centers, r = 0.089338333351),
embedded below as exact decimal strings and parsed with Fraction (no float input).

Certificates (exact integer / Fraction arithmetic only):
  C1  contact classification: 41 circle-circle contacts + 14 wall contacts = 55
      (= Packomania contacts count); all other pairs/walls clear by >= 3e-4
      (scaled-integer check with margin; contact error <= 2e-12).
  C2  rattlers: circles {18,22,27,28} touch nothing (min clearance >= 3e-4);
      backbone = other 27 circles (= 4 loose = Packomania loose count).
  C3  rigidity matrix R is 55 x 54; a 54x54 minor has nonzero determinant
      (Bareiss fraction-free elimination) -> rank 54 (full column rank).
  C4  exact equilibrium stress: R^T w = 0 with all 55 components > 0
      (Bareiss solve with w[54] = 1; positivity + balance checked in Fractions).
  C5  first-order jamming lemma (exact algebra from C4): no infinitesimal
      motion strictly opens every backbone contact gap; hence no smooth
      radius-increasing perturbation exists to first order (collective jamming).

Run: python3 verify_jam.py   (stdlib only; seconds)
"""
from fractions import Fraction
import sys

S = 10 ** 12  # scaling for margin checks

XS = ["-0.410661666649","-0.231984999946","-0.053308333244","0.254662533649",
"0.410661666649","0.100677100202","0.257215322250","-0.410661666649",
"-0.231984999946","-0.053326570270","0.103229888804","0.410661666649",
"-0.229432211345","-0.410661666649","-0.050773781669","0.256676233203",
"0.410661666649","0.078847039992","-0.320031442605","-0.141373012929",
"0.255180873553","0.405733726638","-0.410661666649","0.128837390888",
"-0.049833018312","-0.232003236973","0.405733726644","0.226685239996",
"-0.323543231590","-0.140463242356","0.040797205733"]
YS = ["-0.410661666649","-0.410661666649","-0.410661666649","-0.410661666649",
"-0.323543231590","-0.320031442605","-0.232003236973","-0.231984999946",
"-0.231984999946","-0.229432211345","-0.141373012929","-0.140463242356",
"-0.053326570270","-0.053308333244","-0.050773781669","-0.049833018312",
"0.040797205733","0.078847040001","0.100677100202","0.103229888804",
"0.128837390888","0.226685239992","0.254662533649","0.255180873553",
"0.256676233203","0.257215322250","0.405733726644","0.405733726649",
"0.410661666649","0.410661666649","0.410661666649"]
RS = "0.089338333351"

X = [Fraction(s) for s in XS]
Y = [Fraction(s) for s in YS]
R = Fraction(RS)
N = 31
assert len(X) == len(Y) == N

# ---- candidate backbone contacts (verified exactly below) ----
BPAIRS = [(2,3),(8,14),(6,10),(13,19),(7,11),(20,26),(12,16),(25,30),(3,6),
(14,19),(21,24),(4,5),(23,29),(17,21),(24,31),(5,7),(7,12),(11,16),(20,25),
(26,29),(26,30),(9,10),(9,13),(10,15),(13,15),(4,7),(23,26),(6,11),(19,20),
(16,17),(25,31),(11,15),(15,20),(1,2),(1,8),(2,9),(8,9),(4,6),(19,23),
(16,21),(24,25)]
WALLS = [(1,'L'),(1,'B'),(2,'B'),(3,'B'),(4,'B'),(5,'R'),(8,'L'),(12,'R'),
(14,'L'),(17,'R'),(23,'L'),(29,'T'),(30,'T'),(31,'T')]
RATTLERS = [18,22,27,28]
BACKBONE = [i for i in range(1, N+1) if i not in RATTLERS]

CONTACT_TOL = Fraction(2, 10**12)     # |dist^2 - (2r)^2| <= tol  (sq units)
CLEAR_MARGIN = Fraction(3, 10**4)     # non-contacts clear by >= 3e-4 (dist units)

def sqdist(i, j):
    dx = X[i-1]-X[j-1]; dy = Y[i-1]-Y[j-1]
    return dx*dx+dy*dy

def wallgap(i, w):
    if w == 'L': return X[i-1] + Fraction(1,2) - R
    if w == 'R': return Fraction(1,2) - X[i-1] - R
    if w == 'B': return Y[i-1] + Fraction(1,2) - R
    if w == 'T': return Fraction(1,2) - Y[i-1] - R
    raise ValueError

def main():
    D2 = (2*R)**2
    # ---- C1a: backbone pair contacts exact ----
    bset = set()
    for (i, j) in BPAIRS:
        a, b = (i,j) if i < j else (j,i)
        bset.add((a,b))
    assert len(bset) == 41, len(bset)
    for (i, j) in bset:
        assert abs(sqdist(i,j) - D2) <= CONTACT_TOL, (i, j)
    # ---- C1b: every other backbone pair clears by margin ----
    bb = set(BACKBONE)
    for i in BACKBONE:
        for j in BACKBONE:
            if j <= i: continue
            if (i,j) in bset: continue
            d2 = sqdist(i,j)
            gmin = (2*R + CLEAR_MARGIN)
            assert d2 >= gmin*gmin, ("pair clearance", i, j)
    # ---- C1c: wall contacts exact; other backbone walls clear ----
    wset = set(WALLS)
    assert len(wset) == 14
    for (i, w) in wset:
        assert abs(wallgap(i,w)) <= CONTACT_TOL, (i, w)
    for i in BACKBONE:
        for w in "LRBT":
            if (i,w) in wset: continue
            assert wallgap(i,w) >= CLEAR_MARGIN, ("wall clearance", i, w)
    # ---- C2: rattlers touch nothing ----
    for k in RATTLERS:
        for j in range(1, N+1):
            if j == k: continue
            gmin = (2*R + CLEAR_MARGIN)
            assert sqdist(k,j) >= gmin*gmin, ("rattler pair", k, j)
        for w in "LRBT":
            assert wallgap(k,w) >= CLEAR_MARGIN, ("rattler wall", k, w)
    # rattler clearance rechecked against every circle (loops above); done.
    print("C1/C2: 41 pair + 14 wall contacts exact (err<=2e-12); "
          "all other gaps >= 3e-4; rattlers {18,22,27,28} clear. OK")

    # ---- rigidity matrix (exact Fractions) ----
    idx = {c: k for k, c in enumerate(BACKBONE)}
    n = len(BACKBONE); m = len(BPAIRS) + len(WALLS)
    assert (n, m) == (27, 55)
    rows = []
    for (i, j) in BPAIRS:
        dx = X[i-1]-X[j-1]; dy = Y[i-1]-Y[j-1]
        r = [Fraction(0)]*(2*n)
        r[2*idx[i]] = dx; r[2*idx[i]+1] = dy
        r[2*idx[j]] = -dx; r[2*idx[j]+1] = -dy
        rows.append(r)
    for (i, w) in WALLS:
        r = [Fraction(0)]*(2*n)
        if w == 'L': r[2*idx[i]] = Fraction(1)
        elif w == 'R': r[2*idx[i]] = Fraction(-1)
        elif w == 'B': r[2*idx[i]+1] = Fraction(1)
        else: r[2*idx[i]+1] = Fraction(-1)
        rows.append(r)

    # ---- C3: Bareiss determinant of 54x54 minor (drop last row) ----
    M = [row[:] for row in rows[:54]]
    det = bareiss_det(M)
    assert det != 0
    print(f"C3: rank R = 54 (54x54 minor det != 0; "
          f"det has {len(str(abs(det.numerator)))}-digit numerator). OK")

    # ---- C4: exact stress via Bareiss solve of R55^T w = 0 with w55 = 1 ----
    # Solve A z = b, A = first-54 rows of R^T restricted... use square system:
    # unknowns w[0..53], equations R54^T w[0..53] = -col55_of_R54rows... precisely:
    # full: sum_{k=0..54} R[k][c] w[k] = 0 for each col c (54 cols).
    # Fix w[54]=1 -> A z = b with A[c][k] = R[k][c], b[c] = -R[54][c].
    A = [[rows[k][c] for k in range(54)] for c in range(54)]
    b = [-rows[54][c] for c in range(54)]
    z = bareiss_solve(A, b)
    w = z + [Fraction(1)]
    assert all(v > 0 for v in w), [v for v in w if v <= 0]
    for c in range(54):
        s = sum(rows[k][c]*w[k] for k in range(55))
        assert s == 0, c
    print(f"C4: strictly positive exact equilibrium stress, "
          f"min={min(w)} max={max(w)}. OK")
    print("  stress (contact order: 41 pairs then 14 walls):")
    for k, v in enumerate(w):
        print(f"   w[{k}] = {v}  (~{float(v):.6f})")

    # ---- C5: first-order jamming lemma ----
    print("C5: lemma: with w>0, R^T w=0: any velocity v has some contact row "
          "with (Rv)_k >= 0, i.e. no motion strictly opens all 55 gaps; "
          "to first order no radius-increasing perturbation exists. OK")
    print("ALL CERTIFICATES PASS.")

def bareiss_det(M):
    n = len(M)
    A = [row[:] for row in M]
    prev = Fraction(1)
    for k in range(n-1):
        if A[k][k] == 0:
            piv = next((i for i in range(k+1, n) if A[i][k] != 0), None)
            if piv is None: return Fraction(0)
            A[k], A[piv] = A[piv], A[k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = (A[i][j]*A[k][k] - A[i][k]*A[k][j]) / prev
            A[i][k] = Fraction(0)
        prev = A[k][k]
        if prev == 0: return Fraction(0)
    return A[n-1][n-1]

def bareiss_solve(A, b):
    n = len(A)
    M = [A[i][:] + [b[i]] for i in range(n)]
    prev = Fraction(1)
    for k in range(n):
        if M[k][k] == 0:
            piv = next((i for i in range(k+1, n) if M[i][k] != 0), None)
            assert piv is not None, "singular"
            M[k], M[piv] = M[piv], M[k]
        for i in range(k+1, n):
            for j in range(k+1, n+1):
                M[i][j] = (M[i][j]*M[k][k] - M[i][k]*M[k][j]) / prev
            M[i][k] = Fraction(0)
        prev = M[k][k]
        assert prev != 0, "singular"
    x = [Fraction(0)]*n
    for i in range(n-1, -1, -1):
        s = M[i][n] - sum(M[i][j]*x[j] for j in range(i+1, n))
        x[i] = s / M[i][i]
    return x

if __name__ == "__main__":
    main()
