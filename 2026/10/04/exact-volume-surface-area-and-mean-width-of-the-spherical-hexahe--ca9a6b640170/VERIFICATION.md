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

The exact proof is geometric and does not depend on numerical experiments. The bundled checker verifies the following finite algebraic consequences of the proof:

- the vertex equation and adjacent distance \(\lambda=\sqrt2/3\);
- the exact edge-angle identity \(\cos\alpha=23/27\);
- the exact face-corner cosine \(-1/3\);
- the relation \(\alpha=3\arccos(1/3)-\pi\);
- the Gauss--Bonnet identity for one spherical face;
- the vector-area boundary integral used in the divergence-theorem volume computation;
- the closed volume, surface-area, and mean-width formulas.

As an independent numerical diagnostic, the checker integrates \(r(u)^3/3\) over the unit sphere using the exact radial function
\[
r(u)=\frac{\sqrt{1+\lVert u\rVert_\infty^2}-\lVert u\rVert_\infty}{\sqrt2}.
\]
The quadrature is not used to prove the formula; it only checks the final volume numerically.

The exact argument is limited to the six unit balls with octahedral centers. It does not certify general sphere-intersection formulas or the spherical dodecahedron.
