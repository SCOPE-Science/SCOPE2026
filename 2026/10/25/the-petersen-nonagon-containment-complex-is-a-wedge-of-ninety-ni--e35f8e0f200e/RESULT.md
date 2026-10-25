# The Petersen nonagon-containment complex is a wedge of ninety-nine four-spheres

## Finding
Let \(P\) be the Petersen graph. Define \(K(P)\) to be the abstract simplicial complex with vertex set \(E(P)\), in which a nonempty set \(F\subseteq E(P)\) is a simplex if and only if a longest simple cycle of \(P\) contains every edge of \(F\). Then

\[
K(P)\simeq\bigvee^{99}S^4.
\]

The longest cycles have nine edges, and their twenty edge sets are exactly the facets of \(K(P)\). The complex is pure of dimension eight. Its only nonzero reduced integral homology group is \(\widetilde H_4(K(P);\mathbb Z)\cong\mathbb Z^{99}\).

## Assumptions and scope
All graphs are finite, undirected, and simple. The Petersen graph is taken in its generalized-Petersen realization on vertices \(u_i,v_i\) for \(i\in\mathbb Z/5\mathbb Z\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). Thus it has ten vertices and fifteen edges. The graph is non-Hamiltonian but hypohamiltonian; its circumference is nine. Here a cycle always means a connected simple cycle, not a disjoint union of cycles. The empty simplex is included abstractly but is not a CW cell in the discrete-Morse computation.

The result concerns **subsets of edges contained in a longest cycle**, not the ordinary matching complex, the complex of all degree-at-most-two subgraphs, or the complex of subsets extendible to a Hamiltonian path.

## Proof
The claim follows from an exhaustive finite construction of an acyclic matching on the nonempty-face poset. All enumerated objects and every verification step are defined in the supplied `verify.py`; the script uses only the Python standard library. The main steps are reconstructed here so that the computation has a mathematically precise interpretation.

**1. Exhaustion of the graph cycles.** Number the outer vertices \(0,\ldots,4\) and the inner vertices \(5,\ldots,9\). Order the fifteen unordered graph edges lexicographically as pairs of integers, and represent an edge subset by its fifteen-bit characteristic mask. Test every nonempty mask. An edge subset is precisely a simple cycle if its nonisolated support is connected, contains at least three vertices, and every vertex in that support has degree two. These conditions are necessary and sufficient: a connected finite graph with every degree equal to two is a cycle. Exhaustion over the \(2^{15}-1\) nonempty masks therefore misses no cycle. The counts by length are twelve of length five, ten of length six, fifteen of length eight, and twenty of length nine, with no others. An independent enumeration using the Kneser realization \(\mathrm{KG}(5,2)\), whose vertices are two-subsets of a five-set and edges join disjoint pairs, reproduces these four numbers.

**2. Exact face enumeration.** From each of the twenty nine-edge cycle masks \(C\), insert all its nonzero submasks \(F\) into a set. This is precisely the defining face condition \(F\subseteq C\), and deduplication counts each face once. The resulting 6,320 nonempty simplices have face vector, in increasing dimension zero through eight,

\[
(15,105,445,1215,2010,1610,720,180,20).
\]

The Euler characteristic is \(100\). This arithmetic alone does *not* prove the desired homotopy type.

**3. An explicit discrete-Morse matching.** Initially mark every nonempty face unmatched. Visit the graph edges in the specified lexicographic order, indexed \(j=0,1,\ldots,14\). At stage \(j\), scan the currently unmatched face masks in increasing numerical order. If an unmatched face \(F\) does not contain edge \(j\), and \(F\cup\{j\}\) is also currently unmatched, pair these two faces and remove both from the unmatched set. Each pair is an incident face and coface differing by exactly one vertex of the complex. Exhaustive execution gives exactly 3,110 matched pairs and 100 critical faces: one zero-simplex and ninety-nine four-simplices; there are no critical faces in any other dimension.

**4. Complete gradient-acyclicity test.** Consider *all* codimension-one incidences \(F\subset G\) of nonempty faces, not just the matched incidences. Orient the incidence from \(F\) to \(G\) when it is matched; orient it from \(G\) to \(F\) otherwise. The 6,320 face vertices have exactly 32,775 such directed arcs. Constructing the complete directed Hasse graph and repeatedly deleting vertices with indegree zero removes all 6,320 vertices. A finite directed graph admits such an exhaustive topological sort if and only if it is acyclic. Thus the explicit matching is acyclic in the sense required by discrete Morse theory. Merely exhibiting the pairs or reporting their counts would not establish this step; the complete incidence test does.

