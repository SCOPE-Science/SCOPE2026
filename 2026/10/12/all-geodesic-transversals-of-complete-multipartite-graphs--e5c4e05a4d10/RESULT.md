# All geodesic transversals of complete multipartite graphs
## Finding
Let
\[
G=K_{n_1,\ldots,n_r},\qquad r\ge2,\qquad N=\sum_{i=1}^r n_i,
\]
with partite classes \(V_1,\ldots,V_r\). Put
\[
I=\{i:n_i\ge2\},\qquad q=|I|,\qquad s=r-q,
\]
and let
\[
M=\max_{i\in I}n_i,
\]
with \(M=0\) when \(I=\varnothing\). For \(S\subseteq V(G)\), write
\[
T=V(G)\setminus S.
\]

Then \(S\) is a geodesic transversal if and only if one of the following holds:

1. \(T\subseteq V_i\) for some non-singleton part \(V_i\); or
2. \(|T\cap V_i|\le1\) for every non-singleton part and \(T\) contains at most one vertex belonging to a singleton part.

Thus, if
\[
c=q+\mathbf 1_{\{s>0\}},
\]
then
\[
\operatorname{gt}(G)=N-\max\{M,c\}.
\]

The complete complement-size enumerator is
\[
C_G(y)
=(1+sy)\prod_{i\in I}(1+n_i y)
+\sum_{i\in I}\bigl((1+y)^{n_i}-1-n_i y\bigr).
\]
Equivalently, the geodesic-transversal size enumerator is
\[
\mathcal T_G(z)
=\sum_{S\text{ geodesic transversal}}z^{|S|}
=z^N C_G(z^{-1}).
\]

Minimum transversals are classified by the two competing maximum complement types. If \(M>c\), their complements are precisely the whole partite classes of size \(M\). If \(c>M\), their complements choose one vertex from every non-singleton part and, when \(s>0\), exactly one singleton-part vertex. If \(M=c\), both families occur.

Writing
\[
a=|\{i\in I:n_i=M\}|,
\qquad
b=\bigl(s\mathbf 1_{\{s>0\}}+\mathbf 1_{\{s=0\}}\bigr)\prod_{i\in I}n_i,
\]
the number of minimum geodesic transversals is
\[
\begin{cases}
a,&M>c,\\
b,&c>M,\\
a+b,&M=c.
\end{cases}
\]

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. A geodesic is a shortest path. A maximal geodesic is a geodesic that is not a proper subpath of any longer geodesic. A geodesic transversal is a vertex set meeting every maximal geodesic.

The theorem applies to all connected complete multipartite graphs, including complete graphs, stars, complete bipartite graphs, and Turán graphs.

## Proof
Every connected noncomplete complete multipartite graph has diameter two. Fix a part \(V_i\) with \(n_i\ge2\). For distinct \(u,v\in V_i\) and any \(w\notin V_i\), the path
\[
u-w-v
\]
is a geodesic of length two. Since the graph has diameter two, every such length-two geodesic is maximal.

