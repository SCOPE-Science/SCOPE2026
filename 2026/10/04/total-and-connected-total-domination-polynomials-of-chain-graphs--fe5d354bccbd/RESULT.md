# Total and connected total domination polynomials of chain graphs

## Finding
Let \(G=(A,B,E)\) be a connected chain graph, so the open neighborhoods on each side are linearly ordered by inclusion. Define the two extreme twin classes
\[
A^\star=\{a\in A:N(a)=B\},\qquad B^\star=\{b\in B:N(b)=A\},
\]
and write \(m=|A|\), \(n=|B|\), \(a=|A^\star|\), and \(b=|B^\star|\). Connectedness guarantees \(a,b\ge1\).

A set \(S\subseteq V(G)\) is a total dominating set if and only if
\[
S\cap A^\star\neq\varnothing\qquad\text{and}\qquad S\cap B^\star\neq\varnothing.
\]
Moreover, every total dominating set of a connected chain graph induces a connected subgraph. Hence total domination and connected total domination have exactly the same sets, and their size-generating polynomials are identical:
\[
D_t(G;x)=D_{ct}(G;x)
=\big((1+x)^m-(1+x)^{m-a}\big)
 \big((1+x)^n-(1+x)^{n-b}\big).
\]
Equivalently,
\[
D_t(G;x)=(1+x)^{m+n-a-b}\big((1+x)^a-1\big)\big((1+x)^b-1\big).
\]
Thus \(\gamma_t(G)=\gamma_{ct}(G)=2\), the number of minimum sets is \(ab\), and every cardinality from \(2\) through \(m+n\) occurs.

The factorization also gives the complete root multiset. The root \(0\) has multiplicity two; \(-1\) has multiplicity \(m+n-a-b\); and the remaining roots are \(\zeta-1\), where \(\zeta\) ranges over the nontrivial \(a\)-th and \(b\)-th roots of unity, with multiplicity inherited from the two factors. Hence every non-\(-1\) root lies on the circle \(|z+1|=1\), and all roots are real if and only if \(a\le2\) and \(b\le2\).

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. A chain graph is bipartite with bipartition \((A,B)\) such that the neighborhoods of vertices in either part are nested by inclusion. A total dominating set \(S\) satisfies: every vertex of \(G\), including vertices of \(S\), has a neighbor in \(S\). A connected total dominating set is a total dominating set whose induced subgraph is connected.

The statement includes \(K_2\) and complete bipartite graphs. No claim is made for disconnected chain graphs with isolated vertices, where total domination may fail to exist.

## Proof
Order \(A=\{a_1,\ldots,a_m\}\) so that
\[
N(a_1)\subseteq N(a_2)\subseteq\cdots\subseteq N(a_m)=B.
\]
Because \(G\) is connected, \(N(a_1)\neq\varnothing\). The smallest neighborhood on the \(A\)-side is exactly
\[
N(a_1)=B^\star,
\]
since any vertex of \(B\) adjacent to \(a_1\) is adjacent to every later \(a_i\), and conversely a vertex universal to \(A\) is adjacent to \(a_1\).

Likewise the neighborhoods of vertices of \(B\) are nested. Their smallest member is exactly \(A^\star\): a vertex of \(A\) belongs to every neighborhood on the \(B\)-side precisely when it is adjacent to all of \(B\).

Suppose \(S\) is total dominating. The vertex \(a_1\) must have a neighbor in \(S\), and every neighbor of \(a_1\) lies in \(B^\star\). Hence \(S\cap B^\star\neq\varnothing\). Similarly, a vertex of \(B\) with minimum neighborhood has neighborhood \(A^\star\), so it must be dominated by a vertex of \(S\cap A^\star\). Therefore both intersections are necessary.

Conversely, choose \(\alpha\in S\cap A^\star\) and \(\beta\in S\cap B^\star\). The vertex \(\alpha\) is adjacent to every vertex of \(B\), while \(\beta\) is adjacent to every vertex of \(A\). Thus \(\beta\) dominates all vertices of \(A\), and \(\alpha\) dominates all vertices of \(B\). In particular \(\alpha\) and \(\beta\) dominate one another, so \(S\) is total dominating.

The same pair also proves connectedness of \(G[S]\). Every selected vertex in \(A\) is adjacent to \(\beta\), every selected vertex in \(B\) is adjacent to \(\alpha\), and \(\alpha\beta\in E(G)\). Hence all vertices of \(S\) lie in one connected component. Therefore every total dominating set is connected total dominating.

To enumerate the sets, the generating function for subsets of \(A\) meeting \(A^\star\) is
\[
(1+x)^m-(1+x)^{m-a},
\]
because the second term counts exactly the subsets avoiding \(A^\star\). The analogous factor on \(B\) is \((1+x)^n-(1+x)^{n-b}\). Choices on the two sides are independent, giving the product formula.

Factoring out powers of \(1+x\) yields
\[
D_t(G;x)=(1+x)^{m+n-a-b}\big((1+x)^a-1\big)\big((1+x)^b-1\big).
\]
The two latter factors each have a simple zero at \(x=0\). Their other zeros are obtained from nontrivial roots of unity by the translation \(x=\zeta-1\). This proves the root description. For an integer \(q\ge1\), all roots of \((1+x)^q-1\) are real exactly when \(q\le2\), establishing the final criterion.

## Verification
A standalone exact checker is included as `verify.py`. It enumerates canonical connected chain graphs with both side sizes at most six and total order at most eleven. For every graph it tests every vertex subset directly against the total-domination definition, compares with the two-extreme-class criterion, checks that every accepted set induces a connected subgraph, and compares brute-force coefficient counts with the product formula.

The finite computation is a regression check, not the proof of the arbitrary-order statement.

## Relationship to prior work
Chaluvaraju and Chaitra introduced the total domination polynomial and computed several basic families and graph operations. Their complete-bipartite formula is recovered here by taking \(A^\star=A\) and \(B^\star=B\), when the factorization becomes \(((1+x)^m-1)((1+x)^n-1)\). Their paper does not treat chain graphs. Jha later studied secure total domination in chain graphs and cographs, using chain orderings to obtain minimum secure-total-domination results; that stronger exchange-stability invariant is different from enumerating all total dominating sets.

The present statement adds an all-set classification for every connected chain graph, proves that total domination automatically implies connected total domination on this class, and gives the complete polynomial factorization and root multiset.

## Limitations
The literature search cannot exclude poorly indexed or inaccessible sources that may contain the same chain-graph factorization. The inspected chain-graph paper concerns secure total domination rather than the all-set total-domination polynomial. The exact checker covers only finite orders; arbitrary order is established by the symbolic proof above.

## References
B. Chaluvaraju and V. Chaitra, “Total Domination Polynomial of A Graph,” Journal of Informatics and Mathematical Sciences 6(2) (2014), 87–92. DOI: 10.26713/jims.v6i2.256.

A. Jha, “Secure total domination in chain graphs and cographs,” AKCE International Journal of Graphs and Combinatorics 17(3) (2020), 826–832. DOI: 10.1016/j.akcej.2019.10.005.
