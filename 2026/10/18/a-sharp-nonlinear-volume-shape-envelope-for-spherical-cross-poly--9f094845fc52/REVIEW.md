# Independent mathematical audit

## correctness

PASS

For a full-dimensional convex combinatorial d-crosspolytope, the nonadjacent opposite labeling indexes the 2^d oriented facets. Multilinearity of the signed cone volume sum gives Vol(P)=2^d/d! |det A| exactly even when P is not centrally symmetric; this does not depend on choosing apex inside. Unit sphere vertices yield Delta²=4(d-max_U tr(U^T A))=4(d-||A||_*), with A invertible since determinant equals nonzero volume, and |a_i|<=1. AM-GM over singular values gives product s_j <=(sum s_j/d)^d and equality iff A=sU, 0<s<=1. To prove local sharpness, for s close1 use p_{i,+/-}=sqrt(1-s²)e_{i+1}±s e_i; vertex normals perturb strictly valid regular-crosspolytope facets, preserving combinatorics, A=sI and Delta²=4d(1-s), attaining equality for every sufficiently small nonzero discrepancy. Pair midpoints differ, ensuring a genuinely non-antipodal equality family. Expansion gives optimal leading deficit V0 Delta²/4 with V0=2^d/d!. Independent ConvexHull volume calculations d=2,3,4,5 at s=.995 agreed with determinants/envelope within numerical precision. Finite tests verify only instances; general proof is determinant/polar decomposition/AM-GM plus combinatorial continuity.

## originality

PASS

Horváth–Lángi show regular cross-polytopes maximize inscribed spherical volume, but the new statement is an exact globally valid nonlinear upper envelope in a labeled Procrustes vertex distance with equality for noncentral-symmetric perturbations. The determinant identity and nuclear-norm AM-GM are standard ingredients and are not claimed novel separately.

## value

PASS

Stability of the regular spherical crosspolytope maximizer under a concrete labeled vertex perturbation is a natural convex-geometric question. The exact nonlinear envelope identifies how far volume must fall with the orthogonal vertex discrepancy, yields the sharp quadratic deficit at the maximizer, and unexpectedly admits noncentrally symmetric equality families. Though the AM-GM step is elementary, the exact combinatorial signed-volume identity and geometric attainment convert it into a reusable sharp stability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
