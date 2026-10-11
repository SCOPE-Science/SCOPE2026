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
The proof in `RESULT.md` is symbolic.

Critical checks:
- for a connected rank-function quiver, the affine hull has codimension two;
- the centered rank vector is orthogonal to \(\mathbf1\);
- every arrow root has squared norm \(2\) and centered-rank scalar product \(-1\);
- the orthogonal projection center is \(-r/S\);
- every vertex has exact squared distance \(2-1/S\);
- a common sphere is minimum enclosing exactly when its center belongs to the vertex convex hull;
- barycentric membership is equivalent to a nonnegative arrow flow with the prescribed divergence;
- max-flow/min-cut is equivalent to nonpositive centered-rank sum on every lower ideal.

`verify.py` uses exact rational arithmetic on connected graded quivers with up to five labeled vertices. It checks the sphere identity and compares the lower-ideal criterion with an independent rational max-flow feasibility test. It also checks an explicit connected graded quiver where the criterion fails. Finite computation is corroborative only and does not assess originality.
