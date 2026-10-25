# Review of exact ternary-block Catalan valuation distribution

## Correctness

PASS. The all-\(2\) base-three string, the strings with zero trailing \(2\)s, and those with positive trailing \(2\)s form an exhaustive disjoint partition. Kummer's carry identity minus \(\nu_3(n+1)\) yields the explicitly calculated two-state transition matrix. Its rational resolvent gives the exact polynomial identity for every integer \(L\geq0\). Derivatives and root asymptotics establish finite moments, fixed-valuation tails and the normal limit. Independent factorial-valuation enumeration checks through \(L=9\) agree. Finite checks are not relied upon to prove infinite claims.

## Originality

PASS under inspected evidence, with residual priority risk. OEIS A067397 gives individual valuations and a digit-block recurrence, not the joint bivariate block-length/valuation census with exact variance and a normal limit. Deutsch--Sagan's Catalan congruence results and Chen--Jiang's prime-power congruences do not give the claimed aggregate distribution. Li (2018) gives valuation algorithms. The prime-power divisibility paper of Alter--Kubota (1973) is a particularly relevant unavailable full-text source and may contain a stronger result. Published-result searches and semantic mathematical record searches did not identify the same census. Search absence is not proof of uniqueness.

## Value

PASS. The statistic simultaneously counts every three-adic valuation over complete natural base-three windows, rather than reporting a digit-by-digit lookup or merely the zero-valuation density. The closed rational generating function supplies the full finite-scale law; the exact variance, central limit theorem and fixed-valuation asymptotics separate typical from rare behavior.

## Limitations and closest literature

The scope is the single prime \(3\) and aligned windows of length \(3^L\). No all-prime distribution, effective local central limit theorem or off-grid counting formula is asserted. Key related sources: OEIS A067397 (2002, expanded 2015); Alter--Kubota (1973, full text unavailable); Deutsch--Sagan (arXiv:math/0407326v1, 2004); Chen--Jiang (Integers 13, A36, 2013); Li (2018).

Self-review: passed. Independent audit: not yet performed.
