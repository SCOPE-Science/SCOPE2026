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

The published exact-rational checker can be executed with `python3 hypersimplex_john_checker.py` using the Python 3 standard library. It exhausts the stated test rectangle of 299 pairs, verifies both halfspace slack families, equality supports, boundary contact points, unit ellipsoid norms, John contact moments, determinant and roundness arithmetic. It returns a PASS result for the bounded test rectangle. The all-dimensional result depends on the analytic moment and support proofs, not this computation. Scientific novelty is assessed relative to inspected sources, not certified by unsuccessful searches; independent validation remains unperformed.
