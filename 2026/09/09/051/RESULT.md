# Realizability and orientability of a once-relaxed Vámos matroid and its free 9-point extension (explicit Q-certificates)

## Context and motivation

Which abstract matroids arise from point configurations, and which admit
orientations, is a foundational classification demand in discrete geometry:
Mnev universality shows the rank-4 realizability boundary is wild, and
bracket-ideal / final-polynomial methods give the checkable infeasibility
witnesses. The Vámos matroid V8 (rank 4 on 8 points) is the canonical minimal
non-orientable matroid. Relaxing one circuit-hyperplane can restore
orientability, so the status of the once-relaxed neighbor and its 9-point
extensions is not mechanically implied by V8 itself. The nearest complete
table (Fukuda–Miyata–Moriyama, arXiv:1204.0645) covers 3-dimensional
configurations of 8 points but not rank-4 configurations of 9 points, leaving
this cell open.

## Definitions

- Let V8 be the Vámos matroid of rank 4 on {1,…,8} with circuit-hyperplanes
  1234, 1256, 3456, 3478, 5678 (fixed labeling used throughout).
- Let M8- be the relaxation of V8 at 5678: its bases are the bases of V8 plus
  the set 5678 (a matroid by the circuit-hyperplane relaxation theorem).
- Let M9+ be the single-element extension of M8- placing point 9 generically:
  no 4-set containing 9 is dependent. Since 5678 is a basis of M8-, its span
  is the whole rank-4 space, so this is the free (generic) extension of M8-;
  rank stays 4.

## Result

1. **M8- is realizable over Q** (hence over an ordered field), by the affine
   points (homogeneous columns (x,y,z,1)):
   p1=(1,2,0), p2=(2,1,0), p3=(0,0,0), p4=(1,0,0),
   p5=(2,0,1), p6=(0,0,3), p7=(-1,1,1), p8=(0,1,1).
   The dependent 4-sets among these columns are exactly
   {1234, 1256, 3456, 3478}; in particular det[5678] = 2 ≠ 0.
2. **M9+ is realizable over Q** by adding p9=(7,11,13), which satisfies
   p9 = −16·p5 + 6·p6 − 39·p7 + 50·p8 (affine combination, coefficients
   summing to 1), so 9 lies in the affine span of {5,6,7,8}, and no 4-set
   containing 9 is dependent. The full list of dependent 4-sets on 9 points
   is still exactly the four planes above; rank is 4.
3. **Both are orientable**: the determinant-sign chirotope of the Q-matrix is
   a valid oriented matroid (realizable ⇒ orientable). On M9+ the 122 bases
   split into 73 positive and 49 negative 4×4 determinants.
4. **Simplicity/minors**: the point sets are simple (9 distinct points, no
   two parallel, no three affinely collinear — all C(9,3) triples checked).
   Every deletion is realized by deleting a column; the contraction M9+/9
   (rank 3) is realized over Q by projecting from column 9, with {1,5,7} an
   explicit independent triple ({9,1,2,3} is a basis with det −39, so the
   projection is defined over Q).

## Proof / evidence

Positive verdict by exact certificate (proof, not experiment). All
determinants are exact 4×4 determinants of the homogeneous columns (x,y,z,1)
in exact rational arithmetic:

- Enumerating all C(8,4)=70 quadruples of the first eight columns gives zero
  determinant exactly on 1234, 1256, 3456, 3478, and det(5678)=2. Thus the
  column matroid has precisely the Vámos nonbases minus 5678, i.e. the
  relaxation M8-. By the relaxation theorem no basis-exchange search is
  needed.
- The affine relation for p9 is verified exactly (coefficients sum to 1), and
  enumerating all C(9,4)=126 quadruples shows no dependent set contains 9.
  Hence the extension adds 9 freely; rank stays 4.
- Determinant signs give a chirotope; realizability over the ordered field Q
  implies the oriented-matroid axioms. Sign counts (73+/49−) are read off the
  same determinant table.
- Simplicity: pairwise distinctness plus a cross-product check on all triples
  (no vanishing cross product); independently, every 2- and 3-subset has full
  homogeneous linear rank. Contraction: change-of-basis inverse sending column
  9 to e4 then dropping the last row, all over Q; {1,5,7} has nonzero
  projected 3×3 determinant.

The entire check is replayed by `output/artifacts/verify_m9.py` (stdlib only,
exact `Fraction` arithmetic); it prints `VERIFY_OK`
(bases=122 pos=73 neg=49 planes=4, affine coeffs [-16,6,-39,50]).

## Limitations

- Positive coordinate verdict, so no Sturmfels final-polynomial /
  bi-quadratic obstruction identity is needed or given.
- Catalogue novelty (matroid-database IDs) and equivalence of the five
  possible relaxation choices were not checked; the claim is the explicit
  coordinate verdict itself, replayable without any catalogue.
- Only the stated generic (free) placement of 9 is decided; other placements
  of the 9th point (e.g. creating new dependent planes) are untouched.
- The coordinates were found by a bounded randomized integer search whose
  code is not part of the certificate — only the exact verification script is.
- Vámos labeling conventions vary across sources; the verdict is tied to the
  fixed circuit-hyperplane list above.

## Reproducibility

Run `python3 output/artifacts/verify_m9.py` (Python 3, standard library only).
Expected output ends with `VERIFY_OK`. The audit independently recomputed all
determinants by a separate permutation-expansion implementation and confirmed
the dependent-set lists, det(5678)=2, det(9,1,2,3)=−39, the affine identity,
and the simplicity checks.

## References

- K. Fukuda, H. Miyata, S. Moriyama, Complete enumeration of small realizable
  oriented matroids, arXiv:1204.0645 — table stops at rank-4 on 8 points.
- K. Fukuda, S. Moriyama, H. Nakayama, Every non-Euclidean oriented matroid
  admits a biquadratic final polynomial, arXiv:math/0510500 — method
  framework, no M8-/M9+ row.
- M. Brandt, A. Wiebe, The slack realization space of a matroid,
  arXiv:1804.05264 — general realization-space model, no M8-/M9+ row.
- S. Burton, C. Vinzant, Y. Youm, A real stable extension of the Vamos
  matroid polynomial, arXiv:1411.2038 — different 10-element extension of V8
  for real stability, not this 9-point orientability cell.
- A. Björner et al., Oriented Matroids (2nd ed.); J. Richter-Gebert,
  Realization Spaces of Polytopes (Mnev universality); J. Bokowski,
  B. Sturmfels, Computational Synthetic Geometry — background axioms, methods,
  and wildness context.
