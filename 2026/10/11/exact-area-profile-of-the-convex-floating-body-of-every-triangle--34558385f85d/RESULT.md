# Exact area profile of the convex floating body of every triangle
## Finding
Let \(T\subset\mathbb R^2\) be a nondegenerate triangle with area \(A\). For \(x\in T\), let
\[
D_T(x)=
\inf_H
\frac{\operatorname{area}(T\cap H)}{A},
\]
where the infimum is over closed halfplanes \(H\) containing \(x\). Define the depth region
\[
T_\tau=\{x\in T:D_T(x)\ge\tau\}.
\tag{1}
\]
For uniform area measure, this is the convex floating body corresponding to cap area \(\tau A\).

If
\[
(\alpha,\beta,\gamma),
\qquad
\alpha+\beta+\gamma=1,
\qquad
\alpha,\beta,\gamma\ge0,
\]
are the barycentric coordinates of \(x\), then the published triangle halfspace-depth formula is equivalently
\[
D_T(x)
=
4\min\{\alpha\beta,\beta\gamma,\gamma\alpha\}.
\tag{2}
\]

Hence
\[
T_\tau
=
\left\{
(\alpha,\beta,\gamma):
\alpha\beta\ge\frac{\tau}{4},
\quad
\beta\gamma\ge\frac{\tau}{4},
\quad
\gamma\alpha\ge\frac{\tau}{4}
\right\}.
\tag{3}
\]
It follows that \(T_\tau\) is nonempty exactly for
\[
0\le\tau\le\frac49.
\]

For
\[
0<\tau<\frac49,
\qquad
s=\sqrt{1-2\tau},
\]
the exact normalized area is
\[
\boxed{
\frac{\operatorname{area}(T_\tau)}{A}
=
\frac32s-\frac12
+
\frac{3\tau}{2}
\log\!\left(
\frac{2(1-s)}{1+s}
\right).
}
\tag{4}
\]
The continuous endpoint values are
\[
\frac{\operatorname{area}(T_0)}A=1,
\qquad
\frac{\operatorname{area}(T_{4/9})}A=0,
\]
and
\[
T_{4/9}
\]
is the centroid singleton.

The exact wet-part asymptotic is
\[
\boxed{
\frac{\operatorname{area}(T\setminus T_\tau)}A
=
\frac{3\tau}{2}\log\frac1\tau
+
\frac{3\tau}{2}
-
\frac{3\tau^2}{4}
+
O(\tau^3).
}
\tag{5}
\]
In particular, the leading polygonal coefficient is exactly \(3/2\) for every triangle.

## Assumptions and scope
The construction in (1) is affine invariant. Therefore it is enough to work in barycentric coordinates on the standard simplex
\[
\alpha+\beta+\gamma=1,
\qquad
\alpha,\beta,\gamma\ge0.
\]

Rousseeuw and Ruts computed the halfspace depth of the uniform distribution on an equilateral triangle and showed that its maximal depth is
\[
\frac49
\]
at the centroid. Their formula, transported by affine invariance, gives (2).

The term “convex floating body” is used in the Schütt--Werner sense: the intersection of halfspaces whose boundary lines cut off a prescribed area. This is distinct from the older Dupin floating body, which need not exist for a triangle.

## Proof
Start with the equilateral triangle having vertices
\[
(-1,0),\qquad
(1,0),\qquad
(0,\sqrt3).
\]
Write a point as
\[
x=\alpha(-1,0)+\beta(1,0)+\gamma(0,\sqrt3).
\]
Thus
\[
x_1=\beta-\alpha,
\qquad
x_2=\sqrt3\,\gamma.
\tag{6}
\]

Rousseeuw--Ruts give, in one fundamental symmetry sector, the depth formula
\[
D_T(x)
=
\frac23
\left[
\sqrt3\,x_2(1-x_1)-x_2^2
\right].
\tag{7}
\]
Substitution of (6) gives
\[
D_T(x)=4\alpha\gamma
\]
in that sector. There \(\beta\) is the largest barycentric coordinate, so
\[
\alpha\gamma
=
\min\{\alpha\beta,\beta\gamma,\gamma\alpha\}.
\]
The six symmetry sectors give (2) everywhere. Affine invariance then gives (2) for every triangle.

Put
\[
q=\frac{\tau}{4}.
\]
By permutation symmetry, it is enough to integrate over the chamber
\[
\alpha\ge\beta\ge\gamma.
\tag{8}
\]
In this chamber the minimum in (2) is
\[
\beta\gamma,
\]
so the depth condition becomes
\[
\beta\gamma\ge q.
\tag{9}
\]
Since
\[
\alpha=1-\beta-\gamma,
\]
condition (8) is equivalent to
\[
\gamma\le\beta\le\frac{1-\gamma}{2}.
\tag{10}
\]

