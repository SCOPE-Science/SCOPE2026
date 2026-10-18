---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For a finite tree of order n≥4 with independent homogeneous Bernoulli-open contact edges and one uniform random seed, the unique path formula gives E S=1+2(n−1)p/n+2B(T)p²/n+O(p³). Triple path unions in E S² have 6 contributions per one-edge union and 12 per two-edge union, yielding the stated p² coefficient in Var S. A single deleted edge partitions into sizes s,n−s and contributes s(n−s) q to the variance when q=1−p; summing edge cuts is exactly W(T). For uniform δ_n=1/(100n^6), treating Var as an expectation over two independent percolation/seed copies bounds the k-th Bernoulli derivative by (4(n−1))^k n², so Taylor errors on differences are O(m³n²p³) or O(m²n²q²). Because differences of B and W are nonzero integers, the stated interval dominates the remainders for all trees of order n. Degree convexity and the Wiener cut/leaf argument give unique path/star extremes in opposite regimes. Independently reconstructed exact n=4 variance difference as p²(1−p)(8−6p−5p²−p³)/4, giving exactly one positive interior crossing. Nonuniqueness at intermediate p is NOT asserted.

## originality

PASS

The existing 2020 paper studies first and second bond-percolation cluster moments on rings, paths and stars, so its special-shape formulas and n=4 comparison are not treated as novel. The assigned all-tree coefficient and strictly uniform all-pair B/W comparison has broader quantifiers than the accessible path/ring/star abstract. The full 2020 paper was not accessed: it is specifically plausible and might contain a broader hidden theorem, which is carried as residual risk, not an automatic failure. Other published tree-variance results from similarity search concerned zonotope widths, a different probability model.

## value

PASS

A genuinely global, uniform-in-all-trees ordering reversal of a stochastic epidemic outcome is useful beyond known path/star moment formulas: low-transmission variance is controlled by wedge count, high-transmission variance by Wiener index, and the opposite unique extrema are proved with explicit simultaneous neighborhoods. The tree family and the two invariants are natural, not an arbitrary finite slice. Model limitations are specified rather than conflated with empirical epidemic outcomes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
