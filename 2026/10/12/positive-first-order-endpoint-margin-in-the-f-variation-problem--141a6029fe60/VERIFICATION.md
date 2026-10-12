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

The proof is analytic. For \(t_\pm=d\pm\sqrt{2d}\) and
\[
b_\pm=2d\pm\frac{d+6}{2}\sqrt{2d},
\]
the critical identity is
\[
b_\pm+\left(\frac d2-1\right)t_\pm-\frac{t_\pm^2}{2}
=
\pm2\sqrt{2d}.
\]
Together with the exact first four centered moments of \(V/m-1\), this yields the displayed \(m^{-1}\) coefficient and an \(O_d(m^{-2})\) remainder.

The standalone script `verify_f_endpoint.py` implements regularized beta and gamma functions using only the Python standard library. It compares exact finite F central probabilities with the asymptotic coefficient for several numerator and denominator degrees and prints:
`VERIFY_OK max_scaled_error=0.00483207616522`.

Finite calculations are regression checks only. No explicit or uniform threshold \(M_d\) is certified.
