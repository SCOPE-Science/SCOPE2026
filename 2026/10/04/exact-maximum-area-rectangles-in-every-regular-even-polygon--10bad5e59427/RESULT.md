# Exact maximum-area rectangles in every regular even polygon

## Finding

Let \(P_n\) be a regular even \(n\)-gon with \(n\ge4\) and circumradius \(R\). Let \(M(P_n)\) be the maximum area of a Euclidean rectangle contained in \(P_n\), with no restriction on orientation. Then
\[
M(P_n)=
\begin{cases}
2R^2,& n\equiv0\pmod4,\\
2R^2\cos\!\left(\frac{\pi}{n}\right),& n\equiv2\pmod4.
\end{cases}
\]

There is always an optimal rectangle centered at the center of \(P_n\). Among centered rectangles, all maximizers have both half-diagonal rays through vertices of \(P_n\). When \(4\mid n\), the two half-diagonal lines are orthogonal and the optimum is a square with four polygon vertices as corners. When \(n\equiv2\pmod4\), the acute angle between the two half-diagonal lines is
\[
\frac{\pi}{2}-\frac{\pi}{n},
\]
and the four rectangle corners are two antipodal pairs of polygon vertices.

For example, if \(R=1\), the regular hexagon has optimum \(\sqrt3\), the regular octagon has optimum \(2\), and the regular decagon has optimum \(2\cos(\pi/10)\).

## Assumptions and scope

The rectangle is required to lie in the whole regular polygon, not merely to have its vertices in the circumdisk. Degenerate rectangles have area zero and are irrelevant. The result concerns even \(n\); regular odd polygons are not classified here.

The motivating literature studies maximum-area rectangles in general convex and simple polygons. Cabello, Cheong, Knauer, and Schlipf give an exact cubic-time algorithm for arbitrary convex polygons. Choi, Lee, and Ahn extend exact computation to simple polygons and again give a cubic-time convex-polygon algorithm. The present theorem specializes the continuous optimization problem to a canonical symmetric family and replaces algorithmic optimization by a closed formula with exact equality cases.

## Proof

First reduce every rectangle to a centered one without changing its area. Let \(K=-K\) be any centrally symmetric convex body, and suppose a rectangle in \(K\) has center \(c\) and half-side vectors \(u\) and \(v\), with \(u\perp v\). Its four vertices are
\[
c\pm u\pm v.
\]
For either independent choice of signs, the point \(\pm u\pm v\) is the midpoint of one original vertex \(c\pm u\pm v\) and the reflection through the origin of the opposite original vertex. Both endpoints of that midpoint segment lie in \(K\), so convexity gives
\[
\pm u\pm v\in K.
\]
Thus the centered rectangle with the same half-side vectors lies in \(K\) and has the same area. Since every regular even polygon is centrally symmetric, it is enough to optimize centered rectangles.

For a centered rectangle set
\[
p=u+v,\qquad q=u-v.
\]
The vectors \(p\) and \(q\) are its half-diagonals. Because \(u\perp v\),
\[
|p|=|q|=r.
\]
Conversely, any two equal-length vectors \(p,q\) in a centrally symmetric convex body determine the centered rectangle with corner set \(\{p,q,-p,-q\}\). If \(\delta\in[0,\pi/2]\) is the acute angle between the half-diagonal lines, its area is
\[
A=2r^2\sin\delta.
\]

Scale temporarily to \(R=1\), and put
\[
\alpha=\frac{\pi}{n}.
\]
The vertex rays of \(P_n\) are spaced by \(2\alpha\). If a ray is at angular distance \(s\in[0,\alpha]\) from its nearest vertex ray, its radial reach in \(P_n\) is
\[
\rho(s)=\frac{\cos\alpha}{\cos(\alpha-s)}.
\]
Indeed, the relevant side has support distance \(\cos\alpha\), and the angle between the ray and the side normal is \(\alpha-s\). Notice that \(\rho(0)=1\), \(\rho(\alpha)=\cos\alpha\), and \(\rho\) is decreasing.

Suppose first that \(4\mid n\). For every centered rectangle, \(r\le1\) and \(\sin\delta\le1\), hence
\[
A\le2.
\]
There are orthogonal vertex rays because a quarter turn is an integer number of vertex steps, so taking \(r=1\) and \(\delta=\pi/2\) attains \(A=2\). Equality forces both inequalities to be equalities, hence both half-diagonal rays are vertex rays and are orthogonal.

