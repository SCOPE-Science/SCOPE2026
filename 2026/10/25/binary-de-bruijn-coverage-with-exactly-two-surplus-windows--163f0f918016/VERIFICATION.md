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

The standalone `near_debruijn_verify.py` uses only the Python standard library. Run `python3 near_debruijn_verify.py`; expected final line is `VERIFY_OK`. It enumerates every binary cyclic word at orders 2, 3 and 4, using independent window counting, rotation normalization, and exact grouping by two extra factors. It also uses independent integer Bareiss determinants on augmented and unaugmented de Bruijn Laplacians at orders 2 through 7. The proved all-order result uses the separate symbolic balance/BEST/group-inverse argument; finite checks alone do not prove it. The output classifies oriented circles up to rotation, not reflection. No independent audit or external certification was performed.
