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

The standalone file `check_simplex_moments.py` uses only Python's standard library. Run `python check_simplex_moments.py` to reproduce 52 numerical geometry checks at 70-digit Decimal precision (four deformation parameters in each dimension from two through fourteen), exact rational evaluations of the proposed sharp constant in dimensions two through four, and the strict negative upper-bound certificate for the explicit rational four-simplex. The checker printed `PASS: 52 dimension/scale cases, sharp constants, limiting approach, and an exact-rational four-dimensional negative-gap certificate`.

The universal proof is independent of finite enumeration: first compute uniform-simplex and facet second moments, then use the equilibrium of outer facet normals and Hilbert Cauchy–Schwarz, then construct a nondegenerate two-cluster family approaching the sharp coefficient. The negative witness uses rational upper and lower bounds without relying on a floating-point sign. Numerical cases test the formulas only and do not certify unseen dimensions. The proof and source comparison have had self-review only; independent review is not yet performed.
