# Review

## Correctness

PASS. Direct substitution gives
\[
x_{t+1}=(1-s)x_t-se_t,
\qquad
e_{t+1}=(1-a)e_t+a\varepsilon_{t+1}.
\]
The deterministic matrix is triangular with eigenvalues \(1-s\) and \(1-a\), giving the exact stability range \(0<s<2\) for \(0<a\le1\). Solving the scalar error variance, cross covariance, and iterate variance equations yields the stated covariance. The SGD comparison reduces to an exact positive difference, and the derivative of the variance ratio is positive on the full stated domain.

Risk: the result is a stationary additive-noise benchmark and does not transfer unchanged to sample-dependent curvature or to the adaptive STORM schedule.

## Originality

PASS. The defining STORM paper gives the corrected-momentum update and its general estimator-error recurrence but does not state the additive-noise triangular factorization or stationary covariance. STORM+ restates the update and develops adaptive parameter choices without a quadratic covariance calculation. The earlier hybrid SARAH-SGD paper uses an additional independent fresh-gradient sample, so it has a different noise coupling and does not imply the same-sample cancellation proved here.

Focused semantic searches covered constant-parameter STORM, scalar quadratics, stationary variance, exact covariance, recursive momentum, and equivalent hybrid estimators. No inspected source or published-result search implied the complete covariance-and-stability statement.

## Value

PASS. The STORM literature explicitly identifies the need to trade off momentum weight against learning rate in order to reduce estimator error. This exact benchmark resolves that tradeoff structurally on the canonical additive-noise strongly convex model: corrected momentum preserves the SGD stepsize ceiling, makes estimator error an autonomous autoregression, and quantifies exactly how lower asymptotic noise is purchased by slower memory decay.

Same-model review: passed. Independent audit: not yet performed.
