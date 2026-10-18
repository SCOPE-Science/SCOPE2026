# Two universal endpoint laws for pointwise coverage by side-stratified parallelogram hulls

## Finding

Let \(P\) be any nondegenerate Euclidean parallelogram. Independently select one point uniformly in arclength from each of its four complete sides, and let \(Q\) be their convex hull. For each \(z\in P\), define its *coverage depth* by
\[
D_P(z)=\Pr\{z\in Q\}.
\]
Write \(z=v_0+s\,a+t\,b\) uniquely with \(0\le s,t\le1\), where \(v_0,v_0+a,v_0+a+b,v_0+b\) are the consecutive vertices of \(P\). The depth depends only on \((s,t)\), independently of the parallelogram's side lengths and angle. Under reflection about the coordinate midlines and exchange of coordinates, every \((s,t)\) reduces to \(0\le x\le y\le\tfrac12\). On this fundamental wedge the *complete* depth formula is
\[
D_P(v_0+xa+yb)=x\left[2+\log\frac{1-x}{x}+(2y-1)\log\frac{1-y}{y}\right],\qquad 0<x\le y\le\tfrac12,
\]
with continuous boundary values. The depth vanishes on the host boundary and equals one **only** at the center \(v_0+(a+b)/2\).

Now take \(U\) independently, uniformly by planar area inside \(P\), and set \(Z=D_P(U)\). Then the distribution of this pointwise coverage depth is universal, and has **two different sharp endpoint regimes**:
\[
\boxed{\Pr\{Z\le\varepsilon\}\sim\frac{4\varepsilon}{\log(1/\varepsilon)}}
\qquad\text{and}\qquad
\boxed{\Pr\{Z\ge1-\varepsilon\}\sim\frac\pi4\,\varepsilon}
\quad(\varepsilon\downarrow0).
\]
The second law follows from the uniform center expansion in affine coordinates
\[
1-D_P\left(v_0+(\tfrac12+u)a+(\tfrac12+v)b\right)
=4(u^2+v^2)+O\bigl((|u|+|v|)^3\bigr).
\]
Both asymptotic constants are independent of the Euclidean shape of \(P\); the upper-depth law is circular in the *affine* coordinates, not necessarily in Euclidean distance.

## Assumptions and scope

The host is a fixed, full-dimensional parallelogram, and *exactly four* points are sampled, independently, with one uniform-arclength point on each prescribed side. Sampling four independent points from the pooled perimeter is a different distribution. The point \(U\) defines the area-weighted distribution of the deterministic function \(D_P\); it is not one of the four sampled boundary points. Limits in \(\varepsilon\) are taken through positive real values. The result includes all parallelogram angles and aspect ratios without a uniform-in-shape assertion for other models.

## Proof

**1. Affine normalization and dissection.** The nonsingular affine map \((s,t)\mapsto v_0+sa+tb\) carries unit-square sides to the four sides of \(P\). Constant arclength speed on each side maps uniform arclength precisely to the uniform parameter on that side. Containment is affine-invariant, and normalized area is preserved. Thus work with \([0,1]^2\). Almost surely the four side samples, in cyclic order, form a convex quadrilateral. Its complement in the square consists of four corner triangles with disjoint interiors. The probability a fixed interior point is on any random triangle boundary is zero; the identities extend continuously to host boundaries.

**2. One corner's probability.** For \(a,b\ge0\), set \(F(a,b)\) to be the probability that \((a,b)\) belongs to the corner triangle with vertices \((0,0),(V,0),(0,W)\), where \(V,W\) are independent uniform variables on \([0,1]\). For \(a,b>0\) with \(a+b<1\), the condition is \(a/V+b/W\le1\), whence
\[
F(a,b)=\int_{b/(1-a)}^1\left(1-\frac{aw}{w-b}\right)dw
=1-a-b-ab\log\frac{(1-a)(1-b)}{ab}.
\]
For \(a+b\ge1\), \(F(a,b)=0\); all other values are obtained by continuity. The four complementary corner triangles give the exact all-point identity
\[
D(s,t)=1-F(s,t)-F(1-s,t)-F(1-s,1-t)-F(s,1-t).
\]

**3. Full depth and extremum.** The unit square's dihedral symmetry reduces to \(0\le x\le y\le1/2\). On its strict interior, only \(F(x,y)\) and \(F(x,1-y)\) are nonzero. Substituting the preceding integral yields the stated formula. At \(x=0\) it equals zero, including the endpoints by continuity. For \(0<x\le y\le1/2\), differentiation with \(y\) fixed gives
\[
\frac{\partial D}{\partial x}=2-\frac1{1-x}+\log\frac{1-x}{x}+(2y-1)\log\frac{1-y}{y}>0
\]
except at the center endpoint, since \(2-1/(1-x)\ge0\) and the combined logarithms are at least \(\log((1-x)y/(x(1-y)))\ge0\). Also, with \(x\) fixed,
\[
\frac{\partial D}{\partial y}
=x\left[2\log\frac{1-y}{y}+\frac{1-2y}{y(1-y)}\right]>0
\quad(0<y<1/2).
\]
Thus the unique maximizing point is \((1/2,1/2)\), where the exact formula gives depth one. The boundary has depth zero.

