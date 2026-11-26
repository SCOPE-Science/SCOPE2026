# Independent mathematical audit

## correctness

PASS

The positive elements of S sum to at least 2m. A normalized ideal is obtained by adjoining gaps; adding a small gap forces precisely the high gaps it hits by adding the middle block. For a proper enlargement I of S, the colon omits 0, contains the entire tail, and omits a middle-block position precisely if a selected small gap forbids it. If U is the union of these forbidden-position sets, the bidual has both high gaps and the small gaps with F_m(g) contained in U. No negative x survives since x+(2m−1−x) is a gap and the second summand is in the colon tail. Directly intersecting {2m−2−g,2m−1−g} with the middle block gives endpoint singletons and exactly the adjacent pairs of the length-(m−2) path. Thus the fixed support sets are unions of endpoint singletons and adjacent pairs, equivalently 010-free; the union reconstructs the support from the ideal and preserves inclusion both ways. S is fixed separately; translating commutes with bidual, so normalization counts classes. As an independent count, track the longest suffix that is a proper prefix of 010 (empty, 0, or 01). The generating equations for continuation counts E,B,C are E=1+z(E+B), B=1+z(B+C), C=1+zE. Eliminating B,C yields E=(1+z²)/(1−2z+z²−z³), proving all stated coefficients and growth (the transfer matrix is primitive with Perron root alpha). All-ideal count: the empty small-gap set allows four choices of high gaps, each of the two endpoint singletons allows two, and every other set forces both. The meet deletes isolated interior points from an intersection, and the join is union. At L=2 this is a Boolean diamond above a new bottom; at L≥3 the claimed five sets are a pentagon because the only potentially nonempty cross-intersection is {2}, which is inadmissible. This verifies the sharp nonmodularity boundary, including m=4.

## originality

PASS

Best-of-knowledge pass for the two-gap ideal-lattice result, particularly the full lattice operations and nonmodularity threshold. The closest same-day catalogue finding uses the same window mechanism and would give the same support and counts if extended to block length two, but it explicitly excludes length two and calls it previously treated without identifying a source for that remark. No independently identified earlier r=2 statement was found in the compared sources. That relationship and priority uncertainty must be retained; neither the string-avoidance sequence alone nor the general bidual framework is a new claim.

## value

PASS

This explicitly identifies a natural reflexive sublattice inside the relative ideals of a near-ordinary semigroup. The path description gives both the exponential difference between total and reflexive ideals and a minimal-size structural obstruction to modularity that persists uniformly. The exact transition at the first two multiplicities, and the order-sensitive witness, convey information not provided by a finite-instance bidual algorithm or a binary-word count alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
