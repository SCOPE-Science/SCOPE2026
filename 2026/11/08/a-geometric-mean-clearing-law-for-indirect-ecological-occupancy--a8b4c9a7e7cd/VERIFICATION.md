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

Exact analytic verification starts from the four-state stationary master equations and derives the conditional sensitivity, false-positive rate, unique maximizing clearing rate, and reciprocal symmetry, including the strictly positive parameter domain. `verify.py` independently reconstructs the finite-state generator and solves its stationary law with rational arithmetic over 1296 parameter quadruples, checking all four stationary equations, both conditional error expressions, and reciprocal equal-discrimination identities. Run with `python3 verify.py` using Python 3 standard library only. Finite parameter checks do not establish the universal theorem; the algebra in RESULT.md does. No claim of independent validation, field calibration, or biological universality is made.
