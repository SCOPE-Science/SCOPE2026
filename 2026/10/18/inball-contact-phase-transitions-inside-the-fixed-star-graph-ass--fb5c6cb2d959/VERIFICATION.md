---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Projected leaf-coordinate polytope equals the independent-set polymatroid y_i≥0, y(U)≤A_|U| with rank A_u=Σ_j w_j(C(k,j)−C(k−u,j)), by equality of greedy support functions, not mere necessary facet inequalities. The intrinsic metric after eliminating hub is I+11^T, giving lower intrinsic normal length d=√(k/(k+1)) and subset-upper normal √[u(k−u+1)/(k+1)]. Any inball forces r≤A_u/(ud+ν_u); center with all leaf coordinates dr realizes the minimum and is uniquely forced by every minimizing-cardinality subset. For two strata a,b>0, exact inequalities on pure edge, equal edge+pair and pure pair rays show only cardinalities 1 and k can minimize, with a>b, a=b, a<b yielding respectively 2k,2k+1,k+1 contacting facets; intermediate u never tangent. For canonical m≥3, strict increased hypergeometric intersection probabilities force only u=k. Positive edge and pair simplices already impose the common normal fan, so m=2→3 tangency changes without combinatorial fan changes. Independently compared analytic distances and endpoint inequalities for k=3..16 over (a,b)=(1,3),(1,1),(3,1),(1,2),(2,1) and all m cutoffs. This is not a metric claim after naive hub-coordinate deletion.

## originality

PASS

Prior Resultary full same-object stellohedron result already establishes the m=k endpoint radius/unique uniform center and k+1 facets; prior same-weight-family diameter theorem evaluates a different metric functional. Pešović–Stojadinović gives the underlying m-graph polytopes and star fan stabilization; Behrend/partial-permutohedron paper concerns projected leaf-coordinate geometry. None of these inspected source statements entails the new continuous ratio a/b=1 contact transition, sharp formulas for intermediate m and 2→3 jump inside an identical fan. Novelty excludes previously known endpoint.

## value

PASS

The exact transition gives a realizational geometry invariant not visible from a face lattice/normal fan, and the continuous positive two-weight star family is a natural interpolation from graphical zonotopes to stellohedra. The fully specified contact classes and metric distinction are useful independently of the known terminal inradius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
