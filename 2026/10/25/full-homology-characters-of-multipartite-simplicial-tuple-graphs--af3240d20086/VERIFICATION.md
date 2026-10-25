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

# Verification of graph-tuple character theorem

The proof is in RESULT.md. Execute `python3 verify.py` using Python 3 with only its standard library. Its tests construct every graph vertex and edge for four parameter sets and use exact integer arithmetic to compare complete induced automorphism actions on chain groups against the cycle-polynomial formula, including orientation sign. Output must include four family PASS lines and the double-transposition sign test. The 495 finite checks verify examples only. No external independent audit has been performed.
