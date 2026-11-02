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

The analytical proof establishes the claim for arbitrary common probability spaces. The standalone `verify.py` computes \(\chi^2\) from full tensor-product probabilities in rational arithmetic, verifies the scalar and geometric factorization identities on explicit two- and four-point experiments, and checks the stationary-point formula and the critical quadratic onset numerically.

Run `python3 verify.py` with Python 3 standard library. The reference result is in `verification_output.txt`. Finite tests are not substitutes for the universal proof; no independent validation has been performed.
