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

The actual pinned RESULT.md defines a free join of k>=2 compact full-dimensional factors A_i in pairwise independent affine blocks, with each d_i>=1, and uses the reflection definition (h+1)c-J subseteq hJ. Reflecting an arbitrary generating i-face forces (h+1)t_i-1>0 and the factor containment (h+1)t_i a_i-A_i subset ((h+1)t_i-1)A_i; hence that coefficient >=s(A_i). Summing yields h>=sum_i s(A_i)+k-1. Conversely choose t_i=(s(A_i)+1)/S, S=sum_i(s(A_i)+1): for a generator on face i, the reflected spatial block j has nonnegative join weight s(A_j)+1-delta_ij, and the i-block is in s(A_i)A_i by optimality of a_i. Convexity carries containment to all J. At equality each nonnegative lower-bound deficit vanishes separately, fixing barycentric weights and making every a_i an actual minimizing factor center. Injectivity at positive weights gives the full Cartesian-product center locus and affine dimension sum. This is a proof for all factors, not extrapolation from the LP examples; singleton factors and overlapping joins are outside the stated scope.

## originality

PASS

Mathematical comparison concerns an arbitrary-body free-join composition law and every optimal center, not mere equality of values for simplices, a pyramid point-factor boundary, or a computable generic convex-program prescription. The published special families and symmetrization papers inspected do not establish the universal positive-dimensional multifactor identity or product center locus. This is a qualified best-of-knowledge judgment; an older Cayley/free-join synonym could cover it.

## value

PASS

Free join is a canonical convex-body composition operation. The result gives a new structural all-arity rule for a classical affine invariant independent of factor dimensions and a complete description of nonunique optimal-center sets, including additive dimensions. The invariant is natural before any numerical computation; the theorem controls smooth, nonsymmetric, and polyhedral inputs alike. Knowing asymmetry of factors does not by itself determine behavior of their join without the proved reflection containment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
