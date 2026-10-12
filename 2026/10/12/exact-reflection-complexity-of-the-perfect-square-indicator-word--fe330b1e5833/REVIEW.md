# Scientific review: exact reflection complexity of the perfect-square indicator word

## Correctness — PASS

The square gaps are the strictly increasing odd numbers, so every factor with at least two marked positions has a unique earliest-pair index and a unique left offset. The restrictions from the preceding square yield a complete finite count for each index. Factors with at least three marks have no reversed occurrence because reversing strictly increasing consecutive gaps would make them strictly decreasing. The remaining two-mark factors have precisely identified reversal partners, and the even/odd sums simplify to the asserted exact expression. The proof treats boundary indices, including the adjacent squares \(0\) and \(1\), and factor lengths \(0\) and \(1\). Direct census at all lengths through \(100\) and a separate formula-versus-gap check to length \(2000\) corroborate the arithmetic; neither is substituted for the infinite proof.

## Originality — PASS, conditional on incomplete global indexing

The full accessible text of Allouche–Campbell–Li–Shallit–Stipulanti (arXiv:2406.09302) introduces the invariant and evaluates different sequence families; it does not give this square-support formula. The full accessible text of Dvořáková–Pelantová (arXiv:2511.12358) treats periodicity and low reflection complexity, not this polynomial-support example. Targeted publication searches and semantic research-index queries for exact square-indicator reversal classes, formula aliases and asymptotic ratios did not reveal coverage. The searches do not prove priority; an unindexed exact or more general sparse-word result remains a residual risk.

## Value — PASS

The characteristic word of integer squares is a canonical sparse arithmetic sequence. The closed formula for every factor length is not a generic consequence of the known reflection-complexity bounds. It gives the exact effect of reversal identification in a polynomial-gap setting and proves an asymptotic \(2/3\) ratio to ordinary complexity, in contrast to automatic and exponentially spaced examples. It is a self-contained, motivated complete evaluation rather than an arbitrary finite parameter slice. The result does not assert a general law for all sparse words.

## Restrictions and provenance

The proof is mathematical and the reproducible finite checks use standard Python only. No external expert or independent audit has been performed. The public release date of the motivating invariant is 2024-06-13; the later full-text revision is not substituted for that first release. Priority is subject to the residual literature risks recorded above.

Self-review: passed. Independent audit: not yet performed.
