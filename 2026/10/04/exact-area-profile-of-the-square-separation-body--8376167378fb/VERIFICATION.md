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

For
\[
Q=[-1,1]^2,
\]
the published planar isotropic identity gives
\[
m(Q,z)
=
\frac1\pi\left[L(Q^z)-8\right].
\]
Thus \(\partial Q[\delta]\) is the perimeter-excess level
\[
L(Q^z)-8=\pi\delta.
\]

In a side strip, the fixed tangent vertices are the endpoints of one square side, giving an ellipse with major-axis length
\[
2+\pi\delta.
\]
In a corner chamber, the tangent vertices are the two endpoints of the two-edge boundary chain through the corner, giving an ellipse with major-axis length
\[
4+\pi\delta.
\]

Writing
\[
a=1+\frac{\pi\delta}{2},\qquad b^2=a^2-1,\qquad \beta^2=(a+1)^2-2,
\]
the exact one-side and one-corner area increments are
\[
S=\frac{b^2}{a}+ab\arcsin\!\left(\frac1a\right)
\]
and
\[
C=(a+1)\beta\arcsin\!\left(\frac{b^2}{\sqrt2\,a(a+1)}\right)-\frac{b^2}{a}.
\]
Therefore
\[
\operatorname{Area}(Q[\delta])=4+4S+4C,
\]
which simplifies to the claimed formula.

The embedded `verify.py` was replayed from its actual package path. It reconstructs convex hulls of the square and sampled exterior points, verifies the perimeter excess on both ellipse families, checks the shared transition point, and independently integrates the radial sublevel set in \(2048\) directions.

The replay output was:

`VERIFY_OK square separation-body area profile`

The numerical tests are finite consistency checks only. The all-parameter formula follows from the exact chamber geometry and integrations in `RESULT.md`.
