# Scientific review

## Correctness — PASS

The complete observation is the exact multiset of all 36 substring Parikh vectors, not a set or a restricted-window statistic. The polynomial reciprocal argument establishes the four-member constructions. Exhaustiveness for every finite alphabet size follows from equality of source compositions and reduction to the 22 multiplicity partitions of eight. The supplied standalone checker compares exact entire equivalence fibers for all 95,503 canonical words, confirms only the three listed multiplicity types for quadruple fibers, and independently enumerates all words over alphabets of sizes 2, 3, and 4. A separate 13,390-word canonical census proves the no-nonreversal part for lengths below eight. The class enumeration and zero-error coding interpretation follow directly.

## Originality — PASS, with priority risk

The 2010 foundational paper supplies the binary length-eight example and interleaving principle. The 2014 arXiv full text develops the general polynomial-equivalence framework and reports a binary interleaving classification through length 22. These are credited as earlier results, not replaced. The present quantitative statement—complete fiber sizes and exactly \(\binom{q}{2}^{2}\) quadruple fibers over **every** finite alphabet, yielding \(\frac{q^8+q^4}{2}-\binom{q}{2}^{2}\) distinguishable observations—was not found stated in the inspected primary text or relevant database results. Existing general factorization machinery may allow this finite special case to be recovered, and an unindexed prior computation remains a residual priority risk.

## Value — PASS

The first ambiguous blocklength is a natural boundary of the all-substring-composition reconstruction problem. Determining the entire reconstruction fiber distribution there, for all alphabet sizes, gives exact worst-case list size and exact maximal zero-error code cardinality in a natural observation channel. In particular, it quantifies rather than merely exhibits the first failure of uniqueness and distinguishes reversal-only from genuine four-way ambiguities; this is an exact classification of a well-motivated invariant, not a freely chosen parameter slice.

## Evidence and limitations

The checker is a finite exact proof because common relabeling by the source multiplicity partition reduces *every* alphabet size to the finite 22-case test. No claim is made about arbitrary blocklength, noisy reads, or independent certification. Primary literature compared: the 2010 IEEE conference paper and arXiv:1403.2439, particularly its length-eight construction, generating-polynomial criterion, and interleaving discussion. Historical equivalence under alternative terminology remains possible.

Self-review: passed. Independent audit: not yet performed.
