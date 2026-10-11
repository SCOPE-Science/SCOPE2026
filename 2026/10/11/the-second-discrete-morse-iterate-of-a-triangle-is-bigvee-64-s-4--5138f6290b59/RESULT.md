# The second discrete-Morse iterate of a triangle is \(\bigvee^{64}S^4\)

## Finding
Let \(\mathfrak M(K)\) be the simplicial complex of all acyclic partial matchings on the nonempty-face Hasse diagram of a finite simplicial complex \(K\). For the simplicial three-cycle \(C_3\), the first iterate is the triangular-prism graph \(P=C_3\mathbin{\square}K_2\), and the second iterate satisfies
\[
\mathfrak M(\mathfrak M(C_3))\cong\mathfrak M(P)\simeq\bigvee^{64} S^4.
\]
Thus \(\widetilde H_4(\mathfrak M^2(C_3);\mathbb Z)\cong\mathbb Z^{64}\), with all other reduced integral homology zero. This is a homotopy equivalence, not merely an assertion about Betti numbers.

## Assumptions and scope
All complexes are finite and abstract, with no face-pairing involving the empty simplex. A vertex of \(\mathfrak M(K)\) is a pair \((\sigma,\tau)\) of nonempty simplices satisfying \(\dim\tau=\dim\sigma+1\) and \(\sigma\subset\tau\). A finite set of such pairs is a simplex if each simplex of \(K\) occurs in at most one pair and, after reversing the corresponding Hasse arrows, there is no directed cycle. For a graph \(G\) considered as a one-dimensional simplicial complex, these are equivalently oriented vertex-edge forests, with every selected edge pointing from its matched endpoint toward the other endpoint.

Represent the triangular prism \(P\) on vertices \(0,1,2,3,4,5\) with edges
`(0,1), (0,2), (0,3), (1,2), (1,4), (2,5), (3,4), (3,5), (4,5)`.
The 18 vertices of \(\mathfrak M(P)\) are the incidences \((v,e)\) with \(v\in e\), ordered by lexicographic \(e\) and then \(v\). Every such complex vertex has an index between zero and seventeen; a face is represented by its bit mask on these indices.

## Proof
**First iteration.** The graph \(C_3\) has exactly six vertex-edge incidences. Two distinct incidences can coexist precisely when they use different graph vertices and different graph edges. There are nine such pairs, forming a connected cubic graph with two disjoint triangles; thus the one-skeleton is the triangular prism. A three-element acyclic matching would need to match all three graph vertices to all three graph edges, necessarily making a directed three-cycle, so there are no two-dimensional faces. Hence \(\mathfrak M(C_3)\cong P\) as simplicial complexes; `verify.py` checks this graph isomorphism exhaustively over all six-vertex bijections.

**Exhaustive face generation.** At every vertex of \(P\), choose no outgoing matched edge or one of its three incident edges. Among the \(4^6=4096\) choices, retain exactly those without repeated selected edges and without directed cycles. This enumerates the simplices of \(\mathfrak M(P)\) without omission. The counts of nonempty faces in dimensions zero through four are
\[
(f_0,f_1,f_2,f_3,f_4)=(18,126,428,705,450),
\]
so the complex has 1,727 nonempty faces. Independently, enumerate all 512 graph-edge subsets, discard those with cycles, and for each remaining forest count the product of its tree-component sizes (one root per component). This produces the face counts by cardinality \((1,18,126,428,705,450)\), including the empty simplex.

**Acyclic matching.** Process the 18 incidence indices in their stated order. At stage \(j\), for every currently unpaired face \(\sigma\) missing index \(j\), match it with \(\sigma\cup\{j\}\) whenever the latter is also unpaired. Remove both from subsequent stages. Exactly 828 disjoint pairs are formed. The unmatched faces have dimensions \((0,3,4)\) and multiplicities \((1,3,67)\), with no critical cells in dimensions one or two. Orient each codimension-one Hasse incidence downward unless it belongs to the matching, in which case orient it upward. A complete topological sort visits all 1,727 faces across all 6,606 directed face incidences; hence the matching is acyclic. Forman's theorem gives a CW complex homotopy equivalent to \(\mathfrak M(P)\), with one zero-cell, three three-cells and 67 four-cells. Its three-skeleton is the wedge \(\bigvee^3 S^3\).

