# Independent mathematical audit

## correctness

PASS

For connected rank-two M, there are s>=3 nonempty parallel classes; the base polytope in affine H(sum x_i=2) equals x_i>=0 and x(C_j)<=1. Its coordinates can be realized from hypersimplex class totals by conditional distributions within selected class pairs, including zero-mass classes. Projected normal lengths in H are A=sqrt((n-1)/n), B_j=sqrt(h_j(n-h_j)/n). Ball inclusion iff all c_i>=rA and class totals c(C_j)<=1-rB_j; r feasible iff intervals [h_j r A,1-r B_j] each nonempty and their lower/upper sums straddle 2. These are exactly three upper barriers: 2/(nA), (s-2)/sum(B), min_j 1/(h_j A+B_j). Allocating totals and uniform class coordinates constructs an attaining center. The same inequalities characterize all Chebyshev centers. Independent ConvexHull facet computation and LP for 42 distinct nondecreasing parallel-class partitions with n=3..8 matched formula to <=2.3e-16; examples with all 3 competing active regimes were exhibited. Finite checks support but do not prove all n.

## originality

PASS

Best-of-knowledge original exact Euclidean metric classification of all connected loopless rank-two matroid base polytopes and all optimal centers. The same objects are complete multipartite edge polytopes; full-text primary 2022 and 2025 treatments compute Ehrhart and face data, not Euclidean inradius. A related published same-family result computes Minkowski asymmetry (affine reflection containment, no Euclidean normal lengths) and does not imply this formula. The 2000 Ohsugi–Hibi same-object historical paper is a named residual full-text risk, not proof of coverage or a reason for automatic scientific failure.

## value

PASS

A natural geometric roundness invariant for all connected rank-two matroid base polytopes/complete multipartite edge polytopes. Exact class-size-dependent expression and all incenter vectors give quantitative metric information genuinely separate from known Ehrhart, face and Minkowski-asymmetry data. Each of the three obstructions can be uniquely active in natural examples (uniform U_{2,5}: coordinate; all classes (2,2,2): aggregate class cap; (1,1,3): single-class compatibility). This can be used directly for geometric scaling/conditioning comparisons of rank-two base polytopes; it is a complete class, not an arbitrary finite slice. Its proof is elementary interval LP once facets are known; value is a modest explicit structural classification, not a broad theorem or solution for higher-rank matroids.

The dated certificate retains the supplied scientific assessment, sources and limitations.
