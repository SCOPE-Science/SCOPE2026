# Sharp Schur ordering of triangular central sections of equifacial tetrahedra

## Finding

Consider any nondegenerate equifacial Euclidean tetrahedron, represented up to a rigid motion by the vertices
\[
v_1=(a,b,c),\quad v_2=(a,-b,-c),\quad
v_3=(-a,b,-c),\quad v_4=(-a,-b,c),
\qquad a,b,c>0.
\]
Every equifacial tetrahedron has three equal opposite-edge pairs. For its centered vertices \(w_1,\ldots,w_4\), set \(A=(w_1+w_2)/2\), \(B=(w_1+w_3)/2\), and \(C=(w_1+w_4)/2\). The equalities of opposite edge lengths give \(A\cdot B=B\cdot C=C\cdot A=0\); for example, \(16A\cdot B=\|w_1-w_4\|^2-\|w_2-w_3\|^2=0\). These three nonzero orthogonal vectors yield exactly the displayed positive-axis \(a,b,c\) representation. Its centroid is the origin. Choose an unoriented plane through the centroid with Haar-uniform normal. Almost surely its section is a triangle or a quadrilateral. Put
\[
p_1=\frac{a^2}{a^2+b^2+c^2},\quad
p_2=\frac{b^2}{a^2+b^2+c^2},\quad
p_3=\frac{c^2}{a^2+b^2+c^2}.
\]
The exact probability of a triangular section is
\[
\boxed{\mathcal T(p_1,p_2,p_3)=\frac4\pi\sum_{i=1}^3\arcsin\sqrt{p_i}-2.}
\]
This function is *strictly Schur-concave* on the open probability simplex: any nontrivial pairwise balancing of the squared axis proportions strictly increases the triangular-section probability. In particular,
\[
\boxed{0<\mathcal T(p_1,p_2,p_3)\le\frac{12}{\pi}\arcsin\frac1{\sqrt3}-2
=0.350959312183643\ldots.}
\]
Equality is possible only for the regular tetrahedron, namely \(a=b=c\). The lower endpoint is not attained by a nondegenerate tetrahedron, but every positive value below the upper endpoint occurs. The quadrilateral probability is exactly \(1-\mathcal T\).

Two additional shape-sensitive statements hold. If \(p_i=1/3+\varepsilon_i\) and \(\sum_i\varepsilon_i=0\), then
\[
\mathcal T_{\max}-\mathcal T(p)=
\frac{9\sqrt2}{8\pi}\sum_{i=1}^3\varepsilon_i^2
+O(\|\varepsilon\|^3).
\]
If \(p_3=\epsilon\downarrow0\) while \(p_1\) remains in a compact subinterval of \((0,1)\) and \(p_2=1-p_1-\epsilon\), then
\[
\boxed{\mathcal T(p)=\frac4\pi\sqrt\epsilon+O(\epsilon),}
\]
uniformly on those compact subintervals. Thus the first-order rate of vanishing on every nonvertex edge of the shape simplex is independent of the limiting ratio of the other two axes.

Equivalently, for three independent standard real Gaussian variables \(G_1,G_2,G_3\), the displayed probability equals the probability that the positive lengths \(a|G_1|,b|G_2|,c|G_3|\) satisfy all three strict triangle inequalities. This gives a sharp probability optimizer for *heteroscedastic half-normal triangle formation*.

## Assumptions and scope

All dimensions are Euclidean. The tetrahedron is required to be full-dimensional: \(a,b,c>0\). A plane is sampled by drawing its unit normal uniformly from \(S^2\), identifying antipodal normals; its offset is fixed to zero, the centroid. The sample distribution is **not** random affine planes conditioned on intersection and is **not** the law of planar orthogonal shadows. Probability-one genericity excludes normals orthogonal to a tetrahedron vertex; such orientations form a finite union of great circles. Majorization is the standard ordering on vectors with equal coordinate sum, and strictness means every genuine balancing of unequal components in the open simplex. Error terms in the stability assertions are with respect to the indicated limits.

## Proof

**1. Vertex counts from edge crossings.** Because the origin is a strict interior point of the tetrahedron, a generic plane through it intersects exactly three or four edges, producing a triangle or quadrilateral. Let \(N\in\{3,4\}\) denote that number. For two nonzero vectors \(v,w\) making angle \(\theta\in(0,\pi)\), the random signs of \(U\cdot v\) and \(U\cdot w\) differ with probability \(\theta/\pi\): the exceptional normals occupy two opposite spherical lunes, whose combined area is \(4\theta\) on the sphere of area \(4\pi\). This is an exact spherical-area identity. Therefore
\[
\mathbb E N=\frac1\pi\sum_{1\le i<j\le4}\angle(v_i,v_j).
\]
Since \(N=3\) precisely for triangular sections, \(\Pr(N=3)=4-\mathbb E N\).

