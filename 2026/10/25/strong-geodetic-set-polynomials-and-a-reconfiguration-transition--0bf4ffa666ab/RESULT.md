# Strong geodetic-set polynomials and a reconfiguration transition in complete prisms

## Finding
Let \(H_n=K_n\square K_2\) for an integer \(n\ge2\). A set \(S\subseteq V(H_n)\) is **strong geodetic** if one can select exactly one shortest path between each unordered pair of distinct vertices of \(S\) so that their union covers all vertices. Write the layers as \(a_1,\ldots,a_n\) and \(b_1,\ldots,b_n\), with matching edges \(a_ib_i\). A *column* is \(\{a_i,b_i\}\). Put \(P=\{i:a_i\in S,b_i\notin S\}\), \(Q=\{i:b_i\in S,a_i\notin S\}\), and \(W=\{i:a_i,b_i\in S\}\).

**Classification.** A set \(S\) is strong geodetic if and only if every column meets \(S\), and either \(W\ne\varnothing\), or \(W=\varnothing\) and \(|P|,|Q|\ge2\).

Let \(F_n(z)=\sum_{S\text{ strong geodetic}}z^{|S|}\) and \(M_n(z)=\sum_{S\text{ inclusion-minimal strong geodetic}}z^{|S|}\). Then
\[
F_n(z)=\begin{cases}
z^n\big((2+z)^n-2^n\big),&n=2,3,\\
z^n\big((2+z)^n-2n-2\big),&n\ge4,
\end{cases}
\]
and
\[
M_n(z)=\begin{cases}
n2^{n-1}z^{n+1},&n=2,3,\\
(2^n-2n-2)z^n+2nz^{n+1},&n\ge4.
\end{cases}
\]
In particular, the strong geodetic number is \(n+1\) for \(n=2,3\) and \(n\) for \(n\ge4\); the **strong upper geodetic number** (largest size of an inclusion-minimal strong geodetic set) is \(n+1\) for all \(n\ge2\). For \(n\ge4\) there are exactly \(2^n-2\) inclusion-minimal strong geodetic sets, of precisely the two displayed sizes.

For \(n\ge4\), define the minimum-set **token-jumping graph** to have one vertex for each minimum strong geodetic set, with an edge when one vertex of the underlying prism can be exchanged for one unselected vertex while maintaining the minimum-set property. For \(n=4\) this graph is edgeless on six vertices. For every \(n\ge5\) it is isomorphic to the subgraph of the \(n\)-cube induced by Boolean vectors of Hamming weights \(2,3,\ldots,n-2\); it is connected, the inclusion is isometric in Hamming distance, and its diameter is exactly \(n\).

## Assumptions and scope
All graphs are finite simple undirected Cartesian products with the standard vertex-geodetic definition (not the stronger requirement of covering every edge). Selected pairs are distinguished by their endpoints; for each pair only one geodesic may be chosen. The size polynomials count **labeled vertex subsets**, not their automorphism orbits. The minimality notion is inclusion-minimal strong geodetic, not minimum cardinality. The reconfiguration graph permits arbitrary token jumps, but always keeps the same cardinality and remains inside the family of minimum strong geodetic sets.

## Proof
**1. Shortest paths and required columns.** Distances within either clique, and along a matching edge, are one. Between \(a_i\) and \(b_j\), where \(i\ne j\), distance is two, with exactly the geodesics \(a_i,a_j,b_j\) and \(a_i,b_i,b_j\). Thus any unselected \(a_i\) can only occur internally on a selected-pair geodesic if \(b_i\in S\); symmetrically, an unselected \(b_i\) requires \(a_i\in S\). Consequently no column may be empty.

**2. One full column suffices.** If \(w\in W\), cover each unselected \(b_i\) for \(i\in P\) by the geodesic \(a_i,b_i,b_w\), and cover each unselected \(a_j\) for \(j\in Q\) by \(a_w,a_j,b_j\). Because \(i,j\ne w\), all these paths use distinct selected endpoint pairs: the former are indexed by \((a_i,b_w)\), the latter by \((a_w,b_j)\). Choose arbitrary geodesics for all remaining pairs. Every vertex is covered.

**3. No full column.** If \(W=\varnothing\), the selected vertices consist of the \(a_i\) with \(i\in P\) and the \(b_j\) with \(j\in Q\), where \(P\sqcup Q=[n]\). Every missing vertex lies on a geodesic whose endpoints are one vertex from each chosen layer. There are only \(|P||Q|\) such endpoint pairs, and each can cover at most one unselected vertex. If \(|P|\le1\) or \(|Q|\le1\), then \(|P||Q|<|P|+|Q|=n\), so coverage is impossible. Conversely, suppose \(|P|,|Q|\ge2\). Choose distinct indices \(i_1,i_2\in P\) and \(j_1,j_2\in Q\). Assign pair \((a_{i_1},b_{j_1})\) to missing \(b_{i_1}\), pair \((a_{i_2},b_{j_2})\) to missing \(b_{i_2}\), and each remaining row pair \((a_i,b_{j_1})\) to missing \(b_i\). Assign \((a_{i_2},b_{j_1})\) to missing \(a_{j_1}\), \((a_{i_1},b_{j_2})\) to missing \(a_{j_2}\), and each remaining column pair \((a_{i_1},b_j)\) to missing \(a_j\). No pair is used twice. The selected geodesics thus cover every missing vertex. This proves the classification.

