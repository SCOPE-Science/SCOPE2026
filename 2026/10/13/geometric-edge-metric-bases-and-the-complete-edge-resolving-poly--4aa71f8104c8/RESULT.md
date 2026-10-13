# Geometric edge-metric bases and the complete edge-resolving polynomial of the Pappus graph

## Finding
Let \(H\) be the eighteen-vertex Pappus graph, realized as the incidence graph of the nine points and nine nonvertical lines of the affine plane over \(\mathbb F_3\). An **edge-resolving set** \(S\subseteq V(H)\) distinguishes every two edges by their vectors of shortest-path distances to the vertices of \(S\), where \(d(v,uw)=\min\{d(v,u),d(v,w)\}\). Write \(\mathcal E_H(z)=\sum_{S\text{ edge-resolving}}z^{|S|}\).

The edge metric dimension is \(\operatorname{edim}(H)=4\). There are exactly \(540\) edge-metric bases, with the geometric characterization in the next section. Their five orbits under the complete \(216\)-element automorphism group have lengths \(54,54,108,108,216\). The complete edge-resolving polynomial is
\[
\begin{aligned}
\mathcal E_H(z)={}&540z^4+5976z^5+17106z^6+31392z^7+43704z^8\\
&+48620z^9+43758z^{10}+31824z^{11}+18564z^{12}\\
&+8568z^{13}+3060z^{14}+816z^{15}+153z^{16}+18z^{17}+z^{18}.
\end{aligned}
\]
Thus precisely \(254100\) of the \(262144\) vertex subsets edge-resolve \(H\). Independently checking ordinary vertex-distance resolution gives \(243834\) vertex-resolving subsets, all of which are edge-resolving. Exactly \(216\) of the \(540\) four-element edge bases are also ordinary metric bases; the other \(324\) distinguish all edges but not all vertices.

## Assumptions and scope
Use the field \(\mathbb F_3=\{0,1,2\}\). The point vertices are \(P_{x,y}\), and line vertices are \(L_{a,b}\), with \(x,y,a,b\in\mathbb F_3\). Adjacency is precisely \(P_{x,y}\sim L_{a,b}\) when \(y=ax+b\). There are \(18\) vertices and \(27\) edges. A **column** means the three points with a fixed first coordinate \(x\); a **slope class** means the three lines with fixed \(a\).

A four-element subset is edge-resolving if and only if exactly one of these mutually exclusive descriptions holds:

1. It consists of four points, with two chosen from each of two distinct columns; or of four lines, with two chosen from each of two distinct slope classes.
2. It contains two points \(p,q\) in distinct columns and two lines \(\ell_1,\ell_2\) of distinct slopes. Writing \(\ell_{pq}\) for the unique retained line through \(p,q\), require \(\ell_1\ne\ell_{pq}\), \(\ell_2\ne\ell_{pq}\), and \(\ell_1\cap\ell_2\notin\ell_{pq}\). All intersections here are intersections of affine lines over \(\mathbb F_3\).

No four-element set having exactly one or exactly three point vertices is edge-resolving. The characterization is for **all** minimum edge-resolving sets, not for arbitrary larger sets. In coordinates ordered \(P_{0,0},P_{0,1},\ldots,P_{2,2},L_{0,0},L_{0,1},\ldots,L_{2,2}\), the orbit representatives and lengths are provided in `basis_orbits.csv`.

## Proof
**Distance and finite-decision lemma.** The graph distances between distinct point vertices are \(2\) when their columns differ and \(4\) otherwise. The analogous distances between distinct line vertices are \(2\) for different slope classes and \(4\) otherwise. A point and line have distance \(1\) if incident, and \(3\) if not. These assertions follow by constructing length-two paths through the unique retained line of two points in different columns (or their dual), and length-four paths in the other same-type cases. Hence for every incident point-line pair \(e=P_{x,y}L_{a,b}\), the distance to an arbitrary landmark \(v\) is exactly the minimum of its two endpoint distances, which are given by these explicit rules. In particular, all edge-distance signatures are determined without numerical approximation.

For every pair of distinct edges \(e,f\), let \(B(e,f)=\{v\in V(H):d(v,e)\ne d(v,f)\}\). A subset \(S\) is edge-resolving **if and only if** it meets every \(B(e,f)\). The \(\binom{27}{2}=351\) edge pairs produce precisely \(198\) distinct nonempty separation masks. The supplied standalone verifier builds these masks from the distance formulas, independently computes breadth-first distances, and tests all \(\binom{18}{4}=3060\) four-element sets against the stated coordinate-geometric characterization. It asserts exact equivalence for each of the \(3060\) cases, not a sample. It separately checks all \(\binom{18}{0}+\cdots+\binom{18}{3}=988\) smaller sets and finds no edge-resolving set. This is a finite exhaustive proof that the characterization is exact and the minimum cannot be below four.

