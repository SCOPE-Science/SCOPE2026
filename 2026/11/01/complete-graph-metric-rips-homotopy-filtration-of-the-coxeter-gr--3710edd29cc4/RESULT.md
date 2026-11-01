# Complete graph-metric Rips homotopy filtration of the Coxeter graph

## Finding
Let \(G\) be the 28-vertex cubic Coxeter graph and let \(K_t=\operatorname{VR}_{\le t}(V(G),d_G)\), for real \(t\geq0\), be its *inclusive* Vietoris–Rips complex in the shortest-path metric. Its entire integral homotopy filtration, as a list of homotopy types of spaces, is
\[
K_t\simeq
\begin{cases}
\text{28 discrete points},&0\leq t<1,\\
\bigvee^{15}S^1,&1\leq t<3,\\
\bigvee^{87}S^4,&3\leq t<4,\\
\text{point},&t\geq4.
\end{cases}
\]
Moreover, the inclusion \(K_1\hookrightarrow K_2\) induces an isomorphism on integral homology (indeed, \(K_2\) collapses simplicially onto \(K_1\)). For **every** field \(\mathbb F\), the unreduced degree-zero barcode has 27 intervals \([0,1)\) and one infinite interval, the degree-one barcode has 15 intervals \([1,3)\), and the degree-four barcode has 87 intervals \([3,4)\). There are no other intervals. In particular, all integral homology groups at all scales are torsion-free.

The mathematically new stage under study is the exact degree-four sphere wedge at radius three, including its embedding in the complete filtration. The radius-two collapse follows from the existing high-girth graph-power theorem, and is not claimed as new.

## Assumptions and scope
The vertex set of \(G\) is the set of 28 three-element subsets of \(\{1,\ldots,7\}\) that are **not** lines of the binary Fano plane. The seven lines are precisely the triples \(\{a,b,a\mathbin{\mathrm{xor}}b\}\) for distinct \(a,b\in\{1,\ldots,7\}\), interpreting labels as nonzero three-bit vectors. Two vertices are adjacent if and only if their triples are disjoint. This is the standard Coxeter-graph realization, not the 30-vertex Tutte–Coxeter graph.

The metric \(d_G\) is shortest-path distance between the 28 graph vertices, not the path metric on all points of a geometric graph realization. A simplex in \(K_t\) is a nonempty vertex set whose every pair has distance at most \(t\); the empty face is understood but omitted from the finite face counter. All scales \(t\geq0\) and all coefficient fields are covered.

## Proof
**Graph reconstruction and the first radius.** The Fano-triple construction gives 28 vertices and 42 edges, has girth seven and diameter four. All assertions follow by finite enumeration in `verify.py`; the graph is identified by its standard Fano-plane construction. At radius zero the complex is 28 isolated points. At radius one it is the graph itself, hence a wedge of \(42-28+1=15\) circles.

**Radius two and the persistent degree-one classes.** Proposition 2.2 of Adamaszek, *Clique complexes and graph powers*, proves that the clique complex of the square of a graph of girth at least seven collapses to the original graph. For the Coxeter graph there is also a direct explicit picture: the 28 maximal simplices at radius two are exactly the tetrahedra on the closed vertex neighborhoods, each consisting of a vertex and its three neighbors. Each tetrahedron collapses relative to its three incident original edges: pair its opposite triangular face with the tetrahedron, then pair each of the other three triangular faces with its unique new distance-two edge. No distance-two edge is shared by two such tetrahedra, because that would form a short cycle. Thus the 112 pairs leave the original graph as a subcomplex and establish that the inclusion \(K_1\hookrightarrow K_2\) is a homotopy equivalence. The source theorem, not this restatement, supplies the general high-girth fact.

**Radius three.** The verifier constructs every simplex of the clique complex of the third graph power. Its exact face vector by increasing simplex dimension is
\[
(28,294,1456,3514,3864,1596,144),
\]
so there are exactly 10,896 nonempty faces. The verifier constructs an acyclic discrete-Morse matching with exactly 5,404 disjoint pairs, one critical vertex and 87 critical four-dimensional simplices. Its matching recipe is deterministic: use this fixed vertex-pivot order

`9,27,18,7,21,0,1,17,8,3,19,5,26,4,13,25,11,6,12,23,22,2,15,14,10,24,16,20`