Let
\[
r=\frac{1-\sqrt{1-8q}}2
=
\frac{1-\sqrt{1-2\tau}}2.
\tag{11}
\]
The lower bound
\[
\frac q\gamma\le\frac{1-\gamma}{2}
\]
first becomes feasible at
\[
\gamma=r.
\]
Also the active lower bound for \(\beta\) changes from
\[
\frac q\gamma
\]
to
\[
\gamma
\]
when
\[
\gamma=\sqrt q.
\]
Therefore the area of the admissible set in the chamber, in the affine coordinates \((\beta,\gamma)\), equals
\[
I(q)
=
\int_r^{\sqrt q}
\left(
\frac{1-\gamma}{2}-\frac q\gamma
\right)d\gamma
+
\int_{\sqrt q}^{1/3}
\left(
\frac{1-\gamma}{2}-\gamma
\right)d\gamma.
\tag{12}
\]

The full barycentric simplex has coordinate area
\[
\frac12,
\]
and the six ordering chambers have equal area. Hence the normalized physical area is
\[
12I(q).
\tag{13}
\]
Direct evaluation of (12), followed by
\[
q=\frac{\tau}{4},
\qquad
s=\sqrt{1-2\tau},
\]
simplifies exactly to (4).

The nonempty range follows either from (3) and
\[
\min\{\alpha\beta,\beta\gamma,\gamma\alpha\}
\le\frac19,
\]
with equality only at
\[
\alpha=\beta=\gamma=\frac13,
\]
or from the endpoint \(r=1/3\) in (11). Thus the last nonempty region is the centroid at \(\tau=4/9\).

Finally, expansion of (4) at \(\tau=0\) gives
\[
\frac{\operatorname{area}(T_\tau)}A
=
1
+
\frac{3\tau}{2}\log\tau
-
\frac{3\tau}{2}
+
\frac{3\tau^2}{4}
+
O(\tau^3),
\]
which is equivalent to (5).

## Verification
The bundled `verify.py` checks the new calculation independently.

It first performs the two integrals in (12) symbolically and verifies exact agreement with (4). It then checks the endpoint
\[
\tau=\frac49
\]
and the series (5).

As a separate numerical test, it samples two million points uniformly in barycentric coordinates, evaluates
\[
4\min\{\alpha\beta,\beta\gamma,\gamma\alpha\},
\]
and compares empirical central-region areas with (4) at several levels. The deterministic acceptance tolerance is loose enough that the Monte Carlo calculation is only diagnostic; symbolic identities are the reproducibility certificate.

## Relationship to prior work
Schütt and Werner introduced the convex floating body and proved the characteristic polygonal small-cap behavior
\[
\operatorname{area}(K\setminus K_\delta)
\asymp
\delta\log\frac1\delta
\]
for polygons. Their later paper on almost polygonal bodies studies difference-volume rates in detail, but the inspected material does not give an all-level triangle formula.

Rousseeuw and Ruts computed the halfspace-depth function of the uniform distribution on a triangle, plotted its depth contours, and proved that the maximal depth is \(4/9\). Formula (2) is a barycentric rewriting of their published depth function, not a novelty claim.

Nagy, Schütt and Werner later made the equivalence between halfspace-depth central regions and convex floating bodies explicit. Their full preprint points back to the Rousseeuw--Ruts triangle formula and displays triangle central regions, but does not state the area of those regions as a function of the level.

The new content is the exact integration of the complete triangle depth region, yielding (4), together with the exact wet-part expansion (5).

Targeted searches under triangle floating bodies, uniform-triangle halfspace depth, Tukey-depth region area, barycentric pair products, and logarithmic area profiles did not locate an implication-equivalent published area formula.

## Limitations
The result is specific to triangles. It does not provide the corresponding all-level area profile for general polygons.

The published pointwise depth formula is used as a premise; the new contribution is the exact region-volume computation and its consequences.

The integration is elementary once the barycentric form (2) is recognized, so an unindexed calculation in statistical-depth notes remains a historical originality risk.

No claim is made about the Dupin floating body, which does not exist for triangles at positive levels.

## References
1. C. Schütt and E. Werner, *The convex floating body*, *Mathematica Scandinavica* 66 (1990), 275--290. DOI: 10.7146/math.scand.a-12311.
2. C. Schütt and E. Werner, *The convex floating body of almost polygonal bodies*, *Geometriae Dedicata* 44 (1992), 169--188. DOI: 10.1007/BF00182948.
3. P. J. Rousseeuw and I. Ruts, *The depth function of a population distribution*, *Metrika* 49 (1999), 213--244. DOI: 10.1007/PL00020903.
4. S. Nagy, C. Schütt and E. M. Werner, *Halfspace depth and floating body*, *Statistics Surveys* 13 (2019), 52--118. DOI: 10.1214/19-SS123.
5. A. Stancu, *The Floating Body Problem*, *Bulletin of the London Mathematical Society* 38 (2006), 839--846. DOI: 10.1112/S0024609306018728.
