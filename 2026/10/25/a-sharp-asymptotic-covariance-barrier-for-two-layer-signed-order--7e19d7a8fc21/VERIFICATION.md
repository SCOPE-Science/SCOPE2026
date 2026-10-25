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
# Reproducibility and limits
Run `python check.py` with Python 3 (standard library only). The script integrates separate signed-clique sectors using exact `fractions.Fraction` beta integrals, independently constructs closed covariance expressions, and tests their equality and positive definiteness for 440 integer parameter pairs. The script checks large balanced and unbalanced parameters numerically; it does not claim to prove infinitely many cases. The proof in `RESULT.md` supplies the infinite-parameter identities, covariance diagonalization and asymptotic optimization by exact algebra. This is a self-review, not independent validation.
