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

## Exact-arithmetic reproduction

Extract the complete accompanying `verify.py` next to this file and run `python3 verify.py`. It requires Python's standard library only. Its computation reconstructs the two proposed ellipsoids for 18 complete-bipartite parameter pairs, checks the polar-vertex and primal-vertex contacts using rational Laplacian inverses, and verifies the isotropic dual contact certificate as a full rational matrix equality.

For small cases it independently enumerates feasible integer potential labelings in the exact graph-distance range and tests tight-edge connectedness to recover every polar vertex. No timeout, approximation, or skipped configuration is interpreted as a proof.

## Analytic checks and limits

The standalone analytic proof establishes the polar facet classification, uniform ellipsoid feasibility, a positive Loewner contact measure for the polar, an isotropic uniform edge-vertex measure for the primal, and the eigenvalue determinant identity. Those arguments establish the infinite family; the finite verifier only cross-checks critical formulas. Independent auditing has not been performed. The statements do not infer Banach--Mazur optimality under unrestricted linear maps.
