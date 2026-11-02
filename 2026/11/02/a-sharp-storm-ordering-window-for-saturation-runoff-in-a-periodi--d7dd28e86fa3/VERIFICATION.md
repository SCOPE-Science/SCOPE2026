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

# Verification

Run `python verify.py` in a Python 3 environment. Only the Python standard library is required. The script constructs exact-rational periodic fixed points of capped affine compositions independently of the anchored-storage expressions used in the proof, checks the fixed-point condition and conservation law, compares both cyclic orders with exact formulas, and tests all strictness predictions over 16,500 parameter combinations. It also checks the exact witness \(5/16\) versus \(1/8\).

Expected output: `PASS: 16500 exact triples x parameters; 1632 strict cases; rational witness 5/16 vs 1/8`. The universal proof is in `RESULT.md`; finite enumeration does not itself prove any quantified theorem. The literature comparison is limited to cited accessible material, and independent auditing has not been performed.
