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

The proof was checked symbolically and against the complete primary source.

Checks performed:

- Balanced midpoint rigidity: with \(|A_0|=|A_1|=|A_2|=a\), Brunn--Minkowski gives \(|\tfrac12(A_0+A_2)|\ge a\), while inclusion in \(A_1\) gives the reverse inequality. Equality therefore holds.
- Equality characterization: positive-area equality in Brunn--Minkowski makes \(A_0\) and \(A_2\) homothetic; equal areas force scale one, hence translation. Equal-area inclusion then gives \(A_1=\tfrac12(A_0+A_2)\).
- Shear invariance: \(T(z,x)=(z,x-zv)\) is invertible and restricts on every slice to a translation, so it preserves slice areas and carries halfspaces to halfspaces.
- Horizontal halfspaces: any such halfspace containing the middle point contains at least two full slices, of mass \(2a\).
- Non-horizontal halfspaces: their three slice sections are parallel nested halfplanes. The middle section contains the centroid of \(K\); one outer section contains the middle section.
- Planar centroid inequality: every halfplane containing the centroid of a planar convex body contains at least \(4/9\) of its area. Thus two slices contribute at least \(8a/9\).
- Normalization: since \(\mu(S)=3a\), \((8a/9)/(3a)=8/27\).
- Source comparison: arXiv:2609.32953v1 states the universal \(2/9\) theorem and uses an asymptotically unbalanced sharpness construction; no equal-area constant is stated.

Unproved limits and risks:

- Optimality of \(8/27\) in the equal-area regime is not established.
- No quantitative stability result is proved for nearly equal slice areas.
- Targeted searches cannot rule out a prior equivalent corollary under different terminology.
