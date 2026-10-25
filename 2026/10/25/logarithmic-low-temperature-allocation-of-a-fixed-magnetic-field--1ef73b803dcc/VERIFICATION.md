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

The analytical proof derives the entire Gibbs concurrence function by explicit parity-block diagonalization and identifies every possible maximizing sequence through a compactness argument. The first-derivative stationarity equation supplies the logarithmic boundary-layer coefficient, while a uniform derivative bound handles the strictly subcritical regime.

The included executable `verify_fixed_budget.py` independently forms four-dimensional Gibbs matrices, uses the Wootters spin-flip matrix, and compares directly with the exact scalar formula. It additionally numerically optimizes the constrained scalar function across critical, subcritical and supercritical examples. The program uses NumPy and SciPy. Numerical sampling checks its stated finite cases and does not certify the infinite-parameter theorem. Historical priority has not been independently certified.
