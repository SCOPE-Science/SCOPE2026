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

# Reproduction and boundaries

Execute `python3 checks/verify.py` from the package root with Python 3.9 or later (standard library only). This exact command succeeded for the file included here: the four-type exact rational reciprocity/row-sum identities were confirmed, its sharp spectral value agreed numerically with \((1+\sqrt{13})/5\), and three additional cases each passed 140 comparisons against feasible reciprocal matrices of identical row totals. The tests use explicit random seeds and report their numerical nature.

The theorem for all numbers of types, all fractions, and all admissible matrices is established by the weighted Rayleigh quotient and rank-one comparison in `RESULT.md`. Finite sampling does not establish a universal inequality or uniqueness. Equality characterization is proved algebraically; the script checks sample cases only. Historical novelty is not independently certified. No independent scientific audit has been performed.
