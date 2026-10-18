# Scientific review: A commutator law for small-curvature spectral-norm quadratic descent

## Correctness — PASS

The linear matrix-sign point is uniquely optimal at zero curvature for an invertible square gradient. At scaled orthogonal candidates the spectral-ball normal cone gives a necessary and sufficient positive-semidefinite certificate. The skew-part equation has an invertible derivative on the tangent space, allowing an analytic optimal orthogonal branch and its explicit Sylvester derivative. The positivity of the normal-cone certificate persists, so the branch is a global convex optimum, not merely a stationary restricted rotation. A controlled Taylor expansion gives the stated squared-parameter coefficient and its strictness condition; the same exact normal certificate yields the commuting persistence threshold. Matrix computations and the reproducible checker corroborate the proof but do not replace it.

## Originality — PASS with residual literature risk

The source that introduces quadratic spectral descent (arXiv:2609.07597) already provides the matrix objective, general curvature-sensitive changes and a certificate for optimality; none of those background facts is claimed as new. The claim here instead concerns the explicit analytic commutator response, sharp squared-parameter value coefficient, and the exact persistence condition for the first-order baseline. Published-results searches under equivalent polar-derivative, trust-region, Kronecker and matrix-sign descriptions found no result with the combined mathematical assertion. The complete open primary text of Higham (1986), particularly Sections 2.2 and 2.4, was examined and does not give the quadratic-model value coefficient. Bhatia–Mukherjea (1994) concerns polar derivatives of prescribed matrices rather than the present self-consistent objective.

The most important residual risk is that the full manuscript or appendices of arXiv:2609.07597 were unavailable despite bounded lawful access attempts. The available primary abstract and independent summaries were examined, but they cannot establish whole-document noncoverage. The 1994 related primary full text was also inaccessible. These are specified coverage risks, not a claim that a failed search proves novelty.

## Value — PASS

The exact commutator coefficient is a natural quantitative diagnostic for whether two-sided curvature makes solving the constrained quadratic worthwhile, not a cosmetic perturbation or arbitrary finite enumeration. It distinguishes a continuous-rotation regime from a finite exact-persistence region and determines the actual optimal surrogate gain to leading order in every finite dimension. It does not assert an improvement in nonquadratic training loss or empirical runtime.

## Limits and independent status

All dimensions are finite, gradients are real square and invertible, curvature factors are strictly positive-definite, and the expansion concerns small nonnegative curvature. The exact baseline persistence test applies at every positive parameter but does not characterize the fully curved optimizer beyond the perturbative regime. Numerical experiments are finite checks, not independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.
