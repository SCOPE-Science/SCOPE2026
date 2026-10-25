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

# Verification and limits

The complete proof is in `RESULT.md`. Run `python3 verify.py` with Python 3 and the standard library. Direct exhaustive Dyck generation for semilengths \(1\) through \(12\) checks 290,511 words in total. The script independently compares each contiguous length-\(2k\) factor to the bitwise complement of its first length-\(k\) half for every \(k\ge2\), returning exactly one survivor per semilength. It also checks the constructive candidates through semilength \(80\) and the possible first-return component pairs for \(0\le a,b\le18\). Expected output begins `ANTISQUARE_DYCK_RIGIDITY_PASS`.

Exhaustive work at bounded sizes cannot establish the all-length theorem; this is supplied by the first-return induction and the proof that each survivor contains no prohibited antisquare. No independent audit was performed.
