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

The bundled checker reconstructs the source's baseline endemic equilibrium, analytic Jacobian, and diagonal weak-noise matrix from the printed parameters. It solves both the covariance and adjoint Lyapunov equations with an internal Gaussian-elimination routine and reproduces the independent covariance in Eq. (4.4) to the displayed precision.

It verifies the affine law
\[
\operatorname{tr}W(R)
=
17.2747505624
+5.39530312013\,\rho_{12}
+0.537604148434\,\rho_{13}
+0.152951296895\,\rho_{23},
\]
and evaluates the two rank-one endpoint correlation matrices
\[
R_+=\mathbf 1\mathbf 1^\top,\qquad
R_-=(1,-1,-1)^\top(1,-1,-1).
\]
The resulting traces are approximately
\[
23.3606091279
\quad\text{and}\quad
11.4947945907,
\]
respectively.

The global extremum proof is analytic: representing a correlation matrix as a Gram matrix reduces the minimum to a one-variable function whose derivative is strictly positive on \([-1,1]\).

Finally, the checker verifies that the literal printed Eq. (3.19) at \(R_+\) satisfies
\[
W_{\mathrm{printed}}=W(R_+)+W(I_3)
\]
and has trace approximately \(40.6353596903\).

Unproved limits: the exact finite-noise nonlinear stationary covariance, determinant-extremizing correlations, and individual principal-axis extrema are not claimed.
