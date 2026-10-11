# Same-model review

## Correctness
PASS. On compact support strictly inside the positive half-line, \(Y=\log(X/K)\) and \(Y^2\) are bounded. Invariance applied first to \(Y\) gives \(\mathbb E[X]=K\). Applied to \(Y^2\), the exact cocycle \(Y\circ F-Y=r(1-X/K)\) gives \(2K\operatorname{Cov}(\log X,X)=r\operatorname{Var}(X)\). Positive variance permits division; zero variance is exactly the equilibrium atom. No finite experiment or asymptotic approximation is used.

Risk: the logarithmic proof does not cover invariant laws whose support meets \(0\), stochastic variants, or noncompact laws without separately justified log-square integrability.

## Originality
PASS. The periodic-orbit first-moment calibration is prior: Sacker's inspected 2007 full text derives the telescoping sum behind equality of average population and average Ricker parameter. The accepted statement instead uses the invariant second logarithmic moment to recover the intrinsic growth parameter from a single stationary marginal, and it applies to every compact positive invariant probability measure, not only periodic cycles. Targeted searches covered invariant measures, stationary moments, covariance identities, parameter identifiability, and periodic-orbit aliases. No inspected same-object source implies the covariance-to-variance formula.

Risk: the foundational 1954 article was available only through bibliographic metadata and abstract, and an unindexed occurrence of the elementary second-moment identity remains possible.

## Value
PASS. Parameter recovery is a central use of Ricker-type population models, while nonlinear dynamics can make transition-based likelihoods difficult. The theorem isolates an exact structural dichotomy: any non-equilibrium stationary marginal determines both \(K\) and \(r\), whereas the equilibrium marginal provably loses \(r\). This is a natural invariant-statistics fact with a clear inferential interpretation rather than an arbitrary moment calculation.

Same-model review: passed. Independent audit: not yet performed.
