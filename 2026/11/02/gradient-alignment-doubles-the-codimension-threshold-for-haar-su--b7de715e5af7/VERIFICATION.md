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

# Verification evidence and limits

The standalone `verify.py` recomputes the reduced Hessian, solves its linear equations directly, and compares both special-case identities with exact rational second-moment algebra and Gaussian-orthonormalized random frames. It checks the gradient-alignment discontinuity analytically through rational beta-moment formulae. The submitted theorem is supported by explicit probability-density integrations and exact matrix identities in `RESULT.md`; finite checks do not certify asymptotic tails or completeness of earlier literature.

Independent audit has not been performed.
