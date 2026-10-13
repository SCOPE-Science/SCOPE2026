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

# Verification instructions and limits

Run `python verify.py` with Python 3 (standard library only) from the same directory as this document. The script performs 72 exact rational checks of the history-likelihood Fisher information against its latent-missing-information representation, 84 exact rational checks of the false-positive-free Bernoulli reduction and the sufficient one-visit-optimality inequality, and four numerical diagnostics for the logarithmic scaling regime.

Expected successful output:

`VERIFY_OK identity_cases=72 false_positive_free_cases=84 rare_prevalence_tests=4`

The proof in `RESULT.md` establishes the domain-wide statements. The finite tests independently check critical normalization identities and inequalities but cannot certify arbitrary positive probabilities or the limiting formulas. Assumptions include fixed known detection rates, conditionally independent visits, homogeneous equal-cost designs, and an idealized large-budget local Fisher-information criterion. The noncommuting parameter limits, finite-budget constraints, and unexamined specialized literature are expressly outside the verified claim.
