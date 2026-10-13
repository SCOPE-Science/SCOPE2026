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

The analytic proof is in `RESULT.md`. The standalone checker reconstructs the ordered-sample matrix \(A\) and centered quadratic-form matrix \(B\) exactly over the rationals.

For each
\[
2\le n\le8,
\]
the checker evaluates the raw expectations of the linear maximum form, the quadratic sample-variance form, their product, and the square of the quadratic form directly from
\[
\mathbb E[Z^k]=k!
\]
for \(Z\sim\operatorname{Exp}(1)\).

It verifies the claimed covariance and sample-variance formulas without invoking the linear/quadratic covariance identity used in the proof. It also verifies every row-sum identity for \(B\).

Finally, it checks numerically that
\[
\operatorname{Corr}(M_n,S_n^2)
\frac{\sqrt n}{(\log n)^2}
\]
approaches
\[
\frac{\sqrt3}{2\pi}.
\]

The finite replay is supplementary. The theorem for arbitrary \(n\) follows from the independent-spacing representation and exact matrix calculation.

Independent audit has not been performed.

Deterministic replay result: `VERIFY_OK mean_checks=7 direct_covariance_checks=7 direct_variance_checks=7 row_sum_checks=35 asymptotic_checks=3 target=0.275664447711 last_ratio=0.307423361123`.
