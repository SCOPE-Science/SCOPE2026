# Scientific review

## Correctness — PASS

The action-class payoff formula follows from the pair-incidence identity and is reversible by single-cooperator probes. A 2-design has positive pair incidence, so the best-earner copying mechanism cannot turn the higher-payoff strategy into the lower one, and every mixed state has positive progress probability. The resulting finite monotone chain absorbs almost surely with finite mean. On the complete uniform hypergraph, hypergeometric edge selection gives an exact pure-birth or pure-death chain; geometric waiting times and a two-boundary harmonic estimate establish the stated absorption formulas. On the Fano plane, edge counting yields different transition probabilities for two states with three cooperators. The standalone exact rational checker passed the listed finite tests. The infinite claims rely on analytic steps rather than finite enumeration.

## Originality — PASS, qualified

The closest prior work is Alvarez-Rodriguez et al. (2021), which introduced the hypergraph best-earner mechanism and a well-mixed replicator approximation, and Wei et al. (2026), which used that mechanism with two changing resource states on random uniform hypergraphs. Wang and Su (2026) derive finite-network cooperation criteria under weak selection with different update rules. Liu and Masuda (2023) derive hypergraph fixation formulas under constant-fitness edge-wide birth--death updating, which is a different state-transition mechanism. None of the materially inspected statements gives the exact pair-design if-and-only-if, all-initial-configuration fixation criterion for a strong imitation process, Fano count non-lumpability, or the complete-design elementary-update absorption law jointly established here. Classical design identities and limiting replicator thresholds are credited rather than claimed as novel. Other unexamined supplementary or specialized papers might have a stronger equivalent result; priority is provisional.

## Mathematical value — PASS

The theorem identifies a structural reason that *every* configuration on certain sparse uniform hypergraphs exhibits the same direction of selection. Its threshold depends only on population and group sizes, not the number of interactions or block geometry. The Fano example reveals that this powerful payoff simplification does not guarantee a one-dimensional stochastic reduction, while the complete-design time formula determines the correct discrete absorption scale. This provides a meaningful boundary between exactly solvable stochastic evolutionary models and shape-dependent dynamics, rather than an arbitrary enumeration.

## Scope and residual risk

Assumptions are strictly uniform interaction order, positive constant return on every hyperedge, common hyperdegree, cost one, no mutation, and one specific highest-payoff imitation protocol. Neither heterogeneous or changing-edge games nor general weak-selection dynamics are covered. Broader existing literature may contain an equivalent theorem not found through inspected sources; independent priority and proof reviews remain outstanding.

Self-review: passed. Independent audit: not yet performed.
