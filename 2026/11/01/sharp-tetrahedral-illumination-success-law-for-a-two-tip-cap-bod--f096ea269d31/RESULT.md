# Sharp tetrahedral illumination-success law for a two-tip cap body

## Finding

For \(r>1\), let \(K_r=\operatorname{conv}(B_2^3\cup\{\pm r e_3\})\). Independently choose a Haar-uniform rotation of the four **inward beam directions** forming a regular tetrahedron. Let \(p(r)\) be the probability that these four directions illuminate every boundary point of \(K_r\). Put
\[
\delta=\arccos(1/3),\qquad \alpha=\arcsin(1/r),\qquad
\beta(\alpha)=\arccos\!\left(\frac{\cot\alpha}{\sqrt2}\right),\quad
\eta(\alpha)=\arccos\!\left(\frac{1/3-\cos^2\alpha}{\sin^2\alpha}\right).
\]
Then throughout the exact, nonempty interval \(\sqrt{3/2}\le r<\sqrt3\),
\[
\boxed{p(r)=\frac3\pi\bigl(2\pi-2\eta(\alpha)-4\cos\alpha\,\beta(\alpha)\bigr).}
\]
In addition, \(p(r)=0\) for \(r\ge\sqrt3\), and \(p(r)=1\) for \(1<r\le3/(2\sqrt2)\). On the intervening interval \(3/(2\sqrt2)<r<\sqrt{3/2}\), this result establishes the strict bounds \(0<p(r)<1\), not an evaluated distribution. At the lower endpoint of the evaluated interval, \(p(\sqrt{3/2})=3-4/\sqrt3\). The zero-probability threshold has the sharp onset
\[
\boxed{p(r)\sim\frac{4\sqrt2}{\pi 3^{3/4}}(\sqrt3-r)^{3/2}\quad(r\uparrow\sqrt3).}
\]

## Assumptions and scope

A direction \(v\in S^2\) illuminates a boundary point \(x\) of a convex body when \(x+tv\) lies in the interior for some \(t>0\). The body is the convex hull of the closed Euclidean unit ball and two mutually antipodal points at distance \(r>1\) from its center. The beams are parallel, not point light sources. Haar rotation is over \(SO(3)\); equivalently, the two-tip axis is uniform on \(S^2\) relative to a fixed tetrahedron. Tangency to an illumination cap does not illuminate a tip, but equality events on the rotation sphere have measure zero. All exact statements concern ordinary spherical surface-area probability.

