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

## Reproduction

Run `python verification/verify.py` in the package root, using Python 3 standard library only. The checker reconstructs pair images independently from the definition, compares the proposed ranks with a reverse-BFS computation for orders 2 through 35, checks all local transitions through order 80, and verifies the complete common master path and all suffixes through order 80. The actual output is embedded in `verification/verify_output.txt`. There were 433,740 finite assertions and a `VERIFY_OK` result.

## Scope and limits

These are finite, independently implemented computations. The infinite theorem is supplied by the symbolic rank-decrease and rank-counting arguments in RESULT.md. They do not constitute exhaustive publication-priority verification, independent mathematical audit, or a statement about all automata.
