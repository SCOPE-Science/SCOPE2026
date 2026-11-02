# Self-review

## Correctness

PASS. For every finite alphabet \(\Sigma\) with \(|\Sigma|\ge2\) and each four-letter word, all fifteen possible equality patterns are exhausted by the fourteen positive cases and the single negative pattern `0100`. Thirteen positive cases have explicit stochastic two-state certificates and rigorously positive gaps, verified by exact rational and independent denominator-cleared integer arithmetic. The constant case has an elementary absorbing-reject-state witness. Convex averaging supplies matrices for any unused alphabet letters while preserving a strict maximum. Restricting an alleged `0100` witness to its two active letters contradicts Gill's binary classification, and Kjos-Hanssen gives the three-state upper bound. There is no inductive inference from finite experiments.

## Originality

PASS, subject to stated priority limitations. Gill's 2024 theorem classifies binary words, not patterns with three or four distinct letters. Kjos-Hanssen's 2026 theorem provides three states for all words but does not give a two-state classification for multiletter words. The seven three-/four-distinct-letter length-four patterns, including `0123`, are not consequences of either result. Checked semantic research-record queries, direct web literature searches, and accessible earlier local claims found no exact alphabet-independent length-four classification. The binary cases are explicitly credited to Gill, not presented as new. Unindexed alternate presentations remain a residual risk.

## Value

PASS. This solves the first length where a binary word demonstrably needs three probabilistic states, while allowing any alphabet cardinality. The unexpectedly simple answer (only the `0100` equality pattern is exceptional) gives the exact \(q(q-1)\) count and demonstrates that two stochastic states suffice even for four pairwise distinct symbols. It fills a concrete classification gap left by the binary-only two-state theorem and all-alphabet three-state bound. This is a complete natural small-length classification, not an arbitrary parameter slice or a restatement of numerical data.

## Scope and priority limits

The finding does not classify longer words, optimize probability margins, or certify that no unindexed earlier source implies the statement. The 2026 primary source was materially inspected for its general definition, principal theorem and construction; its full final sections could not be retrieved in this run. The available abstract and introduction explicitly describe a complete *binary*, not nonbinary, determination. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