**4. Enumerators and minimality.** If there is at least one full column, each column is independently of type \(a\)-only (weight \(z\)), \(b\)-only (weight \(z\)), or full (weight \(z^2\)); these configurations contribute \((2z+z^2)^n-(2z)^n\). Configurations with no full column contribute \((2^n-2n-2)z^n\) when \(n\ge4\), and none when \(n=2,3\). This proves \(F_n\).

Every feasible no-full-column set is inclusion-minimal because deleting a chosen vertex empties its column. A set with at least two full columns is not minimal: deleting one vertex of one such column leaves another full column. For exactly one full column \(w\), write \(p=|P|\), \(q=|Q|\), so \(p+q=n-1\). Deleting \(a_w\) gives a feasible no-full-column set exactly when \(p\ge2\) and \(q\ge1\); deleting \(b_w\) gives one exactly when \(p\ge1\) and \(q\ge2\). Deleting any singly selected vertex empties a column. Therefore for \(n\ge4\), the inclusion-minimal one-full-column sets are exactly those with \(p=0\) or \(q=0\), numbering \(2n\), each of size \(n+1\). For \(n=2,3\), every one-full-column configuration is minimal, numbering \(n2^{n-1}\), again of size \(n+1\). This proves \(M_n\) and the extremal parameters.

**5. Reconfiguration.** For \(n\ge4\), a minimum set is exactly a choice of one vertex in every column, with at least two selected vertices in each layer. Encode it by a binary vector of length \(n\): choose \(1\) when the upper-layer vertex is selected. A token jump between two minimum sets cannot change columns, because then one column would be empty; therefore it flips exactly one bit. Thus the graph is the stated rank-selected cube. When \(n=4\), only weight two is permitted and no one-bit flip stays in that layer; there are \(\binom42=6\) isolated vertices. When \(n\ge5\), any two allowed vectors can be connected by flipping only bits on which they disagree, ordering flips to keep the weight in \([2,n-2]\): at the lower boundary do an available addition, and at the upper boundary do an available deletion. Such a flip always exists unless the target is already reached, since otherwise its permitted final weight would lie outside the interval. Hence graph distance equals Hamming distance. Complementary allowed vectors of weights two and \(n-2\) have Hamming distance \(n\), the maximum possible, proving the diameter.

## Verification
The accompanying standalone program `verify.py` constructs \(H_n\) directly, computes all-pairs distances by breadth-first search, and checks strong geodeticity without using the structural classification. It forms a bipartite matching problem between unselected vertices and endpoint pairs: in a diameter-two graph every admissible pair-geodesic can supply at most one unselected internal vertex. The code exhaustively tests every vertex subset for \(n=2,3,4,5,6,7\), compares the exact classification, size polynomial and minimal-set counts, and checks token-jumping components and distances for \(n=4,5,6,7\). There are exactly \(16+64+256+1024+4096+16384=21,840\) evaluated subsets; all tests passed. Finite experiments corroborate but do not replace the proof for all \(n\).

## Relationship to prior work
Iršič and Klavžar established the scalar strong geodetic number of arbitrary products \(K_m\square K_n\) in 2017 (Theorem 3.3). In particular, the minimum cardinalities asserted above were already known; priority for them is **not** claimed. Infanta and Xavier introduced the strong upper geodetic number and studied its general theory in 2021, without the displayed complete-prism distribution in the inspected results. Klavžar and Zmazek studied the **edge-covering** strong geodetic problem on \(P_m\square K_n\), including the same complete-prism family; edge-geodesic coverage is a different predicate and does not count vertex-geodetic subsets. A separately indexed theorem on mixed metric bases for \(K_n\square K_2\) obtains the same minimum transversal pattern for \(n\ge5\), but studies vertex-edge distance signatures rather than fixed shortest-path vertex coverage; this matching minimum-count pattern is acknowledged, and the claim of newness is restricted to the all-set classification, inclusion-minimal spectrum, and associated strong-geodetic reconfiguration description.

## Limitations
No generalization to more than two clique layers or to edge-geodetic coverage is asserted. The result is a mathematical proof with independent brute-force computational corroboration only for \(2\le n\le7\). An exhaustive literature-priority guarantee is not possible: other forms of the result may appear in unindexed work, and the separately indexed mixed-metric-base result could have additional unpublished implications. No independent expert audit or formal proof-assistant certification has been performed.

## References
1. V. Iršič and S. Klavžar, *Strong geodetic problem on Cartesian products of graphs*, arXiv:1708.02414 (first public version August 8, 2017), RAIRO Operations Research 52 (2018), 205–216; Theorem 3.3. https://arxiv.org/abs/1708.02414
2. L. G. Bino Infanta and D. Antony Xavier, *Strong Upper Geodetic Number of Graphs*, Communications in Mathematics and Applications 12(3) (2021), 737–748. https://doi.org/10.26713/cma.v12i3.1597
3. S. Klavžar and E. Zmazek, *Strong Edge Geodetic Problem on Complete Multipartite Graphs and Some Extremal Graphs for the Problem*, arXiv:2312.11199 (2023), Bulletin of the Iranian Mathematical Society 50 (2024), article 13. https://doi.org/10.1007/s41980-023-00849-6
4. B. Bergougnoux, O. Defrain, and F. Mc Inerney, *Enumerating minimal solution sets for metric graph problems*, arXiv:2309.17419 (2023), for general background on enumeration of minimal metric sets. https://arxiv.org/abs/2309.17419
