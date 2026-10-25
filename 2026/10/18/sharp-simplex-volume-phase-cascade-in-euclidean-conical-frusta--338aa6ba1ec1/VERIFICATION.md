---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Affine shear aligns centers without changing determinant multiplier h R^(d-1). Multilinear determinant absolute value is convex in each vertex, ensuring some maximizing simplex on the two bases. For each k+j=d+1 split, expand vertical determinant to a wedge of horizontal within-group differences; Hadamard wedge inequality and the centered-vertex singular-value AM-GM bound C_m s^(m-1) give sharp product C_k C_j t^(j-1), attained by regular simplices in orthogonal complementary subspaces. Ratios A_(j+1)/A_j=t q_j/q_(d-j) with q_m=C_(m+1)/C_m strictly decreasing yield strict log concavity, ordered adjacent-only thresholds; C_d~sqrt(e d) gives freezing at fixed t<1. Independent separate numerical determinant and candidate ratio tests d=2..16 checked all phases and transition counts, not universal proof. Note base-supported equality classification does not exclude additional lateral boundary maximizers.

## originality

PASS

Horváth–Lángi Theorem 2 on d+2 point polytopes inscribed in one sphere supplies orthogonal-join geometry, not maximum d+1 vertex simplex in two unequal parallel balls. Lassak special double-cone and universal approximation bounds do not determine all radius phases; published Santaló law of homothetic frusta is about a different invariant. The exact all-d t-dependent formula and thresholds remain separate best-of-knowledge information. McKinney 1974 central-body cylinder endpoint remains a priority risk.

## value

PASS

Maximum contained simplex volume is a natural convex approximation invariant. The formula simultaneously treats cone, asymmetric frustum and cylinder for every dimension and exhibits a complete nontrivial cascade of optimal layer-vertex counts, plus stable high-dimensional freezing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
