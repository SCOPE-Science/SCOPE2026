---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Choose a generic diagonal C* subgroup on the ambient partially symmetric tensors with all multihomogeneous monomial weights distinct (large-place-value weighting across variables and degrees). Every fixed point of tau(X) is a coordinate monomial. Because tau(X) subset sigma_2(X), every multigraded catalecticant flattening rank is <=2. For local monomial alpha, the order-e catalecticant rank is coefficient [t^e] product_j (1+...+t^{alpha_j}), and all such ranks <=2 iff it is pure or has exponent pattern (1,1) for degree2 or (d-1,1) for d>=3. Product flattening ranks exclude two nonpure factors. Conversely every surviving coordinate monomial is a pure point or a tangent-coordinate direction from replacing one factor in a pure tensor. Thus fixed points count product_i n_i + sum_i a_i product_{j!=i} n_j with a_i=0, binom(n_i,2), n_i(n_i-1) in d_i=1,2,>=3 regimes. Euler localization applies to possibly singular tangential varieties. Independent exhaustive local exponent checks (n=2..4, d=1..5) matched every pattern. Symbolic divisor-rank argument proves all degrees/dimensions.

## originality

PASS

The full relevant Ballico–Bernardi primary arXiv HTML treats ranks and decompositions in the tangential Segre–Veronese variety (Theorem 2.1 for any factor count), but does not state an Euler characteristic, torus fixed-monomial census or a stabilized three-regime mixed multidegree formula. General C*-Euler localization by itself does not give this count: unlike pure Segre secants, most ambient coordinate monomials are NOT in the tangential variety, and classifying the survivors requires the nontrivial catalecticant rank analysis and the tangent converse. One-factor and pure Segre subfamilies alone do not imply mixed degrees. Residual risk of an unindexed motivic/tangent-orbit formula remains.

## value

PASS

A natural global invariant of partially symmetric tensor tangent varieties is computed for all factor counts, dimensions and multidegrees, including a distinct quadratic correction and degree>=3 stabilization of the Euler invariant. This is not an arbitrary finite slice: the rank-two flattening constraints yield a complete structural fixed-monomial classification that can inform topological and motivic study of these varieties. No claim is made that all Betti numbers or topology itself stabilizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
