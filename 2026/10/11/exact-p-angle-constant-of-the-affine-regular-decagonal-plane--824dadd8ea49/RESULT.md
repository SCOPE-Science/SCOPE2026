# Exact P-angle constant of the affine-regular decagonal plane
## Finding
Put
\[
r=\frac{\sqrt5-1}{2},
\qquad
\phi=1+r=\frac{1+\sqrt5}{2}.
\]
Let
\[
X_{10}=(\mathbb R^2,N_{10}),
\]
where
\[
N_{10}(s,t)
=
\max\{
|s+t|,
|rs+t|,
r|t|,
r|s|,
|s+rt|
\}.
\]
For every
\[
x,y\in S_{X_{10}},
\qquad
x\ne\pm y,
\]
write
\[
A=N_{10}(x+y),
\qquad
B=N_{10}(x-y).
\]
Then the two sharp weighted chord inequalities
\[
\boxed{A+rB\le3-r},
\qquad
\boxed{rA+B\le3-r}
\tag{1}
\]
hold.

Consequently, for the Yang--Li P-angle constant
\[
S_P(X)
=
\sup_{\substack{x,y\in S_X\\x\ne\pm y}}
\cos\operatorname{ang}_P(x+y,x-y),
\]
one has
\[
\boxed{
S_P(X_{10})
=
\frac r4
=
\frac{\sqrt5-1}{8}
}.
\tag{2}
\]
The value is attained by the adjacent vertices
\[
x=(1,0),
\qquad
y=(0,1).
\]

## Assumptions and scope
All scalars are real. We use the P-angle formula
\[
\cos\operatorname{ang}_P(u,v)
=
\frac{\|u\|^2+\|v\|^2-\|u-v\|^2}{2\|u\|\|v\|},
\qquad
u,v\ne0.
\tag{3}
\]
The defining preprint for \(S_P\) places a standing dimension assumption in its preliminary section, but its displayed definition is meaningful in dimension two and its geometric discussion explicitly treats the Euclidean plane. Here \(S_P\) denotes that same displayed supremum for the two-dimensional Minkowski norm above.

The unit ball of \(N_{10}\) has the ten vertices
\[
(1,0),\ (0,1),\ (-1,\phi),\ (-\phi,\phi),\ (-\phi,1)
\]
and their negatives. A cyclic list of the ten signed facet functionals is
\[
(r,0),\ (1,r),\ (1,1),\ (r,1),\ (0,r)
\]
and their negatives. Every listed facet has dual norm one.

## Proof
Let \(f\) and \(g\) be signed norming facets satisfying
\[
f(x+y)=A,
\qquad
g(x-y)=B.
\]
Because \(x\) and \(y\) are unit vectors,
\[
\begin{aligned}
A+rB
&=(f+rg)(x)+(f-rg)(y)\\
&\le \|f+rg\|_*+\|f-rg\|_*.
\end{aligned}
\tag{4}
\]
By decagonal symmetry it is enough to fix one signed facet and vary the cyclic separation of the other. Exact evaluation of the dual norm on the ten primal vertices gives the complete table
\[
\begin{array}{c|c|c|c}
k&\|f+rg\|_*&\|f-rg\|_*&\text{sum}\\
\hline
0&\phi&r^2&2\\
1&\phi&r&\sqrt5\\
2&\frac{5-\sqrt5}{2}&1&\frac{7-\sqrt5}{2}\\
3&1&\frac{5-\sqrt5}{2}&\frac{7-\sqrt5}{2}\\
4&r&\phi&\sqrt5\\
5&r^2&\phi&2.
\end{array}
\tag{5}
\]
Since
\[
\frac{7-\sqrt5}{2}=3-r,
\]
equations (4)--(5) prove the first inequality in (1). Replacing \(y\) by \(-y\) interchanges \(A\) and \(B\), proving the second.

The triangle inequality also gives
\[
0\le A\le2,
\qquad
0\le B\le2.
\]
Thus every feasible chord pair lies in the polygon
\[
\mathcal P
=
\left\{
(A,B):
0\le A,B\le2,
\ A+rB\le3-r,
\ rA+B\le3-r
\right\}.
\tag{6}
\]
Its vertices are
\[
(0,0),\ (2,0),\ (2,r),\ (c,c),\ (r,2),\ (0,2),
\tag{7}
\]
where
\[
c=\frac{3-r}{1+r}=2\sqrt5-3.
\]

