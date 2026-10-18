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

# Direct numerical checks and analytic limits

From the same directory run `python verify_design.py` with NumPy and SciPy installed. The program constructs the unnormalized real nine-by-nine Gaussian coherent-intensity measurement matrix with an orthonormal real Hilbert–Schmidt input basis. It independently compares the directly calculated determinant to the exact formula for five ordered-radius triples and eight random angle triples each; verifies one hundred independent real Hermitian coordinate reconstructions at the computed optimal design; checks one hundred twenty angle comparisons against the exact aligned and staggered extrema; tests eighty random radius competitors; and solves the stationary equations numerically to check the exact sum-of-squares identity.

The verification code is finite diagnostic evidence. Universal invertibility for every orientation, equality classification, strict log-concavity, the unique global radius optimizer, and the exact radius identity are proved analytically in `RESULT.md` and are not inferred from these finite checks. The numerical optimum is rounded; no interval-certified digit count is claimed. The source inspection and novelty comparison involve manuscript-level evidence and remain subject to independent historical-priority assessment.
