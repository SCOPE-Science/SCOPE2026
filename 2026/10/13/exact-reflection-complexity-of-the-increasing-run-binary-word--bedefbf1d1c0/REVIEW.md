## Correctness — PASS
Every complete run of W occurs exactly once, so factors with >=2 changes cannot be right-special. The only right-special length-n factors are 0^n, 1^n, 0^a1^b with a<=b and 1^a0^b with a<b, totaling n+1, establishing p(n). Reversal partners cannot exist for >=3 changes because their pair of internal run lengths would need nonincreasing as well as nondecreasing, contradicting the 0^k1^k,0^(k+1) arrangement. Count single-switch pairs as n-1 and two-switch pairs as T(n)+T(n-1), with T(m)=#{1<=a<b: a+2b<=m}. The stated rational generating function yields p(n)-r(n)=floor(n(n+1)/6), proving r(n) and limiting ratio exactly. The independent standard-library checker enumerates factors/orbits through n=140, specials through n=85 and numeric pair identity through n=1000; these are corroboration, not the infinite proof. The word is aperiodic due to unbounded lengths of both symbol runs.

## Originality — PASS
2024 arXiv:2406.09302 supplies the general conjecture, not this word or formula. Dvořáková--Pelantová 2026 explicitly provides a periodic 2/3 example, which fully covers refutation of the unqualified literal conjecture; the present surviving claim instead explicitly gives a nonperiodic 2/3 example and the exact all-length complexity formulas. Their positive ratio-1/2 result requires reversal-closed language, which W lacks. published-finding corpus and web searches targeted constructions, aliases, ratios and stronger cases; no implication covers this aperiodic claim. Residual unindexed-equivalence risk is reported.

## Value — PASS
The precise aperiodic case is motivated by a later peer-reviewed paper pointing out a missing aperiodicity hypothesis in a published conjecture, leaving a natural repair. An exact, elementary binary aperiodic witness with quadratic factor complexity shows that aperiodicity alone does not rescue the proposed 1/2-or-1 dichotomy. The paired-factor counting mechanism supplies interpretable all-n formulas, not a routine finite extrapolation. Does not assert a broader theorem for recurrent, morphic, or reversal-closed words.

## Closest literature and limits
Primary comparisons: arXiv:2406.09302 (original conjecture) and Dvořáková--Pelantová (2026) (periodic 2/3 example and reversal-closed positive cases). The present example is not uniformly recurrent and its language is not closed under reversal; residual priority risk persists for unindexed equivalent descriptions. Finite computation only corroborates the all-length proof.

Self-review: passed. Independent audit: not yet performed.
