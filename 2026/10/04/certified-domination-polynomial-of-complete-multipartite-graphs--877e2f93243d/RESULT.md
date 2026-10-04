# Certified domination polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), \(N=\sum_i n_i\), and parts \(X_i\). For \(D\subseteq V(G)\), put \(d_i=|D\cap X_i|\), \(c_i=n_i-d_i\), and \(q=|V(G)\setminus D|\). Then \(D\) is certified dominating if and only if it dominates \(G\) and \(q-c_i\ne1\) for every \(i\) with \(d_i>0\). Equivalently, domination means that \(D\) meets at least two parts or is one entire part. If \[P_G(z)=(1+z)^N-\sum_{i=1}^r(1+z)^{n_i}+(r-1)+\sum_{i=1}^r z^{n_i},\] then the certified domination polynomial is \[D_{\rm cer}(G;z)=P_G(z)-Nz^{N-1}-\sum_{\substack{1\le i\le r\\N-n_i\ge2}}(N-n_i)z^{N-n_i-1}\big((1+z)^{n_i}-z^{n_i}-1\big)+z^{N-2}\sum_{\substack{i<j\\n_i,n_j\ge2}}n_i n_j.\] This formula specializes to the published coefficient formula for \(K_{3,n}\).

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, with \(r\ge2\), partite classes \(X_1,\ldots,X_r\), and \(N=\sum_i n_i\). A dominating set \(D\) is certified when every selected vertex has either no neighbor or at least two neighbors outside \(D\). The polynomial \(D_{\rm cer}(G;z)\) counts certified dominating sets by cardinality.

## Proof
Write \(d_i=|D\cap X_i|\), \(c_i=n_i-d_i\), and \(q=\sum_i c_i=|V(G)\setminus D|\).

A set \(D\) dominates \(G\) exactly when it either meets at least two parts or consists of one entire part. Indeed, an omitted vertex in \(X_i\) needs a selected neighbor outside \(X_i\).

Now fix a selected vertex in \(X_i\). Its neighbors outside \(D\) are precisely the omitted vertices outside \(X_i\), so their number is
\[
q-c_i.
\]
Thus the certified condition is exactly \(q-c_i\ne1\) for every selected part \(X_i\). This proves the all-set criterion.

The domination polynomial of a complete multipartite graph is
\[
P_G(z)=(1+z)^N-\sum_i(1+z)^{n_i}+(r-1)+\sum_i z^{n_i},
\]
because every subset meeting at least two parts dominates, and among one-part subsets only an entire part dominates.

It remains to delete from \(P_G(z)\) the dominating sets containing a half-shadowed selected vertex. Every dominating set of size \(N-1\) is non-certified, contributing the subtraction \(Nz^{N-1}\).

Suppose now that \(q\ge2\). A selected part \(X_i\) contains half-shadowed vertices exactly when all but one omitted vertex lie in \(X_i\): if \(k=c_i\), then \(1\le k\le n_i-1\) and exactly one omitted vertex lies outside \(X_i\). Such a set is dominating precisely when \(N-n_i\ge2\). Hence the bad sets associated with \(X_i\) contribute
\[
(N-n_i)\sum_{k=1}^{n_i-1}\binom{n_i}{k}z^{N-k-1}
=(N-n_i)z^{N-n_i-1}\big((1+z)^{n_i}-z^{n_i}-1\big).
\]

For \(q\ge2\), two distinct half-shadowed-part events can intersect only when \(q=2\), with one omitted vertex in each of two parts \(X_i,X_j\). Both parts must be non-singleton so that they remain selected. There are \(n_i n_j\) such complements, all of size two, giving the inclusion-exclusion correction
\[
z^{N-2}\sum_{i<j,\ n_i,n_j\ge2}n_i n_j.
\]
No triple intersection is possible. Combining these terms with \(P_G(z)\) yields the displayed polynomial.

## Verification
The included checker constructs complete multipartite graphs directly from their part labels. For every vertex subset, it tests domination vertex by vertex and then counts outside neighbors of every selected vertex, without using the theorem. It compares those sets with the profile criterion and every polynomial coefficient for all complete multipartite isomorphism types of orders two through ten.

As an implication check against the closest explicit enumerative literature, the checker also specializes the formula to \(K_{3,n}\) and verifies coefficient-by-coefficient agreement with the published 2025 theorem for \(3\le n\le10\).

## Relationship to prior work
The foundational certified-domination paper introduces the parameter and gives the certified domination number for complete bipartite graphs, among other elementary classes. It does not give a certified-domination polynomial for arbitrary complete multipartite graphs.

A 2025 paper studies exactly the certified domination polynomial of \(K_{3,n}\), states MSC \(05C69\), and derives a piecewise coefficient formula for that family. The formula above strictly broadens the graph class to arbitrary complete multipartite graphs and specializes to that published \(K_{3,n}\) result.

A semantic search of a published-finding database found a certified-domination extremal result for connected graphs, but no complete-multipartite certified-domination polynomial or all-set classification.

## Limitations
The theorem is restricted to connected complete multipartite graphs. The finite verification is corroborative only; the all-orders result follows from the proof. The 2025 \(K_{3,n}\) paper is genuine prior coverage of a special case. Search coverage cannot exclude a differently phrased or non-indexed arbitrary-multipartite enumeration.

## References
1. M. Dettlaff, M. Lemańska, J. Topp, R. Ziemann, P. Żyliński, “Certified domination,” AKCE International Journal of Graphs and Combinatorics 17(1) (2020), 86–97, DOI 10.1016/j.akcej.2018.09.004.
2. K. Lal Gipson, M. J. Angelin Jenisha, “Certified dominating sets and certified domination polynomial of complete bipartite graph \(K_{3,n}\),” Advances and Applications in Discrete Mathematics 42(3) (2025), 273–283, DOI 10.17654/0974165825018.
