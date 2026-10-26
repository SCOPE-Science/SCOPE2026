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

Execute `python3 check.py` with Python 3 and no third-party packages. The program computes the weighted law directly over every permutation for lengths two to seven with four rational biases and verifies independent-rank moment formulas and normalization with exact `Fraction` arithmetic. It also checks exact rational finite-size bounds against the limiting variance for five positive rational ratios and three large lengths each. The observed output for the embedded code was `PASS 376 exact assertions`.

The checker intentionally does not claim that finite enumeration proves Gaussian convergence. The proof of the limit uses explicit moment computations, Riemann sums, bounded one-dependence, independent blocks separated by discarded sites, and the Lindeberg–Feller theorem. Independent mathematical assessment has not been performed. The original introduction of the model and the exact expectation are credited to the cited primary sources.
