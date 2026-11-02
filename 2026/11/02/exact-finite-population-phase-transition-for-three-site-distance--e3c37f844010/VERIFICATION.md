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

The analytical proof is provided in `RESULT.md`. The exact-rational direct enumeration (`verification/check_three_sites.py`) independently evaluates report-pair probabilities and optimal costs, and tests the closed formula and bounds across thousands of multiplicity/gap configurations. A separate symbolic script (`verification/check_algebra.py`) checks the rational derivative signs and convexity algebra.

Run both scripts with Python 3. The symbolic script needs `sympy`; no other third-party library is needed. Finite testing is not an exhaustive verification of arbitrary population sizes or real gap ratios; the analytical proof supplies those quantifiers. Publication priority beyond the listed literature is not independently certified.
