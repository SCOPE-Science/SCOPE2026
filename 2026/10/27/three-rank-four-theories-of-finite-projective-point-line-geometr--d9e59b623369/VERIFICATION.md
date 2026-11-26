---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The nested sets of atomic extension types, with equality and the two named sorts, give the full rank-four theory. With three named distinct objects, singleton incidences to up to three opposite objects survive their at most two intersection/join exclusions. Double and triple incidences reduce to joining or intersecting, and to collinearity/concurrence. For three lines in a plane the uncovered counts are q(q-2) if concurrent and (q-1)^2 otherwise, with the dual counts for three points. Two objects of one sort leave at least two objects of the other sort avoiding both, so a third previously named object cannot exhaust the avoidance pattern. In dimension at least three the three-object avoidance cases already have witnesses in a containing 3-space (or for three spanning lines, by the total point count); in 3-space three point pencils contain at most 3(q^2+q+1) lines, less than the total. The two-prefix cases depend only on sorts, equality, point-line incidence and line-line intersection versus skew. For intersecting lines, their spanned plane and exterior points give a third line meeting one or neither, and the plane gives both concurrence and triangles. For skew lines, joining points gives a common transversal, and a pencil through a point on one contains more than the q+1 transversals and the original line, giving lines meeting just one; inclusion-exclusion in their 3-space leaves q(q-1)^2(q+1) skew to both. For a point off a named line, a line through the point may meet the line by joining to a point on it or be skew by leaving the spanned plane; a skew line avoiding the point exists in that 3-space since only q^2 of the q^4 lines skew to the named line pass through the point. For a point on the named line, intersections at the point, elsewhere, and skew are realized whenever permitted by incidence and dimension. Repeated objects require no extra geometric cases. These checks justify backward extension matching; for planar rank three the pair extensions are already uniform. Rank-three skew-line existence and the two separate rank-one inner conjuncts in the rank-four concurrent/uncovered witness distinguish the classes. Gaussian counts give the within-family minima 14, 26 and 50. Independent replay (python3 /workspace/checks/check5.py) gave exactly these three rank-four types across PG(2,2), PG(2,3), PG(2,4), PG(2,5), PG(3,2), PG(3,3), PG(4,2), and one common planar rank-three type. The universal argument uses plane incidence axioms, not extrapolation from those tests.

## originality

PASS

The earlier archived uncoloured rank-four plane result and the named Fano/ternary separation are material prior coverage; neither supplies the full named point-line equivalence classification simultaneously for arbitrary finite planes and all higher finite-field dimensions, or its optimal 50-object cutoff. Evidence supports that combined classification; no priority is claimed for the earlier separator or classical counts.

## value

PASS

The full named point-line trichotomy is a finite test set for rank-four sentences on an unbounded natural family, including non-Desarguesian planes. The single higher-dimensional class despite variation in dimension and field, the rank-three/ rank-four transitions, and the sharp point-plus-line representative bound make it useful beyond a previously known separator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
