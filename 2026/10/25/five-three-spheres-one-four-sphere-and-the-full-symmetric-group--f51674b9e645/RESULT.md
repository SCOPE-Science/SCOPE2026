# Five three-spheres, one four-sphere, and the full symmetric-group action in the five-point triangle-free graph complex

## Finding
Let \(\mathcal T_5\) be the simplicial complex whose ten vertices are the edges of the complete graph on \(\{1,2,3,4,5\}\), and whose faces are edge subsets that contain no triangle. There is an integral homotopy equivalence
\[
\mathcal T_5\simeq\bigvee^{5} S^{3}\vee S^{4}.
\]
Under the natural permutation action of \(\mathfrak S_5\), with \(P_5\) the five-dimensional rational permutation module on the graph vertices,
\[
\widetilde H_3(\mathcal T_5;\mathbb Q)\cong \operatorname{sgn}\otimes P_5
\cong S^{(1,1,1,1,1)}\oplus S^{(2,1,1,1)},
\quad
\widetilde H_4(\mathcal T_5;\mathbb Q)\cong \mathbf 1.
\]
All other reduced integral homology groups vanish; \(\widetilde H_3\cong\mathbb Z^5\) and \(\widetilde H_4\cong\mathbb Z\). Thus one rational fourth-homology dimension, and no third-homology dimension, is fixed by the full symmetry group.

## Assumptions and scope
All graphs are finite simple graphs on the *fixed labeled* vertex set \(\{1,2,3,4,5\}\). A face is the set of edges of a graph with no three mutually adjacent graph vertices. The group permutes graph vertex labels and hence acts simplicially on the complex. No result for an arbitrary number of graph vertices is asserted. The primary mathematical content is topological and equivariant, not the elementary characterization of triangle-free graphs.

An equivalent presentation identifies each of the ten graph edges with a vertex of the Petersen graph \(P=\operatorname{KG}(5,2)\): two such vertices are adjacent when their corresponding graph edges are disjoint. The three Petersen neighbors of an edge \(\{a,b\}\) are exactly the three edges of the triangle on the complementary three labels. Hence \(\mathcal T_5\) is the simplicial complex of complements of total dominating sets of \(P\), or equivalently the complex avoiding every entire open neighborhood in \(P\). This is **not** the usual closed-neighborhood dominance complex.

## Proof
**Finite face and matching certificate.** Encode the ten possible edges by ten bit positions in lexicographic order and each face by its bitmask. Explicitly prohibit the ten edge triples representing the triangles on three of the five graph vertices. Exhaustive enumeration of all \(2^{10}=1024\) masks gives 388 faces including the empty face, with nonempty face vector \((10,45,110,140,72,10)\). There are 27 facets: five in simplicial dimension three, twelve in dimension four, and ten in dimension five.

Apply the following deterministic sequential toggle matching to the entire face poset. Initially all faces are unmatched. For bit positions in increasing order, pair every remaining face lacking the bit with its remaining face obtained by adjoining that bit, then discard both; scan remaining faces in increasing bitmask order. The certificate leaves exactly six unmatched masks: five four-element masks \(114,402,538,676,840\) and one five-element mask \(484\). It matches the empty face with the singleton mask \(1\). Deleting this last formal pair yields an ordinary discrete-Morse matching with exactly one critical vertex, five critical three-cells and one critical four-cell, and 190 other matched nonempty face pairs.

Reverse every matched codimension-one incidence and orient every other incidence downward. Enumerating all 1,400 incidences between nonempty faces, a complete topological sort visits all 387 nodes. Thus the matching is acyclic, not merely numerically plausible. The resulting Morse CW model consists of one zero-cell, five three-cells and one four-cell.

