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

# Verification of the metric-ladder mean identity

Run `python3 verify_ladder_mean.py` with Python 3.9+ and no dependencies. This derives graph endpoint distances by BFS and exactly integrates four affine route lengths over edge-pair unit squares using rational polygon clipping. It checks both graph models and the three edge-category conditional means, total means and vertex means for every integer \(n\) from 3 to 18, as well as both mean gaps; 192 exact rational comparisons passed. The all-integer theorem is established by the symbolic geometric proof in `RESULT.md`; finite tests cannot prove universality.

No independent audit or specialist validation has been performed.
