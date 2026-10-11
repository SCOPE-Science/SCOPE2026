# Every connected cosmological polytope has graph-independent Euclidean circumradius
## Finding
Let
\[
G=(V,E)
\]
be a finite connected simple graph with at least one edge, and put
\[
D=|V|+|E|.
\]
Use the standard orthonormal coordinate basis
\[
\{\mathbf x_v:v\in V\}\cup\{\mathbf y_e:e\in E\}
\]
of
\[
\mathbb R^D.
\]

For every edge
\[
e=\{u,v\},
\]
the standard cosmological polytope
\[
P_G
\]
has the three vertices
\[
p_e=\mathbf x_u+\mathbf x_v-\mathbf y_e,
\]
\[
p_{e,u}=\mathbf x_u-\mathbf x_v+\mathbf y_e,
\]
and
\[
p_{e,v}=-\mathbf x_u+\mathbf x_v+\mathbf y_e.
\tag{1}
\]

Define
\[
c_G
=
\frac1D
\left(
\sum_{v\in V}\mathbf x_v
+
\sum_{e\in E}\mathbf y_e
\right).
\tag{2}
\]
Then \(c_G\) is the unique center of the minimum enclosing Euclidean ball of \(P_G\), and
\[
\boxed{
R(P_G)
=
\sqrt{3-\frac1D}.
}
\tag{3}
\]

Every one of the
\[
3|E|
\]
vertices in (1) lies on the boundary of this minimum enclosing ball. Thus the Euclidean circumradius is independent of the incidence pattern of \(G\): among connected graphs it depends only on
\[
|V|+|E|.
\]

There is also an explicit positive contact certificate. If
\[
d_w=\deg_G(w),
\]
assign to the three vertices associated with
\[
e=\{u,v\}
\]
the weights
\[
\lambda_e
=
\frac1{2D}
\left(
\frac1{d_u}+\frac1{d_v}
\right),
\tag{4}
\]
\[
\lambda_{e,u}
=
\frac1{2D}
\left(
1+\frac1{d_u}
\right),
\qquad
\lambda_{e,v}
=
\frac1{2D}
\left(
1+\frac1{d_v}
\right).
\tag{5}
\]
These weights are strictly positive, sum to \(1\), and have weighted barycenter \(c_G\).

## Assumptions and scope
The graph is finite, connected, simple, and has at least one edge. Connectedness ensures every graph vertex has positive degree and matches the standard connected-graph cosmological-polytope definition.

The Euclidean structure is the one in which the source coordinates
\[
\mathbf x_v,\mathbf y_e
\]
are orthonormal. Cosmological polytopes are often discussed projectively; the present theorem concerns the canonical affine representatives (1), all of which lie in the affine hyperplane
\[
\sum_{v\in V}x_v+\sum_{e\in E}y_e=1.
\]

The circumradius means the radius of the smallest Euclidean ball containing \(P_G\). The result is realization-dependent and is not asserted for arbitrary projective or affine changes of coordinates.

## Proof
Every vector in (1) has exactly three nonzero coordinates, each equal to \(1\) or \(-1\). Therefore
\[
\|p_e\|^2
=
\|p_{e,u}\|^2
=
\|p_{e,v}\|^2
=
3.
\tag{6}
\]
Also, the sum of the coordinates of each such vector is \(1\). Hence
\[
\langle p,c_G\rangle=\frac1D
\tag{7}
\]
for every vertex \(p\) of \(P_G\), while
\[
\|c_G\|^2=\frac1D.
\tag{8}
\]
Combining (6)--(8),
\[
\|p-c_G\|^2
=
3-\frac2D+\frac1D
=
3-\frac1D.
\tag{9}
\]
Thus all source vertices lie on one sphere centered at \(c_G\). Since a Euclidean ball is convex, the entire convex hull \(P_G\) lies in the closed ball of squared radius
\[
3-\frac1D.
\tag{10}
\]

It remains to prove that this ball is minimum and uniquely centered. The key point is that \(c_G\) lies in the convex hull of the contact vertices with the explicit positive weights (4)--(5).

First, for a fixed edge \(e=\{u,v\}\),
\[
\lambda_e+\lambda_{e,u}+\lambda_{e,v}
=
\frac1D
\left(
1+\frac1{d_u}+\frac1{d_v}
\right).
\]
Summing over all edges gives
\[
\sum_{e\in E}
(\lambda_e+\lambda_{e,u}+\lambda_{e,v})
=
\frac1D
\left(
|E|
+
\sum_{w\in V}
d_w\frac1{d_w}
\right)
=
\frac{|E|+|V|}{D}
=
1.
\tag{11}
\]