The four fixed tetrahedral directions can be chosen as the rows of the matrix with entries \((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\), each divided by \(\sqrt3\). Each pair of distinct directions has scalar product \(-1/3\), and the directions positively span \(\mathbb R^3\). The result concerns the **success probability of this particular randomized four-direction scheme**, not the optimal number of directions for the body.

## Proof

**1. Illumination is a two-sided cap-hit event.** The illumination-cap characterization (Arman--Kaire--Prymak, Proposition 3) states that a positively spanning family illuminates the cap body provided every external tip is illuminated. For a tip at \(re_3\), its incident outward normal cone consists of positive multiples of normals \(n\) with \(n\cdot e_3\ge1/r\). Thus a direction \(v\) illuminates the tip if and only if its spherical distance from \(-e_3\) is strictly less than \(\alpha=\arcsin(1/r)\). The analogous condition for the opposite tip uses \(+e_3\). Conversely, illuminating all boundary points necessarily illuminates both tips. Therefore the four tetrahedral beams succeed if and only if there are vertices \(v_i,v_j\) with
\[
 v_i\cdot u>\cos\alpha,\qquad v_j\cdot u<-\cos\alpha,
\]
where \(u\) is a uniform direction representing the tip axis. Since \(\alpha<\pi/2\), the indices must differ. This reduces \(p(r)\) to the normalized area of the union of the twelve sets \(C(v_i,\alpha)\cap C(-v_j,\alpha)\), \(i\ne j\), where \(C\) denotes an open spherical cap.

**2. The first joint-hit threshold and disjointness.** The angle between \(v_i\) and \(-v_j\), for distinct indices, is \(\delta=\arccos(1/3)\). Hence a paired cap intersection has positive area precisely when \(2\alpha>\delta\), equivalent to \(r<\sqrt3\). Distinct original tetrahedral vertices have separation \(\gamma=\arccos(-1/3)\). When \(2\alpha\le\gamma\), caps from the positive tetrahedral family have pairwise disjoint interiors, as do caps from the antipodal family. Thus the twelve positive-negative intersections have pairwise disjoint interiors: a common point of two such intersections would have to belong to two different caps in at least one family. Since \(2\alpha\le\gamma\) is equivalent to \(r\ge\sqrt{3/2}\), the probability on the claimed interval is twelve times one spherical lens area divided by \(4\pi\).

**3. Exact lens area.** Consider two spherical caps with equal angular radius \(\alpha\) and center separation \(\delta\) satisfying \(\delta/2<\alpha\le\gamma/2\). Their boundary small circles meet in two points. The spherical cosine rule gives the half-angle of each boundary arc about its cap center as
\[
 \beta=\arccos\!\left(\frac{\cos\alpha(1-\cos\delta)}{\sin\alpha\sin\delta}\right)=\arccos\!\left(\frac{\cot\alpha}{\sqrt2}\right).
\]
The exterior turning angle at each corner, computed from the isosceles spherical triangle joining the two cap centers and a circle-intersection point, is
\[
 \eta=\arccos\!\left(\frac{\cos\delta-\cos^2\alpha}{\sin^2\alpha}\right).
\]
Each of the two boundary arcs has length \(2\beta\sin\alpha\) and geodesic curvature \(\cot\alpha\), contributing \(2\beta\cos\alpha\) to total geodesic curvature. Gauss--Bonnet applied to the topological disk forming the lens therefore gives
\[
 L(\alpha)=2\pi-2\eta-4\beta\cos\alpha.
\]
Consequently \(p(r)=12L(\alpha)/(4\pi)=3L(\alpha)/\pi\). At \(r=\sqrt{3/2}\) the identities \(\beta=\pi/3\), \(\eta=\pi/2\), \(\cos\alpha=1/\sqrt3\) give the stated endpoint probability.

**4. The sharp \(3/2\)-power threshold.** Let \(\alpha_0=\delta/2\), \(\varepsilon=\alpha-\alpha_0\downarrow0\). Use geodesic-normal coordinates \((x,y)\) about the midpoint of the shortest center-joining geodesic, with \(x\) along that geodesic. By the second variation of spherical distance, the two cap conditions have the local form
\[
 \pm x+\frac{\cot\alpha_0}{2}y^2<\varepsilon+o(\varepsilon)
\]
uniformly for \(|x|=O(\varepsilon)\) and \(|y|=O(\sqrt\varepsilon)\). The area element is \(1+o(1)\) on this shrinking region. Integrating the limiting parabolic strip gives
\[
 L(\alpha)\sim\frac83\sqrt{2\tan\alpha_0}\,\varepsilon^{3/2}
 =\frac{8\,2^{1/4}}3\varepsilon^{3/2},
\]
since \(\tan\alpha_0=1/\sqrt2\). As \(\alpha_0=\arcsin(1/\sqrt3)\) and \(d\alpha/dr=-1/(r\sqrt{r^2-1})\), we have \(\varepsilon\sim(\sqrt3-r)/\sqrt6\). Multiplying by \(3/\pi\) yields the displayed coefficient.

**5. Remaining zero, certain, and intermediate regimes.** If \(r\ge\sqrt3\), the paired caps do not intersect with positive area, proving \(p(r)=0\). A regular tetrahedron's four angular caps cover \(S^2\) exactly when \(\alpha\ge\arccos(1/3)=\delta\). (Indeed the four tetrahedral spherical Voronoi cells have antipodal vertices at distance \(\delta\) from their centers.) This is \(1<r\le3/(2\sqrt2)\), where both signs of every axis are covered and \(p(r)=1\). If \(\delta/2<\alpha<\delta\), at least one paired cap intersection has nonempty interior but the single-family covering leaves a nonempty open uncovered region, proving \(0<p(r)<1\). The present result does not evaluate the overlap-rich intermediate interval.

## Verification

The accompanying self-contained `verify.py` checks tetrahedral inner products, the three exact radius thresholds, the twelve pair intersections, and the endpoint constant. It compares the Gauss--Bonnet lens area against an independently derived one-dimensional spherical-polar quadrature at seven radii, tests the critical coefficient by high-precision arithmetic, and compares the predicted probability with a seeded sample of 280,000 uniform axes. Run with `python verify.py` using Python 3, NumPy, SciPy and mpmath. The stochastic comparisons are diagnostics only; the proof is the analytic argument above.

## Relationship to prior work

Arman, Kaire and Prymak prove the general illumination upper bound six for three-dimensional cap bodies. Their Proposition 3 connects tip-cap hits and positively spanning directions, and their Lemma 4 computes the marginal spherical coverage probability for one tip by a random tetrahedral frame. Those ingredients and the one-tip result are **prior work**, not part of the present novelty claim. The new statement quantifies the **joint hit of two antipodal tips**, with a zero-probability phase boundary, a disjoint twelve-lens exact regime, and its sharp noninteger onset exponent. The one-tip marginal does not imply the joint distribution; a four-direction covering upper bound does not determine the probability of a random orientation succeeding. General simplex-centered cap-union inclusion--exclusion is related but involves a single cap family, not simultaneous hits by antipodal families.

## Limitations

No closed-form expression is established here for the interval \(3/(2\sqrt2)<r<\sqrt{3/2}\). The result concerns the fixed random regular-tetrahedron illumination strategy, not optimal illumination over all direction sets or a universal cap-body theorem. Analytic correctness has been checked in the self-review, but no independent audit has occurred. Equivalent formulas in older spherical-cap, covering, or stochastic-geometry literature cannot be excluded without a broader historical search.

## References

1. A. Arman, J. S. Kaire, A. Prymak, *Illumination number of 3-dimensional cap bodies*, arXiv:2507.08712 (first posted July 11, 2025), Proposition 3 and Lemma 4. https://arxiv.org/abs/2507.08712
2. A. Arman, A. Bondarenko, A. Prymak, D. Radchenko, *On a Gallai-type problem and illumination of spiky balls and cap bodies*, Mathematika **71** (2025), e70017. https://doi.org/10.1112/mtk.70017
3. Gauss--Bonnet theorem for smooth arcs with corners on the unit sphere (standard differential-geometric identity, used with explicit arc lengths and corner angles above).
