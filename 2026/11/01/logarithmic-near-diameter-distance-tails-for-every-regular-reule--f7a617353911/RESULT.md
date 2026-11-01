# Logarithmic near-diameter distance tails for every regular Reuleaux odd-gon

## Finding

For each **fixed odd integer** \(n\ge3\), consider the regular Reuleaux \(n\)-gon \(R_n\) of Euclidean width one, and choose \(X,Y\) independently and uniformly by area in \(R_n\). Writing
\[
A_n=\operatorname{area}(R_n)=\frac12\left(\pi-n\tan\frac{\pi}{2n}\right),
\]
we prove the **sharp endpoint law**
\[
\boxed{\displaystyle
\lim_{\varepsilon\downarrow0}
\frac{\mathbb P(\lVert X-Y\rVert>1-\varepsilon)}
{\varepsilon^3\log(1/\varepsilon)}
=\frac{n}{3A_n^2}.}
\]
In particular, for the width-one Reuleaux triangle the coefficient is \(4/(\pi-\sqrt3)^2\). The normalized leading coefficient, after multiplication by the squared area, recovers the number \(n\) of corners.

For comparison, two uniform points in the *disk* of diameter one instead have
\[
\mathbb P(\lVert X-Y\rVert>1-\varepsilon)
\sim \frac{256}{15\sqrt2\,\pi}\,\varepsilon^{5/2};
\]
thus the finite-corner and smooth circular cases have genuinely different endpoint exponents.

## Assumptions and scope

For odd \(n\ge3\), take the vertices of a regular Euclidean \(n\)-gon on a circle of radius \(1/(2\cos(\pi/(2n)))\). Its regular Reuleaux realization is the intersection of the unit closed disks centered at the \(n\) vertices, equivalently the convex curvilinear \(n\)-gon with consecutive vertices joined by radius-one circular arcs centered at their appropriate opposite vertices. Its width and diameter both equal one. Uniform sampling means normalized two-dimensional Lebesgue measure; the two draws are independent. The theorem fixes \(n\) first and then lets \(\varepsilon\downarrow0\).

Define the covariogram \(g(z)=\operatorname{area}(R_n\cap(R_n-z))\). It is even, and the difference body of every width-one planar convex body is the closed unit disk. All areas and angles below are Euclidean.

## Proof

**Step 1: Probability and oriented sectors.** From Fubini and translation invariance, the displacement \(Y-X\) has density \(g(z)/A_n^2\). Since \(R_n-R_n\) is the unit disk, polar integration gives
\[
A_n^2\,\mathbb P(\lVert X-Y\rVert>1-\varepsilon)
=\int_0^\varepsilon (1-s)G_n(s)\,ds,
\qquad
G_n(s)=\int_0^{2\pi}g((1-s)u_\theta)\,d\theta.
\]
Apart from a finite collection of transition angles, every directed unit diameter has a vertex at one endpoint and a smooth point on the opposite arc, which is the circle of radius one centered at that vertex. There are \(n\) sectors of angular width \(\alpha=\pi/n\) with a vertex at the first endpoint and \(n\) reverse sectors; these \(2n\) sectors partition the full circle. Evenness \(g(z)=g(-z)\) allows the same local calculation on both types.

**Step 2: Local wedge coefficient.** In a sector, let \(v\) be the initial vertex and let \(0<\phi<\alpha\) measure the direction within that sector. The interior tangent cone of \(R_n\) at \(v\) is a wedge with unit edge rays \(t_1,t_2\) making angle \(\pi-\alpha\). Write a near-vertex displacement as \(w=a t_1+b t_2\), \(a,b\ge0\). The local area element is \(\sin\alpha\,da\,db\); after exchanging the rays if necessary,
\[
\langle u_\phi,t_1\rangle=\sin\phi,
\qquad
\langle u_\phi,t_2\rangle=\sin(\alpha-\phi).
\]
The opposite circular-arc constraint on \(v+w+(1-s)u_\phi\), whose arc is part of the unit circle centered at \(v\), is
\[
2(1-s)\langle u_\phi,w\rangle+|w|^2\le 2s-s^2.
\]
Ignoring the nonnegative quadratic term bounds the overlap by the wedge simplex. For each fixed interior angle \(\phi\), its area is asymptotic to
\[
g((1-s)u_\phi)\sim s^2 c_n(\phi),\qquad
c_n(\phi)=\frac{\sin\alpha}{2\sin\phi\sin(\alpha-\phi)}
=\frac12\left(\cot\phi+\cot(\alpha-\phi)\right).
\]
The factor \(\sin\alpha\) is the wedge Jacobian; the factor \(1/2\) is the area of the unit two-dimensional simplex.

