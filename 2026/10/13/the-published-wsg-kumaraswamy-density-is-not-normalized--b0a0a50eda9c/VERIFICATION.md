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
Let
\[
\theta(y)=\frac{\pi}{2}(1-y^\delta)^\alpha.
\]
The published CDF is
\[
F(y)=\cos\theta(y)e^{1-\cos\theta(y)}.
\]
Differentiation gives
\[
F'(y)=
\frac{\pi}{2}\delta\alpha y^{\delta-1}(1-y^\delta)^{\alpha-1}
\sin\theta(y)e^{1-\cos\theta(y)}[1-\cos\theta(y)].
\]

The corrected density has unit mass because
\[
\int_0^{\pi/2}\sin t\,e^{1-\cos t}(1-\cos t)\,dt
=
\int_0^1 u e^u\,du
=1.
\]

The printed cosine-factor kernel has mass
\[
I=\int_0^{\pi/2}\cos t\,e^{1-\cos t}(1-\cos t)\,dt.
\]
With \(s=\sin t\) and \(x(s)=1-\sqrt{1-s^2}\),
\[
I=\int_0^1 x(s)e^{x(s)}ds
\le e\left(1-\frac{\pi}{4}\right)<1.
\]
High-precision quadrature gives
\[
I=0.3449927969472642938\ldots .
\]

The bundled checker compares numerical derivatives of the CDF with the corrected density, integrates both corrected and published kernels for multiple parameter pairs, and verifies the universal published mass. These computations support, but are not required for, the analytic proof.
