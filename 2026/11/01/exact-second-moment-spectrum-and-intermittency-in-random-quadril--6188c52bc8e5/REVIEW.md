# Scientific review

## Correctness — PASS

The explicit affine-normal-form symbolic integration verifies the conditional mean, squared-area and opposite-corner-imbalance identities exactly for any strictly convex labeled quadrilateral. Taking expectations yields a fixed \(2\times2\) rational matrix whose characteristic polynomial, eigenvalues and spectral solution were checked. The variance inequality is strict at every positive step outside parallelograms, because the initial imbalance coefficient is proportional to the positive difference of the two eigenvalue powers. The independent proof of almost-sure normalized-area collapse uses a uniform variance gap and square-root contraction, not an extrapolation of numerical tests. Simulations corroborate but are not used to certify universal identities.

## Originality — PASS, historical priority provisional

The principal exact overlap is Nguyen and Volkov, *A universal result for consecutive random subdivision of polygons* (arXiv:1506.04942): they introduced the *same general iterated edgewise model* and analyzed flatness and random-matrix Lyapunov behavior. That model and their results are prior work, not new claims. The second lead is Maesumi, *Triangle Inscribed-Triangle Picking* (arXiv:1804.11007, originally 2018-04-30), which determines moments and a distribution for an independently sampled *inscribed triangle in one step*. The supplied two-state operator instead governs all iterations of a *quadrilateral*. A related published record on iterative random Minkowski symmetrization concerns a different operation. Statement-level and implication-level searches found no evaluated predecessor for this exact rational matrix, all-step variance rigidity or normalized-area contrast; absence from an index is not proof of uniqueness. Volkov's 2011 preprint on random geometric subdivisions uses a different midpoint-selection quadrilateral model; potentially unindexed or alternative formulations remain genuine historical-priority risks.

## Mathematical value — PASS

The natural invariant is the area of a random polygon formed by repeatedly choosing one independent uniform point on every side. Its second moment does not close on area alone; the additional intrinsic opposite-corner area imbalance makes the evolution exactly solvable. The closed spectrum gives every finite-step variance, an exact rigidity inequality for all initial convex quadrilaterals, and a sharp exponential discrepancy between mean-normalized typical area and its second moment. This is substantive stochastic geometry beyond elementary midpoint area, one-step expectations or code-only enumeration.

## Limits

The result assumes strictly convex four-sided polygons, independent uniform edge fractions, and mean-annealed moments. No full area distribution, higher-dimensional analogue or quenched Lyapunov exponent is established. An independent mathematical audit or conclusive bibliographic priority review has not occurred.

Self-review: passed. Independent audit: not yet performed.
