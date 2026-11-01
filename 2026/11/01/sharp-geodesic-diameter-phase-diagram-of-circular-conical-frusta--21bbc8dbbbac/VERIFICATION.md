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

## Proof checks

The statement explicitly restricts to an annular right circular conical lateral surface with two boundary circles and no disks. The intrinsic metric is reduced to a developed annular strip with angular period \(2\phi\). For two points the minimum winding is justified by angular contraction, and the shortest path in the punctured planar disk is either an admissible chord or two tangents plus an arc of the inner boundary. Both distance expressions and their first radial derivatives match exactly at tangency. The radial second derivatives are strictly positive on each branch, establishing radial endpoint maximization. The inner–inner corner is inferior to outer–inner, and the final outer–inner versus outer–outer comparison is explicit algebra. The two singularity-derivative statements and cone/cylinder limits have been independently recomputed from the displayed formula during the self-review.

## Reproducible computations

Run `python3 frustum_diameter_checker.py` with standard Python 3 (no third-party libraries). Observed output:

```
OK cases=270, sampled_pairs=810000, max_positive_violation=0, max_contact_error=5.83e-16
OK radial_grid_cases=20, radial_grid_points_per_case=8281
```

These samples and finite grids do not constitute a universal proof and do not verify historical priority. Numerical discrepancies reflect ordinary double-precision rounding. The full proof is contained in RESULT.md and does not depend on code.

## Scope and integrity

No claims are made about a frustum with planar end caps, arbitrary smooth surfaces of revolution, oblique cones, or any independent mathematical audit. The cited 1987 paper was considered from its publisher abstract only, not its full text. Historical priority therefore remains open to independent examination.
