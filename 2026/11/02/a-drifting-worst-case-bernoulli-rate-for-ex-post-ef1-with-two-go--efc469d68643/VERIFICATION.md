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

Run `python3 verify.py` using only Python 3's standard library. The complete exact checker enumerates independent Bernoulli utility outcomes per participant for sizes 2–6, and additionally enumerates all utility matrices for several two- and three-participant cases. It checks the exact rational formula, the derivative sign change and monotonicity numerically for sizes up to 200, and tests the logarithmic location approximation at sizes up to 100000. Its finite checks do not stand in for the infinite proof given in RESULT.md. Independent audit has not been performed.
