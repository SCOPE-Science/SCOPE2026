# Scientific review: two-neighbour rank-correlation support bound

## Correctness

**PASS.** The finite bound follows from an exact upper-rank threshold decomposition and three finite-state potential certificates. Every supporting inequality is justified by eight nonnegative transition slacks and four terminal-state checks. The proof keeps the three self-neighbour boundary terms, which are necessary for the cancellation. The analytic Riemann-sum computation gives \(L_n/n^2\to13/24\) and the lower-endpoint bound \(-3/8\). A standalone rational checker replays all 36 certificate entries and exhaustively checks 409112 rank permutations for sample sizes through nine. Finite enumeration is not used to justify the universal quantifier.

## Originality

**PASS on inspected evidence.** Lin and Han's paper introduced the precise modified rank statistic and proves the broader but weaker lower range bound \(-1/2+O(M/n)\). Their preprint's complete finite-sample-range discussion and journal article's corresponding remark do not supply the three weighted-path-square inequalities, the explicit integer sum, or the \(-3/8\) guarantee for \(M=2\). Dalitz, Arning and Goebbels investigate the upper endpoint and rescaling of the original one-neighbour coefficient, and Xia et al. employ different inverse-distance weights; neither is a direct proof of this claim. The closest retrieved publicly indexed mathematical findings concern different rank correlations or permutation statistics.

**Residual risks:** A prior result about extremal linear arrangements of the square of a path or finite-range binary-word energy might imply the component inequalities. The finite threshold-bound sum is not proved optimal, and no historical uniqueness is certified.

## Value

**PASS.** Attainable finite-sample values of the multi-neighbour statistic are directly relevant when interpreting a sample dependence score. The prior guarantee allowed values asymptotically as low as \(-1/2\), whereas the new argument excludes every value below \(-3/8-o(1)\) at two right neighbours. The change of one eighth is a fixed-scale improvement, with an explicit integer inequality for every sample size. The boundary correction and the finite-state proof provide a reusable structure for adjacent-neighbour rank functionals, rather than an isolated numerical observation.

## Scope and limitations

The result is a valid lower support bound, **not** an exact determination of the most negative possible statistic. It applies to distinct ranks and the published two-neighbour normalization, with the original end-of-sample self-neighbour convention. The review did not establish the same bound for arbitrary neighbour count, tied samples, or alternate normalizations. Historical originality is not independently certified.

Self-review: passed. Independent audit: not yet performed.
