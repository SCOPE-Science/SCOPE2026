# Mixed metric dimension of complete multipartite graphs: a correction and full classification
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), \(N=\sum_i n_i\), and partite classes \(X_i\). For \(S\subseteq V(G)\), put \(C=V(G)\setminus S\). Then \(S\) is a mixed metric generator if and only if exactly one of the following holds: (i) \(C=\varnothing\); (ii) \(C=\{x\}\) with \(x\in X_i\) and \(n_j\ge2\) for every \(j\ne i\); or (iii) \(r=2\), \(C=\{x,y\}\) with one omitted vertex in each part, and \(n_1,n_2\ge3\). Consequently, if \(q=|\{i:n_i=1\}|\), the mixed resolving-set enumerator is \[\mathcal M_G(z)=z^N+A z^{N-1}+B z^{N-2},\] where \(A=N\) for \(q=0\), \(A=1\) for \(q=1\), \(A=0\) for \(q\ge2\), and \(B=n_1n_2\) exactly when \(r=2\) and \(\min(n_1,n_2)\ge3\), with \(B=0\) otherwise. Hence \[\operatorname{mdim}(G)=\begin{cases}N-2,&r=2\text{ and }\min(n_1,n_2)\ge3,\\N,&q\ge2,\\N-1,&\text{otherwise}.\end{cases}\] This agrees with the original complete-bipartite theorem, but corrects the 2022 claimed complete-multipartite extension; for example, \(\operatorname{mdim}(K_{3,3,5})=10\), not \(8\).

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. Let \(G=K_{n_1,\ldots,n_r}\) with \(r\ge2\), partite classes \(X_1,\ldots,X_r\), and \(N=\sum_i n_i\). For a vertex \(w\), the distance to an edge \(uv\) is \(d(w,uv)=\min\{d(w,u),d(w,v)\}\). A set \(S\subseteq V(G)\) is a mixed metric generator when every two distinct elements of \(V(G)\cup E(G)\) have distinct distance vectors to \(S\).

The polynomial \(\mathcal M_G(z)\) used here is the size enumerator of all mixed metric generators; it is not assumed to be a standard named polynomial.

## Proof
Fix \(S\subseteq V(G)\) and write \(C=V(G)\setminus S\). For a landmark \(s\in S\), a vertex \(v\) has coordinate
\[
d(s,v)=\begin{cases}0,&s=v,\\2,&s\ne v\text{ and }s,v\in X_i\text{ for some }i,\\1,&\text{otherwise}.\end{cases}
\]
For an edge \(uv\), whose endpoints lie in different parts,
\[
d(s,uv)=\begin{cases}0,&s\in\{u,v\},\\1,&s\notin\{u,v\}.\end{cases}
\]
Thus an edge code records exactly which of its endpoints belong to \(S\).

If two omitted vertices lie in the same part, they have identical vertex codes, so \(C\) contains at most one vertex from each part. If \(|C|\ge3\), the omitted vertices lie in distinct parts and hence induce a clique. Distinct edges among three omitted vertices all have the all-ones edge code, so \(|C|\le2\).

Suppose \(C=\{x,y\}\). The two omitted vertices must lie in distinct parts. If \(r\ge3\), choose a selected vertex \(s\) from a third part. Then the distinct edges \(sx\) and \(sy\) have the same edge code: zero at \(s\) and one at every other landmark. Therefore \(r=2\). In this bipartite case, if one part has size one, its omitted vertex has the all-ones vertex code and collides with the omitted edge \(xy\). If one part has size two, its unique selected vertex \(s\) collides with the edge joining \(s\) to the omitted vertex in the other part. Hence both part sizes must be at least three. Conversely, when \(r=2\) and both parts have size at least three, omitting one vertex from each part leaves at least two landmarks in each part. Vertex codes are then distinct, edge codes are determined by their selected endpoints, and every vertex-edge pair is separated either by a selected same-part mate or by a selected endpoint of the edge. Hence every such complement of size two is valid.

Now suppose \(C=\{x\}\) with \(x\in X_i\). If some other part \(X_j=\{s\}\) is a singleton, then the selected vertex \(s\) and the edge \(sx\) have the same mixed code: zero at \(s\) and one at every other landmark. Therefore every part other than \(X_i\) must have size at least two. Conversely assume that condition. Edge-edge collisions cannot occur because there is only one omitted endpoint. Two vertex codes cannot coincide because at most one vertex is omitted. For a selected vertex \(v\), any incident edge is distinguished from \(v\) by either a selected same-part mate or its other selected endpoint; the only possible obstruction would be a selected singleton outside the omitted part, which the hypothesis excludes. The omitted vertex \(x\) is distinguished from every edge because every edge has a selected endpoint. Thus \(S\) is mixed resolving.

Finally, \(C=\varnothing\) is always valid. This proves the classification.

Counting admissible complements gives the enumerator. If there are no singleton parts, every one-vertex complement is allowed, giving \(A=N\). With exactly one singleton part, the only allowed one-vertex complement is that singleton, so \(A=1\). With at least two singleton parts, no one-vertex complement is allowed. Two-vertex complements occur exactly in the bipartite case with both part sizes at least three, and there are \(n_1n_2\) choices. Taking the smallest exponent with nonzero coefficient yields the stated mixed metric dimension formula.

## Verification
The included checker constructs every complete multipartite isomorphism type of orders two through ten. For each vertex subset it forms the distance vector of every vertex and every edge directly from the graph metric, tests whether all element codes are distinct, and compares that definition-level result with the complement classification and every coefficient of \(\mathcal M_G(z)\). It also evaluates \(K_{3,3,5}\) directly.

## Relationship to prior work
The 2016 paper introducing mixed metric dimension proves the complete-bipartite formula: for \(K_{a,b}\) with \(a,b\ge2\), the value is \(a+b-1\) when one part has size two and \(a+b-2\) otherwise. The theorem above agrees exactly on that domain and extends the description from the minimum value to every mixed metric generator.

A 2022 paper states a formula for arbitrary complete multipartite graphs, claiming \(N-1\) when some part has size two and \(N-r\) otherwise. The full theorem does not survive direct code comparison once three or more parts are present. Its example \(K_{3,3,5}\) is decisive: the published formula gives \(11-3=8\), while the classification above forces every mixed generator to omit at most one vertex and the direct checker finds minimum size \(10\). The corrected theorem also handles singleton parts, where multiple omitted singleton parts create unresolved vertex or vertex-edge collisions.

Targeted searches for complete multipartite mixed metric dimension, mixed resolving sets, the \(K_{3,3,5}\) example, and later corrections did not locate a published correction or an equivalent all-set classification.

## Limitations
The result is restricted to connected complete multipartite graphs. The finite exhaustive verification is corroborative only; the all-orders statement follows from the proof. The original complete-bipartite theorem remains valid and is genuine prior coverage of that special case. A later erratum or differently phrased correction not found by the searches remains a residual literature risk.

## References
1. A. Kelenc, D. Kuziak, A. Taranenko, I. G. Yero, “Mixed metric dimension of graphs,” arXiv:1611.04292v1 (14 November 2016); Applied Mathematics and Computation 314 (2017), 429–438, DOI 10.1016/j.amc.2017.07.027.
2. S. Hayat, A. Khan, Y. Zhong, “On Resolvability- and Domination-Related Parameters of Complete Multipartite Graphs,” Mathematics 10(11) (2022), 1815, DOI 10.3390/math10111815.
