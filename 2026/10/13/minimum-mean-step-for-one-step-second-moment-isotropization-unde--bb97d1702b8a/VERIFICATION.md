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

The exact claims follow from the midpoint rotation formula, its second complex harmonic, an explicit nonnegative rational-polynomial identity and the convex geometry of a unit-circle arc. `verify.py` independently rederives the displayed matrix and rational identities with symbolic algebra and verifies finite exact examples; run it with the dependency listed in `requirements.txt`.

The verification does not enumerate all probability laws or prove infinite-dimensional facts by simulation; the universal law-bound follows analytically by integration of an everywhere nonnegative expression. The endpoint \(H=0\) is allowed only in the nonnegative-duration formulation; strictly positive durations attain the sharp frontier only for larger means. The claim concerns second moments and phase dephasing, not full angular uniformity or trajectory-accuracy guarantees. No independent audit has been performed.
