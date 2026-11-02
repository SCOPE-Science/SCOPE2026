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

# Computational verification and limits

The included `verify_direct.py` calculates the boundary of every subset by explicitly testing every graph edge, then uses exact integer dynamic programming on optimal prefix chains to compute the number of optimizing orders. It runs for every integer \(4\le n\le9\); all six instances passed. In order of increasing \(n\), the optimizer counts were \(1024,5120,24576,114688,524288,2359296\).

The included independently structured `verify_structure.py` calculates the boundary by the cycle-run plus rung-crossing formula, checks the exact iff classification of four-boundary subsets for every interior even cardinality, and separately enumerates all twenty-four permutations of each terminal square to recover sixteen admissible orders. All six instances passed.

The mathematical all-parameter proof is in `RESULT.md`. The checks do not themselves prove infinitely many cases, establish historical novelty, or constitute an external audit. The only supplied status is the specified unperformed independent-audit marker.
