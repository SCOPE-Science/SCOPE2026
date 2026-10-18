# Scientific review

## Correctness

PASS. A length-\(n\) word's entire observation is reconstructible from its number of ones, number of constant runs, initial symbol and unrestricted \(01\)-subsequence count; the resulting product bound is an unconditional fourth-degree upper bound. The explicitly specified four-parameter family has positive block lengths, total length \(n\), recoverable first two parameters from the profile, and distinct remaining pairs by the coprimality of consecutive block lengths. This proves a matching fourth-degree lower bound for every \(n\ge100\). The standalone checker directly corroborates small profiles and the full witness sets at five lengths. No infinite conclusion is inferred from finite enumeration.

## Originality

PASS relative to the inspected sources and targeted statement-level searches; residual risk remains. Golm et al. (2022) consider the first gapped-deck collision length as deck order varies; Rigo et al. (2023) study the gapped-binomial complexity of restricted factor languages and give a binary equivalence characterization. The new assertion concerns the sharp polynomial growth exponent for the *entire full binary language*. Classical \(2\)-abelian and contiguous-pair profile counts are not the same observable. None of the inspected original articles states or implies the matching quartic bounds without the new coprime-block lower construction. Broad searches do not establish uniqueness, and related unindexed studies may exist.

## Mathematical value

PASS. A gap-constrained ordered-pair observation is a natural fixed-read-length model in reconstruction coding. The exact fourth-degree growth exponent gives the sharp logarithmic information capacity, resolving the global growth scale beyond the restricted infinite-word complexities treated in prior work. Establishing four independently distinguishable degrees of freedom by a constructive run arrangement is structural; this is not merely a small parameter instance or a recomputation of an existing sequence table. The leading constant and exact finite-length class count remain open.

## Closest literature and limitations

Primary full-text comparisons: *The Gapped k-Deck Problem* (arXiv:2201.12671); *Gapped Binomial Complexities in Sequences* (ISIT 2023); and *k-Abelian Equivalence and Rationality* (2017). The theorem applies to the full binary language, not one prescribed automatic sequence or the classical contiguous-window observation model. The proof does not claim exact finite-length counts or an asymptotic leading constant; an undiscovered equivalent result is possible.

Self-review: passed. Independent audit: not yet performed.
