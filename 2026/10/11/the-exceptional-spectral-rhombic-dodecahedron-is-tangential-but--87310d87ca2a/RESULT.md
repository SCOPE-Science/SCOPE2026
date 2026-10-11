# The exceptional spectral rhombic dodecahedron is tangential but has two exact vertex shells
## Finding
Let \(G\) be the edge graph of the rhombic dodecahedron. Winter identifies this graph as the unique known edge-transitive, non-vertex-transitive graph whose second eigenpolytope reproduces its polytope.

Use the canonical metric convention from the source: choose an orthonormal basis of the second adjacency eigenspace and take its rows as the eigenpolytope vertices. Then, up to an orthogonal transformation,
\[
\boxed{
P_G(2)
=
\operatorname{conv}\!\left(
\left\{
\pm\frac12 e_1,\,
\pm\frac12 e_2,\,
\pm\frac12 e_3
\right\}
\cup
\left\{
\frac14(\varepsilon_1,\varepsilon_2,\varepsilon_3):
\varepsilon_i\in\{\pm1\}
\right\}
\right).
}
\tag{1}
\]

The six vertices of graph degree \(4\) form a regular octahedron and satisfy
\[
\|v\|=\frac12.
\tag{2}
\]
The eight vertices of graph degree \(3\) form a cube and satisfy
\[
\|v\|=\frac{\sqrt3}{4}.
\tag{3}
\]

Consequently the unique minimum enclosing Euclidean sphere is
\[
\boxed{
B\!\left(0,\frac12\right),
}
\tag{4}
\]
and its contact set is exactly the six degree-\(4\) vertices.

The same canonical realization is tangential. Its twelve facets are
\[
\boxed{
\sigma_i x_i+\sigma_j x_j\le\frac12,
\qquad
1\le i<j\le3,\quad
\sigma_i,\sigma_j\in\{\pm1\}.
}
\tag{5}
\]
Hence the unique incenter is the origin and
\[
\boxed{
r_{\mathrm{in}}\bigl(P_G(2)\bigr)
=
\frac1{2\sqrt2}.
}
\tag{6}
\]

Every edge has length
\[
\boxed{
\ell=\frac{\sqrt3}{4}.
}
\tag{7}
\]

Thus the exceptional non-vertex-transitive spectral polyhedron is metrically asymmetric in exactly one transparent way: all facets are tangent to one centered sphere, but its two vertex orbits lie on two different centered spheres.

## Assumptions and scope
The graph \(G\) is the edge graph of the ordinary rhombic dodecahedron.

The eigenpolytope convention is exactly Winter's Definition 2.2: the columns of the eigenpolytope matrix form an orthonormal basis of the chosen adjacency eigenspace. This choice is essential because it fixes metric scale up to orthogonal transformation.

The result concerns the second eigenvalue, which for this graph is \(2\) with multiplicity \(3\).

No statement is made about arbitrary affine realizations of the rhombic-dodecahedron combinatorial type.

## Proof
Realize the rhombic-dodecahedron graph as the incidence graph between the eight vertices of a cube and its six facets.

Index the cube vertices by sign vectors
\[
\varepsilon=(\varepsilon_1,\varepsilon_2,\varepsilon_3)
\in\{\pm1\}^3.
\]
Index the cube facets by signed coordinate conditions
\[
(i,\tau),
\qquad
i\in\{1,2,3\},
\quad
\tau\in\{\pm1\},
\]
where \((i,\tau)\) is incident to \(\varepsilon\) exactly when
\[
\varepsilon_i=\tau.
\tag{8}
\]

Assign vectors
\[
p_\varepsilon
=
\frac14(\varepsilon_1,\varepsilon_2,\varepsilon_3)
\tag{9}
\]
to the eight cube-vertex nodes and
\[
q_{i,\tau}
=
\frac{\tau}{2}e_i
\tag{10}
\]
to the six cube-facet nodes.

