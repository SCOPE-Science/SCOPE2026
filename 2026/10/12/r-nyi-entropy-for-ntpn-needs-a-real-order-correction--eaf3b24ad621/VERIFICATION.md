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
For the NTPN density,
\[
f(x)
=
C^{-1}q(x)(2\pi)^{-1/2}
e^{-(x^2+\lambda^2)/2}
\cosh(\lambda x),
\]
the Rényi integral is
\[
C^{-\gamma}(2\pi)^{-\gamma/2}e^{-\gamma\lambda^2/2}
\int_{\mathbb R}
q(x)^\gamma e^{-\gamma x^2/2}
\cosh(\lambda x)^\gamma\,dx.
\]
If
\[
Z_\gamma\sim N(0,1/\gamma),
\]
this equals
\[
C^{-\gamma}(2\pi)^{-\gamma/2}e^{-\gamma\lambda^2/2}
\sqrt{\frac{2\pi}{\gamma}}\,
\mathbb E\!\left[
q(Z_\gamma)^\gamma
\cosh(\lambda Z_\gamma)^\gamma
\right].
\]

The expectation is finite because a polynomial times
\[
\exp\!\left(-\frac{\gamma x^2}{2}+\gamma\lambda|x|\right)
\]
is integrable for every \(\gamma>0\).

The bundled checker evaluates direct quadrature and the Gaussian-expectation representation independently at noninteger orders and verifies the standard-normal formula. These are consistency checks; the proof of the domain correction is algebraic.
