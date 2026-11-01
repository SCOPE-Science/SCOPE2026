# Exact central-section type law and aspect-ratio recovery for equilateral triangular prisms

## Finding
Let \(R,h>0\), and let \(P_{R,h}\subset\mathbb R^3\) be the right triangular prism with vertices
\[
(R\cos(2\pi j/3),R\sin(2\pi j/3),\pm h),\qquad j=0,1,2.
\]
Choose a plane through its centroid with a Haar-uniform **unoriented normal** and let \(N\) be the number of sides of the polygonal section. Put \(t=h/R>0\). The section is almost surely a triangle, quadrilateral, or pentagon, and its **entire** side-count law is
\[
\begin{aligned}
p_3(t)&:=\Pr(N=3)=1-\frac6\pi\arcsin\frac1{2\sqrt{1+t^2}},\\
G(t)&:=\arccos\frac{t^2-1/2}{t^2+1},\\
\mathbb E[N]&=\frac6\pi G(t)+\frac6\pi\arctan t,\\
p_5(t)&:=\Pr(N=5)=\mathbb E[N]-4+p_3(t),\\
p_4(t)&:=\Pr(N=4)=1-p_3(t)-p_5(t).
\end{aligned}
\]
Every \(p_j(t)\) is strictly positive for finite \(t>0\). Furthermore, \(p_3\) is strictly increasing from zero to one, so the single scalar probability of a triangular central section determines the prism's aspect ratio up to similarity:
\[
\boxed{\ t=\sqrt{\frac1{4\sin^2(\frac\pi6(1-p_3))}-1}\ }. 
\]
The pentagon probability has exactly one global maximum over all \(t>0\). Its maximizer \(t_*\) is the unique positive solution of
\[
1-\frac{2\sqrt3\,t}{\sqrt{1+4t^2}}+\frac{t}{\sqrt{3+4t^2}}=0,
\]
and numerically \(t_*\approx0.531469551063655\), \(p_5(t_*)\approx0.385155805674177\).

## Assumptions and scope
The prism is a **solid** convex right prism with equilateral base, radius \(R\) measured from base centroid to vertices, and full vertical height \(2h\). The plane always contains the three-dimensional centroid. Orientation is Haar-uniform on \(\mathbb {RP}^2\), not the motion-invariant random *affine* plane model conditioned on intersection. Nongeneric planes through one or more prism vertices have Haar probability zero. Probabilities depend only on \(t=h/R\); degeneracies \(R=0\) and \(h=0\) are excluded.

## Proof
**(1) Side-count support and triangular criterion.** A generic section of a convex polyhedron has one side on each intersected face. A triangular prism has five faces, hence a generic central section has between three and five sides. Write a unit normal as \((r\cos\phi,r\sin\phi,w)\). By reversing its sign assume \(w>0\). Put \(a_j=Rr\cos(\phi-2\pi j/3)\), for which \(a_0+a_1+a_2=0\). The upper and lower vertex signs are those of \(a_j+hw\) and \(a_j-hw\). If every upper sign is positive and every lower sign is negative, precisely the three vertical edges are crossed, yielding a triangle. Otherwise at least one horizontal triangular face has mixed signs and contributes two crossed edges. If both horizontal faces have mixed signs, there are already at least four crossings. If only one is mixed, the other is homogeneous: the zero-sum relation forces exactly two vertices of the mixed face to have signs opposite the homogeneous face, hence two more vertical crossings. Such a section has at least four sides. Thus \(N=3\) precisely when \(|a_j|<hw\) for all three \(j\).

**(2) Solid-angle integral.** Put \(t=h/R\), let \(\theta\in[0,\pi/2]\) be the polar angle from the positive vertical axis, and put \(M(\phi)=\max_j|\cos(\phi-2\pi j/3)|\). The triangular criterion reads \(\tan\theta<t/M(\phi)\). The normal-cone area, including both polar hemispheres, gives
\[
p_3(t)=1-\frac1{2\pi}\int_0^{2\pi}\frac{M(\phi)}{\sqrt{t^2+M(\phi)^2}}\,d\phi.
\]
The six unoriented base-vertex directions divide the circle into six sectors of angle \(\pi/3\); within each half-sector, \(M=\cos\delta\), \(0\le\delta\le\pi/6\). Consequently
\[
\begin{aligned}
p_3(t)&=1-\frac6\pi\int_0^{\pi/6}\frac{\cos\delta}{\sqrt{t^2+\cos^2\delta}}\,d\delta\\
&=1-\frac6\pi\arcsin\frac1{2\sqrt{1+t^2}}.
\end{aligned}
\]
Since its arcsine argument decreases strictly with \(t>0\), \(p_3:(0,\infty)\to(0,1)\) is a strictly increasing bijection. Direct inversion gives the formula in the Finding.

