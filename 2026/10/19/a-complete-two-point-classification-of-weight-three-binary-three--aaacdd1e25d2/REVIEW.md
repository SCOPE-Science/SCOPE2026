# Scientific review

## Correctness — PASS

The eight length-three subsequence counts of a binary three-one word follow from the three zero-prefix sums and the three gap coordinates. With the total zero count fixed, the full deck is determined by the counts for 011, 101 and 001. Equality of the first two forces the affine gap displacement \((t,-3t,3t,-t)\); equality of 001 then forces \(t(c-b+3t)=0\). The nonzero solution is unique, proves all fibers have size at most two, and gives an exact involutive parametrization. Independent gap-counting produces the stated rational series, with no extrapolation from finite coefficients. A standalone full-deck checker compares all source words with up to 25 zeros and 500 deterministic larger cases. No theorem for larger weights or alternate channels is claimed.

## Originality — PASS, with residual literature risk

Chrisnata et al., *On the number of distinct k-decks: Enumeration and bounds*, Section 5.3 (DOI: 10.3934/amc.2021032) prove the 2-deck nullspace observation and a cubic-order bound, but expressly formulate the all-length rational series as Conjecture 1. The new part is the complete three-deck fiber classification and an all-length proof of that precise conjecture, not the known nullspace calculation. The 2019 conference antecedent does not give the conjectured enumeration. Nilforoushan–Parvaresh (arXiv:2609.23106) obtain unrestricted-weight growth exponents and linear affine-dimension results, not this exact fixed-weight count; infinite-word binomial complexity is likewise a different problem. Searches by conjecture, equivalent formulations, and deck fiber parameters found no covering result. Equivalent material could exist outside the inspected corpus; the absence of a search hit alone is not treated as novelty proof.

## Mathematical value — PASS

An exact all-length solution to an explicitly posed enumeration conjecture supplies a complete structural account of the zero-error ambiguity for the smallest unresolved fixed-weight three-deck slice. Beyond the rational series, it determines every fiber and proves a nontrivial asymptotic one-quarter ambiguous-word proportion. This is an intrinsic sequence-reconstruction invariant, not an arbitrary finite parameter chosen for computational convenience.

## Residual limitations

The work does not establish higher-weight counts, noisy-channel capacity, or independent third-party validation. It depends on a self-contained proof and finite corroborative checks; no source-access limitation is concealed.

Self-review: passed. Independent audit: not yet performed.
