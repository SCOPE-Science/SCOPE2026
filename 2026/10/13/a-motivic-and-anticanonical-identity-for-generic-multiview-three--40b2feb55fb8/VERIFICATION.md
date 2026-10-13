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
The checker evaluates the formulas for
\[
2\le n\le500.
\]
For every \(n\) it verifies the Betti vector
\[
(1,n+1,n+1,1),
\]
Euler characteristic
\[
2n+4,
\]
anticanonical cube
\[
64-8n,
\]
and constant identity
\[
(-K)^3+4\chi_{\mathrm{top}}=80.
\]

It also verifies additively that each point blow-up contributes
\[
\mathbb L+\mathbb L^2
\]
to the motive and raises Euler characteristic by
\[
\chi(\mathbb P^2)-\chi(\mathrm{pt})=2.
\]

These computations are regression evidence only. The all-parameter theorem is the symbolic blow-up calculation in `RESULT.md`.
