---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof is for the positive operator with the printed array (4.1), not for an undirected hard-core model. The exact mass reduction and inverse recover each fixed point coordinate and preserve positivity and summability. The hyperbolic branch identities, small-parameter Taylor coefficient and large-parameter asymptotic give the below-critical interval by continuity. A separate scalar intermediate value argument supplies an equal-mass root. These analytic steps apply at every integer order at least two.

The unchanged `verify_parity_branch.py` provides supplemental finite checks of the mass equations, local bend, two branch crossings, and the order-two specialization. The recorded replay is `VERIFY_OK cases=44 worst_residual=6.395e-14 k2_specialization=1 two_root_orders=2..12`. It neither certifies the all-order argument nor establishes a Gibbs correspondence.
