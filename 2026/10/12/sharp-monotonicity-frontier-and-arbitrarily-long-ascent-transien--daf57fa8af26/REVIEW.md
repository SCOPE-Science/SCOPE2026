# Review

## Correctness
PASS. Specializing the published AdaNorm recurrence to \(f(x)=\lambda x^2/2\) gives
\[
\gamma_k=\gamma_{k-1}+\lambda^2x_k^2,
\qquad
x_{k+1}=x_k\left(1-\eta\lambda/\sqrt{\gamma_k}\right).
\]
Since \(\gamma_k\ge\varsigma\), the condition \(\eta\lambda\le2\sqrt{\varsigma}\) is sufficient for every step to be objective-nonincreasing. If it fails, the exact first-step inequality yields the stated open ascent interval. For every fixed finite horizon, the accumulator differs from \(\varsigma\) by \(O(x_0^2)\), giving the local multiplier \(1-\eta\lambda/\sqrt{\varsigma}\) and therefore arbitrarily long ascent prefixes. The finite replay is not used as an infinite proof.

## Originality
PASS. The current AdaNorm source, the Ward--Wu--Bottou AdaGrad-Norm analysis, and the Liu--Nguyen--Ene--Nguyen vanilla AdaGradNorm analysis were inspected at their algorithm and convergence statements. None states the sharp monotonicity frontier, the exact first-step ascent basin, or the arbitrary finite ascent-prefix law. Targeted published-result searches returned stability and monotonicity frontiers for other methods but no statement implying this one. Residual risk remains that an older note contains the same elementary scalar calculation under different notation.

## Value
PASS. The result distinguishes convergence robustness from transient objective stability on the simplest possible strongly convex problem. Above one dimensionless threshold, the startup accumulator creates a genuine local repeller: not merely one bad step, but arbitrarily long deterministic ascent can occur for starts sufficiently near the minimizer. This gives a precise diagnostic for initialization or monotonicity safeguards when a user cares about transient behavior, while respecting the source's stronger eventual-convergence guarantees.

## Closest literature and limitations
The closest primary literature proves convergence of AdaGrad-Norm/AdaNorm for broad hyperparameter ranges and studies rates rather than objective-monotone trajectories. The result here is restricted to exact gradients on a scalar quadratic and does not assert divergence, stochastic instability, or a multidimensional classification.

Self-review: passed. Independent audit: not yet performed.
