# The complete Petersen vertex-forest filtration and its simple-collapse plateau

## Finding
Let \(P\) be the Petersen graph, and let \(\mathcal F_d(P)\) be the simplicial complex of vertex subsets whose induced graph is a forest with maximum vertex degree at most \(d\). Its complete integral homotopy-type filtration is
\[
\mathcal F_0(P)\simeq\bigvee^4 S^2,\qquad
\mathcal F_1(P)\simeq\mathcal F_2(P)\simeq S^3,\qquad
\mathcal F_3(P)=\mathcal F_\infty(P)\simeq\bigvee^6 S^5.
\]
Moreover, the canonical inclusion \(\mathcal F_1(P)\hookrightarrow\mathcal F_2(P)\) is a **simple homotopy equivalence**: \(\mathcal F_2(P)\) simplicially collapses onto \(\mathcal F_1(P)\) in exactly 180 explicitly reproducible elementary collapses.

Consequently, the positive-degree reduced integral persistent homology, indexed by integer degree thresholds \(d=0,1,2,3,\ldots\), has four degree-two interval summands \([0,1)\), one degree-three interval \([1,3)\), and six degree-five interval summands \([3,\infty)\), each with coefficient group \(\mathbb Z\). All other reduced integral persistent groups vanish. No canonical decomposition of the sphere summands is claimed.

## Assumptions and scope
Use vertices \(\{0,1,\dots,9\}\), five outer edges \(\{i,(i+1)\bmod5\}\), five inner edges \(\{5+i,5+((i+2)\bmod5)\}\), and five spokes \(\{i,5+i\}\), for \(0\le i<5\). This is the usual cubic Petersen graph. Write \(G[A]\) for the induced graph on a vertex subset \(A\). A subset is a simplex exactly when \(G[A]\) is acyclic and has maximum degree at most \(d\). The empty face is included in the augmented matching but is not counted among nonempty faces. Since the graph is cubic, the filtration is constant for all \(d\ge3\). The comparison is between **vertex-subset** complexes, not edge-based matching complexes.

A face \(A\) is encoded by the mask \(m(A)=\sum_{i\in A}2^i\), with \(0\le m<1024\). The face predicate is checked by scanning the 15 graph edges and verifying the induced maximum degree and the forest identity \(|E(G[A])|=|A|-c(G[A])\), where \(c(G[A])\) is the number of connected components, including \(c(G[\varnothing])=0\).

## Proof
**Complete enumeration.** The standalone verifier exhausts all \(1024\) vertex masks for each parameter. The nonempty face vectors \((f_0,f_1,\ldots)\) are exactly
\[
\begin{array}{c|c|r}
d & (f_0,f_1,\ldots) & \text{nonempty faces}\\\hline
0&(10,30,30,5)&75\\
1&(10,45,90,80,30,5)&260\\
2&(10,45,120,200,180,65)&620\\
3&(10,45,120,210,240,140,20)&785.
\end{array}
\]
These are exhaustive finite counts, not estimates.

**Acyclic Morse reductions.** For \(d\in\{0,2,3\}\), begin with all faces including the empty face available. For each vertex \(v=0,1,\ldots,9\) in that order, visit available face masks \(m\) in increasing order and pair \(m\) with \(m+2^v\) whenever the first does not contain \(v\) and both faces remain available. Remove both paired faces before visiting subsequent vertices. In all three instances the empty face is paired with the vertex \(\{0\}\). The final unpaired masks, and no others, are
\[
\begin{aligned}
d=0 &: \quad (104,208,548,770), &&\text{each of dimension }2;\\
d=2 &: \quad (30), &&\text{of dimension }3;\\
d=3 &: \quad (380,498,756,798,934,978), &&\text{each of dimension }5.
\end{aligned}
\]
The matching has respectively \(36,310,390\) pairs in the augmented face poset. To certify acyclicity without relying on a heuristic toggle argument, orient **every** codimension-one Hasse relation from the lower face to the upper face if matched, and from the upper face to the lower face otherwise. A complete topological sort removes all \(76,621,786\) face-poset vertices, respectively, with \(180,2550,3480\) Hasse arcs. This proves that each directed matching graph is acyclic. Deleting the pair containing the empty face yields an ordinary simplicial discrete-Morse matching with one critical vertex plus precisely the indicated positive-dimensional critical faces. Forman's discrete Morse theorem therefore produces CW complexes consisting of one zero-cell and respectively four two-cells, one three-cell, and six five-cells; the attaching maps target a point, so their homotopy types are the asserted wedges of spheres. This establishes integral homotopy equivalences, not just field homology ranks.

