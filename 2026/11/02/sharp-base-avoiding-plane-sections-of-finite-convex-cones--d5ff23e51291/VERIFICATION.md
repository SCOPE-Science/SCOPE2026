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
# Verification scope

Run `python check_cone.py` with Python 3, NumPy and SciPy. The numerical checker evaluates the analytic base-avoiding probability for multiple base types and heights, compares it to joint normal/offset Monte Carlo under motion-invariant plane measure, and probes four rectangle-width/height crossover parameters. Its tested assertions completed successfully on the recorded implementation. The proof for all convex bases, strict equality cases, and all-height asymptotics is in `RESULT.md`; finite sampling or quadrature cannot certify their universal quantifiers. This verification is an internal self-review, not an independent mathematical audit.
