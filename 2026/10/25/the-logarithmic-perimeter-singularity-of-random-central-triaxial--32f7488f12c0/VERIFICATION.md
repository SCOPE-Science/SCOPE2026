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

The calculation relies on the exact spectral Cauchy-perimeter formula, the classification of stationary normals, principal-axis second derivatives, and a normalized Morse/coarea pushforward. Those steps are proved in RESULT.md. The accompanying Python diagnostic recomputes cross-section perimeters both from invariant coefficients and by explicit plane compression and tests three separated axis triples. It also checks the predicted Hessian signs, coefficients, and support ranges.

A separate twelve-million-orientation random-direction experiment compared density increments across logarithmically separated bins and returned slopes approximately 0.064–0.068 for the expected 0.067301639 on axes (3,2,1). Monte Carlo fluctuation remains and such experiments do not establish the theorem. Independent mathematical validation has not been performed.
