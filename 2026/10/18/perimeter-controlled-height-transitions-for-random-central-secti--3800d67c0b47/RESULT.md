# Perimeter-controlled height transitions for random central sections of cyclic prisms

## Finding
Let \(K\subset\mathbb R^2\) be a strictly convex polygon with \(m\ge3\) vertices \(v_1,\ldots,v_m\) in counterclockwise cyclic order and with the origin in its interior. For \(h>0\), set \(P_h=K\times[-h,h]\subset\mathbb R^3\). Let \(U\) be Haar-uniform on the sphere \(S^2\), and \(N_h\) the number of vertices of the central section \(P_h\cap U^\perp\). Define \(r_i=\|v_i\|\), \(e_i=\|v_{i+1}-v_i\|\), with indices modulo \(m\).

**Theorem (exact expectation and critical perimeter).** For every such polygon and every \(h>0\),
\[
\boxed{\mathcal E_K(h):=\mathbb E N_h=\frac2\pi\sum_{i=1}^m\left[\arctan\frac{h}{r_i}+\arccos\frac{v_i\cdot v_{i+1}+h^2}{\sqrt{r_i^2+h^2}\sqrt{r_{i+1}^2+h^2}}\right].}
\tag{1}
\]
In particular,
\[
\boxed{\lim_{h\downarrow0}\mathcal E_K(h)=4,\qquad
\mathcal E_K(h)=m+\frac{2\left(\operatorname{per}(K)-\sum_i r_i\right)}{\pi h}+O_K(h^{-3})\quad(h\to\infty).}
\tag{2}
\]
Suppose additionally that all vertices lie on a circle of radius \(R>0\) centered at the origin and that \(0\in\operatorname{int}K\). Then:

* If \(\operatorname{per}(K)>mR\), there exists a **unique finite positive half-height** maximizing \(\mathcal E_K(h)\), the maximum is strict and exceeds \(m\), and the function increases strictly before and decreases strictly after this optimum.
* If \(\operatorname{per}(K)\le mR\), the function is strictly increasing for all \(h>0\), and has the **unattained** supremum \(m\).

Consequently, every centered cyclic triangle or quadrilateral has a unique finite maximizer, while every centered cyclic polygon with at least six vertices has none. Centered cyclic pentagons exhibit both regimes; the exact transition is \(\operatorname{per}(K)=5R\), and this threshold is attained by genuine nondegenerate pentagons.

For the regular pentagon, with \(t=h/R\), the optimum and maximal mean are
\[
\boxed{t_*=\frac{3+\sqrt5}{4}=1.309016994374947\ldots,\qquad
\mathcal E_K(Rt_*)=5.246274819729384\ldots.}
\tag{3}
\]
For a regular \(m\)-gon, the unique finite maximizer exists exactly for \(m=3,4,5\); for \(m\ge6\) the mean rises strictly from \(4\) to the unattained limit \(m\).

## Assumptions and scope
The plane is chosen by uniform normal direction, without random translation; the distribution is on unoriented planes through the origin. The prism has two horizontal bases at signed heights \(\pm h\), so the **full height is \(2h\)**. The polygon is strictly convex in the polygonal sense (no redundant collinear consecutive vertices), and the origin is strictly interior. The cyclic hypothesis requires the center of the common vertex circle to be this origin. The conclusion about height optimization is not asserted for noncyclic polygons, although the expectation and asymptotic formulas hold for all polygons meeting the general assumptions. Vertices are counted combinatorially; exceptional normals cutting through prism vertices have spherical probability zero.

## Proof
**1. An angular crossing identity.** For any two nonzero vectors \(a,b\in\mathbb R^3\) with mutual angle \(\theta\in[0,\pi]\), the probability that a uniform \(U\in S^2\) satisfies \((U\cdot a)(U\cdot b)<0\) is \(\theta/\pi\). Indeed, orthogonally project \(U\) onto the two-dimensional span of \(a,b\). Its projected direction is uniform on the unit circle (except on a null set). The two sign-disagreement arcs have total angular measure \(2\theta\) among \(2\pi\) radians.

