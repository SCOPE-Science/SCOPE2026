# Independent mathematical audit

## correctness

PASS

The final claim is R(K_3 Cartesian K_n)=4 for each integer n>=4. A clique projection of any 3-uniform word must repeat one permutation three times; cyclic rotation and column relabeling normalize row A to (A0A1A2A3)^3. Every A+B projection has a B permutation and exactly 24*binom(23,11)=32,449,872 interleavings; no case is omitted. The two source-Git-blob-matched C++ programs independently enumerate the pair structures (354 admissible projections), all 354^2=125,316 ordered (A+B,A+C) pairs, and all gapwise interleavings preserving B/C row orders. Exact direct-merge implementation counted 158,483,130 complete B+C arrangements with zero satisfying all sixteen B_i,C_j adjacency predicates; bitmask/automaton implementation independently found 238,188 arrangements satisfying the four required matching alternations, zero satisfying all twelve nonedge constraints. Both actual compiled programs exited 0 with claimed counts. Upper bound uses Broere--Zantema product theorem on the explicit 2-uniform word for K_n; the exact assigned verify_upper.py Git blob replayed 2<=n<=10 correctly, finite widths only corroborating the universal known theorem. The published R(3,3)=3 subgraph excludes k<=2 on R(3,4); an induced 3x4 rook graph propagates k>=4 to all n>=4. Boundary n=3 expressly excluded. The entire assigned twelve-file Git object tree was independently reconstructed and matched.

## originality

PASS

Best-of-knowledge priority survives precisely for the rigorously exhaustive lower obstruction R(K_3 square K_4)>=4 and consequent exact all-width three-row family. Kitaev--Pyatkin (Acta Informatica 63 (2026), Article 33, Section 2.3) states an unsuccessful computer search but expressly says it is not proof and lists this bound open in Section 3. Broere--Zantema 2019 Theorem 1 supplies the four-uniform Cartesian-product upper construction but no lower bound follows from an existence theorem. The present enumerators exhaust the normalized finite set with exact counts, not an inferred failure from a timeout. Three independent Resultary semantic queries and targeted original-paper/alternative-formulation web searches did not identify a published logically covering certificate. This is best of knowledge, not a declaration of absolute priority.

## value

PASS

A genuinely motivated exact infinite-family graph invariant is determined: the motivating 2026 primary work explicitly leaves the 3-by-4 minimum as an open lower-bound question, after obtaining the 3-by-3 boundary and 2-by-n family. The first missing 3x4 obstruction is sufficient by induced-subgraph monotonicity to settle every 3-by-n width n>=4, and the existing product construction supplies the matching upper bound. A fully checked but finite 12-vertex obstruction is valuable because it resolves the complete natural 3-row family, not because it merely recomputes a table or increases a sample size. The evidence is computation-assisted, with exact complete search rather than a heuristic timeout. No claim is made for four-or-more-row classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
