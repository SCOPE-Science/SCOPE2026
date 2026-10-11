# Exact rotational Minkowski-average area profile of the Reuleaux triangle

## Finding
Let \(R\) be the planar Reuleaux triangle of constant width \(w>0\), centered at the centroid of its generating equilateral triangle. Write \(R_\delta\) for its rotation about that point by \(\delta\), and form the Minkowski arithmetic average
\[
M_\delta=\tfrac12(R+R_\delta).
\]
Then, for every \(0\le\delta\le\pi/3\),
\[
\boxed{\operatorname{area}(M_\delta)
=\frac{w^2}{4}\left(2\pi-3\delta-\sqrt3+3\sin\delta-\sqrt3\cos\delta\right).}
\tag{1}
\]
Its endpoints are
\[
\operatorname{area}(M_0)=\frac{\pi-\sqrt3}{2}w^2,
\qquad
\operatorname{area}(M_{\pi/3})=\frac\pi4w^2.
\tag{2}
\]
The function in (1) is strictly increasing between the endpoints. In addition,
\[
\boxed{\operatorname{area}(M_\delta)
+\operatorname{area}(M_{\pi/3-\delta})
=\frac{3\pi-2\sqrt3}{4}w^2.}
\tag{3}
\]
The maximal mean \(M_{\pi/3}\) is exactly the width-\(w\) disk, not merely an equiareal body. Formula (1) extends to arbitrary relative rotations by periodicity \(2\pi/3\) and evenness in \(\delta\).

## Assumptions and scope
The Reuleaux triangle of width \(w\) is the intersection of three radius-\(w\) disks whose centers are the vertices of an equilateral triangle of side length \(w\). All Minkowski sums and rotations are Euclidean; area is Lebesgue area. We use the support function
\[
h_K(\theta)=\max_{x\in K}\langle x,(\cos\theta,\sin\theta)\rangle,
\]
where translations do not change the area formula.

Scale invariance reduces the proof to \(w=1\). The radius of curvature as a function of outward-normal angle is understood almost everywhere, so corners contribute normal intervals of curvature zero. In a suitable normal-angle origin, the Reuleaux triangle has radius-of-curvature function equal to \(1\) on each of the three intervals of length \(\pi/3\) centered at multiples of \(2\pi/3\), and \(0\) elsewhere. Its support function is continuously differentiable and piecewise twice differentiable; Fourier/area identities follow by integration by parts or smooth convex approximation.

## Proof
Normalize \(w=1\), set \(x=3\delta\), and work in normal-angle coordinates. The periodic curvature function \(\rho=h_R+h_R''\) is
\[
\rho(\theta)=\frac12+
\sum_{\substack{\ell\ge1\\ \ell\ \mathrm{odd}}}
\frac{2(-1)^{(\ell-1)/2}}{\pi\ell}\cos(3\ell\theta),
\tag{4}
\]
with equality in the \(L^2\) sense and at every continuity point. Indeed, integrating \(\cos(3\ell\theta)\) over the three arc-normal intervals gives the stated coefficient; all other nonconstant Fourier coefficients vanish.

Since \(h_R+h_R''=\rho\) and the threefold symmetry eliminates translation modes, the support function is
\[
h_R(\theta)=\frac12+
\sum_{\substack{\ell\ge1\\ \ell\ \mathrm{odd}}}
\frac{2(-1)^{(\ell-1)/2}}
{\pi\ell(1-9\ell^2)}\cos(3\ell\theta).
\tag{5}
\]
These coefficients decay cubically, so the series converges uniformly. Rotation shifts the argument of the support function, while Minkowski averaging averages supports. Hence the \(3\ell\)-th harmonic of \(h_{M_\delta}\) has amplitude equal to that of \(h_R\) multiplied by \(\cos(3\ell\delta/2)\).

