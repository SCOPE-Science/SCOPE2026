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

# Reproducibility and scope of verification

Execute `python3 verify.py` using Python 3.8 or later. It requires no external packages or downloaded data. On the included run, it printed:

`VERIFY_OK cases=27954 firing_steps=65453 two_component_cases=243`

The checker simulates synchronous threshold firing of a bidirected star from every tested initial chip vector, stopping at the first repeated chip state or stabilization. It constructs the full downward-closed simplicial complex of all firing sets and checks exact agreement with the symbolic facet theorem, not merely its Euler characteristic or homology. It independently verifies the explicit criterion for two components and the predicted connected-component count at every finite time prefix. The tested leaf counts are from one to seven, with systematically bounded initial chips; the code documents the bounds. Repeated chip configurations imply identical future firing trajectories, so each tested finite configuration is exhaustively simulated.

This enumeration does not prove claims for unbounded chip amounts or star sizes; those claims rely on the analytic recurrence proof in `RESULT.md`. No independent audit of the proof or research novelty has been performed.
