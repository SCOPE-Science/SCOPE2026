# Review

## Correctness

PASS. The critical-point equation, Hessian entries, and spectrum follow by direct differentiation. The exact factorization \(x^4-y_\star x+1=(x-a)^2(x^2+2ax+3a^2)\) yields the diagonal update. Its quadratic displacement term gives the reciprocal-increment limit; the cubic energy term rules out a local extremum.

## Originality

PASS, narrowly scoped. The inspected primary paper gives the corresponding threshold equality in its non-scalar classification and notes that the fully scalar case is handled separately. This review does not claim the threshold equality as new. The added claim is the explicit cubic coefficient and the exact one-sided inverse-linear asymptotic for simultaneous gradient descent on the invariant diagonal. Searches returned related deep-factorization and optimizer results, but no matching statement; a failed search is not proof of novelty.

## Value

PASS. The result quantifies a concrete failure mode for strict-saddle-based intuition: at the threshold, a degenerate saddle can hold diagonal gradient-descent iterates for a time proportional to the reciprocal initial displacement, with an exact asymptotic constant. This is a specific dynamical refinement, not a general claim about all nearby trajectories.

## Closest literature and remaining limits

The closest source is Chen, Jiang, and Wang (arXiv:2506.20344), which classifies non-scalar critical points and states that gradient methods may converge to non-strict saddles; it notes that the fully scalar case can be handled separately. The 2024 second-order landscape analysis of unregularized deep linear networks is related but uses a different objective. A broader survey of generic degenerate-gradient dynamics was not completed; the exact model-specific coefficient is proved directly here.

Self-review: passed. Independent audit: not yet performed.
