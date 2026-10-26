# Scientific review — obtuse isosceles midpoint interpolation

## Correctness — PASS
The claim is the exact real-linear extension norm for the six-point Euclidean metric obtained by adding all three edge midpoints to an obtuse/right isosceles triangle. All quantities are defined and the endpoint \(h=1\) is included; the degenerate \(h=0\) limit is not treated as a triangle. Reflection-averaging any extension gives a symmetric coefficient at the hypotenuse midpoint. Two explicit unit-Lipschitz source functions imply the sharp lower bound \(L^2/[L+h(L-1)]\), even for signed or asymmetric competitors. The positive candidate meets that bound and its fifteen unordered target pairs are completely classified. The only nontrivial cross-pair comparison reduces to \(5\sqrt2>7\). A standard-library checker independently tests the six source-potential vertices and 11,160 target pair comparisons across 124 heights, but finite evidence is not used as a proof of the continuum statement. The free-space interpretation relies on Basso's established finite-space duality (2021, Eq. (1.6)).

## Originality — PASS, qualified by bibliographic uncertainty
The closest accessible prior material is Basso's 2021 finite-metric extension/projection theory, Bruè–Di Marino–Stra's 2018 general random-projection construction, and the publicly readable result on the canonical barycentric Lipschitz-free interpolation norm of arbitrary Euclidean triangles. The latter calculates the fixed affine rule, which on the stated obtuse isosceles triangles has norm \(L/h\); it does **not** optimize extensions on the six-point vertex-plus-midpoint set. Other finite results about equilateral simplices, rectangles, cubes, and regular polygons use non-isometric vertex configurations and do not imply the present obtuse-isosceles continuum. Meaningful equivalent-formulation, stronger-coverage, exact-value, and claim-implication searches found no covering result; a failed search is not a proof of novelty. Unindexed exact interpolation notes remain a real residual risk.

## Mathematical value — PASS
The object is the smallest Euclidean triangular cell family with a nontrivial angular parameter, precisely the complete class of obtuse/right isosceles similarity types. The calculation identifies the unique sharp stability modulus of simultaneous midpoint extension, an explicit positive universal Banach-valued scheme, and an unbounded stability gap against the conventional affine midpoint rule as cells flatten. In particular the sharp norm converges to one while the standard rule diverges. This is a motivated natural interpolation invariant, not an arbitrary numeric slice or an enumeration-only claim. It is not asserted to imply a global meshing theorem.

## Closest literature and limitations
- E. Bruè, S. Di Marino, F. Stra (2018), arXiv:1801.07533, Sections 3–4: broad linear Lipschitz extension constructions, not an exact six-point interpolation modulus.
- G. Basso (2021), arXiv:2104.14238, Sections 1 and 5: relative projection constants, finite metric extension and linear programming; no evaluation of the six-point obtuse-isosceles family.
- *The sharp Euclidean triangle constant for barycentric Lipschitz-free \(p\)-interpolation* (publicly available 2026 mathematical result, `2026/10/11/SCOPE-the-sharp-euclidean-triangle-constant-for-barycentric-lipschitz--f5c526629bea`), RESULT.md: fixed affine interior retraction, not unrestricted discrete extension.

The finding is restricted to \(0<h\le1\), inherited planar Euclidean distances, and six sample points. The Banach-valued assertion is the upper bound for the displayed coefficientwise operator, not target-by-target minimum. Independent mathematical validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