**(3) Mean side count.** Every section vertex lies on one of the prism's nine edges. For any two nonzero endpoint vectors \(x,y\), the probability that a uniformly random plane through the origin separates them is \(\angle(x,y)/\pi\), because a great-circle normal rotates uniformly through the planar angle subtended by the vectors. The six horizontal edges subtend
\[
G(t)=\arccos\frac{t^2-1/2}{t^2+1}
\]
and the three vertical edges subtend \(2\arctan t\). Summing the nine edge-separation probabilities yields the displayed \(\mathbb E[N]\). Since \(N\in\{3,4,5\}\), the relations \(p_3+p_4+p_5=1\) and \(\mathbb E[N]=4-p_3+p_5\) determine \(p_4,p_5\) exactly.

**(4) Rigidity and pentagon optimum.** Positivity of \(p_3\) and \(p_4\) follows from nonempty open normal sets near the vertical and horizontal directions, respectively. A nonempty open pentagon normal set is obtained from base vertex scalar products proportional to \((2,-0.4,-1.6)\) with vertical scalar product strictly between \(0.4\) and \(1.6\); one vertical and four horizontal edges are then crossed. The base-direction pattern is feasible because it has zero sum and lies in the two-dimensional span of the three equilateral vertex vectors. Varying the normal's slope realizes that pattern for any \(t>0\). Hence \(p_5>0\).

Differentiation gives
\[
p_5'(t)=\frac6{\pi(1+t^2)}H(t),\qquad H(t)=1-\frac{2\sqrt3 t}{\sqrt{1+4t^2}}+\frac{t}{\sqrt{3+4t^2}}.
\]
Furthermore
\[
H'(t)=-\frac{2\sqrt3}{(1+4t^2)^{3/2}}+\frac3{(3+4t^2)^{3/2}}<0
\]
because \(2\sqrt3>3\) and \(1+4t^2<3+4t^2\). As \(H(0)=1\) and \(\lim_{t\to\infty}H(t)=3/2-\sqrt3<0\), exactly one critical point occurs, and it is a strict global maximum. The explicit law gives \(p_5(t)\to0\) at both endpoints, confirming globality.

## Verification
`proof/check_prism.py` independently enumerates actual prism edge-crossing signs for seven aspect ratios using 500,000 independent isotropic normals each, compares with all three formulas and their expected side counts, numerically integrates the triangular normal cone without using the reduced formula, checks inversion at five positive ratios, and checks the unique-maximum root. Run `python proof/check_prism.py` with Python 3, NumPy and SciPy. A representative exact value at \(t=1\) is \((p_3,p_4,p_5)\approx(0.309840,0.362904,0.327256)\). Numerical checks corroborate the analytic argument; they do not prove the universal result.

## Relationship to prior work
Shchur and Konstantinova's 2023 publicly posted study designs uniform random **affine** planes and estimates distributions of section angles numerically, including a regular triangular prism. Its described sampling experiment does not supply the Haar-*central* side-count law or its exact aspect inversion. Related published studies concern random central sections of other polytopes and noncentral sections of triangular prisms. Crucially, the law of planes conditioned on intersecting a prism weights directions by width and integrates over offsets; it does not imply a law at the zero-measure centroid offset. A related calculation for regular even-sided prisms cannot specialize to a triangular base. Literature priority remains provisional because the entire 2023 manuscript was not accessible for checking any ancillary formulas.

## Limitations
Only the equilateral-base **right** triangular prism and Haar-central-plane experiment are classified; arbitrary triangular prisms, offset distributions, section-area statistics, statistical sampling errors, and arbitrary polyhedra are not addressed. Exact shape recovery is up to an overall positive scaling, not absolute dimension. The historical novelty comparison is necessarily qualified by inaccessible plausible published material; no independent mathematical audit has been performed.

## References
- L. N. Shchur and E. P. Konstantinova, *Algorithm for Density of Angle Distribution in Random Sections of Polyhedron*, publicly posted June 20, 2023, SSRN abstract 4485810; subsequent journal DOI: 10.1016/j.eswa.2023.121195.
- E. Milman and Y. Yifrach, *Regular Random Sections of Convex Bodies and the Random Quotient-of-Subspace Theorem*, arXiv:1910.06033, first public version October 14, 2019. It treats high-dimensional diameter and position estimates, not three-dimensional prism face counts.
