# Sharp stochastic height order and exact intrinsic-distance law for square prisms

## Finding
Let \(P_h=[0,1]^2\times[0,h]\), \(h>0\), equipped on its boundary with its intrinsic shortest-path metric \(d_h\). Fix the center \(o=(1/2,1/2,0)\) of the lower square face. Choose \(X_h\) uniformly with respect to surface area on \(\partial P_h\), and put \(D_h=d_h(o,X_h)\). Write \(A_h(r)=\operatorname{area}\{x\in\partial P_h:d_h(o,x)\le r\}\), so that \(\Pr(D_h\le r)=A_h(r)/(4h+2)\).

Set \(r_0=1/\sqrt2\), \(q_h=\sqrt{h^2+h+1/2}\), and \(L_h=h+1\). The complete intrinsic-distance distribution, simultaneously for every \(h>0\), is given by \(A_h(r)=0\) for \(r\le0\), \(A_h(r)=4h+2\) for \(r\ge L_h\), and
\[
A_h(r)=\begin{cases}
\pi r^2,&0<r\le r_0,\\[2pt]
4r^2\arcsin\!\bigl(1/(2r)\bigr)+\sqrt{4r^2-1}-1,&r_0<r\le q_h,\\[2pt]
4r^2\left[\dfrac\pi4-\arccos\!\left(\dfrac{h+1}{\sqrt2\,r}\right)\right]
-2h^2+2(h+1)\sqrt{2r^2-(h+1)^2},&q_h<r<L_h.
\end{cases}
\tag{1}
\]
The two interior thresholds are distinct for every \(h>0\). The ball-area profile is continuously differentiable everywhere, but fails to be twice differentiable at each of \(r_0,q_h,L_h\). At the farthest-point radius the area deficit has the universal leading coefficient
\[
4h+2-A_h(L_h-\varepsilon)=4\varepsilon^2+o(\varepsilon^2)\quad(\varepsilon\downarrow0).
\tag{2}
\]

**Strict stochastic height ordering.** For any \(0<h_1<h_2\) and every \(0<r<L_{h_2}\),
\[
\Pr(D_{h_1}\le r)>\Pr(D_{h_2}\le r).
\tag{3}
\]
Thus increasing prism height strictly increases geodesic distance in first-order stochastic order, notwithstanding the changing face-area weights and the two moving geometric thresholds. In particular,
\[
\mathbb E[D_h^2]=\frac{4h^3+9h^2+8h+2}{6(2h+1)}.
\tag{4}
\]

## Assumptions and scope
The base square has unit edge length, \(h\) is any positive real number, and the surface-area measure is normalized by \(4h+2\). The endpoints of edges and corners are included in the metric space but have zero sampling probability. Every path is confined to the polyhedral surface; the three-dimensional straight-line distance is not used. For square base edge \(a>0\) and physical height \(ah\), the stated results apply after replacing measured distances by their ratios to \(a\) and multiplying unnormalized areas by \(a^2\). No assertion is made for general rectangular (non-square-base) prisms or non-Euclidean intrinsic metrics.

## Proof
**Exact distance potential.** Identify the bottom face with \([0,1]^2\). Its distance to \(o\) is \(\sqrt{(u-1/2)^2+(v-1/2)^2}\). On each of the four lateral faces use the horizontal coordinate \(u\in[0,1]\) and height \(z\in[0,h]\). Define
\[
f(u,z)=\sqrt{(u-1/2)^2+(z+1/2)^2}.
\tag{5}
\]
On the opposite (top) face, with coordinates \((u,v)\in[0,1]^2\), define \(f\) as the minimum of the four Euclidean distances to the source images
\[
(1/2,-h-1/2),\quad(1/2,h+3/2),\quad(-h-1/2,1/2),\quad(h+3/2,1/2).
\tag{6}
\]
Each facewise formula is Euclidean-distance-like and hence 1-Lipschitz. The formulas agree on all common edges: in particular, the two side formulas give the same value on a vertical edge, and on a top horizontal edge the nearest source image is the one across that edge. Thus the continuous piecewise formula is globally 1-Lipschitz for intrinsic paths, giving \(f(x)\le d_h(o,x)\).

For a lateral point, unfold the bottom square and that lateral face: the straight segment from the source image crosses their common edge inside the edge. For a top point, compare squared distances to the four images; for example the front and left image distances differ by \(2(h+1)(v-u)\). The nearest image is therefore the one across a closest top edge. Its Voronoi region is a triangle. The straight segment from this image to the point passes successively through the bottom square, its corresponding lateral rectangle, and that top-face triangle. Folding the segment back yields a surface path of length \(f(x)\). Hence \(d_h(o,x)\le f(x)\), and equality holds everywhere.

