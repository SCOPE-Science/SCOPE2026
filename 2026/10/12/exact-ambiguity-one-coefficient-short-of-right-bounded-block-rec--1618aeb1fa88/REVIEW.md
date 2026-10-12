# Self-review

## Correctness
PASS. The retained right-bounded-block coefficients form a rank-\(m\) truncated Pascal system in \(m+1\) nonnegative run variables. The vector
\[
v_j=(-1)^j\binom mj
\]
annihilates every retained row and is primitive, so every integer collision is exactly \(s+t\,v\). Intersecting this affine lattice with the nonnegative orthant gives
\[
-T_{\rm even}\le t\le T_{\rm odd}
\]
and therefore exactly \(1+T_{\rm even}+T_{\rm odd}\) compatible words. Independent run-vector and direct subsequence-DP checks agree.

## Originality
PASS. The direct source derives the Pascal equations and the worst-case reconstruction bound, but explicitly says it cannot fully characterize uniqueness in general and asks for better uniqueness criteria when fewer coefficients are used. It does not state the one-short primitive-kernel formula, the exact ambiguity count, or the iff uniqueness test. Targeted alias, broader-literature, exact-formula, and implication searches found no covering statement.

Residual risk remains for an unindexed or unpublished derivation of the same elementary Pascal-kernel fact.

## Value
PASS. This solves the natural first unresolved truncation of the source's reconstruction scheme. It upgrades a worst-case sufficient bound to an exact collision classification one measurement earlier, precisely addressing the uniqueness/fewer-coefficients gap identified by the source.

Self-review: passed. Independent audit: not yet performed.
