# Enumerating dominating–locating partitions of complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be any labelled simple complete multipartite graph with \(r\ge2\) nonempty parts. Write \(m_1,\ldots,m_p\ge2\) for the sizes of its nonsingleton parts, and let \(s=r-p\) be its number of singleton parts. A set is **dominating** if every vertex outside it has a neighbour inside it; it is **locating-dominating (LD)** if, additionally, distinct vertices outside it have different nonempty sets of neighbours inside it.

Let \(D_G(z)\) count *ordered* complementary pairs \((A,B)\), where \(A\) is dominating and \(B=V(G)\setminus A\) is LD, with weight \(z^{|A|}\). Then
\[
D_G(z)=\begin{cases}
(1+sz)\displaystyle\prod_{i=1}^{p}(1+m_i z)-1-z\displaystyle\sum_{i=1}^{p}m_i,&p\ge2,\\
sz+sm_1z^2,&p=1,\ s\ge2,\\
sz,&\text{otherwise}.
\end{cases}
\]
The ordered orientation is essential: the first side must be dominating, while the second side must be LD.

Let \(L_G(z)\) count the same ordered pairs when **both** \(A\) and \(B\) are LD, again weighted by \(z^{|A|}\). Its entire spectrum is
\[
L_G(z)=\begin{cases}
2^p z^p,&\text{all }m_i=2,\ s=0,\ p\ge2,\\
2^p(z^p+z^{p+1}),&\text{all }m_i=2,\ s=1,\ p\ge2,\\
2^{p+1}z^{p+1},&\text{all }m_i=2,\ s=2,\\
0,&\text{otherwise}.
\end{cases}
\]
The clause \(s=2\) includes \(p=0\), giving the two ordered partitions of \(K_2\). In particular, every double-LD partition has its two sides differing in size by at most one, even though these graphs can have twins. For \(p\ge2\), the total number of dominating–LD ordered partitions is \((1+s)\prod_i(1+m_i)-1-\sum_i m_i\).

For example, \(K_{2,2,2}\) has \(D_G(z)=12z^2+8z^3\) and \(L_G(z)=8z^3\), whereas \(K_{2,1,1}\) has \(D_G(z)=2z+4z^2\) and \(L_G(z)=4z^2\).

## Assumptions and scope
All graphs are finite, undirected, simple, with labelled vertices and at least two nonempty multipartite classes; hence they have no isolated vertices. Each choice of vertices is counted separately, even when related by an automorphism. The pair \((A,B)\) is ordered and \(B\) is the exact complement of \(A\); no equivalence modulo exchange, relabelling, or graph isomorphism is taken. All polynomial identities hold formally in \(\mathbb Z[z]\).

## Proof
Let the multipartite classes be \(X_1,\ldots,X_r\), and put \(A_i=A\cap X_i\) and \(B_i=B\cap X_i\). For any \(a\in A_i\), its neighbours in the prospective LD code \(B\) are precisely \(B\setminus B_i\). Therefore \(B\) locates all vertices of \(A\) if and only if (i) \(|A_i|\le1\) for every \(i\), and (ii) no two *selected* parts \(i\ne j\) have both \(B_i=B_j=\varnothing\). Indeed, signatures of vertices in distinct selected parts agree precisely when both respective omitted subparts are empty: their disjoint subparts \(B_i,B_j\) must be equal.

Under \(|A_i|\le1\), the condition \(B_i=\varnothing\) for a selected part is equivalent to \(|X_i|=1\). Hence (ii) is equivalent to selecting from at most one singleton part. Moreover, \(B\) dominates \(A\) exactly when every selected class \(X_i\) has some vertex of \(B\) outside \(X_i\). Independently, \(A\) dominates \(B\) exactly when every class containing a vertex of \(B\) has some selected vertex in a different class.

If \(|A|=1\), the latter condition forces the unique chosen vertex to belong to a singleton class: otherwise an unchosen same-class vertex would not be dominated. Conversely, every singleton vertex is universal and gives one valid oriented partition. This contributes \(sz\).

