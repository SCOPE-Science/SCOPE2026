# Two sharp equilibrium transitions in homogeneous regular bipyramids

## Finding
Let \(n\ge 3\) be an integer and \(r,a,b>0\). Take the convex hull \(P=P_n(r,a,b)\) of the regular \(n\)-gon
\[
 v_k=\bigl(r\cos(2\pi k/n),\,r\sin(2\pi k/n),\,0\bigr),\qquad 0\le k<n,
\]
and the two apices \(A=(0,0,a)\) and \(B=(0,0,-b)\). Give \(P\) uniform volume density, and count its nondegenerate static equilibria relative to its own centroid as \((S,H,U)\), where the letters count face-stable, edge-saddle, and vertex-unstable equilibria.

Define the dimensionless asymmetry and equatorial half-angle cosine by
\[
 \tau=\frac{\min(a,b)|a-b|}{4r^2},\qquad c_n=\cos\frac{\pi}{n}.
\]
For every \(\tau\notin\{c_n^2,1\}\), all equilibria are nondegenerate, and the **complete signature** is
\[
 (S,H,U)=
 \begin{cases}
 (2n,3n,n+2),&0\le\tau<c_n^2,\\
 (n,2n,n+2),&c_n^2<\tau<1,\\
 (n,n,2),&\tau>1.
 \end{cases}
\]
The mechanical complexity of Domokos et al., defined as the number of all faces of dimensions zero, one, and two minus the number of equilibria, takes the exact values \(0\), \(2n\), and \(4n\) in these three regimes, respectively.

Each regime is attained by positive heights for every \(n\ge3\). At \(\tau=c_n^2\), precisely \(n\) equatorial edge-saddles meet the \(n\) face-stable points on the shorter-apex side, at equatorial edge midpoints; those points are degenerate. At \(\tau=1\), precisely \(n\) shorter-apex slant-edge saddles meet the \(n\) equatorial vertex-unstable points, at those vertices, again degenerately. No other degeneracies occur.

The middle phase has exact width \(1-c_n^2=\sin^2(\pi/n)\) in the \(\tau\)-parameter and hence shrinks as \(\pi^2/n^2+O(n^{-4})\) as \(n\to\infty\). Thus the two collective losses of equilibria are separated by a sharp, dimensionless, polygon-order-dependent interval even though the combinatorial type never changes.

## Assumptions and scope
A static equilibrium is a point \(x\in\partial P\) such that \(x-g\), with \(g\) the volume centroid, belongs to the outward normal cone of \(P\) at \(x\). An equilibrium is nondegenerate when the supporting plane perpendicular to \(x-g\) meets \(P\) exactly in the face whose relative interior contains \(x\). Facets, edges, and vertices then give stable, saddle, and unstable types, respectively. These are the standard polyhedral normal-cone criteria, not a dynamical friction model. The theorem applies to regular equatorial polygons, collinear opposite apices, uniform *volume* density, and arbitrary positive \(r,a,b\). It makes no claim about oblique apices, arbitrary equatorial polygons, or nonuniform density. Boundary values are classified as degenerate collisions, not assigned the nondegenerate signatures on either side.

## Proof
**1. Centroid and symmetry.** The upper and lower pyramids have common base area \(A_0\) and volumes \(A_0a/3\) and \(A_0b/3\), with axial centroids at heights \(a/4\) and \(-b/4\). Therefore
\[
 g=(0,0,z_0),\qquad z_0=\frac{a^2-b^2}{4(a+b)}=\frac{a-b}{4}.
\]
Reflection through the equatorial plane interchanges \(a,b\) without affecting any equilibrium counts. Hence assume \(a\ge b\), so \(z_0\ge0\) and \(\tau=bz_0/r^2\). Put \(c=c_n\in(0,1)\). The faces fall into \(n\) upper and \(n\) lower triangles, the edges into \(n\) upper slant, \(n\) lower slant, and \(n\) equatorial edges, and the vertices into two apices and \(n\) equatorial vertices. It suffices to check one representative of each orbit.

**2. Face-stable points.** Rotate a representative equatorial edge so its midpoint is \(E=(rc,0,0)\). The corresponding upper and lower triangular supporting planes are
\[
 \frac{x}{rc}+\frac{z}{a}=1,
 \qquad
 \frac{x}{rc}-\frac{z}{b}=1.
\]
The orthogonal foot of \(g\) on the lower plane lies on the face median and has horizontal coordinate
\[
 x_-=\frac{rc\,b(b+z_0)}{b^2+r^2c^2}.
\]
It is strictly inside that triangular face exactly when \(0<x_-<rc\), equivalently
\[
 bz_0<r^2c^2\quad\Longleftrightarrow\quad\tau<c^2.
\]
The corresponding upper foot has coordinate \(x_+=rc\,a(a-z_0)/(a^2+r^2c^2)\); it satisfies \(0<x_+<rc\) because \(0\le z_0<a\). Thus all \(n\) upper faces always support stable points; all \(n\) lower faces do so exactly when \(\tau<c^2\).

**3. Edge-saddles.** For a representative equatorial edge, the orthogonal foot is its midpoint \(E\), with radial vector \(E-g=(rc,0,-z_0)\). The adjacent face normals may be taken as \(N_+=(1/(rc),0,1/a)\) and \(N_-=(1/(rc),0,-1/b)\). Its representation \(E-g=\alpha N_++\beta N_-\) has
\[
 \alpha=\frac{a(r^2c^2-bz_0)}{a+b},
 \qquad \beta=\frac{b(r^2c^2+az_0)}{a+b}.
\]
Hence the foot lies in the **interior** of its edge normal cone precisely for \(\tau<c^2\); this produces the \(n\) equatorial saddles.

