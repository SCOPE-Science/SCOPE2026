# Scientific review

## Correctness
PASS. The rounded scalar gradient update produces an exact two-state Markov kernel. Solving stationary balance gives the claimed invariant mass, while the second eigenvalue proves convergence from every initialization. Explicit integer-part decomposition of \(v=K\eta\) yields the sharp total-variation envelope, and threshold-approaching targets establish that the bound cannot be improved. Standalone exact-rational checks corroborate transition, stationary, two-step, and sharp-bound calculations for 41,776 parameter cases. These finite checks support but cannot replace the written proof.

## Originality
PASS within the inspected literature, subject to residual historical-priority uncertainty. The 2026 survey identifies StochasticA's finite-bit probability floor but gives no stationary minimax classification. Fitzgibbon and Felix (2025) quantify rounding bias and remedies; El Arar et al. (2024/2025) provide rounding-error models and finite-horizon experiments. Li et al. (2017) study stationary laws under ideal stochastic rounding with nondegenerate stochastic gradients, which does not imply the present finite-bit transition law. A related earlier calculation of finite-bit stagnation for repeated floating-point additions concerns monotone binade absorption rather than a two-state gradient-descent invariant. No exact encompassing statement was found in those comparisons, but priority across all quantized Markov-chain literature has not been independently settled.

## Mathematical value
PASS. This is a complete sharp resource/accuracy law on the smallest nontrivial numerical quantization cell. It makes explicit that a one-step rounding probability error of order \(2^{-r}\) can be amplified by the inverse learning-rate factor into order-one long-run bias, and proves the exact bit budget needed for uniform invariant fidelity. The criterion is motivated by hardware random-bit budgets and by the known disparity between ideal and finite-bit stochastic rounding, rather than an arbitrary numerical parameter slice.

## Limits and closest work
The result is restricted to noiseless scalar quadratics, a two-point grid, floor-based finite-bit rounding, exact pre-rounded arithmetic, independent fresh random integers, and fixed \(0<\eta<1\). Its ideal comparator remains binary-valued, not concentrated at the real minimizer. The strongest conceptual predecessors are Li et al. (2017, ideal stochastic-rounding invariant analysis), Fitzgibbon and Felix (2025, finite-bit rounding bias), and El Arar et al. (2024/2025 and 2026, limited-precision stochastic rounding). Equivalent specialized results may exist in older finite-state quantization literature.

Self-review: passed. Independent audit: not yet performed.
