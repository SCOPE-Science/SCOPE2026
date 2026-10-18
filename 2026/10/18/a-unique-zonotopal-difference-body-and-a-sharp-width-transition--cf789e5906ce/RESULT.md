# A unique zonotopal difference body and a sharp width transition in tetrahedral truncations

## Finding
Let the four vertices of a regular tetrahedron be
\[
v_1=(1,1,1),\quad v_2=(1,-1,-1),\quad
v_3=(-1,1,-1),\quad v_4=(-1,-1,1).
\]
For every real \(0\le t\le 1/2\), truncate every vertex by the same fraction of its six incident edges and set
\[
T_t=\operatorname{conv}\{(1-t)v_i+tv_j:i\ne j\},\qquad D_t=T_t-T_t.
\]
Then the **entire difference body** has the exact half-space description
\[
\boxed{D_t=\{x\in\mathbb R^3:\|x\|_\infty\le2,\ \|x\|_1\le4(1-t)\}.}
\]
Among all these truncated tetrahedra, \(D_t\) is a zonotope **if and only if** \(t=1/4\). At that unique parameter, \(D_t\) is the regular truncated octahedron with vertices the signed coordinate permutations of \((2,1,0)\).

The minimum ordinary Euclidean directional width of the truncated tetrahedron is
\[
\boxed{\min_{\|u\|_2=1}\left(\max_{x\in T_t}u\cdot x-\min_{x\in T_t}u\cdot x\right)
=\min\left\{2,\frac{4(1-t)}{\sqrt3}\right\}.}
\]
Put \(t_0=1-\sqrt3/2\). For \(0\le t<t_0\), the only minimizing unoriented normals are the three coordinate-axis directions. For \(t_0<t\le1/2\), the only such normals are the four body-diagonal directions. Exactly at \(t=t_0\), both families minimize, giving seven unoriented directions. The width transition at \(t_0\) is distinct from the zonotopal parameter \(1/4\).

## Assumptions and scope
All bodies, norms, support functions, Minkowski sums and widths are Euclidean in \(\mathbb R^3\). The truncation parameter includes both degenerate endpoints of the truncation process: \(t=0\) is the regular tetrahedron, and \(t=1/2\) is the edge-midpoint octahedron. A zonotope means a Minkowski sum of finitely many line segments; a difference body is the Minkowski sum \(K+(-K)\). Unoriented normals identify \(u\) and \(-u\). The displayed vertex coordinates fix the scale: original tetrahedral edge length is \(2\sqrt2\).

## Proof
**1. Exact difference body.** Write \(a=1-2t\in[0,1]\). The edge points defining \(T_t\) have, with repetitions at the endpoints, the signed-coordinate form of \((1,a,a)\) with sign product positive. Every point of \(D_t\) is a convex combination of differences of two such points. Each coordinate of a difference has absolute value at most \(2\); hence \(\|x\|_\infty\le2\).

For each signed diagonal \(s\in\{\pm1\}^3\), the width of \(T_t\) in the nonunit direction \(s\) is \(2+2a\). Indeed, for \(s=(1,1,1)\) the maximum of \(s\cdot x\) on \(T_t\) is \(1+2a\) and the minimum is \(-1\). Tetrahedral coordinate permutations and even sign changes act transitively on the four sign vectors of positive sign product; reversing \(s\) covers the other four. Thus, for all eight diagonals, \(h_{D_t}(s)=2+2a\), yielding \(\|x\|_1\le2+2a=4(1-t)\). This proves containment in the asserted intersection \(C_a\).

For \(0<a<1\), every facet of \(C_a=\{\|x\|_\infty\le2,\|x\|_1\le2+2a\}\) comes from one of its fourteen defining inequalities. On \(x_1=2\), the facet is the planar diamond \(|x_2|+|x_3|\le2a\), whose vertices are \((2,\pm2a,0)\) and \((2,0,\pm2a)\). On the positive diagonal \(x_1+x_2+x_3=2+2a\), all coordinates must be nonnegative, so the facet is the intersection of \([0,2]^3\) with that plane. Its six vertices are precisely the coordinate permutations of \((2,2a,0)\). Signed-coordinate symmetry gives the remaining facets. Hence \(C_a\) is the convex hull of the 24 signed-coordinate permutations of \((2,2a,0)\).

The difference
\[
(1,a,a)-(-1,-a,a)=(2,2a,0)
\]
is a difference of two actual truncation vertices. The tetrahedral symmetry, coordinate permutations, even sign changes and central symmetry of the difference body supply all the signed permutations. Therefore every vertex of \(C_a\) belongs to \(D_t\), proving \(C_a\subseteq D_t\). At \(a=1\) these vertices merge into twelve cuboctahedral vertices, and at \(a=0\) into six octahedral vertices; the same containment argument holds and yields the asserted equality at both endpoints.

