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

The accompanying `verification.py` is self-contained (Python standard library only). Run `python verification.py`. It checks an exact rational \(2\times2\) witness with negative determinant \(-256\), matches the explicit critical timestep \(2\sqrt{7/15}/(1-\sqrt{7/15})\), and tests the predicted contractivity frontier on 1,364 randomized matrices across dimensions two to four. It also verifies numerical ratios approaching one for the predicted inverse-square angular cutoff. This is evidence for computations and representative cases, not an infinite proof. The exact all-dimensional proof is the Schur-complement argument in `RESULT.md`. No independent validation has been performed.
