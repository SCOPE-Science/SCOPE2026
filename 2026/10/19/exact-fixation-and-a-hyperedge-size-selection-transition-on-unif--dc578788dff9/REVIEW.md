# Scientific review of the uniform-petal sunflower fixation theorem

## Correctness — PASS

The selected claim is a single exact fixation-and-limit theorem for fitness-proportional whole-hyperedge replacement on a disjoint-petal sunflower. The proof specifies integers \(s,m\geq1\), fitness \(r>0\), and all normalization conventions. Once a petal has been updated, it is homogeneous forever; the reduced \((h,j)\) chain has two absorbing states and four possible nontrivial transition types. Its first-step equations yield one geometric ratio, determine hub fixation through the boundary conditions, and determine leaf fixation from its first non-self-loop event. All initial locations and group sizes are covered, including \(s=1\), \(m=1\), and \(r=1\). The neutrality, derivative, and fixed-fitness asymptotics follow by explicit algebra and geometric-sum estimates. Exhaustive small-state Markov checks and exact-rational recurrence checks support the proof. The analytical argument, not a finite experiment, establishes generality.

## Originality — PASS, with residual risk

The nearest source is Liu and Masuda's model-1 hypergraph-fixation study (arXiv:2301.05343, Sections 2, 3.1.3, and S1 Text G). It uses all leaf pairs in its 3-uniform star, not pairwise-disjoint petals. The present source's model-1 update is inherited, but neither its all-pairs star formulas nor its cyclic/complete hypergraphs imply the disjoint-petal formula without an additional reduction. The later multilayer-network paper studies coupled pairwise birth-death dynamics, and the earlier multiplayer-game paper separates interaction and pairwise replacement mechanisms. Searches for sunflower, petal, star, group-broadcast, central-vs-leaf, and exact fixation variants found no covering published classification. The special graph-star and one-petal cases are known benchmarks rather than novelty claims. Less accessible or unindexed evolutionary-population literature may contain an equivalent group-broadcast reduction, and the result has not been independently priority-checked.

## Value — PASS

The hyperedge-size threshold \(s=2\) gives a nontrivial comparison at fixed advantageous fitness: as petals proliferate, the exact limiting fixation of a uniform single mutant changes from amplification under pairwise star copying to a neutral well-mixed limit for three-person copying and persistent suppression for groups of four or more. The theorem quantifies the mechanism with exact finite-size location dependence, a central/peripheral advantage ratio valid for all positive fitnesses, and an exact weak-selection derivative; this is not merely a toy numerical counterexample or a parameter substitution. It provides a tractable reference family for higher-order evolutionary copying processes.

## Scientific limitations

The conclusion is specific to disjoint equally sized petals, constant fitness, and whole-edge copying. It does not prove all-hypergraph suppression, finite-size all-fitness suppression, or a time-to-fixation law. The two numerical verification chains are finite calculations and are not cited as infinite proofs. Residual literature risk remains.

Self-review: passed. Independent audit: not yet performed.
