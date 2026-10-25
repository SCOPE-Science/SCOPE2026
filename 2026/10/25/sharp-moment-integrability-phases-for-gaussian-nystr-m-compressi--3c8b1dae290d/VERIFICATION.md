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

# Reproducibility and evidence

Run `python3 verify.py` using Python 3 and only the standard library. The file contains the exact rational matrix and polynomial calculations and reproducible finite numerical tail checks. Its successful output is:

`VERIFY_OK 252 exact rational and asymptotic checks; independent-tail constant 0.00886391953524`

The code checks the Taylor matrix representation for integer degrees through nine, determinant polynomial expansions and their leading signs through degree fourteen, exact rank-one sketch residual formulas on rational test vectors, asymptotic angular tails for four indefinite RK/Taylor endpoints, and the independent Gaussian angular tail for a positive-definite RK4 endpoint.

The analytical proof in RESULT.md establishes the universal claims independently of the finite tests. Floating-point tail comparisons are diagnostic and cannot certify tail limits or infinite moments. No external independent audit or validation has been performed.
