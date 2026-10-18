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

# Reproducibility checks and limits
The included standard-library Python 3 program `verify_ps.py` exactly enumerates vertices by independent active-set Gaussian elimination over rational numbers, checks all claimed extremal values of defining linear forms, and checks reflected containment for every enumerated vertex in ten sample instances. It independently constructs an interior witness for every proposed center-dimension equality pattern. An executed run returned `ALL_VERIFY_OK cases=10 vertices=210 reflected-facet-checks=2376`.

The program is for bounded finite cases and cannot certify the analytic theorem for all positive real weights or all dimensions. The written proof supplies the non-computational justification and handles limiting boundaries by its strict positivity assumptions. Independent audit and independent validation have not been performed.
