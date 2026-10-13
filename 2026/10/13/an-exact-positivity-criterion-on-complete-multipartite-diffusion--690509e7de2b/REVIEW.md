# Scientific review

## Correctness — PASS

The all-graph equivalence follows from a complete orthogonal-projector resolution of the combinatorial Laplacian of \(K_{a_1,\ldots,a_k}\). The three entry types are derived explicitly. Necessity uses \(K_2\) for the upper scalar bound, the arbitrarily large clique family with a rescaled step for the lower scalar bound, and bicliques \(K_{p,q}\) plus density of rational ratios for monotonicity of the difference quotient. No finite enumeration is used as an infinite proof. The concrete fourth-order multiplier has a strictly positive numerator, is strictly below one, and has a strictly decreasing difference quotient. The exact checker independently reconstructs and compares full rational matrices on 993 graph-step pairs.

## Originality — PASS, with residual uncertainty

Lóczi and Ketcheson prove a zero absolute-monotonicity radius for the unrestricted fourth-order Padé stability function, which does not state that this function is positive on a particular entire graph family at every step. Zappavigna and colleagues provide a universal failure witness and short-step sufficient criterion for Hurwitz Metzler matrices; their entry-support condition does not cover nonsingleton complete multipartite graphs, and their theorem supplies neither the all-scale conclusion nor the scalar iff. The published eight-state Markov result concerns arbitrary generators at small steps and a single pure-birth witness, not the characterized family. A targeted search for graph-filter aliases, complete-bipartite positivity and divided-difference equivalences did not find statement-level coverage. An existing complete-bipartite Padé positivity special case is expressly not counted toward novelty; it does not imply the iff classification for every continuous scalar multiplier on arbitrarily many parts. An older matrix-function classification could still subsume the result under different language; this remains an explicit residual risk, not a novelty certificate.

## Value — PASS

The theorem characterizes an infinite-dimensional cone of scalar time-stepping multipliers by only two scalar shape requirements, for an arbitrarily large and heterogeneous family of diffusion graphs including complete graphs, stars and bicliques. The two-hop nonadjacent entries yield a genuinely independent divided-difference restriction, and a concrete counterexample establishes that pointwise positivity alone is insufficient. The practical corollary resolves an apparently conflicting design question: a classical fourth-order integrator with **zero general-purpose absolute-monotonicity radius** nevertheless preserves the probability simplex for every positive step on this natural family. Both the exact structural criterion and its instance are reusable when choosing rational spectral filters for graph diffusion.

## Closest sources and remaining limits

Closest literature is Lóczi–Ketcheson (arXiv:1303.6651v1, Section 2.2.1), Zappavigna–Colaneri–Kirkland–Shorten (doi:10.1016/j.laa.2011.12.021, Section 4), Blanes–Iserles–Macnamara (arXiv:2102.08242), and *Eight-state barrier for Markov positivity of the [2/2] Padé map* (published RESULT.md linked in RESULT.md). The statement applies only to unweighted connected complete multipartite graphs and the end-step map; no independent audit or exhaustive historical priority claim is made.

Self-review: passed. Independent audit: not yet performed.
