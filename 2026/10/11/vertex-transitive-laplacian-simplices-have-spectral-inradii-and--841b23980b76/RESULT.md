# Vertex-transitive Laplacian simplices have spectral inradii and degree-controlled circumradii
## Finding
Let \(G\) be a connected vertex-transitive simple graph on
\[
n\ge2
\]
vertices. Let \(k\) be its common degree, let \(L\) be its graph Laplacian, and write the Laplacian spectrum as
\[
0=\lambda_1<\lambda_2\le\cdots\le\lambda_n.
\tag{1}
\]

Use the canonical Euclidean realization obtained before any non-orthogonal lattice coordinate change:
\[
\widehat T_G
=
\operatorname{conv}\{Le_1,\ldots,Le_n\}
\subset
\mathbf1^\perp\subset\mathbb R^n.
\tag{2}
\]
The metric is the standard Euclidean metric inherited from \(\mathbb R^n\).

Then the origin is simultaneously the unique circumcenter and the unique incenter of \(\widehat T_G\). Every vertex lies on the circumsphere, every facet is tangent to the insphere, and
\[
\boxed{
R(\widehat T_G)=\sqrt{k(k+1)}.
}
\tag{3}
\]
The exact inradius is the reciprocal square root of a Laplacian spectral moment:
\[
\boxed{
r(\widehat T_G)
=
\left(
n\sum_{j=2}^{n}\lambda_j^{-2}
\right)^{-1/2}.
}
\tag{4}
\]

Let \(L^+\) denote the Moore--Penrose pseudoinverse. If \(F_i\) is the facet opposite the vertex \(Le_i\), then
\[
\boxed{
F_i
=
\left\{
x\in\mathbf1^\perp:
\frac1n+\langle L^+e_i,x\rangle=0
\right\}.
}
\tag{5}
\]
Vertex transitivity gives
\[
\boxed{
\|L^+e_i\|^2
=
\frac1n\sum_{j=2}^{n}\lambda_j^{-2}
}
\qquad
(1\le i\le n),
\tag{6}
\]
so (4) is exactly the common distance from the origin to the facets.

For example,
\[
r(\widehat T_{K_n})=\sqrt{\frac{n}{n-1}},
\qquad
R(\widehat T_{K_n})=\sqrt{n(n-1)}.
\tag{7}
\]
For the cycle \(C_n\),
\[
R(\widehat T_{C_n})=\sqrt6
\]
and the classical fourth-cosecant sum yields
\[
r(\widehat T_{C_n})
=
\sqrt{
\frac{720}
{n(n^4+10n^2-11)}
}.
\tag{8}
\]

## Assumptions and scope
The source introduces the Laplacian simplex from the columns of the graph Laplacian and then passes to lattice coordinates in \(\mathbb R^{n-1}\). Euclidean radii are not invariant under a general unimodular change of coordinates. The theorem therefore fixes the canonical full-Laplacian realization (2) in the Euclidean hyperplane \(\mathbf1^\perp\).

The graph is assumed finite, simple, connected, and vertex-transitive. Connectedness makes the \(n\) Laplacian columns affinely independent in \(\mathbf1^\perp\). Vertex transitivity implies regularity and is used essentially for the equal facet distances.

No claim is made that an arbitrary lattice representative of the same Laplacian simplex has the same Euclidean radii.

## Proof
Because \(G\) is connected,
\[
\ker L=\langle\mathbf1\rangle
\]
and
\[
\operatorname{im}L=\mathbf1^\perp.
\tag{9}
\]
Also,
\[
L\mathbf1=0.
\tag{10}
\]
Thus the \(n\) columns
\[
v_i=Le_i
\]
sum to zero. They are affinely independent: if
\[
\sum_i a_i v_i=0
\quad\text{and}\quad
\sum_i a_i=0,
\]
then
\[
La=0,
\]
so \(a\) is a multiple of \(\mathbf1\); the zero-sum condition forces \(a=0\). Hence (2) is an \((n-1)\)-simplex with centroid \(0\).

