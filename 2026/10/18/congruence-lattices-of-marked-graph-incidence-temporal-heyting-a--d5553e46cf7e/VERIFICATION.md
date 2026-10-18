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

The mathematical proof of the general classification appears in RESULT.md, using the published congruence/archival-upset correspondence and an explicit order-preserving reduction to a quotient incidence poset.

Execute `python verify_archival.py` from the directory containing the two accompanying Python files. It checks all 761 labeled graph/edge-mark combinations with up to four graph vertices, enumerating every subset of the incidence poset and applying the archival definition directly.

Execute `python verify_algebra.py` from the same directory. It counts compatible elements in explicit finite temporal Heyting upset algebras and compares them with the quotient-graph formula for four graph families and, in the three-vertex families, every vertex-reflexivity assignment.

Both scripts use Python's standard library only. The finite tests supplement, but do not replace, the proof for all finite graphs. The source theorem, not software, supplies the general congruence/archival-upset correspondence. Independent mathematical auditing remains unperformed.
