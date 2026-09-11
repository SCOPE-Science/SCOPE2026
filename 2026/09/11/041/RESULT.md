# Realizability lift for the disjoint two-hyperplane cell in Δ(4,8)

## Context

Let Δ(4,8) be the hypersimplex of 4-subsets of [8]={1,…,8}.
Its regular subdivisions controlled by the 3-term Plücker relations form the
Dressian Dr(4,8); the realizable locus is the tropical Grassmannian
Trop Gr(4,8). A recognized open catalogue is: which sparse-paving Dressian
cells lift to Trop Gr(4,8)? The minimal non-uniform sparse-paving stratum on
Δ(4,8) is the cell with exactly two disjoint circuit-hyperplanes.

## Definitions

- M2: the rank-4 collection on [8] whose 4-subsets are all bases except
  1234 and 5678 (68 bases).
- A: the 4×8 rational matrix
  ```
  A = ⎡4  3  4  3  0  0  0  0⎤
      ⎢4  5  3  5  5  2  3  2⎥
      ⎢1  4  4  2  2  1  5  3⎥
      ⎣0  0  0  0  3  5  5  1⎦
  ```
- h: C(8,4)→{0,1} with h=1 on {1234,5678}, 0 elsewhere.
- Valued lift: A(t)=A+tG with G=E41+E15 (1-indexed), over Q(t) with
  t-adic valuation.

## Result

1. M2 is a connected sparse-paving matroid.
2. M2 is realizable over Q by A: the 70 4×4 minors of A vanish exactly on
   {1234,5678} and are nonzero on the remaining 68 four-sets
   (full table in `artifacts/minor_table.csv`).
3. h lies in Dr(4,8), induces a maximal secondary subdivision with three
   full-dimensional (affine dimension 7) matroid-polytope cells, and equals
   the tropicalization of A(t): det₁₂₃₄(t)=−22t, det₅₆₇₈(t)=−18t
   (valuation 1), all 68 basis minors have valuation 0. Hence h lies in the
   relative interior of its own Dressian secondary cone, and that cone meets
   Trop Gr(4,8).

## Proof / evidence

Exact integer/Fraction arithmetic (Python stdlib only):

1. Basis exchange over the 68 claimed bases holds exhaustively; no
   1≤k≤7 subset satisfies r(X)+r(Xᶜ)=4, so M2 is connected. The two
   nonbases are disjoint, giving the sparse-paving shape.
2. Columns 1–4 have row 4 equal to 0 and columns 5–8 have row 1 equal to 0,
   so both target minors vanish. Exact computation of all C(8,4)=70 minors
   gives 0 exactly on the two targets and explicit nonzero integers
   elsewhere; the archived table matches independent recomputation 70/70.
3. (a) All 420 Dressian 3-term relations (base 2-set + complement
   quadruple) satisfy min-attained-twice.
   (b) Maximal cells C0={68 bases}, C1={1234 + 16 neighbors meeting 1234
   in 3 points}, C2={5678 + 16 neighbors} are certified lower faces by
   supporting planes z≡0, z(S)=|S∩1234|−3, z(S)=|S∩5678|−3 with strict
   inequality off-cell; each has affine dimension 7, satisfies basis
   exchange, the three cover all 70 vertices, C1∩C2=∅.
   (c) Permutation-expansion determinant polynomials of A(t) give
   valuations exactly h (0 mismatches in 70), so trop(A(t))=h ∈ Trop Gr(4,8);
   since h induces exactly the subdivision in (b), it is in the relative
   interior of its Dressian secondary cone.

## Limitations

- Realizability over Q (hence any characteristic-0 field); positive
  characteristic not addressed.
- Interior claim is for this specific secondary cone of Dr(4,8) only.
- Computer checks are exact (integer/Fraction arithmetic), not floating point.

## Reproducibility

Run `python3 artifacts/verify_target.py` (Python stdlib only).
Expected output ends with `ALL_CHECKS_PASS`.
`artifacts/minor_table.csv` lists all 70 minors.

## References

- Speyer–Williams, The positive Dressian equals the positive tropical
  Grassmannian. https://people.math.harvard.edu/~williams/papers/Dressian2.pdf
- Herrmann–Joswig–Speyer, Dressians, Tropical Grassmannians, and Their Rays,
  arXiv:1112.1278. https://arxiv.org/abs/1112.1278
- Matroidal subdivisions, Dressians and tropical Grassmannians.
  https://depositonce.tu-berlin.de/handle/11303/7321
- Sage matroid catalog (type-level reference; no covering lift entry).
  http://sporadic.stanford.edu/reference/matroids/sage/matroids/catalog.html
