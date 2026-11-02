# Scientific review: a quadratic recurrence for Thue–Morse shortest absent subsequences

## Correctness

PASS. Each Thue–Morse prefix at substitution level \(m+1\) is a concatenation of \(2^m\) complementary binary blocks, guaranteeing that every binary target of length \(2^m\) embeds, while \(0^{2^m+1}\) is absent. The greedy first-double-block argument gives the exact local forbidden-transition criterion for every target at the shortest absent length. Multiplication of two explicitly specified unimodular matrices counts the distinct absent targets, not their occurrences. The Thue–Morse complement recursion produces a square of a conjugated matrix, and its trace and all-entry sums prove the coupled recurrence for all levels. A separately implemented direct subsequence automaton, brute enumeration and matrix products agree in 276 finite comparisons. Risks: no non-dyadic-prefix extension is claimed; finite enumeration is not a substitute for the algebraic induction.

## Originality

PASS under inspected-source comparison, not a claim of absolute uniqueness. The primary 2021 absent-subsequence paper develops general characterizations and algorithms, but its inspected text does not contain an exact count or quadratic recursion for these specific substitution prefixes. The 2024 extremal-number paper gives broad same-universality envelopes; its proof addresses bounds and alternating permutation blocks, which neither state nor force the nonextremal dyadic-prefix sequence \(3,5,12,74,2666,\ldots\). The 2018 Thue–Morse binomial-complexity paper treats the number of equivalence classes of factors for a fixed comparison depth and multiplicity data; it does not supply the count of distinct missing strings at the growing shortest-absent length. Relevant prior published computational claims on binary Fibonacci extremals and random permutation-block absence counts have different quantifiers and cannot determine this deterministic sequence. Risks: an equivalent automatic-sequence trace-map formula outside the inspected literature may exist; a failed search is not proof of novelty.

## Value

PASS. Distinct shortest absent scattered subsequences are a canonical invariant of subsequence universality. Computing their exact cardinality on every dyadic prefix of the classical Thue–Morse word is a natural infinite-family problem, rather than an arbitrary finite census. The recurrence replaces an exponentially long input and an exponentially large set of potential missing targets by a fixed-size algebraic update and reveals a substitution renormalization invisible in extremal or expectation-only formulas. The precise hierarchy and method can serve as a baseline for other morphic words. No unsupplied downstream theorem is claimed.

## Sources and limitations

Primary papers and dates: Kosche et al. arXiv:2108.13968 (August 31, 2021); Adamson et al. arXiv:2407.18599 (July 26, 2024); Lejeune–Leroy–Rigo arXiv:1812.07330 (December 18, 2018). The important unsolved comparisons are unindexed exact Thue–Morse missing-subsequence enumerations and equivalent trace formulas. The scope is dyadic prefixes only; the independent scientific audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
