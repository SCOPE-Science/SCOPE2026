# Scientific review

## Correctness

**PASS.** The key adjacency criterion is derived from all three neighbours of each prism vertex. Its explicit cyclic vertex ordering bijects the common-neighbour graph with one or two squared cycles, including dimensions three and four. The independent-set coefficient formula is proved by cyclic gap compositions with each set counted exactly once after dividing by its selected-size multiplicity. Polynomial factorization over disjoint components yields every coefficient and the six maximum-set counts. The supplied verifier checks 1,398,080 subsets directly and agrees coefficientwise with the formula and an independent transfer count. None of the finite checks is used as an infinite proof.

## Originality

**PASS within accessible literature, with residual priority uncertainty.** The 2023 bipartite-prism theorem gives the maximum size in even dimensions; it is not novel here. The 2026 cubic-graph theorem translates that parameter into signed total Roman domination, not into a polynomial census. The inspected 2020 Cartesian-product bounds and 2023/2024 injective-colouring product papers give the common-neighbour framework and product chromatic results, but not the complete circular-ladder open-packing distribution or the six-residue numbers of optimum sets. Specific source inspections and implication comparisons are recorded in `AUDIT.json`. Unseen treatments under injective-graph or distance-two-independent-set terminology remain possible.

## Value

**PASS.** Maximum cardinality alone does not give the weight distribution or multiplicity of optimizers. The parity-sensitive conflict-graph decomposition is a reusable structural equivalence; it turns the entire family into explicit cycle-square independent-set calculations. The contrasting multiplicities \(3\), \(9\), quadratic, and quartic in \(n\bmod6\), together with the even-dimension deficit, supply nontrivial enumerative information for a canonical family of cubic graphs. This is not merely a substitution into the previously known maximum-size identity.

## Limits and closest literature

The closest published result is Brešar, Klavžar and Rall (2023), Theorem 2.2, which is strictly weaker in all-set enumeration. Koster, Volkmann and Wehrmann (2026), Theorem 1, supplies the recent cubic-graph motivation. Samadi, Soltankhah and Yero (2024) treat a distinct product-colouring invariant. The proof is exact for all integer \(n\ge3\); priority against all terminology variants and independent validation remain unestablished.

Self-review: passed. Independent audit: not yet performed.
