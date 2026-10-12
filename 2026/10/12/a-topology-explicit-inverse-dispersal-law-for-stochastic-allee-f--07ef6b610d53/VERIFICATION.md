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

# Reproducibility and check scope

The finite-model checker `verify_gap.py` is included in the package. It uses Python 3 and only the standard library. Run `python3 verify_gap.py` to check local rational arithmetic and the lower-event construction.

Observed completion: `VERIFY_OK edge_energy_identities=35952 complete_graph_gap_identities=1089 two_patch_lower_event=1`. The tests cover finite rational configurations, not a census of all graphs, states, or event histories. The universal theorem depends on the analytic proof in `RESULT.md`.

The bound assumes a connected finite undirected graph, symmetric mixing, positive edge and site rates, a common strict threshold, and initial mean different from that threshold. The order-sharpness construction is one explicit two-vertex example, not a claim of optimal constants for every network.

No independent mathematical audit or external verification has been performed.
