# Same-model review

## Correctness
PASS. Stationarity against arbitrary antiderivatives of \(x+y\) and \(y\) gives
\[
\mathbb E[x\mid x+y]=b,
\qquad
\mathbb E[x^2\mid y]=\frac by-a.
\]
These imply the support restriction \(0<y\le b/a\), the exact harmonic defect
\[
\operatorname{Var}(x)
=
\mathbb E[(\dot x+\dot y)^2]
=
b\left(\mathbb E[1/y]-1/y_*\right),
\]
and the conditional-variance defect
\[
\operatorname{Var}(x^2)-\operatorname{Var}(b/y-a)
=
\mathbb E[(\dot y/y)^2].
\]
In either zero-defect case, invariance of the support forces the unique equilibrium.

Risk: compact support is used to justify the test functions and to keep \(1/y\) bounded after the support exclusion.

## Originality
PASS. The complete foundational source and complete open 2021 mathematical study were compared at implication level. The exact-normalization 2022 phase-portrait article supplies the equations, nullclines, classification, and limit-cycle context, but its complete text was inaccessible and is retained as a residual risk. Direct semantic searches for conditional-moment, harmonic-mean, logarithmic-speed, and crossing formulations found no same-object implication.

Risk: the generator calculations are short enough that an equivalent observation could occur incidentally in unindexed literature.

## Value
PASS. The result turns the Selkov mass-balance and substrate nullcline into two equality-rigid stationary diagnostics valid for every compact recurrent statistical state. In a model with nontrivial limit-cycle regimes, it forces every non-equilibrium stationary state across \(x=b\) and below the equilibrium substrate level while quantifying both mass-balance speed and logarithmic substrate speed.

Same-model review: passed. Independent audit: not yet performed.
