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

# Reproducibility and verification

The file `verify_prism_sections.py` uses only the Python 3 standard library and runs directly with `python3 verify_prism_sections.py`. It constructs all original vertices and edges rather than using the closed-form two-orbit angle simplification to evaluate the independent angle sum. It also counts edge intersections by signs of dot products with reproducible isotropic Gaussian normals.

**Actual completed run from the bundled file path:**

```
VERIFY_OK formula_direct_angles=42 derivative_and_asymptotic_checks=294 monte_carlo_normals=260000 max_absolute_sampling_error=0.016526
golden_ratio_half_height=1.309016994374947, pentagon_peak=5.246274819729384, n6_asymptotic_coefficient=0.477464829275686
```

The 42 direct angle comparisons cover six polygon orders and seven heights. The derivative tests confirm the sign pattern around the uniquely determined pentagon optimum and positive finite-height derivatives for orders at least six. High-height comparisons check both the cubic six-gon coefficient and the linear formula for larger bases. The 260,000 normal samples span ten choices of base order and half-height, with a fixed pseudo-random seed. Their largest absolute sampling discrepancy was 0.016526, under the stated 0.045 tolerance.

**Scope of evidence.** Monte Carlo sampling, high-height numerical comparisons, and finite algebraic regressions cannot prove an identity for infinitely many prism orders or arbitrary positive real heights. The universal exactness, uniqueness, and asymptotic limits are established in the analytical proof in `RESULT.md`. No independent mathematical audit was performed, and the verification program makes no such claim.
