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
The inverse formulas from Proposition 3.1 were replayed symbolically. For \((\Phi_E^a)^{-1}\), the finite witness at coordinate \(N\) has output coefficient
\[
a^{-(N-1)}+\sum_{m=1}^{N-1}a^{-m},
\]
whose supremum is \(\max\{1,1/(a-1)\}\). For \((\Psi_E^{b,c})^{-1}\), independent finite alternating tails yield coefficients converging to \(1/(b-1)\) and \(b/[c(b-1)]\). Every input used has norm \(1\) and finite support.

The distortion functions were then checked on their natural parameter regions: \(1<a\le2\) versus \(a\ge2\), and \(c\le b\) versus \(c\ge b\). Their monotonicity gives the unique minima \(a=2\) and \(c=b\), while \((b+1)/(b-1)\to1\) only as \(b\to\infty\).

No numerical experiment, external certificate, or independent audit was used. The limiting arguments establish operator-norm suprema and do not assert norm-attaining vectors at the limiting values.
