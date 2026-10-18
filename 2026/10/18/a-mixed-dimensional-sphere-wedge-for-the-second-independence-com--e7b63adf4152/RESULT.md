# A mixed-dimensional sphere wedge for the second independence complex of the triangular graph \(T_6\)

## Finding
Let \(T_6=L(K_6)=J(6,2)\), the triangular graph on the fifteen two-element subsets of \(\{0,1,2,3,4,5\}\), with two vertices adjacent precisely when their subsets intersect. Its *second independence complex* \(X=\operatorname{Ind}_2(T_6)\) consists of those sets \(F\) of graph vertices for which every connected component of the induced graph \(T_6[F]\) contains at most two vertices. Then there is an **integral homotopy equivalence**
\[
X\simeq\bigvee^{24}S^2\ \vee\ \bigvee^{10}S^3.
\]
In particular, \(X\) is simply connected, its reduced integral homology is \(\mathbb Z^{24}\) in degree two and \(\mathbb Z^{10}\) in degree three, and all its other reduced integral homology groups vanish. The statement classifies a particular natural graph complex; it is not a classification for all triangular graphs.

## Assumptions and scope
All graphs are finite and simple. The line graph \(L(K_6)\) has one vertex for each edge of \(K_6\); two such vertices are adjacent when the corresponding edges share an endpoint. In the original complete graph, a face of \(X\) is precisely a selection of edges whose connected components are each either an isolated edge or a two-edge path on three vertices. The latter is **not** the ordinary two-matching/bounded-degree complex of \(K_6\): that larger complex permits three-edge cycles and longer paths. Nor is \(X\) the ordinary matching complex or the clique complex of the line graph.

For the reproducible finite certificate, label the original vertices \(0,1,2,3,4,5\), and index its fifteen edges lexicographically by integers \(0\) through \(14\). Encode each face as the integer whose set bits are its chosen edge indices. The calculation concerns **all** \(2^{15}\) subsets, without random sampling or truncation.

## Proof
**Step 1: complete face description.** A selected vertex of the induced line graph has degree at most one if and only if all its components have at most two vertices. Therefore the face test amounts to checking, for each selected edge \(e\) of \(K_6\), that at most one other selected edge meets \(e\). Equivalently, the edge-induced graph on the six original vertices is a disjoint union of isolated edges and two-edge paths. If there are \(a\) isolated-edge components and \(b\) two-edge-path components, they use \(2a+3b\le6\) original vertices and contribute \(a+2b\) selected edges. Counting unlabeled components and three choices of the missing edge within each three-element block gives the exact number of such faces:
\[
N_{a,b}=\frac{6!\,3^b}{2^a6^b\,a!\,b!\,(6-2a-3b)!}.
\]
This formula gives the augmented face numbers \((1,15,105,195,90)\) by face cardinality zero through four. In particular there are exactly 405 nonempty faces, with \(15\) maximal triangles and \(90\) maximal tetrahedra. The complex is not pure.

**Step 2: an explicit acyclic discrete-Morse matching.** Use successive element matchings on the **nonempty** face poset, in the vertex-index order
```
6, 12, 5, 4, 2, 7, 1, 0, 10, 11, 14, 8, 3, 13, 9
```
At an index \(j\), among the currently unmatched faces, match each face \(F\) not containing \(j\) to \(F\cup\{j\}\), provided both remain unmatched and are faces. Remove both and continue to the next index. Each such pair is a codimension-one cover relation. The standard successive-element-matching lemma proves acyclicity; independently, the included checker explicitly orients and topologically sorts every cover relation to verify the absence of a directed cycle. The matching has precisely 185 pairs and leaves critical-cell counts \((c_0,c_1,c_2,c_3)=(1,0,24,10)\). These counts are obtained by an exhaustive finite calculation over the complete 405-element nonempty face poset, not inferred from Betti numbers.

