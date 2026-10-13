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

The universal proof is symbolic and analytic. With \(d=c-ab\), positive semidefiniteness is equivalent to
\[
|d|\le\sqrt{(1-a^2)(1-b^2)}.
\]
Conditioning on \(X_1\), applying Isserlis' formula, and using the exact normal moment recurrences reduces the normalized target to
\[
B+4ab(1-\alpha)d+2d^2.
\]
Completing the square and projecting the unconstrained minimizer onto the admissible interval yields the claimed formula and optimizer. The comparison to the earlier factor is the exact identity
\[
L_{\mathrm{unconstrained}}-(1-a^2)(1-b^2)
=(1-\alpha)\bigl(a^2+b^2-(1-\alpha)a^2b^2\bigr),
\]
which is strictly positive unless \(a=b=0\).

The accompanying exact-rational script checks representative Pythagorean correlation pairs and several rational exponents in both optimizer regimes. These computations only guard algebraic transcription and implementation; they are not an exhaustive proof over real parameters.

Scientific limits: three standardized Gaussian coordinates, \(0<\alpha<1\), and two square factors. No assertion is made for higher-dimensional fixed-edge optimization or arbitrary positive exponents.
