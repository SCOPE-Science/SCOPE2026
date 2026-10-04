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

The proof was checked from the support-line model of a regular polygon.

Set
\[
\delta=\frac{\pi}{2N},\qquad c=\cos(2\delta),\qquad
q=\frac{c}{\sqrt2\cos\delta}.
\]
At zero rotation, the diagonal \(y=x\) hits the boundary at \((q,q)\), which gives the necessary lower bound \(t\ge1/(2q)\) from the published coordinate-symmetric covering criterion.

For the sufficient direction, the only nonstandard calculation is the following identity. If side normals are \(a+u\) and \(-(a-u)\), both at support distance \(c\), and
\[
q=\frac{c}{\sin a+\cos a},
\]
then the half vertical-chord length \(h\) at \(x=q\) satisfies
\[
h-q=
\frac{c(1-\cos u)
\left[1+\cos u-\sin a(\sin a+\cos a)\right]}
{(\sin a+\cos a)\sin(a+u)\sin(a-u)}.
\]
This was algebraically expanded from the two line equations. In the required ranges
\[
\frac{\pi}{6}\le a\le\frac{\pi}{3},\qquad |u|\le\frac{\pi}{6},
\]
the denominator is positive and
\[
1+\cos u\ge1+\frac{\sqrt3}{2}
>
\frac{3+\sqrt3}{4}
\ge\sin a(\sin a+\cos a).
\]
Hence \(h\ge q\).

For \(N\equiv2\pmod8\), use \(a=\pi/4+\delta\) and \(u=\theta\). For \(N\equiv6\pmod8\), the two possible lower active sides give either \(a=\pi/4-\delta,\ u=\theta\), or \(a=\pi/4+\delta,\ u=\theta-2\delta\). These cases exhaust the reduced orientation interval.

The closed form was also symbolically checked to reproduce both published small cases \(N=6\) and \(N=10\). Numerical sampling across additional values of \(N\) was used only as a development sanity check and is not part of the proof.

No claim is made for odd \(N\) or for a lattice other than \(\mathbb Z^2\).
