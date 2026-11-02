# Scientific review of sharp binary cyclic pair-profile inverse multiplicity

## Correctness — PASS

The object is an indexed binary circle and the observation is its complete four-entry cyclic ordered-pair frequency matrix. The marked-boundary double count proves the exact fiber formula for every nonconstant realized matrix, including periodic input words. Positivity and the displayed successive-ratio identities prove strict centering for transition counts at least two, then the four-residue optimum and the complete tie classification. Constant words and all cases of length at most five are separately resolved. Standard Stirling estimates prove the asymptotic constant. Both independently implemented finite checks are supporting consistency tests rather than the infinite proof: `verify.py` verifies parameter optima through length 200 and direct input enumeration through 19; `crosscheck.cpp` directly enumerates complete four-entry profiles through 20.

## Originality — PASS, with historical qualification

Jacquet–Knessl–Szpankowski (2009/2010), *Counting Markov Types*, DOI 10.46298/dmtcs.2768, counts the number of balanced matrices/Markov types, not their largest inverse multiplicity. The cited 1955 Whittle work provides general per-type cardinality methods: those are recognized prior art, and the individual fiber formula is not claimed as new. Makri–Psillakis–Arapis (2013), DOI 10.5539/ijsp.v2n3p50, counts circular runs of prescribed sizes and overlaps; it does not supply the all-length four-entry worst-fiber optimizer. Published related work on linear adjacent-pair observations counts distinct output profiles and singleton classes; it does not imply the cyclic maximum without a different global optimization. A full reading of Whittle (1955), Inoue–Aki (2010), or unindexed older run literature could alter priority, but their accessible descriptions do not state the exact four-residue extremum or complete optimizer/tie classification.

## Value — PASS

The worst inverse-list size is a natural, exact reconstruction ambiguity invariant under the noiseless cyclic two-gram channel. Its leading constant, the exact phase-dependent maximizing symbol/run content, and all equality ties quantify a worst-case uncertainty not furnished by enumerating the number of observed types or by an unconstrained binomial mode. These features can be used in worst-case list-decoding analysis, even though no noisy-channel capacity is asserted. The claim is a global extremal theorem with structural equality cases, not an arbitrary small-n table.

## Limits and closest sources

The source alphabet is binary, all symbols are indexed, and all wraparound adjacent pairs are observed. No result is asserted about rotation necklaces, nonbinary alphabets, longer reads, or noise. General Markov-type enumeration and exact fixed-type methods remain known literature; their existence limits the novelty claim to the explicit optimized extremum and equality classification. Historical priority remains qualified until independently checked.

Self-review: passed. Independent audit: not yet performed.
