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

The analytic proof has three checkable steps: (1) the polygon-centroid numerator reduces to the two diagonal asymmetries; (2) the quadrilateral circumcenter of mass satisfies the two perpendicular-bisector dot-product equations; and (3) equality reduces to a two-by-two homogeneous linear system with determinant \(1-4\cos^2\theta\).

`verify.py` uses exact rational arithmetic to replay the centroid identity on multiple nondegenerate rational-direction instances, checks the determinant reduction, and verifies the exact non-parallelogram witness at \(\cos\theta=1/2\). It prints `VERIFY_OK` on success.

The script is supplemental: finitely many test instances are not a proof of the universal theorem. The universal step is the symbolic derivation written in `RESULT.md`. No claim is made for concave, crossed, zero-area, or higher-sided polygons.
