# All strong edge geodetic sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_k}\) with \(k\ge2\), every \(n_i\ge2\), partite sets \(X_1,\ldots,X_k\), and \(N=\sum_i n_i\). Define \(\rho(s)=s-1\) for even \(s\) and \(\rho(s)=s-2\) for odd \(s\), and \(R_i=\min\{n_i,\min_{j\ne i}\rho(n_j)\}\). Then a proper subset \(U\subsetneq V(G)\) is a strong edge geodetic set if and only if there is a unique \(i\) such that \(V(G)\setminus U\subseteq X_i\) and \(1\le |V(G)\setminus U|\le R_i\). Consequently, if \(F_G(z)=\sum_U z^{|U|}\) sums over all strong edge geodetic sets, then \(F_G(z)=z^N+\sum_{i=1}^k\sum_{r=1}^{R_i}\binom{n_i}{r}z^{N-r}\). Writing \(R=\max_i R_i\), one has \(\operatorname{sg}_e(G)=N-R\), and the number of minimum strong edge geodetic sets is \(\sum_{i:R_i=R}\binom{n_i}{R}\).

This gives a complete membership criterion, not only the minimum cardinality. In particular, every minimum set and the exact number of minimum sets follow from the same formula.

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_k}\) with \(k\ge2\), \(n_i\ge2\), and partite sets \(X_1,\ldots,X_k\). A set \(U\subseteq V(G)\) is strong edge geodetic when one may assign at most one shortest path to each unordered pair of vertices of \(U\), so that the assigned paths cover every edge of \(G\).

For an integer \(s\ge2\), write
\[
\rho(s)=
\begin{cases}
s-1,&s\text{ even},\\
s-2,&s\text{ odd}.
\end{cases}
\]

## Proof
We first determine the maximum number of pairwise edge-disjoint edge covers of the complete graph \(K_s\).

Every edge cover of \(K_s\) contains at least \(\lceil s/2\rceil\) edges. Hence at most \(s-1\) pairwise edge-disjoint edge covers exist when \(s\) is even, and at most \(s-2\) exist when \(s\) is odd.

For even \(s\), a one-factorization of \(K_s\) gives exactly \(s-1\) edge-disjoint perfect matchings, so the upper bound is attained.

Now let \(s=2h+1\) be odd and identify the vertices with \(\mathbb Z_s\). For each \(c\in\mathbb Z_s\), set
\[
M_c=\bigl\{\{c+t,c-t\}:1\le t\le h\bigr\}.
\]
The \(M_c\) partition \(E(K_s)\), and \(M_c\) is a near-perfect matching missing only vertex \(c\). Moreover, \(M_0\cup M_1\) is a Hamilton path from \(0\) to \(1\): alternating its two matching edges generates the vertex sequence
\[
0,2,-2,4,-4,\ldots
\]
modulo \(s\), which visits every residue because multiplication by \(2\) permutes \(\mathbb Z_s\). Orient this Hamilton path from \(0\) to \(1\). For each internal vertex \(c\in\mathbb Z_s\setminus\{0,1\}\), let \(e_c\) be the path edge leaving \(c\) toward \(1\). Then
\[
M_c\cup\{e_c\},\qquad c\in\mathbb Z_s\setminus\{0,1\},
\]
are \(s-2\) pairwise edge-disjoint edge covers of \(K_s\). Thus the maximum number of pairwise edge-disjoint edge covers of \(K_s\) is exactly \(\rho(s)\).

We now characterize strong edge geodetic sets of \(G\). Suppose first that \(U\ne V(G)\). Two distinct partite sets cannot both contain an omitted vertex. Indeed, if \(x\in X_i\setminus U\) and \(y\in X_j\setminus U\), \(i\ne j\), then the edge \(xy\) cannot lie on a shortest path whose two endpoints are in \(U\): every shortest path containing \(xy\) has length at most two, so at least one of \(x,y\) is an endpoint. Hence there is a unique incomplete part, say \(X_i\).

