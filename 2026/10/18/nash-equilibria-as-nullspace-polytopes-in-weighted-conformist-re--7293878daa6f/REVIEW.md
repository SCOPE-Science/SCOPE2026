# Scientific review of the weighted conformist–rebel equilibrium theorem

## Correctness — PASS

At every profile, each cross-group edge pays its full weight to exactly one incident player. Each player's best payoff is half its weighted degree plus half the absolute signed neighbor imbalance. At Nash equilibrium the nonnegative regrets sum to zero; their sum is explicitly half the sum of the absolute residuals of the cross-weight matrix and its transpose. This proves exact necessity and sufficiency even on the boundary of the mixed-strategy cube. Rank-nullity gives affine dimension; a maximum-matching determinant monomial gives generic rank; one nontrivial signed incident-weight equation excludes pure equilibria almost surely. The general conclusion is deductive, not based on simulations. A standalone exact-arithmetic independent direct-best-response check reproduced 1,953 profiles and 256 additional positive 2-by-2 weight matrices.

## Originality — PASS, subject to historical-priority risk

The 2018 fashion-game paper gives uniform mixing and devotes its main analysis to pure equilibrium/dynamics. The 2019 network matching-pennies paper studies best-response cycles. The 2026 multi-strategy three-type preprint explicitly states it does not consider mixed strategies; its bipartite results concern pure equilibria. The 2026 heterogeneous-player preprint similarly treats pure equilibria and dynamics. Searches for equivalence by the phrases `nullspace Nash`, `weighted bipartite matching pennies`, `full mixed equilibrium manifold`, `maximum matching and unique equilibrium` did not locate an implication-equivalent statement in the sources investigated. This is a specialization of a zero-sum polymatrix interaction, and the determinant matching correspondence is classical: a stronger abstract game-theoretic characterization could imply the theorem and remains a residual priority risk. No independence or comprehensive-literature priority claim is made.

## Mathematical value — PASS

Opposed incentives on completely heterophilic networks make pure equilibria fragile and mixed outcomes unavoidable. The exact shape of the **entire** Nash set is therefore a natural question. The result gives complete classification for every finite weighted bipartite network, including partial and pure profiles, and turns uniqueness and equilibrium freedom under generic weights into a computable maximum-matching invariant. In particular it separates the possible existence of many pure equilibria at unweighted symmetry from almost-sure pure-equilibrium extinction under arbitrarily small independent continuous weight perturbations, while measuring surviving mixed freedom by matching deficiency. It does not claim a dynamic selection principle, correlated equilibria, or within-type edges.

## Closest literature and limitations

Primary material inspected: Pei–Cao–Zhang, arXiv:2607.10997, model/benchmark and theorem sections; Cao–Sánchez–Zhang, arXiv:2607.05932, model/related-work and main results; Zhang–Cao–Qin–Yang (2018), original game/payoff/mixing paragraphs; Cao–Qin–Yang–Zhang (2019), original introduction and results/related-work sections. See RESULT.md for references and domain restrictions. Existing zero-sum polymatrix and algebraic graph-rank theory remain substantive historical-priority risks; no source was found proving the full specific equivalence, but this is not proof of global novelty.

Self-review: passed. Independent audit: not yet performed.
