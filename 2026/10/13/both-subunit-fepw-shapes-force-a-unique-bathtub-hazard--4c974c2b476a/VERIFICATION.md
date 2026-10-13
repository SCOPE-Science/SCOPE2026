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
For
\[
h(x)=\eta\tau^\eta x^{\eta-1}e^{(\tau x)^\eta}+\varphi\kappa^\varphi x^{\varphi-1},
\]
set
\[
z=(\tau x)^\eta,
\qquad
z_0=(1-\eta)/\eta.
\]
The derivative is
\[
h'(x)=\eta\tau^\eta x^{\eta-2}e^z(\eta z+\eta-1)-\varphi(1-\varphi)\kappa^\varphi x^{\varphi-2}.
\]
For \(z>z_0\), the ratio \(R\) of the positive first term to the magnitude of the negative second term satisfies
\[
\frac{d}{dz}\log R
=1+\frac{\eta-\varphi}{\eta z}+\frac{\eta}{\eta z+\eta-1}.
\]
Writing \(z=z_0+s\), multiplication by the positive denominator yields
\[
\eta\{\eta s^2+(1+\eta-\varphi)s+(1-\eta)\}>0.
\]
Thus \(R\) is strictly increasing from zero to infinity and has exactly one crossing of one.

The bundled checker evaluates the derivative directly, compares the analytic and numerical logarithmic derivatives of \(R\), and solves the unique crossing for several parameter sets. For the first decreasing-hazard Figure 2(b) configuration it returns
\[
x_0\approx3.7589973457546\times10^{27}
\]
and
\[
x_*\approx1.7683454747093\times10^{30}.
\]
The finite computations support reproducibility only; uniqueness follows from the analytic monotonicity proof.
