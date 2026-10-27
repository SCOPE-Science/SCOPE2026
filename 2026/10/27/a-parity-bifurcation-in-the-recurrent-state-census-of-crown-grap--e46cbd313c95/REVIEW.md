# Review: A parity bifurcation in crown-graph majority dynamics

## Correctness — PASS

The update is reconstructed exactly from the deleted matching: each left vertex sees all right spins except the right spin sharing its index. When \(n\) is even, its odd degree makes the one-step map a product of a three-branch cardinality map whose image is an involution. When \(n\) is odd, adding a self-loop realizes the prescribed tie retention, and a bounded strict cross-time energy proves eventual period at most two. The four central-weight cases and all noncentral cases classify the periodic configurations exhaustively; each binomial term counts labelled states. Every configuration for \(3\le n\le9\) was additionally checked by direct enumeration (`verify_crown.py`, `verification_output.txt`). The all-size proof is independent of that finite computation.

## Originality — PASS (bounded literature assessment)

The full-text arXiv preprints of Benjamini et al. (2014, arXiv:1405.2486v1) and Turau (2022, arXiv:2202.01580v1) were compared at the level of update model, graph family and conclusion. The first states a general period-two principle and studies random/infinite graphs; the second characterizes fixed points and two-cycles on **trees**. Neither yields the labelled crown census nor the parity-divergent recurrent fractions. Publicly indexed crown-graph coloring and parity-automaton findings concern distinct invariants or update maps. Keyword, exact-sequence, alias and implication-oriented searches found no decisive covering claim. The 1980 foundational Goles–Olivos work is acknowledged and its general principle not treated as novel; its exact original full text was not available in the inspected materials. An unindexed exact crown-graph computation remains a residual risk, not an established novelty certificate.

## Mathematical value — PASS

The problem is motivated by the difficulty of determining fixed/period-two state counts of majority Boolean networks (explicitly discussed by Turau) and by the role of graph topology in consensus dynamics (Benjamini et al.). The family \(K_{n,n}-M_n\) is a canonical dense, connected, highly symmetric bipartite graph, including the six-cycle and the cube at its two smallest allowed parameters. The complete all-size attractor census reveals a parity bifurcation from a polynomial already-recurrent probability to an exponentially small one. The result includes an exact one-step cutoff on the odd-degree side and an otherwise unique nontrivial two-cycle on the even-degree side. These global distinctions are not mere relabellings of the general period-two theorem.

## Closest literature and limits

1. Benjamini, Chan, O'Donnell, Tamuz and Tan, arXiv:1405.2486v1 (2014): general period-two result, random-graph consensus, no crown formula.
2. Turau, arXiv:2202.01580v1 (2022): structural fixed/period-two enumeration on trees, inapplicable directly to crown graphs with cycles.
3. Goles and Olivos (1980), DOI:10.1016/0012-365X(80)90121-1: general threshold-period result, not claimed as new; full original article not inspected.
4. Crown-graph definition and its standard isomorphic descriptions in MathWorld.

The theorem does not enumerate odd-case basin sizes or provide a sharp odd-case transient cutoff. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
