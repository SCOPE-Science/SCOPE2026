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

The computation uses the unit-circumradius regular decagon with support half-spaces
\[
u_j\cdot x\le\cos(\pi/10).
\]
For
\[
d(t)=(1-t)v_0+t v_1,
\]
the feasible starting points of chords are exactly
\[
P_{10}\cap(P_{10}-d(t)).
\]

On
\[
0\le t\le\tau,
\qquad
\tau=\frac{3-\sqrt5}{2},
\]
the active constraints are \(u_3\) from the original decagon and \(u_1\) from the translate. On
\[
\tau\le t\le\frac12,
\]
they are \(u_3\) and translated \(u_2\).

The checker reconstructs both intersections from these equations. Every unused inequality is affine in \(t\), so nonnegativity at the two interval endpoints proves it on the full interval. The objective-normal decompositions are
\[
n(t)=
\frac{(3-\sqrt5)t+\sqrt5-1}{2}u_3
+
\frac{(\sqrt5-1)(1-t)}{2}u_1
\]
on the first interval and
\[
n(t)=t u_3+(1-t)u_2
\]
on the second.

The resulting height ratios are checked against
\[
r_1(t)=
\frac{3\sqrt5-5}{2}
+\frac{11-5\sqrt5}{2}t
+(\sqrt5-2)t^2
\]
and
\[
r_2(t)=
1-\frac{\sqrt5-1}{2}t(1-t).
\]

Finally,
\[
r_1(0)=r_1(\tau)=r_2(\tau)=\frac{3\sqrt5-5}{2},
\]
\[
r_1''=2(\sqrt5-2)>0,
\]
and \(r_2\) is strictly decreasing on \([\tau,1/2]\). These identities certify the claimed maximum.

The checker uses high-precision algebraic evaluation only to replay trigonometric simplifications; the continuum proof rests on the exact active-normal formulas, affine endpoint feasibility, and exact quadratic inequalities.
