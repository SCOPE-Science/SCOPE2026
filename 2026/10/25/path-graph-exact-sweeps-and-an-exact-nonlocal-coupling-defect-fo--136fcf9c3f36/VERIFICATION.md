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
Run `python verification_checker.py` under Python 3 with NumPy and SymPy installed. The script includes the one-predecessor projection rule, symmetrized positive definite Gram matrices, and exact line searches. Scaling each singleton sketch by the square root of the diagonal Gram entry does not change any nonzero normalized direction or line-search result.

The checker passed symbolic identities for the three-coordinate basis, exact rational updates for a normalized long-range-coupling witness, 2,000 independent random three-coordinate tests of the exact residual ratio, and 600 independent positive-definite tridiagonal matrix tests of complete one-pass exactness in dimensions three, four, five, and seven.

The proof, rather than these finite tests, establishes the general graph characterization. Numerical experiments cannot certify every dimension, exceptional branch, or floating-point implementation. No external independent audit was conducted.
