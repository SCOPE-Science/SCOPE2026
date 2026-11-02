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

# Verification record

The work-noise identities were checked by substitution into the two-state generator and by independently computing the predictable martingale bracket. Under stationary initialization, the corrected martingale covariance is exactly linear in observation time; a separate covariance-limit argument transfers the rate to physical work. The long-time vector normal limit is derived from ergodic bracket convergence, bounded switching jumps, and square-integrable boundary corrections.

Run `python checker.py` in the same directory to verify the exact generator–corrector and jump cancellation identities, the second-moment equations, all entries of the heterogenous-particle covariance matrix with rational parameters, the identical-particle aggregation algebra, and seeded direct trajectory simulation using exact Gaussian segment transitions. The numerical check uses 18,000 sample paths over time 350 with three unequal particles and switching rate 1.5; its tolerance is a statistical diagnostic only.

No numerical sample can certify the infinite-time theorem. Publication-priority review remains non-exhaustive; no independent validation is claimed. The stated Gaussian central limit theorem requires ergodicity and finite stationary fourth moments, supplied by the on/off random affine cycle contraction argument in `RESULT.md`.
