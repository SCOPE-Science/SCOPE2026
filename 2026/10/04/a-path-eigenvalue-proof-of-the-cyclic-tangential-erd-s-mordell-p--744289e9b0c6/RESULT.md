# A path-eigenvalue proof of the cyclic–tangential Erdős–Mordell polygon conjecture

## Finding
Let \(A_1\dots A_n\) be a convex cyclic polygon with \(n\ge 3\), with vertices in circular order, and suppose no two consecutive vertices are antipodal. Let \(P\) be an interior point. Write \(d_i\) for the perpendicular distance from \(P\) to the side line \(A_iA_{i+1}\), with indices modulo \(n\). Write \(D_i\) for the perpendicular distance from \(P\) to the tangent to the circumcircle at \(A_i\). These tangent lines are the side lines of the associated tangent polygon, up to a cyclic index shift.

Then
\[
\sum_{i=1}^n D_i\ge \sec(\pi/n)\sum_{i=1}^n d_i.
\]
The constant \(\sec(\pi/n)\) is sharp. A regular cyclic \(n\)-gon has equality for every interior point \(P\). Conversely, if equality holds for an interior point, then the cyclic polygon is regular.

This establishes the general polygon inequality posed in 2016 as a strengthened Erdős–Mordell-type conjecture.

## Assumptions and scope
The polygon is the convex hull of distinct points \(A_1,\ldots,A_n\) on one Euclidean circle, listed in circular order. Consecutive antipodal vertices are excluded only because the corresponding adjacent tangents are parallel, so the usual finite tangent polygon has a vertex at infinity. The inequality itself is formulated using the tangent side lines and therefore has a natural limiting interpretation in that excluded case, but that limit is not part of the proved statement.

Distances are ordinary unsigned perpendicular distances. The proof scales with the circumradius, so it is enough to normalize the circumradius to \(1\).

## Proof
Let the arguments of the vertices be \(\theta_1<\cdots<\theta_n<\theta_1+2\pi\), and set \(\theta_{n+1}=\theta_1+2\pi\). Define
\[
\alpha_i=\frac{\theta_{i+1}-\theta_i}{2},
\qquad
u_i=\left(\cos\frac{\theta_i+\theta_{i+1}}{2},\sin\frac{\theta_i+\theta_{i+1}}{2}\right),
\qquad
v_i=(\cos\theta_i,\sin\theta_i).
\]
The side line \(A_iA_{i+1}\) is
\[
 u_i\cdot X=\cos\alpha_i.
\]
Because the open circular arc from \(A_i\) to \(A_{i+1}\) contains no other vertex, the entire convex polygon lies in the half-plane \(u_i\cdot X\le \cos\alpha_i\). Hence, for every point \(P\) in the polygon,
\[
 d_i(P)=\cos\alpha_i-u_i\cdot P.
\]
The tangent at \(A_i\) is \(v_i\cdot X=1\). Since the polygon lies in the closed unit disk,
\[
 D_i(P)=1-v_i\cdot P.
\]
Therefore
\[
 F(P)=\sum_iD_i(P)-\sec(\pi/n)\sum_i d_i(P)
\]
is affine in \(P\). It is enough to prove \(F\ge0\) at every vertex of the polygon.

Fix a vertex \(A_k\), cyclically relabel from it, and lift the arguments so that
\[
 x_j=\frac{\theta_{k+j}-\theta_k}{2},
\qquad 0=x_0<x_1<\cdots<x_n=\pi.
\]
Set \(y_j=\sin x_j\). Then \(y_0=y_n=0\) and \(y_j>0\) for \(1\le j\le n-1\). Direct trigonometry gives
\[
 \sum_i D_i(A_k)=2\sum_{j=1}^{n-1}y_j^2
\]
and
\[
 \sum_i d_i(A_k)=2\sum_{j=0}^{n-1}y_jy_{j+1}.
\]
Indeed, the first identity uses \(1-\cos(2x_j)=2\sin^2x_j\), while for the side between the \(j\)-th and \((j+1)\)-st lifted vertices,
\[
 \cos(x_{j+1}-x_j)-\cos(x_j+x_{j+1})=2\sin x_j\sin x_{j+1}.
\]

Now apply the sharp Dirichlet path inequality
\[
 \sum_{j=0}^{n-1}y_jy_{j+1}
 \le
 \cos(\pi/n)\sum_{j=1}^{n-1}y_j^2,
 \qquad y_0=y_n=0.
\]
One proof is spectral: the symmetric \((n-1)\)-by-\((n-1)\) tridiagonal matrix with \(1/2\) on its two adjacent diagonals has eigenvalues \(\cos(k\pi/n)\), so its largest eigenvalue is \(\cos(\pi/n)\). Combining the preceding identities yields \(F(A_k)\ge0\). Since \(k\) was arbitrary and \(F\) is affine, \(F(P)\ge0\) throughout the polygon.

