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

# Reproducibility checks

Run the included Python-standard-library program as `python3 verify.py`. It evaluates the centered spline with exact `fractions.Fraction`, checks the half-frequency Zak rescaling on a rational parameter-and-position mesh, checks positivity of the related difference and rescaled half-frequency fiber, and verifies horizontal zero segments on a grid just below the sharp threshold. Finite complex trigonometric samples additionally check the interior-frequency imaginary-part sign.

The submitted checker was actually executed against the included program before packaging and returned `VERIFY_OK 37564 exact and supplementary numeric comparisons; distinct-boundary and zero-segment tests`. The proof in `RESULT.md` verifies the theorem without depending on finite samples, floats, or code extrapolation. No external mathematical certification or independent audit was performed.
