# Correction and all-set classification for edge metric dimension of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph of order \(N\ge3\), with \(r\ge2\). A set \(S\subseteq V(G)\) is edge resolving if and only if, writing \(T=V(G)\setminus S\), either \(r\ge3\) and \(|T|\le1\), or \(r=2\) and \(T\) has size at most one or consists of one vertex from each bipartition class. Consequently \[\operatorname{edim}(G)=\begin{cases}N-2,&r=2,\\N-1,&r\ge3.\end{cases}\] The number of edge metric bases is \(n_1n_2\) when \(r=2\) and \(N\) when \(r\ge3\), and the complete edge-resolving-set enumerator is \[E_G(z)=z^N+Nz^{N-1}+\mathbf 1_{\{r=2\}}n_1n_2z^{N-2}.\] This corrects the published 2022 formula \(\operatorname{edim}(K_{n_1,\ldots,n_r})=N-r\), which is valid for the bipartite case but false for every \(r\ge3\).

## Assumptions and scope
All graphs are finite, simple, and connected. Let \(G=K_{n_1,\ldots,n_r}\) have partite classes \(X_1,\ldots,X_r\), where \(r\ge2\) and \(N=\sum_i n_i\ge3\). For a vertex \(s\) and an edge \(e=uv\), define
\[
d(s,e)=\min\{d(s,u),d(s,v)\}.
\]
A set \(S\subseteq V(G)\) is edge resolving when every two distinct edges have different distance vectors to \(S\). The edge metric dimension is the minimum size of such a set. The order-two graph \(K_2\) is excluded from the main formula only to avoid the standard nonempty-generator convention for a graph with a single edge.

## Proof
Fix \(S\subseteq V(G)\) and put \(T=V(G)\setminus S\). For any edge \(e=uv\) and landmark \(s\in S\),
\[
d(s,e)=\begin{cases}0,&s\in\{u,v\},\\1,&s\notin\{u,v\}.\end{cases}
\]
If \(s\) is not an endpoint, it is adjacent to at least one endpoint because \(u\) and \(v\) lie in different parts. Hence an edge-distance vector records exactly which endpoints lie in \(S\). Thus two edges \(e,f\) have the same representation exactly when
\[
e\cap S=f\cap S.
\]

Assume \(r\ge3\). If \(|T|\le1\), this intersection map is injective. Conversely, if two omitted vertices \(x,y\) lie in one part, choose any vertex \(z\) outside that part. When \(z\in S\), the edges \(zx\) and \(zy\) both intersect \(S\) in \(\{z\}\); when \(z\in T\), both intersect it in the empty set. If two omitted vertices lie in distinct parts and \(|T|=2\), a vertex in a third part lies in \(S\) and creates the same one-vertex collision. If \(|T|\ge3\), either the previous same-part case occurs or omitted vertices occupy at least three parts, in which case two distinct edges entirely in \(T\) both have empty intersection with \(S\). Hence for at least three parts, exactly the complements of sets of size at most one are edge resolving.

Now let \(r=2\). Complements of size at most one are again edge resolving. If \(T=\{x,y\}\) contains one vertex from each part, the unique edge entirely in \(T\) has empty intersection with \(S\); for each \(s\in S\), exactly one of \(x,y\) is adjacent to \(s\), so at most one edge intersects \(S\) in \(\{s\}\); fully selected edges are identified by their two endpoints. Thus such a set is edge resolving. Two omitted vertices in one part fail by the same one-vertex collision, while any omitted set of size at least three either lies in one part or contains at least two distinct edges entirely in \(T\). This proves the classification.

The minimum sizes, basis counts, and enumerator follow immediately. In particular, for \(r=2\) one omits one vertex from each part, giving \(n_1n_2\) bases of size \(N-2\); for \(r\ge3\), one omits exactly one of the \(N\) vertices, giving \(N\) bases of size \(N-1\).

The published 2022 construction omits one vertex from every part. With three or more parts, two edges among three omitted vertices both have empty intersection with the proposed landmark set and therefore identical all-one distance vectors. For the paper's explicit \(K_{2,3,5}\) example, the published value is \(7\), whereas the corrected value is \(9\).

## Verification
The included checker reconstructs every connected complete multipartite isomorphism type of orders \(3\) through \(10\). It computes all-pairs distances by breadth-first search and, for every vertex subset, forms all edge-distance vectors directly from the definition. It compares the observed resolving sets with the structural classification, minimum dimension, basis count, and enumerator coefficients. It also checks the published-style seven-vertex construction for \(K_{2,3,5}\) and an explicit edge-code collision.

## Relationship to prior work
Kelenc, Tratnik, and Yero introduced edge metric dimension and proved that every complete bipartite graph other than \(K_{1,1}\) has edge metric dimension equal to its order minus two. Their published full text was inspected at the definition and Remark 2.

Hayat, Khan, and Zhong published an arbitrary complete-multipartite formula in 2022. Their Theorem 4 states \(\operatorname{edim}(K_{n_1,\ldots,n_r})=N-r\) and proposes omitting one vertex from each part; Example 3 applies this to \(K_{2,3,5}\), obtaining \(7\). The proof above shows that the construction stops resolving edges as soon as a third part is present.

Targeted searches for the article title, complete-multipartite edge metric dimension, the formula \(N-r\), corrections or errata, and the alternative value \(N-1\) did not locate a later correction. Semantic literature searches returned other complete-multipartite resolving invariants rather than an ordinary edge-metric correction.

## Limitations
The theorem concerns ordinary vertex-based edge metric dimension. It does not address edge multiset dimension, dominant edge metric dimension, fault-tolerant edge resolution, or mixed metric dimension. The finite exhaustive verification is corroborative only; the arbitrary-order classification follows from the proof. Literature search coverage cannot exclude an unindexed or differently phrased correction.

## References
1. A. Kelenc, N. Tratnik, I. G. Yero, “Uniquely identifying the edges of a graph: The edge metric dimension,” Discrete Applied Mathematics 251 (2018), 204–220, arXiv:1602.00291v1, DOI 10.1016/j.dam.2018.05.052.
2. S. Hayat, A. Khan, Y. Zhong, “On Resolvability- and Domination-Related Parameters of Complete Multipartite Graphs,” Mathematics 10(11) (2022), 1815, DOI 10.3390/math10111815.