Now consider an edge \(xy\) with \(x\in V_i\) and \(y\in V_j\), \(i\ne j\). If \(n_i\ge2\), choose \(x'\in V_i\setminus\{x\}\); then
\[
x-y-x'
\]
is a length-two geodesic containing \(xy\). The same holds if \(n_j\ge2\). Therefore the edge \(xy\) is itself a maximal geodesic exactly when both endpoint parts are singletons.

Hence the maximal geodesics are precisely:

- all length-two paths whose endpoints are two vertices of one non-singleton part and whose middle vertex lies outside that part; and
- all edges joining two singleton parts.

A set \(S\) is a geodesic transversal exactly when its complement \(T\) contains no maximal geodesic in full.

Suppose first that \(T\) contains at least two vertices from a non-singleton part \(V_i\). If \(T\) also contains any vertex \(w\notin V_i\), then two of the omitted vertices in \(V_i\), together with \(w\), form an omitted maximal length-two geodesic. Thus in this case necessarily
\[
T\subseteq V_i.
\]
Conversely, every subset contained in one part contains no maximal geodesic, because every maximal length-two geodesic with endpoints in that part has its middle vertex outside the part.

It remains to consider complements that contain at most one vertex from each non-singleton part. Such a complement cannot contain a maximal length-two geodesic. It contains a maximal edge exactly when it contains two vertices from two singleton parts. Therefore it is valid exactly when it contains at most one singleton-part vertex. This proves the classification.

The largest complement of the first type has size \(M\). The largest complement of the second type has size
\[
c=q+\mathbf 1_{\{s>0\}},
\]
so
\[
\operatorname{gt}(G)=N-\max\{M,c\}.
\]

For enumeration, the sparse second family contributes
\[
(1+sy)\prod_{i\in I}(1+n_i y),
\]
because one may choose zero or one vertex from every non-singleton part and zero or one vertex from the union of all singleton parts. The remaining valid complements are, for each non-singleton part, its subsets of size at least two. Their contribution is
\[
\sum_{i\in I}\bigl((1+y)^{n_i}-1-n_i y\bigr).
\]
These families are disjoint, giving \(C_G(y)\). Replacing \(y\) by \(z^{-1}\) and multiplying by \(z^N\) converts complement size into transversal size.

The basis classification follows by identifying which valid complements attain the larger of \(M\) and \(c\). The corresponding counts are immediate from choosing a largest part, or choosing one vertex from each non-singleton part together with one singleton vertex when such vertices exist.

## Verification
The included checker constructs every connected complete multipartite isomorphism type of orders \(2\) through \(10\). It generates maximal geodesics directly: all shortest paths of length two and every edge not contained in such a path. It then tests every vertex subset against the literal hitting-set definition.

For each graph, the direct result is compared with the complement classification, every coefficient of \(C_G(y)\), the formula for \(\operatorname{gt}(G)\), and the stated basis count.

## Relationship to prior work
The geodesic-transversal problem was introduced in 2021 and shown to be computationally difficult in general, with exact algorithms and results for selected graph families. An independently introduced equivalent formulation called the maximal shortest paths cover number appeared later in 2021.

A 2021–2022 paper on joins and lexicographic products proves a general formula for the scalar geodesic-transversal number of a join and explicitly recovers
\[
\operatorname{gt}(K_{p,q})=\min\{p,q\}
\]
for complete bipartite graphs. Since complete multipartite graphs are iterated joins of independent sets, that theorem provides broad scalar context and can be specialized recursively to this family.

The present result is stronger in a different direction: it characterizes every geodesic transversal, gives the complete cardinality distribution, classifies all minimum sets, and makes the two competing complement mechanisms explicit for arbitrary part profiles. Targeted searches under geodesic transversal, maximal shortest paths cover, complete multipartite, complete \(r\)-partite, Turán, and complete bipartite terminology did not locate this all-set classification or enumerator.

## Limitations
The scalar value is related to, and in principle can be recovered from, the published general theorem for graph joins. The originality claim is therefore not that the minimum alone is inaccessible from prior theory; it is the complete arbitrary-part-size classification, exact size enumerator, and full basis description.

No claim is made here about geodesic packing, weighted transversals, or the \(k\)-geodesic-transversal variants.

The finite computation through order \(10\) is corroborative only. The theorem for arbitrary part sizes follows from the explicit classification of maximal geodesics.

## References
1. P. Manuel, B. Brešar, S. Klavžar, “The geodesic-transversal problem,” arXiv:2101.08042v1, 20 January 2021; Applied Mathematics and Computation 413 (2022), 126621, DOI 10.1016/j.amc.2021.126621.
2. I. Peterin, G. Semanišin, “On the Maximal Shortest Paths Cover Number,” Mathematics 9(14) (2021), 1592, DOI 10.3390/math9141592.
3. I. Peterin, G. Semanišin, “Geodesic transversal problem for join and lexicographic product of graphs,” Computational and Applied Mathematics 41 (2022), DOI 10.1007/s40314-022-01834-1.
4. P. Manuel, B. Brešar, S. Klavžar, “Geodesic packing in graphs,” arXiv:2210.15325v1, 27 October 2022; Applied Mathematics and Computation 459 (2023), 128277, DOI 10.1016/j.amc.2023.128277.
