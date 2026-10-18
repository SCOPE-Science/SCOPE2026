# Sharp quadrilateral-section rigidity in the tetragonal disphenoid family

## Finding
Fix the motion-invariant measure on affine planes in Euclidean three-space: an unoriented plane is specified by a unit normal \(u\) and offset \(s\), modulo \((u,s)\sim(-u,-s)\), with measure proportional to spherical area in \(u\) times Lebesgue measure in \(s\). Condition this measure on the plane meeting the interior of a prescribed tetrahedron. Let \(p_4(T)\) be the probability that its section is a quadrilateral (rather than a triangle).

For every nondegenerate tetrahedron \(T\) with six edge lengths \(\ell_e\) and *exterior* dihedral angles \(\alpha_e\in(0,\pi)\) between outward adjacent facet normals, the exact intrinsic formula is
\[
 p_4(T)=\frac{2\pi\sum_e\ell_e}{\sum_e\ell_e\alpha_e}-3.
\]

More significantly, consider the natural one-parameter family of tetragonal disphenoids
\[
 T_t=\operatorname{conv}\{(1,1,t),(1,-1,-t),(-1,1,-t),(-1,-1,t)\},\qquad t>0.
\]
They have four congruent isosceles acute triangular faces and two pairs of equal opposite edges of one length. Put
\[
 L(t)=\sqrt{1+t^2},\quad H(t)=\sqrt{1+2t^2},\quad
 \alpha(t)=2\arccos\frac{t}{H(t)},\quad
 \beta(t)=2\arccos\frac1{H(t)}.
\]
Their exact quadrilateral-section probability is
\[
 \boxed{\ p_4(T_t)=\frac{2\pi[2L(t)+\sqrt2]}{2L(t)\alpha(t)+\sqrt2\beta(t)}-3.\ }
\]
It is strictly decreasing for \(0<t<1\), strictly increasing for \(t>1\), and reaches its **unique minimum** precisely at the regular tetrahedron \(t=1\):
\[
 \boxed{\ p_4(T_t)\ge\frac{2\pi}{\arccos(-1/3)}-3
 =0.288535543072\ldots,\quad \text{equality iff }t=1.\ }
\]
The limiting probabilities are \(\lim_{t\downarrow0}p_4(T_t)=\sqrt2-1\) and \(\lim_{t\to\infty}p_4(T_t)=1\). The strict minimum has a quadratic stability expansion,
\[
 p_4(T_t)=p_4(T_1)+\frac{\pi\sqrt2}{9\arccos(-1/3)^2}(t-1)^2+O((t-1)^3).
\]
The family is complete up to Euclidean similarity among disphenoids with two equal axis parameters; the theorem makes **no** assertion that the regular tetrahedron minimizes this probability among all tetrahedra or all disphenoids.

## Assumptions and scope
A random plane is sampled from the invariant plane measure conditioned to hit \(T\), not by first choosing a uniformly distributed direction and subsequently a uniform hitting offset: the latter alternative gives a different law because hitting directions in the invariant-plane ensemble are *width-biased*. Non-generic planes passing through vertices, edges, or tangent to the body have measure zero. For almost every plane meeting a tetrahedron, the section is a triangle or a quadrilateral. The result is scale invariant, but depends on the Euclidean metric; it is not an affine invariant. Angles \(\alpha_e\) are **exterior** dihedral angles; using the supplementary interior angles would invalidate the formulas. In \(T_t\), all \(t>0\) are genuinely nondegenerate.

## Proof
**1. An intrinsic plane-section count.** For each unit \(u\), order the four vertex projections \(s_1<s_2<s_3<s_4\), which is possible off a spherical null set. The hitting offsets are \((s_1,s_4)\). Those giving quadrilaterals are exactly \((s_2,s_3)\), while the other two ranges give triangular sections. Write \(g_i=s_{i+1}-s_i\) and \(W(u)=g_1+g_2+g_3\). Counting edge crossings, the number of section vertices is \(3g_1+4g_2+3g_3\) when integrated over offset. Equivalently, for every edge \([v_i,v_j]\), its crossings occupy an offset interval of length \(|u\cdot(v_i-v_j)|\). Hence
\[
 \int_{s_1}^{s_4}N(u,s)\,ds=\sum_{e}|u\cdot e|,
 \qquad
 \int_{s_1}^{s_4}\mathbf 1_{\{N=4\}}\,ds=g_2.
\]
For Haar-uniform \(u\in S^2\), \(\mathbb E|u\cdot e|=\|e\|/2\). Let \(\overline W=\mathbb E W(u)\). Integrating the preceding identities over the sphere and taking the quotient of invariant-plane measures yields
\[
 3+p_4(T)=\frac{\sum_e\ell_e}{2\overline W}.
\]
The classical polyhedral mean-width identity, with exterior angles, is
\[
 \overline W=\frac1{4\pi}\sum_e\ell_e\alpha_e.
\]
For completeness, it follows by comparing the coefficient of \(r^2\) in the Steiner polynomial for the outer parallel body \(T+rB\): the rounded-edge tubes contribute \(\tfrac12\sum_e\ell_e\alpha_e\,r^2\), and the standard intrinsic-volume normalization gives the same coefficient as \(2\pi\overline W\,r^2\). This proves the intrinsic formula, including all factors of two and \(\pi\).

