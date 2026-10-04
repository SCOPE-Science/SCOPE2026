# Weight enumerator of total Roman \{2\}-domination on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph, with \(r\ge2\), \(N=\sum_i n_i\), and let \(f:V(G)\to\{0,1,2\}\). For part \(X_i\), write \(w_i=\sum_{v\in X_i}f(v)\), \(p_i=|\{v\in X_i:f(v)>0\}|\), and let \(W=\sum_v f(v)\). Then \(f\) is a total Roman \{2\}-dominating function if and only if its positive support meets at least two parts and \(W-w_i\ge2\) for every part containing a zero-labeled vertex. Consequently, with \(M_i(z)=(1+z+z^2)^{n_i}-1-(z+z^2)^{n_i}\), the exact weight enumerator over all such functions is \[\mathcal T_G(z)=(1+z+z^2)^N-\sum_i(1+z+z^2)^{n_i}+r-1-z\sum_i(N-n_i)M_i(z)+z^2\sum_{\substack{i<j\\ n_i,n_j\ge2}}n_i n_j.\] In particular, the previously known minimum value is recovered: \(\gamma_{t\{R2\}}(G)=2\) when at least two parts are singleton; it equals \(3\) when exactly one part is singleton, or when there are at least three parts and no singleton part, or when \(r=2\) and the smaller part has size \(2\); and it equals \(4\) exactly for \(r=2\) with both parts of size at least \(3\).

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, so \(r\ge2\), with partite classes \(X_1,\ldots,X_r\) and order \(N=\sum_i n_i\). A total Roman \{2\}-dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that every vertex labeled \(0\) has open-neighborhood label sum at least \(2\), and every positive-labeled vertex has a positive-labeled neighbor.

For each part define \(w_i=\sum_{v\in X_i}f(v)\), \(p_i=|\{v\in X_i:f(v)>0\}|\), and \(W=\sum_v f(v)\). The enumerator is \(\mathcal T_G(z)=\sum_f z^{W}\), summed over all total Roman \{2\}-dominating functions.

## Proof
A vertex in \(X_i\) is adjacent to every vertex outside \(X_i\) and to no vertex inside it. Therefore every zero-labeled vertex in \(X_i\) receives neighborhood weight exactly \(W-w_i\). Hence the Roman \{2\} condition is equivalent to
\[
W-w_i\ge2
\]
for every part containing a zero-labeled vertex.

Likewise, a positive-labeled vertex in \(X_i\) has a positive neighbor exactly when some positive-labeled vertex lies outside \(X_i\). Thus the total condition holds for every positive vertex exactly when the positive support meets at least two parts. This proves the structural criterion.

It remains to count the valid functions by weight. Begin with all ternary labelings, contributing \((1+z+z^2)^N\). Remove those whose positive support meets at most one part. For a fixed part \(X_i\), the labelings supported entirely inside \(X_i\) contribute \((1+z+z^2)^{n_i}-1\), while the all-zero labeling is common to all choices. Hence the labelings whose positive support meets at least two parts have generating function
\[
(1+z+z^2)^N-\sum_i(1+z+z^2)^{n_i}+r-1.
\]

Among these, the Roman \{2\} condition fails at part \(X_i\) precisely when \(X_i\) contains both a zero and a positive label and the total weight outside \(X_i\) is exactly \(1\). The inside mixed assignments contribute
\[
M_i(z)=(1+z+z^2)^{n_i}-1-(z+z^2)^{n_i},
\]
and the unique outside positive label can be placed at any of the \(N-n_i\) outside vertices, where it must be label \(1\). Thus the bad family associated with \(X_i\) contributes
\[
(N-n_i)zM_i(z).
\]

Two distinct bad-part events can intersect only when the total weight is \(2\): one label \(1\) lies in each of two parts \(X_i,X_j\), each of those parts also contains at least one zero, and all other labels are zero. This requires \(n_i,n_j\ge2\), and there are \(n_i n_j\) such labelings. No three bad-part events can intersect. Inclusion-exclusion therefore gives
\[
\mathcal T_G(z)=(1+z+z^2)^N-\sum_i(1+z+z^2)^{n_i}+r-1-z\sum_i(N-n_i)M_i(z)+z^2\sum_{\substack{i<j\\ n_i,n_j\ge2}}n_i n_j.
\]

For the minimum weight, weight \(2\) is possible exactly when two singleton parts receive label \(1\). If this is impossible, weight \(3\) is possible when there is one singleton part, when at least three non-singleton parts permit one label \(1\) in each of three parts, or in a bipartite graph with a part of size two by labeling that entire part with \(1\) and one vertex of the other part with \(1\). The only remaining case is \(K_{a,b}\) with \(a,b\ge3\), where weight \(3\) fails and assigning label \(2\) to one vertex in each part gives weight \(4\). This recovers the published complete-multipartite minimum formula.

## Verification
The included checker constructs every connected complete multipartite isomorphism type of orders \(2\) through \(9\). It examines every map to \(\{0,1,2\}\), tests the two defining conditions directly from graph adjacency, independently evaluates the structural criterion, expands the closed polynomial with integer polynomial arithmetic, and compares every coefficient and minimum weight.

## Relationship to prior work
The 2019 foundational paper introduces total Roman \{2\}-domination, develops general bounds and complexity results, and its full manuscript contains no complete-bipartite or complete-multipartite treatment. A 2021 reinforcement paper is the decisive complete-multipartite overlap source: its Proposition 9 gives the exact minimum total Roman \{2\}-domination number for \(K_{p_1,\ldots,p_t}\), and its Theorem 6 gives the reinforcement number. That paper does not enumerate all feasible functions; exact full-text searches return no polynomial or enumeration treatment. Thus the minimum formula above is explicitly prior coverage, while the structural characterization of every feasible labeling and the complete weight enumerator are additional information not implied by the published minimum or reinforcement numbers.

A 2024 survey on Roman \{2\}-domination likewise summarizes the minimum-parameter theory and records the complete-multipartite reinforcement result, but does not provide an all-function generating polynomial.

## Limitations
The theorem is restricted to connected complete multipartite graphs and to the standard total Roman \{2\} definition. The minimum-weight corollary is prior-published and is included only as a consistency check and consequence of the new all-function formula. The exhaustive computation through order \(9\) is finite corroboration only; the arbitrary-order result follows from the proof. Search coverage cannot exclude a differently phrased or non-indexed all-function enumeration.

## References
1. S. Cabrera García, A. Cabrera Martínez, F. A. Hernández Mira, I. G. Yero, “Total Roman \{2\}-domination in graphs,” Quaestiones Mathematicae 44 (2021), 411–434, DOI 10.2989/16073606.2019.1695230; published online 28 November 2019; arXiv:2101.02537v1.
2. M. Kheibari, H. Abdollahzadeh Ahangar, R. Khoeilar, S. M. Sheikholeslami, “Total Roman \{2\}-Reinforcement of Graphs,” Journal of Mathematics (2021), Article 5515250, DOI 10.1155/2021/5515250.
3. “Survey on Roman \{2\}-Domination,” Mathematics 12 (2024), 2771.
