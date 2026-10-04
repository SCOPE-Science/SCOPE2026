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

The proof has four independently checkable components.

First, Jahn--Winter's published criterion implies that an obstruction in dimension seven has a face \\(F\\) and dual face \\(F^\\Delta\\) each with strictly more vertices than facets. Since
\[
\dim F+\dim F^\Delta=6
\]
and dimensions at most two have equal vertex and facet counts, both are three-dimensional.

Second, for every three-polytope,
\[
2e\ge3v,
\qquad
v-e+f=2.
\]
Therefore a three-polytope with \\(v\\le5\\) satisfies \\(f\\ge v\\), so strict vertex excess requires at least six vertices.

Third, a three-face of a seven-polytope needs at least four vertices outside it. If there are exactly four, equality in affine dimension forces the ambient polytope to be the free join of the face with a tetrahedron. Exactly four ambient facets then contain that face, contradicting the at-least-six vertices of its dual face.

Fourth, the triangular prism and triangular bipyramid have vertex/facet counts \\((6,5)\\) and \\((5,6)\\). Their free join has dimension seven and counts \\((11,11)\\); its prism factor contributes the exact criterion violation
\[
6+6>11.
\]

The embedded `verify.py` replays the finite arithmetic and prints:

`VERIFY_OK sharp d7 vertex-facet obstruction threshold`

The checker does not certify the general affine lemma by enumeration; that lemma is proved in the accompanying result text.
