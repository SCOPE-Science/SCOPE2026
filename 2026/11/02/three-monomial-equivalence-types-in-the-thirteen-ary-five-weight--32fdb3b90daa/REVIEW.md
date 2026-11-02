# Review of the thirteen-ary cyclic-code equivalence classification

## Correctness

The source theorem gives an explicit trace generator for every admissible exponent. Coordinate exponent inversion reduces all parameters to the six units modulo \(14\); the field Frobenius gives explicit coordinate-permutation equivalence between each \(r\) and \(-r\). A bijection from all dimension-two subcodes to projective lines establishes the support-size interpretation. The standalone standard-library verifier exhaustively enumerates the unique reduced row-echelon description of each of \(31110\) projective lines, independently compares the \(14028\) secant-pair counts, and verifies the existing five-weight spectrum for all \(28561\) message vectors. The exact code and proof cover all boundaries and all admissible parameters, not merely a sample.

## Originality

Hernández--Vega Theorem 6 proves the common weight enumerator but does not state this complete support-size distribution or partition into three equivalence classes. Its later support-containment analysis is a different invariant. Related published line-spectrum and higher-support results concern different linear codes; those statements cannot imply the exact three profiles here. Searches for aliases, the five-weight parameters, projective secants and subcode support spectra yielded no covering theorem. Residual publication-priority risk remains from unindexed calculations and incomplete access to some older related work.

## Value

A complete equivalence classification is a natural structural problem whenever a single parameterized construction has identical ordinary weight enumerators. The full rank-two subcode support distribution is an invariant not determined by those enumerators and gives a concrete way to distinguish the three classes. Thus this is a classification of the entire admissible parameter set at a natural odd-prime specialization, not an arbitrary extra codeword count. The result does not claim a general odd-alphabet formula or a coding-performance improvement.

Self-review: passed. Independent audit: not yet performed.