Except on finitely many great circles, each section vertex arises from exactly one prism edge with endpoints on opposite sides of the plane. The prism edges are the \(m\) vertical edges \((v_i,-h)(v_i,h)\) and the \(2m\) horizontal edges \((v_i,\pm h)(v_{i+1},\pm h)\). The vertical endpoint angle is \(2\arctan(h/r_i)\); each corresponding horizontal endpoint angle equals
\[
\alpha_i=\arccos\frac{v_i\cdot v_{i+1}+h^2}{\sqrt{r_i^2+h^2}\sqrt{r_{i+1}^2+h^2}}.
\]
Linearity of expectation and the angular crossing identity yield equation (1), without assuming independence between intersected edges.

**2. Limits for arbitrary polygons.** As \(h\downarrow0\), the vertical angles vanish. The horizontal angles converge to the polar-angle gaps \(\delta_i\in(0,\pi)\) between consecutive polygon vertices viewed from the origin. Since the origin is interior, \(\sum_i\delta_i=2\pi\); equation (1) then yields the limit \(4\).

As \(h\to\infty\), the vertical angle obeys
\[
2\arctan(h/r_i)=\pi-\frac{2r_i}{h}+O_K(h^{-3}),
\]
while the horizontal endpoint angle satisfies
\[
\alpha_i=\frac{e_i}{h}+O_K(h^{-3}).
\]
Substitution into the complete edge sum yields equation (2).

**3. Exact one-dimensional optimization for cyclic bases.** Let \(t=h/R\), and let \(\delta_i\in(0,\pi)\) be the successive vertex-angle gaps; their sum is \(2\pi\). Put \(s_i=\sin(\delta_i/2)\) and \(c_i=\cos(\delta_i/2)\), both strictly positive. The horizontal angle formula simplifies to
\[
\alpha_i=2\arcsin\left(\frac{s_i}{\sqrt{1+t^2}}\right).
\]
Hence
\[
\mathcal E_K(Rt)=\frac2\pi\left[m\arctan t+2\sum_{i=1}^m\arcsin\left(\frac{s_i}{\sqrt{1+t^2}}\right)\right].
\tag{4}
\]
Differentiating gives
\[
\frac{d\mathcal E_K(Rt)}{dt}=\frac2{\pi(1+t^2)}B_K(t),\qquad
B_K(t)=m-2\sum_{i=1}^m\frac{s_i t}{\sqrt{t^2+c_i^2}}.
\tag{5}
\]
For every \(t>0\),
\[
B'_K(t)=-2\sum_{i=1}^m\frac{s_i c_i^2}{(t^2+c_i^2)^{3/2}}<0,
\]
while \(B_K(0)=m>0\) and \(\lim_{t\to\infty}B_K(t)=m-2\sum_i s_i=m-\operatorname{per}(K)/R\). Thus exactly one positive root exists when the perimeter exceeds \(mR\), and no positive root exists otherwise. The derivative sign in equation (5) establishes all monotonicity, uniqueness and strictness assertions. When a maximum exists, its value is above its limiting value \(m\), because the function strictly decreases from the maximum to that limit.

**4. Exhaustive side-count transition.** The gap constraints \(0<\delta_i<\pi\), \(\sum_i\delta_i=2\pi\) and concavity of \(x\mapsto\sin(x/2)\) imply the universal strict lower bound
\[
\operatorname{per}(K)=2R\sum_i\sin(\delta_i/2)>4R.
\]
To see this, minimize the concave sum on the compact polytope \(0\le\delta_i\le\pi\), \(\sum_i\delta_i=2\pi\). Its extreme points have two gaps equal to \(\pi\) and the others zero; the minimum is \(2\) before multiplication by \(2R\). Strict concavity on the positive interior makes the inequality strict for a nondegenerate polygon. Thus \(\operatorname{per}(K)>mR\) for \(m=3,4\).

Jensen's inequality gives the complementary sharp bound
\[
\operatorname{per}(K)\le2mR\sin(\pi/m)\le mR\qquad(m\ge6),
\]
where \(2\sin(\pi/m)\le1\) for \(m\ge6\). Consequently no such polygon with at least six vertices has a finite optimizer.