**Integral attaching maps.** Order each simplex by increasing incidence index and use alternating signed simplicial boundaries. For a noncritical three-face \(f\) paired as a lower face to the four-face \(u\), write \(\varepsilon=[u:f]\in\{-1,1\}\). Its reduction to the critical three-cell basis satisfies
\[
R(f)=-\varepsilon\sum_{g\prec u,\,g\ne f}[u:g]R(g).
\]
For a critical three-face \(f\), set \(R(f)\) to its basis vector; for a three-face that is an upper member of a matched pair, set \(R(f)=0\). Acyclicity makes this recursion well founded. Sum these reductions, with oriented incidence signs, over the facets of each critical four-face to obtain the **integer** degree column of its attaching map. `verify.py` recomputes every such column. The critical three-face masks are `25602`, `70658`, `82946`. With the 67 critical four-faces sorted by bit mask, columns indexed `0`, `17`, `28` (corresponding to masks `26692`, `42272`, `84036`) are exactly
\[
(1,0,0)^T,\qquad(0,1,0)^T,\qquad(0,0,1)^T.
\]
These columns assert that three four-cells attach to the three-skeleton by maps of degree one on their respective three-sphere and degree zero on the other two spheres.

For \(\bigvee^3 S^3\), homotopy classes of attaching maps from \(S^3\) are determined by their three integral degree coordinates: \(\pi_3(\bigvee^3 S^3)\cong\mathbb Z^3\), since the first Whitehead-product terms occur above degree three. Therefore the subcomplex consisting of the three-sphere wedge and these three degree-basis four-cells is contractible. Each of the remaining 64 four-cells has attaching sphere mapped into this contractible subcomplex, so its attaching map is nullhomotopic there. Adjoining them yields precisely a wedge of 64 four-spheres. This proves the stated homotopy equivalence and its integral homology consequences.

## Verification
Run `python3 verify.py` and `python3 verify_homology.py` in the directory containing these files; Python's standard library suffices. The first verifies the explicit \(\mathfrak M(C_3)\)-prism isomorphism, all 1,727 faces, the independent rooted-forest enumeration, the 828 matching pairs, the acyclicity of the entire 6,606-incidence Hasse diagram, the critical-cell vector, the signed gradient-path recursion and the three integral basis attaching columns. It prints `VERIFY_OK` and `homotopy=wedge_64_S4`. The independently implemented second verifier enumerates faces from undirected rooted forests and computes exact mod-two boundary ranks \((17,109,319,386)\), giving reduced mod-two Betti vector \((0,0,0,0,64)\).

## Relationship to prior work
Chari and Joswig, *Discrete Morse Complexes* (2000), define \(\mathfrak M\), identify graph discrete-Morse matchings with rooted forests and determine the homotopy types for the cycle family in the **first** iteration. Their results do not determine the next iterate. Kozlov's 2005 paper (primary MSC 57Q10) develops constructive simple-homotopy methods for graph-derived complexes, but its theorems concern Hom-, neighborhood- and related complexes, not the present iterated graph Morse complex. Scoville and Zaremsky (2020) establish connectivity bounds for graph Morse complexes; for the nine-edge cubic prism these yield simple connectivity, not the claimed wedge or exact integral attaching maps.

The most directly overlapping published calculation, *Mod-2 homology of the triangular-prism Morse complex* (public result, 2026), obtains the same \(\mathbb F_2\) Betti rank 64 but explicitly leaves integral homology and homotopy type unproved. The present statement is an upgrade of that specific partial result, not a new claim to the mod-two number. Its three explicitly computed integral unit degree columns supply the additional homotopy information. The iterated notation and rooted-forest formulation are equivalent descriptions of the same object, not independent novelty claims.

## Limitations
The proof determines only the second iterate on the three-cycle, with no general assertion for arbitrary cycles or higher iterates. The graph-prism homology ranks over \(\mathbb F_2\) were already known. The closely related 2020 Master's thesis *The Directed Forest Complex of Cayley Graphs* (Kennedy Courtney) could not be read in full from its institutional download page and is retained as a specific potential overlap risk; its abstract alone cannot establish non-coverage. An unindexed equivalent homotopy calculation is likewise possible. The two checking scripts are reproducibility aids; no independent human audit is asserted.

## References
1. Dmitry N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613, first public submission 2005-03-28; verified primary MSC 57Q10. https://arxiv.org/abs/math/0503613
2. Manoj K. Chari and Michael Joswig, *Discrete Morse Complexes*, arXiv:math/0011234, first public submission 2000-11-28. https://arxiv.org/abs/math/0011234
3. Nicholas A. Scoville and Matthew C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, first public submission 2020-04-22. https://arxiv.org/abs/2004.10481
4. *Mod-2 homology of the triangular-prism Morse complex*, published exact result, 2026, public identifier `2026/10/4/SCOPE-mod-2-homology-of-the-triangular-prism-morse-complex--4af8059de6d1`.
5. Kennedy Courtney, *The Directed Forest Complex of Cayley Graphs*, M.S. thesis, Boise State University, 2020, DOI 10.18122/td/1684/boisestate. https://scholarworks.boisestate.edu/td/1684/
