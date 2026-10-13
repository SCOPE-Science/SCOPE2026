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

Run `python3 CHECK.py` in a directory containing this file and `CHECK.py`. The checker requires Python 3 only, uses exact `fractions.Fraction` arithmetic for the generating polynomial recurrences through sixty vertices, and independently enumerates every uniform recursive tree of orders one through nine by all allowable parent assignments. It compares the entire mixed covariance coefficient vector, checks the root–leaf finite formula for sizes at least two, and confirms covariance conservation at \(z=1\). The replay prints the count of exact equality checks on success. These computations do not certify the infinite analytic limit, which is proved by the recursion and disk-product bound in RESULT.md. Independent scientific audit has not been performed.
