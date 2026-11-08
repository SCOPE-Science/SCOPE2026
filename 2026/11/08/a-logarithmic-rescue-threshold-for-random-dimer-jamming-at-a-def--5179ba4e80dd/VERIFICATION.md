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

From the folder containing `verify.py`, execute `python3 verify.py` using Python 3 (standard library only). The program prints `PASS 53 independent exact and numerical assertions` after comparing the recurrence with independently labeled graph states over all even orders 4 through 12 and allowable hub degrees, checking two boundary cases per order, and three seeded numerical checks of the asymptotic scale.

The infinite-size theorem is established by the random-permutation hazard proof in `RESULT.md`; the finite exhaustive checks and the Monte Carlo tests do not certify an asymptotic statement. The historical novelty assessment is conditional on the inspected literature, not an independence certificate.
