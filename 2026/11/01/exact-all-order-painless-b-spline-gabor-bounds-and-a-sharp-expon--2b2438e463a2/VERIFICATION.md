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

# Reproducible checks
Run `python CHECK.py` using Python 3 and the standard library. The checker independently evaluates finite rational B-spline values by the truncated-power formula, sums periodic squares, tests strict monotonicity at 32 rational points for each order 2 through 12, and checks exact reflection and partition-of-unity equalities. It also checks a finite collection of the exact partial-fraction identities at orders 2 through 10, the explicit endpoint fractions for orders 2 through 6, and numerical scaling for four larger orders. The extracted checker reported `CHECK_OK assertions=1211`.

These verifications establish exact identities only for the finitely tested inputs. The all-order extrema and large-order sharp asymptotic are proved by the analytic Fourier/Laplace argument in `RESULT.md`; the checker does not constitute an infinite certificate. No independently performed audit is claimed.