**4. Near-certain coverage.** In the fundamental wedge put \(x=1/2-h\), \(y=1/2-k\), with \(0\le k\le h\). Taylor expansion of the explicit formula gives
\[
D(x,y)=1-4(h^2+k^2)+O((h+k)^3)
\quad(h+k\downarrow0).
\]
By the eight square symmetries this expansion holds uniformly in every direction about the center. Continuity and the unique maximum ensure that sufficiently high superlevel sets lie entirely in an arbitrarily small center neighborhood. Their affine-coordinate areas are sandwiched between disk areas with radii \((\sqrt\varepsilon/2)(1+O(\sqrt\varepsilon))\). Therefore the probability for area-uniform \(U\) of \(D(U)\ge1-\varepsilon\) is \(\pi\varepsilon/4+O(\varepsilon^{3/2})\).

**5. Low-depth boundary layer.** On the wedge, an equivalent exact expression is
\[
D(x,y)=x\left[2+\log\frac yx+\log\frac{1-x}{1-y}+2y\log\frac{1-y}{y}\right]
\qquad(0<x\le y\le1/2).
\]
Every term after the \(2\) is nonnegative, so \(D(x,y)\ge x(2+\log(y/x))\ge2x\). For each \(y\in(0,1/2]\) and small \(\varepsilon>0\), let \(w_\varepsilon(y)\in[0,y]\) be the length of the interval of \(x\in[0,y]\) satisfying \(D(x,y)\le\varepsilon\). Strict monotonicity from Step 3 makes that set an interval. For every fixed \(\eta\in(0,1/2)\), uniformly in \(\eta\le y\le1/2\),
\[
w_\varepsilon(y)=\frac\varepsilon{\log(1/\varepsilon)}(1+o(1)),
\]
because \(D(x,y)=x(\log(1/x)+O_\eta(1))\) as \(x\downarrow0\).

To control the corner \(y\downarrow0\), split at \(y=\sqrt\varepsilon\). The inequality \(D\ge2x\) bounds the portion \(0\le y\le\sqrt\varepsilon\) by \(O(\varepsilon^{3/2})\) in area. For \(\sqrt\varepsilon\le y\le\eta\), a point of depth at most \(\varepsilon\) has \(x\le\varepsilon/2\) and hence \(\log(y/x)\ge\tfrac12\log(1/\varepsilon)+\log2\). Thus \(w_\varepsilon(y)\le2\varepsilon/\log(1/\varepsilon)\) for small \(\varepsilon\), and this strip contributes at most \(2\eta\varepsilon/\log(1/\varepsilon)\). Since eight congruent wedges partition the square up to null sets,
\[
\Pr\{D(U)\le\varepsilon\}=8\int_0^{1/2}w_\varepsilon(y)\,dy.
\]
First let \(\varepsilon\downarrow0\) and then \(\eta\downarrow0\) to obtain the exact coefficient \(8(1/2)=4\). This completes both endpoint laws.

## Verification

The accompanying standard-library `checker.py` evaluates the corner formula and reduced-wedge expression on 3000 seeded parameter choices, checks direct convex-hull containment of 330000 independently sampled four-side configurations (also after a nonorthogonal affine transformation), verifies boundary/center values, and numerically integrates both endpoint depth-level distributions. Reproduction: run `python3 checker.py` from this package. Numerical convergence and Monte Carlo agreement are supplementary finite tests; Steps 1–5 establish the universal statements analytically.

A second consistency check is the known expected area fraction \(\int_P D_P(z)\,dz/\operatorname{area}(P)=1/2\): each of the four discarded corner triangles has expected normalized area \((1/2)\mathbb E[VW]=1/8\), so together they discard half the host area on average. This mean by itself cannot determine either endpoint depth law.

## Relationship to prior work

Maesumi (arXiv:1804.11007, initially posted 2018-04-30) studies the **area distribution** of a triangle formed by one uniform sample on each of three sides of a host triangle. Reitzner, Schütt, and Werner (arXiv:1911.05917, initially posted 2019-11-14) investigate expectations and asymptotic face counts for independent, pooled-boundary samples of convex polytopes. Their stated models or observables do not give the present four-side pointwise inclusion-depth distribution. The corner integral in Step 2 is elementary and also useful in triangular sampling; its reuse is not an originality claim. The distinct results here are the full four-side depth field, the unique certain-coverage center, and, particularly, the two quantified **area-of-depth-level-set** endpoint laws with different rates. Originality remains subject to unindexed literature and independent checking.

## Limitations

No result is claimed for non-parallelogram quadrilaterals, four iid pooled-perimeter points, other sampling densities, or higher-dimensional boxes. The rates concern the distribution of **conditional coverage depth** at an independent area-uniform point, not the tail of the random inscribed quadrilateral's area. The high-depth quadratic expression is in affine coordinates; it does not claim a Euclidean circular contour for a skew parallelogram. Numerical checks are finite, not a proof of the limiting constants.

## References

1. A. Maesumi, *Triangle Inscribed-Triangle Picking*, arXiv:1804.11007 (first posted 2018-04-30), https://arxiv.org/abs/1804.11007.
2. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first posted 2019-11-14), https://arxiv.org/abs/1911.05917.
