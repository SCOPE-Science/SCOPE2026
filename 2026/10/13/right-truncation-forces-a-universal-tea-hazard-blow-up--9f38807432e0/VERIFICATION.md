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
Let
\[
B_\theta(x)=1-(1+2\theta x)e^{-2\theta x}
\]
and
\[
A_\theta=B_\theta(1).
\]
Then
\[
B_\theta'(1)=4\theta^2e^{-2\theta}>0.
\]
The published CDF is
\[
F(x)=\left(B_\theta(x)/A_\theta\right)^\alpha.
\]

Taylor expansion at \(x=1\) gives
\[
\overline F(x)
\sim
\frac{\alpha B_\theta'(1)}{A_\theta}(1-x)
\]
and
\[
f(x)\to
\frac{\alpha B_\theta'(1)}{A_\theta}.
\]
Therefore
\[
(1-x)h(x)\to1.
\]

A second-order expansion gives
\[
(1-x)^2h'(x)\to1,
\]
so every hazard is eventually increasing.

The bundled checker evaluates the published formulas directly. For \((\alpha,\theta)=(0.2,1)\), it confirms an interior decline from \(h(0.1)\) to \(h(0.4)\), followed by the required endpoint blow-up.
