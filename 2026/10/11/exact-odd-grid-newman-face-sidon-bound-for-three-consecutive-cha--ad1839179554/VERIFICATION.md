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

The proof is analytic. The key all-modulus checks are: the quartic derivative is positive for \(R>0\); the root lies below \(\sqrt{T/D}\), making the convex weight lie strictly between zero and one; the weighted two-sample quadratic has positive-definite Hessian; and its stationarity equations are exactly the balancing relation and the quartic equation.

`artifacts/verify.py` is a corroborative replay. For every odd \(N\) from \(5\) through \(1001\), it reconstructs the root and extremizer, evaluates every sampled grid point, verifies the convex weight and stationarity, and tests forty deterministic pseudorandom competitors on the same sign face. Its recorded output is:

`VERIFY_OK odd_N=5..1001 random_per_N=40 asymptotic_tail_maxerr=6.699e-06`

The pseudorandom tests are regression checks only; they do not establish the infinite theorem or exclude phases outside the stated sign face.
