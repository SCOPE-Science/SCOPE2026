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
# Reproducibility and limits

The analytic argument uses (1) an invariant receptive-edge pattern proven by explicit gap inequalities, (2) a geometric comparison of opinion gap and confidence bound, and (3) a primitive row-stochastic averaging matrix with stationary weights proportional to the self-inclusive degrees. These give the threshold and all quantifiers for arbitrary network size \(n\ge3\).

Run `python verify_edge_repair.py` with Python 3 (standard library only). It constructs rationally exact trajectories, checks 69 parameter/configuration cases for the edge pattern and switching time, and verifies the preserved stationary weighted sum in non-repair paths. The finite suite is not a proof for all agent counts and does not test other network topologies. No independent validation has been performed.
