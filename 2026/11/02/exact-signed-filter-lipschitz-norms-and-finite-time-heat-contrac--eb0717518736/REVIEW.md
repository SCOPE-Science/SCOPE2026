# Independent mathematical audit

## correctness

PASS

For the repaired signed geometry, row cancellation gives y=−x+sum(V)−sum(U) on a fixed edge. At n≥6 the derangement matches disjoint pairs and bounds |x+y| by 2(n−4); four feasible corners have values in an interval of length one. This also corrects the frozen proof's informal 'full sum of absolute coefficients' wording: sign potentials of magnitude 1/2 take half that sum, exactly the claimed norm. At n=5 symmetrization preserves the pair, and distances imply |z|≤2, |z−x|≤2 for z=q−p, hence |y|+|x|≤4. The three prescribed tests and negatives satisfy the metric conditions on all six support points and extend by the explicit McShane formula. Convex combinations fill the respective regions and their support functions give all signs and zero coefficients. The common-neighbor identity is valid on diagonal, disjoint and intersecting entries and J vanishes on the quotient. An independently constructed edge-potential LP anchoring one vertex agreed exactly numerically on all 49 integer coefficient pairs −3…3 for each of n=5,6; replay with graph disjointness, two inequalities per edge, and fixed edge objective. Independent heat LP checks at t=0,0.001,0.05,0.3,1.4 matched the original formula to 6e−16; its increasing log-rate and t=0 Petersen degeneracy also follow by differentiating the exact two-exponential formula. Those finite checks are not an all-n proof. The frozen verification and both checkers were inspected, not executed.

## originality

PASS

The remaining exact joint feasible regions support arbitrary real signed filters. Positive-walk idleness results cover the removed heat finding and the positive support directions, not the claimed full geometry. The opposite-sign Petersen corners in particular require additional feasible potentials; no matching signed-region statement was found in the inspected sources. The all-signed shape is retained as one invariant, not each sign sector as a separate novelty claim.

## value

PASS

The exact joint region is the finite-dimensional invariant controlling every affine adjacency filter and hence every polynomial filter on this quotient. The opposite-sign directions are needed for shifted adjacency and other non-Markov filters, for which idleness comparisons cannot give the amplification. The Petersen hexagon versus the stable parallelogram for n≥6 gives a genuine change in the optimization, including a flat branch for small positive shifts on Petersen. The positive heat calculations alone would be routine applications of prior theorems and were removed as a contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
