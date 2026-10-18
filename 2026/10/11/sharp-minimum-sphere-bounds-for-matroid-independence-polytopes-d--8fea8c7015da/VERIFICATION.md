---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The Boolean squared-norm identity ||v||²=<1,v> converts farthest distance into a linear support functional. For c=projection of cube midpoint u=1/2·1 onto P=conv(independent 0/1 vertices), the projection inequality shows max_v||v-c||²=m/4-||u-c||²; any other center z has a worst-case squared distance larger by ||z-c||², proving uniqueness. Comparing P with the uniform rank-r polytope gives Φ(m,r) and equality iff q=min(r/m,1/2)·1 belongs to P. Edmonds rank inequalities then give precisely uniform density r(S)≥r|S|/m for 2r<m, and |S|≤2r(S) (two-independent-set partition) for 2r≥m. The exposed-face rule gives bases vs every independent indicator as contacts. Projection Pythagorean inequality and Cauchy–Schwarz prove Φ-R²≥max_S(t|S|-r(S))_+²/|S|. Exact independent fractions for U_(1,3)⊕U_(2,2) give R²=7/6, loss=1/12 and 12 contacts, attaining its coefficient. General proof, not small examples, handles all loopless finite matroids, including boundary 2r=m.

## originality

PASS

Best-of-knowledge positive originality for the exact final theorem, differentiating known underlying objects/structural tools from the new quantified result. Direct primary comparisons and bounded actual searches are recorded; inaccessible full texts and missing exhaustive registry coverage remain risks. No search failure is interpreted as novelty proof.

## value

PASS

The all-matroid standard-indicator Euclidean minimum-sphere question has two genuinely different sharp equality classes matching important combinatorial structures—uniform density and arboricity at most two—and distinct complete contact patterns. Exact projection and sharp rank-violation stability are useful structural tools; the theorem is not a disguised uniform-matroid calculation. Generic Boolean projection is conceded classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
