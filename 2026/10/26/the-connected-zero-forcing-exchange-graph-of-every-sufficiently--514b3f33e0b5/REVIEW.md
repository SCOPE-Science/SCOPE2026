# Scientific assessment

## Correctness — PASS

The claim is an infinite-family theorem on labelled graphs \(C_n\square K_2\) for every integer \(n\ge6\). The proof derives a size-four lower bound from the impossibility of continuing from a connected three-vertex path, exhausts all induced connected four-vertex shapes using the triangle-free cubic structure, proves each surviving four-vertex path and square propagates to the whole graph, and enumerates every possible one-vertex exchange by retaining three vertices. The table of \(6,6,8,6\) degrees across the four symmetry classes gives the edge count, and specified cross-class links prove connectivity. Both independent programs reproduce the expected counts, degrees and connectivity; no finite enumeration replaces the all-order arguments.

## Originality — PASS, with residual risk

The 2020 circular-ladder result of Premodkumar–Dominic–Chacko (Proposition 22) determines the already-known *number* \(Z_c=4\) and gives one connected forcing seed, but does not enumerate the minimum seeds, characterize their induced forms, or compute their exchange graph. The 2016 foundational connected-forcing work of Brimkov–Davila does not state an exact prism exchange theorem in the inspected material. The 2020 Geneson–Haas–Hogben token-exchange work treats unrestricted minimum zero forcing, a different configuration space, and its inspected introductory examples cover paths, cycles and complete graphs, not the present connected prism classification. Targeted searches and accessible mathematical research records did not produce an implication covering this theorem. Risk: an equivalent characterization could be present under alternate terminology in unindexed or uninspected literature.

## Mathematical value — PASS

The source literature establishes the optimum cardinality for connected zero forcing on circular ladders, but says nothing about how many optimal connected seed sets exist or whether they are mutually reachable while keeping the connected-forcing constraint. Classifying precisely all \(9n\) optimum seeds and exhibiting a single connected exchange graph with an exact degree distribution and \(28n\) edges resolves these distinct, naturally arising structural questions for every long circular ladder. The four orbit types yield a transparent geometric reason for connectivity. This is more than a routine recomputation of a known minimum cardinality.

## Scope, source and limitations

The theorem excludes small rim sizes \(n\in\{3,4,5\}\), unrestricted zero forcing, and further exchange-graph invariants such as diameter. All included verification programs and output records are reproducibility aids, not external certification. References and comparisons are in RESULT.md and AUDIT.json; originality is best-knowledge, not a universal priority guarantee.

Self-review: passed. Independent audit: not yet performed.
