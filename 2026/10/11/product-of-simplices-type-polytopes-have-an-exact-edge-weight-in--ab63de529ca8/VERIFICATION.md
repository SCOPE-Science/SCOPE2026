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
The arbitrary-factor proof is given in `RESULT.md`.

Critical checks:
- every product edge varies in exactly one simplex factor;
- triangular and square two-face balancing propagates one common weight \(\lambda_i\) through every factor-\(i\) edge;
- the number of factor-\(i\) edge coordinates is
  \[
  E_i=\frac{Vd_i}{2};
  \]
- the normalization is therefore
  \[
  \sum_i d_i\lambda_i=D;
  \]
- \(y_i=\sqrt{E_i}\lambda_i\) is an exact Euclidean isometry on the class-constant subspace;
- the affine normal in \(y\)-coordinates is \((\sqrt{d_i})\), whose squared norm is \(D\);
- the intrinsic distance to facet \(i\) is
  \[
  y_i\sqrt{\frac D{D-d_i}};
  \]
- equalizing all facet distances gives
  \[
  \lambda_i^*
  =
  \frac{D}{S}\sqrt{\frac{D-d_i}{d_i}}
  \]
  and
  \[
  r_{\mathrm{in}}
  =
  \frac{D^{3/2}\sqrt{V/2}}{S};
  \]
- the pure-factor vertices have pairwise squared distances
  \[
  \frac{VD^2}{2}
  \left(\frac1{d_i}+\frac1{d_j}\right).
  \]
For two factors the type simplex is a segment. For at least three factors, the pairwise-distance formula proves regularity exactly when all factor dimensions are equal.

`verify.py` checks deterministic factor-dimension vectors by explicitly building the reduced edge-coordinate simplex, computing projected facet normals, checking all tangent distances, verifying the vertex-distance and regularity formulas, and independently solving the max-min facet-clearance problem by linear programming. Finite computation is corroborative only and does not assess originality.
