# Self-review

## Correctness (C): PASS

The proof is independent of finite enumeration. The gap vector uniquely represents a binary word, and the scattered \(ab\)-count is the weighted sum of the gaps. Fixing the count of internal \(b\)'s yields the complete homogeneous polynomial, which is exactly a shifted Gaussian binomial. The support proof treats \(A=2\), \(A\ge3\) with internal count zero or one, and \(A\ge3\) with internal count at least two separately. The interval endpoints and touching condition are exact integer statements; the range \(0\le C\le AB\), boundary cases \(B=0\) and \(A=2\), and the universal/existential quantifiers are covered. The standalone checker independently computed all 48 parameter pairs with \(2\le A\le7\), \(0\le B\le7\), with 804 conditional support comparisons and 4,640 direct sandwich subsequence checks. All passed. Experiments corroborate but do not establish the infinite theorem.

## Originality (O): PASS, with priority risks

The closest primary reference is Fazekas, Huang and Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices* (first public October 5, 2026, arXiv:2610.06717), on the same classes. Its available abstract states exact arithmetic criteria for entire subsequence universality and an additive approximation scheme for fixed-pattern probability. These statements do not mathematically provide the precise bivariate \((I,C)\) coefficient formula or the complete modular support in this result. A full-text check was attempted but not available, so exact coverage within the inaccessible body remains a real priority risk, not an asserted negative. Richomme (DOI 10.1016/j.tcs.2025.115732) and Renard–Rigo–Whiteland (DOI 10.1016/j.disc.2024.114381) are the closest partition/q-Parikh references by subject, but only descriptive material was available. The standard Gaussian-binomial marginal is acknowledged and does not imply the conditional spectrum alone. Research-record searches for internal gaps, \(ab^t a\), aliases and Gaussian polynomials returned distinct problems; a related enumeration of universal words of composition \((k,k+s)\) and scattered \(ab\)-pairs does not establish this histogram. See `AUDIT.json` for the four implication comparisons, material inspected, and residual risks. No priority certification is claimed.

## Value (V): PASS

The result is a complete, parameter-uniform distributional classification for a natural statistic on the classical binary Parikh-matrix equivalence classes. The statistic is not arbitrary: its threshold precisely determines the occurrence of every scattered sandwich \(ab^t a\). The support exposes two genuinely different regimes (parity at two \(a\)'s, an interval with a single modular obstruction at three or more), supplies exact fixed-pattern probabilities in each class, and explains the sharp universal-avoidance boundary. The contribution is an exact structural classification, not a marginal q-binomial identity or a small finite increment.

## Scientific limits and source-access risks

The claim excludes one-\(a\) words and arbitrary pattern shapes; it does not address larger alphabets. Some highly relevant full papers remained inaccessible, leaving priority uncertainty. Verification is self-review only; no independent mathematical audit or external certification was performed.

Self-review: passed. Independent audit: not yet performed.
