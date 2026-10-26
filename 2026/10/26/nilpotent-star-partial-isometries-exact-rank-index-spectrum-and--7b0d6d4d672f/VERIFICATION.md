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

Run `python verify_star_nilpotent.py` with Python 3 and the standard library. The verifier enumerates every partial injection on up to seven labeled star vertices, filters them by the pairwise shortest-path metric, computes nilpotency by direct powers, and compares joint domain-rank/index counts with an independent construction by unordered labeled sets of linear chains and the hub-exception formula. Results: all checks passed for \(m=1,2,3,4,5,6\); corresponding nilpotent totals are \(3,9,25,93,531,4093\).

An additional direct exact-coefficient recurrence check at \(m=100,500,2000\) gave CDF ratios at Gumbel coordinate \(s=0\) approximately \(0.28224,0.31375,0.33343\) respectively, approaching \(e^{-1}\). Such computations are finite and not a substitute for the local central limit and conditioning proof.

The standalone script has no external dependencies. The independent audit status is not performed.
