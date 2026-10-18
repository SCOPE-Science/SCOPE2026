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
# Reproducibility and scope

Run `python verify_cycle_sentinels.py` using Python 3 standard-library modules only. The program makes no network requests, uses exact rational arithmetic and exhaustively evaluates every finite cycle \(3\le n\le9\), every fixed number of failed edges, every sentinel budget and every deployment. For each deployment, it separately forms all surviving-edge connected components for each failure set and computes the total probability that a uniformly random source has no sentinel in its component. This is compared against the independently written binomial gap formula and optimizer criterion. The run produced 9,151 matching formula-and-optimizer comparisons. It also checked the closed curvature formula for selected larger instances and reproduced the \((n,m,k)=(10,8,2)\) values.

The infinite quantification is supplied by the exact second-difference calculation and exchange proof in `RESULT.md`. Enumeration up to nine vertices is not presented as an infinite proof. Independent scientific verification and independent bibliographic audit have not been performed.
