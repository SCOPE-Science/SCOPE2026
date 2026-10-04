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
The proof reconstructs the exact cyclic sweep matrix and reduces fixed-momentum stability to a complex quadratic Schur--Cohn test. The algebraic factorization leaves a single cubic polynomial \(P_c(\alpha)\); its strict decrease on \([0,1]\) and the unique positive root of the unit-momentum quartic give the complete phase diagram.

`verify.py` checks the matrix formulas, the factorization, the quartic root, representative modal root radii on each side of the boundary, and the two-block stability inequalities. It uses only the Python standard library. Finite checks do not replace the analytic all-parameter proof.
