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

# Reproducibility and checks

Run `python verify_edge_observation.py` with Python 3 and no third-party dependencies. The program computes the observed edge states directly for every binary vertex assignment and groups assignments by their actual observation. It separately computes connected-component bipartiteness, the predicted generating polynomial, and an inverse factorization from the observed polynomial. All of these are checked for every labeled simple graph on one through six vertices and 250 reproducibly sampled labeled graphs at each of orders seven, eight, and nine.

The successful recorded run prints `VERIFY_OK graphs 34617 fiber_enumerator=PASS inverse_recovery=PASS rank3_boundary=PASS`. Its last boundary test confirms that a single three-element hyperedge has one zero-state input, six mixed-state inputs, and one full-state input, so the graph result does not automatically extend to hypergraphs.

The general theorem is proved mathematically using connected-component propagation, proper two-colorings, and factorization of a univariate polynomial. Finite enumeration alone is not an infinite proof. No external/independent audit has been performed.
