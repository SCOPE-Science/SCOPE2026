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

The verification code in `verify.py` is standalone given the packages listed in `requirements.txt`. Execute `python verify.py`. During preparation, the verifier was executed from its packaged source and passed **60,449** checks, including directly diagonalized plane compressions against the cone inequalities, numerical CDF quadrature, independent Haar samples, inverse monotonicity checks, the known prolate limit and sharp upper-tail asymptotics.

All-dimensional or continuum claims do not follow from these tests; the exact cone reduction, spherical integral, dominated-convergence argument and strict elliptic-integral derivative in `RESULT.md` prove the stated three-dimensional theorem. No independent mathematical audit or publication-priority certification is asserted.
