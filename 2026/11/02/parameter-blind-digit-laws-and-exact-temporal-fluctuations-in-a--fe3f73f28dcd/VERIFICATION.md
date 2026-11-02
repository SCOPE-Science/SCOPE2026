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

# Verification of exact six-cell symbolic statistics

The accompanying `verify.py` uses only Python's standard-library exact rational arithmetic. Run `python3 verify.py` from the directory containing this file and the program. It returns a PASS message after verifying all twelve affine branch images, six transition-matrix rows, stationarity of the cell distribution and density, the covariance recurrence, finite variance expressions through ninety-nine time steps, and the exact three-letter joint probability witness to non-Markovianity.

For the infinite statements, the proof derives the Markov property from conditional uniformity of each affine cylinder, proves the matrix identity \(P^2g=-Pg/3\), sums the resulting geometric covariance series exactly, and applies the standard finite-state irreducible aperiodic Markov-chain central limit theorem. A finite loop over lags is not being used to certify the all-lag formulas or an infinite-time limit.

Checks are specific to stationary initialization, the six-cell affine system and map switching with fixed independent probabilities \(p\in[0,1]\). Real-valued observation paths and statistical identifiability with additional measurements are not covered. Independent mathematical audit has not been performed.
