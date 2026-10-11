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

The analytic proof reduces all convexity constraints to
\[
O\cdot u_j\le c_k,
\qquad
0\le j<3k,
\]
where
\[
c_k=\cos\!\left(\frac{\pi(k+1)}{3k}\right).
\]

The key local identity is obtained by rotating one pair of endpoint vertices to
\[
(c_k,-s_k),\qquad(c_k,s_k),
\]
with
\[
s_k=\sin\!\left(\frac{\pi(k+1)}{3k}\right).
\]
For a rotated center \((x,y)\),
\[
\det(P_j-O,P_{j+k+1}-O)
=
2s_k(c_k-x).
\]
Therefore the sign controlling whether the source's wedge angle is at most \(\pi\) is exactly the sign of the claimed half-plane slack.

For \(k\ge3\), the half-plane normals are equally spaced by \(2\pi/(3k)\). Hence the feasible region is a regular \(3k\)-gon with
\[
R_k
=
\frac{c_k}{\cos(\pi/(3k))}
=
\frac12-\frac{\sqrt3}{2}\tan\!\left(\frac{\pi}{3k}\right),
\]
and
\[
A_k
=
3k c_k^2\tan\!\left(\frac{\pi}{3k}\right).
\]
For \(k=2\), \(c_k=0\) and opposite half-planes collapse the center set to the origin.

The bundled checker samples these identities for all \(2\le k\le200\), reconstructs polygon vertices from adjacent support lines, verifies their circumradii and shoelace areas, and checks the stated limits numerically.

Those finite checks are supplementary. The classification for every \(k\ge2\) follows from the exact determinant identity and regular-polygon geometry, not from sampling.

No claim is made about non-spiral equicoverings or measures other than normalized arclength on the unit circle.
