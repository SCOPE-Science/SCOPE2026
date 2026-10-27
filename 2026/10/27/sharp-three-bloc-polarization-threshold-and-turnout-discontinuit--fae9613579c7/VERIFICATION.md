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

The complete proof is in `RESULT.md`; the portable standalone checker is `verify.py` and requires Python 3 only. Run `python verify.py` in this directory.

The reference checker execution passed 13,750 exact-rational grid-policy equilibrium classifications over \(q\in\{1,2,3,4\}\), including threshold weights and the linear-cost continuum on its sampled grid; it also passed 189 exact convexity midpoint inequalities on auxiliary finite-support voter configurations. It verifies turnout formulas by exact arithmetic on tested cases.

The checker does not enumerate all real candidate positions, all real cost powers, or all voter weights, and cannot certify novelty or scientific priority. The mathematical proof independently covers these continuous domains. No independent scientific audit has been performed.
