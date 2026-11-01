# The sharp John-normalized polar-area sum for symmetric tangential hexagons

## Finding
Let \(K\) be a genuine (six nonredundant sides), centrally symmetric convex hexagon in the Euclidean plane. Assume that **every side is tangent to its John ellipse** \(E\), the ellipse of greatest area contained in \(K\). Write \(K^\circ\) for the polar about the center of symmetry and \(E^\circ\) for the polar ellipse. Then
\[
\boxed{\frac{|K|}{|E|}+\frac{|K^\circ|}{|E^\circ|}\le\frac{5\sqrt 2-1}{\pi}}.
\]
This is strictly sharper than the general centrally symmetric planar inequality with right-hand side \(2\). Equality holds exactly for affine images of a unit-circle-tangential hexagon cut from a square by two opposite diagonal truncations, with canonical description
\[
K_0=\{(x,y)\in\mathbb R^2:|x|\le1,\ |y|\le1,\ |x-y|\le\sqrt2\}.
\]
For this shape \(|K_0|=4\sqrt2-2\), \(|K_0^\circ|=1+\sqrt2\), and the John disk is \(B^2\). Its sum is \(5\sqrt2-1\), exceeding the corresponding regular tangential hexagon value \(7\sqrt3/2\). The **complete normalized range** among genuine tangential John hexagons is
\[
\left(\frac6\pi,\frac{5\sqrt2-1}\pi\right].
\]
The lower endpoint is approached by genuine hexagons collapsing into a square but is not attained.

The sharp upper equality has a mixed first/second-order stability. In a neighborhood of the maximizing unordered normal-gap triple, write
\[
\theta_1=\frac\pi2-\eta,\qquad
\theta_2=\frac\pi4+\frac\eta2+\delta,\qquad
\theta_3=\frac\pi4+\frac\eta2-\delta,
\]
with \(\eta\ge0\) and the angles admissible. If \(S=|K|+|K^\circ|\) after disk normalization, then
\[
(5\sqrt2-1)-S=\left(\frac{3\sqrt2}{2}-2\right)\eta+
\left(8-\frac{11\sqrt2}{2}\right)\delta^2
+O(\eta^2+\eta\delta^2+\delta^4).
\]
Both displayed coefficients are strictly positive.

## Assumptions and scope
Polarity is \(K^\circ=\{y:\langle x,y\rangle\le1\text{ for all }x\in K\}\). Ellipse normalization is affine-invariant: under a nonsingular linear transformation, the two individual ratios \(|K|/|E|\) and \(|K^\circ|/|E^\circ|\) are unchanged. Normalize the centered John ellipse to the unit disk \(B^2\). All six sides are tangent to this disk and are distinct.

The three unoriented outward unit normal directions have angles \(\phi_1,\phi_2,\phi_3\) increasing through a half-turn. Define their cyclic gaps \(\theta_1,\theta_2,\theta_3\), so \(\theta_i>0\) and \(\sum\theta_i=\pi\). By the symmetric John contact characterization, the unit disk is a John ellipse exactly when
\[
\theta_1,\theta_2,\theta_3\le\frac\pi2.
\]
Indeed, the John contact condition is that the origin belongs to the convex hull of the three doubled-angle vectors \(e^{2i\phi_j}\). For three points on the unit circle this is equivalent to their three doubled consecutive gaps being at most \(\pi\). Equality of a gap with \(\pi/2\) is allowed: the two perpendicular normal pairs alone then provide a John decomposition. Thus the entire class is represented by the open-in-coordinate, closed-above triangle of admissible gaps.

## Proof
**1. Direct geometric area formulas.** The polar is the inscribed hexagon with the six unit normals as its vertices. The shoelace formula, or decomposition into six triangles, gives
\[
|K^\circ|=\sum_{i=1}^3\sin\theta_i.
\]
Each pair of adjacent tangent lines to the disk forms a polygonal vertex, and summing facet trapezoids gives
\[
|K|=2\sum_{i=1}^3\tan(\theta_i/2).
\]
Consequently, with \(f(t)=\tan(t/2)+\tfrac12\sin t\),
\[
S(\theta_1,\theta_2,\theta_3)=2\sum_{i=1}^3f(\theta_i),\quad
0<\theta_i\le\pi/2,\quad\sum\theta_i=\pi.
\]
This continuous function extends to the compact closed triangle with \(0\le\theta_i\le\pi/2\).

**2. Every boundary case.** When one gap is zero, the other two are \(\pi/2\), giving \(S=6\). Otherwise on the boundary one gap is \(\pi/2\); write the remaining two as \(x+y=\pi/2\), \(x,y\ge0\). Put \(p=\tan(x/2)\), \(q=\tan(y/2)\), \(z=p+q\). The tangent addition law yields \(pq=1-z\). The arithmetic-geometric mean inequality gives
\[
2(\sqrt2-1)\le z\le1.
\]
A direct trigonometric simplification yields
\[
f(x)+f(y)=z+\frac1z-\frac12.
\]
Because this decreases strictly with \(z\) on \((0,1)\), the maximum occurs exactly at \(p=q\), hence \(x=y=\pi/4\), where \(S=5\sqrt2-1\). All equality configurations have unordered gaps \((\pi/2,\pi/4,\pi/4)\).

