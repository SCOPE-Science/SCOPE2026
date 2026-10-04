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

For \(A>0\), \(B\ge0\), and \(\beta\in(0,1)\), the checked boundary is
\[
R_\beta(B)=\frac{A}{\beta(1-\beta)}+\frac{B}{1-\beta}.
\]
The derivative numerator is \(B\beta^2+2A\beta-A\), with exactly one root in \((0,1)\). Substitution of
\[
\beta^*=\frac{\sqrt A}{\sqrt A+\sqrt{A+B}}
\]
returns
\[
R_{\beta^*}(B)=\left(\sqrt A+\sqrt{A+B}\right)^2.
\]
The difference from \(\beta=1/2\) simplifies exactly to
\[
\left(\sqrt{A+B}-\sqrt A\right)^2.
\]

The standalone `artifacts/verify.py` script evaluates these identities across a grid of positive \(A\), nonnegative \(B\), and dense temperatures, verifies that no grid point beats the analytic optimizer within numerical tolerance, and checks convergence of the optimized-to-default ratio toward \(1/2\) for large \(B/A\). A successful run prints `VERIFY_OK`.

The finite calculations are consistency checks only. The proof of global optimality is the analytic derivative/sign argument together with divergence at the two endpoints.