**Step 3: the integral attaching maps.** A discrete-Morse CW model has one zero-cell, no one-cells, 24 two-cells and 10 three-cells. The only potentially nonzero Morse chain differential is \(\partial_3:\mathbb Z^{10}\to\mathbb Z^{24}\). Give every original simplex the orientation of its increasing edge indices. Every incidence coefficient is \(+1\) or \(-1\). For each critical three-cell, start with its signed simplicial boundary. For any two-face \(\tau\) paired upward with a three-face \(\mu\), eliminate its coefficient using the exact integral relation obtained from \(\partial\mu\), whose coefficient at \(\tau\) is a unit. Descending along the acyclic gradient relations makes this a finite process. The included checker performs this recursion for every critical three-cell and finds that **all 240 possible entries** of the \(24\)-by-\(10\) integral Morse matrix are zero. This is an integer equality, not a modular inference.

**Step 4: from chains to homotopy.** The Morse model is a simply connected CW complex with a wedge of 24 two-spheres as its two-skeleton. For such a two-skeleton the Hurewicz map identifies \(\pi_2\) with \(H_2\cong\mathbb Z^{24}\). Hence each three-cell attaching map is classified by its degree vector in that free abelian group. The computed integral Morse differential is zero, so every attaching map is null-homotopic. Attaching the ten three-cells therefore yields exactly the asserted wedge of 24 two-spheres and ten three-spheres.

## Verification
Run `python3 verify.py` from any directory using Python 3.10 or newer; only the standard library is needed. The program independently tests all \(2^{15}\) subsets using both the component-size definition and the local-degree characterization, verifies the closed counting formula, reconstructs the specified matching, checks acyclicity over all 1,155 nonempty face-poset cover incidences, and reconstructs the **signed integer** Morse differential by gradient elimination. It also computes ordinary unreduced mod-two boundary ranks \((14,91,80)\) in positive degrees, corresponding to reduced mod-two Betti numbers \((0,0,24,10)\) in degrees zero through three. The modular computation is corroborative; the homotopy theorem rests on the exact integral Morse differential and the simply connected CW model.

## Relationship to prior work
Deshpande and Singh's initial study of higher independence complexes (arXiv:2001.05448, first publicly posted January 15, 2020) defines the construction, develops successive element matchings and classifies complete multipartite, fully whiskered, path, cycle and perfect-tree families; it does not treat the triangular line graph \(L(K_6)\). Abdelmalek, Deshpande, Goyal, Roy and Singh (arXiv:2106.10863) study shellability and vertex decomposability for chordal graphs and related graph classes; \(T_6\) has induced four-cycles and is not chordal. Goyal, Shukla and Singh (arXiv:2009.12130) determine clique-complex homotopy for line graphs; a clique complex is not the second independence complex here. Singh's higher matching paper (arXiv:2006.13632) studies vertex-degree bounded edge families, and its general results do not imply this **component-size-constrained** calculation. Thus the numerical and integral homotopy conclusions are not consequences of those inspected theorems. The classification remains subject to possible unindexed equivalent literature.

## Limitations
The result concerns \(\operatorname{Ind}_2(L(K_6))\) only. It establishes an ordinary, non-equivariant integral homotopy equivalence, not a canonical sphere splitting respecting the \(S_6\)-action, and gives no formula for larger complete graphs. The finite algorithm is exhaustive **only for this fifteen-vertex complex**, and is not presented as a proof of an infinite-parameter conjecture. No independent mathematical audit has been performed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (initial public version January 15, 2020), https://arxiv.org/abs/2001.05448.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863 (2021), https://arxiv.org/abs/2106.10863.
3. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (2020), https://arxiv.org/abs/2009.12130.
4. A. Singh, *Higher Matching Complexes of Complete Graphs and Complete Bipartite Graphs*, arXiv:2006.13632 (2020), https://arxiv.org/abs/2006.13632.
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145. The standard discrete-Morse equivalence and signed gradient-path boundary are used.
