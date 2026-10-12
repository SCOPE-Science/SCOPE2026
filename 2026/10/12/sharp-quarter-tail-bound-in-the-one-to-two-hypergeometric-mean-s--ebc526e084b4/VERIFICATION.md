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

# Verification of the stated tail theorem

The standalone Python 3 program `check.py` uses only the standard library. It verifies 36 exact grid equations between the claimed coefficient matrix and the factored polynomial, and all coefficient signs. The two polynomials have bidegree at most five; equality at six values of each variable therefore proves their identity for arbitrary real arguments by polynomial interpolation. The code also checks the small-sample formulas, the exact Bonferroni integer identity, and a broad additional exact-rational finite sweep. The sweep alone is not a proof of an infinite claim.

At the proof level, the hypergeometric monotonicity couplings, the factorial-moment formula, and positive coefficient signs supply an all-parameter argument. No Lean formalization, independent referee review, or external scientific certification is asserted. A potential unindexed equivalent earlier inequality is the principal unresolved priority risk.
