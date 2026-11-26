---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

Run `python3 checker.py` with NumPy, SciPy and SymPy. It verifies the radical primitive, the conditional scale-one incidence factorization and the endpoint integral algebraically. Finite quadrature computes the accepted interval in the second endpoint by solving the incidence polynomial at fixed first endpoint; it does not use the closed-form primitive. A separate physical-segment test minimizes the ellipse quadratic along each segment, including same-side segments, for four triangles at five scales. Explicit straddling and nonstraddling chords check the full-scale side tangency. For the universal quantifiers, the analytic argument in `RESULT.md` gives the exact conditional law and accounts for the atom at scale one.
