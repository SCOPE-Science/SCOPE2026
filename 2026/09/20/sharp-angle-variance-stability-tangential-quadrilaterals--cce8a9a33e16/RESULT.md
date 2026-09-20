# Sharp angle-variance stability for Ivanova's tangential-quadrilateral inequality

## Result

Let \(Q\) be a nondegenerate convex tangential quadrilateral with inradius \(r>0\), semiperimeter \(s\), area \(K\), and interior angles
\[
A_1,A_2,A_3,A_4\in(0,\pi),\qquad \sum_{i=1}^4 A_i=2\pi .
\]
Then
\[
\boxed{
s-4r\ge
\frac{3(3\sqrt3-4)}{\pi^2}\,r
\sum_{i=1}^4\left(A_i-\frac{\pi}{2}\right)^2
}
\tag{1}
\]
and, since \(K=rs\),
\[
\boxed{
K-4r^2\ge
\frac{3(3\sqrt3-4)}{\pi^2}\,r^2
\sum_{i=1}^4\left(A_i-\frac{\pi}{2}\right)^2 .
}
\tag{2}
\]
The constant
\[
\kappa_*=\frac{3(3\sqrt3-4)}{\pi^2}
       \approx 0.3635867378558577
\]
is the largest possible universal constant in (1) and (2).

For a proper quadrilateral, equality in either inequality holds only for the square. The sharp constant is not attained by a nonsquare proper quadrilateral: it is approached by a degenerating one-parameter family whose interior-angle vector tends, up to permutation, to
\[
(\pi,\pi/3,\pi/3,\pi/3).
\]

Thus the classical Ivanova inequality \(s\ge4r\), equivalently \(K\ge4r^2\), admits a globally sharp quadratic stability refinement in the angle variance.

## Reduction to a sharp trigonometric inequality

Put
\[
x_i=\frac{\pi-A_i}{2}\in(0,\pi/2).
\]
These are half of the exterior turning angles and satisfy
\[
\sum_{i=1}^4x_i=\pi.
\]
At a vertex with interior angle \(A_i\), the tangent length from that vertex to either neighboring point of tangency is
\[
r\cot\frac{A_i}{2}=r\tan x_i.
\]
Therefore
\[
\frac{s}{r}=\sum_{i=1}^4\tan x_i,
\qquad
\frac{K}{r^2}=\frac{s}{r},
\]
and
\[
\sum_{i=1}^4\left(A_i-\frac{\pi}{2}\right)^2
=
4\sum_{i=1}^4\left(x_i-\frac{\pi}{4}\right)^2.
\]
Hence it is enough to prove
\[
\sum_{i=1}^4\tan x_i-4
\ge
c_*
\sum_{i=1}^4\left(x_i-\frac{\pi}{4}\right)^2,
\qquad
c_*=\frac{12(3\sqrt3-4)}{\pi^2}.
\tag{3}
\]

## Proof of the sharp trigonometric inequality

Let \(\mu=\pi/4\) and define
\[
G(x_1,\ldots,x_4)
=
\sum_{i=1}^4\tan x_i-4
-c_*\sum_{i=1}^4(x_i-\mu)^2
\]
on
\[
\mathcal S=\{x_i\in(0,\pi/2):\ \sum x_i=\pi\}.
\]

### 1. Finite boundary points

If a sequence in \(\mathcal S\) tends to the boundary and one coordinate tends to \(\pi/2\), then \(G\to+\infty\). Thus every finite boundary point has, after permutation, the form
\[
(0,y_1,y_2,y_3),\qquad y_1+y_2+y_3=\pi.
\]
Writing \(\nu=\pi/3\),
\[
\sum_{i=1}^4(x_i-\mu)^2
=
\frac{\pi^2}{12}+\sum_{j=1}^3(y_j-\nu)^2.
\tag{4}
\]
Since \(c_*\pi^2/12=3\sqrt3-4\), (4) gives
\[
G=
\left(\sum_{j=1}^3\tan y_j-3\sqrt3\right)
-c_*\sum_{j=1}^3(y_j-\nu)^2.
\tag{5}
\]

