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

The standalone `verify.py` uses exact rational arithmetic for the radial coefficient recursion and finite-field arithmetic for independent sample-matrix rank checks. Run it as `python3 verify.py`; the expected terminal line is `HOPF_GRID_CHECK_OK 5385 exact assertion groups 17 independent finite-field matrix ranks`. It checks degrees at most twelve, a finite search over rectangular periods, and seventeen selected modular ranks. These finite calculations are not a substitute for the complete proof in `RESULT.md`; in particular no finite-field evaluation proves that the fixed transcendental torus radius avoids all Jacobi zeros. That conclusion follows algebraically from the nonzero rational radial polynomials and transcendence of \(e^{-1}\). Neither a machine proof in a foundational proof assistant nor independent human certification is claimed.
