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

# Verification

`verify.py` reconstructs the complex from the explicit 17-facet list and uses only exact integer/set operations. It checks that there are 24 edges and that edge-to-triangle incidence degrees are 21 edges of degree 2 and 3 edges of degree 3.

For each choice of critical triangle, the verifier recursively assigns each other triangle a distinct incident edge. Each assignment adds the corresponding triangle-transition arcs and updates an exact transitive closure; branches that create a directed cycle are rejected immediately. Every complete accepted assignment is therefore an acyclic triangle-edge matching, and every such matching is reached exactly once. The verifier separately repeats the search with no critical triangle.

For every accepted one-critical-triangle layer, the eight unused edges are checked for connectedness. Since there are eight vertices and eight residual edges, connectedness implies a unique cycle; leaf peeling obtains its length. The exact histogram is then converted to full gradient fields by the rooted-spanning-tree factor `8*cycle_length`.

A successful replay prints exactly:

`VERIFY_OK facets=17 edges=24 full12=0 acyclic16=1992223 cycle_hist=3:754080,4:706489,5:365173,6:131021,7:31621,8:3839 weighted=7952246 optimal_fields=63617968`

The computation is exhaustive only for the supplied labelled complex. It is not evidence that other minimal dunce-hat triangulations have the same count, and it is not a proof-assistant certificate.