For \(f(y)=\tan y\), the second-order tangent quotient at \(\nu\) is
\[
H_\nu(y)=
\frac{f(y)-f(\nu)-f'(\nu)(y-\nu)}{(y-\nu)^2}
=
\int_0^1(1-t)f''(\nu+t(y-\nu))\,dt.
\]
Because
\[
f'''(y)=2\sec^2y\,(1+3\tan^2y)>0,
\]
\(H_\nu(y)\) is increasing in \(y\). Hence
\[
H_\nu(y)\ge H_\nu(0)
=
\frac{12\pi-9\sqrt3}{\pi^2}
>c_*.
\tag{6}
\]
The final strict inequality follows, for example, from
\(12\pi+48-45\sqrt3>0\).
Summing the corresponding tangent-line inequalities and using
\(\sum(y_j-\nu)=0\) shows that the right side of (5) is nonnegative.
It vanishes only at \(y_1=y_2=y_3=\pi/3\). Thus the only finite boundary zero of \(G\), up to permutation, is
\[
(0,\pi/3,\pi/3,\pi/3).
\tag{7}
\]

### 2. Interior critical points

At an interior constrained critical point,
\[
\sec^2x_i-2c_*(x_i-\mu)=\lambda
\qquad(i=1,\ldots,4).
\tag{8}
\]
Set
\[
h(x)=\sec^2x-2c_*(x-\mu).
\]
Since \(h''(x)>0\), each horizontal line meets the graph of \(h\) in at most two points. If two roots \(a<b\) occur at the same level, strict convexity gives
\[
h'(a)<0<h'(b).
\]
But the diagonal Hessian entry of \(G\) is exactly \(h'(x)\). Therefore the smaller root \(a\) cannot occur twice at a constrained local minimum: exchanging two equal \(a\)-coordinates would give a negative second variation. Consequently every nonregular interior local minimum has, up to permutation, the form
\[
(a,b,b,b),\qquad a+3b=\pi,\qquad
0<a<\frac{\pi}{4}<b<\frac{\pi}{3}.
\tag{9}
\]

It remains to show \(G>0\) on (9). Put
\[
t=b-\frac{\pi}{4}\in(0,\pi/12),
\qquad
z=\tan b\in(1,\sqrt3).
\]
Then \(a=\pi-3b\), and the triple-angle identity gives
\[
\tan a+3\tan b
=
-\tan(3b)+3\tan b
=
\frac{8z^3}{3z^2-1}.
\]
Hence, with
\[
N(z)=\tan a+3\tan b-4,
\]
we have
\[
N(z)=
\frac{4(z-1)^2(2z+1)}{3z^2-1},
\qquad
\sum_{i=1}^4(x_i-\mu)^2=12t^2.
\tag{10}
\]

We claim that \(N(z)/t^2\) is strictly decreasing on \(1<z<\sqrt3\). Here
\[
N'(z)=\frac{24z^2(z-1)(z+1)}{(3z^2-1)^2}>0.
\]
Since \(t=\arctan z-\pi/4\), differentiating shows the desired monotonicity is equivalent to
\[
t\le
\rho(z):=
\frac{2N(z)}{(1+z^2)N'(z)}
=
\frac{(z-1)(2z+1)(3z^2-1)}
{3z^2(z+1)(z^2+1)}.
\tag{11}
\]
Let \(D(z)=\rho(z)-(\arctan z-\pi/4)\). Then \(D(1)=0\) and
\[
D'(z)=
-\frac{(z-1)P(z)}
{3z^3(z+1)^2(z^2+1)^2},
\tag{12}
\]
where
\[
P(z)=
9z^6+9z^5-9z^4-21z^3-12z^2-6z-2.
\]
The coefficient sequence of \(P\) has exactly one sign change, so Descartes' rule of signs gives exactly one positive root. Moreover
\[
P(1)=-32,\qquad
P(\sqrt3)=124+12\sqrt3>0.
\]
Thus \(D\) first increases and then decreases on \([1,\sqrt3]\). Finally,
\[
D(\sqrt3)
=
\frac{2\sqrt3}{3}-\frac89-\frac{\pi}{12}>0;
\]
one elementary verification is
\[
\frac{2\sqrt3}{3}-\frac89-\frac{\pi}{12}
>
\frac{38}{33}-\frac89-\frac{11}{42}
=
\frac1{1386}>0.
\]
Therefore \(D(z)>0\) for \(1<z\le\sqrt3\), proving the monotonicity claim. By (10),
\[
\frac{N(z)}{t^2}
>
\frac{N(\sqrt3)}{(\pi/12)^2}
=
\frac{144(3\sqrt3-4)}{\pi^2}
=
12c_*.
\]
Hence every nonregular interior critical point in (9) has \(G>0\).

Combining the finite-boundary analysis, the blow-up at \(x_i\to\pi/2\), and the interior critical-point classification yields \(G\ge0\) on \(\mathcal S\). This proves (3), and therefore (1) and (2).

## Sharpness and equality

Take
\[
x_1=\varepsilon,\qquad
x_2=x_3=x_4=\frac{\pi-\varepsilon}{3},
\qquad \varepsilon\downarrow0.
\]
These angle data are realized by four successive tangent lines to a fixed circle whose exterior turning angles are \(2x_i\). They define proper convex tangential quadrilaterals for every \(\varepsilon>0\). Along this family,
\[
\sum\tan x_i-4\longrightarrow3\sqrt3-4
\]
and
\[
\sum\left(x_i-\frac{\pi}{4}\right)^2
\longrightarrow\frac{\pi^2}{12}.
\]
Thus the quotient in (3) tends to \(c_*\), and the quotient in (1)–(2) tends to
\(\kappa_*=c_*/4\). No larger universal constant is possible.

For a proper quadrilateral, the boundary sharpness configuration is excluded. The proof above leaves only the regular point
\(x_i=\pi/4\), equivalently \(A_i=\pi/2\), as an equality case; a tangential quadrilateral with four right angles is a square.

## Context and originality boundary

The inequality
\[
s\ge4r
\]
for tangential quadrilaterals, with equality only for the square, is attributed to T. A. Ivanova in the literature. Josefsson's 2023 compilation gives both the equivalent area statement \(K\ge4r^2\) and a proof of \(s\ge4r\) from
\[
s=r(\tan\alpha+\tan\beta+\tan\gamma+\tan\delta),
\qquad
\alpha+\beta+\gamma+\delta=\pi,
\]
followed by Jensen's inequality.

Recent square-characterization compilations continue to record the qualitative equality characterization. A 2026 quantitative Pólya--Szegő theorem for tangential polygons contains a nonnegative angular Jensen deficit in a torsional-rigidity estimate, but its stated target and deficit are different from the sharp semiperimeter/area-versus-angle-variance inequality above.

No source located in the checked tangential-quadrilateral, square-characterization, and quantitative tangential-polygon literature states (1) or (2), the constant
\[
\frac{3(3\sqrt3-4)}{\pi^2},
\]
or the boundary family proving its optimality. Originality is therefore asserted only **to the best of our knowledge**. Because the analytic core is a sharp refinement of a four-variable Jensen inequality for \(\tan\), an equivalent statement could exist in older trigonometric-inequality or approximation literature under unrelated terminology.

## Limitations

- The theorem is for Euclidean convex tangential quadrilaterals.
- Stability is measured by the squared Euclidean variance of the four interior angles; no Hausdorff, side-length, or vertex-coordinate stability is claimed.
- The best constant is approached only through degenerating quadrilaterals; among proper nonsquare quadrilaterals it is not attained.
- The result does not claim the analogous best constant for general tangential \(N\)-gons.
- Originality is to the best of our knowledge, with residual risk from differently phrased sharp Jensen refinements.

## References

1. Martin Josefsson, *Great compilation of characterizations of squares*, International Journal of Geometry 12 (2023), no. 3, 13–37.  
   https://ijgeometry.com/wp-content/uploads/2023/06/2.-13-37.pdf

2. Martin Josefsson and Mario Dalcín, *150 characterizations of squares*, International Journal of Geometry 14 (2025), no. 2, 5–34.  
   https://ijgeometry.com/vol-14-2025-no-2-april/

3. Changfeng Gui, Yeyao Hu, Qinfeng Li, *A Quantitative Pólya--Szegő Theorem for Tangential Polygons*, arXiv:2607.28768v2 (2026).  
   https://arxiv.org/abs/2607.28768

4. Eric W. Weisstein, *Tangential Quadrilateral*, MathWorld (background formulas).  
   https://mathworld.wolfram.com/TangentialQuadrilateral.html
