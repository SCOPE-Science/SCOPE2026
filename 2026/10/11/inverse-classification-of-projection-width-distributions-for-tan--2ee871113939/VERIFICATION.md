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

# Verification record

The theorem was checked analytically by reconstructing the tangent-line vertex formula, deriving its support cone and integration intervals, differentiating the width-survival law, and analyzing the complete set of one-sided density singularities. Distinct threshold values determine the normal gaps by the strict monotonicity of the secant; positive square-root coefficients determine multiplicities; the essential lower width endpoint determines scale. Congruence follows from cyclic or reversed order of outward tangent normals. These arguments are exact for every integer \(m\ge2\) and positive normal gaps with half-cycle sum \(\pi\).

The reproducibility script `verification/check_width_spectrum.py` was executed with Python 3 and NumPy. It constructs vertices directly as tangent-line intersections, computes polygon widths independently by direct vertex support maximization, and compares area, perimeter, the lower and upper support bounds, and the analytic survival law on deterministic angular grids. Ten polygon configurations were covered, including generic, repeated-gap, and distinct-gap octagonal examples. The actual output was:

```
VERIFY_OK: 300 independent area/perimeter/support/CDF checks
```

The numerical grid is finite, so it does not certify the infinite theorem or reconstruction uniqueness. Equality of width distributions in the octagon example is established analytically from the same unordered gap data; the numerical exercise only checks consistency. Reproduce with `python verification/check_width_spectrum.py`. No external data files or unpublished computations are required.

All comparisons with earlier geometry literature are documented separately; lack of a matching search result is not an independent originality certification. Independent audit remains not performed.
