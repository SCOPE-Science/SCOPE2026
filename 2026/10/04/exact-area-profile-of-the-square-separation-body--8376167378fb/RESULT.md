# Exact area profile of the square separation body

## Finding

Let
\[
Q=[-1,1]^2.
\]
For \(\delta\ge0\), let \(Q[\delta]\) be the isotropic separation body in Schneider's normalization:
\[
Q[\delta]
=
\left\{
x\in\mathbb R^2:
W(\operatorname{conv}(Q\cup\{x\}))-W(Q)\le\delta
\right\}.
\]

Put
\[
c=\pi\delta,\qquad
a=1+\frac c2,\qquad
b=\sqrt{a^2-1},\qquad
\beta=\sqrt{(a+1)^2-2}.
\]
Then
\[
\boxed{
\operatorname{Area}(Q[\delta])
=
4
+
4ab\arcsin\!\left(\frac1a\right)
+
4(a+1)\beta
\arcsin\!\left(
\frac{b^2}{\sqrt2\,a(a+1)}
\right)
}.
\]

The boundary is also explicit. In the right side strip
\[
x\ge1,\qquad |y|\le1,
\]
the outer arc satisfies
\[
\frac{(x-1)^2}{b^2}+\frac{y^2}{a^2}=1.
\]
In the northeast corner, with
\[
p=\frac{x-y}{\sqrt2},\qquad
q=\frac{x+y}{\sqrt2},
\]
the arc satisfies
\[
\frac{p^2}{(a+1)^2}+\frac{q^2}{\beta^2}=1,
\qquad
|p|\le\frac{b^2}{\sqrt2\,a}.
\]
The other seven arcs follow by square symmetry.

As \(\delta\downarrow0\),
\[
\operatorname{Area}(Q[\delta])-4
=
2\pi^{3/2}\delta^{1/2}
+
\frac{5\pi^{5/2}}4\delta^{3/2}
-
\frac{2\pi^2}{3}\delta^2
+
O(\delta^{5/2}).
\]

Two boundary radii follow immediately:
\[
h_{Q[\delta]}(e_1)
=
1+\sqrt{\pi\delta+\frac{\pi^2\delta^2}{4}},
\]
and the northeast diagonal boundary point is
\[
(t,t),\qquad
t=
\sqrt{1+\pi\delta+\frac{\pi^2\delta^2}{8}}.
\]

## Assumptions and scope

The hyperplane measure is the isotropic motion-invariant measure in Schneider's separation-body construction. In the plane, mean width equals perimeter divided by \(\pi\). Hence, writing
\[
K^x=\operatorname{conv}(K\cup\{x\}),
\]
Schneider's planar polygon formula is
\[
m(K,x)
=
\frac1\pi\left[L(K^x)-L(K)\right].
\]
Therefore
\[
x\in Q[\delta]
\quad\Longleftrightarrow\quad
L(Q^x)-8\le c,\qquad c=\pi\delta.
\]

The formula is valid for all \(\delta\ge0\), with \(\delta=0\) understood by continuity.

## Proof

The four edge lines of \(Q\) partition the exterior into four side strips and four corner regions. In each region the two tangent vertices seen from the exterior point are fixed.

In the right strip
\[
x\ge1,\qquad |y|\le1,
\]
the old side from \((1,-1)\) to \((1,1)\) has length \(2\). For a boundary point \(z=(x,y)\), replacing that side by the two segments from \(z\) gives
\[
\lVert z-(1,-1)\rVert+\lVert z-(1,1)\rVert
=
2+c
=
2a.
\]
Thus the boundary is an ellipse with focal half-distance \(1\), semimajor axis \(a\), and semiminor axis
\[
b=\sqrt{a^2-1}.
\]
Its outer branch is
\[
x
=
1+
b\sqrt{1-\frac{y^2}{a^2}}.
\]
Hence the added area in one side strip is
\[
S
=
\int_{-1}^{1}
b\sqrt{1-\frac{y^2}{a^2}}\,\mathrm dy
=
\frac{b^2}{a}
+
ab\arcsin\!\left(\frac1a\right).
\]

In the northeast corner, the tangent vertices are \((1,-1)\) and \((-1,1)\). The square boundary path between them through \((1,1)\) has length \(4\). Therefore the boundary condition is
\[
\lVert z-(1,-1)\rVert+\lVert z-(-1,1)\rVert
=
4+c
=
2(a+1).
\]
Under the rotation
\[
p=\frac{x-y}{\sqrt2},\qquad q=\frac{x+y}{\sqrt2},
\]
the foci are \((\sqrt2,0)\) and \((-\sqrt2,0)\). The ellipse therefore has semimajor axis \(a+1\) and semiminor axis
\[
\beta=\sqrt{(a+1)^2-2}.
\]

