# Scientific review

## Correctness — PASS
For a two-state generator the rank-one stationary projector gives exactly \(M=\Pi+r(I-\Pi)\), so the smallest diagonal is nonnegative precisely when \(r\ge-m/(1-m)\); the off-diagonals are positive. The stage-derived rational multiplier is differentiated and evaluated at both parameter endpoints. Solving its threshold quadratic in the uniform randomizer proves every branch of the probability law. Exact limiting algebra gives the one-third frontier and square-root onset. The idempotent projector gives the cumulative-product identity and a uniform positive-product cutoff. The standard-library checker passed 4,703 additional rational and deterministic approximation checks. No infinite quantifier is inferred from that finite checker.

## Originality — PASS (subject to historical priority risk)
The July 2026 Eisenmann–Jans–Kruse–Podhaisky source gives the randomized scheme, the scalar amplifier, and A-stability; it does not state a stationary-balance-dependent probability of entrywise-stochastic two-state matrices or the repeated-product dichotomy. Previously studied sign reversal on scalar decay tests \(r<0\), unlike the relevant threshold \(r<-m/(1-m)\); the scalar sign probability alone does not state the one-third balance boundary or the endpoint law for a two-state generator. Published Crank–Nicolson return-resolvent and two-midpoint-step SSP-SDIRK2(2) Markov classifications use different stability maps, and the closest 2024 randomized implicit scheme has a different tableau. Originality is limited to the present combined exact two-state random-matrix classification, not to the projector identity, RK stability function or generic positivity theory. A specialized old theorem might imply the formula; searchable primary literature cannot rule this out.

## Mathematical value — PASS
Whether a numerical transition operator preserves every probability vector is a basic invariant-cone question in conservative kinetics. The exact success probability, sharp one-third rate-imbalance frontier, finite zero-success threshold, and non-Lipschitz onset are directly interpretable as stochastic mesh-step reliability criteria, distinct from scalar A-stability. The distinction between infinitely recurrent unphysical one-step operators and eventually strictly positive accumulated propagators is a useful structural warning against equating local and long-time positivity. The model is intentionally two-state and autonomous; no extension to larger systems is claimed.

## Closest sources and limitations
- Eisenmann, Jans, Kruse, Podhaisky (2026), arXiv:2607.18928v1 — same tableau and scalar amplification, distinct matrix-stochasticity question.
- Bochacik, Przybyłowicz (2024), arXiv:2404.19059 — randomized implicit methods with different stability function.
- Horváth (1998, 2005) — general Runge–Kutta cone-positivity theory, possible broad earlier implications; limited full-text access.
- Published two-state Crank–Nicolson and SSP-SDIRK2(2) Markov analyses — distinct rational maps, no equivalent claim in inspected results.
- Earlier scalar sign-risk computations for this same random tableau — threshold \(r<0\), not stochasticity of a two-state operator.

Self-review: passed. Independent audit: not yet performed.
