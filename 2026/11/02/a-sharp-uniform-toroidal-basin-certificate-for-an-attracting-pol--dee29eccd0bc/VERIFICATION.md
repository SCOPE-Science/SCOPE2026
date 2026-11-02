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

# Reproducible checks

Run `python VERIFY.py` from the extracted package. The checker recomputes the two sharp boundary polynomials, both equilibrium values, the Jacobian trace and determinant, and the exact positive lower bound for the negative-divergence argument, using symbolic rational arithmetic. It checks an outward-pointing witness at width \(\delta=1/2\) for representative positive radial parameters; the proof covers all \(\delta>11/25\) symbolically.

The global convergence claim is an analytic application of positive invariance, a strictly negative divergence, and the Poincaré–Bendixson theorem. These arguments are not replaceable by numerical integrations or a finite checker. The originating source's full article remained inaccessible, so this package does not represent exhaustive historical priority review. Independent validation was not performed.
