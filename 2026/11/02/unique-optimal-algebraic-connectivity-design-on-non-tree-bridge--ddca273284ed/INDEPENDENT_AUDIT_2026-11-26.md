# Independent mathematical audit

## correctness

PASS

Centering the test vector with class levels (3/2,1/2,−1/2,−3/2) gives squared norm D/N; every spoke and the bridge have squared difference one, and every optional edge has zero. The Rayleigh bound is therefore BN/D. Equality requires full budget on the tree edges and the centered vector to be an eigenvector. Its peripheral equations fix the spokes individually; the hub equation fixes the bridge, so equality is rigid without assuming equal input weights or graph symmetries. At that candidate let λ=BN/D. The leaf-transverse eigenvalues are 3qB/D and 3pB/D, with multiplicities p−2 and q−2. In the strict balanced range both exceed λ. In the remaining four-dimensional quotient, eliminating the two positive leaf pivots of L−λI gives a two-by-two hub matrix with off-diagonal −b and a null vector with opposite signs. Both diagonal entries are negative, so exactly one quotient direction is negative and its only zero direction is the designated eigenvector. At q=2p the left pivot is positive and the right pivot is zero; after eliminating the left pivot, the reduced matrix has a hub coupled nontrivially to two zero-diagonal uncoupled coordinates, and inertia is one positive, one negative, one zero. The remaining transverse eigenvalues are nonnegative after the shift. Interchanging p,q handles the other endpoint. Outside the range the larger peripheral class has a positive-dimensional transverse block below λ, so the sole equality candidate fails and compactness makes the optimum strictly smaller. For p=2,q=3,B=1, independent exact calculation gives det(xI−34L)=x(x−5)(x−6)(x−18)(x−39), verifying simplicity and multiplicities. Wan et al.'s actual hypothesis of a non-repeated optimum is satisfied, and its designable edge set includes the zero-weight triangle edge, so the example contradicts the uniqueness-implies-tree direction as stated.

## originality

PASS

The tree-only value and transition are covered by the double-broom solution and should not be credited as new. The distinct result concerns optional edges in the designable graph: it identifies their forced zero weights, gives uniqueness throughout the balanced range and supplies a concrete cyclic design with a simple optimal eigenvalue that contradicts the stated Wan converse. Nothing in the inspected tree theorem, centered unfolding framework or indexed priced tree specialization supplies that cyclic equality-and-uniqueness statement.

## value

PASS

The counterexample addresses a published structural criterion, not a small numerical improvement. Its exact spectrum and Rayleigh rigidity distinguish a cyclic allowed graph with a unique optimizer from its tree support. The full family shows when a simple explicit certificate works and rules out attainment outside the size range, for any subset of internal peripheral edges. This value does not rest on recomputing the double-star tree optimum already available from the double-broom formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
