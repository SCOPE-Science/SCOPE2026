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
The proof is analytic.

The bundled checker verifies three supporting facts from the exact equations:

- subtracting the normalized susceptible equations gives
  \[
  \dot q=-(\mu+\beta(E+I))q-(\alpha-\beta)(E+I)\frac S\rho;
  \]
- the effective susceptibility decomposes as
  \[
  \alpha S+\beta L=
  (\alpha\rho+\beta(1-\rho))(S+L)
  +(\alpha-\beta)\rho(1-\rho)q;
  \]
- the infected block
  \[
  A(a)=
  \begin{pmatrix}
  a-\delta-\mu&a\\
  \delta&-\gamma-\mu
  \end{pmatrix}
  \]
  has determinant
  \[
  (\delta+\mu)(\gamma+\mu)-a(\gamma+\mu+\delta).
  \]

For the source numerical parameters the checker also confirms
\[
\mathcal R_0\approx0.9949909838<1
\]
and the explicit failure of the published pointwise comparison:
\[
\dot E_{\mathrm{actual}}=0.0025,
\qquad
\dot E_{\mathrm{claimed\ bound}}=-0.0025.
\]

Finite computation is not used to establish global convergence.
