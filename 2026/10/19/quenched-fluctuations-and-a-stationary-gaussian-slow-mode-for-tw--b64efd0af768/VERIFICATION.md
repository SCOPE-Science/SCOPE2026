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

Run `python3 verify.py` alongside the mathematical result. The standalone script checks exact rational one-step matrix reductions and stationary moment recurrences for three explicit finite environment distributions and three leakage parameters, including a nonconstant-coefficient case and a nonfluctuating case. It also checks finite approximations to the slow-time limiting covariance. The completed program's numerical counter is printed by the script.

The infinite-horizon existence/uniqueness and finite-dimensional Gaussian convergence are **proved analytically** from uniform contraction, an exact \(L^2\) comparison with a deterministic-coefficient autoregression, and the Lindeberg–Feller theorem. The finite examples do not certify generality or uniqueness. The result does not make claims about the original interval map or any independent audit.
