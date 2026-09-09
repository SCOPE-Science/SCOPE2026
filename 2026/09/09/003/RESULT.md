# Certified jammed backbone for the smallest open equal-circle-in-square case (N = 31)

## Context

The best-known packings of equal circles in a square are catalogued by Packomania
(`https://packomania.com/csq/csq.html`). Bold-face radii denote proven optima.
On the live table, radii for N = 1..30 are bold while the N = 31 radius
r = 0.089338333351 is non-bold (heuristic), with 55 contacts, 4 loose
(rattlers), 16 boundary, 15 core, and D1 symmetry. N = 31 is therefore the
smallest open (heuristic-only) equal-circle-in-square case. The Packomania data
files publish only bare coordinates (`csq31.txt`), total contact counts
(`contacts.txt`: 55 for N = 31), and rattler counts (`loose.txt`: 4 for
N = 31) — no rigidity-matrix rank, no equilibrium stress, and no jamming proof.

The question of which heuristic packings are rigid/jammed at the frontier where
global optimality becomes open belongs to the recognized packing-versus-rigidity
programs (Fejes Toth, Kuperberg, Connelly-type first-order rigidity with dual
stresses).

## Definitions

- Container: the unit square [-1/2, 1/2]^2. Circle i has center (x_i, y_i) and
  common radius r = 0.089338333351 (exact decimal Fraction).
- Committed centers: the 31 Packomania `csq31` coordinate pairs, embedded as
  exact decimal strings and parsed with `Fraction` (no floating-point input).
- Pair contact: dist(i,j) = 2r. Wall contact: the corresponding wall gap
  (x_i + 1/2 - r, 1/2 - x_i - r, y_i + 1/2 - r, 1/2 - y_i - r) equals 0.
- Backbone: the 27 circles remaining after removing rattlers {18, 22, 27, 28}.
- Rigidity matrix R (55 x 54): one row per backbone contact; for a pair (i,j)
  the row carries (x_i - x_j, y_i - y_j) at circle i's two columns and its
  negation at circle j (parallel to the contact normal, so each component
  (Rv)_k has the sign of the corresponding gap-opening rate); wall rows are
  +/- unit vectors matching wall-gap derivatives.
- Equilibrium stress: a vector w with R^T w = 0.
- Collective (first-order) jamming of the backbone: no infinitesimal velocity
  assignment strictly opens every backbone contact gap simultaneously.

## Result (headline claim)

The 27-circle backbone (rattlers {18, 22, 27, 28} removed) of the committed
N = 31 equal-circle packing in the unit square (r = 0.089338333351) is
collectively (first-order) jammed:

- (C1) Exactly 41 circle-circle contacts plus 14 wall contacts (55 total,
  matching the published Packomania contact count). Every listed contact
  satisfies |dist^2 - (2r)^2| <= 2e-12 (pairs) or |wall gap| <= 2e-12 (walls),
  with observed maximum pair squared-error 4.4e-13 and wall error 0. Every
  other backbone pair/wall gap clears by >= 3e-4.
- (C2) Circles {18, 22, 27, 28} touch nothing (all pair/wall clearances
  >= 3e-4), matching the published loose count of 4.
- (C3) The 55 x 54 rigidity matrix has exact rank 54 (full column rank): a
  54 x 54 minor (first 54 rows) has exactly nonzero Bareiss determinant
  (445-digit numerator).
- (C4) There exists an explicit exact strictly positive equilibrium stress:
  with w[54] = 1, the square system R_54^T z = -col_55 solved by exact Bareiss
  elimination yields w with all 55 entries > 0 (minimum ~0.369, maximum
  ~25.73) and R^T w = 0 checked entrywise in `Fraction` arithmetic.
- (C5) Jamming lemma: with w > 0 and R^T w = 0, for any velocity v,
  0 = w . (Rv) = sum_k w_k (Rv)_k forces some (Rv)_k >= 0; hence no
  infinitesimal motion strictly opens all 55 backbone gaps. To first order,
  the common radius cannot be increased while keeping all backbone contacts
  feasible.

Contact lists (1-based circle labels):

- Backbone pair contacts (41): 1-2, 1-8, 2-3, 2-9, 3-6, 4-5, 4-6, 4-7, 5-7,
  6-10, 6-11, 7-11, 7-12, 8-9, 8-14, 9-10, 9-13, 10-15, 11-15, 11-16, 12-16,
  13-15, 13-19, 14-19, 15-20, 16-17, 16-21, 17-21, 19-20, 19-23, 20-25, 20-26,
  21-24, 23-26, 23-29, 24-25, 24-31, 25-30, 25-31, 26-29, 26-30.
- Wall contacts (14): 1L, 1B, 2B, 3B, 4B, 5R, 8L, 12R, 14L, 17R, 23L, 29T,
  30T, 31T.

## Proof / evidence

All certificates use exact integer / `Fraction` arithmetic (stdlib only) and
replay in ~0.4 s with `python3 artifacts/verify_jam.py`:

1. Contact classification: brute-force exact check of all backbone pairs and
   walls against the 2e-12 contact tolerance and the 3e-4 clearance margin;
   rattler clearances checked against every other circle and wall.
2. Rank: fraction-free (Bareiss) determinant of the leading 54 x 54 minor is
   exactly nonzero (numerator with 445 digits), so rank is 54.
3. Stress: Bareiss solve of the 54 x 54 system with w[54] = 1, then exact
   positivity check (all > 0) and entrywise R^T w = 0 verification.
4. Lemma: exact algebra from (C4), as stated above.

Independent audit cross-checks (separate code): brute-force re-enumeration
reproduces exactly the 41-pair / 14-wall sets; rank mod p = 1000003 and
mod p = 1000033 is 54 in both cases; float SVD minimum singular value is
0.0159 (full column rank); float stress solve confirms all entries positive
with residual max 1.8e-15; embedded coordinates match fetched `csq31.txt`
to 1e-15 for all 31 centers.

## Limitations

- The coordinates are the heuristic-derived committed 12-decimal points, not
  a proven global optimum; no N = 31 optimality claim is made.
- Jamming is first-order (infinitesimal) via the positive stress; no nonlinear
  neighbourhood-exclusion box is closed.
- Rattler labeling is relative to the committed coordinates; rattlers could in
  principle jam under large perturbations — irrelevant to the backbone claim.
- The tightest clearance is 3.72e-4 (rattler pair 27-28) against the 3e-4
  threshold, so the classification margin, while positive and exact, is thin.

## Reproducibility

- `python3 artifacts/verify_jam.py` (stdlib only) replays C1-C5 and prints the
  exact stress vector; `artifacts/verify_output.txt` is a logged run.
- The verifier embeds the 31 centers and radius as exact decimal strings.

## References

- Packomania, Best known packings of equal circles in a square (main table).
  https://packomania.com/csq/csq.html
- Packomania csq31 coordinates. https://packomania.com/csq/txt/csq31.txt
- O. R. Musin, A. V. Nikitenko, Optimal packings of congruent circles on a
  square flat torus. arXiv:1212.0649.
