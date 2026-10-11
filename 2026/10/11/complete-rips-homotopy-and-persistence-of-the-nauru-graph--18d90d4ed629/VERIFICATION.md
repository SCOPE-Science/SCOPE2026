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

# Reproducibility

Run `python3 verify.py` from the same directory as `collapse_certificate.json`. Both files are included and require only the Python standard library.

Expected final line:

`VERIFY_OK vertices=24 radius2_faces=276 relative_pairs=96 critical_2cells=12 radius3_faces=5328`

The program reconstructs all graph edges and exact shortest-path distances; checks graph diameter four; enumerates all radius-two simplices; checks connected, orientable, closed twelve-vertex torus triangulations via vertex links, edge incidences, and triangle orientations; replays 96 genuine free-face pairs in the specified chronological order with 12 critical two-faces; verifies signed integral boundaries of the 12 projected attaching loops against 12 displayed two-chain certificates; reconstructs the exact radius-three simplicial join; and computes exact mod-two boundary matrix ranks for each relevant complex. It checks radius-one graph cycle rank from counted vertices and edges. The written proof supplies the topological implications (surface classification, nullhomologous loops on a torus, and suspension splitting); finite computation is not treated as an infinite theorem or as an independent audit.

Same-model review: passed. Independent audit: not yet performed.
