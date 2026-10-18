# Shortest octahedral carriers and integral orbit obstructions in the Dürer matching complex

## Finding
Let \(G=GP(6,2)\) be the Dürer graph, with twelve vertices, eighteen edges, and its ordinary matching complex \(K=\mathcal M(G)\). There is an integral homotopy equivalence
\[
K\simeq\bigvee^{22}S^3.
\]
The minimum number of vertices of an **induced** subcomplex supporting nonzero third reduced homology is eight. Exactly \(93\) induced eight-vertex subcomplexes have nonzero third homology, and every one is an octahedral three-sphere \((S^0)^{*4}\). Every fundamental class maps to a primitive nonzero element of \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{22}\), and the \(93\) classes together generate this group over \(\mathbb Z\). An explicit selection of \(22\) of the classes is an integral basis.

The full graph automorphism group \(D_6\) has exactly eleven orbits on the \(93\) carriers. Ordered by the lexicographically smallest carrier in each orbit, their sizes and individual integral homology ranks are respectively
\[
(6,12,6,3,12,12,12,12,6,6,6),\qquad
(5,8,6,3,12,12,9,8,6,6,6).
\]
No union of at most two orbits spans the rational third homology. Of the \(165\) three-orbit unions, exactly \(26\) span rationally; \(23\) of those generate integrally, and **exactly three** have index four, with quotient \((\mathbb Z/2)\oplus(\mathbb Z/2)\). Using zero-based orbit indices, those exceptional triples are \((2,4,10)\), \((2,5,7)\), and \((2,5,10)\). Thus minimum-size geometric spheres can span all rational homology yet miss two independent integral parity directions.

## Assumptions and scope
All graphs are finite, simple and undirected; all homology is ordinary reduced simplicial homology with integral coefficients unless indicated. Explicitly, \(V(G)=\{0,1,\dots,11\}\), with the following eighteen edges in this order: six exterior cycle edges \(\{i,i+1\bmod6\}\), six spokes \(\{i,i+6\}\), and six interior edges \(\{i+6,6+(i+2\bmod6)\}\), for \(0\le i<6\). Repeated unordered edges do not occur. Each edge of \(G\) is a vertex of \(K\); faces are matchings. The induced subcomplex \(K[W]\) is on an edge-set \(W\subseteq E(G)\) (vertices of \(K\)), not on a subset of the original graph's vertices. A geometric carrier means an induced octahedral three-sphere together with either choice of fundamental-cycle orientation. No claim is made about other graphs or all higher support strata.

A canonical orientation is fixed as follows. Label the matching-complex vertices by indices \(0,\dots,17\) in the preceding edge order. A carrier is a lexicographically sorted tuple of four pairs \((a,b)\), with \(a<b\), representing four mutually vertex-disjoint two-edge paths in \(G\). Orient each corresponding zero-sphere by \([a]-[b]\), take their simplicial join in pair order, and sort simplex vertices to the standard increasing orientation. The verifier implements precisely this convention. Carrier indices are zero-based positions in the lexicographically sorted list of all \(93\) tuples.

## Proof
**1. Sharp support bound.** The matching complex is flag because pairwise disjoint edges form a matching. For any flag complex with a nonzero reduced degree-\(d\) class of minimal induced support, the number of support vertices is at least \(2d+2\). Indeed, for any vertex \(v\) in its minimal support, the class cannot come from deleting \(v\); the long exact sequence of the pair with the vertex deletion forces nonzero \(\widetilde H_{d-1}(\operatorname{lk}(v))\). By induction, its flag link has at least \(2d\) vertices. Further, \(v\) has a nonneighbor (otherwise the induced complex is a cone); hence the support has at least \(2d+2\) vertices. At equality each vertex has exactly one nonneighbor. The complement of the one-skeleton is a perfect matching, forcing the complex to be \((S^0)^{*(d+1)}\). Apply this with \(d=3\). The induction begins with a nonzero reduced degree-zero class requiring two vertices; the pair relative-homology identification is the reduced homology of the link shifted by one.

**2. Exhaustive classification of equality.** To obtain \((S^0)^{*4}\) as an induced subcomplex of a matching complex, the eight graph-edge vertices must split into four conflicting pairs, with every edge from one pair disjoint from every edge of each other pair. In a simple graph each conflicting pair consists of two distinct edges meeting at a vertex, hence is a path of length two. Distinct pairs then have disjoint sets of three original vertices. Conversely such four disjoint paths give exactly the desired induced octahedron. Since \(G\) has twelve vertices, any four such paths cover its entire vertex set. There are \(36\) individual two-edge paths (twelve degree-three centers, three choices each), and an exhaustive four-path compatibility test gives exactly \(93\) distinct sorted carriers. In each carrier the join of the four signed zero-spheres is a signed three-cycle with sixteen tetrahedra; its signed simplicial boundary vanishes by direct cancellation.

