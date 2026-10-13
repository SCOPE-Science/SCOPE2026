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

Run `python verify.py` with a standard Python 3 interpreter in the directory containing that file. It enumerates every permutation for orders 1 through 8 and every next relative insertion for orders 1 through 6, using exact rational arithmetic. It checks the comparison-cost expectation, inversion first two moments, zero mixed covariance, reflection symmetry within each comparison-cost class, an explicit finite-dependence example at order 3, the external-gap identity, and the comparison martingale conditional expectation. The expected terminal message is `VERIFY_OK`.

The verification program is exhaustive only over the stated finite ranges. It neither samples nor certifies the infinite-dimensional limiting law or the nonlinear decorrelation bound. Those conclusions rely on the proof in `RESULT.md` and standard elementary martingale and Lindeberg arguments. No independent scientific audit has been conducted.
