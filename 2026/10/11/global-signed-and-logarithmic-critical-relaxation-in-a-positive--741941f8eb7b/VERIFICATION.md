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

The exact symbolic checker is `verify.py`. Invoke `python verify.py` with a Python 3 installation containing SymPy. It checks all displayed rational factorizations, the six-jet of the second iterate, the reciprocal-square increment through its quadratic term, and the exact algebra yielding the signed square-root and logarithmic coefficients. Finite examples are sanity checks only and are not used to establish global convergence.

Global positivity, monotonic convergence of the second iterate, uniform analytic remainder in a neighborhood of the equilibrium, and absolute summability of the final residual increments are proved in `RESULT.md`. The argument quantifies over every \(x_0>0\), \(x_0\ne1\), and all sufficiently large even iteration counts, with the additive constant allowed to depend on \(x_0\).

The originality comparison credits existing flip results and generic power-law critical scaling; an independent priority determination and an independent mathematical audit have not been performed.
