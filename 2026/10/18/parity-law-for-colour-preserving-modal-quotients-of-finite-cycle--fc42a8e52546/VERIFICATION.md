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

Reproduce with `python3 check_candidate.py` and `python3 verify_graph_maps.py` in the directory containing these files. The first compares predicted quotient types against explicit phase-induced target colourings for all binary words of lengths 3–14 and all ternary words of lengths 3–9. The second independently generates graph maps from the local-neighbourhood back condition for all cycle source orders 3–18, yielding 288 source/target size tests. Neither finite test proves the all-size theorem: the proof is given separately in RESULT.md. No external datasets are required.
