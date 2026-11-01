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

The analytical proof is given in `RESULT.md`. It relies only on explicit affine integration, positivity/monotonicity of barycentric coordinates, and a one-variable Taylor/implicit-branch analysis. The derivation proves the result for all specified parameters; the program below is an independent check rather than exhaustive evidence.

Run `python verify.py` with NumPy and SciPy available. The executable code compares the exact Lambert solution against `solve_ivp` on the **original two-dimensional affine mode**, using directional event detection of the outgoing vertex ray. It checks 864 combinations, 3 central startup regimes plus an additional admissible parameter family, and exact implicit identities over selected additional parameters. The recorded run produced a maximum observed absolute error of \(4.7336982150551735\cdot10^{-12}\) and no failed assertions. It does not simulate arbitrary discontinuous selections at switching boundaries.

Reproducibility scope: the original field, event condition, parameter samples, numerical tolerances, and all dependencies are defined in the included checker. A numerical ODE tolerance is not an error bound for the analytic theorem. There is no independent audit or external certification associated with this work.
