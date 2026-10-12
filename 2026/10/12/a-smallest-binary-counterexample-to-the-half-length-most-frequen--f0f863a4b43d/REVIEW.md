# Self-review

## Correctness (C): PASS

For a given binary input word \(w\), appending its last symbol partitions every occurrence of every subsequence according to whether that position is used. This gives a complete, exact integer recurrence. Exhaustion of all binary source words of lengths \(2\) through \(14\), with no quotienting by symmetry, finds only four exceptions, all of length \(14\). Two independent direct position-subset tallies cross-check every frequency for representatives `01010001110101` and `01110101010001`; their unique length-eight maximizing subsequences occur 144 and 147 times, while the best length-at-most-seven patterns occur 136 and 144 times. The attached verifier checks every assertion and outputs an explicit success marker only after all checks.

## Originality (O): PASS; residual risk

Fang's full arXiv:2406.02971v3, Section 5, Conjecture 5.7 asserts that *at least one* most frequent subword has length at most \(\lceil n/2\rceil\). It is contradicted by both explicit strict frequency gaps. The first arXiv version uses a stronger, differently phrased quantifier and is not treated as the target of the contribution. Source tables concern entropy-minimizing inputs, not exhaustive input-word counterexamples; Menon–Singh studies fixed-pattern counting and different optimization order. Targeted searches for half-length and mode-length formulations, exact 14-bit words, and semantic-index nearest results did not identify any covering theorem or known identical certificate. Absence of a search result is not a proof of first discovery; an unindexed equivalent result or relevant uninspected appendix remains possible.

## Mathematical value (V): PASS

This provides a substantive negative answer to an explicit conjecture that proposes a general algorithmic reduction in the search length. Exact binary minimality and complete first-failure classification identify where the heuristic ceases to work; the strict margin of eight or three occurrences, respectively, rules out a mere tie at half length.

## Limits

The result only classifies binary inputs through length fourteen, establishes binary minimality, and refutes the alphabet-unrestricted conjecture using a binary example. It does not classify longer or larger-alphabet cases, settle complexity of finding a most frequent scattered subword, or claim unique historical priority.

Self-review: passed. Independent audit: not yet performed.
