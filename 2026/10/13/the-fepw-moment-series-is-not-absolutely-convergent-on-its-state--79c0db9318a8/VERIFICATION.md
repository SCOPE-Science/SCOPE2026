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
At
\[
r=\tau=\eta=\kappa=\varphi=1,
\]
the coefficient in the source's Eq. (3.2) is
\[
a_{i,j}
=
e\frac{(-1)^i i^j}{i!}.
\]
Hence
\[
a_{1,j}=-e
\]
for every \(j\), which proves that the published double series is not absolutely convergent at this admissible point.

The true mean is
\[
\mu_1
=
e\int_0^\infty e^{-e^x-x}\,dx
=
e\Gamma(-1,1).
\]
The included checker compares high-precision quadrature with the incomplete-gamma value and obtains agreement.

For
\[
\eta=\varphi=p,
\qquad
c=(\kappa/\tau)^p,
\]
the transformed moment identity is
\[
\mu_r
=
\frac{r e}{p\tau^r}
\int_1^\infty
(\log z)^{r/p-1}z^{-c-1}e^{-z}\,dz.
\]
The checker also compares this representation with the original survival integral at a second positive parameter point.

Finite rectangular truncations are reported only as an illustration of numerical instability. The scientific proof of the convergence failure is the exact nonzero row term.
