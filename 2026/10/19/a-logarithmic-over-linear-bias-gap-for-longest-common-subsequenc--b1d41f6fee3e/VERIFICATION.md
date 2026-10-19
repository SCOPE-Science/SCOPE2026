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
# Verification of the reported bound

The argument does not depend on numerical calculations. To reproduce the finite cross-checks, run `python3 check_candidate.py` in an environment with Python 3 standard-library support. The script performs exhaustive exact-rational binary enumeration and an additional independent dynamic-programming computation of two-string LCS events. It verifies every assertion and records a series of finite-rate evaluations in `verification_output.txt`.

The literal numerical calculations use floating-point exponentials only for corroboration of the Laplace upper bound. The proof supplies the infinite statements: for every fixed \(\mathbf p\) with a unique maximal entry, the asymptotic upper coefficient and lower baseline hold for arbitrarily large \(d\). The checker does not claim exhaustive testing of all distributions or infinitely many string lengths.