**2. Explicit formula.** All four vertex vectors have squared norm \(s=a^2+b^2+c^2\). Among their six unordered pairwise scalar products the values \(2a^2-s\), \(2b^2-s\), and \(2c^2-s\) each occur exactly twice. Hence
\[
\mathbb EN=\frac2\pi\sum_{i=1}^3\arccos(2p_i-1).
\]
Using \(\arccos(2t-1)=2\arccos\sqrt t=\pi-2\arcsin\sqrt t\) for \(0<t<1\) yields the claimed probability formula. The Gaussian representation of a uniform sphere normal is \(U=G/\|G\|\); multiplying the four vertex projections by \(\|G\|\) leaves their signs unchanged. Their four signs are those of \(A+B+C,A-B-C,-A+B-C,-A-B+C\), where \(A=aG_1\), \(B=bG_2\), \(C=cG_3\). Flipping the sign of a Gaussian coordinate merely permutes these four expressions or changes all four signs, leaving the one-versus-three property invariant. For nonnegative \(A,B,C\), the first expression is positive and the other three are negative exactly when each positive length is less than the sum of the other two; otherwise one of the remaining expressions is positive and the pattern is two-versus-two. This proves the strict triangle-inequality equivalence. This proves the alternative probability interpretation.

**3. Strict majorization.** Let \(f(t)=\arcsin\sqrt t\) for \(0<t<1\); then
\[
f'(t)=\frac1{2\sqrt{t(1-t)}}.
\]
If \(x>y>0\) are two components of an interior three-part probability vector, its third component \(z=1-x-y\) is strictly positive and
\[
x(1-x)-y(1-y)=(x-y)z>0.
\]
Consequently \(f'(x)<f'(y)\), *including when \(x>1/2\)*, despite \(f\) not being globally concave on \((0,1)\). Transferring any amount strictly between zero and half of \(x-y\) from \(x\) to \(y\) strictly increases \(f(x)+f(y)\), since its derivative along the transfer equals \(f'(y+t)-f'(x-t)>0\) until equality. Finite sequences of such transfers characterize majorization on the three-part simplex, so \(\mathcal T\) is strictly Schur-concave. All interior shapes majorize \((1/3,1/3,1/3)\); thus the regular tetrahedron is the unique maximizer, up to similarity. The event of strict Gaussian triangle inequalities has positive probability for all positive axes, giving strict positivity. The formula extends continuously to the closed simplex and vanishes on its boundary by \(f(t)+f(1-t)=\pi/2\) and \(f(0)=0\). Continuity along a path from the regular point to a boundary point gives every intermediate probability.

**4. Stability and degeneration.** Differentiation gives
\[
f''(t)=\frac{2t-1}{4[t(1-t)]^{3/2}},\qquad
f''(1/3)=-\frac{9\sqrt2}{16}.
\]
Taylor expansion, using \(\sum_i\varepsilon_i=0\), produces the asserted positive quadratic deficit coefficient \(9\sqrt2/(8\pi)\). Finally, on compact nonvertex boundary arcs, \(f(p_1)+f(1-p_1-\epsilon)=\pi/2+O(\epsilon)\) uniformly, while \(f(\epsilon)=\sqrt\epsilon+O(\epsilon^{3/2})\). Substitution yields the uniform square-root boundary law. Every asymptotic statement follows from explicit differentiation or Taylor's theorem; finite experiments are not used as infinite proof.

## Verification

The standalone script `check_sections.py` was run with Python 3 from this package. It compares independently derived edge-crossing and arcsine formulas on 1000 parameter triples; checks 12000 Gaussian pointwise triangle/section equivalences; tests 10000 strict pair-balancing moves; tests the local quadratic expansion and nonvertex square-root cusp; and compares the exact formula with 320000 directly simulated Haar normal orientations for four different shapes. The checker reports `ALL_CHECKS_PASSED`. This finite corroboration does not replace the analytic proof or establish historical originality.

## Relationship to prior work

The spherical-lune edge-crossing identity is classical, as is the angle/projection framework of Feldman--Klain (2008). Kabluchko's 2019 paper studies expected solid-angle sums of random simplices, and Godland--Kabluchko--Zaporozhets (2020) studies angle sums and Gaussian projections. These are credited background, not an assertion of an entirely new angular formula. Results for regular-simplex central sections give the single equilateral benchmark. The new statement here is the *entire disphenoid shape law*, strict majorization and unique optimizer, together with local rigidity and uniform boundary degeneration for a **central section** rather than an orthogonal shadow. An indexed literature search did not reveal an equivalent sharp shape-ordering theorem, but a complete historical priority certification is not claimed.

## Limitations

Only three-dimensional equifacial tetrahedra, zero-offset centroid sections, and Haar-uniform orientations are covered. The result does not optimize over arbitrary tetrahedra or describe offset-random sections, shape distributions of individual triangles/quadrilaterals, or the area of sections. The quadratic coefficient is local; no globally optimal quadratic stability constant is asserted. The geometric equivalence to half-normal triangle formation does not imply an analogous extremizer for other length distributions. Bibliographic priority remains provisional and independent audit has not been performed.

## References

1. Z. Kabluchko, *Angle sums of random simplices in dimensions 3 and 4*, arXiv:1905.01533, first posted 2019-05-04, https://arxiv.org/html/1905.01533v1.
2. T. Godland, Z. Kabluchko, D. Zaporozhets, *Angle sums of random polytopes*, arXiv:2007.02590, first posted 2020-07-06, https://arxiv.org/html/2007.02590v2.
3. D. V. Feldman, D. A. Klain, *Angles as probabilities*, arXiv:0809.3459, first posted 2008-09-19, https://arxiv.org/abs/0809.3459. Its triangular **projection** identity is distinct from the centroid-sectional event here.
