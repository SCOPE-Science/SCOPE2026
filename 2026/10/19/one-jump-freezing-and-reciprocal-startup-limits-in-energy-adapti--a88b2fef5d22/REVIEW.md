# Scientific review

## Correctness — PASS

The direction field and fixed-step energy recurrence are exactly specified. The proof establishes the identity \(\|x_{k+1}-x_k\|=(r_k-r_{k+1})/\|F(x_k)\|\), invokes a valid first-exit argument on a ball where \(F\) stays bounded away from zero, and obtains both geometric energy extinction and summable infinite tail length. The \(O(\eta^{-2})\) remainder includes all iterations after the second, not merely a fixed finite prefix. On \(L(x)=x^2/2\), the landing map is exactly \(-2c/x_0\); for \(c=x_0=1\), \(\eta\ge16\) ensures an invariant negative interval. The 2,372 reproducibility checks agree with the proof but are not an infinite-iteration certificate.

## Originality — PASS with residual risks

The motivating AEPG paper, arXiv:2310.06733, Section 2 and Appendix A, proves unconditional energy stability and *small-step* convergence but does not give the large-step nonstationary limiting map, first-order correction, or infinite-horizon trapping. The original AEGD paper arXiv:2010.05109 anticipates the qualitative caveat that energy stability need not yield primal convergence, but does not supply the quantitative opposite-regime classification here. Semantic mathematical-record and targeted bibliographic comparisons surfaced analogous stability-frontier results for other optimizers, but no statement implying this theorem. Equivalent results under alternative energy-variable terminology remain possible; absence from searches is not proof of global novelty.

## Value — PASS

The theorem resolves a concrete reliability question left open by energy stability: what happens if the base step becomes extremely large? Its all-horizon single-jump limit and first-order correction show a robust open set of nonstationary frozen trajectories even for strictly convex objectives. The reciprocal-startup law and explicit sufficient threshold provide a reproducible benchmark for energy-based gradient methods, beyond a one-step overshoot or a numerical nonconvergence anecdote. The result does not claim a new optimization algorithm or universal finite-step safety threshold.

## Scientific limits

Autonomous smooth positive-definite preconditioners, deterministic exact arithmetic, and noncritical landing points only; the scalar threshold is sufficient rather than optimal. No assertion about stochastic training or full constrained variants. Similar unpublished or older invariant-energy results remain a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