Let \(\Phi\) be the \(14\times3\) matrix having these vectors as rows.

For a cube-vertex node \(\varepsilon\), its three neighbors are
\[
q_{1,\varepsilon_1},
\quad
q_{2,\varepsilon_2},
\quad
q_{3,\varepsilon_3}.
\]
Therefore
\[
\sum_{v\sim\varepsilon}\Phi_v
=
\frac12(\varepsilon_1,\varepsilon_2,\varepsilon_3)
=
2p_\varepsilon.
\tag{11}
\]

For a cube-facet node \((i,\tau)\), its four neighbors are the sign vectors with
\[
\varepsilon_i=\tau.
\]
Their two unrestricted coordinates cancel in pairs, while the \(i\)-th coordinate contributes \(4\tau/4=\tau\). Hence
\[
\sum_{v\sim(i,\tau)}\Phi_v
=
\tau e_i
=
2q_{i,\tau}.
\tag{12}
\]

Equations (11)--(12) say
\[
A_G\Phi=2\Phi.
\tag{13}
\]

The three columns of \(\Phi\) are orthonormal. For one coordinate, the two axis vertices contribute
\[
2\left(\frac12\right)^2=\frac12,
\]
and the eight cube vertices contribute
\[
8\left(\frac14\right)^2=\frac12.
\]
Thus each column has squared norm \(1\). Distinct columns have zero scalar product because the eight sign products cancel, and the axis vertices contribute no cross terms.

The incidence matrix \(B\) of cube vertices versus cube facets satisfies
\[
B^{\mathsf T}B=4I+2A_{\mathrm{oct}},
\]
where \(A_{\mathrm{oct}}\) is the octahedral graph adjacency matrix. Since
\[
\operatorname{Spec}(A_{\mathrm{oct}})
=
\{4,0,0,0,-2,-2\},
\]
the rhombic-dodecahedron graph has adjacency spectrum
\[
\{2\sqrt3,\ 2,2,2,\ 0,0,0,0,0,0,\ -2,-2,-2,\ -2\sqrt3\}.
\tag{14}
\]
Thus \(2\) is the second eigenvalue with multiplicity \(3\). Because the columns of \(\Phi\) are an orthonormal basis for that eigenspace, Definition 2.2 identifies the row convex hull of \(\Phi\) with the canonical eigenpolytope \(P_G(2)\), up to orientation. This proves (1).

The two vertex radii (2)--(3) follow immediately from (9)--(10).

The six outer points
\[
\pm\frac12e_1,\,
\pm\frac12e_2,\,
\pm\frac12e_3
\]
already force any enclosing ball to have radius at least \(1/2\). Indeed, for any candidate center \(z\) and any coordinate \(i\),
\[
\frac12
\left(
\left\|z-\frac12e_i\right\|^2
+
\left\|z+\frac12e_i\right\|^2
\right)
=
\|z\|^2+\frac14.
\tag{15}
\]
Hence some member of each antipodal pair is at distance at least
\[
\sqrt{\|z\|^2+\frac14}.
\]
At \(z=0\), the six axis vertices have distance \(1/2\), while every cube vertex has distance \(\sqrt3/4<1/2\). Therefore (4) is the minimum enclosing sphere, and (15) makes its center unique.

We next prove the facet description. Every vertex in (1) satisfies
\[
\sigma_i x_i+\sigma_jx_j\le\frac12
\tag{16}
\]
for all distinct \(i,j\) and all signs. For a fixed choice of \(i,j,\sigma_i,\sigma_j\), equality holds at exactly four displayed vertices:
\[
\frac{\sigma_i}{2}e_i,
\qquad
\frac{\sigma_j}{2}e_j,
\qquad
\frac14(\varepsilon_1,\varepsilon_2,\varepsilon_3)
\]
with
\[
\varepsilon_i=\sigma_i,\qquad
\varepsilon_j=\sigma_j,
\]
and either choice for the remaining sign. These four points span a two-dimensional rhombus, so (16) supports a facet.

