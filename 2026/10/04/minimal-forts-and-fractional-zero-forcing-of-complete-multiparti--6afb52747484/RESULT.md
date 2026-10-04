# Minimal forts and fractional zero forcing of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph. Let \(q\) be the number of singleton parts and let \(m_1,\ldots,m_p\ge2\) be the sizes of the non-singleton parts. A subset \(F\subseteq V(G)\) is a minimal fort if and only if it is one of the following: (i) two vertices from one non-singleton part; (ii) two singleton vertices; or (iii) three vertices from three distinct parts, with at most one of those parts singleton. Hence every minimal fort has size \(2\) or \(3\). If \(e_2=\sum_{i<j}m_im_j\) and \(e_3=\sum_{i<j<k}m_im_jm_k\), then the number of minimal forts is \[\sum_i\binom{m_i}{2}+\binom q2+q e_2+e_3.\] Writing \(o=|\{i:m_i\text{ is odd}\}|\) and \(\varepsilon=q\bmod2\), the fort number is \[\operatorname{ft}(G)=\sum_i\left\lfloor\frac{m_i}{2}\right\rfloor+\left\lfloor\frac q2\right\rfloor+\left\lfloor\frac{o+\varepsilon}{3}\right\rfloor.\] The fractional zero forcing number is \[\operatorname Z^*(G)=\begin{cases}(N-1)/2,&q=1,\\N/2,&q\ne1,\end{cases}\] where \(N=|V(G)|\).

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, so \(r\ge2\). A nonempty set \(F\subseteq V(G)\) is a fort when no vertex outside \(F\) has exactly one neighbor in \(F\). It is minimal when no proper subset is a fort.

Let \(q\) be the number of singleton parts, and write \(m_1,\ldots,m_p\ge2\) for the non-singleton part sizes. Let
\[
e_2=\sum_{i<j}m_i m_j,\qquad
e_3=\sum_{i<j<k}m_i m_j m_k.
\]
The fort number \(\operatorname{ft}(G)\) is the maximum number of pairwise disjoint minimal forts. The fractional zero forcing number \(\operatorname Z^*(G)\) is the fractional transversal number of the minimal-fort hypergraph.

## Proof
For a set \(F\), write \(f_i=|F\cap X_i|\) and \(t=|F|\). A vertex outside \(F\) in part \(X_i\) has exactly \(t-f_i\) neighbors in \(F\). Thus \(F\) is a fort exactly when
\[
t-f_i\ne1
\]
for every part \(X_i\) that is not completely contained in \(F\).

First suppose \(|F|=2\). If both vertices lie in one non-singleton part, every outside vertex sees either zero or two vertices of \(F\), so \(F\) is a fort. If they lie in distinct parts, then a selected part containing an outside vertex would see exactly one neighbor in \(F\); hence both selected parts must be singleton. Therefore the minimal forts of size two are exactly the two types in (i) and (ii).

Now let \(F\) be a minimal fort with \(|F|\ge3\). It cannot contain two vertices from one non-singleton part, because those two already form a fort. It also cannot contain two singleton vertices, because that pair already forms a fort. Hence \(F\) contains at most one vertex from each part and at most one singleton vertex. If \(|F|=3\), every outside vertex in a selected non-singleton part sees the other two selected vertices, and every vertex in an unselected part sees all three. Thus such a triple is a fort exactly when its vertices lie in three distinct parts with at most one singleton part. No two-element subset of such a triple is a fort, so it is minimal.

If \(|F|\ge4\), choose three vertices of \(F\). Since \(F\) has at most one singleton vertex and at most one vertex from each part, that triple is itself a fort of type (iii), contradicting minimality. This proves the classification.

The number of size-two minimal forts is
\[
A_2=\sum_i\binom{m_i}2+\binom q2.
\]
A size-three minimal fort either uses three non-singleton parts or two non-singleton parts and one singleton part. Hence
\[
A_3=e_3+q e_2.
\]
Therefore the total number of minimal forts is \(A_2+A_3\).

For the fort number, begin by pairing vertices within every non-singleton part and pairing singleton vertices. This gives
\[
B=\sum_i\left\lfloor\frac{m_i}2\right\rfloor+\left\lfloor\frac q2\right\rfloor
\]
disjoint size-two minimal forts. The unused vertices consist of one vertex from each odd non-singleton part and, when \(q\) is odd, one singleton vertex. Let \(o\) be the number of odd non-singleton parts and \(\varepsilon=q\bmod2\). These leftovers can be grouped into
\[
\left\lfloor\frac{o+\varepsilon}3\right\rfloor
\]
disjoint type-(iii) forts: if the singleton leftover is used, combine it with two non-singleton leftovers; all remaining triples use three non-singleton leftovers.