For any support function
\[
h(\theta)=a_0+\sum_{k\ge1}\bigl(a_k\cos(k\theta)+b_k\sin(k\theta)\bigr),
\]
its planar area satisfies the Parseval/Green identity
\[
\operatorname{area}(K)=
\frac12\int_0^{2\pi}(h^2-(h')^2)\,d\theta
=\pi a_0^2-
\frac\pi2\sum_{k\ge2}(k^2-1)(a_k^2+b_k^2).
\tag{6}
\]
Inserting (5), and setting \(D(x)=\pi/4-\operatorname{area}(M_{x/3})\), gives the absolutely convergent identity
\[
D(x)=\frac1\pi\sum_{\substack{\ell\ge1\\ \ell\ \mathrm{odd}}}
\frac{1+\cos(\ell x)}{\ell^2(9\ell^2-1)},
\qquad 0\le x\le\pi.
\tag{7}
\]
It is legitimate to differentiate this series twice, obtaining
\[
D''(x)=-\frac1\pi\sum_{\substack{\ell\ge1\\ \ell\ \mathrm{odd}}}
\frac{\cos(\ell x)}{9\ell^2-1}.
\tag{8}
\]
The following elementary Fourier cosine expansion holds on \([0,\pi]\):
\[
\sum_{\substack{\ell\ge1\\ \ell\ \mathrm{odd}}}
\frac{\cos(\ell x)}{9\ell^2-1}
=\frac\pi{36}\left(\sqrt3\cos(x/3)-3\sin(x/3)\right).
\tag{9}
\]
For completeness, the right side has zero mean over \([0,\pi]\); direct integration against \(\cos(kx)\) gives cosine coefficient \((9k^2-1)^{-1}\) for odd positive \(k\) and zero for even \(k\). Uniqueness and uniform convergence of its cosine series therefore prove (9), including the endpoints.

Combining (8)--(9) yields
\[
D''(x)=-\frac{\sqrt3}{36}\cos(x/3)+\frac1{12}\sin(x/3).
\tag{10}
\]
By (7), \(D'(0)=0\). The other boundary condition is \(D(\pi)=0\): rotation by \(\pi/3\) takes \(R\) to \(-R\) up to its threefold symmetry, and the constant-width identity says \(R+(-R)\) is the unit disk. Two integrations of (10) with these boundary conditions give
\[
D(x)=\frac{x-\pi+\sqrt3-3\sin(x/3)+\sqrt3\cos(x/3)}4.
\tag{11}
\]
Substitution of \(x=3\delta\) and restoration of the scaling \(w^2\) prove (1).

Differentiating (1) gives
\[
\frac1{w^2}\frac{d}{d\delta}\operatorname{area}(M_\delta)
=\frac{-3+3\cos\delta+\sqrt3\sin\delta}{4}
=\frac{2\sqrt3\cos(\delta-\pi/6)-3}{4}.
\tag{12}
\]
This is strictly positive for \(0<\delta<\pi/3\), because \(\cos(\delta-\pi/6)>\sqrt3/2\) there. The derivative vanishes at both endpoints. Finally, replacing \(\delta\) by \(\pi/3-\delta\) in (1), adding, and using angle subtraction identities gives (3).

## Verification
The bundled `verify.py` uses symbolic trigonometry to verify the differential equation (10), both endpoint values, the derivative formula, and the complementary identity. It independently computes the Fourier cosine coefficients of the proposed summation function for several odd and even harmonics and verifies the general parity identity algebraically.

Separately, it constructs the boundary support points of the Reuleaux triangle directly from its three radius-one circular arcs and three vertices, rotates and averages those support points, and computes the area of the resulting polygonal sampling. Its values at several angles agree with (1); this numerical experiment is only a regression check and is not used for the all-angle proof.

## Relationship to prior work
Resnikoff develops Fourier support representations, the constant-width harmonic condition, and the Fourier/Parseval area formula for convex ovals. These are precisely the standard tools used here, but the inspected treatment does not consider the area of a Reuleaux triangle averaged with a continuously rotated copy.

Bogosel studies mixed areas of a Reuleaux polygon and its opposite, and specifically verifies the classical relation \(R+(-R)=B\) (for width one) and the opposite-pair mixed area. That paper covers the terminal angle \(\delta=\pi/3\), not the full intermediate-angle profile (1). The established endpoint \(\delta=0\) is simply the classical Reuleaux-triangle area. Neither endpoint is claimed as new.

The contribution is the complete one-parameter area expression, including strict monotonicity and the complementary-angle conservation identity. The closest published statements determine individual endpoint values and general Fourier tools but do not supply the exact correlation sum (9) evaluated in (11) for this two-body family.

## Limitations
The result concerns the single canonical Reuleaux triangle and Minkowski arithmetic means with one rotated copy. It is not a universal monotonicity theorem for arbitrary constant-width bodies or for other averaging weights.

The Fourier-support formula and opposite-body/disk identity are prior work. A calculation of the same angular mixed-area profile may exist in older unindexed constant-width literature; the literature searches and material inspections reported separately do not eliminate that residual risk.

## References
1. H. L. Resnikoff, *On Curves and Surfaces of Constant Width*, arXiv:1504.06733v1, publicly submitted 25 April 2015. https://arxiv.org/abs/1504.06733.
2. B. Bogosel, *Mixed volumes and the Blaschke–Lebesgue theorem*, arXiv:2311.14618v1, publicly submitted 24 November 2023. https://arxiv.org/abs/2311.14618.
3. A. Al-rabtah and K. Al-Banawi, *Vertices of Ovals with Constant Width Relative to Particular Circles*, *Mathematics* 11 (2023), 4179, DOI: 10.3390/math11194179. Its published primary MSC is 52A10.
