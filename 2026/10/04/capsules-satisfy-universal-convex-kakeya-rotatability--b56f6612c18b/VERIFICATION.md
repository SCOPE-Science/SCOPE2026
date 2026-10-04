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

The central identity is
\[
\rho(T+rB_2^d)+w
=
\rho T+w+rB_2^d
\]
because
\[
\rho B_2^d=B_2^d
\]
for every
\[
\rho\in\operatorname{SO}(d).
\]

For
\[
C=K\ominus rB_2^d
=
\{x:x+rB_2^d\subset K\},
\]
one therefore has
\[
\rho(T+rB_2^d)+w\subset K
\]
if and only if
\[
\rho T+w\subset C.
\]

This is a two-sided logical equivalence for each individual placement, not only an implication at the level of existence. Consequently the rotation and translation parameter pairs for thickened copies in \(K\) are exactly the same parameter pairs as for unthickened copies in \(C\). Any continuous path of one type is therefore a continuous path of the other type.

The eroded host is compact and convex because
\[
K\ominus rB_2^d
=
\bigcap_{b\in rB_2^d}(K-b).
\]

For a segment \(L\), Janzer's Theorem 1.2 gives path-connectivity for unit length; similarity gives every positive length. This proves the capsule result.

The embedded `verify.py` was replayed from its actual package path. For random polyhedral halfspace hosts in dimensions \(2\) through \(5\), it checks the support-function form
\[
h_{\rho L+w}(a)+r\lVert a\rVert\le b
\]
against the eroded-host condition
\[
h_{\rho L+w}(a)\le b-r\lVert a\rVert.
\]
It also checks the parallel and perpendicular capsule widths.

The replay output was:

`VERIFY_OK capsule Kakeya erosion reduction`

These finite tests are consistency checks only. The theorem is proved by the exact set identity above.
