# Scientific review

## Correctness — PASS

Under the exact default-delegation payoff definition, the utility splits into a strictly length-increasing part and a distance penalty in the interval \([0,Dq(1-q^{n-1})]\). The smallest marginal length improvement is \(\tau p q^{n-1}\); the stated sufficient threshold dominates the maximum possible penalty difference. A direct functional-digraph argument constructs a strictly longer unilateral orbit for every non-Hamiltonian map, including a tree attached to a cycle and the multiple-cycle case. Every Hamiltonian cycle is immune because deviations shorten the orbit. The expected vote-loss lower bound is the all-abstain event. The three-person phase result follows from explicit enumeration of eight loop-free profiles and the exact signed payoff difference \(pq(q(\tau-h)-h)\). The proof treats all integers \(n\ge2\) and all admissible real parameters, not only checker instances. The standalone exact-rational checker confirms 10,236 graph profiles, 197,226 unilateral comparisons, 99 cycles across parameter settings, and 15 three-person phase settings.

## Originality — PASS, with residual risk

The motivating full primary manuscript, Brill et al., arXiv:2607.12610, was inspected for the payoff model, Theorems 1, 5, 13, and 14, and Proposition 19. Proposition 19 already proves that full cycles optimize expected vote loss, so that **isolated** statement is acknowledged as prior art and not claimed new. Theorems 5 and 14 restrict components or a single voter's preferred traversal, but do not assert the all-equilibria collapse under an explicit tolerance inequality, an exact equilibrium count, or the three-person threshold. Older liquid-democracy models in arXiv:1802.08020 and arXiv:1904.05775 use different delegation payoffs/updates. Keyword, semantic, and published-result searches found no statement known to imply the full new conjunction. Search incompleteness and the possibility of equivalent unpublished arguments remain real risks; this is not a claim of guaranteed uniqueness.

## Value — PASS

A stochastic default-delegation model explicitly distinguishes a socially efficient global cycle from individually optimal forwarding and allows multiple Nash components in general. The theorem closes this natural model gap by providing a transparent, all-population-size sufficient condition where selfish play **necessarily** yields the global optimum, with the exact number of distinct pure equilibria. The sharp three-agent example demonstrates a genuine equilibrium-structure transition at a smaller explicit tolerance and quantifies conservativeness of the universal sufficient estimate. The result does not rely on an arbitrary finite census or merely a routine normalization check.

## Literature and limitations

Closest source: Brill et al., *Cycles in Liquid Democracy: A Game-Theoretic Justification*, arXiv:2607.12610. See RESULT.md for the precise all-size assumptions, high-tolerance sufficiency (not necessity), three-agent sharp range, vote-loss proof, and additional directly inspected liquid-democracy literature. An equivalent formulation absent from the inspected records cannot be ruled out. The checker corroborates but cannot prove the quantification over all real inputs and all population sizes.

Self-review: passed. Independent audit: not yet performed.
