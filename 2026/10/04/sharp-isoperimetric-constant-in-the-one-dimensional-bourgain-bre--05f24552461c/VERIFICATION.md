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

The primary-source normalization was checked directly. The Fourier transform is
\[
\widehat f(\xi)=\int_{\mathbb R}e^{-ix\xi}f(x)\,dx,
\]
the Hilbert transform is \(H=-i\operatorname{sign}(D)\), and all \(L^2\) pairings in the one-dimensional appendix are Hermitian.

With this convention,
\[
\mathcal F^{-1}(1/\xi)=\frac i2\operatorname{sign}(x).
\]
For mean-zero \(f\), convolution with this kernel gives
\[
|D|^{-1}\operatorname{sign}(D)f=iF,
\qquad
F(x)=\int_{-\infty}^xf(t)\,dt.
\]
Substitution into the source's exact energy-difference identity gives exactly twice the primitive curve's algebraic area.

The sharp geometric step is independently reconstructed. After arclength parameterization and subtraction of the curve mean,
\[
\int|G|^2\le\left(\frac{L}{2\pi}\right)^2\int|G'|^2
\]
by periodic Wirtinger, while Cauchy--Schwarz bounds twice the absolute area by
\[
\left(\int|G|^2\right)^{1/2}
\left(\int|G'|^2\right)^{1/2}.
\]
Since \(|G'|=1\) almost everywhere, this gives
\[
|\mathcal A|\le\frac{L^2}{4\pi}.
\]
The simultaneous equality conditions force a once-traversed circle. The explicit circle primitive verifies the coefficient symbolically.

For general \(L^1_0\) data, the source's annular regularization can be used before passage to the limit. Equivalently, symmetric multiplier truncations justify the pairing identity without presupposing both half-Sobolev energies are finite; the sharp uniform difference bound then supplies the missing component.

No numerical experiment, finite enumeration, or computational certificate is used as proof.
