# Anti-forcing spectrum and two-factor types of the Möbius–Kantor graph

## Finding
For the Möbius–Kantor graph \(G=\operatorname{GP}(8,3)\), there are exactly 33 perfect matchings, and their anti-forcing polynomial is
\[
A_G(z)=\sum_{M\text{ perfect}}z^{\operatorname{af}(G,M)}=3z^4+30z^5.
\]
More precisely, every matching is characterized by the cycle lengths of its complementary two-factor as follows:

| Complementary cycle lengths | Number of perfect matchings | Anti-forcing number | Automorphism orbit size |
|:--|--:|--:|--:|
| \((8,8)\) | 3 | 4 | 3 |
| \((16)\) | 6 | 5 | 6 |
| \((6,10)\) | 24 | 5 | 24 |

The automorphism group of \(G\) has order 96. Moreover, for every perfect matching \(M\), the anti-forcing number equals the largest number of \(M\)-alternating cycles that pairwise share no edges outside \(M\). This equality is asserted only for this graph, not as a general nonplanar minimax theorem.

## Assumptions and scope
The labeled graph has vertices \(u_i,v_i\) with \(i\in\mathbb Z/8\mathbb Z\). Its 24 edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), for each index \(i\). These define a connected, simple, cubic bipartite graph. A perfect matching \(M\) covers each vertex exactly once. Its anti-forcing number \(\operatorname{af}(G,M)\) is the minimum cardinality of a set \(F\subseteq E(G)\setminus M\) such that \(M\) is the unique perfect matching of \(G-F\). The complement of a perfect matching is a 2-regular spanning subgraph; its cycle-length multiset is well defined.

## Proof
First, enumerate all matchings by recursively taking the least uncovered vertex and matching it to each currently uncovered neighbor. Every matching is reached once. The attached standalone verifier uses this recursion and independently computes the permanent of the \(8\times8\) bipartite adjacency matrix by an exact subset recurrence. Both methods yield 33 matchings. For each matching, remove its eight edges, traverse the remaining degree-two graph, and obtain exactly the cycle types and multiplicities in the table.

For an arbitrary perfect matching \(M\), choose its eight edges to label eight contracted vertices, with the endpoints organized according to the bipartition \(L\sqcup R\). For each nonmatching edge joining the left endpoint of matching edge \(i\) to the right endpoint of matching edge \(j\), insert a directed arc \(i\to j\). A directed cycle of these arcs is exactly an \(M\)-alternating cycle before contraction. Therefore an edge set outside \(M\) makes \(M\) unique exactly when its corresponding arcs meet every directed cycle.

Let \(D\) be the resulting eight-vertex, sixteen-arc digraph. For a vertex subset \(S\), write \(f(S)\) for the minimum number of backward arcs among all total orders of \(S\), with \(f(\varnothing)=0\). Placing \(i\in S\) last gives the exact recurrence
\[
f(S)=\min_{i\in S}\left[f(S\setminus\{i\})+\bigl|\{(i,j)\in E(D):j\in S\setminus\{i\}\}\bigr|\right].
\]
A minimum feedback-arc set is exactly a minimum set of backward arcs for some ordering: deleting all backward arcs leaves a directed acyclic graph, and an optimal deletion has a topological ordering of what remains. Thus \(f(V(D))=\operatorname{af}(G,M)\). The recurrence is evaluated for every one of the 256 subsets and each of the 33 matchings. It gives anti-forcing value 4 for the three \((8,8)\) matchings and 5 otherwise.

To verify the orbit refinement, the supplied verifier generates *all* adjacency-preserving bijections by exhaustive backtracking on 16 vertices. It finds exactly 96 automorphisms and proves that their actions on the 33 matchings give three orbits of sizes 3, 6, and 24. On one representative of each orbit, a second exact method enumerates deleted subsets of the 16 nonmatching arcs in increasing size and tests acyclicity directly. Its minima are 4, 5, and 5. Finally, all simple directed cycles are enumerated on each orbit representative and an exhaustive disjoint-arc packing recurrence finds 4, 5, and 5 cycles, respectively. Their edge disjointness establishes matching lower bounds; the deletion sets establish upper bounds. Automorphism invariance transfers both conclusions to every matching in the corresponding orbit.

## Verification
Run `python3 mk_antiforcing_verify.py` using Python 3 with no third-party dependencies. The script checks the graph size and bipartition, compares independent perfect-matching enumerations, calculates all 33 anti-forcing values by subset dynamic programming, enumerates the 96 automorphisms and their matching orbits, tests independently constructed minimum feedback-arc sets, and produces packings of edge-disjoint directed cycles. The terminal line is `VERIFY_OK`. All counts are exhaustive over the stated finite graph; no random sampling is used.

## Relationship to prior work
Lei, Yeh and Zhang (2014, arXiv:1406.3796) introduced the fixed-matching anti-forcing number and the alternating-cycle obstruction, including a minimax theorem for **plane** bipartite graphs. Deng and Zhang (2016, arXiv:1607.05392) studied general cyclomatic upper bounds, extremal anti-forcing configurations and even polygonal chains. Neither cited result gives the three-class anti-forcing census above: in particular the cyclomatic bound here is 9, whereas the computed maximum is 5. A 2025 matching-polynomial study of the Möbius–Kantor graph reports 33 perfect matchings, agreeing with our independent count; that aggregate count does not determine the anti-forcing distribution. The Möbius–Kantor graph is not planar: a connected planar bipartite graph of girth at least six with sixteen vertices has at most 21 edges, while this graph has 24 and girth six. The plane-bipartite minimax theorem therefore cannot be invoked directly, although its equality is verified here by finite cycle packings.

## Limitations
This is an exact classification for one finite graph. The computations do not imply analogous formulas for other generalized Petersen graphs, nonplanar bipartite graphs, or all cubic symmetric graphs. The 2025 matching-polynomial full text was not available for comprehensive inspection in the literature comparison; possible unindexed or inaccessible prior enumerations of these anti-forcing values remain an originality risk. External independent validation has not been conducted.

## References
1. H. Lei, Y.-N. Yeh and H. Zhang, *Anti-forcing numbers of perfect matchings of graphs*, arXiv:1406.3796, first publicly submitted 2014-06-15. https://arxiv.org/abs/1406.3796
2. K. Deng and H. Zhang, *Extremal anti-forcing numbers of perfect matchings of graphs*, arXiv:1607.05392, first submitted 2016-07-19. https://arxiv.org/html/1607.05392v1
3. *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, *Symmetry* **17** (2025), article 133, doi:10.3390/sym17010133. https://doi.org/10.3390/sym17010133
