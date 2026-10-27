# The fourteen \(K_5\) exchange components of minimum Heawood feedback vertex sets

## Finding
Let \(H\) be the Heawood graph, the bipartite point-line incidence graph of the Fano projective plane. A feedback vertex set (FVS) \(S\subseteq V(H)\) is a vertex set for which \(H-S\) is acyclic. The exchange graph \(\mathcal C_k(H)\) has as vertices the FVSs of size \(k\), with two adjacent when their symmetric difference has size two.

**Theorem.** The feedback vertex number is \(\tau(H)=4\). There are exactly \(70\) minimum feedback vertex sets, and their exchange graph is
\[
\mathcal C_4(H)\cong\bigsqcup_{i=1}^{14}K_5.
\]

More explicitly, for every line \(L\) of the Fano plane define \(U_L=\{L\}\cup(P\setminus L)\), consisting of the line-vertex and its four nonincident point-vertices. For every point \(p\), let \(U_p=\{p\}\cup(\mathcal L\setminus\mathcal L(p))\), consisting of the point-vertex and its four nonincident line-vertices. The minimum FVSs are **exactly** the \(4\)-subsets of these fourteen \(5\)-element sets. For each \(U\), the five such FVSs form one exchange component \(K_5\); no exchange crosses between distinct \(U\)'s. In particular, the exchange graph has \(140\) edges and is disconnected even though \(H\) is a \(3\)-connected cubic bipartite graph.

## Assumptions and scope
The Fano plane has seven points \(P\), seven lines \(\mathcal L\), three points on each line, three lines through each point, a unique line through each pair of points, and a unique intersection point of each pair of lines. The Heawood graph has vertices \(P\sqcup\mathcal L\) and an edge \(pL\) precisely when \(p\in L\); it has \(14\) vertices and \(21\) edges. A forest is an undirected graph containing no cycle, not necessarily connected. All exchanges replace exactly one selected vertex by one unselected vertex and maintain cardinality four; no auxiliary vertices, token slides, or temporary extra tokens are allowed. The claim concerns this graph and this exchange operation, not all cubic graphs.

## Proof
**1. Lower bound and independence.** For a selected set \(S\) of \(k\) vertices, the remaining induced graph has \(14-k\) vertices and exactly \(21-3k+e_H(S)\) edges, where \(e_H(S)\) is the number of edges with both endpoints in \(S\). An acyclic graph on \(14-k\) vertices has at most \(13-k\) edges. Thus a feedback set must satisfy \(21-3k+e_H(S)\le 13-k\), equivalently \(2k\ge 8+e_H(S)\). Therefore \(k\ge4\). If \(k=4\), necessarily \(e_H(S)=0\), and the remaining graph, with ten vertices and nine edges, must be one tree. In particular each minimum FVS is independent.

**2. Classification by bipartition.** Write \(a=|S\cap P|\) and \(b=|S\cap\mathcal L|\), so \(a+b=4\). For \((a,b)=(4,0)\), the three retained points induce a cycle with their joining lines exactly when they are noncollinear: noncollinearity gives a six-cycle; when collinear, every retained line meets the three points in at most one point except their common line, so the retained incidence graph is a forest. Thus the selected four points must be \(P\setminus L\) for a unique line \(L\), and then \(S\subseteq U_L\).

For \((a,b)=(3,1)\), independence requires the selected line \(L\) to avoid all three selected points. All three points therefore lie among the four points off \(L\), and \(S\) is a four-subset of \(U_L\). Conversely, selecting \(L\) and any three of its four nonincident points leaves four point-vertices: the three on \(L\) and one off it. Removing the line-vertex \(L\) deletes all pair connections between the three points on \(L\); the remaining pair-incidence graph on retained points is a three-edge star centered at the off-line point. Every other retained line-vertex has degree at most one into retained points. Hence the entire retained graph is a tree and \(S\) is an FVS.

The mixed case \((a,b)=(2,2)\) is impossible. If the two selected points are \(p,q\), the two selected lines must be precisely the two lines avoiding both \(p\) and \(q\) (there are seven lines, of which exactly five meet \(p\) or \(q\)). Let \(pq\) denote the unique line through them. On the four other points off \(pq\), the two non-\(pq\) lines through \(p\) define a perfect matching of two point pairs; the two non-\(pq\) lines through \(q\) define a different perfect matching. These matchings are edge-disjoint: any common pair would lie on two lines, contrary to the uniqueness of the line through two points. The union is a four-cycle, which lifts to an eight-cycle in the retained incidence graph. Thus no such selection breaks every cycle.

