# Scientific review

## Correctness (PASS)

For \(d\ge2\), \(1\le k<d\), all real calibration factors and every positive normalized step, the centered quadratic difference equals the exact directional derivative. The Gaussian fourth-moment covariance identity yields the stated exact block-energy matrix, verified by independent rational moment replays. Its nonnegative Perron eigenvalue yields the sharp asymptotic factor, and direct minimization establishes the unique optimal step and the strict stability interval. A separate exact one-step calculation and exact triangular power at perfect calibration establish the transient claims. Strict monotonicity of the Perron root and trace/determinant scaling yield the claimed improvement interval and critical dimension-dependent calibration window. Boundaries at \(\beta=0,1,2\) and \(k=1\), \(r=1\) are included. No finite simulation is treated as an infinite proof.

## Originality (PASS, best-knowledge with residual priority risk)

The 2026 directional-hint article was inspected in its publicly accessible full HTML, including the estimator, oracle choice, adaptive rates and pertinent appendix. It does not state the exact centered-quadratic two-block energy recurrence, best-step Perron constant, equality of worst one-step rates, triangular transient formula, or sharp \(d^{-1/2}\) calibration transition. The standard Gaussian identity and the source control-variate construction are expressly credited. Comparisons with the published prior-guided search and Gaussian two-point optimization literature show materially different estimators or qualitative bounds. Indexed prior mathematical claims with similar general themes concern uncalibrated probes, Haar subspace sampling, or other optimizers. A full historical-priority guarantee is not claimed; an unknown specialized mean-square filtering identity could dominate.

## Value (PASS)

The result resolves a precise practical-analytic tension: projected gradient hints can be asymptotically effective even though they fail to improve worst-case first-step error and can create arbitrarily large transient amplification. It supplies an exact stable step-size rule and a necessary-and-sufficient calibration scale for a nearly full-dimensional hint, useful in analyzing surrogate reliability and deciding when an asymptotic bound is an unsafe finite-horizon proxy. It is a tractable benchmark, not a general nonconvex theorem or a promise of query-efficiency gains.

## Closest literature and limitations

Primary: Ryabchenko–Qian–Mou (2026), arXiv:2609.08277v1, establishes the control-variate framework, but not this exact centered quadratic theorem. Cheng–Wu–Zhu (2021) uses prior-guided biased random search. Guided Evolutionary Strategies (2019) uses anisotropic Gaussian sampling. A 2026 two-point Gaussian paper addresses high-probability last-iterate bounds without the projected control variate. The derivation relies on exact quadratic directional derivatives and a fixed projector. It does not cover the source's one-sided smoothing error, finite-precision effects, noisy or changing hints, or total query cost. More exhaustive classical adaptive-filtering bibliography remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
