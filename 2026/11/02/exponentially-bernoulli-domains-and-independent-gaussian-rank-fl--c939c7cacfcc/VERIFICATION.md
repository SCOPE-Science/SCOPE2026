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

# Mathematical verification

The companion `verify.py` enumerates finite partial functions directly, tests both cyclic orientation preservation and idempotence, groups their domain and image ranks, and compares the result with a wholly separate integer combinatorial coefficient formula. Its second independent test uses an integral recurrence for the rank polynomial, and checks the binomial transform through size 50.

Run from this package directory with `python3 verify.py`. Observed result: `VERIFY_OK: 56 enumeration and exact polynomial checks`.

The asymptotic domain law is justified by exact comparison of subset weights and a uniform exponentially decaying bound. The multivariate Gaussian limits are justified by uniform local analytic dominance and differentiation of the leading logarithmic moment-generating function. Finite enumeration does not establish an asymptotic theorem or novel publication priority.
