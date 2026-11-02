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

The mathematical statement is proved by the five steps in `RESULT.md`. The test program `checker.py` is Python-standard-library-only and independently compares exhaustive multi-bin allocation with the prefix criterion on all integer partitions of ground-set sizes from one to seventeen, for target budgets two through five. It also verifies small greedy capacity instances for target budgets two through six.

Replay by executing `python3 checker.py`. The expected terminal line is:

`ALL_CHECKS_OK compared_weight_multisets=4844 k_ranges=2..5 n_ranges=1..17`

All finite tests were executed on the packaged standalone source. No test enumerates arbitrary finite sizes. The proof, not the execution log, establishes the unbounded mathematical statement. Independent scholarly audit and independent validation have not been performed; potential historical-priority overlap remains possible.
