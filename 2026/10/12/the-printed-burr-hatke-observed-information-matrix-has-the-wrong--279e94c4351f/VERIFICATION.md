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
For the source log-likelihood,
\[
\ell_1''(\alpha_1)=-\sum_{i,j}\left(\frac{x_{ij}+1}{\alpha_1(x_{ij}+1)+1}\right)^2
\]
and
\[
\ell_2''(\alpha_2)=-\sum_i\left(\frac{y_i+1}{\alpha_2(y_i+1)+1}\right)^2.
\]
Hence observed information \(I=-\nabla^2\ell\) has positive diagonal entries.

The bundled checker compares these formulas against numerical score derivatives on a positive censored sample. For \(k=s=1\), it also evaluates \(P(X>Y)\), obtains a nonzero numerical gradient, and checks that the corrected delta variance is positive while the variance produced by the printed negative information matrix is its exact negative.

The numerical example supplements the analytic sign proof.
