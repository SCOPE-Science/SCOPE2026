# Mathematical review

## Correctness — PASS

For the precise three-dimensional family, exact projector geometry gives the two surrogate errors. The nonstandard step—proving all-parameter *strict* deterioration—rests on the exact invariants \(T=(r^2+3)/2\), \(D=2r^2/(r^2+1)\), the negative determinant \(1-T+D\), and the positive difference \(T^2-D(r+r^{-1})^2=(r^2-1)^2/4\). These establish the singular-value ordering and the strict condition-number inequality for every \(r>1\). The packaged checker independently evaluates representative cases, but finite checks are not the proof.

## Originality — PASS, residual risk retained

The motivation and spectral preconditioner formula are credited to Huh, Cartis and Nakatsukasa [1]. Their qualitative over-preconditioning discussion and conditional perturbation bound do not contain or imply the precise error-monotone, condition-number-antimonotone construction under the stated parameter hypotheses. Earlier approximate-invariant-subspace deflation theory [2] concerns a different operator and noncovering small-angle regimes. A broader preconditioning literature might contain an equivalent construction, and this residual bibliographic risk is retained rather than asserting uniqueness.

## Mathematical value — PASS

One natural rank-adaptive design heuristic is to increase surrogate rank when the approximation improves. The exact family demonstrates why this signal alone cannot certify favorable spectral preconditioning, even with an SPD matrix and target levels matched to the true trailing singular values. The unbounded rank-increase penalty supplies a quantitative stress test. The claim does not assert the motivating CUR method itself generates these projection surrogates, or that LSQR must converge slowly.

## Limitations and references

Exact arithmetic; fixed three-dimensional SPD family; projection-based rank-nested surrogates; unregularized spectral right preconditioner, not a CUR sampling guarantee. Relevant primary sources are [1] arXiv:2604.05065v1 §§3.1, 4.1, 7.2 and Appendix A, and [2] arXiv:1209.1963 on deflated CG.

Self-review: passed. Independent audit: not yet performed.
