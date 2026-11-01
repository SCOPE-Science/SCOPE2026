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

# Reproducibility and proof limits

Run `python verify.py` after installing SymPy. The script builds mass-normalized facet-network operators for unit-area regular square and hexagon factors, independently assembles their adjacent and cross-factor conductances, and compares the full and antipodally even rational spectra with the predicted shifted factor spectra. Six tests use two-factor cases (4,4), (4,6), (6,6), and three-factor cases (4,4,4), (4,6,4), (6,6,6), where entries denote facet counts of the polygon factors. A seventh test constructs the facet masses and conductances of a three-dimensional regular octahedron times a unit-area square, and checks its predicted spectrum. All seven tests check exact mass-self-adjointness and the constant zero mode. All seven tests passed.

The proof covers arbitrary full-dimensional origin-symmetric polytope factors of dimension at least two, with no restriction on number of facets or regularity. A finite test cannot establish the general result; the independent argument is the explicit product-facet mass and ridge-conductance decomposition in RESULT.md. The full focal paper was not accessible, so comprehensive novelty verification remains incomplete. External independent scientific review has not been performed.
