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

# Reproducibility

Run `python verify_bdf3_periodic.py` with Python 3 and SymPy. The verifier derives both BDF3 row coefficients from derivatives of Lagrange basis polynomials at the new node, constructs the companion matrices, and independently checks the rational trace and determinant of the two-update monodromy. It verifies the three exact polynomial positivity identities used by the \(1/5\) Schur--Jury proof, the palindromic reciprocal discriminant, and both singular-limit roots. Representative numerical roots are additional checks, **not** the infinite proof.

The analytic proof in `RESULT.md` supplies the strict inequalities for every \(r>0\), the one-sign-change argument for the unique phase root, and the bounded-power deduction. The computation does not certify arbitrary variable grids, perturbed stability, nonlinear convergence, or estimates uniform as \(r\to0\) or \(r\to\infty\). Independent audit has not been performed.
