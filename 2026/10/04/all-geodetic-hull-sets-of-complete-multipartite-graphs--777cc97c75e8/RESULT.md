# All geodetic hull sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with parts \(V_1,\ldots,V_r\), where \(r\ge2\), and put \(N=\sum_{i=1}^r n_i\) and \(p=|\{i:n_i\ge2}|\). For \(S\subseteq V(G)\), write \(s_i=|S\cap V_i|\).

Then the geodetic hull sets of \(G\) have the following complete classification.

\[
S\text{ is a hull set}\iff
\begin{cases}
\text{some }s_i\ge2,&p\ge2,\\
V_j\subseteq S,&p=1\text{, where }V_j\text{ is the unique non-singleton part},\\
S=V(G),&p=0.
\end{cases}
\]

Thus, defining the hull-set cardinality enumerator by
\[
H_G(x)=\sum_{S\text{ a hull set}}x^{|S|},
\]
one obtains
\[
H_G(x)=
\begin{cases}
(1+x)^N-\displaystyle\prod_{i=1}^r(1+n_i x),&p\ge2,\\
x^{n_j}(1+x)^{N-n_j},&p=1,\\
x^N,&p=0.
\end{cases}
\]

The inclusion-minimal hull sets are exactly the two-element subsets contained in a non-singleton part when \(p\ge2\), the whole unique non-singleton part \(V_j\) when \(p=1\), and \(V(G)\) when \(p=0\). In particular,
\[
h(G)=
\begin{cases}
2,&p\ge2,\\
n_j,&p=1,\\
N,&p=0.
\end{cases}
\]
The scalar hull-number formula is stated only as a consequence; the all-set classification and its enumerator are the claim assessed here.

## Assumptions and scope
The graph is finite, simple, undirected, connected, and complete multipartite. Geodetic convexity uses ordinary shortest paths. For vertices \(u,v\), their interval \(I[u,v]\) is the set of vertices lying on at least one shortest \(u\)-\(v\) path. For \(X\subseteq V(G)\), let \(I[X]=\bigcup_{u,v\in X}I[u,v]\), and define the geodetic convex hull of \(X\) by iterating \(I\) until it stabilizes. A hull set is a set whose resulting hull is all of \(V(G)\).

## Proof
If \(u\) and \(v\) lie in different parts, then they are adjacent, so \(I[u,v]=\{u,v}\). If they are distinct vertices of the same part \(V_i\), then their distance is two and every vertex outside \(V_i\) is the internal vertex of a shortest \(u\)-\(v\) path. No third vertex of \(V_i\) can lie on such a path. Therefore, for every \(S\subseteq V(G)\),
\[
I[S]=S\cup\bigcup_{i:s_i\ge2}\bigl(V(G)\setminus V_i\bigr).
\]

Suppose first that \(p\ge2\). If every \(s_i\le1\), then the displayed formula gives \(I[S]=S\), so \(S\) cannot be a hull set. Conversely, suppose \(s_i\ge2\) for some \(i\). The first interval step contains every vertex outside \(V_i\). Because there is another non-singleton part \(V_j\) with \(j\ne i\), that first step contains all of \(V_j\), hence contains two vertices of \(V_j\). A second interval step using those two vertices adds every vertex outside \(V_j\), including all vertices of \(V_i\) that might have been missing. Thus the hull is all of \(V(G)\).

Suppose next that \(p=1\), with unique non-singleton part \(V_j\). No singleton part can contain two selected vertices. If fewer than two vertices of \(V_j\) are selected, no interval step adds anything. If \(2\le s_j<n_j\), the first interval step adds every vertex outside \(V_j\), but those outside parts are all singletons, so no new same-part pair is created; the process stabilizes while vertices of \(V_j\) remain missing. If \(s_j=n_j\), the pair already present in \(V_j\) adds every outside vertex in one step. Hence the hull sets are exactly the supersets of \(V_j\).

Finally, if \(p=0\), then \(G\) is complete. Every pair of distinct vertices is adjacent, so \(I[S]=S\) for all \(S\); hence only \(V(G)\) is a hull set.

For \(p\ge2\), the non-hull sets are exactly those choosing at most one vertex from each part. Their cardinality enumerator is \(\prod_i(1+n_i x)\), while all subsets have enumerator \((1+x)^N\), proving the first polynomial formula. The other two cases follow directly from their classifications. The description of inclusion-minimal hull sets and the hull-number formula are immediate.

## Verification
A standalone checker constructs every nondecreasing complete-multipartite profile of order at most nine with at least two parts, computes all-pairs graph distances, and for every vertex subset iterates the literal shortest-path interval operator to closure. It compares the resulting hull predicate against the theorem, then independently checks every enumerator coefficient and the minimum hull-set size. The replay output is:

`VERIFY_OK profiles=87 subset_checks=22932 hull_sets=12835 coefficient_checks=728 minimum_checks=87 max_order=9`

This finite census tests boundary cases and all small part profiles but is not used as an infinite proof; the proof above supplies the general argument.

## Relationship to prior work
Araujo, Campos, Giroire, Nisse, Sampaio, and Soares study geodetic convexity and algorithms for the hull number on several graph classes. Their full text notes that hull number is polynomial-time computable on cographs and extends algorithmic coverage to broader classes, but it does not state a complete-multipartite all-hull-set classification or a cardinality enumerator. Complete multipartite graphs are cographs, so their algorithmic results cover the scalar optimization problem in principle; accordingly, the scalar hull number is not treated here as the originality-bearing contribution.

Kante and Nourine give a linear-time method for finding a minimum hull set in distance-hereditary graphs and formalize the same shortest-path hull notion. Their inspected full manuscript contains no occurrence of “multipartite” or “complete bipartite.” The generic optimization result likewise does not imply the closed symbolic classification of every hull set for arbitrary part sizes or the displayed enumerator without additional analysis.

The present result is therefore positioned as an exact family-level structural classification and counting formula, not as a new complexity algorithm.

## Limitations
The theorem is specific to ordinary geodetic convexity on complete multipartite graphs. It does not address monophonic, triangle-path, or other graph convexities. The literature search cannot exclude an obscure earlier formula under alternate terminology; the strongest residual risk is an unindexed family-specific note. Generic cograph and distance-hereditary hull algorithms are known and cover minimum-hull computation, so only the explicit all-set classification and enumerator are claimed as new here.

## References
1. J. Araujo, V. Campos, F. Giroire, N. Nisse, L. Sampaio, and R. Soares, “On the hull number of some graph classes,” Theoretical Computer Science 475 (2013), 1–12. DOI: 10.1016/j.tcs.2012.12.035. An earlier repository version is HAL/INRIA inria-00576581.
2. M. M. Kante and L. Nourine, “Polynomial Time Algorithms for Computing a Minimum Hull Set in Distance-Hereditary and Chordal Graphs,” SIAM Journal on Discrete Mathematics 30 (2016), 311–326. DOI: 10.1137/15M1013389.
