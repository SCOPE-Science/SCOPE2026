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

Run `python3 verify.py` in a Python 3 environment (standard library only). This finite checker enumerates all projective points, all normalized ordered sextuples, and confirms the histograms with exact arithmetic. It additionally computes the four-by-four defining determinant pointwise for one representative of every output class. The normal-form bijection and determinant identity are proved in RESULT.md; separate symbolic reduction of the integer determinant expression modulo two gave the zero polynomial. Actual replay output: `F8 {145: 120} F16 {417: 1440, 433: 144, 449: 600}` and `VERIFY_OK`. This certifies the reported *finite* census, not any claim at larger field size, and is not an independent audit.
