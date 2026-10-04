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

The critical analytic steps were checked directly.

The source normalization with \(v(r)=\omega^2r^2\) gives the physical interaction \(\omega^2(x_1-x_2)^2/2\). In the symmetric rotated wedge the form is
\[
q_+[u]=\int\left(|u_r|^2+|u_s|^2+\omega^2r^2|u|^2\right).
\]
The transverse factorization gives the exact one-dimensional threshold \(\omega\), with ground state proportional to \(e^{-\omega r^2/2}\).

For
\[
u_b(r,s)=e^{-\omega r^2/2-b\sqrt\omega s},
\]
direct integration gives
\[
\frac{q_+[u_b]}{\|u_b\|^2}=\omega\left(1+3b^2-2b\frac{e^{-b^2}}{\sqrt\pi\operatorname{erfc}(b)}\right).
\]
At \(b=1/3\), the proof does not rely on floating-point evaluation. It uses the strict bounds \(e^{-1/9}>8/9\), \(e^{-t^2}>1-t^2\) for \(0<t\le1/3\), the classical \(\pi<22/7\), and exact rational comparisons to obtain
\[
\frac{e^{-1/9}}{\sqrt\pi\operatorname{erfc}(1/3)}
>\frac{72000}{91613}>\frac{157}{200}.
\]
This yields the strict Rayleigh bound \(81\omega/100\) for every \(\omega>0\).

The accompanying standard-library script checks the exact integer cross-multiplications and numerically corroborates the closed-form quotient and its scale invariance. It does not certify the infinite statement; that follows from the analytic inequalities above.

The verification does not establish optimality of the constant, the exact ground energy, or uniqueness of the quadratic-model discrete eigenvalue.
