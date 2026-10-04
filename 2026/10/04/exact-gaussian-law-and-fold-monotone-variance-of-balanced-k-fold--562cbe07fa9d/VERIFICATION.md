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

`verify.py` uses Python standard-library exact rational arithmetic. It checks the deterministic K-fold decomposition for many balanced \(n,K\) pairs on deterministic rational data, the expectation and variance coefficient identities, the derivative identity and positivity argument for strict monotonicity, the leave-one-out reduction, and the residual covariance formulas. A successful run prints `VERIFY_OK`.

The independent-chi-square step is the standard Gaussian one-way ANOVA orthogonal decomposition and is not inferred from finite simulation. The verification therefore separates an externally standard probabilistic lemma from algebraic identities replayed in the package.

The result is limited to iid Gaussian observations, balanced folds, the sample-mean predictor, squared loss, and the natural training-size target associated with each fold count.
