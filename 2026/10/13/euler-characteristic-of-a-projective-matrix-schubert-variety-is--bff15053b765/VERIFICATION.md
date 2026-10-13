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
The checker enumerates every permutation for
\[
1\le n\le7.
\]

For each \(w\), it constructs
\[
r_w(i,j)
=
\#\{k\le j:w(k)\le i\}
\]
directly.

For every coordinate matrix \(E_{ij}\), it tests every northwest rank condition without using the closed formula. The resulting fixed-point count is compared with
\[
\sum_{j=1}^{n}(n-m_j+1).
\]

It also verifies the sharp lower and upper bounds, the unique minimum at the long permutation, and the maximum criterion \(w(1)=1\).

Finite checks are regression evidence only. The infinite theorem is proved by the torus fixed-point argument in `RESULT.md`.
