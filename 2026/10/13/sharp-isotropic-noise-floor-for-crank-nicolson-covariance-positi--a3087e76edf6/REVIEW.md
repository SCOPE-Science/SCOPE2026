# Self-review

## Correctness
PASS. The exact direct Crank–Nicolson component formulas reduce positive-semidefinite preservation on the trace-constrained two-dimensional covariance cone to a rank-one determinant test. Its quadratic in squared modal weight is
\[
F_s(t)=s^2+s[rt+\ell(1-t)]-E t(1-t),
\quad E>0.
\]
The displayed threshold makes this quadratic the nonnegative perfect square
\[
F_{s_*}(t)=E(t-t_*)^2,
\quad0<t_*<1.
\]
Strict monotonicity in the noise parameter proves the full if-and-only-if statement. Exact rational arithmetic independently replays the equality and failure examples, while the \(h^2\) asymptotic follows from a symbolic expansion.

## Originality
PASS, with residual risks. General non-preservation of matrix positivity by direct higher-order numerical Lyapunov integrators is prior mathematics, decisively covered by Dieci and Eirola's full 1994 paper. The full 2013 Gillis–Diehl study supplies an alternative PSD-preserving covariance update rather than a threshold for an unchanged direct trapezoidal update. The surviving statement is specifically the exact minimum isotropic diffusion required for the direct step on every covariance of fixed positive trace in two diagonal modes. Targeted alias, stronger-coverage, database and implication searches did not find the same threshold; the remaining risk is earlier Schur-multiplier or numerical covariance literature phrasing the same quantitative result differently.

## Value
PASS. A process-noise covariance is a natural parameter in a differential Lyapunov equation, and initial total variance supplies its meaningful normalization. The exact forcing floor distinguishes positivity lost because of matrix interaction from the simpler scalar damping restriction. It provides a sharp design-scale criterion, including the equality direction and the second-order small-step dependence, instead of merely exhibiting a negative determinant.

## Closest literature and limitations
Dieci–Eirola prove the covered generic high-order barrier; Gillis–Diehl propose a distinct positivity-preserving covariance discretization. The present claim is confined to one exact-arithmetic direct Crank–Nicolson step, two distinct diagonal stable modes, isotropic additive noise, positive fixed trace, and scalar-positive damping steps. The input trace need not be conserved across subsequent steps. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
