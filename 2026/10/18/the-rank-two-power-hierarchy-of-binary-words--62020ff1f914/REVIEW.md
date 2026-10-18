# Scientific assessment: rank-two power hierarchy of binary words

## Correctness — PASS
A word's rank-two first-order sentence theory is completely determined by the realized pointed rank-one context triples (letter, set of letters to its left, set to its right). The square and cube signatures follow by separating the first, final, and interior copies of a root. Their deterministic prefix transition is mathematically exact, and closure over both possible appended letters exhausts all finite roots. The accompanying plain-Python verifier reconstructs all 37 reachable states and 32 two-letter states; confirms 30 square images, 16 cube images, and both root-minimum histograms; directly recomputes actual word signatures; and checks pairwise separations with the two-round game. The conceptual proof of stabilization for every power at least three is independent of enumeration.

## Originality — PASS, with priority risk
The closest inspected full text is Weis and Immerman's ranker structure theorem for two-variable logic on words (arXiv:0907.0616v2, especially Theorem 8). It characterizes the **logic** but does not tabulate the exact images of the binary square and cube maps or sharp shortest roots. The 1997 temporal-logic equivalence is similarly a general expressive-power theorem. The 2015 paper on 2-binomial squares concerns a different word equivalence. Searches did not locate the precise numerical power-image classification, but absence of matches is not a uniqueness proof; older or unindexed tabulations remain possible, and only summary-level access was available for a separate one-red-word rank-profile result.

## Value — PASS
Power words are a standard natural test family for finite traces and logical periodicity. The theorem classifies which bounded-depth properties can be realized by a repeated binary motif, separates the genuinely distinct square and stable higher-power regimes, and gives exact shortest motifs sufficient to realize every possible rank-two theory in each regime. The figures 30, 16, six, and five are not forced by the generic finite-index assertion alone, and are useful as complete reproducible benchmarks in finite-model logic over periodic words.

## Scientific scope and limits
This is not an unrestricted-word or higher-rank classification; the exact result applies to words containing both named colours, under linear order without a successor relation. The full statement and code-derived finite-state proof are in `RESULT.md`, `verify.py`, and `certificate.json`. Literature priority is provisional pending independent audit.

Self-review: passed. Independent audit: not yet performed.