**2. Unique zonotope.** For \(0<a<1\), the positive-diagonal facet of \(D_t\) is the ordered hexagon with vertices
\[
\begin{split}
&(2,2a,0),\ (2,0,2a),\ (2a,0,2),\\
&(0,2a,2),\ (0,2,2a),\ (2a,2,0).
\end{split}
\]
The sums of its three pairs of opposite vertices are
\[
(2,4a,2),\quad(2,2,4a),\quad(4a,2,2).
\]
A convex hexagon is centrally symmetric only when these sums agree, which here holds exactly for \(a=1/2\). Every two-dimensional face of a zonotope is centrally symmetric: an exposed face of a segment sum is itself a sum of points and segments. Thus the difference body is not a zonotope for any other \(0<a<1\). At \(a=0\) and \(a=1\), the diagonal faces are triangles, excluding the endpoints as well.

Conversely, at \(a=1/2\) let the six vectors be
\[
\begin{split}
&g_1=(1,1,0),\ g_2=(1,-1,0),\ g_3=(1,0,1),\\
&g_4=(1,0,-1),\ g_5=(0,1,1),\ g_6=(0,1,-1).
\end{split}
\]
The zonotope \(Z=\sum_{j=1}^6[-g_j/2,g_j/2]\) lies in \(C_{1/2}\): its coordinate supports are \(2\), and its supports at all signed diagonals are \(3\). The sum of the six positive generators, each multiplied by \(1/2\), is \((2,1,0)\). Coordinate signed permutations preserve the generator set up to sign, so \(Z\) contains all 24 vertices of \(C_{1/2}\). Hence \(Z=C_{1/2}=D_{1/4}\). Its square and regular hexagonal facets all have common edge length \(\sqrt2\), so it is the regular truncated octahedron.

**3. Sharp minimum width and equality normals.** The directional width of \(T_t\) equals the support function of \(D_t\). Therefore its minimum over Euclidean unit normals is the radius of the largest centered Euclidean ball contained in \(D_t\). The fourteen facet inequalities of the exact intersection give centered ball radius
\[
r=\min\{2,(2+2a)/\sqrt3\}.
\]
A tangent normal of a centered ball must be parallel to the normal of a facet inequality at distance \(r\) (equality in Cauchy–Schwarz). The six coordinate inequalities have distance \(2\), and the eight diagonal inequalities have distance \((2+2a)/\sqrt3\). Comparing them gives the displayed width and the exhaustive minimizing-normal classification, including the equality case \(a=\sqrt3-1\), equivalent to \(t=t_0\). No additional normals can attain this minimum.

## Verification
Run `python3 checker.py` (standard library only). It checks all defining half-space supports and all claimed intersection vertices against the complete pairwise difference set for seven exact rational parameters, verifies a six-segment representation at \(t=1/4\), and checks the opposite-pair condition for representative exact hexagons. The general-in-parameter result follows from the symbolic facet-and-symmetry proof above, not finite parameter testing.

## Relationship to prior work
Martin Winter's *Classification of Vertex-Transitive Zonotopes* (first public version 2019-12-22, journal 2021) establishes the zonotope characterizations and places the regular truncated octahedron in the type-\(A_3\) permutahedral family. Those known facts do not identify which tetrahedral truncations have a zonotopal difference body, nor give their entire difference-body profile and exact minimum-width normals. A published study of tetrahedral volume in the cube–cross-polytope intersection family treats the same *output* family but a different invariant; the present claim determines the input truncation/difference-body correspondence and its two sharp parameter transitions. Earlier public discussions of Minkowski sums of Archimedean solids explain isolated sums, not the stated all-parameter difference-body and width classification.

## Limitations
The theorem concerns uniform edge-fraction truncations of a regular tetrahedron in the stated Euclidean realization. It does not assert the same formulas for irregular tetrahedra or asymmetric truncations. The complete all-parameter argument is elementary but has not received independent mathematical review. An equivalent older derivation under different truncation or Wythoffian terminology is a residual bibliographic possibility.

## References
1. Martin Winter, *Classification of Vertex-Transitive Zonotopes*, arXiv:1912.10469 (first public 2019-12-22); *Discrete & Computational Geometry* 66 (2021), 1446–1462. https://arxiv.org/abs/1912.10469 ; https://doi.org/10.1007/s00454-021-00303-6
2. Aaron Goldsmith, *A Proof of the Simplex Mean Width Conjecture*, arXiv:2112.03393 (first public 2021-12-06), for the broader support-function treatment of simplex mean width. https://arxiv.org/abs/2112.03393
3. *Sharp tetrahedral-volume profile in the cube–octahedron intersection family*, publicly indexed mathematical result; comparison made to its accessible statement rather than an inaccessible full text.
