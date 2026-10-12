# Self-review

## Correctness
PASS. The compatibility-graph formulation is equivalent to the non-overlap definition. The exact size-\(14\) optimum is published, and the bundled exhaustive search visits every size-\(14\) clique once. Direct pairwise Hamming checks give \(1{,}148\) cases of minimum distance \(1\) and four of minimum distance \(2\); the four form one complement/reversal orbit.

## Originality
PASS. The closest primary source proves the size-\(14\) optimum. The later full-census paper computes all optimum solutions and their number but does not state the Hamming-distance refinement in the inspected text. Alias, exact-parameter, table/database, and implication searches found no source stating or implying the final histogram and orbit claim. Residual risk remains that an unindexed computation derived the same statistic from the public optimum data.

## Value
PASS. Hamming separation is directly motivated by synchronization in the presence of symbol errors. The result isolates the only four cardinality-optimal binary length-nine synchronizing codes that avoid distance-one codeword pairs and classifies them up to the natural complement/reversal symmetry.

## Closest literature and limitations
Chee et al. establish the exact cardinality \(14\) at binary length nine. Stanovnik et al. later compute the full optimum-solution set. This result neither improves that size nor claims a general family; it resolves only the secondary Hamming-distance extremum and equality cases at this parameter.

Self-review: passed. Independent audit: not yet performed.