The cases \((1,3)\) and \((0,4)\) follow from the dual Fano-plane argument, interchanging points and lines. They are exactly the four-subsets of \(U_p\) for points \(p\). This proves both directions of the classification and, since the constructed sets exist, also \(\tau(H)=4\).

**3. Enumeration and exchanges.** There are seven line-based families \(U_L\) and seven point-based dual families \(U_p\), each of size five. For distinct lines \(L,M\), their nonincident-point sets intersect in exactly two points because \(|L\cup M|=5\); the line-vertices are distinct, so \(|U_L\cap U_M|=2\). Dually \(|U_p\cap U_q|=2\) for distinct points. A four-subset from a line-based family contains at least three point-vertices and at most one line-vertex, while any four-subset from a point-based family contains at most one point-vertex and at least three line-vertices; such two sets intersect in at most two vertices. Therefore a four-subset belongs to a unique one of the fourteen families, and two minimum FVSs from different families intersect in at most two vertices. They cannot be adjacent, since one-vertex exchange of four-subsets requires an intersection of exactly three vertices. Within a given five-element \(U\), any two distinct four-subsets intersect in three elements and are adjacent. Each family therefore contributes exactly a \(K_5\) component, and the components have no cross-edges. The total counts are \(14\cdot5=70\) vertices and \(14\binom52=140\) exchange edges.

## Verification
The algebraic proof above establishes the theorem without computational assumptions. Two independently implemented exhaustive checkers are also supplied. `verify_fano_vectors.py` constructs the incidence graph via nonzero binary three-vectors and their dot-product relation, enumerates all vertex subsets of size at most four, checks forests by component-edge counts, and compares the entire minimum-set family to the stated geometric classification. It also checks three-vertex-connectivity by deleting every set of fewer than three vertices. `verify_cyclic_incidence.py` instead uses the cyclic Fano difference set \(\{0,1,3\}\) and a disjoint-set union cycle test; it independently enumerates all relevant subsets, tests the classification, and constructs exchange edges and components. Both run using only the Python standard library:

```
python verify_fano_vectors.py
python verify_cyclic_incidence.py
```

Their complete recorded outputs are included as `vector_check_output.txt` and `cyclic_check_output.txt`. Both agree on the minimum size \(4\), count \(70\), fourteen size-five components and \(140\) exchange edges. Exhaustive tests here serve as corroboration, not as an extrapolation to an infinite graph family.

## Relationship to prior work
The 2015 presentation of the Heawood graph via Fano point-line incidence supplies the graph construction and its elementary geometry [1], not a classification of feedback vertex sets. Bousquet, Hommelsheim, Kobayashi, Mühlenthaler and Suzuki study the same one-vertex FVS exchange operation and prove broad connectivity results for restricted subcubic graphs, alongside disconnected examples for odd feedback numbers at least five [2]. Their displayed results do not establish the even-size-four Heawood classification or the fourteen component geometry; the indexed introduction and theorem statements, rather than complete publisher full text, were available for comparison. Nedela and Škoviera discuss decycling sets of cubic graphs and existence results, not the complete configuration enumeration visible in the accessible abstract [3]. The claim is a complete finite classification and an explicit small even-feedback-number disconnected exchange example; it does not claim the minimum cardinality bound or general FVS reconfiguration framework as new.

## Limitations
The theorem is graph-specific, and no extension to all Fano-derived designs, all cubic bipartite graphs, or even all Heawood-graph operations is established. The graph is nonplanar, so the planar/subcubic positive reconfiguration theorem does not contradict the result. The accessible primary excerpts do not amount to exhaustive full-text literature clearance: an unindexed equivalent calculation, especially in an appendix or computational table, remains possible. Publication priority and independent external verification are not asserted.

## References
[1] John Baez, “Heawood Graph”, Visual Insight, American Mathematical Society, 1 August 2015. https://blogs.ams.org/visualinsight/2015/08/01/heawood-graph/

[2] N. Bousquet, F. Hommelsheim, Y. Kobayashi, M. Mühlenthaler, A. Suzuki, “Feedback vertex set reconfiguration in planar graphs”, Theoretical Computer Science 979 (2023), 114188. https://doi.org/10.1016/j.tcs.2023.114188

[3] R. Nedela and M. Škoviera, “Cyclic connectivity, edge-elimination, and the twisted Isaacs graphs”, Journal of Combinatorial Theory Series B 155 (2022), 17–44. https://doi.org/10.1016/j.jctb.2022.01.007
