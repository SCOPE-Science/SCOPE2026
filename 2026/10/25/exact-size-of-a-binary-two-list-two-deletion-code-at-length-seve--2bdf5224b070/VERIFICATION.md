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

# Verification record

The included `verify.py` uses only the Python standard library. It checks the eleven-word construction against every one of the thirty-two possible received words, confirms the exact dual-weight sum, and checks the dual inequality for all one hundred twenty-eight length-seven binary words with integer arithmetic. It then verifies \(2\sum_y w_y+14=666\) and \(666/59<12\). The finite upper certificate and explicit lower witness establish the claimed optimum.

The check does not classify all optimal codebooks and makes no claim about other lengths, deletion counts, list sizes, or alphabets. Independent audit and independent validation have not been performed.
