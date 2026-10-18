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

The standalone script `tetra_truncation_verify.py` checks the graph cut enumeration exactly, using all nontrivial binary sign assignments to the twelve cut vertices. It verifies the analytic criterion for 14,279 nondegenerate exact-rational direction configurations, across two tetrahedron affine shapes and six independent truncation vectors. Five normal-distribution Monte Carlo comparisons, each using 150,000 directions, test the metric spherical-area formula; random direction tests are corroboration, not proof. Its final output includes `EXACT_GRAPH_CUTS_OK 32 EXACT_RATIONAL_NORMALS_OK 14279` and `SPHERICAL_SOLID_ANGLE_FORMULAS_OK`.

Reproduction: Python 3 standard library, run `python tetra_truncation_verify.py` in this directory. The proof for all tetrahedra and real corner fractions is in RESULT.md and uses the exact three-edge-cut classification, sign inequalities, centering argument and Girard's spherical excess theorem. No proof has been formalized in a theorem prover and no independent mathematical audit has been performed.
