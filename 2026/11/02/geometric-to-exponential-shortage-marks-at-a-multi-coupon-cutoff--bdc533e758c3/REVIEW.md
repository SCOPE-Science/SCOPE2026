# Scientific review

## Correctness — PASS

The exact Poisson/Gamma lower-tail identity and falling-factorial ratios determine the conditional shortage mark. In the large-multiplicity regime the necessary uniform approximation holds because \(m_nh_n^2\sim2\log n\to\infty\), so mark scales \(j=O(1/h_n)\) make the factorial error vanish. The hazard identity converts the extreme Gamma quantile into an \(e^{-x}\) rare-event intensity. Poissonization gives independence; an order-preserving Poisson-clock sandwich de-Poissonizes *cumulative* depth counts and hence the whole finite marked law. The standalone checker reproduced 276 finite assertions. These computations support exact identities but do not replace the limiting proof. The result assumes uniform iid coupons and a convergent quota-to-logarithm ratio; temporal joint convergence is not proved.

## Originality — PASS, with priority limitations

The closest direct earlier work is Long, arXiv:2604.25108v2, §3.1, where the *indicator* that a type is short is counted via an exact binomial law. Castro and Marinho, arXiv:2610.33199v1, establish the growing-quota completion-time cutoff, not the conditional depths and their geometric/exponential regimes. The present claim differs by tracking the number of missing *copies* and proving a marked point-process and compound-Poisson family in all three growth regimes. Ilienko's fixed-index occupancy limits and Gnedin–Janson–Malinovsky's fixed-threshold stopped extrema were inspected for possible stronger implications; their quantified regimes do not supply this growing-quota result. Older broad occupancy point-process or threshold theory may contain an equivalent corollary; novelty has not been independently validated.

## Mathematical value — PASS

The scalar Gumbel event answers whether all quotas have been met, but does not describe the unfinished workload conditional on failure. The shortage total is a natural operational statistic, not a freely selected invariant. Its limiting law changes from a simple Poisson count to geometric compound Poisson and then to a rescaled exponential compound Poisson. The transition is nontrivial because the number of deficient types stays tight while their individual depths change scale. This distinguishes occupancy geometry at a natural cutoff, independently of any further downstream application.

## Limits and relationships

No extension to nonuniform coupon probabilities, stopping-time configurations, or an entire time-evolving marked process is asserted. The quantile scale and unmarked rare-event count are credited to earlier work; the mathematical priority of the marked-depth statement remains subject to broader human inspection.

Self-review: passed. Independent audit: not yet performed.