Now suppose \(n\equiv2\pmod4\). Write \(n=4m+2\). Modulo reversal of a line, the vertex-line directions form \(2m+1\) equally spaced points on a circle of angular circumference \(\pi\). Their largest possible acute separation is
\[
\delta_0=\frac{\pi}{2}-\alpha.
\]
If \(\delta\le\delta_0\), then \(r\le1\), so
\[
A\le2\sin\delta\le2\sin\delta_0=2\cos\alpha.
\]
This bound is attained by choosing two vertex lines whose acute separation is \(\delta_0\).

It remains to rule out an improvement when \(\delta>\delta_0\). Write
\[
\delta=\delta_0+t,\qquad 0<t\le\alpha.
\]
Let \(s_1,s_2\in[0,\alpha]\) be the angular distances of the two half-diagonal lines from their nearest vertex lines. Any two vertex lines have acute separation at most \(\delta_0\), so the triangle inequality on the circle of unoriented lines gives
\[
s_1+s_2\ge t.
\]
Consequently \(\max(s_1,s_2)\ge t/2\), and the common half-diagonal length obeys
\[
r\le\rho(t/2)=\frac{\cos\alpha}{\cos(\alpha-t/2)}.
\]
Therefore
\[
\frac{A}{2}
\le
\frac{\cos^2\alpha\,\cos(\alpha-t)}{\cos^2(\alpha-t/2)}.
\]
The elementary identity
\[
\cos^2\!\left(\alpha-\frac t2\right)-\cos\alpha\cos(\alpha-t)
=\frac{1-\cos t}{2}
\]
shows that the right-hand side is at most \(\cos\alpha\), and it is strictly smaller when \(t>0\). Hence
\[
A\le2\cos\alpha,
\]
with equality exactly at \(t=0\) and \(r=1\), which forces both half-diagonal lines to be vertex lines of separation \(\delta_0\).

Rescaling from circumradius \(1\) to circumradius \(R\) multiplies area by \(R^2\), proving the formula and the centered equality classification.

## Verification

The centralization step was checked independently: for each sign pair, the centered vertex is the midpoint of two points known to lie in the centrally symmetric convex polygon. This preserves the side vectors, orthogonality, and area.

The radial formula was checked directly from the apothem \(\cos\alpha\). The mod-four split comes from the projective-circle lattice of vertex lines: when \(4\mid n\), a right angle is a vertex-line separation; when \(n\equiv2\pmod4\), the closest vertex-line separation to a right angle falls short by exactly \(\alpha\).

For the second case, the only nontrivial inequality is
\[
\cos\alpha\cos(\alpha-t)
\le
\cos^2\!\left(\alpha-\frac t2\right),
\]
whose deficit is exactly \((1-\cos t)/2\). This also certifies strictness for every \(t>0\).

A dense numerical angular sweep for \(n\in\{6,10,14,18\}\) independently located the predicted maximizing diagonal separation and matched the closed formula to the grid resolution; this computation was a sanity check only and is not used in the proof.

## Relationship to prior work

Knauer, Schlipf, Schmidt, and Tiwary study approximation algorithms for maximum-area rectangles in arbitrary convex polygons. Cabello, Cheong, Knauer, and Schlipf later give exact \(O(n^3)\)-time algorithms for maximum-area and maximum-perimeter rectangles in convex \(n\)-gons. Choi, Lee, and Ahn give exact algorithms for simple polygons and another \(O(n^3)\) convex-polygon algorithm.

The inspected full texts formulate and solve the general algorithmic problem, but no regular-polygon specialization or mod-four closed formula was found. In particular, direct text searches of the two most relevant full texts found no occurrence of “regular” in the sense of a regular-polygon special case. The theorem here does not improve the worst-case algorithms; instead it identifies the exact value and equality geometry for the infinite regular-even family.

## Limitations

No formula is claimed for regular odd polygons, maximum-perimeter rectangles, fixed-aspect-ratio rectangles, or general centrally symmetric polygons. The originality assessment is based on targeted semantic searches, exact-expression searches, and inspection of the most directly relevant primary texts. Because the proof is elementary once central symmetry is exploited, an equivalent special-case formula could exist in older recreational, textbook, or weakly indexed literature under different terminology.

## References

Y. Choi, S. Lee, and H.-K. Ahn, “Maximum-Area Rectangles in a Simple Polygon,” arXiv:1910.08686, first submitted 2019-10-19.

S. Cabello, O. Cheong, C. Knauer, and L. Schlipf, “Finding Largest Rectangles in Convex Polygons,” arXiv:1405.1223, first submitted 2014-05-06; later published in Computational Geometry 51 (2016), 67–74.

C. Knauer, L. Schlipf, J. M. Schmidt, and H. R. Tiwary, “Largest Inscribed Rectangles in Convex Polygons,” Journal of Discrete Algorithms 13 (2012), 78–85, DOI 10.1016/j.jda.2012.01.002.