**Source-domain geometry and integration.** Under these unfoldings, the four lateral rectangles and four equal triangles of the top face join the bottom square into the planar radial domain
\[
S_h=\bigl\{(x,y)\in\mathbb R^2:\min(|x|,|y|)\le1/2,\ |x|+|y|\le h+1\bigr\}.
\tag{7}
\]
Its area is \(4h+2\). It is an area-preserving development of the surface apart from a finite cut graph, and the intrinsic distance to \(o\) becomes ordinary distance to the origin. By reflection symmetry it suffices to work on \(0\le\theta\le\pi/4\), where the radial boundary is
\[
\rho_h(\theta)=\min\!\left\{\frac1{2\sin\theta},\frac{h+1}{\cos\theta+\sin\theta}\right\}.
\tag{8}
\]
At \(\theta=0\), interpret the first term as infinite. The two branches meet at \(\theta_h=\arctan(1/(2h+1))\). The radial integral is
\[
A_h(r)=4\int_0^{\pi/4}\min\{r^2,\rho_h(\theta)^2\}\,d\theta.
\tag{9}
\]
For \(r\le r_0\), all sectors are uncut, so \(A_h(r)=\pi r^2\). For \(r_0<r\le q_h\), the active angle is \(\alpha=\arcsin(1/(2r))\) and the lateral boundary contributes \(\frac14\int_\alpha^{\pi/4}\csc^2\theta\,d\theta\); this evaluates to the middle branch of (1). For \(q_h<r<L_h\), the active angle is \(\alpha=\pi/4-\arccos((h+1)/(\sqrt2r))\). Integrating the cap contribution \((h+1)^2/(\cos\theta+\sin\theta)^2\) and the unchanged lateral part gives the last branch of (1). These evaluations also prove the endpoint continuities.

For \(r\in(0,L_h)\), differentiating (9) at ordinary radii gives \(A_h'(r)=8r\alpha_h(r)\), where \(\alpha_h\) is respectively \(\pi/4\), \(\arcsin(1/(2r))\), and \(\pi/4-\arccos((h+1)/(\sqrt2r))\) in the three open regimes. These angles match at \(r_0,q_h,L_h\); their one-sided first derivatives do not match. Accordingly \(A_h\) is \(C^1\), but not \(C^2\), at these three radii. Expanding \(\rho_h(\theta)=(h+1)(1-\theta+O(\theta^2))\) near \(\theta=0\) in (9) proves (2).

**Stochastic order.** An area-uniform point in \(S_h\) has an unsigned octant polar angle \(\Theta_h\in[0,\pi/4]\) with density proportional to \(\rho_h(\theta)^2\); conditional on that angle, its radius equals \(\rho_h(\Theta_h)\sqrt U\), with \(U\sim\operatorname{Unif}[0,1]\) independent. For \(h_2>h_1\), the boundary ratios \(\rho_{h_2}(\theta)/\rho_{h_1}(\theta)\) are nonincreasing in \(\theta\): they are constant \((h_2+1)/(h_1+1)\) below \(\theta_{h_2}\), then proportional to \(1+\cot\theta\), and finally equal one above \(\theta_{h_1}\). The angle-density likelihood ratio is therefore nonincreasing, so the quantile coupling may be chosen with \(\Theta_{h_2}\le\Theta_{h_1}\). Since both radial boundaries decrease in angle and \(\rho_{h_2}\ge\rho_{h_1}\) pointwise,
\[
\rho_{h_2}(\Theta_{h_2})\sqrt U\ge\rho_{h_1}(\Theta_{h_1})\sqrt U
\quad\text{almost surely}.
\]
For every \(0<r<L_{h_2}\), a positive-measure set of small angles has the larger boundary strictly beyond \(r\), and the common continuous \(U\) has a positive interval straddling the threshold; hence the distribution inequality is strict, proving (3).

Finally, integrate squared radial distance directly over the bottom square, four lateral rectangles, and four top triangles, obtaining respectively \(1/6\), \(2h(2h^2+3h+2)/3\), and \((6h^2+8h+3)/6\). Their sum divided by \(4h+2\) gives (4).

## Verification
The standalone `reproduce.py` independently samples surface points face by face, evaluates the radial quadrature (9), compares it to the closed form (1), checks the exact squared moment (4), and samples the strict height ordering. Its default run completed 5,245 numerical comparisons/checks successfully, spanning heights \(0.05,0.23,0.8,1,2,7\). Numeric experiments provide corroboration only; the global path potential and the angular likelihood-ratio argument provide the proofs for all positive heights. The endpoint coefficient in (2) was additionally checked numerically for several heights.

## Relationship to prior work
Miller and Pak, *Metric combinatorics of convex polyhedra: cut loci and nonoverlapping unfoldings* (arXiv:math/0312253, first posted 12 December 2003), prove general source-unfolding theory and explicitly depict the source unfolding of a **cube** from a face center in Figure 1. That geometric special case is acknowledged; the claim here is the fully height-parametric geodesic distribution, three moving/unmoving transition radii, and strict first-order stochastic ordering across all heights. The general existence of a source unfolding does not by itself give the square-prism-specific radial domains or the monotone-likelihood-ratio comparison. Classical Euclidean random-distance calculations for cubes study a different metric and sampling procedure.

## Limitations
The result is elementary once the correct geodesic source domain and angular comparison are found. A prior explicit computation for right square prisms might be unindexed or absent from accessible abstracts. No claim of uniqueness in the literature, independent verification, a universal inequality across non-square-base prisms, or an exact two-random-point law is made. The three non-\(C^2\) radii and the asymptotic coefficient concern only the specified source point and intrinsic metric.

## References
1. E. Miller and I. Pak, *Metric combinatorics of convex polyhedra: cut loci and nonoverlapping unfoldings*, arXiv:math/0312253v1, 12 December 2003, especially Figure 1, Example 2.5, Theorem 2.9, and Theorem 3.5; https://arxiv.org/abs/math/0312253.
2. E. D. Demaine and J. O'Rourke, *Geometric Folding Algorithms*, Cambridge University Press, 2007, Chapter 24 (source-unfolding background).
3. A. M. Mathai, P. Moschopoulos, and G. Pederzoli, *Distance between random points in a cube*, Statistica 59 (1999), 61–81, DOI 10.6092/issn.1973-2201/1104 (Euclidean-distance comparator).
