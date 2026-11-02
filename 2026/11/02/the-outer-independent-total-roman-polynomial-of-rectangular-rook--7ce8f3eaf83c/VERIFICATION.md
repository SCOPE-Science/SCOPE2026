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

The included `verify_oit_rook.py` implements the original conditions: zeros independent, every zero adjacent to a label \(2\), and every positive vertex adjacent to another positive vertex. Its direct checks do not use the claimed inclusion-exclusion identity to decide validity.

Run with `python3 verify_oit_rook.py`; Python 3.9 or later is required. The tested boards are \(2\times2\), \(2\times3\), \(2\times4\), \(2\times5\), \(3\times3\), \(3\times4\), \(3\times5\), and \(4\times4\). The first six use direct enumeration of all ternary assignments. The last two enumerate all independent zero matchings and all binary label-\(2\) assignments to other squares. Every polynomial coefficient and the exact minimum multiplicity was checked; the run terminated with `VERIFY_OK`.

Finite checks do not prove the all-parameter statements. The proof in RESULT.md provides the infinite argument. No independent audit or external formal certification is asserted.
