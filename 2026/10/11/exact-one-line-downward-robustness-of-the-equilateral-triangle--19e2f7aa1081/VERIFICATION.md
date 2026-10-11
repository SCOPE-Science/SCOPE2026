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
The proof was reconstructed from the source definitions of polygonal equilibrium and full robustness, together with its explicit proposal to restrict truncations to straight lines.

Actual checks performed:
- The equilateral triangle was normalized to \(A=(0,\sqrt3)\), \(B=(-1,0)\), and \(C=(1,0)\).
- Centroids of both possible retained pieces were computed by exact area-weighted formulas.
- Every side-equilibrium projection parameter was derived symbolically and reduced to the displayed rational functions.
- The polynomial identities controlling the cut side and the endpoint factorizations were replayed exactly.
- The symmetric threshold was substituted exactly, giving projection parameters \(1/2,1,1/2,0\) around the retained trapezoid.
- `verify.py` completed with `VERIFY_OK`.

The rational-grid stress test in `verify.py` is not used as proof. The proof covers all proper cuts by the two-parameter reduction and exact inequalities.

Scientific limit: the value is for the single-straight-line reduced model and is an infimum because the threshold body has degenerate equilibria. No claim is made about unrestricted full robustness or regular polygons with more sides.
