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

The proof was checked at the level of slices, centers, compactness, and the final polygon geometry.

For a centrally symmetric body with center \((a,b)\), vertical slice lengths satisfy \(\lambda(2a-x)=\lambda(x)\). Steiner symmetrization about the \(x\)-axis therefore produces a body invariant under \((x,y)\mapsto(2a-x,-y)\), so its center is \((a,0)\). If the contained body is already symmetric about that axis, its centered slice remains contained after the same symmetrization. Repeating this on two nonparallel axes gives centers obtained by alternating orthogonal projections, hence converging to the axes' intersection.

All iterates stay inside a fixed centered disk by monotonicity of Steiner symmetrization. Blaschke selection supplies a Hausdorff-convergent subsequence, area is continuous for planar convex bodies under Hausdorff convergence, and central symmetry passes to the limit because the symmetry centers converge. These facts establish the centered minimizer without numerical approximation.

`verify.py` was executed from its packaged path. It constructs regular polygons for every \(3\le n\le101\), computes the convex hull after adjoining antipodes, and verifies the hull-vertex count and area ratio against the parity formula. It returned `VERIFY_OK`.

The finite checker is not used to infer the theorem for arbitrary \(n\) or arbitrary two-axis convex bodies; those claims are supplied by the symbolic proof.
