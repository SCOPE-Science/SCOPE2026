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

Run `python verify.py` with Python 3 and SymPy. The checker reconstructs the matrices from the declared primal-first update, confirms exact one-step and two-step trace/determinant identities, the full degree-two Schur/Jury expressions, both algebraic boundaries, and the rational unstable witness. It also evaluates the original update directly on exact rational input families. The completed run reported `PASS: 1941 exact algebraic/rational checks`.

The proof of the continuum classification is in RESULT.md and does not depend on a finite test grid. The checker is not an independent audit. No claims are made about floating-point stability, automatic stepsize feedback, nonlinear problems or arbitrary switching.
