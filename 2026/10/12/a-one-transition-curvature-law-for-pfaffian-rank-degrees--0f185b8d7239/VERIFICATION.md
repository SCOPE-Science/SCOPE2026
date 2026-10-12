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
For
\[
s=n-2r-1,
\]
the starting degree formula is
\[
D_{n,s}
=
\prod_{1\le i\le j\le s}
\frac{n-s-1+i+j}{i+j}.
\]

Exact factorial cancellation gives
\[
\frac{D_{n,s}}{D_{n,s-2}}
=
\frac{\prod_{k=-(s-1)}^{s-1}(n+k)}
{(2s)!\,C_{s-1}}.
\]
Taking one more adjacent quotient gives the stated curvature ratio.

The monotonicity certificate is the polynomial identity
\[
Q_n(s+2)-Q_n(s)
=
-4(2s+3)\bigl(n^2+255s^2+765s+701\bigr),
\]
which is strictly negative on the admissible domain.

The bundled checker uses exact rational arithmetic for all admissible levels with
\[
4\le n\le120.
\]
It verifies the source degree product, the adjacent-ratio formula, the curvature identity, the two-step sign decrease, and the correspondence between the sign of \(Q_n(s)\) and the logarithmic-curvature inequality.

The finite computation is regression evidence only. The proof is symbolic.
