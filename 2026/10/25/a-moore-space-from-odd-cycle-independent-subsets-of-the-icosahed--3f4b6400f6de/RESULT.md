# A Moore space from odd-cycle-independent subsets of the icosahedral graph

## Finding
Let \(I\) be the simple twelve-vertex graph of the regular icosahedron. Let \(B(I)\) be the abstract simplicial complex consisting of the subsets \(A\subseteq V(I)\) for which the induced graph \(I[A]\) is bipartite (equivalently, contains no odd cycle). Let \(T(I)\) consist of the subsets for which \(I[A]\) contains no triangle. Then
\[
T(I)\searrow B(I)\simeq M(\mathbb Z/2,4),
\]
where the left arrow is a sequence of exactly twelve elementary simplicial collapses and \(M(\mathbb Z/2,4)\) is the mapping cone of the degree-two map \(S^4\to S^4\). Furthermore, \(B(I)\) is a pure, connected, nonorientable five-dimensional pseudomanifold with precisely one hundred facets. In particular,
\[
\widetilde H_k(B(I);\mathbb Z)=
\begin{cases}\mathbb Z/2,&k=4,\\0,&k\ne4.\end{cases}
\]
This identifies integral homotopy type, not only field homology.

## Assumptions and scope
The graph is finite, simple and undirected, with twelve labeled vertices \(0,\ldots,11\). Its complete adjacency table is embedded as the tuple `NBR` in `VERIFY.py`; there are thirty edges and every vertex has degree five. This is the standard icosahedral graph. A face is indexed by its twelve-bit membership mask. Both complexes include the empty face. No assertion is made for other graphs or larger orders, nor is a general Moore-space classification claimed. The verification uses only integer arithmetic and finite exhaustive enumeration.

