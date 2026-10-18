# Scientific assessment

## Correctness — PASS

The result holds for independent equiprobable orientations on every complete graph with at least three vertices. The deterministic transitive-triple identity is reconstructed in the proof. Its centered form decomposes the cyclic-triangle count into quadratic degree-score statistics. Conditioning on the sole edge common to two degree scores proves pairwise orthogonality without assuming independence. The fourth central binomial moment yields the variance. Conditioning on the complete outneighborhood of one vertex gives an independent fair tournament on the remaining vertices and a binomial cross-edge cycle contribution; pairwise indicator orthogonality proves the conditional variance. An \(L^2\) projection then proves the sharp \(1/n\) explained-variance bound. Exact-rational exhaustive enumeration for \(3\le n\le6\) verifies all formula families. Infinite-parameter correctness depends on the displayed proof, not on these checks.

## Originality — PASS, with residual historical uncertainty

The classical deterministic formula expressing the cyclic-triangle count through the whole score sequence is explicitly not claimed as new. Grzesik, Kráľ, Lovász and Volec (arXiv:2008.06577) discuss this identity while studying extremal cycle densities. Kolesnik and Sanchez (arXiv:2009.09322) give a geometric description of realizable mean-score vectors. Kuo, Liu, Ribas and Zhou (2019, *The Shifted Turán Sieve Method on Tournaments*) give counting bounds for tournaments with a prescribed number of cycles. Their inspected statements do not supply the per-vertex orthogonal quadratic fluctuation decomposition, exact two conditional moments, or the optimum nonlinear \(1/n\) variance fraction.

The closest previously recorded related result concerns an orthogonal decomposition between three- and four-cycle counts on four-vertex subsets; it does not express cyclic triangles through conditionally predictable vertex-score fluctuations. Andersson (1998, *On the asymptotic distributions of subgraph counts in a random tournament*) is a relevant broader source: its abstract was inspected, but complete text was not obtainable, so possible implications cannot be ruled out. An older generating-function treatment of score sequences might also make these formulas implicit. Search nonhits alone are not used as proof of novelty. Independent historical-priority assessment is still outstanding.

## Value — PASS

The statistic is natural in paired-comparison data: the total number of intransitive triples measures global cyclicity, whereas a competitor's number of wins is a directly observable local score. The exact sharp value \(1/n\) answers a concrete prediction question: no arbitrary nonlinear transformation of one score can explain more than this fraction of global cycle variance. The otherwise uncorrelated raw score becomes informative through its centered square, and the complete conditional variance measures the residual uncertainty for every attainable score. This finite-size projection and orthogonality structure is more than a restatement of the known deterministic score identity.

## Limits

The statements apply only to independent fair games, not general stochastic score sequences. Quadratic score terms are orthogonal but need not be independent. The checked contemporary papers are not an exhaustive history of tournament probability. The finite computation is supplementary and the reported originality remains subject to external priority review.

Self-review: passed. Independent audit: not yet performed.
