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

The analytic proof in `RESULT.md` is primary. `verify.py` numerically evaluates the exact integral at \(\alpha=0.05\), \(n=100\), \(\rho=0.1\), checks the \(\kappa=1\) local-limit constant, checks the \(n=1\) boundary numerically, and verifies the omitted-direction covariance identity on a positive-definite example. Successful replay prints `VERIFY_OK`.

These computations do not replace the infinite-family proof. No finite Monte Carlo budget, learned nuisance model, non-Gaussian extension, or vector-valued extension is claimed.
