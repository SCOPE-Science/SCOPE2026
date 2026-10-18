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

The exact-rational standalone verifier `verify.py` separately checks the water-filling formula, projected facet normals and inequalities, contact equality and constructed contact points. It executes with Python 3 and requires no third-party packages.

Executed result: `PASS: 8318 exact water-filling instances; 3703 separately projected facet inequalities; 2851 exact contact points in the polytope; ['both', 'row_only', 'sphere', 'threshold']`.

All general assertions rely on the symmetry, halfspace, and strictly concave determinant proof; finite arithmetic tests alone are not a proof for all parameters. No independent audit has been performed.
