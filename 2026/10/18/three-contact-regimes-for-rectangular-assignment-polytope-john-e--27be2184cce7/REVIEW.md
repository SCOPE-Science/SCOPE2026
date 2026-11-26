# Independent mathematical audit

## correctness

PASS

The fixed-value k bipartite flow formulation gives the stated halfspaces by integrality (unit capacities on source-to-row and column-to-sink arcs, and integral total flow). The uniform center is strict, so the intrinsic dimension is mn−1. For k>1 each prescribed facet can be saturated leaving all the others strict: for an entry omit that entry and distribute k uniformly over the rest; for a row fill it uniformly to sum 1 and distribute the remaining k−1 uniformly over the other rows, and similarly for a column. Uniqueness and independent row/column permutations fix the center and make the shape scalar on the three inequivalent real irreducible summands (standard⊗trivial, trivial⊗standard and standard⊗standard). Projecting the entry normal gives squared norms A,B,D; projecting a row normal gives n(m−1)/m entirely in the row summand, and its slack is (m−k)/m. The column calculation is the transpose. The resulting budget and separate caps are necessary and sufficient. The trial shape (min(q,U),min(q,V),q) uses the full budget for the unique positive root q. Its objective gradient, with weights equal to mn times the budget coefficients, equals mn/q times the budget gradient plus nonnegative corrections on capped coordinates only. The supporting inequality for the concave log objective thus proves global optimality, with uniqueness by strict concavity. Since (x−k)²/(x−1) increases for x>k≥1, U<V. Solving the budget consecutively gives the stated q0, q1 and two-cap expression and the boundary equalities activate the corresponding faces. At k=1 the coordinate-only radius is strictly below both cap levels. Independently substituting the three examples gives q=1/140<U=1/108 at (4,9,3), U=1/60<q=1/40<V=1/20 at (4,5,3), and V=1/98<q=31/2352 at (7,8,6). The eigenvalue product gives the intrinsic volume. The same support computation gives the displayed contact points.

## originality

PASS

The square fixed-k result uses the same symmetry idea but has coincident row and column caps. The rectangular all-cardinality results differ in domain and give a row-product criterion in full ambient dimension. The fixed-cardinality enclosing formulas reverse the optimization. The published matching result supplies the polytope description, not the inscribed ellipsoid. The unequal two-cap threshold and exact intermediate row-only contact phase are supported as distinct in the bounded comparisons.

## value

PASS

The maximum inscribed Euclidean volume and spectrum are natural geometric data for a canonical matching relaxation. A single scalar formula gives them over the full unsaturated rectangular domain and reveals that the first active row cap need not make the column cap active. The three strict examples show a real geometric distinction rather than redundant constraints or a cosmetic extension from square notation. It supplies exact radii and contact types without vertex enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
