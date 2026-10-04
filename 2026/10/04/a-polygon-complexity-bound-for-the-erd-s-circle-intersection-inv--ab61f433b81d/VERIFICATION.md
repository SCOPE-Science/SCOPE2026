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
The theorem is proved by exact inequalities and incidence counts; no numerical experiment is needed.

For the polygon bound, the critical check is the sign identity
\[
\frac{d}{dt}|V_1+t(V_2-V_1)-V_0|^2
=2(V_1-V_0)\cdot(V_2-V_1)+2t|V_2-V_1|^2.
\]
When \(\angle V_0V_1V_2\ge\pi/2\), the first dot product is nonnegative, so distance is nondecreasing on \(V_1V_2\). This makes \(V_0V_1\cup V_1V_2\) contribute at most one distinct circle intersection for every radius. The remaining edge count is therefore exactly bounded by \(1+1+2(n-3)=2n-4\).

For a right or obtuse triangle, the same monotonicity leaves exactly two intersections for small positive radii and never more than two. For an acute triangle, the upper bound four follows from centering at a vertex. The lower bound was checked from the boundary distance function: the acute-angle dot products make each relevant vertex a strict local maximum, and a level just below the second-largest vertex value produces four distinct crossings by continuity.

Unproved here: sharpness of \(2n-4\) for general \(n\), exact values for all quadrilaterals or pentagons, and any universal bound for unrestricted planar convex bodies.
