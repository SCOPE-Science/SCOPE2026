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

Let
\[
a=\frac{\pi}{2n},
\qquad
H=\sqrt{4\cos^2 a-1},
\]
and define
\[
\gamma=\frac{H}{\sqrt3\cos a},
\qquad
\zeta=\frac{\tan a}{\sqrt3}.
\]
The proof uses the exact identities
\[
\gamma^2+\zeta^2=1
\]
and
\[
\zeta H=\gamma\sin a.
\]

At the representative upper vertex, the outward facet normals are
\[
e_3,
\qquad
(\gamma,0,-\zeta),
\qquad
(\gamma\cos2a,\pm\gamma\sin2a,\zeta).
\]
For
\[
d_\phi=(\cos\phi,\sin\phi,H),
\]
their scalar products are
\[
H,
\qquad
\gamma(\cos\phi-\sin a),
\qquad
\gamma(\cos(\phi\mp2a)+\sin a).
\]
Therefore the line \(\mathbb R d_\phi\) X-rays that vertex exactly when
\[
\operatorname{dist}_{S^1}(\phi,0)
<
\frac{\pi}{2}-a.
\]

The checker verifies the coordinate edge lengths, these scalar-product identities, the transformed lower-ring criterion, and complete coverage by the three prescribed lines for every integer from \(3\) through \(200\). It also verifies that the displayed base and triangular normals have negative scalar product, so the family is outside the almost-smooth hypothesis.

The finite range is diagnostic only. The proof for all integers \(n\ge3\) is the symbolic normal calculation plus the fact that three open arcs of radius at least \(\pi/3\), centered \(2\pi/3\) apart, cover all relevant transformed vertex azimuths.
