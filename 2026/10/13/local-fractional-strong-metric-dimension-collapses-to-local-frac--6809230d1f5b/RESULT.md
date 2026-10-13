# Local fractional strong metric dimension collapses to local fractional metric dimension
## Finding
For every finite connected simple graph \(G\) and every edge \(uv\),
\[
L_S(u,v)=L(u,v),
\]
where \(L_S(u,v)\) is the local strong resolving neighborhood and \(L(u,v)\) is the ordinary local resolving neighborhood.

Therefore the two linear programs have exactly the same feasible functions. In particular,
\[
\operatorname{lsdim}_f(G)=\operatorname{ldim}_f(G),
\]
and the complete sets of minimum local strong resolving functions and minimum local resolving functions are identical.

A direct consequence is
\[
\operatorname{lsdim}_f(G)=1
\quad\Longleftrightarrow\quad
G\text{ is bipartite}.
\]
Thus the previously stated path-only characterization for value one does not hold under the published definitions; the four-cycle \(C_4\) is an immediate counterexample.

## Assumptions and scope
All graphs are finite, simple, and connected.

For an edge \(uv\), the local resolving neighborhood is
\[
L(u,v)=\{w\in V(G):d(w,u)\ne d(w,v)\}.
\]

The local strong resolving neighborhood is
\[
L_S(u,v)=
\{w\in V(G):
u\text{ lies on a }w\text{-}v\text{ geodesic, or }
v\text{ lies on a }w\text{-}u\text{ geodesic}\}.
\]

A local resolving function is a map
\[
f:V(G)\to[0,1]
\]
such that
\[
\sum_{w\in L(u,v)}f(w)\ge1
\]
for every edge \(uv\). A local strong resolving function is defined by the same inequality with \(L_S(u,v)\) in place of \(L(u,v)\).

The quantities \(\operatorname{ldim}_f(G)\) and \(\operatorname{lsdim}_f(G)\) are the minimum total weights of these two classes of functions.

## Proof
Fix an edge \(uv\) and a vertex \(w\).

Because \(u\) and \(v\) are adjacent, the triangle inequality gives
\[
|d(w,u)-d(w,v)|\le1.
\]
The two distances are integers. Hence
\[
d(w,u)\ne d(w,v)
\]
if and only if
\[
|d(w,u)-d(w,v)|=1.
\]

Assume first that \(w\in L(u,v)\). After exchanging \(u\) and \(v\) if necessary,
\[
d(w,u)=d(w,v)+1.
\]
Take a shortest \(w\)-\(v\) path and append the edge \(vu\). The resulting \(w\)-\(u\) walk has length
\[
d(w,v)+1=d(w,u),
\]
so it is a geodesic and contains \(v\). Therefore \(w\) strongly resolves \(u\) and \(v\), and
\[
w\in L_S(u,v).
\]

Conversely, suppose \(w\in L_S(u,v)\). If \(v\) lies on a \(w\)-\(u\) geodesic, then, because \(uv\) is an edge,
\[
d(w,u)=d(w,v)+1.
\]
If \(u\) lies on a \(w\)-\(v\) geodesic, then
\[
d(w,v)=d(w,u)+1.
\]
In either case the two distances differ, so
\[
w\in L(u,v).
\]

Thus
\[
L_S(u,v)=L(u,v)
\]
for every edge \(uv\).

Every local strong resolving constraint is therefore literally the corresponding local resolving constraint. The feasible polytopes coincide, so their minimum weights and all minimizers coincide:
\[
\operatorname{lsdim}_f(G)=\operatorname{ldim}_f(G).
\]

The foundational local-fractional paper proves
\[
\operatorname{ldim}_f(G)=1
\]
if and only if \(G\) is bipartite. Hence the same characterization holds for \(\operatorname{lsdim}_f\).

For the explicit counterexample \(C_4\), every vertex has unequal distances to the endpoints of every edge, so every local and local-strong resolving neighborhood is \(V(C_4)\). The constant function of weight \(1/4\) on each vertex is feasible and has total weight \(1\).

## Verification
The included checker exhaustively enumerates every connected labeled graph on \(2\) through \(6\) vertices. For every edge and every vertex, it computes shortest-path distances and independently evaluates membership in the local resolving neighborhood and in the local strong resolving neighborhood.

It also checks \(C_4\) explicitly and confirms that every local and local-strong resolving neighborhood is the whole vertex set.

## Relationship to prior work
The fractional local metric dimension was introduced in a 2018 preprint and later journal publication. That work defines \(L(u,v)\) by unequal distances to adjacent endpoints, gives the associated fractional linear program, lists MSC \(05C12\), and proves that the parameter equals one exactly for bipartite graphs.

A 2021 IEEE Access paper introduced local fractional strong metric dimension using strong resolution restricted to adjacent pairs. Its published definitions are exactly the two definitions compared above. That paper stated only
\[
\operatorname{ldim}_f(G)\le\operatorname{lsdim}_f(G)
\]
and subsequently asserted that \(\operatorname{lsdim}_f(G)=1\) exactly for paths.

A 2023 continuation uses the same local-strong definition and computes additional graph families. In particular, its even-cycle value is one, which is consistent with the equality theorem above and already incompatible with a path-only value-one characterization.

The equality of the two neighborhoods for adjacent vertices makes the distinction disappear at the definition level. Hence every theorem about local fractional metric dimension transfers immediately to local fractional strong metric dimension, and no separate optimization is required.

## Limitations
The collapse uses adjacency essentially. For arbitrary nonadjacent vertex pairs, unequal distance and strong resolution are different conditions, so ordinary fractional metric dimension and fractional strong metric dimension do not collapse by this argument.

The theorem concerns the published local-strong definition based on adjacent vertex pairs. A differently defined parameter using another locality condition would require a separate analysis.

The computational verification is corroborative only; the equality for all connected graphs follows from the two-line distance argument in the proof.

## References
1. H. Benish, M. Murtaza, I. Javaid, “The Fractional Local Metric Dimension of Graphs,” arXiv:1810.02882v1, 5 October 2018; Contributions to Discrete Mathematics 19(3) (2024), 163–177, DOI 10.55016/ojs/cdm.v19i3.62807.
2. F. Jamil, A. Kashif, S. Zafar, Z. Bassfar, A. M. Alanazi, “Local Fractional Strong Metric Dimension of Certain Rotationally Symmetric Planer Networks,” IEEE Access 9 (2021), 159326–159333, DOI 10.1109/ACCESS.2021.3131311.
3. F. Jamil, A. Kashif, S. Zafar, M. O. Ojiema, M. Wang, “Local Fractional Strong Metric Dimension of Certain Complex Networks,” Complexity 2023, Article 3635342, DOI 10.1155/2023/3635342.
