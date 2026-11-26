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

For X_i=U_i U_i^T−I/d, the triangle is tr((I/d+X_i)(I/d+X_j)(I/d+X_k)). Its linear terms vanish by tracelessness, the pair terms equal ((U_i·U_j)^2−1/d)/d, and the cubic term is completely degenerate by independence and E X_i=0. Pair and cubic contributions are orthogonal, even at partial index overlap. Fourth spherical moments yield E h²=(d+8)/(d²(d+2)²), Var(h)=A=(d−1)(d²+8d+4)/(d⁴(d+2)²) and pair-projection variance B=2(d−1)/(d⁴(d+2)); the third-order variance per triple is A−3B=(d−2)(d−1)(d+4)/(d⁴(d+2)²). Distinct triples sharing exactly one edge have covariance B and there are C(n,2)C(n−2,2) unordered such pairs. The planar identity is the vanishing 3-by-3 Gram determinant. The repaired Bingham comparison is exact: B_n−m=d(d+2)P/n, so the pair contribution after n² scaling is (1−2/n)(B_n−m)/(d²(d+2)); Var(Q/n²)=O_d(1/n). This verifies the same fluctuation law, finite variance coefficient and d=2 and n=3 boundaries, with no assumption of full-rank Gram matrices. The frozen Python script was inspected, not executed; actual simulation n=500 differs from a stale n=1000 inline comment, and the icosahedral checks use floating-point tolerance. Neither is used in the proof.

## originality

PASS

Pass applies to the repaired finite-sample claim: the exact total and degenerate third-order variances and the resulting dimension-specific error in the pair approximation. The repair explicitly credits the exact pointwise Gram identity as elementary and the limiting law as a consequence of the classical Bingham null limit, not independent novelty. The checked moments and broader asymptotics do not give the exact all-n third-order residual.

## value

PASS

The signed triangle sum is the distinct-index part of the cubic Gram trace, and its natural pair approximation is the centered frame potential. The exact residual variance gives the finite-sample mean-square loss incurred by replacing triangles with pairs, with a sharp dimension boundary: loss is zero in the plane and strictly positive elsewhere, though asymptotically lower order at fixed d. This information is useful when distinguishing higher-order terms from a known pair fluctuation; it is not supplied by the limiting distribution alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
