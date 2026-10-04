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

The verification is proof-based and has no numerical dependency.

1. **Aging and scaling.** A black level-2 triangle \([ab][ac][bc]\) is the medial triangle of \(abc\); a white level-2 triangle \([xa][xb][xc]\) is a translated copy of \(abc\) scaled by \(1/2\). Therefore smallest-enclosing-circle radii scale by exactly \(1/2\).

2. **Deletion triangulations.** For any complete level-2 hypertriangulation aged from \(P\), rescaled white triangles rooted at \(x\) triangulate \(\operatorname{st}(P,x)\cap\operatorname{conv}(A\setminus\{x\})\). Replacing the star by this region and retaining all nonincident triangles gives a complete triangulation \(P^{-x}\) of \(A\setminus\{x\}\). Hence
\[
2c(H)=\max\!\left(c(P),\max_{x\in A}c(P^{-x})\right).
\]

3. **Delaunay identification.** At order \(2\), black triangles have empty circumcircles in \(A\), while a white triangle rooted at \(x\) has exactly \(x\) inside its circumcircle. After deleting \(x\), the latter circle is empty. Conversely, every triangle of \(\operatorname{Del}(A\setminus\{x\})\) sees \(x\) strictly inside or outside its circumcircle because no four points are cocircular, giving respectively a white or black order-2 triangle. Thus the deletion triangulations of \(\operatorname{Del}_2(A)\) are exactly \(\operatorname{Del}(A\setminus\{x\})\).

4. **Extremal step.** Rajan's Theorem 2 states that ordinary Delaunay minimizes maximum min-containment radius. Applying that theorem separately to \(P\) and every \(P^{-x}\) and then taking the maximum proves the level-2 inequality.

The proof explicitly covers convex-hull deletions through the intersection with \(\operatorname{conv}(A\setminus\{x\})\), and it uses \(\#A\ge 4\) so every deletion remains triangulable. No claim depends on an experiment, a timeout, or an incomplete enumeration.
