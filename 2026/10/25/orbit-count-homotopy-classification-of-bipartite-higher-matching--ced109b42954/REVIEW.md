# Independent mathematical audit

## correctness

PASS

The vertex H-orbits are products of H_L row orbits and H_R column orbits. A geometric fixed point has constant barycentric coordinates on each vertex orbit, and positive orbits may be used only when their union is a simplex; this gives a simplex-wise affine PL homeomorphism to the quotient forbidden-full-row/column complex N_{s,t}. If either orbit count=1 no nonempty face exists. For s,t>=2, sequential greedy cell toggles first s-1 rows. The first-row survival partition has class A containing all first-row cells except the first, and class B with a saturated lower first column, which is eliminated by subsequent toggles. Induction leaves exactly the cell set {(i,j):i<s,2<=j<=t}, a single unmatched simplex of (s-1)(t-1) cells, with the augmented empty simplex matched. Acyclicity by standard element matching and the basepoint Morse conclusion yield S^{(s-1)(t-1)-1}, including S^0. This is homotopy, not PL-homeomorphism to the standard sphere. Independent check: Independent face-set generation and staged toggles for each of the 9 rectangles 2<=s,t<=4 left exactly the prescribed unique unmatched simplex. The quotient-orbit PL identification follows directly from coordinates for arbitrary product subgroups, not only finite checks; the repository supplies 34 additional finite orbit-action corroborations.

## originality

PASS

Singh 2020 establishes X_n~S^{(n-1)^2-1} only for the equal-sided square and the discrete Morse construction. The present fixed-space classification is over all row- and column-permutation product subgroups and all rectangular quotient sizes; neither square homotopy nor rational representation theory determines all these geometric fixed spaces. General rectangular forbidden-line complexes could be known under another dual/complex-of-arrangements name; qualified priority risk.

## value

PASS

Geometric fixed-point spaces, not merely homology characters, are canonical equivariant invariants. The sharp empty/sphere transition, explicit dimension, and independence from orbit sizes classify a natural infinite family and all its product-subgroup fixed-point homotopy types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
