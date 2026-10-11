# Same-model review — sharp joint-noise stability frontier

## Correctness — PASS

At the positive equilibrium \((u^2,u(1-u^2))\), direct differentiation gives the displayed drift matrix. Independent Itô noises produce the exact three-moment closure \(K\); the characteristic polynomial is checked symbolically. Necessity follows from the stochastic Lyapunov equation with forcing \(-I\): after normalizing its positive-definite solution, the two diagonal inequalities force \(0<\eta<\delta/(2d)\) and \(\eta>Qb/(2bd-Qz)\). Sufficiency follows by choosing \(\eta\) strictly between these bounds and constructing a positive-definite quadratic Lyapunov matrix with strictly negative generator. All quantifiers and equality boundaries are treated. The checker verifies the exact identities and 1260 supplementary numerical cases; simulations are not used as proof of the continuum claim.

## Originality — PASS

The Tan–Wang–Feng primary paper (DOI 10.3390/math10214087) gives the mean-square stability matrix and single-noise graphs, without the complete two-noise iff threshold. Buckwar–Kelly (DOI 10.1137/120893859) establish the general Kronecker-moment methodology and investigate an analogous Holling-II predator–prey system, but do not state this explicit square-root frontier. Senosiain–Tocino (DOI 10.1007/s11075-022-01478-6) provide exact formulas for different, chiefly upper-triangular, drift/noise structures. The present claim is specifically the exact model-parametric elimination and strict variance comparison, **not** novelty of the general mean-square spectral test. Residual risks are an unindexed equivalent algebraic specialization and abstract-only access to an earlier 2020 stochastic nonnormality paper. These do not constitute a known decisive coverage claim from material inspected.

## Value — PASS

The exact frontier addresses the source's mathematically motivated question of relative susceptibility to independent population perturbations. It resolves every joint-noise intensity pair in the model, proves both boundaries sharp, and identifies a strict predator-first threshold for every deterministically stable coexistence equilibrium. This is a structural analytic classification of a naturally coupled stability region rather than a gratuitous case study or a single numerically sampled improvement.

## Limitations

Conclusions apply to the centered linear Itô equation with independent Brownian drivers. They make no claim about nonlinear stochastic global stability, positivity, extinction, almost-sure Lyapunov exponents, transient amplification, or independent outside validation. The general stochastic covariance method predates this result.

Same-model review: passed. Independent audit: not yet performed.
