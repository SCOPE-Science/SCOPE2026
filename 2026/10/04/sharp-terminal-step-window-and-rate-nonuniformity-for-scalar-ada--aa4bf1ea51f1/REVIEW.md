# Review

## Correctness

PASS. After scaling, the recurrence is
\[
r_{t+1}^2=r_t^2+z_t^2,
\qquad
z_{t+1}=(1-r_{t+1}^{-1})z_t.
\]
If the accumulator never reaches \(1\), it is automatically bounded. After it reaches \(1\), the decrease in \(z_t^2\) dominates the increase in \(r_t\), so the accumulator remains bounded. Its convergence forces \(z_t\to0\). A terminal value at or below \(1/2\) would make \(|z_t|\) nondecreasing, giving a contradiction. The exact tail ratio and the finite startup-count bound then follow directly. Explicit initialization families prove sharpness of both terminal-step endpoints.

Risk: the terminal accumulator itself has no closed-form expression for general initial data.

## Originality

PASS. Prior AdaGrad-Norm theory already covers robust convergence, bounded accumulation, eventual descent, and linear convergence; those facts are explicitly treated as prior coverage. The surviving claim is sharper and different: the closure of possible terminal normalized steps is exactly \([0,2]\), neither stability endpoint is attained by a nontrivial trajectory, both are approachable, the exact asymptotic factor is determined by the terminal accumulator, and therefore no hyperparameter-uniform contraction factor exists. The inspected full texts do not state or imply the explicit endpoint constructions or the startup-count bound.

Focused semantic searches over terminal accumulators, limiting effective steps, scalar quadratic phase behavior, and exact asymptotic factors returned no matching AdaGrad-Norm theorem.

## Value

PASS. AdaGrad-Norm is motivated by robustness to unknown smoothness and arbitrary hyperparameter initialization. The result distinguishes stability robustness from rate robustness: the algorithm automatically enters the right scalar stability interval, yet can settle arbitrarily close to either unstable boundary. This gives a precise benchmark for what “self-tuning” does and does not guarantee, and the finite startup bound quantifies the transient before monotone contraction.

Same-model review: passed. Independent audit: not yet performed.
