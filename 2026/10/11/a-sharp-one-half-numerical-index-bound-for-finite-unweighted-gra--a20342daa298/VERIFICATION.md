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

# Reproduction and scope

Run `python3 artifacts/verify.py` with Python 3 and the standard library. It checks the linked edge-height construction by exact rational arithmetic, all connected labeled simple graphs of orders 2–4, five representative graphs of order 5, and the explicit sharp triangle operator.

Observed successful result:

`VERIFY_OK graphs=48 zero-edge_face_checks=556 triangle_norm=1 triangle_radius=1/2`

The general lower bound does **not** follow from finite enumeration: its proof is the connected-tight-edge integrality lemma, the reweighted shortest-path construction, and the exact decomposition of any zero-slope extreme functional into two norming functionals. No numerical approximation, unavailable computation, or outside certificate is used for that argument.

The statement does not concern weighted graphs, complex scalars, or infinite metric spaces. Independent audit has not been performed.
