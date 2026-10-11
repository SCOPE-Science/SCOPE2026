---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The analytic reduction shows that equality for a principal-plane reflection of a three-dimensional parallelotope can occur only when its unit normal has, up to permutation, one of the two squared-coordinate patterns
\[
\left(
\frac{3+\sqrt3}{6},
\frac{3-\sqrt3}{12},
\frac{3-\sqrt3}{12}
\right)
\]
or
\[
\left(
\frac{3-\sqrt3}{6},
\frac{3+\sqrt3}{12},
\frac{3+\sqrt3}{12}
\right).
\]

The bundled exact checker constructs every signed and permuted vector of these two types using symbolic algebraic numbers. It verifies that there are \(48\) such signed vectors, \(48\) orthogonal unordered pairs, and no orthogonal triple. More strongly, every orthogonal pair has one vector of each type with the same distinguished coordinate, and the squared-coordinate multiset of its cross product is exactly
\[
\{0,1/2,1/2\}.
\]

This finite enumeration is exhaustive because the preceding analytic argument has already classified every equality normal into those two finite signed-permutation families. It is not numerical sampling and is not used to infer anything outside that equality locus.

The other inputs are published theorems: the Minkowski-chirality Banach--Mazur upper bound, complementary-dimension equality and polarity invariance from the primary source, and the three-dimensional Banach--Mazur equality classification from Grundbacher--Kobos.

No uniform quantitative gap below \(\sqrt3\) is verified or claimed.
