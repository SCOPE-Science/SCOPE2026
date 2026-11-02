# Independent mathematical audit

## correctness

PASS

For every m>=1 and the specified standard orthonormal source-coordinate realization, the affine hull has dimension 2m and consists of coordinate-sum 1. Kühne–Monin Theorem 2.1 gives exactly m leaf facets L_i=x_i+y_i>=0 and 2^m central subset facets F_S=x_0+sum_{i in S}x_i+sum_{j not in S}y_j>=0. Their intrinsic projected normal norms are beta_m=sqrt(2(2m-1)/(2m+1)) and alpha_m=sqrt(m(m+1)/(2m+1)). For a contained radius-rho ball, sum_i L_i>=m rho beta_m forces x_0<=1-m rho beta_m; average_S F_S=(1+x_0)/2>=rho alpha_m forces x_0>=2 rho alpha_m-1. Hence rho<=2/(2alpha_m+m beta_m). The proposed c_m=(1-m r_m beta_m; each x_i=y_i=r_m beta_m/2) satisfies all m+2^m inequalities at equality, attaining that radius. Equality in the two averaged/slack inequalities makes every facet tight, then F_{S+{i}}-F_S=x_i-y_i=0 and the affine condition prove unique center. The proof is symbolic for arbitrary integer m>=1; m=1 yields sqrt(2/3) and m=2 sqrt(5/24). Independent finite facet/normal/LP checks m=1..7 corroborate but do not substitute for the exact proof.

## originality

PASS

Qualified best-of-knowledge originality. The primary face theorem and the later dual theorem supply the complete facet-vector data, but no inspected source states or mathematically directly implies the sharp all-m Euclidean inball formula together with all-facet tangency and uniqueness without doing the new intrinsic-normal and aggregate-slack optimization. The distinct same-object Resultary Euclidean circumradius is an outer-ball statement and does not imply this inner-ball result. Resultary search also returns the assessed claim itself, which is not independent evidence of priority.

## value

PASS

The exact Euclidean inball is a natural realization-dependent convex-geometric invariant of a classical graph-indexed polytope. The star family is the simplest nontrivial all-dimensional tree family, but has exponentially many genuine facets (m+2^m). The result explains a strong global metric property (every facet tangent to the same optimal sphere) and rigid uniqueness for every dimension, complementing known combinatorial face/dual, triangulation, and vertex-controlled outer-sphere theory. Its all-facet contact certificate and exact formula could be used in geometric analysis of the family; no paper-sized extension to arbitrary graphs is required. A brief proof using symmetry/averaging does not make this a mere textbook substitution; its object, metric and structural invariant are genuinely motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
