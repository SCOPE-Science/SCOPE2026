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

For B_{h,p}, verified exact Gaussian width coupling Y=R^-1 H, H=max|G_u−G_v| over edges and R=||ΠG||/sqrt(h+p). Hub-leaf maximum S_h=b_h+|Z|+o_{L²}(1), because positive and negative iid leaf maxima both center at b_h and share hub Gaussian Z. Internal handle increments are 1-dependent N(0,2), adjacent normalized correlation −1/2, and independent of hub/leaf set; adjacent simultaneous-exceedance probability ≤4exp(−2u²/3) makes local dependence negligible, giving fine Gumbel at c_p,s_p. Even/odd independent increments separately give L_p−c_p→0 in L². Bridge increment is tight, so asymptotically cannot win. Chi-square normalization error O(sqrt(log n/n)) in L² is negligible even relative to s_p. Hence max selection gives the three asserted regimes, critical atom P(|Z|≤−t)=2Φ(−t)−1 for t<0, and explicit moments; expansion of b_{floor(p² exp(lambda sqrt(log p)))}−c_p→lambda/2. Does not infer moment convergence in fine Gumbel regime.

## originality

PASS

Best-of-knowledge PASS. The classic tree-root-polytope equivalence gives crosspolytope combinatorics only, and regular-matroid/facet papers do not supply Euclidean directional-width laws. Generic locally dependent Gaussian maxima yields the handle Gumbel ingredient, but does not by itself state the correlated hub–path competition and the centered critical atom or branch exposure probabilities. An earlier tree-root-polytopes mean-width limit or broader Gaussian moving-average extremal-process result remains a live priority risk; explicit new order-one limit exceeds prior leading-order means.

## value

PASS

All n-vertex tree-root polytopes share the crosspolytope face lattice and fixed intrinsic volume, while Euclidean directional width and exposed-edge family remain graph-sensitive. The broom is the natural meeting point of shared-hub and local-chain Gaussian extremes; an exact critical crossover law, atomic centered limit and exposed-branch share are mathematically motivated geometric-probability structure beyond leading mean width.

The dated certificate retains the supplied scientific assessment, sources and limitations.