For optimality, consider a maximum matching of minimal forts. If two size-three forts use vertices from the same non-singleton part, replace those two triples by the pair formed by their two vertices in that part and by one minimal fort contained in the other four vertices. Such a fort always exists: either two of those four vertices lie in one non-singleton part, two are singleton vertices, or three lie in distinct parts with at most one singleton. This replacement preserves the matching size and reduces repeated use of that part by triples. The same argument replaces two triples that use singleton vertices by their singleton pair plus a minimal fort on the remaining four non-singleton vertices. Repeating, there is an optimal matching in which triples use at most one vertex from each non-singleton part and at most one singleton vertex.

Relative to \(B\), taking one vertex from an odd non-singleton part for a triple costs no pair, while taking one from an even part costs one pair. Likewise, a singleton used by a triple is free exactly when \(q\) is odd. Therefore only the \(o+\varepsilon\) parity leftovers can increase the matching size above \(B\), and every added triple consumes three such leftovers. This proves
\[
\operatorname{ft}(G)=B+\left\lfloor\frac{o+\varepsilon}3\right\rfloor.
\]

For fractional zero forcing, each non-singleton part supplies every two-vertex subset as a minimal fort. Hence the fort-cover constraints restricted to a part of size \(m_i\) force total weight at least \(m_i/2\). If \(q\ge2\), the singleton vertices likewise induce all two-element fort constraints and force total singleton weight at least \(q/2\). Thus \(\operatorname Z^*(G)\ge N/2\) when \(q\ne1\), except that when \(q=1\) the unique singleton carries no two-vertex constraint and the lower bound is \((N-1)/2\).

These bounds are attained by assigning weight \(1/2\) to every vertex when \(q\ne1\). When \(q=1\), assign weight zero to the unique singleton and weight \(1/2\) to every other vertex. Every size-two fort then has weight at least one, and every type-(iii) fort has weight at least one because it contains at least two vertices from non-singleton parts. Hence the displayed formula for \(\operatorname Z^*(G)\) follows.

## Verification
The included checker independently enumerates every nonempty vertex subset of every connected complete multipartite isomorphism type through order ten. It tests the fort definition directly, filters inclusion-minimal forts by checking all proper subsets, and compares the resulting hypergraph with the three-family classification.

It then computes the fort number by an exact bitmask matching dynamic program and computes the fractional zero forcing number by solving the minimal-fort transversal linear program. The count formulas, matching formula, and fractional formula are checked against these independent computations.

## Relationship to prior work
The 2023 fort-hypergraph paper introduces the fort number and fractional zero forcing number and determines them for several families. Its complete-bipartite example proves that when both parts are nontrivial, the minimal forts are precisely same-part pairs, giving \(\operatorname{ft}(K_{p,q})=\lfloor p/2\rfloor+\lfloor q/2\rfloor\) and \(\operatorname Z^*(K_{p,q})=(p+q)/2\); it also treats stars separately. The theorem here recovers those cases and shows the new size-three phenomenon that appears as soon as three or more parts interact.

The 2024 paper devoted to counting minimal forts proves general extremal bounds and exact formulas for paths, cycles, spiders, wheels, sunlets, windmills, and graph-product constructions. Its full text contains no complete-multipartite or complete-bipartite section beyond the general fort framework. The present classification therefore supplies the missing arbitrary complete-multipartite fort hypergraph and, from it, exact values of both fort number and fractional zero forcing number.

Targeted searches for minimal forts, fort hypergraphs, and fractional zero forcing on complete multipartite graphs did not locate an equivalent arbitrary-part result.

## Limitations
The theorem concerns standard zero-forcing forts. It does not classify analogous obstruction families for positive-semidefinite, skew, or other forcing rules. The exhaustive computation through order ten is corroborative only; the arbitrary-order result follows from the proof. Search coverage cannot exclude a differently phrased or non-indexed complete-multipartite treatment.

## References
1. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, “Forts, (fractional) zero forcing, and Cartesian products of graphs,” arXiv:2310.17904v1, 27 October 2023.
2. P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, “On the number of minimal forts of a graph,” arXiv:2404.05963v1, 9 April 2024.
