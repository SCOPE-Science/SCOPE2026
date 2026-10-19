# Review of the first third-binomial period-doubling collision

## Correctness
**PASS.** The proof reduces all factors through length ten to slices of three explicit length-thirty-two substitution images; this is exhaustive because factors shorter than sixteen positions cross at most one block boundary. A standalone exact integer recurrence verifies all fourteen subsequence counts for every candidate. There is exactly one doubleton at length ten and no collisions at shorter lengths. Morphism preservation of third-binomial equivalence is proved by decomposing selected subsequence positions into their source blocks, and injectivity of the substitution gives distinct factors at arbitrarily large dyadic lengths. Neither infinite assertion is inferred from a finite experiment.

## Originality
**PASS, subject to the stated literature risk.** Rigo–Stipulanti–Whiteland, arXiv:2201.04603, Section 7, says only that computations suggest a strict third-binomial defect for the period-doubling word; it does not give the unique first length-ten collision or the proven infinite dyadic family. The related Thue–Morse classification concerns another morphism. A 2021 doctoral thesis referenced for second-binomial complexity could not be inspected, so an equivalent unindexed prior statement cannot be definitively excluded. Broader results from available literature and relevant indexed research were compared at the level of their assertions and do not imply the proved sharp threshold.

## Value
**PASS.** The first failure of fixed-order subsequence reconstruction is a natural sharp invariant of a classical automatic word. The unique minimal witness distinguishes the third-order and ordinary factor complexities exactly, and its propagation supplies certified obstructions at infinitely many scales, improving a previously experimental observation. The result does not purport to give a complete third-binomial complexity function.

## Closest sources and remaining limits
The closest fully inspected work is Rigo–Stipulanti–Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, arXiv:2201.04603, notably its explicit period-doubling paragraph. The 2021 Lejeune thesis is a residual access risk. Independent audit has not been performed; possible prior equivalent formulations remain a conventional novelty risk.

Self-review: passed. Independent audit: not yet performed.
