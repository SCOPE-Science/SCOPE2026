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

The included `verify.py` is standalone source for bounded numerical diagnostics. Run `python verify.py` with NumPy and SciPy available. It reconstructs pure-gas and condensed branch densities separately using the principal Lambert function, compares the full absolute-density integral with the exact total-variation formula, checks profile sign order across the interface, differentiates numerically against the analytic derivative, and tests the upper-fold expansion coefficient. In its recorded execution it reported 2,180 checks passed.

The proof in `RESULT.md` is the basis for the global assertion. Tests of finite grids cannot establish infinitely quantified monotonicity, uniqueness, optimality, or asymptotic statements. The exact source model and normalization, all quantified parameter ranges, and the numerical examples are stated in `RESULT.md`. No independent external mathematical audit, publication-priority certification, or microscopic particle simulation is claimed.
