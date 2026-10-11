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

The octagon is represented by the eight exact inequalities
\[
n_j\cdot x\le1,
\]
with normals in \(\mathbb Q(\sqrt2)^2\). A centered affine-regular hexagon is encoded by three positive vertices
\[
u,\quad v,\quad v-u.
\]

The checker fixes \(u\) on one edge by dihedral symmetry. It then tries every edge for \(v\) and every active edge for \(v-u\). The active equality determines the edge parameter of \(v\) as an affine function of the parameter of \(u\); all remaining membership conditions are linear inequalities. Exact feasibility leaves three positive-determinant chambers and three reflected negative-determinant chambers.

On each feasible chamber the determinant is a quadratic in the remaining parameter. Exact endpoint and critical-point evaluation gives
\[
\min\lvert\det(u,v)\rvert=rac{2+3\sqrt2}{8},
\qquad
\max\lvert\det(u,v)\rvert=rac{3-\sqrt2}{2}.
\]
Multiplication by \(3\) gives the hexagon area extrema, and division by \(2\sqrt2\) gives the normalized values.

`verify.py` performs this finite symbolic calculation directly from the facet equations. No floating-point sampling is used to establish the theorem.
