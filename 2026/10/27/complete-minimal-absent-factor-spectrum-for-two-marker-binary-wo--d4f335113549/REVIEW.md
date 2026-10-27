# Scientific review: complete two-marker minimal-absent-factor spectrum

## Correctness — PASS

The result uses the exact noncircular contiguous-factor definition. Prefix/suffix factor existence is necessary and sufficient for an absent string of length at least two to be minimal; missing alphabet letters are handled separately. Candidate words are exhausted by their number of ones (zero, one, two, or three), with four or more impossible. The union of two down-closed lattice rectangles yields the complete one-one-containing list; two-one candidates require the sole actual internal gap, except for missing core gaps with present left/right contexts. These facts imply the three-case count. A disjoint gap-order partition proves both the all-length sharp maximum and uniqueness for length at least six. Direct geometric summations yield the generating function and its leading coefficient. The actual checker in this package was executed and matched 1,531 independent MAW sets, 32 aggregate coefficients, and extrema for all lengths 6 through 89. These finite checks corroborate, rather than substitute for, the infinite proof.

## Originality — PASS, with priority risk

The 2014 suffix-array work provides a general extraction algorithm and a minimality test, but not a fixed-weight-two structural formula. The 2018 alignment-free comparison paper is particularly close: its Section 3 already uses exactly the family of words with ones at the endpoints to show a linear lower bound and explicitly describes the length-minus-two core minimal absences. The witness and its linear order are known; neither is being claimed as original. The result assessed here is the *complete* seven-type gap-dependent antictionary, its exact three-case cardinality, full sharp extremal classification, and rational aggregate across all weight-two words. Neither inspected primary paper states or logically determines those formulas without further case analysis. Searches of published mathematical records and the scientific literature did not locate an equivalent. An unindexed exact classification remains a residual risk.

## Value — PASS

Minimal absent factors are the finite antidictionary of a word, an alignment-free pattern-information invariant. Fixed minority weight two is the first nontrivial sparse regime in which two separate marker contexts interact. Exact cardinality and the full absent-set list quantify that interaction for *every* gap triple; the rational weight-two mean gives a natural statistic rather than a handpicked finite count. The unique high-antidictionary configuration for all sufficiently long words provides a sharp structural extremum. The result does not claim general Hamming-weight bounds or improvements to generic extraction algorithms.

Closest literature: Barton et al., arXiv:1406.6341 (2014), and Charalampopoulos et al., arXiv:1806.02718 (2018). Limits: noncircular binary strings with precisely two ones; residual risk of earlier unindexed equivalent results.

Self-review: passed. Independent audit: not yet performed.
