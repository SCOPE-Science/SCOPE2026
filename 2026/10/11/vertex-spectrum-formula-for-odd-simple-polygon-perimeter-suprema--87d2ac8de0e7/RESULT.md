# Vertex-spectrum formula for odd simple-polygon perimeter suprema
## Finding
Let \(C\subset\mathbb R^2\) be a nondegenerate Euclidean convex polygon with extreme-vertex set \(V\), and let \(m\ge3\) be odd. Define
\[
S_m(C)=\sup\{\operatorname{perim}P:P\subset C\text{ is a simple }m\text{-gon}\}.
\]
For \(T=(a,b,c)\in V^3\), put
\[
p(T)=|a-b|+|b-c|+|c-a|,
\qquad
d(T)=\max\{|a-b|,|b-c|,|c-a|\}.
\]
Then
\[
S_m(C)=\max_{T\in V^3}\left(p(T)+(m-3)d(T)\right).
\]
Consequently the entire odd-index spectrum \(m\mapsto S_m(C)\) is the upper envelope of finitely many affine functions.

Let
\[
D=\operatorname{diam}C,
\qquad
P_D=\max\{p(T):T\in V^3,\ d(T)=D\}.
\]
If
\[
m-3\ge
\max_{T:\,d(T)<D}
\frac{(p(T)-P_D)_+}{D-d(T)},
\qquad
(x)_+=\max\{x,0\},
\]
then
\[
S_m(C)=P_D+(m-3)D.
\]
Thus only finitely many phase changes can occur as the odd number of sides grows, and the final phase is always controlled by a vertex triangle containing a diameter of \(C\).

For a regular pentagon of unit side length, write \(\varphi=(1+\sqrt5)/2\). For every odd \(m\ge3\),
\[
S_m(C)=1+(m-1)\varphi.
\]
The maximizing vertex triangles are precisely the five triples with side-length multiset \(\{1,\varphi,\varphi\}\).

## Assumptions and scope
A simple polygon has no self-intersections except that consecutive edges meet at their common endpoint. The quantity \(S_m(C)\) is a supremum. For \(m=3\) it is attained by a maximizing triangle. For \(m\ge5\), the proof only requires arbitrarily close simple approximants to a triangle with a multiple longest edge; no assertion about attainment by a nondegenerate \(m\)-gon is made.

The set \(V\) consists of the extreme vertices of \(C\), so no element of \(V\) lies in the relative interior of an edge of \(C\). Distances are Euclidean.

## Proof
Lángi proved that for every odd \(m\ge3\) and every simple \(m\)-gon \(P\subset C\), there is an inscribed triangle with side lengths \(\alpha\ge\beta\ge\gamma\) such that
\[
\operatorname{perim}P\le (m-2)\alpha+\beta+\gamma.
\]
For a triple \((x,y,z)\in C^3\), define
\[
G_m(x,y,z)=|x-y|+|y-z|+|z-x|
 +(m-3)\max\{|x-y|,|y-z|,|z-x|\}.
\]
The source theorem gives
\[
S_m(C)\le \max_{(x,y,z)\in C^3}G_m(x,y,z).
\]

Each map \((x,y,z)\mapsto |x-y|\), and similarly the other two distance maps, is convex. The maximum of finitely many convex functions is convex, and \(m-3\ge0\). Hence \(G_m\) is convex on the product polytope \(C^3\). Every point of \(C^3\) is a convex combination of points of \(V^3\); Jensen's inequality therefore gives
\[
\max_{C^3}G_m=\max_{V^3}G_m.
\]
This proves the upper bound in the displayed formula.

For the reverse inequality, first note that a maximizing vertex triple can be chosen nondegenerate. A triple with a repeated vertex has value at most \((m-1)D\). If \(a,b\in V\) are diameter endpoints and \(c\in V\) is off their line, then strict triangle inequality gives
\[
G_m(a,b,c)=(m-2)D+|a-c|+|b-c|>(m-1)D.
\]
Thus no repeated triple can maximize.

