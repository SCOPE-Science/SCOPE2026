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

The analytic proof establishes the exact critical-point count for all sufficiently small positive intensity ratios. It verifies that differentiation of the expected richness leads to the stated signed numerator, and partitions the whole positive area axis into controlled early, crossover, intermediate, late, and tail regions. In particular, numerical root counts alone are not used to exclude additional far-tail extrema.

The accompanying independent standard-library Python script `verify.py` recomputes both derivative-numerator expressions, performs 2,000 deterministic randomized algebraic/derivative checks, and bisects both turning points for five rare-intensity settings. It checks convergence of the peak's rescaled location and height and the logarithmic minimum-scale approximation. Run with `python3 verify.py`.

The verification is confined to algebra, finite numerical consistency and an analytic proof; it provides neither independent expert audit nor a numerical value of the smallest admissible intensity contrast. Historical coverage of the original Coleman work remains incomplete.