For the \(\mathbf y_e\)-coordinate, the contribution of the three edge-\(e\) vertices is
\[
-\lambda_e+\lambda_{e,u}+\lambda_{e,v}
=
\frac1D.
\tag{12}
\]
For a graph vertex \(u\), the contribution from an incident edge
\[
e=\{u,v\}
\]
to the \(\mathbf x_u\)-coordinate is
\[
\lambda_e+\lambda_{e,u}-\lambda_{e,v}
=
\frac1{Dd_u}.
\tag{13}
\]
Summing (13) over the \(d_u\) incident edges gives
\[
\frac1D.
\]
Equations (11)--(13) prove that the weighted barycenter of all contact vertices is exactly \(c_G\).

Now let \(q\in\mathbb R^D\) be any center of a ball containing \(P_G\). For the contact vertices \(p\) with weights \(\lambda_p\), the barycentric identity gives
\[
\sum_p\lambda_p\|p-q\|^2
=
\sum_p\lambda_p\|p-c_G\|^2
+
\|q-c_G\|^2.
\tag{14}
\]
The first sum on the right equals
\[
3-\frac1D
\]
by (9). Therefore
\[
\max_p\|p-q\|^2
\ge
3-\frac1D+\|q-c_G\|^2.
\tag{15}
\]
If
\[
q\ne c_G,
\]
the right side is strictly larger than (10). Hence no other center can attain the radius in (3), and no smaller enclosing ball exists. This proves the theorem.

## Verification
The proof is exact and applies to every connected simple graph with at least one edge.

The source-dependent premise was checked directly in the original cosmological-polytope paper and in the later mathematical face-structure paper: an edge \(e=\{u,v\}\) contributes exactly the three vectors in (1), and the cosmological polytope is their convex hull.

The accompanying `verify.py` exhaustively checks every connected labeled simple graph on
\[
2\le |V|\le6.
\]
For each graph it verifies, using exact rational arithmetic, positivity and total mass of the weights (4)--(5), every coordinate of their barycenter, the common squared vertex distance
\[
3-\frac1D,
\]
and the weighted variance identity underlying (14). The finite replay is corroborative only; the degree-sum proof above establishes the result in all dimensions.

## Relationship to prior work
Arkani-Hamed, Benincasa, and Postnikov introduced cosmological polytopes in 2017 and gave the standard \(3|E|\)-vertex realization used here. Kühne and Monin subsequently initiated a mathematical study of the face structure, giving criteria for faces, edge graphs, special vertex and cycle faces, and face counts. Their paper classifies the subject primarily under MSC \(52B05\).

The inspected primary texts do not state an Euclidean circumradius, minimum-enclosing-ball center, or graph-independent outer-radius theorem. The original paper studies canonical forms, triangulations, dual polytopes, and physical symmetries; the later paper studies combinatorial faces. Targeted searches under “cosmological polytope”, “circumradius”, “circumsphere”, “Euclidean radius”, “enclosing ball”, and regular-graph variants did not locate a statement implying (2)--(5).

The conclusion is stronger than the elementary observation that every displayed vertex has norm \(\sqrt3\). The origin is not in the affine hyperplane of the polytope, and a common sphere through all vertices need not be a minimum enclosing sphere. The positive degree-sensitive barycentric certificate (4)--(5) is what proves optimality and uniqueness for every connected graph, including highly irregular ones.

## Limitations
The metric is tied to the standard orthonormal coordinate realization. A projectively equivalent realization need not have the same Euclidean circumradius.

The theorem assumes a connected simple graph with at least one edge. The later face-structure literature allows extensions involving disconnected graphs and isolated vertices; those require a separate affine-span normalization and are not claimed here.

The theorem determines the complete outer contact set in the standard realization but does not determine the inradius, John ellipsoid, or pairwise Euclidean distance spectrum.

A residual originality risk remains that the graph-independent sphere or its barycentric optimality certificate appears in physics-oriented notes under projective normalization rather than Euclidean-radius terminology. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Nima Arkani-Hamed, Paolo Benincasa, and Alexander Postnikov, *Cosmological Polytopes and the Wavefunction of the Universe*, arXiv:1709.02813, first public version 2017-09-08.
2. Lukas Kühne and Leonid Monin, *Faces of Cosmological Polytopes*, arXiv:2209.08069, first public version 2022-09-16; Annales de l'Institut Henri Poincaré D 12 (2025), 445--461, DOI 10.4171/AIHPD/192.
