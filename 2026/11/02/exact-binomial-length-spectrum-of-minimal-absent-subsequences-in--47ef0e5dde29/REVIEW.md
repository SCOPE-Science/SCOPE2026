# Scientific review

## Correctness — PASS

The proof identifies an exact block-use cost for greedy subsequence embeddings in alternating binary words. An explicit case analysis of single-letter deletions gives necessary and sufficient local constraints, not just necessary ones; a four-state transfer matrix counts exactly the resulting words. A formal binomial-series expansion yields every length-refined count. The standalone program separately checks every candidate through the eighth parameter value, all one-position deletion cases, and 50 integer transfer-count distributions. The proof, rather than finite checks, establishes all positive parameter values. Residual risk is limited to possible human errors in the transfer-matrix simplification or coefficient extraction, both symbolically and computationally cross-checked.

## Originality — PASS with residual priority risk

The closest 2025 primary paper establishes algorithms for arbitrary words, not the explicit fixed-family closed-form spectrum stated here. The foundational 2021/2022 paper provides general structural tests, and the 2024 paper counts all absent subsequences rather than their minimal elements. Published related work on maximal counts of shortest absent subsequences and on subsequence universality covers different quantifiers and statistics. No equivalent statement was identified by targeted source and mathematical-record searches. The 2023 Troníček paper is materially relevant and has not been examined in full; a matching special-case theorem there or in unindexed work remains a possible prior-art risk, not evidence of novelty. Independent publication-priority review is still needed.

## Value — PASS

The alternating family is a canonical minimal-length binary family whose entire scattered-subsequence content is understood by block structure. The theorem answers the natural next question: the complete minimal-absence boundary, its lengths and multiplicities, and the output-size growth relevant to any minimal-absence enumeration method. The exact binomial spectrum is an infinite-family classification, not a sporadic numerical table; its exponential total despite a linear shortest-length layer is a meaningful structural contrast. The result does not assert a new general-purpose algorithm.

Self-review: passed. Independent audit: not yet performed.
