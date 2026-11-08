---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For a regular n-gon with unit incircle and k rotated sets, normal angular gaps g sum 2π/n. Tangency triangles yield area nΣtan(g_i/2), polar normal convex hull yields area n/2 Σsin(g_i), including zero gaps by continuity. The pairwise derivative identity reduces strict Schur concavity to DA−B>0, D=(1+cos g_i)(1+cos g_j). With s=g_i+g_j≤π/2, D≥2 gives positive terms; for s>π/2, s≤2π/3, D≥1, remaining sine sum≤π/6 and sin s≥√3/2, so strict positivity. Strict balancing transfers imply global majorization and only equal-gap/vertex equality cases. The Taylor second derivative on Σeps=0 has coefficient −n²k cos(gbar)tan²(gbar/2)/4, as stated. No numerical tests are used as all-parameter proof.

## originality

PASS

Classical Meyer–Reisner regular polygon maximal volume product and Böröczky et al. rotation-symmetry lower product cover endpoints only. A full related published SCOPE article orders expected intersection area under random rotations, not deterministic Mahler product under angle-gap majorization. The strict global angular majorization comparison is a stronger distinct ordering.

## value

PASS

The previously known regular polygon extrema are strengthened to a strict partial-order law for arbitrary nonuniform rotational placements, including equality cases and a local quadratic stability constant. This is a structural geometric inequality beyond endpoint restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
