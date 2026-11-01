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

# Reproducibility checks

Run `python verify.py` with Python 3.9 or later and no external packages. The program uses rational arithmetic for the explicit sharpness construction in dimensions two through six. For all sign facets it verifies the exact supporting equations, strict exclusion of other vertices, and the exact deficit identity at \(c=899/901\), \(s=60/901\). It is an independent finite sanity check of an analytically universal argument, not a computer-assisted exhaustive proof over arbitrary dimensions or all convex polytopes.

The critical continuum arguments are stated in the Proof: oriented signed facet determinant, orthogonal trace maximization, singular-value arithmetic–geometric mean, and the facet-support inequalities when \(c>2s\). No independent audit was performed.
