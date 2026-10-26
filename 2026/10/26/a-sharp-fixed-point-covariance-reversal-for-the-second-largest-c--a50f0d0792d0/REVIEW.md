# Scientific review: a sharp fixed-point/second-cycle covariance reversal

## Correctness
PASS. Conditioning on one fixed point proves the exact covariance identity. The classic ranked-cycle insertion construction gives a nonnegative cycle-type expectation \(T_m\) and the exact sign formula \(\operatorname{Cov}(F_{m+1},B_{m+1})=(1-T_m)/(m+1)\). Two disjoint explicit families of cycle partitions yield a harmonic lower bound exceeding one for odd \(m\ge9\) and even \(m\ge14\); exact rational cycle-index sums close the remaining cases. The asymptotic covariance follows from the known second-ranked cycle limit and the standard vanishing-ties estimate. Two different exact rational algorithms and enumeration of \(46{,}232\) permutations agreed. No finite experiment is used as an infinite proof.

## Originality
PASS, subject to historical-priority uncertainty. Shepp and Lloyd (1966) explicitly give the ranked-cycle insertion moment formula and the second-ranked mean constant; those are prior ingredients. Ford (2022) provides relevant cycle-count bounds, and Mukherjee (2015) discusses fixed-point limits. The examined full texts did not state a finite fixed-point/second-largest-cycle covariance sign classification with its exact size-six threshold, nor the limiting negative covariance. A general insertion identity does encode the moments but does not supply the needed all-size harmonic comparison. Searches of mathematical literature and analogous permutation-dependence claims found no logically stronger direct coverage. A historical derivation not indexed by these sources remains possible.

## Mathematical value
PASS. The sharp threshold is a natural, full-parameter dependence classification between two classical statistics: a local singleton-cycle count and a macroscopic ranked-cycle length. The sign becomes strictly negative at the first size six and never returns, with a nonzero limiting covariance \(-\gamma_2\); this cannot be inferred from their marginal distributions or generic asymptotic independence of short-cycle counts.

## Scope and limitations
Uniform permutations only; the second-largest length counts tied cycles separately and is zero for one-cycle permutations. The proof cites classical ordered-cycle limit theory and a tie bound; its quantitative limiting constant is not newly discovered. The general ranked-cycle insertion identity originates with Shepp and Lloyd. Historical-priority risk persists; no external or independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
