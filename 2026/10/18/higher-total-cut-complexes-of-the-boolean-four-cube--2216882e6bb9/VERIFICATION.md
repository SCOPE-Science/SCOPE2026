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

The bundled `verify_q4_totalcut.py` and `certificate_q4_totalcut.json` form an executable finite certificate, requiring only Python 3. Invoke `python3 verify_q4_totalcut.py certificate_q4_totalcut.json`. It reconstructs all independent sets, checks the two independently defined face sets agree, builds the matching, verifies every directed Hasse cover through topological sorting, and checks the critical-cell lists and matched-pair digests. No infinite extrapolation, homology-field assumption, or unstated external certificate is used. The established claim is confined to \(4\le k\le8\) for \(Q_4\); the independent mathematical audit remains unperformed.
