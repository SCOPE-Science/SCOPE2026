# Self-review: first eight-term threshold for factorial divisor sums

## Correctness — PASS

The inclusion/exclusion recurrence for sets of sums using exactly \(j\) distinct divisors is an exact finite identity. The verifier checks every sum in \([0,n!]\), every divisor and every term count through eight for \(1\le n\le12\). At \(12!\), the seven-term complement contains exactly \(175\) integers and the eight-term union covers all \(479001601\) totals, including zero. The two divisor-generation methods, a permuted-order replication, and direct set-based checks for \(n\le5\) independently check the implementation. The explicit eight-term representation of the first difficult integer is confirmed.

There is no inference from a partial census to an infinite statement; the theorem is explicitly finite.

## Originality — PASS

Hughes, arXiv:2609.10902v1, introduces the exact same \(h(n!)\) invariant but proves a large-\(n\) bound and cites the \(\gg(\log n)^2\) lower bound; it supplies no initial-value table. Tenenbaum and Yokota (1990) likewise prove an asymptotic divisor-sum representation result, not the exact first eight-term transition. published-finding corpus and exact database searches found no equivalent factorial-12 classification. The nearest published divisor-subset-sum classification for \(2^a p^b\) covers a different two-prime support and does not control cardinality-constrained representations of \(12!\).

Yokota’s 1992 paper uses the same functional and its 1995 paper concerns factorial knapsacks. Only abstracts/bibliographic material could be accessed, not their full texts, so undiscovered exact data in those sources remain a specifically recorded residual originality risk rather than a claimed impossibility.

## Value — PASS

The 2026 source emphasizes Erdős’s unresolved question for the growth of \(h(n!)\). Determining the complete first 12 values and exactly where the eight-term layer first appears supplies a natural sharp finite benchmark. The 175-element set of difficult integers at \(12!\) is particularly thin and creates a reproducible starting point for studying how such exceptional layers evolve.

## Scope and remaining risks

Nothing here settles the asymptotic rate, subsequent transitions, or a closed-form description of the 175 exceptional values. All claims are self-reviewed finite mathematics, not independently certified.

Self-review: passed. Independent audit: not yet performed.
