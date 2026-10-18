# Scientific review: sharp periodic-Poisson factorial-count variance

## Correctness — PASS
The two-window factorial generating function yields an exact covariance, and the unit-period block statistics form a stationary one-dependent sequence with all moments, giving the central limit theorem. The period-integrated covariance is evaluated by Parseval. Constant rate is the unique equality case in the lower bound; positive arc masses exclude attainment of the upper bound and a smooth approximate identity proves sharpness. The accompanying program passed 64 independently implemented deterministic assertions; numerical tests are supporting diagnostics only.

## Originality — PASS, with residual literature risk
The closest motivating study is Stewart and Sahani, *Sampling on Discrete Spaces with Temporal Point Processes* (arXiv:2603.09089; first public March 10, 2026), which constructs the periodic Poisson special case and leaves oscillatory-efficiency effects as a question. The classical general variance formula and normal-approximation framework for Poisson U-statistics are due to Reitzner and Schulte (arXiv:1104.1039), not new here. The examined texts do not state the resulting exact seasonal Fourier penalty, its sharp upper/lower design bounds and unique optimizer. Targeted literature and mathematical-record searches returned no matching explicit coverage; older implicit coverage remains possible, and partial abstract-only comparisons are not full-text clearances.

## Mathematical value — PASS
A normalized intensity oscillation leaves every sampled Poisson marginal unchanged, but worsens physical-time uncertainty in its second factorial moment by a computable harmonic penalty, while the corresponding linear observable is unaffected. This is a natural estimator-efficiency design question for temporal point-process samplers, with a sharp continuous class minimizer and unattained supremum. The effect is structurally linked to pair overlaps and supplies an exact motivation for uniform driving intensity when estimating a quadratic observable.

## Scientific limitations and integrity
Only continuous positive period-one rates, a univariate Poisson target, physical-time unit-window averages and the explicitly stated observables are covered. Neither all target distributions nor other sampling schemes are classified. The exact variance is proved analytically, not inferred from finite quadrature. Independent priority and correctness audit have not been performed.

Self-review: passed. Independent audit: not yet performed.
