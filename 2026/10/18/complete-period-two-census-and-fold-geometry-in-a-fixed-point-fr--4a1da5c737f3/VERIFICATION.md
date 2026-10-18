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

The proof gives a two-way algebraic equivalence between all primitive period-two orbits and positive roots of the explicitly displayed quadratic. Its root census covers the equality cases and all strictly positive parameters. The return Jacobian is smooth at both points of each period-two orbit, and the exact factorization of its \(+1\)-multiplier determinant is checked symbolically.

Run `python3 checks/check_period_two.py` with SymPy installed. The executed script returned `PERIOD_TWO_EXACT_IDENTITIES_AND_RATIONAL_EXAMPLES_OK`. It tests symbolic identities and rational examples but is not a substitute for the universal algebraic proof. The exact positive-root count, square-root expansion, and Schur criterion are justified in RESULT.md. This is not a certification of arbitrary higher-period behavior, nonlinear stability at multiplier boundaries, or absolute literature priority.
