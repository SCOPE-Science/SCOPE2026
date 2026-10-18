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

# Reproducible checks

The exact integer/fraction checker `verify.py` was executed from the package staging directory. It reported: `PASS: 12192 exact complete ring update/reconstruction tests; 2 exact local-covariance regimes.` The program uses no third-party package. It checks all binary initial states for each ring size 5 through 11 at three exact rational interaction strengths, the complete trajectory assertions through time five, the run-based periodicity and final-support classification, total biomass changes, all finite-ring means and second moments, oscillator counts, and the 3-, 4-, and 5-bit local covariance identities.

The program covers a finite test range. Exact results for every size at least five follow instead from the local-sign and run-decomposition argument, covariance locality, and standard finite-dependent central limit theory detailed in `RESULT.md`. No independent scientific audit was performed.
