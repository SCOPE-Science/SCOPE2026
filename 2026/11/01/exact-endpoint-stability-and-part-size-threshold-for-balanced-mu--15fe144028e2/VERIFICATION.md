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

The exact rational checker `verify_balanced_metric_graph.py` was executed on its included source and returned `PASS; exact assertions: 4690 balanced multipartite configurations: 26`. It computes the mass matrix afresh from the edge set and checks its independently inverted entries, every vertex's exact absolute kernel integral, and symbolic identities for the formula, monotonicity and both limits.

The proof, rather than the finite checks, verifies all integers \(m\ge1\) and \(r\ge2\). It uses the explicit inverse of the nodal Gram matrix, a closed absolute-linear-integral identity and the reduction of affine edge maxima to vertices. The exact norm is attained on \(L^\infty\) by kernel sign inputs; continuity of these inputs is not asserted. The weighted, unbalanced, complex and subdivided graph cases are outside scope.
