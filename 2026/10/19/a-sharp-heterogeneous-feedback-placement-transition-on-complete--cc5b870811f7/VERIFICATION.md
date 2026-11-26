---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The pinned Laplacian is positive definite: a vector in the Laplacian kernel is constant and the positive pins exclude every nonzero constant. Its covariance for independent unit-intensity disturbances is one half the inverse. I checked the rank-two determinant expansion and independently reproduced all three rational comparisons (3)–(5) with an equitable quotient rather than the frozen pseudoinverse calculation. Use a singleton for each leader and one cell for the unpinned vertices of each part; the quotient has diagonal degree plus assigned gain and off-diagonal entries minus opposite-cell sizes. Add contrast contributions (cell size minus one)/part degree to the inverse trace, omitting an empty cell; if retained symbolically at size zero its diagonal inverse contribution cancels the formal contrast term. Compute the quotient inverse trace as the sum of diagonal cofactors divided by its determinant. This gives AB−BA with the sign of (a−b)(p−q), AA−BB strictly negative, and AB−AA with the opposite sign of P(a)=Da²−Ea−F. The displayed bounds on H, W and V are positive for the entire integer domain, and P(b)<0 accounts for equal gains and forces the positive root above b when D>0. D≤0 gives P<0 for all allowed a. The positivity criterion q²−q>3p² and enumeration of p+q≤7 give the unique smallest graph K_{2,5}. Independent exact inversion with b=1 gives J_AB−J_AA=−(a²−26a−45)/[(7a+5)(8a+5)], verifying 27, 28, and the radical tie. The finite witness supplements rather than proves the uniform algebra.

## originality

PASS

The inverse-trace objective and the general update methods are prior. The supported distinct statement is the full placement and tie classification with two prescribed heterogeneous gains across all unequal unit complete bipartite graphs. The strongest inspected overlaps share either the graph, the pair-of-gains setup, or the general objective, but not the resolved heterogeneous bipartite comparison.

## value

PASS

A natural design question has a nontrivial answer: unlike at equal gains, one of two noisy leaders can relocate to the larger part when the other becomes strong enough, but only in sufficiently imbalanced graphs and below a cutoff on the weaker gain. The all-parameter rule, tie classification and first feasible graph give more than a recomputed objective or isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
