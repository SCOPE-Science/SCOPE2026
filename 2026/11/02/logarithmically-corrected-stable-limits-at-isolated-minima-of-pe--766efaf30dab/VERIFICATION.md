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

# Mathematical verification and limits

The rescaled jump compensator is checked by the change of variables \(y\mapsto b_n y\) in the symmetric Lévy kernel. Its stationary average is evaluated using a nondegenerate Laplace saddlepoint expansion on the spatial torus, with the \((\log n)^{d/2}\) factor exactly canceling the \((\log b_n)^{-d/2}\) volume of the minimizing neighborhoods. The uniform exponential-mixing covariance inequality controls the triangular-array error by \(O((\log n)^d/n)\) on finite time intervals. Standard semimartingale characteristic convergence then establishes the functional stable limit; this last implication rests on the referenced general convergence theorem.

The accompanying `verify_scaling.py` produced the retained `verification_output.txt` with 95 passing deterministic checks, including one-, two-, and three-dimensional cosine-index torus integrals, weighted two-regime saddlepoint sums, and logarithmic normalization identities. These are checks of the analytic coefficients, **not** stochastic-process simulation or proof by extrapolation. To rerun: `python verify_scaling.py` in an environment with Python 3 and SciPy.

Assumptions not supplied solely by the cited mixing result include continuous strictly positive invariant densities at the minimizer locations. The convergence is for fixed initial states and symmetric stable-like kernels; no general degenerate-minimum result, independent review, or historical-priority certification is implied.
