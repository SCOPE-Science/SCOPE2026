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
The bundled checker verifies
\[
\lambda(\phi)
=
\mathcal R_0+\frac{1-\mathcal R_0}{1+c\phi}
\]
and therefore the strict floor
\[
\mathcal R_0<\lambda(\phi)<1
\]
for finite positive \(\phi\).

It verifies that
\[
q(h)=e^{-c(1-\mathcal R_0)h}
\]
reaches the floor at
\[
h_*=
\frac{-\log\mathcal R_0}{c(1-\mathcal R_0)}.
\]

For
\[
\phi(h)=\frac{e^{\mu h}-1}{\mu},
\]
the checker verifies the small-step decay-rate limit and the large-step limits
\[
\lambda(h)\to\mathcal R_0,\qquad
\rho_{\rm NSFD}(h)\to0.
\]

For the exact witness it verifies
\[
\mathcal R_0=\frac12,\quad
h=\log2,\quad
\phi=1,\quad
\lambda=\frac58,\quad
q=\frac1{2\sqrt2},
\]
with
\[
q<\mathcal R_0<\lambda.
\]

No finite experiment is used to prove the structural claim.