**3. Complete integral homotopy and chain-coordinate model.** Direct face enumeration gives the face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(18,117,334,402,156,10)
\]
and \(1037\) nonempty simplices. The deterministic sequential-edge-toggle matching on the nonempty face poset has exactly \(507\) matched face pairs and only \(23\) critical faces: one zero-cell and \(22\) three-cells. The explicit verifier constructs the entire directed Hasse graph (\(3684\) incidences) with every matched incidence reversed and checks acyclicity by a topological sort consuming all \(1037\) faces. Forman's integral discrete Morse theorem therefore gives the asserted homotopy wedge without an unverified boundary map: the Morse CW complex has one point and precisely \(22\) attached three-cells, with no other cells.

For a lattice comparison, the verifier computes exact signed boundaries in the ordinary simplicial basis and performs elementary integral unit cancellations in the matching order. Every cancellation of a three-/four-cell matched pair has pivot \(\pm1\); this yields a free integral coordinate basis indexed by the \(22\) critical three-cells. The resulting coordinate matrix \(T\) has \(22\) rows and \(93\) columns, one per oriented octahedral carrier. Each column has coordinate gcd one, proving primitiveness. Its Hermite normal form is the \(22\)-identity matrix, proving integral generation. More concretely, columns with zero-based indices

`[78,43,14,13,35,26,30,66,20,51,71,17,64,77,85,87,16,72,88,53,39,59]`

have exact signed determinant \(+1\) in that order and form an integral basis. These are machine indexing data, not algebraic variables.

**4. Full symmetry and orbit obstructions.** The six inner vertices are the only graph vertices lying in a triangle; graph automorphisms therefore preserve the two inner triangles and the exterior induced six-cycle. Each exterior-cycle dihedral automorphism lifts, yielding all twelve automorphisms. Acting on the complete carrier list gives the eleven orbit sizes displayed above. For each orbit or union of orbits, form the corresponding column submatrix of \(T\) and compute its Hermite normal form. Its column count is its rational rank, and, at full row rank, the absolute determinant is its sublattice index in \(\mathbb Z^{22}\). Every singleton orbit is saturated in its rational span. Exhaustively checking all \(55\) two-orbit and \(165\) three-orbit unions gives no full-rank pairs and precisely \(26\) full-rank triples: twenty-three determinant-one lattices and three determinant-four lattices. Computing the Smith normal form of each determinant-four case gives nonunit invariant factors \((2,2)\), proving that the quotient is \((\mathbb Z/2)\oplus(\mathbb Z/2)\), not cyclic of order four.

## Verification
Run `python -m pip install -r requirements.txt` and then `python verify_durer.py` using Python 3.10 or later. The script constructs the graph, all faces, the full acyclic face-poset matching, the complete octahedral-carrier list, all signed cycles, the exact integral reduction, the basis determinant, the twelve graph automorphisms, all eleven orbit lattices and all \(165\) triple unions from scratch. It uses arbitrary-precision integers and exact Hermite/Smith normal forms. The expected final marker is `VERIFY_OK_DURER_INTEGRAL_SHORTEST_OCTAHEDRAL_CARRIERS`. No external data file or previously generated computational output is required.

## Relationship to prior work
Shareshian and Wachs [1] establish matching-complex homology and torsion results for **complete and complete-bipartite graphs**; their results do not give a Dürer-specific support or lattice computation. Engström [2] studies connectivity of independence complexes of claw-free graphs, hence gives context for line-graph independence complexes, but does not determine this integral orbit-lattice structure. Bayer, Goeckner and Jelić Milutinović [3] classify manifold matching complexes; the present nonpure complex lies outside their manifold hypothesis. Bayer, Jelić Milutinović and Vega [4] prove a wedge theorem for **outerplanar** graphs, whereas the Dürer graph is not outerplanar. Zhao [5] computes a matching-forcing polynomial for generalized Petersen graphs, a different invariant not implying the present theorem. Other published computations on the octahedral, truncated-tetrahedral, and dodecahedral graphs concern distinct matching complexes. No accessible primary statement inspected implies the exact \(93\)-carrier classification or the index-four orbit obstruction.

## Limitations
The result is for this one explicitly defined finite graph. The verifier proves finite exhaustive statements, not a general theorem for other generalized Petersen graphs. The exact numerical orbit indexing depends on the stipulated deterministic edge and carrier order; the multiset of orbit sizes and the existence and structure of the index-four obstructions do not. The evidence of originality is a documented comparison of accessible sources and search results, not a proof of absence from all literature; an unknown equivalent calculation remains a bibliographic risk. Independent scientific audit has not been performed.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054 (first public preprint 2004-09-03), https://arxiv.org/abs/math/0409054.
2. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420 (2005), https://arxiv.org/abs/math/0512420.
3. M. Bayer, B. Goeckner and M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328 (2019), https://arxiv.org/abs/1906.03328.
4. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (2024), https://arxiv.org/abs/2411.04601.
5. S. Zhao, *Matching forcing polynomial of generalized Petersen graphs*, arXiv:2110.03978 (2021), https://arxiv.org/abs/2110.03978.
