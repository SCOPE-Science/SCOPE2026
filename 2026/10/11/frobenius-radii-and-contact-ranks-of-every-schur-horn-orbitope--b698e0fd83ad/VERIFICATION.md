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
The arbitrary-dimensional theorem is proved symbolically in `RESULT.md`; finite computation is not used to infer it.

The critical checks are:
- The complete Schur-Horn inequalities are the rank-\(k\) partial-eigenvalue bounds.
- A rank-\(k\) projection has traceless tangent normal \(P_L-(k/d)I\) with squared Frobenius norm \(k(d-k)/d\).
- The Ky Fan variational principle converts all subspace inequalities for a center \(C\) into the ordered-eigenvalue inequalities in the complete incenter formula.
- Orthogonal averaging preserves feasibility of a fixed-radius center and sends every center to the scalar trace center.
- Every orthogonal-orbit extreme point lies at the same centered Frobenius distance, and strict convexity excludes non-extreme convex combinations from the outer sphere.

The accompanying `verify.py` checks exact rational squared-distance formulas for many integer spectra, enumerates permutation vertices for the corresponding permutahedra, and confirms the standard-spectrum closed forms through dimension \(12\). These checks are corroborative only and do not assess originality.
