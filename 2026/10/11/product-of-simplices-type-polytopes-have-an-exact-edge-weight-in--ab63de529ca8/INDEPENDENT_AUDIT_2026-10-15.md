# Independent mathematical audit

## correctness

PASS

The 2022 primary source Defines 1-Minkowski weights by vector balancing on each 2-face (Definition4.1) and normalizes ∑edges ω(E)=f1(P) (Definition4.3). Triangle and product square face equations propagate a unique weight λ_i to every edge moving in simplex factor i. Exactly E_i=C(d_i+1,2)∏_{j≠i}(d_j+1)=Vd_i/2 edges are of class i, giving ∑ d_i λ_i=D. Orthogonal disjoint classes make y_i=√E_i λ_i a genuine isometry into a coordinate simplex with normal a_i=√d_i and ∥a∥²=D. The projection of e_i to its tangent plane has norm √((D−d_i)/D); therefore facet clearance δ_i=y_i√(D/(D−d_i)). Equalizing all facet clearances uniquely gives r=D^(3/2)√(V/2)/S and λ_i*=D/S √((D−d_i)/d_i); this is a globally maximal inball because any radius r imposes all k coordinate inequalities and their weighted sum bounds r. Pure-factor vertices have pairwise disjoint supports, yielding the squared-distance formula; all sides equal for k≥3 iff all d_i equal; any k=2 case is a segment. The d-cube specialization checked. Independent cases d=(1,1),(1,2,3),(2,3,4),(3,3,3) yield identical facet clearances and exact normalization. General theorem is symbolic, not inferred from these cases.

## originality

PASS

Castillo–Doolittle–Goeckner–Ross–Ying 2022 full PDF Section4 defines precisely the same normalised edge-weight TP(P), Example4.7 says parallel edges share one weight for regular cubes, and Theorem5.10 proves simplicial combinatorial type for any product of simplices. These facts give the geometric input but no Euclidean metric normalization, facet-projected normal distances, incenter/inradius closed form, or equality rigidity across mixed factor dimensions is stated in inspected theorem/section. General weighted simplex incenter calculus is classical and makes rediscovery straightforward; nevertheless the claim fixes the natural source edge-coordinate metric and gives new dimension-vector closed forms rather than renaming a parameter. No stronger exact original metric theorem found; this is best-of-knowledge, with easy-derivation risk retained.

## value

PASS

The source parameterizes actual deformations by one length weight per edge; therefore intrinsic Euclidean distance to the boundary equals robustness margin before a class of edge deformations vanishes. The all-factor-dimension incenter/radius and regularity classification are natural exact geometric invariants of this deformation parameter space, not arbitrary algebraic slices. The answer is elementary only after a nontrivial verified edge-balancing and metric reduction; an exact all-dimensional formula is potentially useful for numerical deformation comparison. No claim of a new general simplex metric theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
