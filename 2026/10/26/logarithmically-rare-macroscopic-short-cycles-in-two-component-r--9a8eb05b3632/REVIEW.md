# Self-review

## Correctness

**PASS.** The exact law follows by choosing the cyclic core, counting rooted forests and permutations with two cycles, and correctly dividing the equal-length case by two. The normalization \(Z_n\) is derived rather than assumed. The Gaussian product bound controls the core-count Riemann sums; the macroscopic bivariate intensity follows by a second lattice Riemann sum and an explicit antiderivative. For any fixed \(q>0\), the singularity in the smaller-cycle moment kernel is integrable, which justifies Gaussian domination and yields the sharp integral coefficient. The variance calculation discards the squared mean only after showing that it has smaller logarithmic order. The logarithmic weak limit is distinguished from the nonuniformly integrable moment law. Exact exhaustive enumeration verifies every stratum for mapping sizes two through six; it is not used as an infinite proof.

## Originality

**PASS on inspected evidence, with residual priority risk.** Arratia and Tavaré (1992) treat unconditioned random-mapping core cycles and small-cycle Poisson approximation, including its \(o(\sqrt n)\) range. Their 1994 assembly framework supplies general conditional enumerations, but the inspected sections do not calculate the two-component macroscopic minimum-cycle intensity or its all-positive-power moments. Granville (2006) covers fixed-cycle-count permutation behavior on logarithmic scales, so the logarithmic weak law and exact two-cycle enumeration are credited as classical consequences, not as the novelty. Finch (2022) analyzes fixed-component mapping cycles. The proposed quantitative contribution isolates the \(1/\log n\) boundary layer and the exact associated moment constants. This is not implied by weak-log-scale convergence alone. A prior tailored use of the 1994 generating-function framework or an older mapping monograph could remain unlocated.

## Value

**PASS.** The shortest of two directed cycles in a random mapping is a natural order statistic under a natural rare component-count conditioning. Its logarithmic typical scale suggests a smaller-than-macroscopic cycle, yet *every* fixed positive moment is controlled by logarithmically rare cycles of order \(\sqrt n\). The complete boundary-layer measure explains that mismatch, gives a testable tail integral at every positive scale, and supplies sharp mean and variance constants, not merely an isolated finite coefficient or routine marginal recomputation.

## Literature and limits

The closest inspected primary sources are Arratia–Tavaré (1992, 1994), Granville (2006), Finch (2022), and Tavaré (2022). General conditioned-component enumerations make historical priority difficult to prove exhaustively; a result with the same conditional macroscopic tail would supersede the proposed contribution, but no such claim was located in the inspected material. The theorem is only for fixed component count two, uniform self-maps and fixed positive moment orders. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
