# Scientific review

## Correctness (C): PASS

Greedy subsequence matching in the repeated block has last position \(1+u_m+3H(u)\); absence is therefore equivalent to at least \(k\) weak descents. A one-letter deletion removes either zero or one descent. Requiring one removed descent at both ends and every interior position produces exactly the finite-state language in the theorem, with no missing boundaries. Nine-state transfer multiplication enumerates every such word once; the matrix determinant and adjugate have been expanded exactly by the accompanying symbolic checker. Direct subsequence tests reproduce every layer through \(k=6\), and separate integer transfer counts match totals through \(k=8\). The asymptotic statement is an explicit exponential lower bound, not a numerical extrapolation.

## Originality (O): PASS, residual literature risk

The closest inspected primary source is Kosche et al., arXiv:2108.13968 (2021), Section 3 (in particular pp. 205–212 and Proposition 3.6). Its repeated-increasing-block result presupposes an even alphabet of at least four letters, and provides an exponential construction rather than a ternary bivariate length enumerator. Manea et al., arXiv:2504.21471 (2025), chiefly introduction and stated results, give general enumeration algorithms and a longest-minimal-absent-subsequence algorithm, without the closed family-specific rational series. Search terms included variants of minimal absent subsequence, ternary repeated permutation, weak descents, rational generating function, the leading counts, and scattered subsequence; no covering formula surfaced. Relevant source statements, not merely their titles, were compared. The prior binary repeated-block calculation is limited to a two-letter alphabet and has a different generating function. A possibly unindexed computation or an earlier explicit specialization of the general characterization remains a genuine priority risk.

## Mathematical value (V): PASS

The precise family is naturally singled out by the arch factorization and by the earliest constructions showing that minimal absent subsequences can be exponentially more numerous than shortest ones. The original even-alphabet construction does not treat ternary words. The theorem closes this first nonbinary small-alphabet gap with an exact *length-resolved* infinite classification, not a routine finite table or a mere existence proof. The weak-descent language description, explicit nine-state transfer, rational bivariate series, and exponential lower-bound construction provide reusable structure and benchmarks for combinatorics on scattered subsequences.

## Scope and remaining risks

Only the increasing ternary cycle repeated in a linear word is classified. The univariate rational denominator does not by itself establish an optimal real-valued growth constant here, which is not claimed. More targeted human bibliographic review could uncover an equivalent closed formula. No independent assessment is represented.

Self-review: passed. Independent audit: not yet performed.
