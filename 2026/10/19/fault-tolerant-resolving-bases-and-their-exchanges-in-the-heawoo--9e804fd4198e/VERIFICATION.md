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
# Verification summary

`verify_distances.py` computes shortest-path distances of the fourteen-vertex incidence graph, constructs all 91 distinguishing masks, checks every vertex subset of size below seven and every seven-subset, forms token-jump adjacency directly, and runs BFS from all 280 vertices in the main component. It emits `reconfiguration_certificate.json`, whose states and 784 edges are explicit.

`verify_geometry.py` derives point–line tests using the Fano incidence design rather than graph distances. It generates the predicted five-choice families (28 noncollinear point triples and 28 nonconcurrent line triples), independently evaluates all candidate sets up through size seven, constructs adjacency by six-vertex intersections, recomputes eccentricities, and checks every certificate state and edge. It also confirms the geometric description of all 56 peripheral states.

Actual replay records are in `verify_distances.stdout` and `verify_geometry.stdout`; both end with `VERIFY_OK`. The finite exhaustive checks establish the stated finite results, not a statement for arbitrary projective planes. Bibliographic overlap remains subject to further expert verification. External independent audit has not been performed.
