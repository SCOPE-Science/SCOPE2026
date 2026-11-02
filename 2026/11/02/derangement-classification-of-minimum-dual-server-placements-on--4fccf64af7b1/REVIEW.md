# Self-review

## Correctness — PASS
Every zero cell must see both colours in its row or column. The proof independently shows that any placement of weight at most \(2n-2\) must have both colours missing from a row and a column; otherwise the forced opposite-colour rectangle yields at least \(2n-1\) selected cells. For nonempty four missing-line sets, their two forced rectangular blocks and the residual row/column cover bound give a sharp lower bound \(2n-2+|u-v|\). Equality forces two complementary bar orientations and a pair of disjoint perfect matchings on the residual square. The counting distinguishes the boundary where orientations coincide, and correctly includes \(u=0\) and excludes \(u=1\). Exhaustive, directly simulated verification of all support-minimal functions and the preceding support layer was performed for \(n=2,3,4,5\). No computational extrapolation is used in the proof.

## Originality — PASS, provisional historical priority
The already-known scalar value \(2n-2\) is not a new claim. The distinguishing assertion is the complete optimizer characterization and closed derangement formula for each \(n\). The 2026 dual-server graph-operations and rainbow-domination papers establish definitions and broader results but do not yield the exact enumerator. A complete-multipartite two-rainbow function census concerns a different graph, which is not generally the square Cartesian rook product. Checks of equivalent single-colour-at-vertex, two-server, line-graph edge-domination and row-column service formulations did not identify a stronger covering optimizer classification. No absence of a search hit is treated as a proof of priority. Residual risk: unindexed or inaccessible literature could contain equivalent enumeration.

## Mathematical value — PASS
A known minimum cost does not reveal whether the optimum is rigid or highly degenerate. The full classification exhibits two transverse bar phases, a shared boundary, a forbidden single-cell interior, and a nontrivial derangement-controlled family of labelled optimal placements. For instance the optimizer counts jump from \(320\) on the \(4\times4\) board to \(8450\) on the \(5\times5\) board. This answers a natural exact-optimum-structure problem for an infinite canonical graph-product family and is not a re-expression of the scalar bound.

## Boundaries and limitations
The scope is the square rook product and single-colour labels only, with named red and blue. The proof does not address general rectangular counts, other rainbow domination variants or nonminimal assignments. Finite verification corroborates but does not independently certify the infinite statement.

Self-review: passed. Independent audit: not yet performed.