**Integral attaching degree.** Orient all simplices by the increasing edge-bit order. For the critical four-cell at mask \(484\), compute its signed Morse boundary using recursive cancellation of matched face–coface pairs, where deletion of bit \(i\) has coefficient \((-1)^{\#\{j<i\;:\;j\text{ present}\}}\). The exact integer coefficient vector against the five critical three-cells is \((0,0,0,0,0)\). The three-skeleton of this Morse CW complex is \(\bigvee^5 S^3\). Its four-cell attaching map lies in \(\pi_3(\bigvee^5S^3)\cong H_3(\bigvee^5S^3;\mathbb Z)\cong\mathbb Z^5\) by Hurewicz, so a zero integral degree vector means it is nullhomotopic. This proves the claimed integral homotopy type. An independent simplicial calculation gives the mod-two reduced Betti vector \((0,0,0,5,1,0)\).

**Symmetry character.** Every permutation \(g\in\mathfrak S_5\) acts on the oriented simplicial chains by a signed permutation. Enumerating the fixed faces with their induced orientation signs gives the reduced Lefschetz number
\[
L(g)=1-\operatorname{sgn}(g)\,|\operatorname{Fix}_{\{1,\ldots,5\}}(g)|.
\]
It is checked individually for all 120 permutations, with class values \((-4,4,0,-1,1,2,1)\) on cycle types \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\). By the integral homotopy computation, \(L=\chi_{H_4}-\chi_{H_3}\). The one-dimensional rational \(H_4\) character is either trivial or sign, since \(\mathfrak S_5\) has precisely these two one-dimensional characters. The sign choice would make the trivial-character multiplicity in \(H_3\) equal to \(-1\), impossible. Hence \(H_4\) is trivial and \(\chi_{H_3}=\operatorname{sgn}\cdot\#\operatorname{Fix}\), the sign twist of the five-point permutation character. The stated Specht splitting follows from \(P_5\cong\mathbf1\oplus S^{(4,1)}\).

## Verification
Run `python3 verify.py` with Python 3.8 or newer; the script uses only the standard library. Successful execution ends with `VERIFY_OK` and reproduces `verification_output.txt`. It includes three equivalent face predicates, all 1,024 graph edge masks, the complete incidence-acyclicity check, the exact signed Morse boundary vector, independent modular simplicial ranks, and the full 120-element symmetry character. The finite computation is exhaustive for the precisely stated five-point complex; it is not evidence for any infinite family.

## Relationship to prior work
The five-point case is the *first* graph order at which triangle-free edge sets differ from bipartite edge sets: in order five, every triangle-free nonbipartite graph is exactly a five-cycle. There are twelve labeled five-cycles. Thus the triangle-free complex is the two-colorable-graph complex with exactly twelve additional four-simplices. The known two-colorable graph-complex results of Linusson and Shareshian provide the natural comparison, but do not themselves establish this mixed-dimensional triangle-free homotopy type or its \(\mathfrak S_5\) character.

Jonsson's *Simplicial Complexes of Graphs*, Chapter 26, explicitly discusses triangle-free graph complexes. The chapter's complete content was not accessible for inspection; an earlier equivalent calculation in its pages is a material originality risk, not something ruled out by a title or preview. Related cut and neighborhood complexes on the Petersen or triangular graphs have different allowed-face definitions. In particular, the ordinary four-cut complex of the triangular graph is not the present triangle-forbidden edge-set complex; their homotopy degrees and symmetry characters also differ. The distinction is made at the level of simplices, not merely by comparing names.

## Limitations
The result is confined to graphs on five *labeled* vertices and supplies no general theorem for triangle-free complexes on larger graph orders. The full text of Jonsson's directly relevant chapter was not available, so complete exclusion of earlier equivalent published or unindexed classifications cannot be asserted. Its integral symmetry action is classified only rationally; no separate description of a canonical integral module lattice is claimed. The supplied verification is independently reproducible from finite combinatorics but has not undergone independent external scientific review.

## References
1. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928 (Springer, 2008), especially Chapter 26, §26.7, “Triangle-Free Graphs.” DOI: `10.1007/978-3-540-75859-4` (book); chapter DOI: `10.1007/978-3-540-75859-4_26`. First softcover publication: 2007-11-15.
2. S. Linusson and J. Shareshian, “Complexes of t-Colorable Graphs,” *SIAM J. Discrete Math.* 16 (2003), DOI: `10.1137/S0895480100366968`.
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, “Total Cut Complexes of Graphs,” arXiv:`2209.13503`. Different face definition; inspected for comparison.
4. M. A. Henning, “Graphs with large total domination number,” *J. Graph Theory* 35 (2000), DOI: `10.1002/1097-0118(200009)35:1<21::AID-JGT3>3.0.CO;2-F` (first public online date 2000-08-09). Standard total-domination terminology; not a topological classification.
