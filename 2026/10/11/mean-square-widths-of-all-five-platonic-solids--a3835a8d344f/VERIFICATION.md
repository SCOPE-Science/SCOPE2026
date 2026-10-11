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

For a unit-edge centrally symmetric regular polyhedron with \(N\) vertices, circumradius \(R\), and valency \(q\), one vertex normal cell \(C\) satisfies
\[
h(u)=R\cos\theta,
\qquad
\sin\delta=\frac1{2R}.
\]
Splitting \(C\) into \(q\) sectors of azimuthal half-width
\[
\alpha=\frac\pi q
\]
gives
\[
\tan\theta_b(\psi)=\frac{\tan\delta}{\cos\psi}.
\]
Direct integration yields
\[
\int_C\cos^2\theta\,d\sigma
=
\frac q3\left[
2\alpha
-2\arcsin(\sin\alpha\cos\delta)
+\frac{
2\sin^2\delta\sin\alpha\cos\delta
}{
\sqrt{1-\sin^2\alpha\cos^2\delta}
}
\right].
\]
Central symmetry then gives
\[
\mathbb E\,w^2
=
\frac{NR^2}{\pi}
\int_C\cos^2\theta\,d\sigma.
\]

The checker reconstructs standard unit-edge coordinates for the cube, octahedron, dodecahedron, and icosahedron and confirms the radius and cell-inradius data used in each substitution. It numerically re-integrates the sector formula and directly integrates support functions on a deterministic spherical grid.

The tetrahedron is not covered by the central-symmetry reduction; its exact second moment is the published Finch formula and is independently checked numerically from unit-edge vertex coordinates.

All numerical calculations are regression tests only. The universal continuum statements for the four centrally symmetric solids follow from the exact sector antiderivative, not from finite sampling.
