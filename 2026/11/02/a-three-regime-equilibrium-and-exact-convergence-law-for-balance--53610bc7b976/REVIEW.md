# Scientific review

## Correctness — PASS

The utility axiom implies an exact ordinal reduction to a two-segment tent function. For every cross-part exchange of opposite colors, both agents' old and new own-color fractions are equal and complementary, yielding one strict half-threshold comparison. Same-color exchanges cannot improve both agents, and opposite-color exchanges within one part do not alter the fractions. The resulting one-dimensional rules give a complete classification, an exact strictly decreasing clock along every profitable move, and a binomial equilibrium enumerator. The exact initialization mean follows from a displayed telescoping identity; the square-root asymptotics follow from Stirling. The direct independent-payoff program checked 32,928 state-peak cases and 215,664 profitable pairs. Scope excludes unequal part sizes, unequal color totals and non-strict swaps.

## Originality — PASS (priority risk remains)

The closest originating paper is Bilò et al., arXiv:2204.12599 (2022). Its full accessible source was examined in the model, principal lemmas and results, topology, welfare and appendix sections. Its finite-improvement and independent-set-existence theorems do not enumerate equilibrium colorings or determine exact choice-independent maximal path lengths for the balanced biclique. A 2021 monotone swap model and a 2023 single-peaked jump model differ in their incentives or available actions. Searches by utility normalization, bilateral exchange, biclique, tolerance and exact time did not find a stronger covering result; lack of a hit alone does not certify uniqueness. Relevant results from mathematical indexes and accessible previous claims concern different graph properties, monotone preferences, or vacant-node dynamics.

## Value — PASS

A global-existence theorem alone does not describe how tolerance changes the size of the equilibrium set or the time to reach it. The sharp threshold is especially informative: as peak preference crosses \(\Lambda=1/2\), the equilibrium count changes from two to the entire \(\binom{2n}{n}\)-element coloring space, and then to midpoint-occupancy colorings. All maximal improvement paths have the same length even where the next profitable swap is not unique. The exact hypergeometric mean distinguishes linear-in-size and square-root-in-size expected improvement counts. These are structural characteristics of a standard network game rather than an arbitrary parameter slice.

## Closest literature and limitations

- Bilò, Bilò, Lenzner and Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599 (first posted 2022-04-26), Theorem 1, Theorem 4, Corollary 1: broader existence and improvement claims, but not this exact classification.
- Agarwal et al., *Schelling Games on Graphs*, Artificial Intelligence 301 (2021): monotone same-type utility, not the single-peaked closed-neighborhood model.
- Friedrich et al., *Single-Peaked Jump Schelling Games*, arXiv:2302.12107 (2023): vacant-node jump games, not bilateral swap games.
- The theorem applies to equal biclique sides, equal total colors, common utility axioms, and strict mutual improvement. Broader graph classes and other payoff conventions are unproved. No external independent audit or definitive publication-priority search has been performed.

Self-review: passed. Independent audit: not yet performed.