Since \(G\) is vertex-transitive, it is \(k\)-regular. Each column \(v_i\) has one entry \(k\), exactly \(k\) entries equal to \(-1\), and all remaining entries zero. Therefore
\[
\|v_i\|^2=k^2+k=k(k+1)
\tag{11}
\]
for every \(i\).

Let \(y\in\mathbf1^\perp\). Since the vertex centroid is zero,
\[
\frac1n\sum_{i=1}^n\|v_i-y\|^2
=
\frac1n\sum_i\|v_i\|^2+\|y\|^2
=
k(k+1)+\|y\|^2.
\tag{12}
\]
Consequently every enclosing ball centered at \(y\) has radius at least
\[
\sqrt{k(k+1)+\|y\|^2}.
\]
At \(y=0\), all vertices have radius \(\sqrt{k(k+1)}\). Thus (3) is the minimum enclosing radius, and equality is possible only at
\[
y=0.
\]
This proves the circumcenter statement.

We next compute every facet exactly.

For \(x\in\mathbf1^\perp\), define
\[
\alpha(x)
=
L^+x+\frac1n\mathbf1.
\tag{13}
\]
Since
\[
LL^+x=x
\]
on \(\mathbf1^\perp\), and since the columns of \(L^+\) lie in \(\mathbf1^\perp\),
\[
L\alpha(x)=x,
\qquad
\mathbf1^{\mathsf T}\alpha(x)=1.
\tag{14}
\]
Therefore the entries of \(\alpha(x)\) are exactly the barycentric coordinates of \(x\) with respect to the vertices \(v_1,\ldots,v_n\):
\[
x=\sum_{i=1}^n\alpha_i(x)v_i.
\tag{15}
\]
In particular,
\[
\alpha_i(x)
=
\frac1n+\langle L^+e_i,x\rangle.
\tag{16}
\]
The facet opposite \(v_i\) is characterized by
\[
\alpha_i(x)=0,
\]
which is (5). Its intrinsic normal in \(\mathbf1^\perp\) is \(L^+e_i\). Hence the distance from the origin to \(F_i\) is
\[
d_i
=
\frac{1/n}{\|L^+e_i\|}.
\tag{17}
\]

Let \(P\) be the permutation matrix of a graph automorphism. Then
\[
PL=LP,
\]
and therefore
\[
PL^+=L^+P.
\tag{18}
\]
Because the automorphism group acts transitively on vertices, the quantities
\[
\|L^+e_i\|
\]
are all equal. Write their common squared value as \(q\). Summing over \(i\),
\[
nq
=
\|L^+\|_{\mathrm F}^2
=
\operatorname{tr}\bigl((L^+)^2\bigr).
\tag{19}
\]
The eigenvalues of \(L^+\) are
\[
0,\lambda_2^{-1},\ldots,\lambda_n^{-1},
\]
so
\[
q
=
\frac1n\sum_{j=2}^{n}\lambda_j^{-2}.
\tag{20}
\]
Equations (17)--(20) give (4) and (6). In particular, the origin is equidistant from all facets.

For completeness, this common facet distance is globally optimal without appealing to a separate simplex-center theorem. Let a radius-\(\rho\) ball centered at \(x\in\widehat T_G\) lie inside the simplex. The signed clearance from \(x\) to \(F_i\) is
\[
\frac{\alpha_i(x)}{\|L^+e_i\|}.
\]
Since all normal lengths equal \(\sqrt q\),
\[
\alpha_i(x)\ge \rho\sqrt q
\qquad
(1\le i\le n).
\tag{21}
\]
Summing the barycentric coordinates,
\[
1=\sum_i\alpha_i(x)\ge n\rho\sqrt q,
\]
so
\[
\rho\le\frac1{n\sqrt q}
=
\left(
n\sum_{j=2}^{n}\lambda_j^{-2}
\right)^{-1/2}.
\tag{22}
\]
The origin attains equality. Equality in (22) forces
\[
\alpha_i(x)=\frac1n
\]
for every \(i\), hence
\[
x=0.
\]
Thus the incenter is unique and every facet is tangent.

