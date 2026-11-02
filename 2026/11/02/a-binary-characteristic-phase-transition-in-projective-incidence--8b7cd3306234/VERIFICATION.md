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

The bundled `verify_projective_incidence.py` uses Python 3 standard library only. Run `python verify_projective_incidence.py`. It checks eight explicit prime-field point–hyperplane graphs, all their incidence intersections and shortest-path distances, direct powered-distance eigenvector identities, spectral signs below and above the critical exponent, and exact elementary integer inequalities. Expected terminal marker: `PROJECTIVE_INCIDENCE_NEGATIVE_TYPE_PHASE_OK`. Exact theoretical coverage of all prime powers and every dimension comes from the algebraic and analytic argument in RESULT.md; this finite checker does not prove the universal quantifiers. An independent mathematical audit has not been performed.
