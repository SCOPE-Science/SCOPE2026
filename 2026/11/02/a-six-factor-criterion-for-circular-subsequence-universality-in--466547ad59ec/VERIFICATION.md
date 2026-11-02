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

Run `python checker.py` with Python 3.9+ and no external packages. The final line must read `CHECKS_PASSED`. The script exhausts all 65,536 Boolean feedback functions on four-bit suffixes, reconstructs and verifies all 2,048 binary de Bruijn cycles of order five, and independently enumerates them using Eulerian circuits. It checks the 32 rotation indices per cycle with both greedy binary-arch factorization and distinct-subsequence dynamic programming. All counts are exact integer counts.

## Interpretation and limits

The complete finite proof is explained in `RESULT.md`: the feedback-table parametrization is bijective, both subsequence methods characterize the stated invariant, and the alternating two-state obstruction excludes simultaneous alternating factors. The executable certificate establishes the remaining finite tabulation. No full formal-verification implementation or independent human audit is claimed. The result makes no claim about higher de Bruijn orders or windows traversing more than one complete cycle.