For (7), the nonzero Laplacian eigenvalues of \(K_n\) are all \(n\). For (8), the cycle eigenvalues are
\[
4\sin^2\left(\frac{\pi j}{n}\right),
\qquad
1\le j\le n-1,
\]
and
\[
\sum_{j=1}^{n-1}
\csc^4\left(\frac{\pi j}{n}\right)
=
\frac{n^4+10n^2-11}{45}.
\]

## Verification
The proof is symbolic for every connected vertex-transitive simple graph.

The source-dependent premises were checked directly in the primary full text: the graph Laplacian convention, symmetry and kernel facts, the construction of the Laplacian simplex from the Laplacian columns, affine independence, the origin-interior statement, and the complete-graph and cycle examples. The source's stated focus is Ehrhart theory, reflexivity, integer decomposition, and unimodality rather than Euclidean radii.

The accompanying `verify.py` performs exact rational replay on four vertex-transitive graphs with distinct spectral behavior:
\[
K_5,\qquad C_6,\qquad Q_3,\qquad \text{the Petersen graph}.
\]
For each graph it verifies the Laplacian rank, the barycentric facet formula, equality of the \(L^+e_i\) norms, the spectral trace identity, the inradius formula, and the degree-controlled circumradius. These finite checks are corroborative only; the arbitrary-graph proof is the argument above.

## Relationship to prior work
Braun and Meyer introduce Laplacian simplices and study their normalized volume, reflexivity, integer decomposition property, and Ehrhart \(h^*\)-vectors. Their primary paper explicitly says that the construction is obtained from the columns of the graph Laplacian, proves the origin lies in the interior, and studies trees, cycles, and complete graphs. It does not state Euclidean inradii, circumradii, Chebyshev centers, or pseudoinverse facet normals.

Meyer and Pllaha later study reflexive Laplacian simplices through coding theory. Their full text likewise focuses on lattice equivalence, duality, codes, reflexivity, and Ehrhart theory rather than Euclidean center geometry.

A distinct older literature studies the Laplacian lattice using a simplex-induced non-Euclidean distance. That work analyzes Voronoi and Delaunay structures of the lattice, not the Euclidean inball or circumball of the Laplacian simplex itself.

The spectral formula (4) is not a consequence of the Matrix--Tree Theorem or of the source normalized-volume formula. The latter is governed by the product of nonzero Laplacian eigenvalues, whereas (4) is governed by the reciprocal fourth spectral moment
\[
\sum_{j=2}^{n}\lambda_j^{-2}.
\]
Thus graphs with the same degree and spanning-tree count can still have different Euclidean inradii.

Targeted searches under “Laplacian simplex”, “inradius”, “circumradius”, “Chebyshev center”, “pseudoinverse”, “vertex-transitive”, and “spectrum” did not locate a theorem implying (3)--(6).

## Limitations
The radii are attached to the canonical full-Laplacian Euclidean realization (2). They are not invariants of the unimodular-equivalence class used for lattice-polytope questions.

Vertex transitivity is sufficient for the common facet-normal length in (6), but it is not claimed to be necessary. Non-vertex-transitive graphs can have unequal values of \(\|L^+e_i\|\), and their Euclidean incenter need not be the origin.

The result does not determine John or Löwner ellipsoids, edge-length spectra, or Euclidean radii of the higher-dimensional Laplacian polytopes of simplicial complexes.

A residual originality risk remains for a general simplex-pseudoinverse identity stated outside the Laplacian-simplex literature. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Benjamin Braun and Marie Meyer, *Laplacian Simplices*, arXiv:1706.07085, first public version 2017-06-21; *Advances in Applied Mathematics* 114 (2020), article 101976, DOI 10.1016/j.aam.2019.101976.
2. Marie Meyer and Tefjol Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960, first public version 2018-09-09.
3. Madhusudan Manjunath and Bernd Sturmfels, *The Laplacian lattice of a graph under a simplicial distance function*, *European Journal of Combinatorics* 34 (2013), 1051--1070, DOI 10.1016/j.ejc.2013.01.010.
