# Self-review

## Correctness

PASS. The domain requires \(b\to\infty\) and \(m_b\to\infty\), independent fair unary colours, and exactly equal-size equivalence classes. The probability that some class has exactly \(j\) red vertices is \(1-(1-p_{j,b})^{m_b}\), with \(p_{j,b}=\binom bj2^{-b}\to0\). Its convergence is equivalent to extended convergence of the expected count. The ratio of consecutive expectations tends to infinity, so at most one fixed minority index has a finite positive limit. Multinomial generating functions prove independent complementary Poisson counts at that index; binomial variance bounds prove absence/abundance elsewhere. The truncated-colour EF back-and-forth game establishes sufficiency for **all** fixed first-order ranks and exact attainable threshold-event spectra. The executable finite checks corroborate the enumerative and finite-game components without certifying infinite assertions.

## Originality

PASS, with historical-priority risk. published-finding corpus searches of the equal-block coloured-equivalence convergence criterion, critical binomial cell intensities, aliases, and broader random-partition limit laws did not identify the same necessary-and-sufficient theorem. Koponen's 2026 result concerns FMP and conditions for deterministic zero–one laws of base structures, not this sharp colouring-scale classification. Ahlman–Koponen (2013) studies uniform structures conditioned by automorphism-group support, not independent fair unary colourings of equal blocks. Prior analysis of **uniform random set partitions** with sparse markings concerns a different base law and does not imply conditioning on all block sizes being equal. The elementary Poisson and EF machinery is acknowledged prior mathematics. Search failure alone does not establish historical uniqueness; a general, unlocated product-class limit-law theorem could subsume the result.

## Value

PASS. This gives an exact and necessary-and-sufficient classification of a natural random expansion's logical convergence across **all** growing block-count scales, detects exactly when convergence is nonzero–one, and describes the complete limiting-probability spectrum. The critical logarithmic hierarchy \(m_b\asymp2^b/b^k\) has a concrete logical interpretation as visibility of exactly \(k\) exceptional vertices of either colour per class; the statement is not a single isolated counting identity or a routine increase in a bounded computational cutoff.

## Closest literature and limitations

The closest checked source is Koponen, arXiv:2610.16163v1, especially Example 2.12, Corollary 2.14, Remark 2.15 and Theorem 3.1. Ahlman–Koponen, arXiv:1305.3097v3, Sections 1 and 6, supplies a distinct earlier programme of logical limit laws. The result excludes unequal class sizes, biased/dependent colouring, extra order relations, and stronger logics. The uniform effectiveness statement is confined to explicit canonical sequences. Historical priority is qualified and external independent scientific assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
