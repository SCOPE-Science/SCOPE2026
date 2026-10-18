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

The finite-state rational certificate consists of `CERTIFICATES.json` and `verify_exact.py` in this same directory. With Python 3, run `python3 verify_exact.py`; the checker uses only the standard library and verifies both \(729\)-state derivative identities, boundary conditions, the exact \(90\)-configuration balanced spectrum on each graph, and all label-exchange antisymmetry identities. This is an exact machine-checkable finite computation, together with the uniqueness argument in `RESULT.md`.

The check concerns the derivative of fixation probability at zero selection; it does not independently validate an empirical ecological model, all parameter intensities, or a general larger-graph theorem. Independent audit has not been performed.
