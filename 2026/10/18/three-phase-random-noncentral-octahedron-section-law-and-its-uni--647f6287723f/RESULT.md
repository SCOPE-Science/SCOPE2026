# Three-phase random noncentral octahedron-section law and its unique quadrilateral optimum

## Finding
Let \(C=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\subset\mathbb R^3\), with vertex radius one. Choose \(U\) uniformly on the sphere \(S^2\), fix \(0\le t\le1\), and intersect \(C\) with the plane \(H(U,t)=\{x:U\cdot x=t\}\). Almost surely this intersection is empty or a convex quadrilateral or hexagon; let \(N_t\in\{0,4,6\}\) record that outcome. Put
\[
 a=1/\sqrt3,\qquad b=1/\sqrt2,\qquad
 J(t)=t\arcsin\!\left(\frac{t}{\sqrt{1-t^2}}\right)+\arctan\!\sqrt{1-2t^2}-\frac\pi4
 \quad(0\le t\le b).
\]
The entire distribution is the following exact, continuous three-phase law, with coordinates ordered as \(\bigl(\Pr(N_t=0),\Pr(N_t=4),\Pr(N_t=6)\bigr)\):
\[
\begin{cases}
\displaystyle\left(0,\frac{12J(t)}\pi,1-\frac{12J(t)}\pi\right),&0\le t\le a,\\[3pt]
\displaystyle\left(1-3t+\frac{12J(t)}\pi,-3+9t-\frac{24J(t)}\pi,3-6t+\frac{12J(t)}\pi\right),&a\le t\le b,\\[3pt]
\bigl(3t-2,3(1-t),0\bigr),&b\le t\le1.
\end{cases}
\]
The probability of a quadrilateral has precisely one maximizer on \([0,1]\):
\[
 t_*=\sqrt{\frac{5+2\sqrt2}{17}}=0.678598344545847\ldots,\qquad
 \max_{0\le t\le1}\Pr(N_t=4)
 =3-\frac{24}{\pi}\arctan\!\sqrt{\frac{7-4\sqrt2}{17}}
 =0.906685679338729\ldots.
\]
The two distinct critical offsets have geometric meaning: for \(t<a\), every plane meets the octahedron; for \(t>b\), a nonempty section is almost surely quadrilateral, never hexagonal.

## Assumptions and scope
The octahedron is normalized by its vertex distance one from the origin, so the plane's Euclidean distance from the origin is exactly \(t\). The random variable \(U\) has normalized Haar area measure; \(H(U,t)\) and \(H(-U,-t)\) represent the same unoriented plane, and symmetry makes either convention equivalent. At isolated orientations where the plane contains a vertex or is tangent to a face, the polygon type need not be generic, but those events have measure zero. At \(t=1\), the generic intersection is empty; at \(t=0\), it is hexagonal. Statements of uniqueness concern probability over random orientations, not maxima of section area or the existence of a prescribed combinatorial section.

