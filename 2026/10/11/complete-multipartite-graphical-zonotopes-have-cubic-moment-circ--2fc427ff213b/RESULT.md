# Complete multipartite graphical zonotopes have cubic-moment circumspheres
## Finding
Let
\[
G=K_{n_1,\ldots,n_k},
\qquad
k\ge2,
\qquad
n_i\ge1,
\]
be a complete multipartite graph. Put
\[
N=\sum_{i=1}^k n_i.
\]
Its standard graphical zonotope is
\[
Z_G
=
\sum_{\{u,v\}\in E(G)}
[e_u,e_v]
\subset\mathbb R^N.
\tag{1}
\]

If \(v\) lies in part \(i\), then
\[
\deg(v)=N-n_i.
\]
The unique Euclidean circumcenter of \(Z_G\) is
\[
\boxed{
c_v=\frac{N-n_i}{2}.
}
\tag{2}
\]
Its squared circumradius is
\[
\boxed{
R^2
=
\frac{N^3-\sum_{i=1}^k n_i^3}{12}.
}
\tag{3}
\]
Because \(Z_G\) is centrally symmetric about \(c\),
\[
\boxed{
\operatorname{diam}(Z_G)
=
2R
=
\sqrt{
\frac{N^3-\sum_i n_i^3}{3}
}.
}
\tag{4}
\]

The circumsphere meets \(Z_G\) in exactly
\[
\boxed{k!}
\tag{5}
\]
vertices. They are the vertices indexed by the acyclic orientations obtained as follows: choose a total order of the \(k\) multipartite classes and orient every edge from the earlier class to the later class.

Equivalently, a farthest graphical-zonotope vertex is characterized by the fact that every pair of multipartite classes is oriented uniformly.

For the complete graph, where every \(n_i=1\), equation (3) reduces to the classical centered permutahedral value
\[
R^2=\frac{N(N^2-1)}{12}.
\]
For the complete bipartite graph \(K_{p,q}\), it becomes
\[
R^2=\frac{pq(p+q)}4.
\]

## Assumptions and scope
The graph is finite, simple, and complete multipartite with at least two nonempty parts. The realization is the standard graphical zonotope in (1), and distance is the ambient Euclidean distance on its affine span.

The theorem is realization-specific. Arbitrary affine images of the same zonotope need not have the same radius.

The circumradius is the radius of the smallest Euclidean ball containing the whole polytope. The diameter is the ordinary ambient Euclidean diameter, not the graph diameter of the one-skeleton.

## Proof
The cited graphical-zonotope literature defines
\[
Z_G=\sum_{\{u,v\}\in E(G)}[e_u,e_v]
\]
and identifies its vertices with acyclic orientations of \(G\).

The midpoint of the summand \([e_u,e_v]\) is
\[
\frac{e_u+e_v}{2}.
\]
Therefore the center of symmetry of \(Z_G\) is
\[
c=\frac12\sum_{\{u,v\}\in E(G)}(e_u+e_v),
\]
so its \(v\)-coordinate is
\[
c_v=\frac{\deg(v)}2.
\]
This proves (2).

A centrally symmetric compact convex body has its unique minimum enclosing ball centered at its symmetry center. Indeed, after translating the symmetry center to the origin, let \(x\) be a point of maximum norm \(R\). Any ball centered at \(q\) containing both \(x\) and \(-x\) must satisfy
\[
R_{\!q}^2
\ge
\frac{\|x-q\|^2+\|-x-q\|^2}{2}
=
R^2+\|q\|^2.
\]
Thus \(q=0\) is the unique optimal center.

Now fix an acyclic orientation \(\omega\) of \(G\), and let \(z_\omega\) be the corresponding graphical-zonotope vertex. Choosing the endpoint selected by each oriented edge shows that
\[
(z_\omega)_v=\operatorname{indeg}_\omega(v).
\]
Hence
\[
(z_\omega-c)_v
=
\operatorname{indeg}_\omega(v)-\frac{\deg(v)}2
=
\frac{
\operatorname{indeg}_\omega(v)-\operatorname{outdeg}_\omega(v)
}{2}.
\tag{6}
\]
Therefore
\[
4\|z_\omega-c\|^2
=
\sum_v
\left(
\operatorname{indeg}_\omega(v)-\operatorname{outdeg}_\omega(v)
\right)^2.
\tag{7}
\]

Write
\[
d_v=\deg(v),
\qquad
i_v=\operatorname{indeg}_\omega(v),
\qquad
o_v=\operatorname{outdeg}_\omega(v).
\]
Since
\[
(i_v-o_v)^2=d_v^2-4i_vo_v,
\]
equation (7) becomes
\[
\|z_\omega-c\|^2
=
\frac14\sum_v d_v^2
-
\sum_v i_vo_v.
\tag{8}
\]

Choose any topological ordering of \(\omega\). The quantity
\[
\sum_v i_vo_v
\]
counts triples
\[
u<v<w
\]
in that topological order for which both \(uv\) and \(vw\) are edges.

