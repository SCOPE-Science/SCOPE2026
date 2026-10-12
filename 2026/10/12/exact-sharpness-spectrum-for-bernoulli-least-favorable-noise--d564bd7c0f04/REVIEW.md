# Review of Exact sharpness spectrum for Bernoulli least-favorable noise

## Correctness
**PASS.** The covariance inequality is a direct Cauchy--Schwarz consequence with the correct equality conditions. Equality forces affine conditional regression with slope \(a=\sigma^2/(\sigma^2+v)\). Since a Bernoulli conditional mean is bounded, the centered sum and noise are bounded, so their characteristic functions are entire. At a simple complex zero of the centered Bernoulli characteristic function, the regression differential identity forces an integer zero multiplicity \((1-a)/a=v/\sigma^2\); the same identity then identifies the centered noise characteristic function as the corresponding convolution power. Integer-ratio attainment follows from exchangeability. Huang's existence theorem justifies strictness of the infimum away from integer ratios.

## Originality
**PASS.** The motivating paper proves the integer-multiple construction and optimality, and its Bernoulli section studies low-budget optimizers, but the inspected full text does not state that integer multiples are the only budgets at which the universal covariance bound is sharp or that equality forces a shifted binomial law. Exact and semantic published-finding corpus searches for least-favorable Bernoulli noise, affine regression, covariance sharpness, characteristic-function zeros, and shifted-binomial equality returned no covering result. Classical discrete-regression characterization papers were inspected because they are the main plausible equivalence risk; the accessible 1983 full text requires a prescribed conditional-distribution family in addition to regression, and the 1985 abstract describes the same two-input characterization framework rather than this variance-budget statement.

## Value
**PASS.** The result identifies an exact arithmetic obstruction inside a published extremal-noise problem. It explains why the source's simple convolution solution works at integer variance multiples yet cannot extend by affine regression to intermediate budgets, and it classifies all equality noises at the sharp points. This is a structural boundary result rather than a finite numerical refinement.

The closest literature supplies the integer sharp points, existence of minimizers, and broader discrete-regression characterization machinery. It does not determine the noninteger least-favorable value; that remains a limitation, as does residual risk from older poorly indexed characterization literature.

Self-review: passed. Independent audit: not yet performed.
