# Scientific review: neighboring central trinomial residues modulo five

## Correctness

**PASS.** The mod-five digit product follows by the Frobenius congruence and the no-cross-digit-cancellation argument for signed exponents in the interval from minus four to four. Exact multiplicative character orthogonality counts digit-product fibers. The unique trailing-four decomposition partitions every index other than the all-four endpoint, and four explicit quotient calculations for each parity yield the two lookup vectors. The endpoint contributes exactly once. The deviation-sign argument applies to every \(L\ge2\); the boundary values \(L=0,1\) are checked directly. A standalone exact-arithmetic program corroborates all sixteen cells through \(L=7\), but the proof is infinite and does not rely on that enumeration.

## Originality

**PASS on the inspected evidence, with disclosed residual priority risk.** Deutsch--Sagan and Rowland--Yassawi provide the Lucas-product and automatic congruence framework but no displayed explicit joint sixteen-cell law or sharp two-point total-variation expression. Kohen's later paper proves an offset-carry decomposition and applies it to densities of linear comparisons involving adjacent central trinomials, including \(T_n\equiv T_{n+1}\pmod p\); that marginal is **prior coverage**, not new here. The accessible earlier local results concerning central trinomial pairs are modulo eight, while a separate neighboring criterion is modulo nine; neither implies the mod-five pair formula. Targeted scientific-record searches and public literature queries returned no exact coverage. General automatic-sequence and Kohen offset-carry methods could allow implicit derivations not stated in the inspected full texts; independent priority checking is outstanding.

## Value

**PASS.** Adjacent arithmetic sequences are correlated by carry propagation, so a one-point Lucas law alone does not specify an adjacent-pair distribution. The result gives a closed finite-window sixteen-cell census at every scale, proves every possible pair appears at the first nontrivial full-digit scale, and determines the exact rate and constant of convergence to independence and uniformity. These are natural complete invariants of a classical number-theoretic sequence, not an arbitrary isolated numerical instance. The restriction to prime five and two consecutive terms remains explicit.

## Closest literature and limitations

See Deutsch--Sagan (2004), Rowland--Yassawi (2013), and Kohen (2024) as listed in RESULT.md. The primary theoretical precursor is the Lucas digit product, rather than any assertion that no general automatic-sequence machinery can recover the count. The stronger novelty risk is a general previously published two-point theorem whose specialization would dominate the exact count. No claim is made about longer patterns, prime powers or arbitrary cutoffs.

Self-review: passed. Independent audit: not yet performed.