Classify triples by their multipartite classes.

If \(u,v,w\) lie in three distinct parts, exactly one contribution occurs, independently of their order.

If exactly two vertices, say \(u,w\), lie in the same part and the third vertex \(v\) lies in another part, the triple contributes exactly when the singleton \(v\) lies between the two same-part vertices in the topological order.

Triples lying in one part contribute nothing.

Thus
\[
\sum_v i_vo_v
=
\sum_{1\le i<j<\ell\le k}n_in_jn_\ell
+
I(\omega),
\tag{9}
\]
where \(I(\omega)\ge0\) is the number of interleaving triples consisting of two vertices from one part and a vertex from another part lying between them.

Consequently the squared norm in (8) is maximal exactly when
\[
I(\omega)=0.
\tag{10}
\]
Condition (10) holds exactly when every multipartite class is a contiguous block in a topological order. Indeed, any noncontiguous class has two of its vertices with a vertex of another class between them, producing an interleaving triple. Conversely, a block order has no such triple.

A block topological order is equivalent to totally ordering the multipartite classes and orienting all cross-edges from earlier classes to later classes. Hence there are exactly \(k!\) maximizing orientations, proving (5).

For such an orientation, equation (8) gives
\[
R^2
=
\frac14
\sum_{i=1}^k
n_i(N-n_i)^2
-
\sum_{i<j<\ell}n_in_jn_\ell.
\tag{11}
\]
Using
\[
\sum_i n_i=N
\]
and the elementary identity
\[
\sum_{i<j<\ell}n_in_jn_\ell
=
\frac{
N^3
-
3N\sum_i n_i^2
+
2\sum_i n_i^3
}{6},
\]
equation (11) simplifies to
\[
R^2
=
\frac{N^3-\sum_i n_i^3}{12},
\]
which proves (3).

Finally, a farthest vertex has an antipodal farthest vertex because \(Z_G\) is centrally symmetric. Their distance is \(2R\), and no pair can be farther than \(2R\) inside the radius-\(R\) enclosing ball. This proves (4).

## Verification
The proof is symbolic and applies to every complete multipartite graph with at least two nonempty parts.

The critical literature input was checked directly: the standard graphical zonotope is the Minkowski sum of the edge segments, and its vertices correspond to acyclic orientations. A second source explicitly identifies complete multipartite graphs as iterated joins of empty graphs and states that shuffling graphical zonotopes corresponds to graph join.

The accompanying `verify.py` exhaustively enumerates all distinct multipartite topological words for every integer partition of orders up to \(8\). For each word it reconstructs the centered indegree vector, computes its exact squared norm, verifies (3), and checks that the maximizing words are exactly the \(k!\) block orders. It also verifies (4). These finite calculations are corroborative only.

## Relationship to prior work
Padrol, Pilaud, and Poullot study graphical zonotopes and their deformation cones. Their full text recalls the standard Minkowski-sum realization and the acyclic-orientation model for vertices, then develops irredundant deformation-cone equations and inequalities. It does not state an Euclidean circumradius or diameter theorem.

Chapoton and Pilaud introduce shuffles of deformed permutahedra. Their full text emphasizes that the shuffle of graphical zonotopes is the graphical zonotope of the graph join, and explicitly notes that the join of empty graphs is a complete multipartite graph. This makes complete multipartite graphical zonotopes a natural iterated-shuffle family. Their results concern face structure, lattice properties, and related realizations rather than Euclidean circumspheres.

Targeted published-result and literature searches used “complete multipartite graphical zonotope”, “circumradius”, “Euclidean diameter”, “acyclic orientation”, “indegree imbalance”, “complete bipartite”, and “farthest vertex”. No statement was located that gives (3), the exact \(k!\) contact classification, or an implication covering them.

## Limitations
The theorem is restricted to complete multipartite graphs. For a general graph, maximizing (8) is an extremal problem over acyclic orientations and need not collapse to a closed cubic moment.

The formula concerns the standard unweighted graphical zonotope. Edge-weighted graphical zonotopes require a weighted version of the orientation-imbalance optimization.

The literature comparison cannot exclude an equivalent observation hidden in oriented-matroid, scheduling, or graph-imbalance terminology. The proof is short once the orientation-square identity (8) is written down, so folklore remains a genuine residual risk.

## References
1. Arnau Padrol, Vincent Pilaud, and Germain Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first public version 2021-11-24; Discrete & Computational Geometry 73 (2025), 447--465, DOI 10.1007/s00454-023-00586-x.
2. Frédéric Chapoton and Vincent Pilaud, *Shuffles of Deformed Permutahedra, Multiplihedra, Constrainahedra, and Biassociahedra*, arXiv:2201.06896, first public version 2022-01-18; Annales Henri Lebesgue 7 (2024), 1535--1601, DOI 10.5802/ahl.225.
