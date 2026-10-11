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

The mathematical argument uses: (i) the \(q\)-numerical-range variational constraint; (ii) the Perron simplicity of an irreducible positive tridiagonal singular-value matrix; (iii) the strictly convex singular-norm envelope; and (iv) the Schur-complement expansion of a simple sine-mode eigenvalue. Explicitly, the first positive derivative is \(q_n=\cos(\pi/n)\), the second derivative is \(a_n=(n+2)\sin^2(\pi/n)/n\), and the Legendre-type infimum yields the \(1/(2a_n)\) quadratic loss.

`verify_qshift.py` was executed with NumPy and SciPy available, checking the positive-edge radius for \(n=4,5,6,7,8\) at two small perturbations and the associated singular-norm expansion. Observed terminal marker: `JORDAN_Q_RADIUS_EDGE_NUMERICAL_CHECK_OK`. Execute `python verify_qshift.py` from the directory containing this file to reproduce. No output of this finite program certifies the theorem for arbitrary dimension. The critical algebraic formulas are verified in the written proof, not inferred from experiment. A broader 1998 primary source remains incompletely accessible. Independent audit: not performed.
