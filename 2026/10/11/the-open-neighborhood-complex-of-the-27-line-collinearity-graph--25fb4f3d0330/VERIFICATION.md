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

Run `python3 verify_neighborhood_gq.py` to reconstruct all exceptional-line intersection edges, all 23,778 nonempty open-neighborhood simplices, all 11,853 matched pairs and the 71 remaining critical four-cells. The program constructs the entire directed Hasse diagram and verifies global acyclicity by Kahn topological sorting: 126,522 edges, 23,778 of 23,778 nodes processed. It asserts the graph's complete common-neighbor parameters, the face vector and Euler characteristic.

Run `python3 verify_polar_model.py` to construct an independently defined elliptic quadratic space over \(\mathbb F_2\), explicitly match its 27 singular points to the 27 cubic-surface line labels, check adjacency on every unordered pair and count the complete open-neighborhood face vector by combinations.

These are complete finite graph/face/matching checks, not partial experiments. The topological implication invokes the ordinary discrete-Morse theorem: one critical zero-cell and 71 critical four-cells leave a CW space homotopy equivalent to a wedge of 71 four-spheres. This does not establish analogous results for any other graph or guarantee priority against unindexed publications.