For \(m=5\), the regular pentagon has perimeter \(10R\sin(\pi/5)>5R\). Conversely, for every sufficiently small \(\varepsilon>0\), take a cyclic pentagon with successive angular gaps
\[
\pi-2\varepsilon,\quad\pi-2\varepsilon,\quad\varepsilon,\quad\varepsilon,\quad2\varepsilon.
\]
These are positive and strictly smaller than \(\pi\), sum to \(2\pi\), and make the perimeter approach \(4R<5R\) as \(\varepsilon\downarrow0\). Continuous interpolation of the gap vectors with those of the regular pentagon retains strict centered convexity and therefore realizes the equality \(\operatorname{per}(K)=5R\) at an intermediate genuine pentagon. This proves that all three perimeter regimes occur in the five-sided family.

**5. Regular-pentagon constant.** With all gaps equal to \(2\pi/m\), equation (5) reduces to
\[
B_K(t)=m\left(1-\frac{2t\sin(\pi/m)}{\sqrt{t^2+\cos^2(\pi/m)}}\right).
\]
For \(m=5\), solving \(B_K(t)=0\) gives
\[
t_*=\frac{\cos(\pi/5)}{\sqrt{4\sin^2(\pi/5)-1}}=\frac{3+\sqrt5}{4}.
\]
Equation (4) evaluated there gives equation (3). Every stationary-point classification follows from strict monotonicity of \(B_K\), not numerical maximization. \(\square\)

## Verification
Run `python3 checker.py` with Python 3.10 or later. The standalone checker cross-compares the all-polygon edge-angle formula with the independent cyclic-angle simplification for regular bases of 3 through 11 sides and two contrasting cyclic pentagons. It verifies the derivative formula by centered finite differences, checks the finite-maximizer and monotone regimes, and samples 770,000 independent Gaussian normal vectors to count actual section-edge crossings for seven prism configurations, including one noncyclic pentagon. The checker reports 135 successful comparisons with a fixed random seed. Finite numerical sampling corroborates, but does **not** prove, the infinitely quantified theorem; the proof above is analytic.

## Relationship to prior work
Brandenburg, De Loera, and Meroni [1] describe chambers of affine and central polytope sections and algorithms maximizing the number of faces of a section of a **fixed** polytope. Their Theorems 1.1 and 1.3 do not integrate vertex count against rotation-invariant measure, optimize the prism half-height, or identify the perimeter threshold for cyclic bases. Their general chamber idea is compatible with step 1, but does not imply the displayed exact distributional formula and shape transition without further geometric work.

Konstantinova and Shchur [2] numerically study angle distributions in random sections of polyhedra, including a triangular prism and a cube; the accessible abstract does not establish the present universal perimeter classification. The full text could not be inspected and remains a bibliographic limitation.

For rectangular boxes, the known cube-section law and a later shape-optimized rectangular-box result [3] give the four-sided, rectangular special case of expected vertex counts; the result here **does not claim that case as new**. Existing work on the full triangular-prism polygon-type law similarly covers one regular three-sided specialization. The present new scope is the general edge-angle expectation for nonregular polygons, the full perimeter-controlled regime change for **all** centered cyclic polygons, and the five-sided golden-ratio optimization. An unrelated exact prism *width-moment* calculation [4] measures a different random variable and does not imply the section-complexity phase diagram.

## Limitations
The formula concerns central Haar planes only, not random affine offsets. The height transition requires a cyclic polygon centered at its circumcenter; it is not asserted for an arbitrary noncyclic base. The theorem provides the expected vertex count, not the complete distribution of section polygon types, which remains a distinct quantity. An unindexed stereological or older section-combinatorics identity might overlap the angular expectation formula. The more specific perimeter transition and its sharp five-sided classification were not located in the inspected sources, but that negative finding is not a proof of historical priority. Numerical comparisons alone cannot establish the all-parameter claims.

## References
1. M.-C. Brandenburg, J. A. De Loera, and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1, 27 April 2023, https://arxiv.org/abs/2304.14239; complete version at https://arxiv.org/html/2304.14239v1.
2. L. N. Shchur and E. P. Konstantinova, *Algorithm for Density of Angle Distribution in Random Sections of Polyhedron*, SSRN 4485810, posted 20 June 2023, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4485810.
3. *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.
4. *Exact mean-square width of every uniform regular prism*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-mean-square-width-of-every-uniform-regular-prism--eb371b3be549.
