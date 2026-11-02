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

Run `python verify.py` from the directory containing this document. Python 3 standard library only.

The program performs the following checks:

- All \(2536\) allowed approval-interval profiles for one through four agents, compared to **all** set partitions of those agents.
- \(5000\) deterministic-seed profiles of five through eight agents, each compared to exhaustive labeled set partitions.
- \(1250\) additional deterministic-seed profiles for nine, ten, eleven, twelve and fifteen agents, independently checked by enumeration of all flexible-type split counts, rather than by repeating the dynamic-programming recurrence.
- For every computed feasible instance, the returned minimum and maximum witness partitions are directly checked for disjointness, full coverage, approved group sizes and the claimed number of groups.

All these checks completed successfully under Python 3 in the scientific preparation. The included code can reproduce them. Finite tests do not certify the infinite-family theorem; the mathematical proof is in `RESULT.md`.

The complexity proof assumes word-RAM operations on \(O(\log n)\)-bit integers. Priority against all possible unpublished or differently named results is not verified. Independent audit: not yet performed.
