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

# Reproducibility and boundaries

The standalone `verify.py` uses Python 3 and NumPy. Run `python verify.py` in the directory containing the embedded code. The completed execution printed `PASS 7942 deterministic checks; max n = 4001`.

Checks include direct dense-matrix versus Fourier-block eigenvalues for small graph sizes, universal upper bounds at thousands of graph sizes with randomized symmetric orbit budgets, separate randomly generated *nonuniform* edge-weight networks, and the parity-stratified asymptotic construction through graph size 4001. These samples are supplementary numerical validations and do not establish any universal statement.

The universal theorem follows from the analytic Fourier decomposition, positivity certificate, escaping-mode estimates, and trial-vector optimality inequalities in `RESULT.md`. Numerical eigensolvers do not constitute exact arithmetic certification of the infinite theorem. The exact numerical value of the finite maximizing network and independent audit remain outside the verified scope.
