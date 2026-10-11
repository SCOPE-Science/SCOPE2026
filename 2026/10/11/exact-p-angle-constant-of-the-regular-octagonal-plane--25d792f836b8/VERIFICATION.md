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

The proof uses the eight supporting linear functionals of the regular octagonal norm. By dihedral symmetry one boundary edge for the first unit vector is fixed, while the second unit vector ranges over all eight edges. For each pair of active support functionals, the feasible parameter region is a convex polygon in \([0,1]^2\).

On such a cell, \(a=N(x+y)\) and \(b=N(x-y)\) are affine. The required inequality is
\[
a^2+b^2-(\sqrt2-1)ab-4\le0.
\]
The quadratic form in \((a,b)\) is positive definite, hence its pullback to the cell is convex and its maximum is attained at a cell vertex. The bundled `verify.py` enumerates those vertices exactly in \(\mathbb Q(\sqrt2)\).

A successful replay prints `VERIFY_OK`, `feasible_cells 126`, and `checked_cell_vertices 176`. It also verifies exactly that the adjacent-vertex witness has \(a=2\), \(b=2(\sqrt2-1)\), and P-angle cosine \((\sqrt2-1)/2\).

The computation is finite and exhaustive for the stated octagonal plane. It does not certify any infinite family of regular polygons.
