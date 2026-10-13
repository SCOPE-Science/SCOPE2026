# Review

## Correctness
PASS. The local divisibility argument proves squarefreeness without importing a nonstandard lemma. Parity completely handles even \(N\) and forces odd \(M\ge3\) for odd \(N\). For fixed support size the exact expression \((\prod(p_i+1)+1)/\prod p_i\) is coordinatewise decreasing in every prime, so the first odd primes give the maximum. Exact rational evaluation through fifteen primes gives a strict bound below \(3\), contradicting integral odd \(M\ge3\). The checker independently replays each finite arithmetic step.

## Originality
PASS. Subbarao's inspected 1998 paper proves the sixteen-prime bound for the plus-sign equation \(\psi(N)=MN+1\), not the minus sign. Yamada's inspected 2023 paper gives analytic upper bounds for both signs but cites the lower-support result only on the plus branch. Searches for the minus congruence, low-support classification, and sixteen-prime threshold returned no covering statement. OEIS A001615 and A203444 give function/range data rather than the equation theorem.

## Value
PASS. The result closes the entire low-support region for the minus-sign companion equation at the same natural sixteen-prime boundary that is classical on the plus side. The cutoff is structurally motivated by the extremal Euler product rather than an arbitrary computational range, and the proof isolates reusable squarefreeness and parity reductions.

## Closest literature and limitations
The closest prior theorem is Subbarao's plus-sign lower bound \(\omega(N)\ge16\). Yamada treats \(\pm1\) simultaneously only for upper bounds on the multiplier. No existence is established beyond the new barrier, and an unindexed elementary observation remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
