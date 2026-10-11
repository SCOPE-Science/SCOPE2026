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

The checker reconstructs the boundary chord identity
\[
\lVert r(t)-r(s)\rVert^2
=4\sin^2d\left(a^2\sin^2m+b^2\cos^2m\right)
\]
with \(m=(t+s)/2\) and \(d=(t-s)/2\).

For the minor-axis half it verifies the reduction to
\[
4u\left(a^2-(a^2-b^2)u\right),\qquad 0\le u\le1,
\]
and its exact maximum on both sides of \(a^2=2b^2\).

For the elongated regime it checks
\[
\sin^2d_*=\frac{a^2}{2(a^2-b^2)},
\qquad
L(d_*)^2=2a^2,
\qquad
M^2=\frac{a^4}{a^2-b^2},
\]
plus the inequality \(L(d_*)>M\) under \(a^2>2b^2\). It also verifies the explicit later-orientation witness and threshold continuity.

Dense numerical scans over boundary pairs and center-line orientations are included only as regression tests. They are not used to infer the universal theorem.