**2. Geometry of the tetragonal family.** The opposite edges corresponding to the two horizontal coordinate directions both have length \(2L(t)\), with two edges of each type, while the remaining pair has length \(2\sqrt2\). Using the outward face normals proportional to the sign patterns \((\pm1,\pm1,\pm1/t)\), their corresponding exterior angles are \(\alpha(t),\alpha(t),\beta(t)\), each appearing twice. The outward-normal dot products are exactly \(\cos\alpha(t)=-1/(1+2t^2)\) and \(\cos\beta(t)=(1-2t^2)/(1+2t^2)\), consistent with the half-angle expressions above. Therefore
\[
 \sum_e\ell_e=4(2L+\sqrt2),\qquad
 \sum_e\ell_e\alpha_e=4(2L\alpha+\sqrt2\beta),
\]
which establishes the asserted formula.

**3. Global strict rigidity.** Set
\[
 F(t)=\frac{2L(t)\alpha(t)+\sqrt2\beta(t)}{2L(t)+\sqrt2}.
\]
Direct differentiation gives
\[
 \alpha'(t)=-\frac2{(1+2t^2)L(t)},\qquad
 \beta'(t)=\frac{2\sqrt2}{1+2t^2},
 \qquad 2L(t)\alpha'(t)+\sqrt2\beta'(t)=0.
\]
Thus
\[
 F'(t)=\frac{2\sqrt2\,t[\alpha(t)-\beta(t)]}{L(t)[2L(t)+\sqrt2]^2}.
\]
Because \(\arccos\) is strictly decreasing and the two half-angle cosines are respectively \(t/H(t)\) and \(1/H(t)\), the sign of \(\alpha-\beta\) is the sign of \(1-t\). Hence \(F\) strictly increases up to \(t=1\) and strictly decreases thereafter. Since \(p_4(T_t)=2\pi/F(t)-3\) and \(F(t)>0\), the claimed unique minimum and strict sides follow for every real \(t>0\), with no finite sampling assumption.

At \(t=1\), \(\alpha=\beta=\arccos(-1/3)\). For \(t\downarrow0\), \((L,\alpha,\beta)\to(1,\pi,0)\), yielding \(p_4\to\sqrt2-1\). For \(t\to\infty\), \(L\to\infty\), \(\alpha\to\pi/2\), \(\beta\to\pi\), giving \(F\to\pi/2\) and \(p_4\to1\). Finally \(F''(1)=-\sqrt2/9\), so Taylor expansion of \(2\pi/F-3\) yields the displayed quadratic coefficient.

## Verification
The complete proof is analytical and valid over the infinite interval \(t>0\). The standalone standard-library `checker.py` independently integrates the sorted projected vertex gaps over 180,001 equal-area Fibonacci directions for each of seven shape parameters. It compares the resulting Crofton quadrilateral fraction with the analytic formula, and verifies the expected section-edge identity, mean-width identity, monotone sampled profile, limiting constants, and local quadratic coefficient. The checker prints `VERIFY_OK`. Its finite directional quadrature is a **numerical consistency check**, not the basis for strict inequalities or infinite-domain claims.

## Relationship to prior work
Finch, *Width Distributions for Convex Regular Polyhedra* (public preprint 2011-10-04, arXiv:1110.0671), explicitly studies random widths and mean-square widths of the **regular** tetrahedron and cube; it does not establish this invariant-plane section-type law or its strict one-parameter disphenoid minimum. Hajja and Walker, *Equifacial Tetrahedra* (2001, DOI 10.1080/00207390110038231), examine the equifacial/disphenoid class and its distinguished centers, not invariant-plane section frequencies. Kabluchko, Litvak and Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables* (preprint 2015-11-26, arXiv:1511.08479), study regular-polytope widths and an inscribed-sphere mean-width extremal conjecture, a different normalization and family. The Crofton edge-crossing identity, polyhedral mean-width formula and the regular tetrahedron's mean width are **classical inputs, not claimed as new**. The assessed contribution is the explicit section law and globally sharp shape rigidity **within the tetragonal disphenoid family**, including its two unequal degenerations and second-order stability.

## Limitations
The new strict minimum is asserted only for the one-parameter tetragonal subfamily, not all equifacial tetrahedra or tetrahedra; no originality claim is made for the classical Crofton and Steiner identities. The result uses the invariant-plane measure and cannot be transferred unchanged to uniform-direction-first sampling. Relevant unindexed geometric-stereology or historical disphenoid inequalities could contain equivalent coverage; independent historical-priority and mathematical review have not been performed.

## References
- S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, initially public 2011-10-04. https://arxiv.org/abs/1110.0671
- M. Hajja and P. Walker, *Equifacial Tetrahedra*, International Journal of Mathematical Education in Science and Technology, 2001, DOI:10.1080/00207390110038231. https://doi.org/10.1080/00207390110038231
- Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, initially public 2015-11-26. https://arxiv.org/abs/1511.08479
- Classical polyhedral mean-breadth/Steiner formula, e.g. Stoyan, Kendall and Mecke, *Stochastic Geometry and Its Applications*, 1995, as cited in the matGeom `polyhedronMeanBreadth` documentation. https://mattools.github.io/matGeom/api/matGeom/meshes3d/polyhedronMeanBreadth.html
