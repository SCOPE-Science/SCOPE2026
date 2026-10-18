# Scientific review

## Correctness

**PASS.** Every attribute subset of logarithmically subcritical size has an independently binomial number of supporting rows with polynomially growing mean. Conditioned on the supporting rows, the outside attribute indicators remain independent, so Chernoff and union bounds establish simultaneous closure with summable failure probability. For the upper bound, each concept is uniquely determined by either projection, and those with large extents and intents inject into all-one rectangles; their expected count has a maximum at the double logarithmic cutoff and summable Markov tail. Borel–Cantelli and countably many cutoffs yield the almost-sure limit without cross-size independence. The bounds also yield the expectation exponent. Exhaustive small cases provide independent consistency checks but not a substitute for the analytic argument.

## Originality

**PASS, subject to specialist-literature risk.** Kovács (2018) derives a corresponding exact *expectation* expression, not a concentration theorem. Sakurai (arXiv:2101.11023v1, 2021) proves an *expected-value* superpolynomial lower bound using a related random-context model; Theorem 5.1 does not establish a matching typical-count exponent or simultaneous closure of logarithmically many attributes. Felde–Hanika–Stumme (2020) investigates the Bernoulli coin-toss null model and more general sampling, not the almost-sure concept-count exponent. Searches of published mathematical findings and synonym-based primary-literature searches found no statement implying the combined theorem. Equivalent maximal-biclique-count results outside these accessible sources remain possible.

## Mathematical value

**PASS.** In a standard probabilistic baseline for formal concept analysis, the new law identifies the sharp logarithmic-size exponent of the *typical* full concept lattice, rather than a moment bound. The uniform subcritical-intent result is a concrete structural strengthening. The balanced law provides a sharp baseline for judging the likely output size of concept enumeration. The result addresses a motivated asymptotic gap without claiming an algorithmic running-time bound.

## Limitations and residual risks

The theorem does not give lower-order terms, concentration width, varying incidence probabilities, or dependent incidence patterns. The almost-sure assertion presumes a joint coupling of marginals for each positive integer; cross-size independence is expressly not assumed. Novelty cannot be guaranteed against all unindexed or inaccessible random bipartite maximal-biclique literature. Verification code tests finite consistency only. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
