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

The argument in `RESULT.md` proves the sign of the exact objective difference for every real finite-dimensional symmetric positive-definite matrix, not merely an experimental sample. Checkable algebraic subclaims are the moment identity, upper bounds on moments, the endpoint energy-ratio factorization, the cubic discriminant, and a concrete rational counterexample.

Run `python3 csd2_cycle_verify.py` in a Python 3 environment with SymPy installed. The checker was executed from its actual saved file path and printed `VERIFY_OK`, an exact step of `17/21`, an objective ratio of `5599232/5250987`, and a threshold approximation of `4.89373323813879641`. Algebraic assertions are evaluated symbolically with SymPy; objective values are evaluated with Python `fractions.Fraction`. The checker corroborates the displayed identities and the witness; it does not itself certify the global quantified inequality. The proof's use of moment constraints, polynomial signs, and strict-continuity arguments supplies that global step.

No independent audit, expert certification, or formal proof assessment has been performed. Full-text availability of some older literature and indexing completeness are separate originality limitations.
