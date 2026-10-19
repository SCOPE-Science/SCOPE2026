# Scientific review

## Correctness — PASS
The proof reduces binary 2-binomial equivalence at fixed length to the exact pair of invariants \((t,J)\). It establishes a complete even/odd factor decomposition for the period-doubling morphism and verifies both affine weighted-sum transformations. It then proves the two outer counts by parity separation and the middle arithmetic-progression count by a single-step overlap, with the full length-three base. This proves every exponent. The included verification independently enumerates complete factor profiles through \(k=13\) and checks a separate digit-valuation generator through \(k=10\); finite experiments are not substituted for induction.

## Originality — PASS against inspected sources
Rigo and Salimov introduced the invariant in 2013. The closest direct source is Lejeune's thesis (2021, §4.5, printed pp. 115–117), which considers the same period-doubling fixed point, gives a small-scale plot and qualitative power-of-two versus non-power comparison, but explicitly does not obtain a precise 2-binomial complexity computation. Rigo, Stipulanti, and Whiteland (2022, §7.1) concern related comparisons without the present non-dyadic formula. A matching shifted numerical sequence in OEIS A052968 comes from a different arithmetic interpretation and does not establish this word-specific theorem. Published nearby results on greedy attractors, cocycle ranks, and contiguous composition reconstruction are not covering statements. Earlier equivalent unindexed results remain possible.

## Value — PASS
An infinite natural non-power-of-two family receives an exact formula, with separate class counts at every permitted weight and a complete weighted-position progression at the central weight. The additive \(k+3\) term is explained by the substitution overlap rather than numerical extrapolation. This supplies nontrivial structure for the refined factor complexity of a classical automatic word.

## Limitations
The theorem gives no formula away from lengths \(3\cdot2^k\). The checker has a finite cutoff and does not certify the universal statement by enumeration. Independent audit and external validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
