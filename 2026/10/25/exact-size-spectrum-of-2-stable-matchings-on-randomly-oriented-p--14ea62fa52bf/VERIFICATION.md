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
# Verification details

The universal claim follows from the blocking-rank reduction, an exact bijection to six-state closed walks, the matrix characteristic polynomial, and extraction of every even coefficient of the two-eigenvalue trace. It does not depend on experimental extrapolation.

The accompanying `verify_cycle_k2.py` was executed against its actual embedded source prior to packaging. It enumerates each preference profile and feasible matching independently for every labeled cycle with \(3\le n\le11\), recomputes rank improvements, and checks the exact size histogram. It also checks transfer traces at integer weights \(z\in\{0,1,2,3,7\}\) for exponents through \(16\). Results are in `checks.txt`. The finite tests are not proofs for \(n>11\); the symbolic argument is.

A symbolic determinant computation independently reproduced the factorization \(\lambda^4((\lambda-1)^2-4z)\). The first accessible official online-publication date for the primary source is 2026-08-25; an earlier undiscovered public version remains possible. No independent scientific audit has been performed.
