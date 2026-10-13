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
The verification script expands
\[
P_n(q)=\frac{(1-q^{n+1})(1-q^n)(1-q^{n-1})}{(1-q)^2(1-q^2)}
\]
by exact integer polynomial arithmetic for every \(2\le n\le300\).

For each \(n\), it checks palindromicity, the exact maximum \(\lfloor3n^2/8\rfloor\), and the claimed plateau indices in all three residue classes. It also verifies strict increase before the plateau and strict decrease after it.

Independently, it reconstructs the first differences from
\[
c(j)=\left\lfloor j/2\right\rfloor+1
\]
and checks the symbolic simplifications used in the proof throughout the range containing the center.

Finite computation is regression evidence only. The infinite result follows from the coefficient identities in `RESULT.md`.