**Step 3: Uniform interior control and endpoint bounds.** Put \(L_s=\log(1/s)\) and \(\delta_s=\sqrt{s}\,L_s\). The displayed wedge approximation holds *uniformly, with relative error tending to zero*, on the trimmed interval \(\delta_s\le\phi\le\alpha-\delta_s\). Here is a geometric justification with the required scale control. In that interval the simplex inequality forces \(|w|\le C_n s/\delta_s=C_n\sqrt{s}/L_s\), so the circular quadratic term is \(O_n(s/L_s^2)\). At the initial vertex the two adjacent circular boundary arcs deviate quadratically from their tangent rays: requiring both wedge coordinates to exceed \(C_n s/L_s^2\) and decreasing the simplex right-hand side by \(C_n s/L_s^2\) gives an inside approximation losing an \(O_n(L_s^{-2})\) relative area. All nonincident disk constraints have positive slack near the vertex. At the opposite boundary arc, the neighboring disk constraints have slack bounded below by a constant multiple of the angular distance \(\delta_s\) from its endpoints, whereas \(|w|+s=O_n(\sqrt{s}/L_s)\); they are therefore inactive for the shrunken simplex. The wedge-simplex upper bound and this explicit interior approximation establish the uniform estimate.

For the two excluded endpoint intervals let \(\Delta=\min\{\phi,\alpha-\phi\}\). The same circular inequality yields \(|w|^2\le C_ns\) and \(\langle u_\phi,w\rangle\le C_ns\). Since at least one of the two ray projections stays bounded away from zero in a fixed sector, one wedge coordinate is \(O_n(s)\) and the other is \(O_n(\sqrt{s})\). Together with the simplex upper bound this gives, uniformly in each sector,
\[
0\le g((1-s)u_\phi)
\le C_n\min\left\{s^{3/2},\frac{s^2}{\Delta}\right\}.
\]
Integrating this bound over both endpoint intervals of width \(\delta_s\) gives
\[
O_n\bigl(s^2[1+\log L_s]\bigr)
=o_n\bigl(s^2\log(1/s)\bigr).
\]
The endpoint regions therefore do not affect the leading logarithmic coefficient.

**Step 4: The logarithmic angular integral.** The explicit coefficient has antiderivative given by logarithms of sines, hence
\[
\int_{\delta_s}^{\alpha-\delta_s}c_n(\phi)\,d\phi
=\log\frac{\sin(\alpha-\delta_s)}{\sin\delta_s}
=\frac12\log(1/s)-\log L_s+O_n(1).
\]
Steps 2–3 show that *each* of the \(2n\) oriented sectors contributes \(\frac12s^2\log(1/s)(1+o_n(1))\). Consequently,
\[
G_n(s)\sim ns^2\log(1/s).
\]
Finally \(\int_0^\varepsilon s^2\log(1/s)\,ds
\sim(\varepsilon^3/3)\log(1/\varepsilon)\); inserting this into Step 1 proves the theorem.

**Disk comparator.** For the disk of radius \(1/2\), the overlap of two copies displaced by distance \(1-s\) is \(\frac{4}{3\sqrt2}s^{3/2}(1+o(1))\). Polar integration and division by the squared disk area \((\pi/4)^2\) give the stated coefficient \(256/(15\sqrt2\pi)\).

## Verification

The standalone file `verify_reuleaux_log_tail.py` independently constructs \(R_n\) as an intersection of unit disks and evaluates its overlap with translates by direct one-dimensional vertical-slice integration. It checks the local middle-sector and transition-direction scalings for \(n=3,5,7\), and the trigonometric coefficient and its exact angular primitive for odd \(n\) through eleven. Running `python verify_reuleaux_log_tail.py` reported `REULEAUX_FINITE_CHECKS_OK: 278 checks; 3, 5, 7, 9, 11 vertices`. These are finite checks, not a proof of the limit; the uniform estimates in Steps 2–4 supply the proof.

## Relationship to prior work

Falcó and Myroshnychenko (2026, arXiv:2608.05125, first public August 5) characterize the regular Reuleaux odd-gons as symmetry-constrained area minimizers and give the construction and area formula used here; neither a pair-distance distribution nor this near-diameter logarithmic law is their stated conclusion. Pure–Durrani–Tong–Pan develop distance distributions for *straight-edged polygons*, whereas the relevant contact geometry here is the pairing of circular arcs with corners. Bonnet–Gusakova–Thäle–Zaporozhets study bounds for *mean* distances between two random points, not this endpoint tail. The covariogram identity and the disk comparison are classical ingredients, not claimed as new. No claim of definitive publication priority is made.

## Limitations

The assertion is pointwise in every fixed odd \(n\); the constants in the uniform local estimates may depend on \(n\). It does not supply an exact finite-\(\varepsilon\) CDF, nor a joint limit with \(n\to\infty\), nor a law for arbitrary nonsymmetric constant-width bodies. Identifying all historical equivalents in the broader covariogram literature remains a genuine priority risk. Independent verification by another researcher has not been performed.

## References

1. J. Falcó and S. Myroshnychenko, *Area Minimization Among Group-Invariant Planar Convex Bodies of Constant Width* (2026), arXiv:2608.05125, https://arxiv.org/abs/2608.05125 (first public August 5, 2026).
2. R. Pure, S. Durrani, F. Tong and J. Pan, *Distance distribution between two random points in arbitrary polygons*, Mathematical Methods in the Applied Sciences 45 (2022), 2760–2775, DOI:10.1002/mma.7951.
3. G. Bonnet, A. Gusakova, C. Thäle and D. Zaporozhets, *Sharp inequalities for mean distance of random points in convex bodies*, arXiv:2010.03351.
