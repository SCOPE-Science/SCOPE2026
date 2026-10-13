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

The analytic proof uses only three source-level facts: the uniform multimode steady-state identity \(\operatorname{tr}(V^{-1})=2N/\nu\), the generalized entropy-production identity, and the Gaussian displacement-QFI formula. The new step is the reciprocal-spectrum inequality
\[
\sum_{i=1}^{2N}\frac1{x_i}
\ge
\frac1R+\frac{(2N-1)^2}{2N-R}
\]
for positive \(x_i\) with \(\sum_i x_i=2N\) and \(\max_i x_i=R\). It follows directly from convexity of \(1/x\) applied to the \(2N-1\) coordinates other than a maximizer.

The bundled checker verifies the algebraic identity
\[
\frac1R+\frac{(2N-1)^2}{2N-R}-2N
=
\frac{2N(R-1)^2}{R(2N-R)}
\]
and tests the reciprocal-spectrum inequality on deterministic finite samples. Those tests do not prove the theorem.

For \(N>1\), equality of the spectral relaxation is not asserted to be physically attainable: symplectic uncertainty and the Lyapunov steady-state constraint may strengthen the bound. The theorem remains valid because those constraints only reduce the admissible covariance set.
