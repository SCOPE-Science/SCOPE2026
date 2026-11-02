# Scientific review

## Correctness — PASS
The source's Bernoulli RandProx-LC Algorithm 4 and 5 were reconstructed, including the \(\omega=(1-p)/p\) scaling and the final \(1/p\) primal correction. With \(\gamma=1/\mu\) the primal dependence on its initial value cancels in the first step, leaving one multiplicative iid dual factor. The displayed recurrences yield exact time-indexed moments, the iff interval \(0<a<2\) under nonzero initial dual, the geometric integrated squared-feasibility objective and its unique positive optimum. Algebraic differentiation and boundary/asymptotic calculations were checked both directly and with the packaged symbolic verifier. Finite enumeration supplies corroboration but is not the proof of infinite-time statements.

## Originality — PASS, qualified
The inspected full HTML of Condat–Richtárik, arXiv:2207.12891v3 (Algorithms 2, 4 and 5, Theorem 4, Appendix A.1) supplies the stochastic framework and the sufficient step condition; it does not state the specialized exact cumulative feasibility optimum. ProxSkip, arXiv:2202.09357v2 (Algorithm 1, Theorem 3.6 and Section 3.5), controls Lyapunov rate and sampling frequency at a fixed parameter coupling rather than this unconstrained dual-stepsize tradeoff. Actual search comparisons examined close deterministic primal–dual tuning claims and stochastic variance-reduction results; their assumptions or objectives do not imply the claimed Bernoulli RandProx-LC cumulative law. A related earlier exact scalar analysis under different terminology remains possible, so this is a best-knowledge originality judgment, not independent priority certification.

## Value — PASS
The mean-square feasibility of an equality-constrained solver measures the extent of constraint violation at every iterate, whereas optimizing only the asymptotic dual rate can allow large intermittent primal residuals. The result gives an explicit and unique risk-optimal parameter, separates it from the fastest mean-square rate and from the generic theorem's sufficient boundary, and proves an asymptotically unbounded cumulative-risk improvement as skipped updates become rare. Its practical reach is limited to the stated scalar exact-gradient problem; the exact tradeoff provides a mathematically motivated boundary example, not a broad algorithmic recommendation.

## Scope and remaining risks
The quadratic is scalar, the primal step exactly cancels its smooth gradient, skip indicators are iid, and the metric is cumulative expected squared feasibility. Originality risk persists for unindexed analyses of linear stochastic fixed-point splittings. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
