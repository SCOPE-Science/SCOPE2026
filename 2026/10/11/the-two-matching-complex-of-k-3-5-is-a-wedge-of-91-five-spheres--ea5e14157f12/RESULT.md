# The two-matching complex of \(K_{3,5}\) is a wedge of 91 five-spheres

## Finding
Let \(G=K_{3,5}\), with bipartition \(R=\{0,1,2\}\) and \(C=\{0,1,2,3,4\}\). Let \(M_2(G)\) be the abstract simplicial complex whose vertices are the fifteen edges of \(G\) and whose simplices are those sets of edges in which every vertex of \(G\) has degree at most two. There is an integral homotopy equivalence
\[
M_2(K_{3,5})\simeq\bigvee^{91}S^5.
\]
In fact, there is an explicit acyclic discrete-Morse matching with precisely one critical zero-simplex and ninety-one critical five-simplices. This is a statement about the complete nonequivariant homotopy type, not merely rational homology.

## Assumptions and scope
All graphs are finite and simple. The complex is the ordinary two-matching complex, *not* the ordinary (degree-one) chessboard complex, the perfect-matching complex, or a multiplicity complex admitting two distinct rooks in the same square. Every edge is present at most once. The result is only asserted for \(K_{3,5}\) with row and column degree capacities exactly two.

Index the edge \((i,j)\) by \(5i+j\), with \(0\le i<3\) and \(0\le j<5\). For a bitmask \(b\in\{1,\ldots,2^{15}-1\}\), define the associated nonempty face by the selected bit positions. It is admissible precisely when all its three row counts and five column counts are at most two. This convention completely specifies the complex.

## Proof
**Finite face census.** Directly test every nonzero fifteen-bit mask against the eight degree inequalities. The resulting \(3,480\) nonempty faces have dimension-wise counts
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(15,105,420,990,1260,690),
\]
and no face has dimension greater than five. The exact finite enumeration, not an extrapolation, is reproduced by `verify_morse.py`.

**Matching construction.** Initially all nonempty faces are unmatched. For each edge index \(k=0,1,\dots,14\), in increasing order, pair every currently unmatched face \(b\) *not* containing \(k\) with \(b\cup\{k\}\) if both faces are still unmatched. Remove both faces from further matching stages. Each pair is a genuine codimension-one face/coface pair; the code implements the rule literally. The matching has \(1,694\) disjoint pairs. Exactly ninety-two faces remain: one of dimension zero and ninety-one of dimension five.

**Acyclicity certificate.** Form the full Hasse directed graph on the \(3,480\) nonempty faces. For each codimension-one face/coface incidence, direct its arrow from coface to face unless the pair is in the matching, in which case reverse the arrow. There are exactly \(15,870\) such incidences. Kahn's exact topological sort removes all \(3,480\) vertices, proving that this entire directed graph has no directed cycle. In particular the discrete-Morse matching is acyclic. No sample of paths, random search, or timeout is used. The finite topological-sort certificate is independently and deterministically reconstructed by `verify_morse.py`.

**Homotopy consequence.** Forman's discrete-Morse theorem gives a CW complex homotopy equivalent to \(M_2(G)\) with one cell in dimension zero, ninety-one cells in dimension five, and no other cells. Its four-skeleton is a single point, so all five-cell attaching maps are null. It is therefore a wedge of exactly ninety-one five-spheres, as claimed. This is an integral homotopy equivalence: no coefficient field is needed.

## Verification
Run `python3 verify_morse.py` and `python3 verify_boundary.py` in a directory containing the two unmodified files. Both require only the Python standard library. The first checks every face, all matching pairs, the complete directed Hasse graph, all unmatched critical cells and exact acyclicity. The second uses a different column-major vertex order, generates simplices from combinations rather than the first program's mask enumeration, and independently obtains the mod-two simplicial boundary ranks
\[
\operatorname{rank}(\partial_1),\ldots,\operatorname{rank}(\partial_5)=(14,91,329,661,599).
\]
These yield reduced mod-two Betti number \(91\) in degree five and zero elsewhere. The independent homology computation is a consistency check; the actual integral homotopy proof is the acyclic matching.

## Relationship to prior work
This is the bounded-degree bipartite graph complex \(\Delta_{(2,2,2),(2,2,2,2,2)}\) in the terminology of Wachs's survey (Section 7, particularly pp. 24–30). Reiner and Roberts' rational equivariant homology formula applies to **all** such complexes, so neither the rational Betti number nor the rational group-representation decomposition is claimed as new. Wachs's survey discusses general homotopy theorems for bounded-degree *complete graph* complexes and explicitly poses the problem of finding bipartite homotopy analogues (Problem 7.10). Those cited general results do not, by themselves, supply this exact integral homotopy equivalence.

Singh's theorem about higher matching complexes of complete bipartite graphs determines \(M_{n-1}(K_{n,n})\) for square matrices; the present rectangular matrix with two-per-vertex capacity is outside that theorem. Vega's study of two-matching complexes concerns different graph families. A published computation of \(M_2(K_{3,4})\simeq S^5\) concerns a smaller board and neither identifies nor dominates the present 91-sphere decomposition.

## Limitations
This is a fully reproducible finite certificate, not an infinite-family classification. Nothing is asserted about arbitrary row or column capacities, other board sizes, equivariant integral or rational representations, or special simple-homotopy properties beyond those that follow from the given acyclic matching. Bibliographic searching cannot exclude an equivalent unindexed or unpublished calculation; the intended novelty is the explicitly verified *integral homotopy type*, not the already-known rational homology dimensions.

## References
1. M. L. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, Algebra Universalis **49** (2003), 345–385, doi:10.1007/s00012-003-1825-1. Author's public full-text manuscript: https://www.math.miami.edu/~wachs/papers/tmc.pdf.
2. V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, published author's PDF: https://www-users.cse.umn.edu/~rober005/chessmatch.pdf, especially Theorem 3.3.
3. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, particularly Theorem 1.2 and Section 4.
4. J. Vega, *2-matching complexes*, arXiv:1909.10406.
5. R. Forman, *Morse theory for cell complexes*, Adv. Math. **134** (1998), 90–145. The original discrete-Morse cell theorem is used in its standard finite-simplicial-complex form.
