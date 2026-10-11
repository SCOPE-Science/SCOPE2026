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
# Verification

The analytic chain checked is
\[
\log\!\frac1{1-p}=\int_0^T\!\left[(x-\alpha)(1-x)-\frac{\lambda y}{x+y}\right]dt,
\]
\[
y(0)>\tau,\qquad \dot y\ge-\beta y,\qquad y(t)>\tau e^{-\beta t},\qquad x(t)<h,
\]
and therefore
\[
\log\!\frac1{1-p}<\rho T-\frac{\lambda}{\beta}\log\!\frac{h+\tau}{h+\tau e^{-\beta T}}.
\]
The packaged script checks the piecewise \(\rho\), the condition \(\rho\ge\lambda\tau/(h+\tau)\), monotonicity of \(F\), and the two reported roots by bracketing and bisection. It does not numerically integrate an orbit and is not used as a substitute for the proof.

Scientific limits: existence, stability, sharpness, higher-order cycles, and uniqueness of a root when the monotonicity condition fails are not proved.