There are
\[
3\cdot4=12
\]
such supporting planes. The edge graph has
\[
8\cdot3=24
\]
edges and \(14\) vertices, so Euler's formula gives exactly
\[
24-14+2=12
\]
facets. Thus (5) is the complete facet list.

Each facet normal has norm
\[
\sqrt2,
\]
and every facet support value is
\[
\frac12.
\]
Therefore the centered distance to every facet is
\[
\frac{1/2}{\sqrt2}
=
\frac1{2\sqrt2},
\]
so the origin-centered ball of radius (6) is feasible.

Uniqueness follows from opposite facet pairs. A radius-\(1/(2\sqrt2)\) inscribed ball centered at \(z\) must have full radius clearance from both
\[
x_i+x_j\le\frac12
\quad\text{and}\quad
-x_i-x_j\le\frac12,
\]
forcing
\[
z_i+z_j=0.
\]
Applying this to the three coordinate pairs gives
\[
z=0.
\]

Finally, every graph edge joins a cube vertex \(p_\varepsilon\) to an incident facet vertex \(q_{i,\varepsilon_i}\). Their difference has three coordinates of absolute value \(1/4\), so
\[
\|p_\varepsilon-q_{i,\varepsilon_i}\|
=
\frac{\sqrt3}{4}.
\]
This proves (7).

## Verification
The proof is exact.

The source-dependent points were checked directly in Winter's full text and page images: Definition 2.2 uses an orthonormal eigenspace basis specifically to preserve metric properties; Remark 5.3 identifies the rhombic dodecahedron as the only known spectral polytope that is not vertex-transitive; and Theorem 5.7 isolates it as the non-vertex-transitive edge-transitive spectral exception.

The accompanying `verify.py` reconstructs the \(14\)-vertex incidence graph, verifies its exact characteristic polynomial, checks \(A_G\Phi=2\Phi\), checks \(\Phi^{\mathsf T}\Phi=I\), verifies the two vertex shells and all edge lengths, and checks all twelve supporting inequalities and facet equality sets.

## Relationship to prior work
Winter's paper emphasizes that vertex-transitive spectral polytopes are inscribed, while the rhombic dodecahedron is the exceptional known spectral example outside vertex transitivity. It does not give the orthonormal canonical coordinates, the two exact vertex-shell radii, the minimum-enclosing contact set, or the inradius of that canonical realization.

Winter also cites Licata and Powers for the earlier observation that the rhombic dodecahedron reproduces from its second eigenspace. An indexed excerpt of that earlier report confirms a computational eigenmatrix reconstruction, but the directly hosted PDF was not accessible during this check. The available material does not state the two-shell metric profile or the inball calculation.

Classical coordinate descriptions of the rhombic dodecahedron of course give affine or scaled models of the same polyhedron. What is specific here is the exact normalization forced by the orthonormal eigenpolytope convention and the resulting spectral interpretation of the two graph-vertex orbits.

Targeted searches for the rhombic dodecahedron together with eigenpolytope, canonical spectral coordinates, local multiplicities, circumradius, minimum enclosing sphere, and two vertex shells did not locate a statement implying the complete metric profile above.

## Limitations
The theorem is about the canonical orthonormal spectral realization. Arbitrary affine rhombic dodecahedra can have different vertex radii and different inradii.

The older Licata--Powers report was only partially inspectable through indexed excerpts because direct PDF retrieval was blocked. It remains the principal residual originality risk.

The metric calculation does not address Winter's broader open question of finding additional non-vertex-transitive spectral polytopes.

## References
1. Martin Winter, *Eigenpolytopes, Spectral Polytopes and Edge-Transitivity*, arXiv:2009.02179, first public version 2020-09-04.
2. Carolyn Licata and David L. Powers, *A surprising property of some regular polytopes*, Scientia 1 (1988), 73--80; earlier technical-report version cited by Winter.
