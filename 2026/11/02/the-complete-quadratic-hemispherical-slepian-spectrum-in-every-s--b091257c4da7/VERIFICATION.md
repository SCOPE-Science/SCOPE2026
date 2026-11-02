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

# Checks and limitations

The claim is established by the analytic decomposition and beta-moment calculations in `RESULT.md`. Running `python check.py` with the dependencies in `requirements.txt` independently constructs monomial Gram matrices for the full sphere and hemisphere and solves the complete generalized eigenvalue problem for every dimension 3 through 10, testing all 268 computed eigenvalues against the explicit formulas. The executed run returned `ALL_CHECKS_PASS` and also checked the dimension-three special values and the exact rational parity-step inequalities.

These finite calculations are corroboration, not a proof for untested dimensions. The limiting formula relies on the usual gamma-ratio asymptotic. The novelty comparison is provisional: an equivalent formula could be contained in less-visible literature. Independent mathematical audit has not been performed.
