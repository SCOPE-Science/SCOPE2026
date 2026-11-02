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

# Reproducibility

Execute `python check.py` with Python 3.9 or newer. No internet, external corpus, packages, or randomized seed is needed. The checker visits all 65,536 state-switch rules and all 65,536 rooted traversals, recomputing two greedy parsings by direct sources and LCP dynamic programming; an independent 65,536-priority Euler-tour generation confirms all 2,048 necklaces. Its `VERIFY_OK` means all assertions about the exact tables passed, not that an independent scholarly audit occurred.

The full theorem is a finite exhaustiveness claim supported by the graph permutation parameterization and by exhaustive evaluation. No infinite or higher-order extrapolation is asserted. Exact outputs include all 24 positive joint cells, seven gain values and eight per-cycle gain ranges. The decoded standalone `joint.csv` independently permits checking each row sum and both marginal sums.
