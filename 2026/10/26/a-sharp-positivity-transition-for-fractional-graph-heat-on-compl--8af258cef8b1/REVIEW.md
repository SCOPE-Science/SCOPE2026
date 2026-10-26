# Scientific review

## Correctness — PASS
The proof uses an explicit orthogonal decomposition of the complete multipartite Laplacian. Its off-diagonal matrix entries have only two forms, making both positivity and induced endpoint norms exact; strict convexity after multiplying the within-part entry by an exponential proves that each relevant part has exactly one positive cutoff. Direct differentiation gives the unique peak for that part; Taylor expansion after factoring out the always-present time-zero root yields the two different critical orders. The checker independently reconstructs and diagonalizes the finite graph matrices (11,556 successful assertions). Infinite-family conclusions are proved analytically, not inferred from the checks.

## Originality — PASS within the inspected evidence
Riascos–Mateos develop a fractional graph diffusion formalism and focus on the positive range of fractional powers. The 2015 eventual-positivity papers of Daners–Glück–Kennedy give general spectral conditions but not the full sharp multi-partition norm and critical-order crossover. Earlier exact fourth-order heat formulas on complete bipartite graphs are subsumed as a known restricted slice; the fractional-power family, the sharp critical transition, and unequal-part comparisons are not asserted to follow from those fixed-power results. A related published three-spectral-value theorem was seen in abstract, but no full text was available to compare beyond its qualitative statement. Literature could contain an equivalent calculation not located in the inspected sources.

## Value — PASS
The order-one spectral-power boundary separates genuine positivity preservation from eventual positivity in a natural class of higher-order network diffusion models. The result quantifies not just the first safe time but the maximum possible sign-induced sup-norm amplification, with different first nonzero exponents in the near-critical asymptotics. Both invariants have independently meaningful uses in estimating positivity recovery and bounded-data stability on graph networks; the formulas apply to all finite part-size profiles and do not require solving a new matrix problem for each graph.

The asserted historical novelty is limited to the scope of the comparisons performed. No independent mathematical or bibliographic certification was obtained. The analytical theorem is limited to the unnormalized, undirected complete multipartite Laplacian with a fixed graph in the critical asymptotics.

Self-review: passed. Independent audit: not yet performed.
