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

Running `python verify.py` with Python 3 and SymPy verifies the exact rational generating function by symbolic calculation of all 81 explicitly specified four-state matrices. It independently counts using the triple-observation streaming automaton through length 64 and literally enumerates all words through length 15. The final output is `ALL CHECKS PASSED`.

The exact finite algebra, not the length-limited experiments, establishes the generating function for arbitrary length. Standard polynomial partial fractions then yield the stated recurrence and asymptotic; the root moduli follow from the cubic and Vieta's product. No independent audit is claimed.