The side and corner arcs meet on \(y=1\). The side equation gives
\[
x-1=\frac{b^2}{a}.
\]
Set
\[
d=\frac{b^2}{a},\qquad p_0=\frac d{\sqrt2}.
\]
The corner arc has \(|p|\le p_0\), while the square corner boundary in rotated coordinates is
\[
q=\sqrt2+|p|.
\]
Thus one corner contributes
\[
C
=
\int_{-p_0}^{p_0}
\left[
\beta\sqrt{1-\frac{p^2}{(a+1)^2}}
-
\sqrt2-|p|
\right]\mathrm dp.
\]
Evaluating the ellipse integral and using the endpoint identity gives
\[
C
=
(a+1)\beta
\arcsin\!\left(
\frac{b^2}{\sqrt2\,a(a+1)}
\right)
-
\frac{b^2}{a}.
\]

The exterior is the disjoint union, up to boundaries, of four congruent side strips and four congruent corners. Therefore
\[
\operatorname{Area}(Q[\delta])
=
4+4S+4C.
\]
The terms \(b^2/a\) cancel, giving the claimed formula.

For the small-parameter expansion, set \(c=s^2=\pi\delta\) in the closed form. Direct expansion gives
\[
4+2\pi s+\frac{5\pi}{4}s^3-\frac23s^4+O(s^5),
\]
which is the stated expansion.

The axis radius is obtained from \(y=0\) in the side ellipse. On the northeast diagonal, \(p=0\), so \(q=\beta\) and \(x=y=\beta/\sqrt2\).

## Verification

The accompanying `verify.py` reconstructs the convex hull of the square and one exterior point directly and computes its perimeter. It checks that both ellipse families have exactly the prescribed perimeter excess for several parameter values and dense samples along each arc.

It separately verifies that the side and corner equations have the same transition point.

For an independent area check, the script reconstructs the radial function of the perimeter sublevel set by bisection in \(2048\) directions and numerically integrates
\[
\frac12\int_0^{2\pi}\rho(\theta)^2\,\mathrm d\theta.
\]
The numerical areas agree with the closed formula to less than \(2\times10^{-6}\) at several parameter values.

The small-\(\delta\) expansion is also checked at a sequence of shrinking positive parameters.

The replay output is:

`VERIFY_OK square separation-body area profile`

The finite computations are consistency checks only. The all-parameter result is proved by the chamber decomposition and exact ellipse integrations above.

## Relationship to prior work

Schneider introduced separation bodies for translation-invariant hyperplane measures and showed that, in the isotropic planar polygon case,
\[
m(K,x)
=
\frac1\pi\left[L(K^x)-L(K)\right].
\]
He also observed that, inside each chamber cut out by the edge lines of a polygon, the boundary of the separation body is an ellipse arc.

The earlier work of Böröczky and Schneider already used the isotropic mean-width sublevel body
\[
K[t]
=
\left\{
x:
W(\operatorname{conv}(K\cup\{x\}))-W(K)\le t
\right\}
\]
and proved its convexity for random circumscribed-polytope estimates. Its full text does not specialize the construction to the square or give an ellipse/area profile.

The present result carries the local polygon observation through globally for the square, identifies the two inequivalent ellipse families and their transition points, and integrates them to a single closed area formula valid for every parameter.

Schneider's volume comparison theorem makes this profile directly usable in the associated Poisson-halfspace model: the area increment of \(Q[1/n]\) is an explicit lower benchmark for the expected excess area.

Targeted searches for square separation bodies, mean-width sublevel bodies of a square, square ellipse-arc profiles, and exact area formulas did not locate an equivalent statement.

## Limitations

The result concerns the isotropic planar separation body of the square. It does not give a closed formula for arbitrary polygons, whose edge-line arrangements can have many inequivalent chambers.

The parameter uses Schneider's mean-width normalization; alternative normalizations rescale \(\delta\).

The literature search found no equivalent square formula, but an unindexed computation in older stochastic-geometry literature remains a residual originality risk.

The stochastic consequence is a lower benchmark from Schneider's comparison theorem. No exact random-cell expectation or matching new upper bound is claimed.

## References

R. Schneider, “Separation bodies: a conceptual dual to floating bodies,” arXiv:1910.12670, first submitted 2019-10-28; Monatshefte für Mathematik 193 (2020), 611–622, DOI 10.1007/s00605-020-01443-2.

K. J. Böröczky and R. Schneider, “The mean width of circumscribed random polytopes,” arXiv:0901.3343, first submitted 2009-01-21; Canadian Mathematical Bulletin 53 (2010), 614–628, DOI 10.4153/CMB-2010-067-5.