For a slant edge from a base vertex to the upper apex, the orthogonal-foot parameter measured from the base vertex is
\[
 s_+=\frac{r^2+az_0}{r^2+a^2}\in(0,1).
\]
For a slant edge to the lower apex, it is
\[
 s_-=\frac{r^2-bz_0}{r^2+b^2},
\]
which belongs to \((0,1)\) exactly when \(\tau<1\). Each such foot has its radial vector along the positive bisector of the two incident face normals (the face normals are reflections of one another across its axial symmetry plane), and hence strictly inside the edge normal cone. Therefore all \(n\) upper slant edges always support saddles, whereas all \(n\) lower slant edges do so exactly for \(\tau<1\).

**4. Vertex-unstable points.** Both apices support nondegenerate unstable equilibria: the vertical radial direction strictly exposes the corresponding apex. For a base vertex take \(v=(r,0,0)\). Its radial vector is \((r,0,-z_0)\). Its dot products with the incident edge directions to the two adjacent base vertices are strictly negative, and with the edge directions to the upper and lower apices are, respectively,
\[
 -r^2-az_0<0,
 \qquad -r^2+bz_0=r^2(\tau-1).
\]
The normal-cone interior test is therefore satisfied exactly when \(\tau<1\). Hence the \(n\) base vertices contribute unstable equilibria precisely in the first two regimes.

**5. Completeness, boundaries, and realization.** Every equilibrium must lie in the relative interior of some facet, edge, or vertex; steps 2--4 exhaust all such faces and all associated foot/normal-cone conditions. Summation gives the claimed three signatures. Since the total number of faces of dimensions zero, one and two is \((n+2)+3n+2n=6n+2\), subtracting \(S+H+U\) gives the stated mechanical complexities \(0,2n,4n\). They each satisfy \(S-H+U=2\), consistently with the polyhedral Poincaré--Hopf identity. At \(\tau=c^2\), the lower face foot reaches its equatorial edge midpoint exactly when the equatorial saddle normal-cone coefficient \(\alpha\) vanishes, yielding \(n\) simultaneous degenerate collisions. At \(\tau=1\), the lower slant foot parameter \(s_-\) reaches zero exactly when the base-vertex radial vector lies on its normal-cone boundary, yielding the second \(n\) collisions. The strict inequalities above exclude all other degeneracies. For any prescribed \(\tau\ge0\), choose \(r=b=1\) and \(a=1+4\tau\); thus all three open phases occur for every \(n\). Finally, \(1-c_n^2=\sin^2(\pi/n)\) has the stated expansion.

## Verification
A standalone standard-library program, `bipyramid_checker.py`, reconstructs all vertices, triangular facets, outward facet normals, and adjacent edges for each test body. Without using the theoretical orbit counts in its classification, it tests face orthogonal-foot barycentric inequalities, edge orthogonal feet and two-normal cone coefficients, and vertex radial support inequalities. It passed \(56\) combinations of polygon orders \(n\in\{3,4,5,6,8,11,20\}\) and asymmetries spread across all three regimes. All observed counts agree with the displayed signatures and satisfy the Euler identity. This numerical check is supplementary; the proof covers all integers and positive real parameters by exact inequalities.

## Relationship to prior work
Schettini Gherardini (2026) constructs a mono-monostatic polyhedron and states the general normal-cone tests used for polyhedral equilibria, but does not give the two-height regular-bipyramid phase diagram. Bozóki, Domokos, Papp, and Regős (2024) prove that a mono-unstable homogeneous polyhedron has at least seven vertices; they discuss the triangular-bipyramid graph in their exclusion argument, but do not determine the gravitational signatures of the regular, unequal-height family. Domokos, Kovács, Lángi, Regős, and Varga (2020) study the global realizability and mechanical complexity of polyhedral equilibrium signatures; their regular-pyramid example and general existence theorem do not evaluate asymmetric regular-bipyramid height thresholds. Várkonyi and Domokos (2006) develop a general stable/saddle/unstable signature classification, rather than these exact height thresholds. The theorem here is the complete sharp parameter classification for a fixed natural family, not a claim to the general equilibrium criteria. Its conclusion concerns a different invariant from previously studied illumination numbers of symmetric regular bipyramids.

## Limitations
The result does not minimize stable or unstable counts over arbitrary convex polyhedra, and in particular supplies no new Gömböc construction or resolution of the minimum-face problem. Nongeneric boundary configurations have degenerate equilibria and cannot be counted using the open-regime signatures. The proof does not address oblique, nonregular, nonhomogeneous, or other combinatorial types. Exhaustive coverage of older, unindexed statics examples is not established; potential historical priority overlap remains a scientific risk.

## References
1. T. Schettini Gherardini, *An explicit mono-monostatic polyhedron*, arXiv:2609.07827v1, first posted September 7, 2026, Sections 1--4. https://arxiv.org/abs/2609.07827
2. S. Bozóki, G. Domokos, D. Papp, and K. Regős, *The smallest mono-unstable, homogeneous convex polyhedron has at least 7 vertices*, arXiv:2401.17906, especially Sections 1 and 4. https://arxiv.org/html/2401.17906v1
3. P. L. Várkonyi and G. Domokos, *Static Equilibria of Rigid Bodies: Dice, Pebbles, and the Poincaré--Hopf Theorem*, Journal of Nonlinear Science 16 (2006), 255--281. https://gomboc.eu/wp-content/uploads/2021/09/93.pdf
4. G. Domokos, F. Kovács, Z. Lángi, K. Regős, and P. T. Varga, *Balancing polyhedra*, Ars Mathematica Contemporanea 19 (2020), 95--124; arXiv:1810.05382, especially Section 3. https://arxiv.org/abs/1810.05382