Now fix a nondegenerate triangle \(abc\subset C\) and suppose \([a,b]\) is a longest side. For \(m=3\), the triangle itself realizes \(G_3(a,b,c)\). For odd \(m\ge5\), put \(q=m-2\), which is odd. After a rigid motion take \([a,b]\) horizontal and \(c\) above it. For sufficiently small \(\varepsilon>0\), choose points
\[
x_0,x_1,\ldots,x_q
\]
inside the triangle so that their heights increase strictly from \(0\) to \(\varepsilon\), \(x_0=a\), the even-indexed points are arbitrarily close to the side through \(a\), and the odd-indexed points are arbitrarily close to the side through \(b\). Connect
\[
x_0x_1,x_1x_2,\ldots,x_{q-1}x_q,x_qc,cx_0.
\]
Nonadjacent zigzag edges lie in disjoint horizontal slabs, while the final two edges lie above the zigzag or on the outer side of it, so this is a simple \(m\)-gon for small enough \(\varepsilon\). As \(\varepsilon\downarrow0\), its first \(q=m-2\) edge lengths tend to \(|a-b|\), and the last two tend to \(|b-c|\) and \(|c-a|\). Hence its perimeter tends to
\[
(m-2)|a-b|+|b-c|+|c-a|=G_m(a,b,c).
\]
Therefore \(S_m(C)\ge\max_{V^3}G_m\), proving equality.

The phase statement is now finite algebra. Each vertex triple contributes the affine function
\[
m\longmapsto p(T)+(m-3)d(T).
\]
Among triples with \(d(T)=D\), the largest intercept is \(P_D\). A triple with \(d(T)<D\) is no larger than the diameter class exactly when
\[
p(T)+(m-3)d(T)\le P_D+(m-3)D,
\]
which rearranges to the stated threshold. Taking the maximum over the finitely many subdiametral triples proves eventual stabilization.

For the unit-side regular pentagon, every distance between distinct vertices is either \(1\) or
\[
\varphi=\frac{1+\sqrt5}{2}.
\]
Every distinct vertex triple has one of two side-length multisets:
\[
\{1,1,\varphi\}
\quad\text{or}\quad
\{1,\varphi,\varphi\}.
\]
Their contributions are respectively
\[
2+(m-2)\varphi
\quad\text{and}\quad
1+(m-1)\varphi.
\]
The second exceeds the first by \(\varphi-1>0\). Any repeated-vertex triple contributes at most \((m-1)\varphi\), which is smaller by \(1\). Hence the five \(\{1,\varphi,\varphi\}\) triangles are exactly the maximizing vertex triples and
\[
S_m(C)=1+(m-1)\varphi
\]
for every odd \(m\ge3\).

## Verification
The accompanying `verify.py` checks the regular-pentagon classification symbolically in \(\mathbb Q(\sqrt5)\). It enumerates all ordered vertex triples using the exact two-distance metric of the unit-side regular pentagon, confirms that the only maximizing distinct-triple type is \(\{1,\varphi,\varphi\}\), verifies the closed formula for symbolic odd parameter \(m\), and checks representative odd values from \(3\) through \(31\).

The finite checker is only a reproducibility check for the pentagon corollary. The general theorem follows from Lángi's source theorem, convexity on \(C^3\), and the explicit simple-polygon approximation above.

## Relationship to prior work
Lángi's paper solves the continuous convex-body problem by proving that every odd simple-polygon perimeter is bounded by the weighted perimeter of an inscribed triangle, and its introduction explains the multiple-edge triangle as the corresponding supremal configuration. The paper also illustrates maximizing triangles for a square and a disk. It does not state a finite reduction to extreme vertex triples for polygonal containers, an upper-envelope description of the full odd-index spectrum, an eventual diameter phase, or the regular-pentagon formula above.

Audet, Hansen, and Messine solved the earlier unit-disk problem; that result is a special container and does not imply the polygonal vertex-spectrum statement.

Targeted searches using the phrases “convex polygon”, “vertex triple”, “simple polygon perimeter”, “upper envelope”, “diameter phase”, “regular pentagon”, and the golden-ratio formula found no statement covering the theorem.

## Limitations
The reduction is specific to Euclidean polygonal containers. Although Lángi's source theorem also covers the hyperbolic plane, the convexity argument used here relies on the Euclidean norm and on the ordinary product polytope \(C^3\); no hyperbolic finite-vertex analogue is claimed.

The theorem determines a supremum. It does not classify all near-maximizing simple polygons, and it does not assert that the supremum is attained for \(m\ge5\).

The phase threshold is exact but may not be the smallest odd integer at which a diameter triple wins if equality ties are simplified in a particular polygon; the finite maximum formula itself resolves such ties exactly.

## References
1. Z. Lángi, *On the perimeters of simple polygons contained in a plane convex body*, arXiv:1003.2944, first public 2010-03-15; Beiträge zur Algebra und Geometrie 54 (2013), 643--649; DOI: 10.1007/s13366-012-0120-8. The relevant source statements are the Euclidean theorem and the introductory multiple-edge interpretation.
2. C. Audet, P. Hansen, and F. Messine, *Simple polygons of maximum perimeter contained in a unit disk*, Discrete & Computational Geometry 41 (2009), 208--215; public GERAD report G-2007-56.
