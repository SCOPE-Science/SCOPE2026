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
Run `python3 verify_minimal_edge_covers.py` using only the Python standard library. The program has two distinct checks: explicit construction of an edge cover for every binary trace for each \(3\le a,b\le7\), and direct enumeration of all edge subsets for small parameter pairs to obtain every inclusion-minimal cover and compute VC dimension without using the claimed formula. It additionally computes finite Littlestone ranks as diagnostic tests.

Expected summary is `THREE_COMPONENT_ALL_TRACES_PASS cases 7688` followed by finite census rows and `ALL_MINIMAL_EDGE_COVER_SHATTERING_CHECKS_PASS`. The mathematical proof, not this finite enumeration, handles all \(a,b\ge1\). This verification neither establishes publication priority nor represents an independent scientific audit.
