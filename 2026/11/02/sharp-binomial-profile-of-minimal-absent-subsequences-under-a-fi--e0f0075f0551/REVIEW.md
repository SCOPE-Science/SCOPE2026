# Scientific review: sharp fixed-letter-count MAS profile

## Correctness

**PASS.** The statement quantifies over all binary source words with exactly \(k\ge1\) ones and every integer \(r\). Greedy matching of every minimal absent word with its final symbol removed provides a well-defined ordered subset of source one-indices. Minimality fixes every zero block preceding one of those indices and fixes the final zero block. Thus the pair (selected source indices, final bit) is an injection, yielding Pascal's identity for each layer. The explicit source \((010)^k\) realizes all encoded pairs; the two-zero interior gaps give concrete one-index shifts that embed the word after deletion of any letter. The argument treats the empty selection, consecutive selected indices, terminal zero versus terminal one, and all boundary layers. A separate Python implementation tests all 4094 nonempty binary inputs through length 11 and every candidate from the extremal construction for \(1\le k\le9\).

The proof, not the finite experiments, establishes the all-length assertion. Code correctness does not certify the general theorem independently.

## Originality

**PASS with residual novelty risk.** The closest primary work, Kosche–Koß–Manea–Siemer, *Absent Subsequences in Words* (arXiv:2108.13968), establishes the definition and greedy-embedding characterization of MAS and exhibits general exponential families. Its Theorem 3.1 has arbitrary source content and provides no sharp upper bound by the number of occurrences of a designated letter or exact \(\binom{k+1}{r}\) profile. The present quantitative injection, the simultaneous extremizer, and the complete Pascal profile are additional statements requiring distinct arguments. Adamson et al., *Tight Bounds for the Number of Absent Subsequences* (arXiv:2407.18599), counts all missing length-constrained subsequences at fixed universality, not minimal missing subsequences with prescribed Parikh coordinate. Manea et al., *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String* (arXiv:2504.21471), treats output-efficient algorithms, not this parameterized maximum. Targeted literature searches did not identify the same statement or a stronger theorem immediately implying it.

Residual risk: an equivalent inequality for minimal excluded subwords under the subsequence order might be available in unindexed literature or an unstated corollary of an older combinatorial structure theorem. This was not independently audited.

## Value

**PASS.** Minimal absent scattered subsequences are natural antichain generators of the complement of a word's subsequence language. General input-length bounds can be exponentially large and are not sensitive to a rare letter. The theorem identifies a sharp, source-length-independent parameterized bound \(2^{k+1}\) when only \(k\) ones occur, and resolves the entire rare-letter composition spectrum at the same time. Its explicit all-layer extremizer demonstrates that none of the binomial layer bounds can be improved separately. The result is a complete natural extremal classification of *counts*, not a table recomputation or an arbitrary short input case. It does not classify all extremizing source words.

## Closest literature and limits

- https://arxiv.org/abs/2108.13968 — definition, canonical MAS characterization (Theorem 3.1), and general exponential examples.
- https://arxiv.org/abs/2407.18599 — all absent subsequences at fixed pattern length/universality; different statistic.
- https://arxiv.org/abs/2504.21471 — modern MAS algorithms and longest-MAS computation; no prescribed-letter sharp extremum in the inspected analysis.

The result is confined to a fixed binary alphabet and minimal scattered subsequences; it neither supplies larger-alphabet analogues nor resolves input-length-based MAS maxima. The explicit verifier checks finite examples and construction behavior, not an infinite certificate.

Self-review: passed. Independent audit: not yet performed.