Let \(Q=X_i\setminus U\) and \(r=|Q|\). Fix a full part \(X_j\), \(j\ne i\). For each omitted vertex \(q\in Q\), every edge from \(q\) to \(X_j\) must be covered by length-two geodesics whose endpoints both lie in \(X_j\). The unordered endpoint pairs used for a fixed \(q\) therefore form an edge cover of the complete graph on \(X_j\). Different omitted vertices must use disjoint endpoint pairs because only one shortest path may be assigned to a given pair of vertices of \(U\). Hence \(K_{n_j}\) must contain \(r\) pairwise edge-disjoint edge covers, so
\[
r\le \rho(n_j)
\]
for every \(j\ne i\). Also \(r\le n_i\). Therefore \(r\le R_i\).

Conversely, suppose \(Q\subseteq X_i\) has size \(r\le R_i\), and let \(U=V(G)\setminus Q\). For each full part \(X_j\), choose \(r\) pairwise edge-disjoint edge covers of the complete graph on \(X_j\), indexed by the vertices of \(Q\). If \(q\in Q\) and \(ab\) belongs to the edge cover indexed by \(q\), assign the geodesic \(a-q-b\) to the pair \(a,b\). These paths cover every edge joining \(q\) to \(X_j\). Assign the one-edge geodesic to every selected pair in different partite sets. All edges are then covered, and no endpoint pair receives two paths. Thus \(U\) is strong edge geodetic.

The full vertex set is trivially strong edge geodetic. Therefore the characterization is complete. A proper strong edge geodetic set with exactly \(r\) omissions from \(X_i\) can be chosen in exactly \(\binom{n_i}{r}\) ways, which yields
\[
F_G(z)=z^N+\sum_{i=1}^k\sum_{r=1}^{R_i}\binom{n_i}{r}z^{N-r}.
\]
The smallest strong edge geodetic sets maximize the number of omissions. If \(R=\max_i R_i\), then
\[
\operatorname{sg}_e(G)=N-R,
\]
and precisely the parts with \(R_i=R\) can contain the omitted vertices of a minimum set. Hence the number of minimum sets is
\[
\sum_{i:R_i=R}\binom{n_i}{R}.
\]

## Verification
The accompanying `verify.py` uses the definition directly. For each candidate vertex subset, it constructs every admissible shortest path associated with each selected endpoint pair and performs an exact backtracking search for a path assignment that covers all graph edges. It does not use the edge-cover criterion in its feasibility test.

The program exhaustively checks all \(32\) complete multipartite isomorphism types with every part of size at least two and total order at most \(10\), comprising \(17008\) candidate vertex subsets. It confirms the membership characterization, the minimum value, and the minimum-set count in every case. It also checks the symmetric minimum-value formula against the published 2024 piecewise formula on \(5574\) multipartite types of total order at most \(30\).

## Relationship to prior work
Klavžar and Zmazek determined the strong edge geodetic number of complete bipartite and complete multipartite graphs. Their Lemma 2.2 establishes the key necessity that, in the bipartite case, one whole part belongs to every strong edge geodetic set; their Theorem 2.7 determines the minimum cardinality for arbitrary complete multipartite graphs. Their proof uses edge-colorings to construct minimum sets in the required parity cases.

The present result strengthens that value theorem to an if-and-only-if description of every strong edge geodetic vertex set, a closed size enumerator, and an exact count of all minimum sets. The additional structural ingredient is the exact packing number \(\rho(s)\) of pairwise edge-disjoint edge covers of \(K_s\).

Targeted database and literature searches for all minimum strong edge geodetic sets, basis counts, set enumerators, and edge-cover decompositions for complete multipartite graphs did not locate an equivalent classification. Later literature located in the search treats the complete multipartite result as a value formula rather than an all-set enumeration.

## Limitations
The theorem assumes every part has size at least two, matching the scope of the published complete-multipartite value theorem. Singleton parts require separate bookkeeping because they change the endpoint-pair structure. The computational verification is finite and corroborative only; the all-orders statement rests on the proof. Literature searches cannot prove the absence of differently phrased or non-indexed prior work.

## References
1. S. Klavžar and E. Zmazek, “Strong Edge Geodetic Problem on Complete Multipartite Graphs and some Extremal Graphs for the Problem,” arXiv:2312.11199, first public version 18 December 2023; Bulletin of the Iranian Mathematical Society 50, 13 (2024), DOI 10.1007/s41980-023-00849-6.
2. P. Manuel, S. Klavžar, D. A. Xavier, A. Arokiaraj, and E. Thomas, “Strong edge geodetic problem in networks,” Open Mathematics 15 (2017), 1225–1235, DOI 10.1515/math-2017-0101.
