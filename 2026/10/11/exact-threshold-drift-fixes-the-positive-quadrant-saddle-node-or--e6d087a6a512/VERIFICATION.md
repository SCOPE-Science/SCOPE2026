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

The printed vector field was reconstructed directly at the critical surface \(m=aq\), with \(A=1+D_1\) and \(q=1-D_2/A\). Differentiating \(U=(D_1/A)x_1+x_2\) gives
\[
\dot U=\frac{x_2^2(q-a-x_2)}{x_2+a}.
\]
The identity was expanded independently in two forms and the expressions agree exactly.

The origin Jacobian is
\[
\begin{pmatrix}-A&D_2\\D_1&-D_1D_2/A\end{pmatrix}.
\]
Its determinant is zero, its nonzero eigenvalue is \(-(A+D_1D_2/A)\), its positive right nullvector is \((D_2/A,1)^T\), and a left nullvector is \((D_1/A,1)^T\). Projection of the quadratic term along these nullvectors yields
\[
\kappa=\frac{A^2(q-a)}{a(A^2+D_1D_2)}>0.
\]
For the numerical parameters displayed in the source's critical phase portrait, \(D_1=0.6\), \(D_2=0.5\), and \(a=0.18\), the values are \(q=0.6875\), \(m=0.12375\), \(q-a=0.5075\), and \(\kappa\approx2.5236985237\).

The proof does not infer global convergence to the positive equilibrium from the local calculation alone. Its global conclusion is only the exclusion of convergence to the origin for nonzero nonnegative trajectories at the stated critical surface. No independent audit has been performed.
