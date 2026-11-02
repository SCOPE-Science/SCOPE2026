# Scientific review

## Correctness — PASS

The pivot event was derived from the spectral decomposition of the indefinite quadratic form associated with the two sketched column norms. Two independent Gaussian sketch rows produce independent \(\chi^2_2\) variables and an exact exponential integral. This proves the probability and expected loss for every rank-two real input, not merely an asymptotic or sample estimate. Rotating the fixed Gram spectrum yields the full feasible interval of column-norm gaps. A one-variable derivative with the unique positive root of \(u^2+u-1=0\) proves the global piecewise maximum and equality cases, including the transition boundary. Checks from the standalone program agree with the formulas; they supplement rather than replace the proof.

## Originality — PASS (qualified)

The first sketch-pivot mechanism and rank-revealing guarantees are established in the 2015 randomized QR literature and the 2023 CQRRPT paper. Sign laws for Gaussian quadratic forms and chi-square differences are established separately, including Gaunt (2024, Theorem 2.1 and Corollary 2.11); **neither the distributional representation nor the sign formula is claimed as new**. The distinctive claim is the complete orientation optimization of expected squared-first-pivot loss at fixed singular spectrum, its golden-ratio crossover and strict equality classification. The inspected sections of the primary full-text sources did not state or imply the optimized loss curve as a previously established theorem. Search results do not prove uniqueness: an earlier equivalent calculation in a specialized statistics or randomized QR analysis remains a meaningful residual risk, and Duersch–Gu's full preprint was not available for thorough inspection.

## Value — PASS

The first diagonal entry in QR with max-norm pivoting is the length of the chosen column, so its squared expected regret is a canonical local measure of pivot fidelity. The result shows an unexpected orientation transition invisible to singular values alone: at high anisotropy the worst loss comes from two nearly equal-length, strongly correlated columns, not orthogonal singular-axis columns. Its exact asymptotic coefficient quantifies the limitation of using a minimal Gaussian sketch for the first pivot. This result does not assert downstream approximation-error or stability bounds.

## Closest sources and limitations

- Melnichenko et al., arXiv:2311.08316, §§2.1–2.3 and 4: Gaussian-sketch QRCP, embedding-based guarantees, and pivot-quality comparisons rather than this exact extremal expected loss.
- Martinsson et al., arXiv:1512.02671, §§3.1 and 4.2: Gaussian-sketch pivot choice and numerical comparison, not a spectral-orientation maximization.
- Gaunt, arXiv:2408.04101, Theorem 2.1 and Corollary 2.11: a stronger general sign-distribution framework covering the probability sublemma; no QR regret orientation maximum.
- Duersch and Gu, arXiv:1509.06820: related randomized QR construction; the accessible material was insufficient for a conclusive full-document negative comparison.

The findings are limited to two Gaussian sketch rows, two real matrix columns, squared first-pivot norm regret, fixed Gram spectrum, and exact arithmetic. Independent originality confirmation has not been performed.

Self-review: passed. Independent audit: not yet performed.
