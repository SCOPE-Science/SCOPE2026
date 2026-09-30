# Review

**Independent-audit repair required and supplied.**

## Correctness

**PASS.** The all-connected-bipartite standard-model equality classification follows from the equality conditions inside Zhu's two single-class comparisons. A cyclic auxiliary graph gives strict inequality. When the auxiliary graph is a tree, its edge increments are independent Bernoulli variables with nonzero probabilities `2/(2^{t_e}+2) <= 1/2`; since the path range sequence is strictly increasing, equality forces `t_e=1` on every auxiliary edge. Applying the criterion to both bipartition classes forces maximum degree at most two. Even cycles of length at least six have cyclic same-class auxiliary graphs, and `C_4` violates the codegree-one condition, so only a path remains.

The quantitative gap-transfer inequality follows directly from Zhu's zero-edge contraction identity, the BHM inequality on every contracted quotient, and retention of the nonnegative contribution from the no-zero-edge event. Its probability is `|H(G,o)|/|L(G,o)|`; for a tree independent lazy edge increments give `(2/3)^{n-1}`.

## Originality

**PASS AFTER ATTRIBUTION REPAIR.** The prior version understated the 2016 literature. Wu--Xu--Zhu's full manuscript is search-indexed with the relevant theorem text: Corollary 2.6 states `h(G) <= h(P_n)` for every tree with equality iff `G=P_n`, and Corollary 2.12 states the analogous unique-path equality for the standard/bipartite height. Those tree equality cases are therefore prior work, not a residual possibility.

The genuinely new scope retained by the repaired record is narrower and still substantive: Zhu's 2026 theorem covers every connected bipartite graph but does not state its complete equality classification, and the exact auxiliary-tree/codegree-one criterion yields that classification. The general quantitative standard-to-lazy gap transfer was not found in the compared sources. The all-connected lazy unique-maximizer statement is now explicitly presented as a prior consequence/consistency corollary rather than a new theorem.

## Scientific value

**PASS.** Classifying equality in the newly completed BHM expectation theorem is a meaningful extremal refinement beyond the 2016 tree case. The gap-transfer inequality also gives a quantitative mechanism converting any standard-model deficit into a lazy-model deficit on every connected bipartite graph. Removing the overstated novelty around the lazy/tree equality result leaves a coherent and worthwhile contribution.

## Limitations

- Originality is claimed only for the all-connected-bipartite BHM equality classification and the quantitative gap transfer.
- The stronger stochastic-domination form of BHM is not addressed.
- The factor `p_G` may be exponentially small, and no sharp universal stability gap depending only on `n` is claimed.
- Very recent parallel work remains possible because the 2026 source is new.
