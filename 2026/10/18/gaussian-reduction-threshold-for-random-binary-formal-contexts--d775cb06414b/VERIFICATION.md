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

The command `python3 verify_reduction.py` performs three-way exact-rational checks of the new formula: brute-force incidence-table enumeration, conditional-binomial enumeration, and inclusion–exclusion. All 33 tested rational-parameter cases agreed. The one-column boundary was separately checked. The program prints `VERIFY_OK` on success.

The asymptotic Gaussian profile is verified by the analytical Chernoff/union-bound sandwich and the binomial central limit theorem presented in the result; finite code tests alone do not verify an infinite limit. Simultaneous deletion and non-i.i.d. contexts are outside scope.
