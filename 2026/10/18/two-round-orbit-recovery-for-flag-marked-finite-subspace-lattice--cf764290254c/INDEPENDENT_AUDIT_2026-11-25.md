# Independent mathematical audit

## correctness

PASS

A proper r-space has fewer strict subspaces than an (r+1)-space, by embedding it and including it among the latter's proper subspaces. Thus round one identifies ranks from total lower counts. Each one-dimensional subspace has exactly one strict predecessor; its round-one colour also determines containment in U_i, including equality with a marked one-space via retention of its mark. The number of such atoms strictly below W lying inside U_i is (q^e_i-1)/(q-1) for dim W>=2, so the round-two colour recovers e_i. Rank zero and one already give the full signature in round one; trivial flag endpoints and the no-mark flag are covered. A C^2 formula counts strict predecessors that satisfy the atom test and the mark-or-strict-containment test, each rank one (local shadowing of the other variable is allowed), giving the rank-two claim. For completeness, lift each basis of (W∩U_i)/(W∩U_(i-1)) into W∩U_i; these lifts are independent modulo U_(i-1), so they can be included at the corresponding step of an adapted basis, proving transitivity for equal signatures by mapping matched bases. Marks and order determine meets and ranks intrinsically, and refinement is invariant, so larger lattice automorphism groups do not change the conclusion. At stage i, lifts of a projected a_i-space through W_(i-1) are graphs into U_(i-1)/W_(i-1), giving exactly q^(a_i sum_{j<i}(d_j-a_j)) maps and the claimed product of Gaussian coefficients; coordinate choices realize every signature. The sharpness pair consists of two unmarked two-spaces with exactly four proper subspaces and four proper superspaces each, incomparable to the marked two-space, but with intersection dimensions zero and one. Inspected both checkers and checks_output.txt; not rerun. Standard and selected extended tests are finite and the exact group-action examples are only binary, as listed in VERIFICATION.md. Neither cover-only refinement nor recognition of arbitrary structures is implied.

## originality

PASS

Credit the distinct recovery of the full flag signature and orbit partition in two rounds for the full strict-containment structure, with sharpness. The geometric orbits, Gaussian counts and C^2/equitable-partition framework are not separately original. The strongest indexed near match changes both the vertex universe and the adjacency relation and supplies no two-round implication for this structure.

## value

PASS

The result takes a natural filtration invariant of subspace geometry and shows that an inexpensive, highly restricted logic exactly recovers it on an unbounded family, uniformly in q and flag length. The concrete obstruction to one round isolates why atom membership must be propagated. The classical enumeration clarifies the stable colour classes without being credited as a separate discovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