The path inequality has equality exactly when
\[
 y_j=\lambda\sin(j\pi/n),\qquad 1\le j\le n-1,
\]
for some scalar \(\lambda\). For a regular polygon this occurs at every vertex, so the affine function \(F\) vanishes identically and equality holds for every \(P\).

Conversely, suppose \(P\) is interior and \(F(P)=0\). An affine function that is nonnegative on a polygon and vanishes at an interior point must vanish identically. Thus equality holds at every vertex. At a fixed vertex, comparing the first and last coordinates in the equality eigenvector gives equality of the sines of the two adjacent half-gaps. Cycling through the vertices shows that all \(\sin\alpha_i\) are equal. Let \(a\in(0,\pi/2]\) be the smaller angle with this common sine. Then every \(\alpha_i\) is either \(a\) or \(\pi-a\). Since \(\sum_i\alpha_i=\pi\), the second choice cannot occur for \(n\ge3\); otherwise the sum is at least \(\pi-a+(n-1)a>\pi\). Hence all \(\alpha_i=a=\pi/n\), so the polygon is regular.

## Verification
A standalone deterministic checker, `verify_polygon.py`, tests the distance formulas, the vertex-to-path reduction, the sharp path inequality, the main inequality, and regular-polygon equality on cyclic polygons with \(3\le n\le15\). It includes polygons with strongly nonuniform central gaps and interior points generated as strictly positive convex combinations of vertices.

The packaged checker returns `VERIFY_OK` on \(7020\) checks. The largest observed vertex-reduction discrepancy and regular-equality discrepancy are both \(5.329\times10^{-15}\); the largest observed violation of either inequality is \(0\) to the printed precision. These finite tests are only consistency checks. The infinite statement is proved by the affine reduction and the exact path-eigenvalue argument above.

## Relationship to prior work
On July 24, 2016, Đào Thanh Oai stated exactly the all-\(n\) cyclic-versus-tangent-polygon inequality above and asked for a proof of the general case. The post cites the triangle case as already proved in Dao, Nguyen, and Pham, *A Strengthened Version of the Erdős–Mordell Inequality*, Forum Geometricorum 16 (2016), 317–321, MR 3556993. The accessible text of that paper treats the triangle version and a weighted triangle extension, not the all-polygon statement.

Lenhard's 1961 polygonal Erdős–Mordell generalization proves a different inequality whose left side is a sum of distances from \(P\) to the vertices (and an intermediate angle-bisector sum). It does not state the sum of distances to the circumcircle tangents and therefore does not imply the claim above by statement alone.

Targeted searches for the exact formula, its tangent-line formulation, Erdős–Mordell polygon variants, and cyclic/tangential aliases found the 2016 conjecture, the triangle theorem, and regular-polygon special cases, but no source giving the general proof. Published-finding searches likewise returned results on reduced polygons, bicentric quadrilaterals, regular polygons in Minkowski norms, and triangle roundness, none of which implies this tangent-distance inequality.

## Limitations
The result concerns convex cyclic polygons in the Euclidean plane and interior points. It does not assert an analogue for nonconvex star polygons, points outside the polygon, non-Euclidean metrics, or the case of a formally unbounded tangent polygon created by consecutive antipodal vertices.

The literature search cannot prove absolute historical novelty. In particular, an equivalent argument may exist under older terminology for pedal distances, polar duality of cyclic polygons, or discrete Wirtinger inequalities. No such source was located in the inspected materials. The direct 2016 conjecture page still displayed no answer in the inspected version, but web-page status is not a substitute for exhaustive bibliographic coverage.

## References
1. Đào Thanh Oai, “An inequality in cyclic polygon and tangential polygon,” MathOverflow, asked July 24, 2016. https://mathoverflow.net/questions/244984/an-inequality-in-cyclic-polygon-and-tangential-polygon
2. Dao Thanh Oai, Nguyen Tien Dung, and Pham Ngoc Mai, “A Strengthened Version of the Erdős–Mordell Inequality,” Forum Geometricorum 16 (2016), 317–321, MR 3556993. https://forumgeom.fau.edu/FG2016volume16/FG201638.pdf
3. Hans-Christof Lenhard, “Verallgemeinerung und Verschärfung der Erdös-Mordellschen Ungleichung für Polygone,” Archiv für Mathematische Logik und Grundlagenforschung 12 (1961), 311–314. https://doi.org/10.1007/BF01650566