For \(x\ne\pm y\), both \(A\) and \(B\) are positive. Applying (3) to
\[
u=x+y,
\qquad
v=x-y
\]
and using
\[
\|u-v\|=\|2y\|=2
\]
gives
\[
\cos\operatorname{ang}_P(x+y,x-y)
=
\frac{A^2+B^2-4}{2AB}.
\tag{8}
\]
Consider the quadratic form
\[
Q(A,B)
=A^2+B^2-\frac r2AB.
\tag{9}
\]
Its Hessian has eigenvalues
\[
2-\frac r2
\quad\text{and}\quad
2+\frac r2,
\]
so \(Q\) is convex. A convex function on the polygon \(\mathcal P\) has a maximum at a vertex. At the six vertices in (7),
\[
Q(0,0)=0,
\]
\[
Q(2,0)=Q(0,2)=Q(2,r)=Q(r,2)=4,
\]
and
\[
Q(c,c)
=
\frac{321-137\sqrt5}{4}
<4.
\tag{10}
\]
The last inequality follows from
\[
137\sqrt5>305,
\]
which is equivalent after squaring to
\[
93845>93025.
\]
Hence
\[
A^2+B^2-\frac r2AB\le4.
\]
Substitution into (8) yields
\[
\cos\operatorname{ang}_P(x+y,x-y)
\le
\frac r4.
\tag{11}
\]

For sharpness choose
\[
x=(1,0),
\qquad
y=(0,1).
\]
Both are unit vectors and
\[
N_{10}(x+y)=2,
\qquad
N_{10}(x-y)=r.
\]
Therefore
\[
\cos\operatorname{ang}_P(x+y,x-y)
=
\frac{4+r^2-4}{4r}
=
\frac r4.
\]
This proves (2), while the same pair also makes the first inequality in (1) an equality.

## Verification
The bundled `verify.py` works exactly in the quadratic field
\[
\mathbb Q(\sqrt5).
\]
It verifies all ten primal vertices and all ten signed dual facets, checks all one hundred ordered signed-facet pairs in (4), reproduces the six-row dual table (5), validates the six vertices of \(\mathcal P\), checks the exact central value in (10), and replays the equality pair.

No finite experiment is used as an infinite proof. The exhaustive part is finite because the norm has exactly ten signed facets; the passage from the facet table to all unit vectors is the dual-norm inequality (4), and the final optimization is over the explicitly proved polygonal envelope (6).

## Relationship to prior work
Yang and Li introduced \(S_P\), established the universal range
\[
0\le S_P(X)\le\frac12,
\]
and related the constant to the James and modified von Neumann--Jordan constants, convexity, smoothness, uniform non-squareness, normal structure, and fixed-point properties. Their inspected preprint includes an \(\ell_p\) example but no regular-polygon or decagonal computation.

Published exact computations for the same invariant on other classical spaces do not imply (2). In particular, the exact \(\ell_p\) sequence-space formula concerns smooth coordinate balls rather than the decagonal facet geometry. Exact P-angle computations for the affine-regular hexagon, regular octagon, and regular dodecagon likewise use different support polygons and produce different constants.

Other exact results for the same affine-regular decagon concern unit-distance angle moduli, centered-triangle constants, weighted James profiles, and Birkhoff--James chord quantities. Those statements impose different admissibility conditions or optimize different functions of \(A\) and \(B\). None supplies the two weighted inequalities (1), which are the decisive input for (2).

## Limitations
The weighted chord envelope and exact P-angle value are proved here only for the affine-regular decagonal plane. No formula is asserted for all regular polygons.

The proof identifies one sharp adjacent-vertex orbit but does not classify every maximizing ordered pair.

The defining preprint's preliminary section states a dimension restriction, whereas the displayed P-angle supremum itself and its Euclidean-plane discussion are two-dimensional. The present result uses that displayed definition directly on the Minkowski plane; it does not claim that every theorem in the source paper transfers without checking dimensions.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent decagonal calculation could exist under another linearly equivalent normalization or only as a chord-pair inequality without the notation \(S_P\).

## References
1. Z. Yang and Y. Li, “New Geometric Constant Related to the P-angle Function in Banach Spaces,” arXiv:2208.11239, first public version 24 August 2022. Mathematics Subject Classification: 46B20.
