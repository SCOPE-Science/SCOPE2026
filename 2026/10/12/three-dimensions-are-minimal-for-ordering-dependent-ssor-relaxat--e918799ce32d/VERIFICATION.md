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
The universal statements are proved analytically in `RESULT.md`. The checker replays exact algebraic identities at rational parameters and verifies the concrete \(r=1/2\) derivative sign.

For every normalized \(2\times2\) test matrix, the generalized characteristic polynomial has product
\[
1-\rho^2
\]
and sum
\[
2-\rho^2+\rho^2(\omega-1)^2.
\]
The checker confirms this identity at several rational values of \(\rho\) and \(\omega\).

For the natural three-node path at \(r=1/2\), it verifies
\[
F(\lambda,1)
=-(\lambda-1)
\left(
\lambda^2-\frac{23}{16}\lambda+\frac12
\right)
\]
and the exact derivative
\[
\frac{d}{d\omega}\kappa(M_\omega^{-1}A_{1/2})\bigg|_{\omega=1}
=-\frac18-\frac{23\sqrt{17}}{136}<0.
\]

For the center-first ordering, it verifies that the nontrivial generalized roots have product \(1-2r^2\) and sum
\[
2-2r^2+2r^2(\omega-1)^2,
\]
so \(\omega=1\) is the unique optimum whenever \(r\ne0\).

Finite replay is corroborative only. The minimal-dimension theorem follows from the analytic all-\(2\times2\) proof and the exact three-dimensional family.

Unproved limits include the global optimal relaxation for arbitrary \(3\times3\) SPD matrices, higher-dimensional classifications, finite-precision effects, and cost-aware ordering choices.
