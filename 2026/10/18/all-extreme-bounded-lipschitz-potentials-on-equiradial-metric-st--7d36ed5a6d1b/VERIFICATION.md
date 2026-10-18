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

The standalone script `verify.py` uses exact rational row reduction on all inequality-active combinations for \(m\in\{1,2,3\}\) at specified positive rational radii, then matches the computed vertices to the analytic families. It also independently checks the closed dual norm against complete enumeration of those displayed sign families for 1,500 rational sample measures.

With optional NumPy and SciPy installed, direct halfspace-intersection and linear-program computations cover 18 parameter pairs (two to seven leaves and three radii each); 288 unrelated sample coefficient vectors give the same optima every computed hull matches the predicted vertices, and facet ranks agree for all sampled stars. The script prints the observed counts.

Execute `python verify.py`. Install NumPy and SciPy for optional numerical checks; the exact rational checks require only the Python standard library. All tests were replayed from the included script in its actual package working path and passed.

These finite tests verify examples and implementation consistency, not the theorem's universal quantifiers. The proof in `RESULT.md` is elementary, uses exact finite-dimensional active-constraint rank arguments, and does not require experimental inference. No computer proof assistant or external certification is claimed.
