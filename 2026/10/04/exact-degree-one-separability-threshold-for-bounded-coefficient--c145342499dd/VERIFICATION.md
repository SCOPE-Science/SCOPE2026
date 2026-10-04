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

The analytic proof reduces every maximum-degree-one term-overlap graph to isolated vertices and edges. The one-term case is a Pauli-parity mixture. For a commuting edge, the nonidentity Pauli coefficient sum is bounded by \(2t+t^2\), which equals one at \(t=\sqrt2-1\). For an anticommuting edge, the coefficient sum is bounded by \(2\beta J\), which is strictly below one at \(\beta J=z_1^*\).

For the sharp commuting witness \(H_*=-J(X\otimes X+Z\otimes Z)\), the partial transpose has minimum eigenvalue
\[
\lambda_{\min}=\frac{1-2t-t^2}{4},\qquad t=\tanh(\beta J),
\]
so its sign changes exactly at \(t=\sqrt2-1\). The included script checks the closed-form identities, coefficient inequalities over a dense coefficient grid, and the partial-transpose sign change on both sides of the threshold.

The checker is a finite replay aid, not a replacement for the analytic argument. Literature priority and later revisions are not independently validated.
