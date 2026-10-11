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

The infinite statement is established analytically in `RESULT.md`.

The one-step calculation uses the exact transformed fiber
\[
[-\lambda\ell,(1-\lambda)\ell].
\]
Reflection about the possible center \(tu\) changes this to
\[
[2t-(1-\lambda)\ell,\;2t+\lambda\ell].
\]
Equality with the opposite fiber gives
\[
2t=(1-2\lambda)\ell.
\]
For \(\lambda<1/2\), this can hold for all projected fibers only when their length is constant.

The constant-length condition makes the two convex boundary functions sum to a constant. Hence each is affine, and the body is exactly the Minkowski sum of one facet and a segment in direction \(u\).

The countability step uses only that distinct facets have disjoint relative interiors of positive \((n-1)\)-dimensional Hausdorff measure and that the boundary of a convex body has finite surface area.

The bundled checker confirms the interval-reflection algebra for exact rational sample parameters, verifies the resulting symmetry center for prism fibers, and checks a representative strictly convex ellipsoid has nonconstant parallel chord lengths.

Finite checks are supplementary and are not used as a substitute for the all-dimensional proof.
