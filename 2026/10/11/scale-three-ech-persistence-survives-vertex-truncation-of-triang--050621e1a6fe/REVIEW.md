# Scientific review: scale-three Čech persistence under vertex truncation

## Correctness — PASS

The theorem specifies the finite connected simple triangle-free base graph, the oriented-incidence graph model, the unit-edge intrinsic Čech normalization, and the exact inclusion under discussion. The odd/even graph Čech generating-facet formula is supported by Adams--Shukla--Singh, arXiv:2212.05871, Lemma 2.2. Four explicit stages of elementary simplicial collapses are justified by the uniqueness of the indicated remote-pair or mixed-cross markers and by descending face-size ordering. The first two stages preserve the full scale-two subcomplex and prove the actual inclusion is a simple-homotopy equivalence, not merely an abstract equality of Betti numbers. The later stages reduce scale two to a graph obtained from the base graph by vertex-tree expansions. The integral first-homology kernel is the direct sum of independently embedded complete-graph cycle lattices. Degree-one, tree, and vanishing-cycle cases are treated. The standard-library verifier exhaustively confirms four relative collapse stages on thirty-eight finite triangle-free graphs and independently calculates the mod-two obstruction for the triangle base. Only the symbolic combinatorial argument establishes the universal statement; finite checking alone does not.

## Originality — PASS

Adams--Shukla--Singh establish the Čech facet formula and hypercube results, but do not classify the scale-three nerves of arbitrary vertex-truncations of triangle-free graphs or prove this inclusion is a collapse. Goyal--Shukla--Singh, arXiv:2009.12130, Corollary 3.3, cover the clique complex of a line graph, not the odd-scale intrinsic Čech nerve. Earlier scale-two results for certain line graphs and computational Vietoris--Rips statements about a truncated cubical example neither state nor imply the scale-three relative collapse; the latter concerns a different simplicial construction. Metric-gluing literature uses a different center set and does not give this vertex-centered claim. Searches for graph Čech subdivision, truncation, line-graph and radius-three equivalences did not identify a stronger covering statement. This does not establish absolute novelty; unindexed or unpublished equivalent work remains a residual risk.

## Value — PASS

The result covers an infinite arbitrary-degree family, including graphs containing arbitrarily many cycles and high-degree local cliques, with a uniform explicit elementary collapse at a scale where the generic girth-based reconstruction criterion fails for truncations at vertices of degree at least three. It identifies which integral first-homology generators die from scale one to two and shows precisely that all remaining classes persist to scale three. Such an inclusion-level statement is useful for exact persistence, topology-preserving sparsification, and distinguishing the effect of local clique filling from underlying cycles. The triangle counterexample gives a motivated boundary. It is not a routine substitution into the known clique-complex result.

## Primary literature and limitations

Adams, Shukla, Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (original posted 2022-12-12), §§2–3; Goyal, Shukla, Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (original posted 2020-09-25), Lemma 2.3 and Corollary 3.3; Adamaszek et al., *Vietoris–Rips and Čech Complexes of Metric Gluings*, SoCG 2018, DOI 10.4230/LIPIcs.SoCG.2018.3. The conclusion is limited to finite connected simple triangle-free base graphs and scales one through three. There is no all-scales classification and no claim of independence or external verification.

Same-model review: passed. Independent audit: not yet performed.
