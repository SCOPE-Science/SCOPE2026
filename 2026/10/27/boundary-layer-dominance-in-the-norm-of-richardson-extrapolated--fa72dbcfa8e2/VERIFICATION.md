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

# Reproducibility

Execute `python check.py` (Python standard library only) alongside `RESULT.md`. Rational arithmetic enumerates all signed-node extremizers for degrees one through four at six rational inputs, verifies the finite total-variation formula, and bounds \(e^{-7/5}\), \(e^{-14/5}\), and \(e^{-28/5}\) by exact rational Taylor-series inequalities. It certifies \(1.395<G(7/5)<1.396\), checks the exact negative-mass support, and compares selected finite norms with the boundary and bulk predictions through degree 500.

The infinite limit assertions are analytic consequences of the local-limit and compactness arguments in `RESULT.md`; no finite enumeration, numerical computation, or checker execution independently certifies them. The full text of the 2022 reference was not available, and the Poisson maximizing parameter is not claimed unique.
