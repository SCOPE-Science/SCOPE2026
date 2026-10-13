# Self-review

## Correctness — PASS

The unique multiplier solves the exact half-squared-norm plus half-ridge convex simplex problem. Its variational inequality at every vertex yields \(\langle g_i,v\rangle\ge\|v\|^2-\rho(\lambda_i-\|\lambda\|^2)\); the simplex maximum of the parenthesized quantity is exactly \((m-1)/(4m)\). An explicit two-dimensional family satisfies all multiplier KKT equations and attains equality for every \(m\ge2\). A separate pair of strongly convex quadratics gives exact objective ascent and exhibits another direction decreasing both objectives. The standalone exact-rational tests pass for the documented finite instances; the all-parameter conclusion comes from the proof. Boundaries at equality and zero multipliers are covered by the simplex proof, without hidden generic-position assumptions.

## Originality — PASS with stated residual risk

The primary 2026 paper's Sections 3.1 and 4, including the proof of Lemma 4.1, were checked at their operative equations. Its general constrained bound implies only the weaker \(\|v\|^2>\rho(m-1)/m\) directional-negativity criterion when specialized to the unconstrained formula; it does not state the optimal \(1/4\) replacement, all-\(m\) extremizing family, or the exact convex objective-increase example. Fernando et al. (2022) use the same simplex ridge operator under a rescaling of \(\rho\), but their materially inspected Sections 2.2, 3.1, 3.3 and relevant theoretical appendix concern stochastic gradient tracking and convergence, not this sharp componentwise margin. The inspected earlier unregularized multi-gradient and direction-oriented constructions do not imply the ridge margin directly. Searches also covered variants involving Tikhonov, regularized weights, common descent, simplex projections, and multiobjective gradient methods. Since first-order optimality and simplex maximization are standard, possible unindexed equivalent derivations remain a concrete originality risk; search failure alone is not a proof of novelty.

## Value — PASS

The sharp inequality is a computable pointwise safeguard in a currently used function-value-free multiobjective method. It strictly improves the primary paper's unconstrained directional sign certificate by a factor of four in the norm-squared regularization threshold; its exact constant is not an arbitrary numerical curiosity because every coefficient larger than this fails on a two-dimensional nonstationary family. The strongly convex explicit example demonstrates why the additional safety check can matter for individual objectives, without implying the whole algorithm fails or that componentwise monotonicity is needed by its theory. The scope is a useful local algorithmic certificate, not a standalone global convergence theorem.

## Closest literature and scientific limits

Li–Wang–Chen, arXiv:2609.02722v1, Section 3.1, Lemma 4.1 and proof; Fernando et al., arXiv:2210.12624, §3.1 and theoretical analysis; Liu–Vicente, arXiv:1907.04472; Xiao–Ban–Ji, arXiv:2305.18409. The sharp certificate applies to an exact unconstrained multiplier, not to projected or approximate updates. It does not claim independent validation or any stronger global convergence property.

Self-review: passed. Independent audit: not yet performed.
