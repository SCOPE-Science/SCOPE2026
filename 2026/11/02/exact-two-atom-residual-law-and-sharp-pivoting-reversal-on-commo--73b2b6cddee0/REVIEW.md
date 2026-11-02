# Scientific review

## Correctness

**PASS.** The Schur complement of \(D+b\mathbf1\mathbf1^{\mathsf T}\) after any chosen subset is \(D_{S^c}+(b^{-1}+\sum_{i\in S}d_i^{-1})^{-1}\mathbf1\mathbf1^{\mathsf T}\). This proves order-independence and the two possible trace values. Conditional pivot probabilities give the finite survival product. The exact difference factorization proves both optimal-subset classification and randomized-versus-greedy comparison, including equality. The explicit scaling family proves the divergent ratio and uniform correlation limit. An extracted-package checker should reproduce 9,345 rational/computational checks; these do not replace the proof.

## Originality

**PASS, with priority risk.** Chen–Epperly–Tropp–Webber (2022; especially Algorithm 1, Sec. 4.2, App. C.2) already establish general greedy failure and rank-one Schur algebra, but their block-diagonal obstruction does not imply all pairwise normalized correlations tending to one, nor does it supply this exact \(k\)-step two-value trace law and sharp criterion. Steinerberger (2024, Secs. 2.2–2.3) analyzes greedy's misleading diagonal information and alternative randomized exponents, without the displayed common-factor classification. Epperly (2026, Secs. 1–4) supplies broad random pivoting error bounds, not the particular distribution or finite-parameter equivalence. Searches of original papers, published research records, and the accessible local claim index did not surface a direct equivalence. A previous specialist result may have been missed; independent literature checking remains appropriate.

## Value

**PASS.** Common-factor covariance models are a natural testbed in kernel low-rank approximation. The exact law gives testable benchmarks for randomized pivoting, and the sharp crossover identifies when choosing the largest variance is counterproductive. The fully coherent, almost equal-diagonal counterexample rules out a plausible heuristic that high mutual correlation protects greedy pivoting, going beyond a routine small numerical example. General optimality of random pivoting or a general positive-definite matrix classification is not claimed.

## Limits and closest literature

The result is algebraic, exact-arithmetic and trace-norm-specific. It does not extend by assertion to other error norms, weighted kernels, arbitrary diagonals or floating-point implementations. Closest references: https://arxiv.org/abs/2207.06503, https://arxiv.org/abs/2404.11487 and https://arxiv.org/abs/2608.20633.

Self-review: passed. Independent audit: not yet performed.
