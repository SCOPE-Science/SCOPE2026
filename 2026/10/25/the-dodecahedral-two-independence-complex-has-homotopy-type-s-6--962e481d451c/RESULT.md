# The dodecahedral two-independence complex has homotopy type \(S^6\)

## Finding
Let \(D\) be the dodecahedral graph, realized as the generalized Petersen graph \(\operatorname{GP}(10,2)\). The two-independence complex \(\operatorname{Ind}_2(D)\), whose faces are subsets inducing components of order at most two, satisfies the integral homotopy equivalence

\[
\left|\operatorname{Ind}_2(D)\right|\simeq S^6.
\]

In particular, \(\widetilde H_6(\operatorname{Ind}_2(D);\mathbb Z)\cong\mathbb Z\), and all other reduced integral homology groups vanish. This is a homotopy-equivalence statement, not a claim of homeomorphism: the complex has facets in four different dimensions, including dimension eleven.

## Assumptions and scope
The vertices are \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\). The edges are exactly \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+2}\}\), with subscripts reduced modulo ten. For computations, the vertex indices \(0,\ldots,9\) denote \(u_0,\ldots,u_9\), and indices \(10,\ldots,19\) denote \(v_0,\ldots,v_9\).

A subset \(W\subseteq V(D)\) is a face if every connected component of its induced subgraph \(D[W]\) contains one or two vertices. Equivalently, no connected three-vertex subset is contained in \(W\). Since \(D\) is cubic and triangle-free, there are exactly sixty distinct minimal forbidden triples, each consisting of a vertex and two of its three neighbors.

The theorem concerns this single explicitly defined twenty-vertex graph and the parameter two; it asserts no analogous classification for arbitrary cubic graphs or other independence parameters.

## Proof
**1. Exact face recognition.** Encode a subset by the twenty-bit nonnegative integer whose set bits indicate selected vertices. Let \(F(s)\) indicate whether the subset represented by \(s\) belongs to the complex. Set \(F(0)=1\). For positive \(s\), let \(j\) be its least set-bit index and \(p=s-2^j\). Then \(F(s)=1\) exactly when \(F(p)=1\) and \(p\) contains none of the two-vertex complements \(T\setminus\{j\}\) for the forbidden triples \(T\) containing \(j\). This recurrence follows because any forbidden triple first appearing in \(s\) must contain \(j\). It decides all \(2^{20}\) subsets, with no probabilistic sampling or truncation.

The resulting face numbers, ordered by cardinality from zero through twelve, are

\[
(1,20,190,1080,3985,9772,15870,16640,10770,4000,750,60,5).
\]

The number of faces including the empty face is 63,143. The maximal faces are exactly 25 of dimension seven, 60 of dimension eight, 420 of dimension nine, and five of dimension eleven. The reduced Euler characteristic computed from the face numbers is one.

**2. Explicit discrete-Morse matching.** List all faces in increasing integer-mask order, including the empty face. Process the vertex indices in the following fixed order:

`10,17,4,16,14,0,8,6,1,9,5,3,13,7,11,2,12,19,18,15`.

At the stage associated with index \(j\), match every still-unmatched face \(W\) not containing \(j\) with \(W\cup\{j\}\) whenever the latter is still unmatched and is a face. These are cover relations, and no face is used twice. After all stages, unmatch the pair \((\varnothing,\{v_0\})\); this gives an ordinary (nonaugmented) face-poset matching. It has 31,570 pairs, exactly one unmatched nonempty zero-face \(\{v_0\}\), and exactly one unmatched six-face

\[
\{u_0,u_3,u_6,u_7,u_9,v_4,v_8\}.
\]

The latter is bitmask 279241 in the specified encoding. The empty face is unmatched and is not a cell of the ordinary face-poset Morse model.

**3. Exhaustive acyclicity certificate.** Give each covering edge \(\sigma\subset\tau\) in the augmented face poset the direction \(\sigma\to\tau\) when matched and \(\tau\to\sigma\) otherwise. The standalone checker builds all 410,520 such directed incidences and performs an integer Kahn topological-sort elimination; it visits every one of the 63,143 faces. Therefore the directed cover graph has no directed cycle. Restricting to nonempty faces preserves acyclicity. These conclusions are verified by finite enumeration of the full poset, not by a partial search or an unverified matching count.

**4. Homotopy conclusion.** By discrete Morse theory, the realization has the homotopy type of a CW complex with exactly one zero-cell and one six-cell, and no other cells. The unique attaching map of the six-cell has target the one-point five-skeleton, hence is constant. Its CW quotient is \(S^6\). This establishes the integral homotopy equivalence and, consequently, the stated homology with arbitrary coefficients.

## Verification
The file `verify_dodecahedron.cpp` contains the complete finite certificate. It builds the graph independently of any external graph library, evaluates every one of the \(2^{20}\) vertex subsets using both the forbidden-triple recurrence and a separate connected-component breadth-first search, verifies the full face and facet vectors, constructs the stated matching, and checks every cover edge and the global acyclicity of the directed Hasse graph. Compile using `c++ -O2 -std=c++17 verify_dodecahedron.cpp -o verifier` and execute `./verifier`. Success terminates with `VERIFY_OK`; discrepancies terminate nonzero. The same calculations were replayed with two C++ compilers, and with undefined-behavior checking enabled.

## Relationship to prior work
Deshpande and Singh study higher independence complexes and give homotopy classifications for complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect rooted trees. Ghosh and Selvaraja subsequently establish shellability criteria for specified forest, block-graph and graph-attachment families. The dodecahedral graph is neither a forest nor a block graph, and it is not among the graph families for which those papers provide an exact two-independence homotopy type.

Related published computations for the same graph treat its ordinary one-independence complex, not the two-independence complex. A published two-independence computation for the ten-vertex Petersen graph concerns a different graph and does not imply the present twenty-vertex result. The present classification therefore adds a natural nonchordal cubic symmetric example at the first higher-independence parameter. These comparisons establish a specific distinction from inspected prior claims, not universal proof of priority.

## Limitations
This is an exact finite-graph classification supported by an exhaustive, deterministic computational certificate, not a symbolic classification of all generalized Petersen graphs. No uniqueness or generalization to other cubic graphs is established. An equivalent unindexed earlier computation may exist; independent scientific review has not been conducted. The proof uses the standard discrete-Morse theorem and the stated complete executable certificate; the displayed face counts by themselves would not prove the homotopy equivalence.

## References
- P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first posted January 15, 2020. https://arxiv.org/abs/2001.05448
- A. Ghosh and S. Selvaraja, *Chordality and Shellability of Higher Independence Complexes*, arXiv:2505.06614, first posted May 10, 2025 (later versions under the title *Shellability of Higher Independence Complexes of Graphs*). https://arxiv.org/abs/2505.06614
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
- E. W. Weisstein, *Dodecahedral Graph*, MathWorld; identifies the graph with \(\operatorname{GP}(10,2)\). https://mathworld.wolfram.com/DodecahedralGraph.html
