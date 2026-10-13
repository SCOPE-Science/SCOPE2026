# Scientific review

## Correctness — PASS

The statement fixes a three-symbol ordered alphabet, all lengths at least six, and both self-overlaps and distinct-word overlaps of precisely lengths two and three. A code of length at least six injects into its set of three-symbol prefixes, arbitrary middle words, and three-symbol suffixes. Its prefix and suffix triple sets are disjoint and their respective two-letter end-block sets are disjoint. Each ordered pair of symbols has exactly three exhaustive statuses (unused/prefix/suffix), giving 19683 configurations. For each, allocating the intersection of the two candidate triple sets gives the stated exact integer upper envelope. Two implementations of this finite optimization both attain maximum 132; the construction has eleven allowed triples at the left and twelve at the right and satisfies both disjointness conditions. This proves the exact all-length result without extrapolating finite experiments.

## Originality — PASS

Yang–Ding's full-text Construction 3.5 and Theorem 3.4 give a family of restricted-overlap codes, not an optimum for the unrestricted ternary \((2,3)\) problem; specialization to their short-block bipartition choices yields at most \(108\cdot3^{n-6}\). Stanovnik's Proposition 3 already supplies the scaling in length, but not the missing numerical base value. Blackburn and collaborators' full-text treatment derives general bounds and binary constructions for \((1,k)\); their Cartesian prefix–suffix decomposition is prior technique, not the ternary optimum. Exact-value, alias, and upper-bound literature comparisons did not find the value 132. Residual risk: earlier unindexed computations or independent derivations could contain an equivalent optimum.

## Value — PASS

Determining the maximum at the smallest stable base length resolves a natural open finite coding-size invariant and all its arbitrary-length extensions. The result strictly improves the size of the available simple alphabet-bipartition construction in the emerging ternary setting, from 108 to 132 at base length six. It is neither a renamed binary statement nor merely a computation of codewords in a previously specified construction; the upper bound quantifies over all codes with the prescribed overlaps.

## Scientific limits

The proof uses a complete 19683-case integer certificate, whose source is embedded; the formula does not apply to all non-overlapping codes or to forbidden intervals other than \((2,3)\). The known length-reduction proposition is credited rather than claimed. Scientific validation beyond the checks described here is outstanding.

Self-review: passed. Independent audit: not yet performed.
