# Independent mathematical audit

## correctness

PASS

The actual pinned RESULT.md specifies Q_d in R^(2^d) by two-sided |chain sum|<=1 for every nonempty Boolean inclusion chain, in the standard coordinate Euclidean norm. Every full chain has d+1 coordinates, so any radius-r ball imposes |sum_C c|+r sqrt(d+1)<=1; the origin attains r=1/sqrt(d+1) against every shorter chain. At this optimum all full-chain sums vanish. Adjacent transpositions of maximal chains exchange one rank-k subset; the corresponding equalities and connectedness of the Johnson graph force centers constant on each rank, with total rank sum zero. A chain omitting rank k then imposes |t_k|<=1-sqrt(d/(d+1)); this includes bottom and top k. Conversely an s-element chain samples s distinct ranks, and its rank sum is bounded by a_d min(s,h-s). The convex F(z)=1-sqrt(1-z/h) has F(0)=0 and increasing slopes, hence F(m)>=m F(1) for integer m>=1; thus a_d min(s,h-s) <=1-sqrt(s/h), satisfying ALL signed-chain ball inequalities. Finally the central cube hyperplane section has dimension h-1=d. Every vertex has >=h-1 saturated coordinate bounds. For h even the final coordinate is forced to a sign (balanced h/2 and h/2); for h odd the free coordinate is zero with balanced remaining signs. This gives the claimed two exact vertex counts for every d>=1. Independently computed Gaussian rational rank, entire cube-section vertex enumeration, and all rank-subset slacks for d=1..4, matching ranks (1,2,5,12) and vertices (2,6,6,30); finite checks are corroborative only.

## originality

PASS

Best-of-knowledge PASS for the combined complete Boolean signed-chain incenter locus, its dimension d and parity-dependent vertex counts. The numeric inradius 1/sqrt(d+1) is not novel by itself: the 2026 published enriched-chain result gives that radius for all finite posets, and the signed model contains its enriched subset while the common longest-chain halfspace gives the matching upper bound. Crucially, the enriched chain body has ALL sign-pattern chain facets and only the origin as a center on a pure Boolean poset, whereas the assigned two-sided chain-sum body has a d-dimensional nonunique center set. The 2023 primary signed-chain sources define the actual object and study reflexivity/integer/Ehrhart data but do not give its full Euclidean center locus. The published ordinary chain and signed order results use different halfspaces and cannot be applied by a Euclidean isometry or implication. Targeted full-theorem, dual-name, general coverage, and numerical-table searches found no older equivalent full classification. Search absence is not novelty proof; the conclusion is limited to inspected sources and mathematical implications.

## value

PASS

The Boolean lattice B_d is canonical and parameter-free; the signed-chain polytope was previously defined and studied for lattice/Ehrhart phenomena. A natural metric question asks for ALL centers of maximum Euclidean inscribed balls, not merely a single radius. The complete answer has unexpected affine dimension d inside ambient dimension 2^d, a clean rank-layer cube-section model, and an exact even/odd vertex census. Its distinction from the enriched chain body is structurally sharp: the enriched model has a unique center for Boolean B_d at the same radius. These full-center facts were not implied by the inspected previous facet and radius results and could be reused to study contacts and symmetry. This is a motivated all-dimensional classification, not an arbitrary small-n calculation. The individual max-chain bound and elementary cube-section vertex count are textbook ingredients and alone are not a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
