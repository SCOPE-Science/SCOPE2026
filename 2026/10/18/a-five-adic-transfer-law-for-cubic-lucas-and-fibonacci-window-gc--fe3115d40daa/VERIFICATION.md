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

Run `python3 verify.py` from the directory holding these embedded artifacts. The expected exact output is in `verification_output.txt`. The script checks the integral cubic-shift transfer, its determinant, the fourth-order recurrence, the modulo-\(25\) and modulo-\(125\) boundary certificates, and 320 window lengths by direct arithmetic. The unbounded conclusion depends on the proof's five-adic lifting lemma, not on extrapolating finite experiments.

No independent audit has been performed. An undetected equivalent theorem in non-indexed literature remains a bibliographic risk.
