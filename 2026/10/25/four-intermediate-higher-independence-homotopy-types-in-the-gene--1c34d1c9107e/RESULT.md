# Four intermediate higher-independence homotopy types in the generalized Petersen family

## Finding
For \(n\in\{6,7,8,9\}\), let \(G_n=\operatorname{GP}(n,2)\). The two-independence complex has the following **integral homotopy types**:
\[
\begin{aligned}
|\operatorname{Ind}_2(G_6)|&\simeq S^3\vee S^3\vee S^3\vee S^4,\\
|\operatorname{Ind}_2(G_7)|&\simeq S^5,\\
|\operatorname{Ind}_2(G_8)|&\simeq\bigvee^{7}S^5,\\
|\operatorname{Ind}_2(G_9)|&\simeq\bigvee^{4}S^5.
\end{aligned}
\]
In particular, the Dürer graph \(G_6\) exhibits two distinct nonzero positive homology degrees, whereas each of the next three intermediate complexes is a wedge in one degree. These are four exact finite cases, **not** an infinite-family periodicity assertion.

## Assumptions and scope
The generalized Petersen graph \(\operatorname{GP}(n,2)\) has vertices \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\) and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). Fix exactly \(n=6,7,8,9\), without any edge weights or additional symmetries. The two-independence simplicial complex \(\operatorname{Ind}_2(G)\) consists of all subsets \(A\subseteq V(G)\) such that **every connected component** of the induced graph \(G[A]\) has at most two vertices. Equivalently, every vertex has degree at most one within \(G[A]\). All homotopy and homology assertions are integral; no equivariance or classification beyond these four values is asserted.

## Proof
For any listed \(n\), represent a subset of vertices by a \(2n\)-bit unsigned integer mask, with bits \(0,\ldots,n-1\) representing the \(u\)-vertices and the remaining bits representing the \(v\)-vertices. The degree-at-most-one characterization above makes a complete, integer-only enumeration of the face set possible: iterate over all \(2^{2n}\) masks and retain exactly those for which every selected bit has at most one selected neighbor. This is exhaustive because every vertex subset has exactly one bitmask.

An explicit acyclic discrete-Morse matching is described by the four permutations \(O_n\) in the embedded file `verify_gp2.py` (the `ORDERS` mapping). Begin with every **nonempty** face unmatched; for each vertex in \(O_n\), in increasing order of simplex dimension and then integer mask, pair every still-unmatched simplex \(\sigma\) not containing the vertex with \(\sigma\cup\{v\}\), provided both are present and unmatched. Discard a matched pair from further steps. The empty face is never matched. The verifier enumerates the entire face poset, checks that every pair is an actual codimension-one face relation, reverses the matching edges in the full Hasse diagram, and proves acyclicity by an exhaustive topological sort. The topological-sort successes are finite, fully enumerated certificates rather than samples or heuristic matching claims.

The complete nonempty-face counts are, respectively, \(809,2268,6710,20799\). The numbers of matched pairs are \(402,1133,3351,10397\). The surviving critical cells, indexed by their dimensions, are
\[
\begin{array}{c|l}
n&\text{critical-cell dimensions and multiplicities}\\\hline
6&0:1,\quad 3:3,\quad 4:1\\
7&0:1,\quad 5:1\\
8&0:1,\quad 5:7\\
9&0:1,\quad 5:4
\end{array}
\]
Thus, by discrete Morse theory, for \(n=7,8,9\) the CW models comprise a single vertex and respectively \(1,7,4\) cells of dimension five. The resulting spaces are precisely the asserted wedges of five-spheres, with no possible attaching maps in lower positive dimensions.

For \(n=6\) there remain a vertex, three three-cells, and a single four-cell. The three-skeleton is a wedge of three three-spheres. Its attaching map lies in
\[\pi_3(S^3\vee S^3\vee S^3)\cong H_3(S^3\vee S^3\vee S^3;\mathbb Z)\cong\mathbb Z^3.\]
The first isomorphism is the Hurewicz isomorphism for a two-connected CW complex. Therefore **it suffices to compute the integral attaching degrees**, not just Betti numbers. Using increasing vertex order as the simplex orientation, the explicit integer Morse-reduction recurrence cancels every matched three/four pair using its unit incidence coefficient. All degree-three gradient paths are completely expanded, and the signed boundary of the unique critical four-cell (bitmask `724`) against critical three-cell bitmasks `402`, `420`, `585` is verified to be the vector \((0,0,0)\). Since the Hurewicz map is an isomorphism, the attaching map is null-homotopic. The four-cell attaches trivially, giving \(S^3\vee S^3\vee S^3\vee S^4\).

## Verification
Execute the embedded standard-library-only script from its actual extracted path with `python3 verify_gp2.py`. It reconstructs all four graphs and verifies cubic vertex degrees, enumerates all faces, regenerates all Morse pairs, checks completeness and critical-cell vectors, constructs every nonempty face-poset cover and runs an exhaustive directed-acyclicity check. Its four outputs report, respectively, \(3180,10248,34576,121482\) directed Hasse edges. For \(n=6\), it additionally propagates **signed integral coefficients** through all relevant gradient cancellations, establishing the zero attaching-degree vector. The computations use exact integers throughout; no field approximation, graph-library calls, randomness, or saved reference log is required. A separate small finite-field homology cross-check agreed with the resulting homology ranks; the infinite-family validity of unrelated statements is not claimed.

## Relationship to prior work
Ghosh–Selvaraja (arXiv:2505.06614, initially posted 2025-05-10) studies higher-independence shellability/chordality and graph constructions; the inspected primary text does not supply these four generalized-Petersen homotopy types. Deshpande–Roy–Sawant (arXiv:2510.25710, first posted 2025-10-29) works with Alexander-dual higher-independence complexes for other graph classes, giving no identified statement implying the four types. Pandey (arXiv:2601.03293, first posted 2026-01-05) treats the **ordinary** independence polynomial of the same generalized-Petersen graph family, not these two-independence complexes or homotopy. Previously available computations of the Petersen \(n=5\) and dodecahedral \(n=10\) two-independence complexes are adjacent boundary cases but do not imply any of the four intermediate homotopy types; general matching complexes, ordinary independence complexes, and graph-metric Rips complexes are different objects. The Alexander-dual viewpoint alone does not fix the integral attaching maps.

## Limitations
Only four explicitly named finite graphs are classified; the computation does not prove a uniform formula, periodicity, equivariant homotopy result, or behavior of any larger parameter. The zero integral attaching degree for \(n=6\) is essential and must not be replaced by mod-two ranks or an unverified wedge inference. The originality comparison covers the stated inspected sources and available indexed research, but cannot exclude equivalent unindexed computations. The work has no independent external scientific audit.

## References
1. A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614 (initial posting 2025-05-10), https://arxiv.org/abs/2505.06614.
2. P. Deshpande, A. Roy, and R. Sawant, *The Complex of \(r\)-Co-Connected Subgraphs, Chordality and Fröberg's Theorem*, arXiv:2510.25710 (initial posting 2025-10-29), https://arxiv.org/abs/2510.25710.
3. R. Pandey, *Parity-Dependent Real-Rootedness in Independence Polynomials of Generalized Petersen Graphs*, arXiv:2601.03293 (initial posting 2026-01-05), https://arxiv.org/abs/2601.03293.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145 (general acyclic-matching theorem).
