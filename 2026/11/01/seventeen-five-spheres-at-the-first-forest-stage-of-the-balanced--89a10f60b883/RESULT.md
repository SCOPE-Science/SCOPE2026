# Seventeen five-spheres at the first forest stage of the balanced triple categorical product

## Finding
Let \(G=K_2\times K_3\times K_3\) be the categorical graph product of three complete graphs. Its first forest-filtration complex has the integral homotopy type
\[
\mathcal F_1(G)\simeq\bigvee^{17}S^5.
\]
Thus \(\widetilde H_5(\mathcal F_1(G);\mathbb Z)\cong\mathbb Z^{17}\) and all other reduced integral homology groups vanish. The claim is an integral homotopy equivalence, not merely a mod-two computation.

## Assumptions and scope
All graphs are finite, simple and undirected, and all simplicial complexes are interpreted as their geometric realizations. Identify the vertex set with
\[
V(G)=\{(a,i,j):a\in\{0,1\},\ i,j\in\{0,1,2\}\}.
\]
Two vertices are adjacent if and only if all three coordinates are unequal. There are exactly 18 vertices, 36 edges, and every vertex has degree four. For any vertex set \(U\subseteq V(G)\), the set \(U\) is a face of \(\mathcal F_1(G)\) precisely when every vertex of the *induced* subgraph \(G[U]\) has degree at most one. This also ensures \(G[U]\) is a forest. It is the two-independence complex \(\operatorname{Ind}_2(G)\), not the ordinary independence complex or the edge-matching complex. The empty face is included in the abstract complex but omitted from the nonempty face-poset matching.

## Proof
Number the vertices lexicographically, \(v=9a+3i+j\), with \(0\leq a\leq1\) and \(0\leq i,j\leq2\). Represent a face by the 18-bit integer whose set bits are its vertices. For each \(v\), let \(N(v)\) be its four graph neighbors. The face predicate is exactly
\[
U\in\mathcal F_1(G)\quad\Longleftrightarrow\quad
\lvert U\cap N(v)\rvert\leq1\quad\text{for every }v\in U.
\]
Equivalently, no set of three chosen vertices may contain a center together with two distinct neighbors of that center. There are exactly 108 such forbidden three-vertex subsets. The verifier enumerates every one of the \(2^{18}\) subsets and proves the two predicates define *identical* face sets, consisting of 8,564 nonempty faces.

For a completely specified matching, initialize the set of unmatched faces to all 8,564 nonempty faces. For pivot vertex \(v=0,1,\ldots,17\), scan all faces in increasing integer bit-mask order and pair each still-unmatched face \(\sigma\) without \(v\) with \(\sigma\cup\{v\}\), provided the latter is still unmatched. Remove both members of each pair before continuing. This gives 4,273 pairs, leaving precisely one critical zero-simplex and seventeen critical five-simplices. Both the exact list and the construction of all matching pairs are recomputed from first principles by the accompanying standalone source file `verify.py`.

To verify acyclicity, form the Hasse diagram of the nonempty face poset with a directed edge for every codimension-one incidence. Direct an incidence from its smaller face to its larger face exactly if it is a matched pair; direct all unmatched incidences from larger to smaller. The verifier explicitly constructs all 42,786 incidences and topologically sorts this directed graph: all 8,564 faces are visited. Therefore there is no directed cycle, so the matching is acyclic. By the discrete-Morse theorem, the complex has a CW model with one zero-cell, seventeen five-cells, and no other cells. Every five-cell attaches to the single zero-cell, hence this CW model is a wedge of seventeen five-spheres. This proves the stated homotopy equivalence *over the integers*.

## Verification
Run `python3 verify.py` from a directory containing that file using Python 3.8 or newer; no nonstandard package or network connection is needed. The complete output is included as `verification_output.txt`. The source asserts the equality of two independent face predicates, all graph parameters, the critical-cell counts, a topological-sort certificate over the complete directed Hasse graph, and an independent exact mod-two simplicial boundary calculation. The f-vector of nonempty faces, indexed by dimension zero through eight, is
\[
(18,153,708,1890,2826,2184,720,63,2).
\]
The independent binary chain computation gives reduced mod-two homology of rank 17 in dimension five and zero in all other dimensions. It is a consistency check; the acyclic Morse matching is the actual integral homotopy proof. The complex has dimension eight despite collapsing homotopically to dimension five.

## Relationship to prior work
Carnero Bravo, *The Forest Filtration of a Graph* (first submitted July 25, 2023), introduces \(\mathcal F_d\), treats two-factor categorical complete-graph products, computes the case \(K_2\times K_2\times K_n\) in Corollary 43, and then asks for the remaining triple-product forest-filtration homotopy types in Question 44. Neither the two-factor results nor that corollary covers this balanced case with both remaining factors of order three. Antolín Camarena and Carnero Bravo (2023) prove a result about \(\mathcal F_0=\operatorname{Ind}\) of triple products, a different stage: the already known answer for this graph is \(\mathcal F_0(G)\simeq\bigvee^{14}S^3\), which does not imply the present answer. Deshpande and Singh (2020/2021) classify higher-independence complexes of complete multipartite graphs, paths, cycles, fully whiskered graphs and perfect rooted trees. This connected 18-vertex four-regular bipartite graph is not complete multipartite, nor one of those specified classes.

## Limitations
The theorem concerns this single graph and the first forest level only. It does not classify \(\mathcal F_d(K_2\times K_m\times K_n)\) for general parameters or determine inclusion-induced persistent maps. An unidentified equivalent earlier computation in inaccessible or unindexed sources remains possible. The proof is a finite exhaustive combinatorial certificate, not a universal symbolic parameter formula. Independent external review has not been performed.

## References
- A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, §§3–4.2.2, Corollary 43 and Question 44, first public July 25, 2023. https://arxiv.org/abs/2307.13271
- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, §4 (2023). https://arxiv.org/abs/2307.12401
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, Theorems 3.5, 3.8, 4.6 and 5.6 (2020/2021). https://arxiv.org/abs/2001.05448
