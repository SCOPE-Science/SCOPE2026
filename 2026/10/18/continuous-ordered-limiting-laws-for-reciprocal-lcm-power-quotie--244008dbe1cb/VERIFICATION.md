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

Exact rational checks compare the prime-square-difference identity against the average-of-endpoints formula for eight primes and eight exponents. Two independently coded rational calculations of the global normalized square quotient agree for all integers through 1200. The closed \(\kappa=2\) Euler factor is checked in rational arithmetic, and numerical finite-sample/truncated Euler-product means are compared (not used as proof).

Run `python3 verify.py` in the directory with this file. Expected terminal marker: `VERIFY_OK`.

The infinite weak convergence, non-atomicity, full support and parameter interpolation are proved mathematically in RESULT.md, not certified by finite tests. Only self-review has been performed.
