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

The theorem is analytic. The accompanying checker uses exact rational arithmetic.

For rational Marshall–Olkin parameters it verifies the published Kendall, Spearman, and directional Chatterjee formulas and checks the identity
\[
\rho_S=\frac{3\tau}{2+\tau}.
\]

For rational \(t\in(0,1)\), it samples rational values of \(\alpha\) in the exact fixed-tau interval, reconstructs
\[
\beta=\frac{t\alpha}{\alpha(1+t)-t},
\]
and verifies the sharp lower bound and strict upper bound for \(\xi_{Y\mid X}\) by exact cross multiplication.

The checker separately verifies the unique optimizer
\[
\alpha_*=\frac{4t}{t+3},
\qquad
\beta_*=\frac{4t}{1+3t},
\]
the factorized forward-minus-reverse Chatterjee identity, the tail-dependence interval, and reconstruction of the unordered parameter pair from \((t,\lambda_U)\).

The computation does not establish originality and does not replace the derivative proof.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK formula_checks=20000 fiber_checks=47840 optimizer_checks=80 direction_checks=40000 tail_checks=15880`.
