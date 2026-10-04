# All secure total dominating sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), parts \(X_1,\ldots,X_r\), and \(D\subseteq V(G)\). Write \(d_i=|D\cap X_i|\). Then \(D\) is a secure total dominating set if and only if either it meets at least three parts, or it meets exactly two parts \(X_i,X_j\) and \((d_i=n_i\text{ or }d_j\ge2)\) and \((d_j=n_j\text{ or }d_i\ge2)\). Consequently, if \(B_i(z)=(1+z)^{n_i}-1\) and \[Q_{ij}(z)=(B_i(z)-n_i z)(B_j(z)-n_j z)+\mathbf 1_{n_i\ge2}n_j z^{n_i+1}+\mathbf 1_{n_j\ge2}n_i z^{n_j+1}+\mathbf 1_{n_i=n_j=1}z^2,\]then the secure-total-domination size enumerator is \[S_G(z)=(1+z)^N-1-\sum_i B_i(z)-\sum_{i<j}B_i(z)B_j(z)+\sum_{i<j}Q_{ij}(z),\]where \(N=\sum_i n_i\). This classification also gives the exact minimum size and number of minimum sets: for \(r\ge3\), the minimum is \(2\) when at least two parts are singletons and otherwise \(3\); for \(r=2\), it is \(2\) for \(K_{1,1}\), equals \(N\) when exactly one part is a singleton, equals \(3\) when neither part is a singleton and at least one has size \(2\), and otherwise equals \(4\).

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, with \(r\ge2\), partite classes \(X_1,\ldots,X_r\), and \(N=\sum_i n_i\). A total dominating set \(D\) has the property that every vertex, including every vertex of \(D\), has a neighbor in \(D\). It is secure total dominating when every vertex \(v\notin D\) can replace an adjacent vertex \(u\in D\) so that \((D\setminus\{u\})\cup\{v\}\) is again total dominating.

## Proof
In a complete multipartite graph, a set is total dominating exactly when it meets at least two parts. Indeed, if it meets at least two parts, every vertex has a selected neighbor in another part; if it is contained in one part, selected vertices have no selected neighbors.

Let \(D\) meet at least three parts. For any \(v\notin D\), choose a defender \(u\in D\) from a part different from that of \(v\). After replacing \(u\) by \(v\), at least two represented parts remain: if the part of \(u\) disappears, a third represented part remains alongside the part of \(v\). Hence every such \(D\) is secure total dominating.

Now suppose that \(D\) meets exactly two parts \(X_i,X_j\), with positive counts \(d_i,d_j\). If \(v\in X_i\setminus D\), every possible defender lies in \(X_j\). Replacing a defender leaves a total dominating set exactly when either some selected vertex remains in \(X_j\), namely \(d_j\ge2\), or there is no such outside vertex to defend, namely \(d_i=n_i\). Thus vertices omitted from \(X_i\) are defensible exactly when \(d_i=n_i\) or \(d_j\ge2\). Symmetrically, vertices omitted from \(X_j\) are defensible exactly when \(d_j=n_j\) or \(d_i\ge2\). Vertices outside both represented parts cause no extra restriction: after a swap, the new part and the untouched represented part give two selected parts. This proves the all-set criterion.

Put \(B_i(z)=(1+z)^{n_i}-1\), the generating polynomial for nonempty choices from \(X_i\). Subsets meeting at least three parts contribute
\[
(1+z)^N-1-\sum_i B_i(z)-\sum_{i<j}B_i(z)B_j(z).
\]
For exactly two represented parts \(X_i,X_j\), the valid choices split disjointly into four cases: both selected counts are at least two; \(X_i\) is selected completely and exactly one vertex is chosen from \(X_j\); the symmetric case; or both parts are singletons. Their contribution is exactly
\[
Q_{ij}(z)=(B_i(z)-n_i z)(B_j(z)-n_j z)
+\mathbf 1_{n_i\ge2}n_j z^{n_i+1}
+\mathbf 1_{n_j\ge2}n_i z^{n_j+1}
+\mathbf 1_{n_i=n_j=1}z^2.
\]
Summing gives the displayed enumerator.

The minimum-size cases follow directly from the criterion. If \(r\ge3\), two selected vertices work exactly when they occupy two singleton parts; otherwise one vertex from each of three parts gives a secure total dominating triple. For \(r=2\), a singleton part forces every vertex of the other part to be selected. If both parts have size at least two, a three-set works exactly when one represented part of size two is taken completely; otherwise two vertices from each part give a four-set.

For completeness, let \(s\) be the number of singleton parts and \(t\) the number of parts of size two. When \(r\ge3\), the number of minimum sets is \(\binom{s}{2}\) if \(s\ge2\), and otherwise
\[
\sum_{i<j<k}n_i n_j n_k+t(N-2).
\]
When \(r=2\), the minimum-set count is one for \(K_{1,1}\) and for a star \(K_{1,n}\); it is \(t(N-2)\) when at least one part has size two and neither is a singleton; and when both part sizes \(a,b\ge3\), it is
\[
\binom{a}{2}\binom{b}{2}+\mathbf 1_{a=3}b+\mathbf 1_{b=3}a.
\]

## Verification
The included checker builds every complete multipartite graph of orders two through ten from its part labels. For every vertex subset it tests total domination directly, then for each unselected vertex searches all possible adjacent defenders and retests total domination after the swap. It compares this definition-level result with the structural criterion, every coefficient of the enumerator, and every stated minimum-size and minimum-count case.

## Relationship to prior work
Jha studies secure total domination on chain graphs and cographs and gives a linear-time algorithm for the minimum secure total domination number. Complete multipartite graphs are explicitly defined in that paper and form a cograph subclass. The cograph results therefore provide broader algorithmic coverage for computing the minimum number, but they do not classify every secure total dominating set or give a size enumerator. The present statement strengthens the information available on this subclass from optimization alone to an exact feasible-set description and distribution by cardinality.

Targeted database and literature searches for “secure total domination polynomial,” “secure total dominating sets complete multipartite,” and complete-bipartite variants did not locate an equivalent all-set formula. A 2022 paper on secure-total-domination cover pebbling treats complete multipartite graphs only for the pebbling invariant, not for the underlying secure-total set enumerator.

## Limitations
The theorem is specific to complete multipartite graphs. The minimum-number corollaries are compatible with the earlier cograph algorithm and are not asserted to supersede its broader scope. The finite computation is corroborative only; the all-orders result follows from the proof. Search coverage cannot exclude a differently phrased or non-indexed enumerative treatment.

## References
1. A. Jha, “Secure total domination in chain graphs and cographs,” AKCE International Journal of Graphs and Combinatorics 17 (2020), 826–832, DOI 10.1016/j.akcej.2019.10.005, published online 27 May 2020.
2. W. F. Klostermeyer, C. M. Mynhardt, “Secure domination and secure total domination in graphs,” Discussiones Mathematicae Graph Theory 28 (2008), 267–284, DOI 10.7151/dmgt.1405.
