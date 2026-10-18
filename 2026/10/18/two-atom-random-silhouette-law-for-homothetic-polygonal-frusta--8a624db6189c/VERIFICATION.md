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

# Reproducibility and limits

Run `python check_shadow.py` with NumPy and SciPy installed. The bundled checker independently enumerates convex-hull vertices after applying the exact linear-equivalence shear, compares 20 analytic versus integral probability values, tests 2,250 randomly constructed nonregular polygon pairs, and checks 21,000 random spherical viewing directions in six regimes. Its verified output is `HOMOTHETIC_FRUSTUM_SHADOW_OK area_integrals=20 irregular_hulls=2250 monte_carlo=21000`.

The infinite-dimensional claim is analytical: tangent-ray hull combinatorics, Cauchy ratio Jacobian, and solid-angle integration. Numeric trials cannot establish exhaustive novelty or mathematical truth outside sampled inputs. Only the effective parameter is recovered and no sample stability or independent audit is claimed.
