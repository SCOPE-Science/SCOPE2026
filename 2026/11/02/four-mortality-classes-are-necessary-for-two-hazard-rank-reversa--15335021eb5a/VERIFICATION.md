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

The general bound for one, two and three shared mortality classes follows analytically from the exact exponential-sum numerator and the single-sign-change argument in `RESULT.md`. The lower bound is not based on exhaustive parameter sampling.

For the constructive four-class part, run `python CHECK.py` after extracting all files. It uses exact rational arithmetic and checks the polynomial identities and rational brackets of the two distinct roots. Independently of this program, the quadratic discriminant establishes strict survival ordering at every positive age, while Descartes' rule plus the two sign brackets establishes exactly two positive roots and rules out other positive roots. Approximate crossover ages are descriptive rather than proof certificates.

The scientific claim does not include a sampling-error bound or a clinical interpretation. The historical literature comparison is not an independent priority certification.
