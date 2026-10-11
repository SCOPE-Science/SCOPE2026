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
p=\frac{(1,0,-1)}{\sqrt2},\qquad q=\frac{(0,1,-1)}{\sqrt2}.
\]
These are adjacent vertices of the spherical square identified as the Gauss image. Their dot product is
\[
\langle p,q\rangle=\frac12,
\]
so their spherical distance is
\[
\arccos\!\left(\frac12\right)=\frac{\pi}{3}.
\]

The same value follows from the stereographic square corners \(z_1=\sqrt2-1\) and \(z_2=i(\sqrt2-1)\): inverse stereographic projection gives two unit vectors with dot product \(1/2\).

Along a face arc, free-boundary orthogonality implies that the surface unit normal is the planar unit normal to the boundary curve, up to sign. Therefore the spherical arclength of the Gauss image is exactly the integral of the planar absolute curvature. The degree-one square mapping assigns one full square side to each of the four boundary arcs.

The packaged checker verifies the two coordinate computations of the square-side length. It does not certify the analytic boundary correspondence; that step rests on the exact Gauss-map theorem and the elementary free-boundary normal identity.

Unproved limits: no pointwise curvature formula, no corner-turning total, and no extension to general tetrahedra.
