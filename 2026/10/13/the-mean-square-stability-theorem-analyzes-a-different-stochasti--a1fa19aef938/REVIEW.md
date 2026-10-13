# Self-review

## Correctness
PASS. Equation (2) has diffusion
\[
\Sigma(X)=\operatorname{diag}(\alpha_1X_1,\alpha_2X_2,\alpha_3X_3),
\]
so at a strictly positive deterministic drift equilibrium \(E^*\) the diffusion is nonzero. Exact translation therefore produces a nonzero additive Brownian term at zero displacement, while Equation (13) deliberately uses centered diffusion that vanishes there. Itô's formula gives a strictly positive initial derivative of the mean-square displacement for Equation (2). The Section 3 stability theorem consequently applies to a different centered-noise SDE.

## Originality
PASS. Exact DOI/title searches of the current and latest prior ledgers found no duplicate, and source-specific published-finding corpus searches returned no equivalent published correction. A close stochastic predator–prey predecessor explicitly introduces deviation-from-equilibrium noise as a separate model; it supports the modeling distinction but does not imply the source-specific conclusion.

## Value
PASS. The distinction changes the interpretation of a central theorem about noise tolerance. In the ecological SDE actually formulated in Section 2, the positive deterministic equilibrium is not a stochastic equilibrium solution; the appropriate long-time object may instead be a random or stationary distribution. The finding therefore separates the theorem's valid scope from the stochastic model to which the paper otherwise returns.

## Closest literature and limitations
Shao and Kong, DOI 10.3390/math10183378, is a close methodological comparison because it explicitly uses equilibrium-centered random disturbances in a predator–prey setting. The result here does not claim that centered noise is invalid, does not quantify long-time fluctuations for Equation (2), and does not reassess persistence or stationary-distribution theorems.

Self-review: passed. Independent audit: not yet performed.
