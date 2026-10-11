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

# Exact arithmetic reproducibility

The included `verify.py` uses the standard-library `fractions.Fraction` type throughout. Running `python3 verify.py` yields `EXACT_AFFINE_FACET_CERTIFICATE_OK` after checking: the matrix inverse; its eighth power; candidate polygons in the three parameter regimes; affine two-endpoint feasibility of all candidate vertices; a common supporting halfplane for each moving edge; the inverse-image invariance of each polygon; and the exact area identities.

The infinite-index statement is independently justified by convex nesting in eight residue classes. It is not inferred from a finite computational loop. At the upper excluded parameter endpoint the certificate uses the degenerate limiting polygon only to validate affine inequalities; the theorem asserts positive-area formulas strictly below that endpoint.

The theorem does not calculate global basins, physical escape-to-infinity rates, or invariant-graph stationary distributions. Source comparison is based on the full accessible arXiv HTML papers, supplemented by semantic research-record searches. No outside independent mathematical audit has been conducted.
