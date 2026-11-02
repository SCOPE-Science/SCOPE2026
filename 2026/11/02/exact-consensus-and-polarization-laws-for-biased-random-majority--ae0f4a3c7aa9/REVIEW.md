# Scientific review: biased random majority on complete bipartite networks

## Correctness (PASS)

The state reduction is exact because all vertices in a part see the same other part. The even-time parts depend on disjoint sets of random coins, so their limiting colors are independent conditional on the fixed initial coloring. The first two-step update of a tied part gives the renewal equation \(u_*=C+D(A+Bu_*)\), and its companion for \(v_*\). Central binomial tie masses satisfy \(B,D\le1/2\), giving contraction \(BD\le1/4\), eventual absorption and the explicit uniform geometric tail. Product probabilities follow from the two independent limiting side colors. The central limit theorem yields the claimed critical scaling with opposite-side orientation. Eighty independent exact-rational absorbing-chain calculations (980 states) support, but do not substitute for, this infinite-family proof. Risks: the tail bound may be non-optimal; extension to other graph families is not established.

## Originality (PASS with residual priority uncertainty)

The most relevant full-text source, A. N. Zehmakan's 2023 preprint and 2024 open journal version, contains fair-tie even-cycle outcome probabilities and the even-time independence argument. Those are expressly credited and not claimed as new. The source does not present a deterministic-initial-state exact formula for every biclique with two different tie probabilities, its uniform hitting bound or its Gaussian two-bias transition. The 2022 Lesfari–Giroire–Pérennes model selects one update at a time and favors an opinion even outside ties, so does not imply the statement. Search of available published research findings yielded static multipartite majority coloring and parity-automaton classifications, but no covering stochastic-majority result. Implication was checked by update rule, graph family, initial-condition type, parameter coverage and conclusion, not by title. Residual priority risk: an unindexed biclique-specific or interacting-particle result might already contain the formulas; this review does not establish unique historical priority.

## Mathematical value (PASS)

The three-class hitting distribution is a complete exact classification for an infinite, natural two-community graph family, with two independently variable behavioral biases and arbitrary deterministic initial colors. It pinpoints a discontinuous macroscopic consensus-versus-polarization change when biases cross one-half, a nontrivial Gaussian finite-size scaling window and a universal expected transient bound. In contrast, general networks can exhibit exponentially long transients in the motivating work. These statements describe structural social-dynamics behavior rather than a routine finite special case.

## Verification boundaries

Independent external proof audit and specialist-priority review have not been carried out. Mathematical generalizations beyond complete bipartite networks are unproved. All finite exact computations were reproduced from the standalone code and form corroboration only.

Self-review: passed. Independent audit: not yet performed.
