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
# Computational and analytic verification

Run `python CHECK.py` in a Python environment with NumPy and SciPy. The checker evaluates the *exact* infinite-lattice diagonal Fourier resolvent by adaptive quadrature and solves its monotone scalar eigenvalue equation for five fixed detunings and three defect strengths. It compares four moderate-coupling cases with the largest eigenvalue of an independently assembled 1201-site Dirichlet matrix and verifies the quartic-merger coefficient. In the documented run, all 15 scaled-resolvent tests, all four finite-matrix comparisons, and the coefficient check passed.

The analytical certificate is the exact identity \(E_a(k)-(2-2a)=8(a-1/4)(1+\cos k)-4a(1+\cos k)^2\) combined with the rank-one resolvent equation and its quartic rescaling. The limiting integral evaluates explicitly and is strictly decreasing above the limiting upper band edge, justifying unique-root convergence. The resulting positive cubic root and exact free-band subtraction prove the stated coefficient.

The finite checker cannot prove pointwise asymptotic convergence or exclude an equivalent theorem from earlier literature. No independent external audit has been performed.
