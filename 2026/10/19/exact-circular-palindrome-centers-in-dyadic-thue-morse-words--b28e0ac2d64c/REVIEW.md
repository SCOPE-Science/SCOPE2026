# Mathematical review

## Correctness — PASS

The 4-letter substitution-block calculation rules out cyclic palindromes of length five and hence all odd lengths at least five. Exact mirror-pair decimation relates even-gap palindrome radii to parent anti-palindrome radii. At odd gaps the latter are exactly one or three, governed by the equality of two parent symbols; a fourth pair would require a forbidden five-letter palindrome. Base cases at depths one and two handle all exceptional full axes. The valuation recursion gives every asserted center radius, and a direct residue check at depths three and four proves both parity-specific sharp bounds. Half-turn complementarity gives the two distinct long factors. `verify.py` checks all 131056 centers at depths four through sixteen by a separate direct scan, but the proof—not the scan—establishes the infinite scope.

## Originality — PASS with residual risk

Materially inspected literature discusses infinite-word palindromic complexity/lacunae, general circular-palindrome bounds, and periodicity from palindromic equations. The nearest relevant complete preprint (Blondin Massé et al., 2011, doi:10.1016/j.tcs.2010.07.005) addresses different equations and does not imply this Thue–Morse gap-wise formula. Simpson (2014) states a universal count bound in its accessible abstract, which cannot supply individual radii. Search comparisons of conjugate words, exact tables, equivalent local-symmetry statements, and stronger covering claims did not identify the classification. The full Simpson article and some Thue–Morse specialized papers remain incompletely accessible; equivalent unindexed work is possible.

## Mathematical value — PASS

The position-resolved classification reveals sharp parity-dependent macroscopic reflection structure in a canonical cyclic automatic word, with exactly four secondary centers and an exact long-palindrome count at every relevant length. This is a natural structural invariant not determined by the existing aggregate palindromic-complexity values or a routine small numerical extension.

## Limitations

All statements are for dyadic circular Thue–Morse words, at substitution depth at least four, counting palindromic factors no longer than the circle. Finite checks do not certify statements beyond their tested depth. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
