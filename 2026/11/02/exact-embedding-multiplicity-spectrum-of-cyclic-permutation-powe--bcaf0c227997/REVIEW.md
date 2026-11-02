# Scientific assessment: exact cyclic subsequence embedding multiplicities

## Correctness — PASS

A strictly increasing positional embedding corresponds bijectively to block indices satisfying explicit adjacent gap inequalities; nonnegative slacks sum to the period budget. Stars and bars gives every exact coefficient. An increasing-block cut double count proves the generating function and finite alternating-sum formula. Every feasible weak-descent count is realized by bounded increasing runs; strict monotonicity of the binomial coefficient then gives the full exact multiplicity spectrum. The standalone checker compared independent position-wise counting against 9,287 literal distinct targets in 16 host instances, plus 52,318 formal coefficient checks. All parameters and normalizations, including the one-period boundary and equal adjacent target letters, are handled.

## Originality — PASS, with explicit residual risk

Flaxman–Harrow–Sorkin (2004) Theorem 5 gives distinct-subsequence support sizes for cycling source words, not the distribution of index-embedding counts. Kosche–Koß–Manea–Siemer (2021) analyze absent subsequences and their extremal subsets, not positive multiplicity frequencies. Leroy–Rigo–Stipulanti (2017) study general word-binomial coefficients; their general framework does not by itself state this complete cycling-host histogram. Actual searches of published research records and primary literature did not locate an equivalent or stronger encompassing claim. The classical weak-descent enumerator is deliberately not claimed as new. A specialization elsewhere in \(P\)-partition or word-binomial literature is the principal remaining priority for independent checking.

## Mathematical value — PASS

The all-length exact multiplicity distribution is a natural invariant of uniform deletion channels on periodically structured words. It is strictly finer than counting which deletion outputs are merely possible, supplying every attainable nonzero output probability and its number of preimages. The result is a parameter-uniform complete classification, with an independently established positivity range, not an arbitrary finite census.

## Boundaries and closest sources

The proof applies to complete strictly increasing alphabet-permutation periods and uniform selection of surviving positions. It makes no claim about arbitrary periodic words, truncated periods, or optimal coding properties. Primary reference: Flaxman et al. (2004), Theorem 5, on distinct subsequences. Guiding 2021 paper: Kosche et al., *Absent Subsequences in Words*, arXiv:2108.13968. General binomial-coefficient framework: Leroy et al., arXiv:1705.08270.

Self-review: passed. Independent audit: not yet performed.
