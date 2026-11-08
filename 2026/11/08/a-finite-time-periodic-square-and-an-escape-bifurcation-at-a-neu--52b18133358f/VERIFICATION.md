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

The proof uses exact affine iterates, a four-coordinate criterion for entering the left half-plane, and a scalar exterior first-return map. No numerical result is used to infer a universal or infinite-time statement.

Execute `python3 verify.py` beside this file. The independent rational test loops in this package check 1,144 quarter-turn identities, 616 section return identities, 12,496 finite steps to the section or absorbing square, and 68 capture-count cases. The primitive period-three orbit and its exact separator formula are also tested.

The checker uses finite rational samples rather than an exhaustive census of all real starting points. Its floating-log ceiling comparisons tolerate one-unit numerical error at equality; the exact algebraic derivation in RESULT.md establishes the stated ceilings. Historical priority and independent scientific review remain outstanding.
