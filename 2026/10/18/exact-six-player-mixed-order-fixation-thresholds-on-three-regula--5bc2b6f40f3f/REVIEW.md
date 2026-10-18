# Review: exact six-player mixed-order fixation thresholds

## Correctness — PASS

The claim specifies all quantifiers, payoff normalizations, selection updating and the uniformly random initial mutant. The neutral chain is a symmetric voter model with fixation probability equal to the starting cooperator fraction. Differentiation gives the exact rational transient system \(A h'=B\). The delivered `verify.py` reconstructs the systems independently from the stated update rule; exact fraction elimination and residual checks reproduce each coefficient and all ten triple partitions. The cost-only coefficient \(-5/4\) is also derived by a separate exact birth-death argument. The example signs are strict, so they imply the weak-selection sign for sufficiently small positive intensity. Finite arithmetic is used to prove a finite theorem, not to extrapolate an infinite claim.

## Originality — PASS

The closest direct primary source, Llabrés et al. (arXiv:2604.07228v1), defines this Fermi model and studies mean-field stationary transitions and large-population hypergraph simulations, not exact single-mutant fixation on the six-cycle. Sheng et al. (arXiv:2605.23444v1) supply a large-population uniform-order hyperedge approximation with a different updating rule. The general weak-selection machinery of McAvoy and Allen (arXiv:1908.03827) is acknowledged but does not itself state the three rational values or opposite sign. Published-result index searches, aliases and recoverable previous claims revealed no equivalent or dominating evaluated theorem. An abstract-only inspection of older mixed-order literature and ordinary search incompleteness remain documented residual risks; the searches do not prove universal uniqueness.

## Value — PASS

Six players are the first nontrivial cycle size with two disjoint triple games and multiple choices of their relative placement. All ten placements are classified, and moving the same-sized groups while keeping every individual’s pair and triple degrees fixed reverses whether natural selection favors cooperation. This exact finite threshold classification isolates structural alignment as a distinct evolutionary mechanism; its purpose is not merely to reproduce a known numerical table. The parameter-uniform polynomial laws avoid an arbitrary fixed-number experiment.

## Limits

The conclusion is exact only for the prescribed binary-strategy six-cycle, two disjoint triples and Fermi rule. The favored/suppressed assertion concerns the linear-in-selection fixation derivative and sufficiently small intensity; it is not a universal result for arbitrary hypergraphs or finite intensities. The claim has undergone self-review only.

Self-review: passed. Independent audit: not yet performed.
