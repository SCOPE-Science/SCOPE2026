# Exact mean-square width of every uniform regular prism
## Finding
For every integer \(n\ge3\), let \(P_n\subset\mathbb R^3\) be the uniform right \(n\)-gonal prism whose regular base edges and vertical edges all have length \(1\). If \(U\) is uniformly distributed on \(S^2\) and
\[
W_n=w_{P_n}(U),
\]
then
\[
\boxed{
\mathbb E W_n^2=
\begin{cases}
\displaystyle
\frac13+\frac{1}{3\sin^2(\pi/n)}+
\frac{n}{3\pi}\left(2+\cot\frac{\pi}{n}\right),& n\ \text{even},\\[9pt]
\displaystyle
\frac13+\frac{1}{12\sin^2(\pi/(2n))}+
\frac{n}{6\pi}\left(4+\cot\frac{\pi}{2n}\right),& n\ \text{odd}.
\end{cases}}
\tag{1}
\]
For \(n=4\), equation (1) becomes
\[
\mathbb E W_4^2=1+\frac4\pi,
\]
the classical unit-cube value.

## Assumptions and scope
The base \(B_n\subset\mathbb R^2\) is a regular \(n\)-gon with side length \(1\), centered at the origin, and
\[
P_n=B_n\times[-1/2,1/2].
\]
Thus every edge of \(P_n\) has length \(1\). This is the standard uniform-prism normalization.

For a convex body \(K\),
\[
w_K(u)=h_K(u)+h_K(-u)
\]
is its width in direction \(u\).

The result gives only the second directional-width moment. It does not give the full width distribution or higher moments for the prism family.

## Proof
Write a uniform random direction as
\[
U=(\sqrt{1-Z^2}\,V,Z),
\]
where \(Z\) is uniform on \([-1,1]\), \(V\) is uniform on \(S^1\), and \(Z,V\) are independent. Because support functions add under Cartesian products,
\[
W_n=\sqrt{1-Z^2}\,w_{B_n}(V)+|Z|.
\tag{2}
\]
Squaring and averaging gives
\[
\mathbb E W_n^2
=
\mathbb E(1-Z^2)\,\mathbb E w_{B_n}(V)^2
+
\mathbb E Z^2
+
2\mathbb E\!\left(|Z|\sqrt{1-Z^2}\right)\mathbb E w_{B_n}(V).
\]
The one-dimensional integrals are
\[
\mathbb E(1-Z^2)=\frac23,
\qquad
\mathbb E Z^2=\frac13,
\qquad
\mathbb E\!\left(|Z|\sqrt{1-Z^2}\right)=\frac13.
\]
Hence
\[
\mathbb E W_n^2
=
\frac23 M_{2,n}+\frac13+\frac23 M_{1,n},
\tag{3}
\]
where
\[
M_{1,n}=\mathbb E w_{B_n}(V),
\qquad
M_{2,n}=\mathbb E w_{B_n}(V)^2.
\]

Cauchy's planar perimeter formula gives
\[
M_{1,n}=\frac{\operatorname{per}(B_n)}{\pi}=\frac n\pi.
\tag{4}
\]
It remains to evaluate \(M_{2,n}\).

For every planar convex body,
\[
w_{B_n}(v)=h_{B_n-B_n}(v).
\tag{5}
\]
If \(n\) is even, \(B_n\) is centrally symmetric, so
\[
B_n-B_n=2B_n.
\]
The difference body is therefore a regular \(n\)-gon with circumradius
\[
R_n^{\rm ev}=\frac1{\sin(\pi/n)}.
\tag{6}
\]

If \(n\) is odd, the extreme differences are obtained from the two nearly antipodal vertex separations. They alternate in angle, so \(B_n-B_n\) is a regular \(2n\)-gon. Since the base circumradius is
\[
\frac1{2\sin(\pi/n)},
\]
the difference-body circumradius is
\[
R_n^{\rm odd}
=
\frac{\cos(\pi/(2n))}{\sin(\pi/n)}
=
\frac1{2\sin(\pi/(2n))}.
\tag{7}
\]

Now let \(D_m\) be a regular \(m\)-gon of circumradius \(R\). On the normal cone of one vertex, parameterized by
\[
-\frac\pi m\le t\le\frac\pi m,
\]
its support function is
\[
h_{D_m}(t)=R\cos t.
\]
Therefore
\[
\frac1{2\pi}\int_0^{2\pi}h_{D_m}(v)^2\,dv
=
R^2\left(
\frac12+\frac{m\sin(2\pi/m)}{4\pi}
\right).
\tag{8}
\]

For even \(n\), substitute \(m=n\) and (6) into (8):
\[
M_{2,n}
=
\frac1{\sin^2(\pi/n)}
\left(
\frac12+\frac{n\sin(2\pi/n)}{4\pi}
\right).
\tag{9}
\]
Combining (3), (4), and (9) gives
\[
\mathbb E W_n^2
=
\frac13+\frac{1}{3\sin^2(\pi/n)}+
\frac{n}{3\pi}\left(2+\cot\frac\pi n\right).
\]

For odd \(n\), substitute \(m=2n\) and (7) into (8):
\[
M_{2,n}
=
\frac1{4\sin^2(\pi/(2n))}
\left(
\frac12+\frac{n\sin(\pi/n)}{2\pi}
\right).
\tag{10}
\]
Equations (3), (4), and (10) give
\[
\mathbb E W_n^2
=
\frac13+\frac{1}{12\sin^2(\pi/(2n))}+
\frac{n}{6\pi}\left(4+\cot\frac\pi{2n}\right).
\]
This proves (1).

## Verification
The bundled `verify.py` checks equations (5)--(10) in two independent numerical ways. First it directly samples the planar width of regular polygons and compares its first two moments with the difference-body formulas. Second it samples the three-dimensional prism width on a deterministic Fibonacci sphere and compares the resulting second moment with (1) for several even and odd values of \(n\).

The numerical tests are regression checks only. The proof of (1) is the exact product decomposition (2), Cauchy's formula (4), the exact difference-body descriptions (6)--(7), and the elementary normal-cone integral (8).

## Relationship to prior work
Finch introduced exact mean-square-width calculations for regular polyhedra, obtaining the unit-edge tetrahedron and cube values and explicitly expressing the hope that analogous computations would be made for other convex bodies.

Kabluchko, Litvak, and Zaporozhets later proved a higher-moment Sudakov formula for random projection length and explicitly evaluated the regular cube, simplex, and crosspolytope families. Their paper has primary MSC \(52A23\). Its full searchable text contains no occurrence of “prism,” so it supplies the general moment framework but not formula (1).

The present result gives the entire infinite family of uniform regular prisms. The cube appears as the single case \(n=4\), while both parity branches are controlled by the planar difference body of the regular base.

Targeted searches for regular-prism mean-square width, second width moment, random projection length, mean caliper diameter, and Feret-diameter formulations did not locate a prior formula equivalent to (1).

## Limitations
The formula applies to right uniform prisms with base-edge and height both equal to \(1\). A general height \(h>0\) can be handled by the same decomposition, but that scaling variant is not part of the accepted claim.

The result concerns only the second moment, not the full width law. It also does not treat antiprisms or arbitrary nonregular prism bases.

A classical stereological source could record an equivalent formula under older caliper or Feret terminology; this remains the main bibliographic residual risk.

## References
1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, 4 October 2011.
2. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1, 26 November 2015.
