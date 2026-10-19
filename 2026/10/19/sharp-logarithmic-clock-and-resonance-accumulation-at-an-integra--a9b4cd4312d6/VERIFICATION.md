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

# Reproduction and limitations

Run `python verify.py` (requires SymPy and SciPy). The program verifies three symbolic identities for the separatrix and the algebraic Poincaré–Lindstedt coefficient. It numerically checks the exact turning-point quadrature against the proposed logarithmic asymptotic at four sample values of \(\gamma\).

The analytical result is supported by the explicit oscillator conjugacy, elementary matched-integral limit, analytic center expansion and period-continuity argument in `RESULT.md`. Sample calculations cannot certify asymptotics for all parameters, and the script does not test global period monotonicity or novelty. Full-text comparisons for two older papers on Hopf–Langford integrability and invariant ellipsoids remain unavailable; an independent audit has not been conducted.