and at each pivot match every currently unmatched nonempty face not containing the pivot to the face obtained by adjoining it, when the latter face is still unmatched. Ties are processed by increasing face size and then increasing bitmask. The program validates every pairing against the reconstructed face set and independently checks acyclicity on the **entire** oriented Hasse diagram: orient matched cover relations upward, all other cover relations downward; a topological sort visits all 10,896 faces across 48,916 cover incidences. Hence Forman's discrete-Morse theorem gives a CW model with one zero-cell and precisely 87 four-cells and no cells of any other positive dimension. Every attaching map is constant, so \(K_3\simeq\bigvee^{87}S^4\) integrally.

**Radius four and all persistence intervals.** The diameter is four, so \(K_4\) is a full simplex. At each integer threshold the homotopy groups change exactly as stated. The radius-one-to-two inclusion is a homotopy equivalence by the relative collapse above, the only surviving positive-degree homology in the intermediate stage is degree one, and the only nonzero positive-degree homology at radius three is degree four. Since the next complex is contractible, the field-independent barcode follows. These claims require no extrapolation from coefficient-field computations.

## Verification
Run `python verify.py` in the same directory as this file. It requires Python's standard library only. It reconstructs the Fano construction, breadth-first distances, girth, all cliques in each graph power, and the exact discrete-Morse matching. It then checks the full oriented Hasse DAG by topological sorting. The independent mod-two boundary-rank check returns the boundary ranks \((27,267,1189,2325,1452,144)\) at radius three, giving the expected degree-four Betti number 87. The output of an executed run is included as `verified_output.txt`. **The Morse matching and Hasse acyclicity, not the mod-two rank computation, prove the integral homotopy statement.** Exhaustive finite enumeration is valid here because the object has exactly 28 vertices, and all clique faces are generated recursively with no size cutoff.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* (arXiv:1104.0433, originally public April 3, 2011), particularly Proposition 2.2 and Sections 3 and 6, supplies the graph-power framework and already proves the radius-two collapse from the girth bound. Its cycle-power classification does not imply the Coxeter radius-three 87-sphere wedge: the Coxeter graph is cubic of order 28 and is not a cycle; girth seven does not satisfy the source's required bound of at least ten for radius three. The standard description of the Coxeter graph fixes the named graph and its Fano-triple realization.

The closest indexed same-name result concerns the **independence complex of the Coxeter graph** (independent subsets of edges' nonadjacent vertices), not the Rips complex of its third power. The indexed scale-three Tutte–Coxeter calculation concerns a different, 30-vertex, bipartite graph, with a different homotopy degree and multiplicity. Neither result implies the present statement for the 28-vertex Coxeter graph. Targeted searches for the Coxeter third graph power, its radius-three Rips complex, equivalent distance-four independence formulation, and the specific four-dimensional homology multiplicity found no covering statement. Non-indexed or inaccessible equivalent calculations remain a publication-priority risk.

## Limitations
This is an exact nonequivariant integral homotopy and all-field persistence result for this one 28-vertex graph, not a classification of arbitrary high-girth graphs. It does not compute the automorphism representation on the 87 homology generators, explicit integral cycle bases, Steenrod operations, or the homotopy types of symmetry quotients. The finite checker is a transparent computational proof of a fixed complex; it is not an independent external audit. Originality rests on comparisons with accessible literature and indexed research records and is not a claim of exhaustive publication priority.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (initial submission April 3, 2011), especially Proposition 2.2 and Sections 3, 6 and 7. https://arxiv.org/abs/1104.0433
2. Wolfram MathWorld, *Coxeter Graph*: https://mathworld.wolfram.com/CoxeterGraph.html (standard finite graph definition, not a Rips-topology calculation).
3. published-finding corpus record, *The scale-three Rips complex of the Tutte–Coxeter graph is a wedge of 256 three-spheres*, indexed 2026: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-scale-3-rips-complex-of-the-tutte-coxeter-graph-is-a-wedge-o--9454ecd0bd54 (different graph; full page inaccessible during comparison).
4. published-finding corpus record, *The Coxeter graph independence complex is a wedge of seven six-spheres*, indexed 2026: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-coxeter-graph-independence-complex-is-bigvee-7-s-6--8a1bdfa47e09 (different simplicial complex; full page inaccessible during comparison).
