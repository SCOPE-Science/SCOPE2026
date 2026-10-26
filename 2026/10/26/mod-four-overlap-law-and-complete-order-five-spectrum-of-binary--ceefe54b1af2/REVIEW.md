# Review

## Correctness — PASS

The local matching of the two incoming to two outgoing arcs at each binary de Bruijn vertex gives a unique bit, and the resulting permutation is a single cycle if and only if its wiring represents an order-\(k\) cyclic de Bruijn sequence. Each agreement of wiring bits contributes exactly two common length-\(k+1\) factors. Both constant vertices are forced to have crossed wirings to avoid a self-loop being a separate permutation cycle, proving the lower bound \(4\). Single-cycle permutations all have the same sign; changing one local wiring swaps two images, so the total wiring distance is even, proving the congruence modulo \(4\). For \(k=5\), both exhaustive methods in `verify_overlap.py` passed and counted all \(2048\) circuits and all \(2096128\) unordered pairs. The computed spectrum is not extrapolated to other orders.

## Originality — PASS

The 2011 orthogonal de Bruijn paper's full text supplies the definition and binary obstruction, but does not enumerate nonzero overlap or the exact order-five pairwise spectrum. The 2011 CDMA paper exhausts the same \(2048\) cycles for cyclic bit cross-correlation, a different mathematical statistic from set intersection of six-mer types. Relevant 2025 generalized-orthogonality sections address collection-size bounds and balanced variants. The closest previous local result on order-five palindrome counts concerns an invariant of individual cycles, not pairwise common contexts. The novel comparison is the exact statement and its implication, not merely the absence of the same numbers in a search. Residual risk: the full 2025 paper and some specialized arc-disjoint-cycle literature were not comprehensively inspected.

## Value — PASS

Orthogonality is a natural design objective for collections of de Bruijn sequences, but binary pairs cannot have zero context overlap. The exact mod-four restriction, attainment of the forced value four, and full distribution over the first family of \(2048\) cycles quantify that obstruction directly. At the sharp end only \(736\) cycles admit an optimum partner and it is unique when present, a useful structural classification that is not determined by the known count of de Bruijn cycles or by bit cross-correlation.

Self-review: passed. Independent audit: not yet performed.
