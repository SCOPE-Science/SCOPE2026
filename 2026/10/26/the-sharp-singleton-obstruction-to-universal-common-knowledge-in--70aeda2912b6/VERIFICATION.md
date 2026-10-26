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

The included `verify.py` enumerates all partitions via restricted-growth strings, computes the join by union–find, and counts connected ordered tuples for agent counts 2 and 3 and world sizes 1 through 5. It separately generates Bell numbers and the exact connected-component recurrence, then asserts that the independent methods agree. No random sampling is used in those assertions. It prints `PARTITION_JOIN_CHECK_OK` only after all equalities pass. The displayed finite probability-to-first-moment ratios are exploratory finite sanity checks, not asymptotic certification. The analytic proof invokes the published Bell-number ratio asymptotic and controls the full non-singleton component-size range, which finite tests cannot certify.
