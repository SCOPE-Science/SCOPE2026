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

The included `verify.py` is a standalone SymPy checker of the exact stationary Lyapunov equations, both diagonal covariance formulas, the derivative sign polynomial, the PSD coefficient inequalities, the trace derivative identity, the independent-noise incompatibility identity, and the radical witness. It also evaluates 1,280 rational PSD covariance tuples. Running `python verify.py` completed successfully.

The all-parameter conclusion does **not** follow from the finite grid. It follows from the written partial-fraction single-stationary-point argument, the positive-semidefinite coefficient obstruction, and the matrix trace monotonicity inequality. Algebraic checks are reproducible but independent external scientific validation has not been performed. The model does not make claims about extinction probabilities or nonlinear population persistence.
