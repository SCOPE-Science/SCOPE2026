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

# Reproduction

Run `python3 VERIFY.py`, requiring only a Python 3 standard library. A successful execution returns `VERIFY_OK` and the exact computed values.

The script implements binary polynomial arithmetic modulo `0b11111`, enumerates the explicit S5 line orbit, checks the source line satisfies the quartic equation, computes the Frobenius permutation and exact modular matrix-rank lower bounds, and enumerates all projective representatives of the two extension fields. These are exhaustive finite verifications. The published statement that the 60 lines span a rank-20 geometric Néron–Severi lattice supplies the dimension upper bound; the étale cohomology trace formula supplies the global inference. The script is not a substitute for those theorems or an independent scientific audit.
