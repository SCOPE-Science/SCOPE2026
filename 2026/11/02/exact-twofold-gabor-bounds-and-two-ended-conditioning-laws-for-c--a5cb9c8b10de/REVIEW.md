# Scientific review: sharp Erlang Gabor bounds

## Correctness — PASS

The analysis energy is Zak-diagonal at integer translations and half-integer modulations, with multiplier exactly \(|Zg_a(x,\omega)|^2+|Zg_a(x,\omega+1/2)|^2\), rather than half or twice that value. The geometric-series Zak identity is verified algebraically, and the fiber multiplier is strictly increasing in squared cosine frequency, giving exact lower and upper spatial envelopes. Both derivative equations are explicit quadratics with positive discriminant. The lower envelope has coincident endpoints and a strictly negative derivative at zero, forcing its unique global minimum at the smaller root. The upper envelope has coincident endpoints and a strictly negative derivative at one, forcing its unique global maximum at the larger root. The formulas imply positive optimal bounds for every \(a>0\); uniform small-parameter convergence and large-parameter stationary-root expansions establish both sharp condition-number laws. The actual embedded Python checker reproduces the defining Zak series and passes 72,421 finite consistency assertions. Its finite grid is not used as a proof of global extrema.

## Originality — PASS under inspected evidence

The motivating August 5, 2026 paper by de Dios Pont and collaborators establishes the all-lattice frame **existence criterion** for totally positive generators but does not calculate the optimal bounds for the order-two causal exponential window. Kloos–Stöckler's inspected 2013 text treats a Zak transform framework and lower bounds for the even two-sided exponential, a genuinely different generator, not these two exact shape-dependent optima. The inspected 2023 Ghosh–Selvan text determines sufficient frame-region conditions rather than this optimizer. Relevant public mathematical records and prior recoverable local claims discuss compact hat splines, two-sided exponentials, and Gabor existence, none of which implies the repeated-pole Erlang formulas or the two parameter-end asymptotics. Janssen's 1996 paper on exact frame-bound calculations could not be read beyond its abstract; absence of coverage is not claimed, and this incomplete material is an explicit residual risk. The similarity search is evidence of overlap screening only and not a proof of novelty.

## Value — PASS

The repeated-pole Erlang function is a basic smooth, causal, totally positive generator for which the recent frame-set theorem guarantees existence at all strict subcritical densities. Exact *optimal* constants at fixed twofold oversampling answer the distinct stability/design question and show how the window's shape destroys numerical conditioning at both ends even though frame existence never fails. The polynomial \(4a^{-4}\) loss at one extreme and the exponential \(e^{2a-2}/a^2\) loss at the other distinguish two natural degeneration mechanisms, give sharp benchmarks for window selection, and avoid conflating qualitative frame existence with useful conditioning. These statements are neither a reformulation of the frame-set theorem nor generic scaling corollaries.

## Closest literature and limitations

Primary comparisons: de Dios Pont et al., arXiv:2608.04992v1; Kloos–Stöckler, arXiv:1311.7359; Ghosh–Selvan, arXiv:2304.11322. Janssen (1996), DOI 10.1016/0019-3577(96)85088-9, remains a plausible incompletely inspected historical source. Other limitations: only the fixed translation one/modulation half lattice and the exact unnormalized gamma-shape-two family are treated; the minimizing shape parameter's uniqueness is not proved, and the shape asymptotics are not uniform over changing lattices.

Self-review: passed. Independent audit: not yet performed.