**Counting the characterized bases.** Four points, or dually four lines, can be chosen in \(\binom32\binom32^2=27\) ways. For a mixed base, first choose its point pair in distinct columns, giving \(\binom32\cdot 3^2=27\) choices. Once these points and their retained joining line are fixed, choose two lines of distinct slopes: \(\binom32\cdot 3^2=27\) possibilities. Exactly six pairs contain the joining line. Among the remaining pairs, precisely one pair has its two lines meet at each of the three points of the joining line; these three disjoint pairs are forbidden. Thus \(27-6-3=18\) line pairs work for each point pair, giving \(27\cdot18=486\) mixed bases. The total is \(27+27+486=540\).

**Polynomial and the vertex/edge comparison.** The same separation-mask test enumerates all \(2^{18}=262144\) subsets, binned by cardinality, and independently compares the result with the direct all-edge-signatures predicate on every subset. A separately implemented C++ breadth-first search and direct-signatures enumerator reproduces each coefficient. Replacing edge signatures by vertex signatures independently shows \(243834\) ordinary resolving subsets, all lying among the \(254100\) edge-resolving subsets, with exactly \(216\) common four-element bases. Finite exhaustive loops in the supplied sources cover every relevant subset and have no stochastic or heuristic branch.

**Automorphisms and orbits.** Every part-preserving automorphism permutes the three point columns. Every permutation of \(\mathbb F_3\) is affine; preserving the unique retained line through points from distinct columns forces the multipliers of the three within-column affine permutations to agree. Hence there are at most \(3!\cdot2\cdot3^2=108\) part-preserving automorphisms. All \(108\) are realized by
\[
(x,y)\longmapsto (\alpha x+\beta,\gamma x+\delta y+\varepsilon),
\qquad \alpha,\delta\in\mathbb F_3^\times,\quad \beta,\gamma,\varepsilon\in\mathbb F_3,
\]
with the corresponding action on line equations. The involutory incidence duality interchanges \(P_{x,y}\) with \(L_{x,-y}\). Since the incidence graph is connected bipartite, every automorphism either preserves or exchanges its two parts. Therefore the full group has order \(216\). Applying these \(216\) explicitly constructed and edge-preserving permutations to every base partitions the \(540\) sets into orbits of lengths \(54,216,108,108,54\); the full representatives are in `basis_orbits.csv`. Both the edge-preservation and exact orbit unions are asserted in `verify.py`.

## Verification
Run `python3 verify.py` using Python \(\ge 3.8\), and independently compile and run `verify_independent.cpp` with a C++17 compiler. Both use only standard libraries. The Python checker verifies the distance lemma against breadth-first paths, the exact geometric criterion for every four-subset, all masks versus all direct edge signatures for every one of the \(262144\) subsets, every polynomial coefficient, the full explicit automorphism action, and the five complete base orbits. The C++ checker independently builds the graph and distances and separately enumerates edge and vertex signatures for the entire power set. See `VERIFICATION.md` for the observed checks and their boundaries.

## Relationship to prior work
Kelenc, Tratnik, and Yero introduced the vertex-to-edge distance metric and edge metric dimension, deriving general comparisons and formulas for other graph families (arXiv:1602.00291v1, January 31, 2016). Their full paper does not state this Pappus census. Bailey's classification of the ordinary **vertex** metric dimensions of small distance-regular graphs reports value \(4\) for the Pappus graph (arXiv:1312.4973v1, December 17, 2013, Table 1); that scalar vertex invariant does not determine the edge-resolving polynomial or the five edge-base symmetry types. Bartoli, Héger, Kiss, and Takáts study metric dimension in general biaffine planes, defining the exact partial-plane model used here, but their result is about vertex-to-vertex resolution and their quantitative biaffine bounds begin at order \(q\ge4\), so they neither imply nor tabulate this order-three edge census. This result makes the distinction quantitative: \(540\) edge bases versus \(216\) ordinary metric bases.

## Limitations
All assertions concern this explicit eighteen-vertex graph only; nothing is inferred for larger affine planes or all cubic graphs. Exact finite enumeration proves the given finite claims, not their historical priority. An equivalent earlier enumeration under a different name or in an unindexed table cannot be excluded without further bibliographic investigation. Orbit statements use the specified graph automorphism action, not color or landmark relabeling.

## References
1. A. Kelenc, N. Tratnik, and I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291v1, publicly submitted January 31, 2016. https://arxiv.org/html/1602.00291v1
2. R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, arXiv:1312.4973v1, publicly submitted December 17, 2013, especially Table 1. https://arxiv.org/html/1312.4973v1
3. D. Bartoli, T. Héger, G. Kiss, and M. Takáts, *On the metric dimension of affine planes, biaffine planes and generalized quadrangles*, arXiv:1706.06583v1, publicly submitted June 20, 2017. https://arxiv.org/html/1706.06583v1