## Proof
**Faces and minimal obstructions.** Enumerating all \(2^{12}=4096\) membership masks and testing two-colorability gives the face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(12,66,200,345,300,100)
\]
for \(B(I)\), consisting of 1,023 nonempty faces. Independently enumerating every simple odd cycle by graph depth-first search verifies the same face predicate for each mask. The inclusion-minimal nonfaces are exactly twenty triples (the graph's triangles) and twelve five-sets (five-cycles); no larger minimal obstruction exists.

**The twelve collapses.** The triangle-free complex \(T(I)\) has 1,047 nonempty faces. The difference \(T(I)\setminus B(I)\) consists of exactly twelve five-element subsets and twelve six-element subsets. Each five-element subset in the difference has exactly one proper coface in \(T(I)\), of cardinality six, and these cofaces are distinct. Removing these twelve free-face/coface pairs yields precisely \(B(I)\). Each removal is an elementary simplicial collapse, establishing the claimed simple-homotopy equivalence.

**Pseudomanifold and nonorientability.** The one hundred six-element facets are all maximal. Every one of the three hundred five-element faces is contained in exactly two facets. Their dual adjacency graph is connected (one hundred vertices and three hundred edges). Thus \(B(I)\) is a closed connected simplicial pseudomanifold of dimension five. Orient each six-vertex facet according to ascending vertex labels. Across each common five-vertex face, the sign needed to orient the next facet consistently is the negative product of the two simplicial incidence signs. The closed dual-facet walk, specified by membership masks
`09f -> 89e -> a96 -> 2b6 -> 2b5 -> 0bd -> 09f`,
has transition-sign product \(-1\), preventing a globally coherent orientation. The exact sign computation is reproduced by `VERIFY.py`.

**A complete acyclic Morse matching.** For \(v=0,1,\ldots,11\) in order, pair every as-yet-unpaired nonempty face \(A\) not containing \(v\) with \(A\cup\{v\}\) whenever both remain. The numbers of pairs by successive vertex are
`[351, 77, 30, 28, 15, 1, 0, 4, 1, 0, 3, 0]`.
This gives 510 pairs and exactly three critical faces: mask `001` in dimension zero, mask `a52` in dimension four, and mask `f60` in dimension five. In the complete directed Hasse graph, reverse precisely the 510 matched face--coface arrows and leave all others directed downward. An exhaustive topological sort visits all 1,023 face vertices and checks all 4,212 directed incidences, proving there is no directed cycle. Therefore Forman's discrete Morse theorem supplies a CW model with one cell in each of dimensions zero, four and five and no other cells.

**The integral attaching degree.** Use ascending-vertex simplicial orientations. For any four-face \(a\) paired upward with a five-face \(b\), eliminate \(a\) using the signed relation \(\partial b=0\): its coefficient in a four-chain is replaced by the negative incidence-normalized combination of the other four-faces in \(\partial b\). Any four-face paired downward to a three-face projects to zero, and the sole critical four-face projects to the unit generator. The acyclic matching makes the recursive elimination terminate. Applying it to the boundary of the critical five-face `f60` gives the **exact integer coefficient \(+2\)** at critical four-face `a52`. The executable computes the recursively reduced coefficient over all 300 four-faces, without floating point approximation. Consequently the Morse CW complex is \(S^4\cup_{\deg 2}e^5\), which is precisely \(M(\mathbb Z/2,4)\). This completes the homotopy and integral-homology claims.

## Verification
Run `python3 VERIFY.py` beside this document. The program is self-contained, requires only the Python standard library, reconstructs the adjacency matrix and all 4,096 subsets, checks bipartiteness both by parity propagation and by complete enumeration of odd simple cycles, verifies the twelve free pairs, connected signed dual pseudomanifold and negative orientation holonomy, constructs and exhaustively checks the complete discrete-Morse matching, and calculates the integral Morse differential. As an independent chain-level check, it computes ranks \((200,99)\) in degrees four and five over \(\mathbb F_2\) and \((200,100)\) over \(\mathbb F_3\). These agree with a degree-two Moore attachment. The exact captured stdout is in `VERIFICATION_OUTPUT.txt`; the program must independently exit with `VERIFY_OK`.

## Relationship to prior work
Grady, Knoll, Laskar and Lipman (initially public 9 May 2015, arXiv:1505.02268, Section 2) define *odd-cycle-independent* vertex sets as precisely those inducing bipartite subgraphs and study their extremal parameters and domination inequalities. This supplies the natural graph-theoretic object, but their accessible full text contains no homotopy, homology or icosahedral Moore-space classification. Jonsson's book on graph complexes (2007) and Hultman's 2004 directed-subgraph-complex paper concern primarily **edge-set** simplicial complexes, and their general results do not identify the present **vertex-set** complex. Jonsson's 2005 paper develops decision trees/discrete Morse methodology but does not supply this icosahedral calculation in its accessible abstract. The exact related icosahedral complexes present in indexed mathematical records (ordinary independence, higher independence, matching, neighborhood and cut complexes) have different face conditions; their published conclusions do not imply this theorem. The present complete integer attachment and elementary-collapse comparison concern the induced-odd-cycle property specifically.

## Limitations
This is a complete exact finite computer-assisted proof for one graph, not a new theorem for arbitrary graphs. Full text of Jonsson's relevant book chapters was not accessible; the book principally defines graph complexes through edge sets, but any unindexed analogous vertex-subset treatment cannot be ruled out. Searches of public literature and mathematical-result indexes do not by themselves prove uniqueness. Independent external mathematical review has not been performed. The pseudomanifold assertion does not claim manifold links, and it should not be read as a homeomorphism classification.

## References
- A. Grady, F. Knoll, R. Laskar, D. J. Lipman, *Cycle domination, independence and irredundance in graphs*, arXiv:1505.02268, first submitted 9 May 2015; especially Definition 2.7 and Section 2. https://arxiv.org/abs/1505.02268
- J. Jonsson, *Optimal Decision Trees on Simplicial Complexes*, Electronic Journal of Combinatorics 12 (2005), R3, DOI 10.37236/1900. https://doi.org/10.37236/1900
- J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928 (2007/2008), DOI 10.1007/978-3-540-75859-4. https://doi.org/10.1007/978-3-540-75859-4
- A. Hultman, *Directed Subgraph Complexes*, Electronic Journal of Combinatorics 11 (2004), R75, DOI 10.37236/1828. https://doi.org/10.37236/1828
- R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