**The intermediate simple collapse.** Independently retain the full face sets for \(\mathcal F_1(P)\) and \(\mathcal F_2(P)\). Starting with the latter, repeatedly take a face \(\sigma\notin\mathcal F_1(P)\) having exactly one immediate coface \(\tau\) in the current complex, such that \(\tau\) has no immediate coface and \(\tau\notin\mathcal F_1(P)\). Pick the eligible pair with largest \(\dim\tau\), breaking ties by smallest face-mask of \(\sigma\). Each pair is a free face and its unique containing facet, hence deleting the pair is an elementary simplicial collapse. After exactly \(180\) iterations there are no faces left outside \(\mathcal F_1(P)\), and every face of \(\mathcal F_1(P)\) has been preserved. The fully specified finite algorithm and assertions are in `verify_petersen_forest.py`; in particular every eligibility condition is checked afresh in the current complex. Thus the inclusion \(\mathcal F_1(P)\hookrightarrow\mathcal F_2(P)\) is a simple homotopy equivalence, and \(\mathcal F_1(P)\simeq S^3\) follows from the already proved reduction of \(\mathcal F_2(P)\).

**Persistence.** The four reduced degree-two generators present at threshold \(0\) map to zero at threshold \(1\), because \(\mathcal F_1(P)\) has no reduced degree-two homology. The integral degree-three generator at threshold \(1\) maps isomorphically through the inclusion into threshold \(2\), by the elementary collapse. It maps to zero at threshold \(3\), because the terminal complex has no reduced degree-three homology. Six free degree-five generators appear at threshold \(3\) and persist unchanged thereafter, since every subsequent filtration complex is identical. There are no additional generators or torsion by the CW decompositions above.

## Verification
From a directory containing the two standalone Python scripts, run `python3 verify_petersen_forest.py` and `python3 verify_petersen_homology.py`. Only the Python standard library is required. The first checks all graph edges, all \(1024\) subsets at four thresholds, the complete acyclic matching digraphs, and every one of the \(180\) free-face collapses. The second uses a separate cycle-detection forest predicate and exact oriented simplicial boundary matrices over fields of characteristics \(2,3,5,101\); its reduced Betti numbers are \((0,0,4,0)\), \((0,0,0,1,0,0)\), \((0,0,0,1,0,0)\), and \((0,0,0,0,0,6,0)\). The first script's complete verified matchings and collapses, not the finite-field ranks, supply the integral homotopy proof. Recorded reproducible output is provided in `verification_output.txt`.

## Relationship to prior work
Carnero Bravo introduced the forest filtration and calculated its homotopy for several graph families, including paths, cycles, double stars, cactus graphs and certain graph products; the relevant results do not give the four-stage Petersen classification. The present graph is a connected cubic girth-five graph with overlapping cycles, not a cactus or any of those directly treated families. Deshpande and Singh studied higher independence complexes of several graph families. The Petersen second higher-independence complex is **exactly** \(\mathcal F_1(P)\), and a published independent calculation already establishes \(\mathcal F_1(P)\simeq S^3\); that previously known fact is **not claimed as an original result** here. Berghoff computed the Petersen independence-complex homology, which concerns the threshold \(\mathcal F_0(P)\), not the degree-two collapse or the full forest stage. The contributions here are the explicit simple collapse \(\mathcal F_2(P)\searrow\mathcal F_1(P)\), the homotopy type of \(\mathcal F_\infty(P)\), and the complete inclusion-induced persistence. The ordinary Petersen edge-matching complex, three-cut complexes, and graph-metric complexes use distinct simplices and do not imply these statements.

## Limitations
The result concerns this specified ten-vertex Petersen graph and the induced-forest **vertex** filtration only. It does not classify arbitrary cubic or vertex-transitive graphs, and it asserts neither equivariance of chosen Morse matchings nor a canonical splitting into sphere factors. The finite proof exhausts all vertex subsets of this graph; it is not an infinite-family classification. A separately indexed or unpublished equivalent calculation may exist. The source homotopy data for the independence and higher-independence endpoints is acknowledged; originality concerns the explicitly distinguished new collapse, unrestricted endpoint and persistence.

## References
- A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first publicly posted 2023-07-25; definitions in Section 3 and graph-family results in Section 4.
- P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first publicly posted 2020-01-15.
- M. Berghoff, *On the Homology of Independence Complexes*, arXiv:2008.06267, Section 6 (Petersen example).
- *The Petersen two-independence complex is a three-sphere*, publicly available mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-petersen-two-independence-complex-is-a-three-sphere--0d53a7f4e76a .
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145.