**5. Homotopy conclusion.** The discrete-Morse theorem gives a CW complex homotopy equivalent to \(K(P)\) with exactly one cell of dimension zero and 99 cells of dimension four, and no other cells. Its attaching maps for the four-cells have a point as their target, so they are constant. Consequently that CW complex is a wedge of ninety-nine four-spheres. The equivalence is integral, not merely rational or mod-two. This proves the theorem.

## Verification
Run `python3 verify.py` alongside this document. The included `verify_output.txt` is the recorded output of a successful run of this exact script, ending with `VERIFY_OK`. Its assertions verify every cycle mask, independent Kneser-model cycle counts, all generated faces, all pairs and critical faces, the complete oriented Hasse graph, and a separate mod-two simplicial boundary-rank calculation. The boundary ranks in dimensions zero through eight are \((0,14,91,354,861,1050,560,160,20)\), giving mod-two Betti numbers \((1,0,0,0,99,0,0,0,0)\). The latter computation is a consistency check, not a substitute for the acyclic matching needed to establish homotopy.

As an additional face-condition check, the 128 inclusion-minimal edge subsets that do not lie in a longest cycle have size profile: ten of size three, thirty of size four, forty-eight of size five, and forty of size six. This explains why the complex is not the full simplex despite containing every one-edge and two-edge subset.

## Relationship to prior work
Holton and Sheehan's *The Petersen Graph* (1993) surveys the graph and hypohamiltonicity, making its longest cycles a canonical object. Brouwer's Petersen graph reference table gives the exact counts of simple cycles by length, including twenty nine-cycles and no ten-cycles. Neither those counts nor a statement that the graph is hypohamiltonian specifies how the twenty nine-edge sets overlap as faces, and therefore neither determines the homotopy type of their downward closure.

Nelson, Plummer, Robertson, and Zha (2011) investigate structural characterizations of the Petersen graph using chordless odd cycles and connectivity. Their statements concern graph cycles and paths, not the homotopy of this edge-subset complex. Barmak (2010) studies independence complexes and methods for their topology; its face condition is different. In fact, this complex contains all pairs of its fifteen vertices but omits ten triples, so it is not a flag independence complex on the same fifteen vertices.

Other Petersen constructions with known sphere-wedge types, including the ordinary matching, degree-at-most-two matching, graph Morse, total three-cut, and Hamiltonian-path containment complexes, use different face conditions. In particular, a nine-cycle itself is not a nine-edge Hamiltonian path. Knowing the homotopy of any one of those different complexes does not determine the homotopy of this one. The contribution is the complete homotopy classification under the exact nine-cycle containment condition.

## Limitations
This is one exact, finite-graph homotopy classification, not a theorem for arbitrary hypohamiltonian graphs or generalized Petersen graphs. The proof relies on exhaustive finite computation, but it is reproducible and verifies the complete acyclic matching rather than inferring homotopy from an experiment or homology alone. No full-text comparison with Chapter 7 of the 1993 monograph was possible; its available first-chapter excerpt and table of contents do not justify claiming the entire book lacks a related result. An earlier nonindexed or differently named equivalent calculation remains possible. No independent scientific audit is asserted.

## References
1. D. A. Holton and J. Sheehan, *The Petersen Graph*, Australian Mathematical Society Lecture Series 7, Cambridge University Press, 1993. DOI: 10.1017/CBO9780511662058. The publisher records original publication on 22 April 1993; a first-chapter excerpt is publicly accessible.
2. A. E. Brouwer, *The Petersen graph*, online mathematical graph reference, https://aeb.win.tue.nl/graphs/Petersen.html, section “Circuits and Hamiltonicity.”
3. D. Nelson, M. D. Plummer, N. Robertson, and X. Zha, “On a conjecture concerning the Petersen graph,” *Electronic Journal of Combinatorics* 18 (2011), article P20, published 19 January 2011. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v18i1p20/pdf/.
4. J. A. Barmak, “Star clusters in independence complexes of graphs,” arXiv:1007.0418v1, publicly posted 2 July 2010, https://arxiv.org/abs/1007.0418.
5. R. Forman, “Morse theory for cell complexes,” *Advances in Mathematics* 134 (1998), 90–145. DOI: 10.1006/aima.1997.1650.