Suppose \(|A|\ge2\). The location restriction forces one selected vertex from each of at least two distinct classes, with at most one selected singleton; these two distinct classes guarantee that \(A\) dominates \(B\). If \(p\ge2\), each nonsingleton class retains at least one vertex of \(B\), and at least two such classes exist, so \(B\) also dominates every selected vertex. One may therefore select one vertex or none from every nonsingleton class, and optionally one of the \(s\) singleton vertices, excluding the empty choice and all choices of exactly one nonsingleton vertex. The resulting generating function is \((1+sz)\prod_i(1+m_i z)-1-z\sum_i m_i\).

If \(p=1\), a configuration with two or more selected vertices can only consist of one vertex from the unique nonsingleton class and one singleton vertex. The selected nonsingleton vertex is dominated by \(B\) exactly when a *different*, unselected singleton class remains, which happens if and only if \(s\ge2\). There are \(sm_1\) choices of such pairs. If \(p=0\), two selected vertices always violate location, as both selected singleton classes have the same neighbourhood in \(B\). This proves \(D_G(z)\) in all cases.

For \(L_G(z)\), both sides are LD. Applying the first location condition with \(A\) and \(B\) interchanged shows that each class has at most one vertex on each side, hence every class has size at most two. Each nonsingleton class must therefore have size exactly two and be split one-to-one, giving two labelled choices per such class. The second location condition in both orientations says that at most one singleton vertex belongs to each side, hence \(s\le2\). If \(p\ge2\), all these constraints are sufficient: both sides contain a vertex from each of at least two split doubleton classes, ensuring mutual domination, and the classwise distinct-neighbourhood conditions hold. The \(s=0\), \(s=1\) and \(s=2\) generating polynomials then follow by allocating the singleton vertices.

If \(p=1\), a double-LD partition is possible only when \(s=2\): the two singleton vertices must lie on opposite sides, so each selected doubleton vertex has a neighbour in the other side *outside its own class*. This yields four ordered partitions, each with two vertices on either side. With fewer singleton classes, domination fails for the selected doubleton vertex on one side. If \(p=0\), the graph is complete; the location condition in both directions restricts each side to at most one vertex, so precisely \(K_2\) admits such a partition. These cases are exactly those listed for \(L_G(z)\), completing the proof.

## Verification
The standalone file `VERIFY.py` constructs every graph for the 147 unordered part-size profiles of between two and six parts, with each part at most five vertices and total order at most twelve. Without assuming the structural classification, it exhausts all \(2^{|V(G)|}\) candidate first sides, directly checks domination and LD neighbourhood signatures on both sides, and compares every coefficient of both generating polynomials. This totals 209812 tested subsets. Run `python3 VERIFY.py`; the expected final line is `VERIFY_OK profiles=147 subsets=209812 both_complete_weight_enumerators=true`. The exhaustive calculations are finite corroboration; the proof above supplies the all-orders statements.

## Relationship to prior work
Chakraborty, Foucaud, Henning and Laihonen (2026, Theorem 6) prove that every isolate-free graph has a partition into a dominating and an LD set. Their general existence theorem does not count these partitions by side cardinality or determine when both sides can be LD. Foucaud, Maniya, Paul and Pradhan (2025 preprint; 2026 journal) establish two-LD partitions for specified *twin-free* graph classes, including split and co-bipartite graphs. The present classification addresses complete multipartite graphs with arbitrary open-twin classes and singleton universal-vertex classes, including graphs which are not twin-free. The direct parts of the earlier theorems establish existence on overlapping subfamilies, not these coefficient formulas; a possible broader, earlier exact enumeration remains an originality caveat.

## Limitations
The result concerns only complete multipartite graphs with at least two nonempty classes and *ordered* vertex partitions. It does not determine an analogous distribution for general graphs, unordered partitions, or automorphism orbits. Although source comparisons found no equivalent explicit formula, historical completeness and independent review are not established.

## References
1. D. Chakraborty, F. Foucaud, M. A. Henning and T. Laihonen, “A Note on Partitioning the Vertex Set of a Graph into a Dominating Set and a Locating Dominating Set,” *Electronic Journal of Combinatorics* **33** (2026), #P1.51, published 2026-03-13. DOI: `10.37236/14049`.
2. F. Foucaud, P. V. Maniya, K. Paul and D. Pradhan, “Locating-dominating partitions for some classes of graphs,” arXiv:`2506.12933`, first posted 2025-06-15; *Discrete Mathematics* **349** (2026), 114886. DOI: `10.1016/j.disc.2025.114886`.
