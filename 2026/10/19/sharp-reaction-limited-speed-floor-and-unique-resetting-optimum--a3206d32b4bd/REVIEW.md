# Scientific review

## Correctness — PASS

The killed drift-resolvent and Poisson renewal formula are derived directly with the correct delta-killing normalization. A coefficient-sign argument proves a unique global optimizing reset rate for every inward drift, including zero drift. The global lower bound follows from elementary inequalities, is strict for finite parameters, and is saturated in a controlled strong-drift limit. Symbolic perturbation yields the two-term optimized rate and time expansions. The small-drift derivative proves a turnover must occur. The standalone checker reproduces independent resolvent and algebraic computations; numerical sampling does not serve as an infinite proof.

## Originality — PASS (residual risk)

The motivating 2026 article explicitly contains the exact forward drifted mean absorption formula and plots a nonmonotonic optimum for representative parameters, so neither is claimed new. Its Appendix A.2 proves uniqueness only without drift; Appendix A.5 treats weak drift and direct numerical optimization rather than all-parameter inward-drift uniqueness, the sharp finite-reactivity bound, and strong-drift asymptotics. The 2013 partial-trap result is driftless. The 2018 drift-restart paper assumes a perfectly absorbing boundary, with a distinct zero-optimum phase. Published-record searches and comparisons with accessible prior local claims did not uncover equivalent statements. A broader restart-optimization theorem could still implicitly imply some conclusions, and the exact forward solution makes these asymptotics derivable; this is an acknowledged literature-coverage risk, not a novelty certificate.

## Value — PASS

The theorem quantifies a physically motivated reaction-limited obstruction to arbitrarily fast transport: increasing inward drift without bound cannot reduce the optimized mean below \(eL/k\) for a finite-reactivity point target. It gives an explicit reset-rate design law, a diffusion-dependent first correction to the optimal time, and an all-parameter explanation for the drift-speed turnover observed numerically. These are not arbitrary parameter substitutions or isolated computations.

## Limits

The theorem assumes a single one-dimensional delta trap, identical reset location, constant inward drift, and fixed finite positive reactivity. Perfect absorption and outward drift are outside the asymptotic claim. At least one, not exactly one, turnover in drift speed is proved. Independent audit and experimental validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