## Proof
**Crossed edges and section types.** Almost surely none of the six vertex values \(\pm U_i\) equals \(t\). Let \(M=\#\{i:|U_i|>t\}\). If \(M=0\), all vertices lie below the plane, and the section is empty. Otherwise precisely \(M\) of the six octahedral vertices lie strictly above the plane, one from each of \(M\) distinct coordinate axes. The octahedral graph contains each pair of vertices except the three antipodal pairs. Exactly \(M(6-M)-M=M(5-M)\) edges cross the plane, where the subtracted \(M\) are the forbidden antipodal pairs. Their intersection points are distinct vertices of the planar section: consequently \(M=1\) gives four vertices and \(M=2,3\) give six. Thus \(N_t\) is determined by \(M\).

**Spherical overlap probabilities.** Define
\[
 a_k(t)=\Pr(|U_1|>t,\ldots,|U_k|>t),\qquad k=1,2,3.
\]
For \(0\le t\le1\), uniformity of each coordinate on \([-1,1]\) gives \(a_1(t)=1-t\). Let \(\theta(t)=\arcsin(t/\sqrt{1-t^2})\), defined for \(0\le t\le b\). To obtain \(a_2\), note that \(a_2=4\Pr(U_1>t,U_2>t)\). Conditioned on \(U_1=t\), the point \((U_2,U_3)\) is uniform on a circle of radius \(\sqrt{1-t^2}\); the fraction having \(U_2>t\) equals \(1/2-\theta(t)/\pi\). Differentiating with respect to the two thresholds gives
\[
 a_2'(t)=-2+\frac{4\theta(t)}\pi\quad(0<t<b).
\]
Similarly \(a_3=8\Pr(U_1>t,U_2>t,U_3>t)\). The conditional circle arc satisfying both \(U_2>t\) and \(U_3>t\) has normalized measure \(1/4-\theta(t)/\pi\) when \(0\le t\le a\), so differentiation at the three equal thresholds yields
\[
 a_3'(t)=-3+\frac{12\theta(t)}\pi\quad(0<t<a).
\]
Direct differentiation establishes \(J'(t)=\theta(t)\) and \(J(0)=0\). Since \(a_2(0)=a_3(0)=1\), integration yields
\[
 a_2(t)=1-2t+\frac{4J(t)}\pi\quad(0\le t\le b),\qquad
 a_3(t)=1-3t+\frac{12J(t)}\pi\quad(0\le t\le a).
\]
The unit-sphere constraint forces \(a_2=0\) for \(t\ge b\) and \(a_3=0\) for \(t\ge a\). These formulas are continuous at their boundary points.

**Distribution.** Expanding the three indicators \(\mathbf1_{\{|U_i|>t\}}\), or simply applying inclusion–exclusion, gives
\[
 \Pr(M=0)=1-3a_1+3a_2-a_3,\quad
 \Pr(M=1)=3a_1-6a_2+3a_3,\quad
 \Pr(M\ge2)=3a_2-2a_3.
\]
The classification from crossed edges now yields exactly the three displayed branches.

**Sharp maximization.** On \((0,a)\), the quadrilateral probability has derivative \(12\theta(t)/\pi>0\). On \((a,b)\), its derivative is \(9-24\theta(t)/\pi\), strictly decreasing from \(3\) to \(-3\), because \(\theta\) is strictly increasing from \(\pi/4\) to \(\pi/2\). On \((b,1)\), its derivative equals \(-3\). Therefore there is exactly one global maximum, at the unique \(t\in(a,b)\) satisfying \(\theta(t)=3\pi/8\). Solving \(t/\sqrt{1-t^2}=\sin(3\pi/8)\) gives \(t^2=(5+2\sqrt2)/17\). Substitution into the middle branch and cancellation of the linear terms gives the stated closed maximum probability.

## Verification
The standalone `checker.py` uses a fixed random seed, independently reconstructs all twelve edges from the six vertices and counts their intersections with the offset plane for \(250{,}000\) random orientations at each of eight offsets (two million evaluations of a full twelve-edge count). The simulated proportions agree with all three analytic probabilities with maximum observed discrepancy below \(0.0012\). The script checks their normalization, the radical critical offset, and the closed maximum value; it completed without error. The experiments are diagnostic checks only; the all-offset theorem, its boundaries, and uniqueness follow from the exact analytical argument above.

## Relationship to prior work
Liu and Tkocz (2019) optimize noncentral cross-polytope sections by length or volume at prescribed offsets; they do not establish the orientation-averaged combinatorial-type distribution. Brandenburg, De Loera, and Meroni (2023) develop hyperplane-arrangement methods for polytope sections and enumerate possible section types, including the octahedron; their section chamber classifications do not provide these offset-dependent Haar probabilities or the unique quadrilateral optimum.

The publicly available note *Exact width distribution of the unit-edge regular octahedron* (2026, scientific record `953206d3d8c4`) evaluates a relevant two-cap spherical lens and the distribution of the largest absolute normal coordinate. That **already implies the empty-section probability**, after adjusting normalization, and supplies overlap information on the interval \([1/\sqrt3,1/\sqrt2]\); these ingredients are explicitly prior, not claimed new here. A one-dimensional largest-coordinate width law does not itself determine the distribution of how many coordinates exceed the threshold, which controls the quadrilateral/hexagon split, nor give the stated unique optimal offset. The additional three-coordinate overlap calculation and its use in the complete section-type law and global optimization constitute the assessed result. Results on uniformly oriented *projections* of octahedra concern a different construction from offset-plane *sections*.

## Limitations
The result concerns the three-dimensional regular cross-polytope and a fixed offset measured in vertex-radius units; it does not classify affine-regular octahedra, arbitrary polyhedra or general-dimensional cross-polytopes. Its elementary overlap integrals share ingredients with earlier random-width calculations. The literature comparison does not exclude an unknown equivalent classical stereological evaluation. Independent external validation has not been performed.

## References
1. R. Liu and T. Tkocz, *A note on the extremal noncentral sections of the cross-polytope*, arXiv:1910.06993v1, first submitted 15 October 2019, https://arxiv.org/abs/1910.06993.
2. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1, first submitted 27 April 2023, https://arxiv.org/abs/2304.14239.
3. *Exact width distribution of the unit-edge regular octahedron*, publicly available mathematical note (2026), record `953206d3d8c4`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-width-distribution-of-the-unit-edge-regular-octahedron--953206d3d8c4.
