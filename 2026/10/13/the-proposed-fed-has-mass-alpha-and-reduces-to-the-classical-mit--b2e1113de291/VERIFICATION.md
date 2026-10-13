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
The exact identity
\[
-\frac{d}{dx}E_\alpha(-\lambda x^\alpha)
=
\lambda x^{\alpha-1}E_{\alpha,\alpha}(-\lambda x^\alpha)
\]
is obtained by termwise differentiation of the entire defining series.

Therefore the corrected density has unit mass and the published density has mass
\[
\alpha.
\]
The source's claimed survival in Eq. (6.20) is consistent with the corrected density, not with Eq. (6.17).

For \(0<\alpha<1\), the published asymptotic
\[
E_\alpha(-\lambda x^\alpha)
\sim
\frac{x^{-\alpha}}{\lambda\Gamma(1-\alpha)}
\]
and the tail-integral formula imply
\[
\mathbb E[X^r]<\infty
\iff
r<\alpha.
\]

The bundled checker uses the closed form at \(\alpha=1/2\),
\[
E_{1/2}(-\lambda\sqrt{x})
=
e^{\lambda^2x}\operatorname{erfc}(\lambda\sqrt{x}),
\]
to verify the normalization factor, tail constant, and divergent mean behavior numerically. These computations are consistency checks; the proof is analytic.
