# Complete six-vertex tournament neighborhood-complex homotopy census
## Finding
For the out-neighborhood complex \(\overrightarrow{\mathcal N}(T)\) of a tournament \(T\) on six vertices, the 56 isomorphism classes have exactly the following homotopy-type distribution:
\[
34\,[\mathrm{pt}],\quad 11\,[S^1],\quad 4\,[\bigvee^2 S^1],\quad 2\,[\bigvee^3 S^1],\quad 1\,[\bigvee^4 S^1],\quad 3\,[S^0],\quad 1\,[S^1\sqcup\mathrm{pt}].
\]
Every one of the 56 neighborhood complexes admits an explicit acyclic discrete-Morse matching with no critical cells above dimension \(1\). In particular, the largest possible first Betti number is \(4\), and it is attained by a unique tournament isomorphism class. One representative has out-neighborhoods
\[
\begin{aligned}
N^+(1)&=\{4,6\},&N^+(2)&=\{1,3,6\},&N^+(3)&=\{1,5\},\\
N^+(4)&=\{2,3\},&N^+(5)&=\{1,2,4\},&N^+(6)&=\{3,4,5\}.
\end{aligned}
\]
Its outdegree sequence is \((3,3,3,2,2,2)\), and its out-neighborhood complex is homotopy equivalent to \(\bigvee^4 S^1\).

## Assumptions and scope
A tournament is an orientation of the complete graph. For a digraph \(G\), the out-neighborhood complex \(\overrightarrow{\mathcal N}(G)\) is the simplicial complex whose facets are the out-neighborhoods \(N^+(v)\), with vertex set consisting of vertices of positive indegree. The classification is up to digraph isomorphism and concerns exactly six vertices.

The literature source motivating the computation introduces directed neighborhood complexes, identifies their homotopy type with the directed homomorphism complex from a directed edge, gives the complete five-vertex tournament homology table, and proves vanishing of homology in dimensions at least \(2\) for six-vertex simple digraphs. The present finding supplies the complete six-vertex homotopy census rather than only the higher-dimensional vanishing bound.

## Proof
Encode a labeled six-vertex tournament by a 15-bit word, one bit for each unordered pair \(\{i,j\}\), recording its orientation. There are exactly \(2^{15}=32768\) labeled tournaments. Acting by all \(6!\) vertex permutations partitions these into 56 orbits; the verifier constructs every orbit explicitly and chooses its least bit-mask as canonical representative.

For each canonical representative, the verifier constructs every nonempty face contained in some out-neighborhood. It then searches the \(6!\) vertex orders for a stagewise face matching: at the stage for vertex \(v\), an unmatched face \(\sigma\) not containing \(v\) is paired with \(\sigma\cup\{v\}\) whenever both are still unmatched faces. The resulting matching is independently checked for acyclicity by orienting every Hasse cover downward except matched covers, which are reversed, and performing a complete topological-sort test.

For every one of the 56 canonical tournaments, a verified acyclic matching exists with no critical face of dimension greater than \(1\). Moreover the number of critical vertices equals the number of connected components, so the Morse CW complex is a graph with one vertex in each component. The critical-edge counts therefore determine the homotopy type componentwise. The resulting counts are exactly the seven cases stated above.

The unique class with four critical edges has canonical mask `1332` in the verifier's encoding. Its orbit has 240 labeled tournaments, so its automorphism group has order \(3\). The explicit out-neighborhood list above is reconstructed directly from this representative.

As a regression check against the source literature, the same independent enumeration on five vertices produces 12 tournament isomorphism classes and the reduced-homology-rank distribution reported in the published five-vertex table: eight classes with \((\widetilde\beta_0,\beta_1)=(0,0)\), two with \((0,1)\), one with \((1,0)\), and one with \((1,2)\).

## Verification
Run `python3 verify_tournament_neighborhoods.py t6_neighborhood_census.json`. The verifier reconstructs all labeled tournaments, recomputes the 56 isomorphism orbits, rebuilds every neighborhood complex, searches and checks every discrete-Morse certificate, verifies the complete homotopy distribution, verifies uniqueness of the \(\beta_1=4\) class, and performs the five-vertex literature regression. A successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Dochtermann and Singh introduce directed out- and in-neighborhood complexes and show that each is homotopy equivalent to the directed homomorphism complex from a directed edge. Their Table 1 gives all 12 tournaments on five vertices together with neighborhood-complex homology, while their Theorem 4.12 implies that a six-vertex simple digraph has no reduced homology in dimensions at least \(2\). Their Proposition 5.1 gives explicit tournaments realizing spheres at the minimum vertex count allowed by that vanishing theorem. The inspected paper does not state a six-vertex tournament census, the seven homotopy-type counts above, or the unique \(\beta_1=4\) extremizer.

published-finding corpus searches for six-vertex tournament neighborhood complexes, directed \(\operatorname{Hom}(K_2,T)\) homology, and a six-vertex extension of the published five-vertex table returned no finding that implies or duplicates this census. General six-vertex simplicial-complex torsion censuses and unrelated tournament results do not determine these directed neighborhood complexes.

## Limitations
This is an exact finite classification at order six, not a structural classification for arbitrary tournament order. The uniqueness statement is only for the six-vertex maximum \(\beta_1\). The literature search found no exact prior six-vertex census, but an obscure source not indexed by the searched databases could exist.

## References
1. Anton Dochtermann and Anurag Singh, “Homomorphism complexes, reconfiguration, and homotopy for directed graphs,” arXiv:2108.10948v1, first posted 2021-08-24; European Journal of Combinatorics 110 (2023), 103704, DOI 10.1016/j.ejc.2023.103704.
2. Robin Forman, “Morse theory for cell complexes,” Advances in Mathematics 134 (1998), 90–145.
