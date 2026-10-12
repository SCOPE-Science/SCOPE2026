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

The infinite statement is proved in `RESULT.md`. The executable check is a finite regression test and is not used as a substitute for the proof.

`verify.py` enumerates all derangements for \(3\le n\le8\). For each selected subset of matching edges it directly counts how many derangements extend those selected edges. It then compares that direct uniqueness test with the claimed structural rule, checks the fixed-matching enumerator \(x^n+n x^{n-1}+(n-t_2(\pi))x^{n-2}\), and checks the aggregate coefficient \(n d_n-\binom n2 d_{n-2}\).

Observed replay output:

`VERIFY_OK n_range=3..8 subset_checks=4053088 matching_checks=17007 aggregate_checks=6 cycle_type_checks=17007 max_order=16`

The verified finite range is only \(3\le n\le8\). No finite run is treated as evidence for all \(n\); the general proof supplies that step.
