---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: The only linear dependence among v_i=e_i-1/n 1 is Σv_i=0, with any n-1 independent, so a codimension-one face of the (n-1)-dimensional zonotope requires exactly n-2 generators annihilated by its normal; in H this leaves a normal proportional to e_i-e_j. Direct support-function evaluation gives |x_i-x_j|<=(w_i+w_j)/2, each supporting an actual facet; there are n(n-1) oriented facets. Central symmetry guarantees a globally optimal origin-centered inball with radius r=min_{i<j}(w_i+w_j)/(2sqrt2). Erosion by the Euclidean ball gives all optimal centers as |z_i-z_j|<=(w_i+w_j-s)/2. For every minimum-sum pair an edge of G_s, equality forces z_i=z_j; for every nonedge the inequality is strictly slack at z=0 in the component-constant subspace, proving affdim c(G_s)-1. A min-weight multiplicity k>=2 gives clique K_k and n-k free components; unique min with q second-minimizers gives star K_{1,q} and n-q-1; unique center iff all tied or unique lightest with all others equally second. The projected-box corner has squared norm [Σw_i²−(Σeps_i w_i)²/n]/4. Mixed-sign patterns expose distinct zonotope vertices, and every all-same-sign pattern can be improved in absolute discrepancy by one flip; maximizing the convex norm over the corners gives exactly the signed-discrepancy minimizers as outer contacts, with unique circumcenter by antipodal symmetry. PARTITION equivalence is precisely weak NP-completeness under positive integral weights. Independently tested 5 weight patterns (ties and strictly increasing cases), all corner facet inequalities, signed discrepancy radius, predicted G_s center affine dimensions and facet contacts. These finite examples do not prove the all-n arbitrary-real result.

## originality

PASS

The searched primary statements were compared for mathematical implication, with prior scalar/global ingredients explicitly credited. A best-of-knowledge PASS attaches only to the incremental claim and retains genuine residual risks, not to any global proof of historical priority.

## value

PASS

PASS: This is a complete and natural classification of ALL optimal Euclidean inball centers (not merely the scalar radius) for weighted projection-of-cube simplicial-generator zonotopes, with sharp center-dimension jumps controlled by the graph of the two smallest weights. Generic weights yield an (n-2)-dimensional incenter set whereas symmetric and special tied profiles have a unique incenter; the juxtaposition with discrepancy-controlled outer contacts shows a structural difference between minimal facet distances and hard signed partitions. This all-dimensional, equality-case-sensitive result is independently useful and not simply a numeric substitution into known zonotope radius formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
