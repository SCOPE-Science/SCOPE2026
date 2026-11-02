# Review: exact covering-distance spectrum

## Correctness — PASS

The original published 84 integer codewords are embedded in full. All 84 values are distinct and within the 22-bit domain, and the exact minimum pairwise Hamming distance is 9. A direct distance computation runs over each of the 4,194,304 ambient words and all 84 codewords, while an independent multi-source Hamming-cube BFS visits all 4,194,304 states and produces exactly the same 23 bucket counts. The direct loop and the BFS are exhaustive algorithms for a finite domain, not empirical projections. Both show radius 8, 176 deepest holes, and exact mean nearest-codeword distance 2737427/524288. The embedded standalone source can be rebuilt and replayed.

## Originality — PASS, with residual risk

The closest source is Ota, Osa and Harada's arXiv:2610.11609v1, first posted October 8, 2026. It establishes the (22,84,9) construction and minimum distance, but does not provide its covering radius, complete ambient distance spectrum, or number of deep holes. Comparison by implication matters: knowing the original codewords and minimum pairwise distance does not already state or logically force the specific calculated histogram without additional analysis. Targeted searches of published mathematical records, related coverage tables, and accessible prior claims found no equal result; this does not preclude obscure or unindexed computations. The exact list is credited, not presented as a new code construction.

## Value — PASS

Covering radius is the natural maximum nearest-codeword distance, contrasting the minimum distance used for guaranteed correction; the complete nearest-distance spectrum quantifies how many received words lie at each separation. The exact 176 deepest holes and mean distance add useful decoding-geometric information about a freshly published record construction that the size-and-distance parameters omit. This is a whole-space, canonical invariant of a named mathematical object, not an arbitrary subinstance or known-table recomputation.

## Limits

No optimality among all codes with these parameters, asymptotic extension, or independent external audit is claimed.

Self-review: passed. Independent audit: not yet performed.
