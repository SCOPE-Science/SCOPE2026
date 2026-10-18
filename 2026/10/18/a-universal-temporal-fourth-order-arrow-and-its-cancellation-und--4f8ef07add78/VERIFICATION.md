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

# Verification record

The proof in `RESULT.md` derives the two-sided stationary stochastic integral, the exact stationary moments, the degree-one and degree-three generator equations, and the fourth-order temporal contrast. Direct integration proves sign rigidity at every lag and an exact zero-contrast but irreversible overshoot model.

`python verify_time_arrow.py` is an executable cross-check (Python 3; NumPy, SciPy, SymPy). The inspected package script passed 124 counted assertions: symbolic coefficient identities; exact gamma-moment relations and rate positivity; parameterized multiplier laws; and independent five-dimensional polynomial-generator matrix exponentials at several positive lags.

Finite numerical checks do not establish positivity at arbitrary real parameters or all continuous lags. Those conclusions depend on the analytical formula and strictly positive integral. Unique stationarity is asserted among finite-fourth-moment invariant laws. No independently conducted audit or experimental validation is asserted.
