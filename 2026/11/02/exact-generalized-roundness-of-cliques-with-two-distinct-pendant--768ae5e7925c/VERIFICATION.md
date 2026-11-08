---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The full RESULT.md gives an exact powered-distance quadratic decomposition for K_m with two unit pendant leaves attached to distinct core vertices (m>=3,k=m-2), separating a negative fluctuation space, an antisymmetric 2x2 sector (strictly negative for 0<p<2) and symmetric 2x2 block with determinant -k[kU(p)+V(p)]. With U(p)=4^p-6*2^p+3^p+3 and V(p)=2*3^p-4*2^p-2, the derivative/convexity inequalities show kU+V increases from negative at 1 to positive at 2 with unique root p_m. An explicit zero-sum kernel vector at the root gives a one-dimension drop in centered Gram rank (m+1 below to m at p_m). Li–Weston exponent reduction excludes recovery of negative type beyond the endpoint. The strictly negative V on [1,2) and U increasing give strict m monotonicity and asymptotic p_infty≈1.629581635586, correction 0.342777710028/(m-2). Independently built BFS graph distance matrices and recomputed critical eigenvalue signs for m=3..10, giving m=3:1.801349035 and m=4:1.743145058, but finite checks do not establish universal theorem.

## originality

PASS

The m=3 graph is the bull graph, distinct pendant leaves attached to two different triangle vertices; its higher-m graph is clique-expanded bull. Sánchez arxiv:1108.0451 gives generic finite-metric determinant and different five-vertex examples, not an evaluated bull-clique infinite-family equation. Li–Weston arxiv:0901.0695 supplies strictness theory but not this graph spectral calculation. Resultary bull-graph Morse complex and pineapple graph curvature results treat other invariants. Best-of-knowledge exact threshold/equality/asymptotic are additional mathematics, with unindexed graph metric priority risk.

## value

PASS

The bull graph and its clique expansion are a natural minimal nontrivial two-articulation extension of a complete metric graph. Unlike one-hub variants, cross-pendant distances introduce a 3^p spectral term. The result gives a complete exact all-order negative-type threshold, a one-dimensional first-loss equality space, the Hilbert snowflake dimension change, monotone dependence on clique order, and a computable limiting exponent with first correction. Those natural structural facts are not routine small-instance type checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
