# All local edge resolving sets of complete split graphs
## Finding
Let
\[
S_{m,n}=K_m\vee\overline{K_n},
\qquad
m,n\ge1,
\]
be the complete split graph with clique
\[
C=\{c_1,\ldots,c_m\}
\]
and independent set
\[
I=\{u_1,\ldots,u_n\}.
\]
Put
\[
N=m+n.
\]

Under the standard convention that a local edge metric generator is nonempty, the complete classification is as follows.

If
\[
m\ge2,
\]
then \(R\subseteq V(S_{m,n})\) is local edge resolving if and only if
\[
|V(S_{m,n})\setminus R|\le1.
\]
Therefore
\[
\operatorname{edim}_{\ell}(S_{m,n})=N-1,
\]
there are exactly \(N\) local edge metric bases, and the complete size enumerator is
\[
L_{m,n}(z)=z^N+Nz^{N-1}.
\]

If
\[
m=1,\qquad n\ge2,
\]
then \(S_{1,n}\) is a star. A set \(R\) is local edge resolving if and only if it contains at least \(n-1\) independent vertices; the center may be selected or omitted. Hence
\[
\operatorname{edim}_{\ell}(S_{1,n})=n-1=N-2,
\]
there are exactly \(n\) bases, and
\[
L_{1,n}(z)=z^{n-1}(n+z)(1+z).
\]

For the one-edge graph
\[
S_{1,1}=K_2,
\]
there is no adjacent pair of distinct edges. With the nonempty-generator convention, every nonempty vertex set is local edge resolving, so
\[
\operatorname{edim}_{\ell}(K_2)=1
\]
and
\[
L_{1,1}(z)=2z+z^2.
\]

Thus adding a second clique vertex causes a sharp transition: the star family permits the center to be irrelevant and one leaf to be omitted, whereas every larger complete split graph permits at most one omitted vertex anywhere in the graph.

## Assumptions and scope
Graphs are finite, simple, connected, and undirected.

For a vertex \(x\) and edge \(e=uv\), define
\[
d(x,e)=\min\{d(x,u),d(x,v)\}.
\]
A nonempty set \(R\subseteq V(G)\) is a local edge metric generator if every two adjacent edges \(e,f\) have different distance vectors to \(R\). The local edge metric dimension is the minimum cardinality of such a set.

The theorem concerns complete split graphs
\[
K_m\vee\overline{K_n}.
\]

## Proof
Consider two adjacent edges
\[
xy,\ yz
\]
with common endpoint \(y\) and distinct nonshared endpoints \(x,z\).

In a complete split graph, for every landmark
\[
w\notin\{x,z\},
\]
the two edge distances are equal:
\[
d(w,xy)=d(w,yz).
\]
Indeed, this can be checked by the four possible edge-type configurations.

If both nonshared endpoints are independent vertices, then the common endpoint is a clique vertex. Every other clique vertex is adjacent to all three relevant vertices, while every other independent vertex has distance one to the common clique endpoint and distance two to the two independent endpoints. In either case the minimum distance to both edges is the same.

If both nonshared endpoints are clique vertices, then the common endpoint may lie in the clique or in the independent set. Every other clique vertex has distance at most one to both edges, and every independent vertex has distance one to every clique endpoint. Again the two minima agree.

If one nonshared endpoint is in the clique and the other in the independent set, then the common endpoint must lie in the clique. A third clique vertex is adjacent to every endpoint involved, while a different independent vertex is adjacent to both clique endpoints and at distance two from the independent endpoint. The minimum distance is again the same for both edges.

By contrast, the nonshared endpoints distinguish:
\[
d(x,xy)=0<d(x,yz),
\qquad
d(z,yz)=0<d(z,xy).
\]
Hence the local resolving neighborhood of any adjacent edge pair is exactly
\[
\{x,z\}.
\tag{1}
\]

Suppose first that \(m\ge2\). Every unordered pair of distinct vertices can occur as the two nonshared endpoints of adjacent edges.

For two independent vertices, use any clique vertex as the common endpoint.

For two clique vertices, if there is a third clique vertex it can be the common endpoint; when \(m=2\), any independent vertex can be the common endpoint.

For a clique vertex \(c\) and an independent vertex \(u\), choose a second clique vertex \(c'\). Then
\[
cc',\ c'u
\]
are adjacent edges whose nonshared endpoints are \(c,u\).

Therefore, by (1), a local edge metric generator must meet every two-element subset of \(V(S_{m,n})\). Equivalently,
\[
|V\setminus R|\le1.
\]
Conversely, every set omitting at most one vertex meets every pair \(\{x,z\}\), so (1) shows that it resolves every adjacent edge pair. This proves the classification for \(m\ge2\).

Now let \(m=1\). The graph is a star with center \(c\). Every adjacent pair of distinct edges has the form
\[
cu_i,\ cu_j,
\]
and by (1) its resolving neighborhood is exactly
\[
\{u_i,u_j\}.
\]
Thus \(R\) is local edge resolving precisely when it meets every two-element subset of the leaf set \(I\), or equivalently
\[
|I\setminus R|\le1.
\]
The center is unrestricted. This yields the star classification and its enumerator.

The basis counts and dimensions follow immediately from the minimum valid sizes in the classified set families.

## Verification
The included checker constructs every complete split graph
\[
S_{m,n}
\]
with
\[
1\le m,n\le6.
\]
It computes all-pairs vertex distances by breadth-first search, forms the edge-distance vectors directly from the definition, and tests every vertex subset against every adjacent edge pair.

It compares the direct result with the theorem's structural classification and independently checks every minimum dimension and basis count.

## Relationship to prior work
Local edge metric dimension was introduced in 2020. The introducing paper computes exact values for paths, ladders, cycles, stars, and wheels. Its searchable full text contains no split-graph occurrence. In particular, it proves the star value, which is recovered here as the \(m=1\) boundary while the present theorem classifies every local edge resolving set.

Later work formulates the parameter by integer programming and determines local edge metric dimensions for corona and edge-corona products. That source explicitly places the parameter in MSC 2020 class \(05C12\), but it does not state a complete-split formula in the inspected abstract and metadata.

The complete split result is not implied by ordinary edge metric dimension. Local edge resolution compares only adjacent edge pairs; the proof above shows that on complete split graphs those local comparisons already force the sharp global pair-hitting structure.

## Limitations
The theorem concerns local edge metric dimension, not ordinary edge metric dimension, local vertex metric dimension, fractional local edge dimension, or local edge partition dimension.

The one-edge graph \(K_2\) is treated separately because the introducing definition requires a nonempty generator even though there is no adjacent pair of distinct edges.

The exhaustive verification is corroborative only. The arbitrary-parameter result follows from the exact local resolving neighborhood calculation in the proof.

A differently named or non-indexed complete-split treatment may exist despite targeted searches.

## References
1. R. Adawiyah, Dafik, R. Alfarisi, R. M. Prihandini, I. H. Agustin, M. Venkatachalam, “The local edge metric dimension of graph,” Journal of Physics: Conference Series 1543 (2020), 012009, DOI 10.1088/1742-6596/1543/1/012009.
2. F. Amini, M. A. Henning, M. Tavakoli, “Local edge metric dimensions via corona products and integer linear programming,” Computational and Applied Mathematics 43 (2024), Article 358, DOI 10.1007/s40314-024-02879-0.
