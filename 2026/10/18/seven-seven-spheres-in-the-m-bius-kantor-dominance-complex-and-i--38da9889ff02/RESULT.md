# Seven seven-spheres in the Möbius–Kantor dominance complex and its cyclic homology character

## Finding
Let \(M=GP(8,3)\) be the sixteen-vertex Möbius–Kantor graph. The dominance complex \(\mathcal D(M)\) consists of all vertex subsets \(S\) such that \(V(M)\setminus S\) is dominating (every vertex lies in or is adjacent to that complement). Then
\[
\mathcal D(M)\simeq\bigvee^{7}S^{7}.
\]
For the graph automorphism \(\rho:u_i\mapsto u_{i+1},\ v_i\mapsto v_{i+1}\), the character of \(\widetilde H_7(\mathcal D(M);\mathbb Q)\) on \(\rho^t\), \(t=0,\ldots,7\), is
\[
(7,-1,3,-1,7,-1,3,-1).
\]
Thus as a rational representation of the cyclic order-eight group it is \(\mathbb Q^2\oplus\varepsilon^{\oplus3}\oplus\mathbb Q(i)\), inflated from its order-four quotient. Here \(\varepsilon(\rho)=-1\) and \(\rho\) acts by multiplication by \(i\) on \(\mathbb Q(i)\).

## Assumptions and scope
All vertex indices below range over \(\mathbb Z/8\mathbb Z\). The vertices are \(u_i,v_i\), with undirected edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). The complex uses *closed-neighborhood domination*, not total domination, ordinary independence, matching, or graph-edge domination complexes. A face \(S\) is allowed exactly when no vertex's entire closed neighborhood is contained in \(S\). The integral homotopy classification refers to this single graph; the representation is over \(\mathbb Q\) for the specified cyclic subgroup, not the full automorphism group.

## Proof
**Face model.** Label \(u_0,\ldots,u_7,v_0,\ldots,v_7\) by integers \(0,\ldots,15\). Let \(N[w]\) be the closed neighborhood of a graph vertex. By the definition of domination, a subset \(S\) is a face of \(\mathcal D(M)\) if and only if \(N[w]\not\subseteq S\) for every \(w\). Because \(M\) is cubic, each forbidden mask has four vertices. Exhaustive evaluation of all \(2^{16}\) masks gives \(32,391\) faces including the empty face, with face counts by dimension \(0,\ldots,11\) equal to
\[
(16,120,560,1804,4176,6976,8208,6462,3136,832,96,4).
\]
The enumeration checks each mask against every one of the sixteen explicitly constructed closed neighborhoods and verifies downward closure.

**Complete discrete-Morse matching.** Start with all faces unmatched. For each vertex \(j=0,1,\ldots,15\) in that order, match every still-unmatched face \(\sigma\) not containing \(j\) with \(\sigma\cup\{j\}\), whenever both faces are unmatched. The algorithm yields \(16,192\) disjoint pairs, including \((\varnothing,\{u_0\})\), and seven remaining faces, each with eight vertices. Remove the empty-face pair, leaving \(16,191\) pairs on the nonempty face poset and critical cells consisting of a single vertex and seven seven-dimensional simplices. Their exact bit masks, with bit \(j\) representing vertex \(j\), are \(13110,21930,26214,39322,43606,52428,65280\).

For every cover relation \(\tau\subset\sigma\) between nonempty faces, orient the incidence downwards except that matched pairs are oriented upwards. The standalone verifier builds the entire graph of \(32,390\) nodes and \(218,672\) incidences and proves its acyclicity by consuming *every* node in a topological sort. This is an exhaustive finite certificate, not a sample. Forman's discrete-Morse theorem supplies a CW homotopy equivalent to \(\mathcal D(M)\) with exactly one zero-cell and seven seven-cells. Because there are no intermediate cells, every attaching map to the zero-skeleton is constant, giving precisely a wedge of seven seven-spheres. This proves the integral homotopy statement.

**Cyclic character.** For each \(\rho^t\), evaluate the signed trace on each oriented simplicial chain group. A face contributes zero unless its vertex set is fixed; a fixed face contributes the sign of the induced permutation of its ordered vertices. The reduced alternating trace is the alternating sum of these signed traces, subtracting the empty-face contribution. By the Lefschetz trace identity and the concentration of reduced homology in degree seven, it equals the negative of the trace on \(\widetilde H_7\). The exact signed enumeration for all eight powers gives \((7,-1,3,-1,7,-1,3,-1)\). The rational irreducible representations of \(C_4\) are the trivial line, the sign line, and the two-dimensional cyclotomic module \(\mathbb Q(i)\), with character values on the four powers respectively \((1,1,1,1)\), \((1,-1,1,-1)\), and \((2,0,-2,0)\). Their combination \(2(1,1,1,1)+3(1,-1,1,-1)+(2,0,-2,0)=(7,-1,3,-1)\) is the calculated periodic character. Therefore the asserted \(C_8\)-module decomposition follows.

## Verification
The package includes `evidence/verify_mk_morse.py` and `evidence/verify_mk_independent.py`; run both using standard-library Python 3. The first independently constructs the forbidden neighborhoods from the generalized-Petersen edge rules, counts all faces, produces the complete specified matching, checks all directed Hasse incidences and their acyclicity, and calculates every signed Lefschetz trace. The second constructs the cyclic \((8_3)\) incidence graph from shifts \(\{0,1,3\}\), checks an explicit isomorphism to the generalized-Petersen presentation, and enumerates dominating complements by direct graph adjacency. It reproduces the full face vector and reduced Euler characteristic \(-7\). Both programs were executed successfully and replayed from the exact embedded package files.

## Relationship to prior work
Matsushita and Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals* (arXiv:2312.02639, first public 2023-12-05), identify general Alexander-duality relationships for dominance complexes and study several graph families. The general equivalence \(\mathcal D(G)=\mathcal N(\overline G)^*\) does not supply the homotopy type or group character for this specific sixteen-vertex graph; the inspected classification sections do not contain this graph. Other available results for the Möbius–Kantor graph concern its ordinary independence complex, matching complex, cut complexes, or graph-metric Vietoris–Rips filtration, which are not the present forbidden-closed-neighborhood complex. An exact external record of this full homotopy and cyclic character was not identified in the checked sources.

## Limitations
The rational character determines the \(C_8\)-module over \(\mathbb Q\), but not an integral lattice classification or the full automorphism-group module. The kernel of the homology action need not act trivially on the underlying complex. The proof is an exhaustive certificate for this fixed graph, with no asserted generalization to all generalized Petersen graphs. Literature searches cannot eliminate the risk of an unindexed equivalent computation; no independent mathematical audit is claimed.

## References
Matsushita and Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639 (first public 2023-12-05), https://arxiv.org/abs/2312.02639.

Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
