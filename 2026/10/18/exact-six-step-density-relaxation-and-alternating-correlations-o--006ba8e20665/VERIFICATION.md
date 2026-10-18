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

Run `python verify.py` with SymPy installed. The program independently checks the invariant interval's algebraic constants, the four-by-four transfer matrix, mass preservation, stationarity, its exact factored characteristic polynomial, and the entire six-step projection identity by symbolic arithmetic over the real quadratic field. It recomputes the stationary mean and checks 18 successive coordinate covariances, including each of the six residue classes three times.

A successful replay prints a single `PASS` statement. This is an exact finite algebraic cross-check of the stated analytical proof, not a finite-data inference of an infinite mixing theorem. No checks of the Navier--Stokes flow, of the spline conjugacy's regularity, or of arbitrary BV/Lipschitz density mixing are claimed. Independent audit: not yet performed.