**3. No larger interior maximum.** The derivatives are
\[
f'(t)=\frac1{1+\cos t}+\frac12\cos t,\qquad
f''(t)=\sin t\left(\frac1{(1+\cos t)^2}-\frac12\right).
\]
At an interior constrained stationary point the three first derivatives agree. For two distinct angles \(a,b\) in \((0,\pi/2)\), the equation \(f'(a)=f'(b)\) is equivalent to
\[
(1+\cos a)(1+\cos b)=2.
\]
Thus three distinct stationary angles are impossible. The equal-angle point has gaps \((\pi/3,\pi/3,\pi/3)\) and \(S=7\sqrt3/2<5\sqrt2-1\). In every remaining stationary point two angles equal \(a\), the third is \(b=\pi-2a\). Writing \(v=\cos a\), the preceding equation becomes \((1-v)(1+v)^2=1\), hence \(v=(\sqrt5-1)/2\). Along the admissible perturbation \((a+t,a+t,b-2t)\), the second derivative of the sum of the three \(f\)'s at zero is
\[
2f''(a)+4f''(b)=2\sqrt v\left(\frac32-2v\right)>0.
\]
So these points are not local maxima. Compactness and the boundary calculation prove the sharp global upper bound and its full equality class.

**4. Geometry and lower endpoint.** The normal triple \((0,\pi/2,3\pi/4)\) yields exactly \(K_0\). The perpendicular pairs of contact points ensure \(B^2\) is its John disk. All permutations of the maximizing gap pattern differ only by a rigid motion and reflection, so undoing normalization gives the stated affine-rigid equality class. The established area-sum inequality of Aczél–Fuchs/Florian gives \(S\ge6\), with equality among circle-inscribed and circumscribed polar polygons only for a square. No genuine tangential hexagon is a square, so \(S>6\). Along the continuous admissible path \((\pi/2,\pi/2-t,t)\), \(0<t\le\pi/4\), the sum runs continuously from the limiting value \(6\) to the upper value \(5\sqrt2-1\). Thus the full range is exactly the claimed interval.

**5. Local sharpness orders.** Taylor expansion about \((\pi/2,\pi/4,\pi/4)\), using \(f'(\pi/2)=1\), \(f'(\pi/4)=2-3\sqrt2/4\) and \(f''(\pi/4)=-4+11\sqrt2/4\), gives the stated positive linear and quadratic coefficients with the displayed remainder. The normal gap upper cap explains the first-order term; balancing the unconstrained two gaps produces the quadratic term.

## Verification
The standalone script `verify_john_hexagon.py` is included in this package. Running `python3 verify_john_hexagon.py` with Python 3 and SymPy performs 104,412 deterministic consistency checks. These include exact symbolic derivatives and equality values, an independent shoelace computation of the original and polar hexagon areas for 25,000 pseudorandom admissible normal triples, John contact decompositions, boundary identities, and local two-scale expansion comparisons. The script reports `PASS: 104412 independent symbolic, deterministic geometric, and boundary checks`. The proof above—not finite testing—establishes the statements for all admissible real angles.

## Relationship to prior work
K. J. Böröczky and E. Makai's February 16, 2026 preprint *A strengthening of the Blaschke–Santaló inequality for o-symmetric planar convex bodies* (arXiv:2602.14750v1, Theorem 1.1 and Corollary 1.2) proves the universal normalized upper bound \(2\) and supplies the symmetric John contact framework. Its general bound is weaker than the constant above; the inspected paper does not contain the sharp tangent-hexagon maximum or equality classification. A. Florian's 1995 *On the Area Sum of a Convex Polygon and its Polar Reciprocal*, including its proof and corollary, concerns the opposite **lower** bound \(6\); this lower result is used rather than reclaimed. The 1950 Aczél–Fuchs polygon inequality is the earlier version of that lower estimate.

Some published geometric results analyze inverse width distributions of tangential symmetric polygons or enclosures of symmetric hexagons. Their different functionals do not imply this polar **area sum** sharp maximum. These comparisons distinguish statement implications, not just titles. Searches cannot rule out every older equivalent formulation; historical priority remains provisional.

## Limitations
The theorem assumes both central symmetry and tangency of **every** one of the six sides to the John ellipse. It does not optimize arbitrary centrally symmetric hexagons with only some John contacts, nonsymmetric hexagons, or higher-dimensional polyhedra. This is a mathematical proof and self-review, not an independent audit or a definitive historical-priority certification.

## References
1. K. J. Böröczky and E. Makai, *A strengthening of the Blaschke–Santaló inequality for o-symmetric planar convex bodies*, arXiv:2602.14750v1 (first posted February 16, 2026), https://arxiv.org/abs/2602.14750 .
2. A. Florian, *On the Area Sum of a Convex Polygon and its Polar Reciprocal*, Mathematica Pannonica **6**(1) (1995), 77–84, https://mathematica-pannonica.ttk.pte.hu/articles/mp06-1/mp06-1-077-084.pdf .
3. J. Aczél and L. Fuchs, *A minimum-problem on areas of inscribed and circumscribed polygons of a circle*, Compositio Mathematica **8** (1950), 61–67 (cited by Florian).