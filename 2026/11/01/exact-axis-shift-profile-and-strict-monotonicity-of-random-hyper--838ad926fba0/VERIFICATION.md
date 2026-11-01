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

# Reproduction and limits

Run `python check.py` (Python 3, standard library only). The checker evaluates the displayed formula, an independent sum of spherical endpoint angles over every cube edge, and an independent count of edge crossings using Gaussian normal vectors. It uses deterministic pseudorandom seeds and checks six Gaussian Monte Carlo benchmarks against analytic expectations, along with sampled monotonicity and uniform-scaling tests. The saved run reported `PASS 2477 deterministic checks; MC uses independent normal sign events.`

The deterministic parameter checks and finite Monte Carlo tolerances neither establish strict monotonicity for every real displacement nor prove the dimension limit. Those conclusions are analytically shown in `RESULT.md`, including the exceptional three-dimensional bound. There is no external, independent audit or certification.
