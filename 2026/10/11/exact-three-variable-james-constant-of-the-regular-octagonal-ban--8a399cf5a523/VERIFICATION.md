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
The analytic upper bound has two exhaustive pieces. For cyclic gaps
\[
0\le g\le\frac52,
\]
the normed difference is affine before applying the convex norm on each of four polygonal cells, so its maximum is attained at the listed cell vertices. Exact evaluation gives no value above
\[
L=1+\frac1{\sqrt2}.
\]

For
\[
g=\frac52+h,
\qquad
0<h<\frac12,
\]
the proof derives an exact phase criterion for when the distance exceeds \(L\). Three pairwise distances above \(L\) would force three such gaps with excesses summing to \(1/2\); the cyclic phase recurrence then gives an algebraic contradiction.

The sharp triple
\[
x=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right),
\quad
y=\left(\frac{\sqrt2-1}{2},-1\right),
\quad
z=\left(-1,\frac{\sqrt2-1}{2}\right)
\]
is checked exactly and has all three distances equal to \(L\).

`verify.py` implements arithmetic in \(\mathbb Q(\sqrt2)\). It verifies every finite convexity-cell vertex and its exact maximum, reconstructs the sharp triple, and tests the strict-gap criterion and the short-gap bound on exact rational grids. These grids are supplementary; the continuum result is proved symbolically in `RESULT.md`.

No independent audit or independent validation has been performed.
