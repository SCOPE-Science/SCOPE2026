# Small-threshold rank-constrained Gaussian maxima are governed by circumscribed-polytope volume
## Finding
For integers \(d\ge 1\) and \(n\ge d+1\), let \(\mathcal E_n\) denote the set of \(n\times n\) correlation matrices. For \(G\in\mathcal E_n\), let
\[
F_G(t)=\Pr\{X_i\le t\text{ for every }i\},
\]
where \(X\) is centered Gaussian with covariance \(G\), and define
\[
m_{d,n}(t)=\min\{F_G(t):G\in\mathcal E_n,\ \operatorname{rank}G\le d\}.
\]
For unit vectors \(u=(u_1,\ldots,u_n)\in(\mathbb S^{d-1})^n\), set
\[
K(u)=\{x\in\mathbb R^d:\langle u_i,x\rangle\le1\text{ for every }i\},
\]
and assign \(\operatorname{vol}_d K(u)=+\infty\) when \(K(u)\) is unbounded. Put
\[
V_{d,n}=\inf_u\operatorname{vol}_d K(u).
\]
Then
\[
\boxed{\lim_{t\downarrow0}\frac{m_{d,n}(t)}{t^d}=(2\pi)^{-d/2}V_{d,n}.}
\]
Thus the low-threshold phase of the rank-constrained Gaussian-maxima problem is exactly the minimum-volume problem for polyhedra with at most \(n\) tangent supporting planes around the Euclidean unit ball.

For \(d=3\) and \(n=5\), the classical solved five-face case of the circumscribed-polyhedron problem is the right equilateral triangular prism. Its unit-insphere volume is \(6\sqrt3\). Therefore
\[
\boxed{m_{3,5}(t)=\frac{6\sqrt3}{(2\pi)^{3/2}}t^3(1+o(1))}
\qquad(t\downarrow0),
\]
where the coefficient is approximately \(0.6598452203723182\). A leading-order realizing configuration consists of the five outward normals
\[
e_3,-e_3,(1,0,0),\left(-\frac12,\frac{\sqrt3}2,0\right),\left(-\frac12,-\frac{\sqrt3}2,0\right).
\]
These five points form a triangular bipyramid on the sphere.

## Assumptions and scope
The Gaussian vectors are centered and have unit coordinate variances. Rank at most \(d\) is equivalent to realization by unit Gram vectors in \(\mathbb R^d\). The asymptotic concerns \(t\downarrow0\) with fixed \(d,n\). It does not assert which configuration minimizes the Gaussian probability at any fixed positive \(t\), nor does it give a convergence rate or a uniqueness theorem for asymptotically minimizing configurations.

The definition allows repeated or redundant supporting directions. This does not alter the \(d=3,n=5\) value: a bounded intersection with fewer than five active planes has at least four faces, and the minimum-volume four-face circumscribed polyhedron is the regular tetrahedron, whose unit-inradius volume \(8\sqrt3\) is larger than \(6\sqrt3\).

## Proof
Every \(G\in\mathcal E_n\) with \(\operatorname{rank}G\le d\) is the Gram matrix of unit vectors \(u_1,\ldots,u_n\in\mathbb R^d\). If \(W\sim N(0,I_d)\), then
\[
F_G(t)=\Pr\{\langle u_i,W\rangle\le t\text{ for every }i\}=\gamma_d(tK(u)),
\]
where \(\gamma_d\) is standard Gaussian measure on \(\mathbb R^d\).

The main point is to make the small-dilation limit uniform over configurations that may vary with \(t\). For \(R>0\), define
\[
a_R=\min_u\operatorname{vol}_d(K(u)\cap B_R).
\]
The parameter space \((\mathbb S^{d-1})^n\) is compact. For fixed \(R\), the truncated volume is continuous in \(u\): away from the finitely many limiting supporting hyperplanes, membership in \(K(u)\cap B_R\) is eventually constant, so dominated convergence applies. Hence the minimum defining \(a_R\) exists. The numbers \(a_R\) are nondecreasing and satisfy \(a_R\le V_{d,n}\).

In fact \(a_R\uparrow V_{d,n}\). If the limit were \(a<V_{d,n}\), choose \(R_k\to\infty\) and minimizing configurations \(u^{(k)}\), then pass to a convergent subsequence \(u^{(k)}\to u^*\). For every fixed \(L\), eventually \(R_k\ge L\), and
\[
\operatorname{vol}_d(K(u^{(k)})\cap B_L)\le a_{R_k}.
\]
Continuity of the fixed-\(L\) truncated volume gives \(\operatorname{vol}_d(K(u^*)\cap B_L)\le a\). Letting \(L\to\infty\) yields \(\operatorname{vol}_d K(u^*)\le a<V_{d,n}\), a contradiction.

Write \(\varphi_d(0)=(2\pi)^{-d/2}\). For any fixed \(r>0\), every configuration satisfies
\[
\gamma_d(tK(u))\ge \varphi_d(0)e^{-r^2/2}\operatorname{vol}_d(tK(u)\cap B_r)
=\varphi_d(0)e^{-r^2/2}t^d\operatorname{vol}_d(K(u)\cap B_{r/t}).
\]
Therefore
\[
\liminf_{t\downarrow0}\frac{m_{d,n}(t)}{t^d}
\ge \varphi_d(0)e^{-r^2/2}V_{d,n}.
\]
Letting \(r\downarrow0\) gives the lower bound \(\varphi_d(0)V_{d,n}\).

For the upper bound, choose a configuration with finite volume at most \(V_{d,n}+\varepsilon\). A finite-volume convex intersection containing the unit ball is bounded. After the change of variables \(x=ty\),
\[
\frac{\gamma_d(tK(u))}{t^d}
=\varphi_d(0)\int_{K(u)}e^{-t^2\lvert y\rvert^2/2}\,dy
\longrightarrow \varphi_d(0)\operatorname{vol}_dK(u)
\]
by dominated convergence. Hence the limsup is at most \(\varphi_d(0)(V_{d,n}+\varepsilon)\), and \(\varepsilon\downarrow0\) proves the general formula.

For \(d=3,n=5\), the solved Lindelöf five-face problem identifies the right equilateral triangular prism as the minimum-volume polyhedron circumscribed about the unit sphere. Its triangular base has inradius \(1\), side length \(2\sqrt3\), and area \(3\sqrt3\); the two tangent base planes are distance \(2\) apart. Its volume is therefore \(6\sqrt3\). The five displayed normals cut out exactly this prism, proving the stated coefficient.

## Verification
The proof was checked at the level of quantifiers and the only delicate interchange is avoided: no uniform pointwise density approximation is assumed over all configurations. Instead the lower bound uses the compact truncated-volume minima \(a_R\), and the upper bound uses one fixed finite-volume near-minimizer. The argument covers unbounded and degenerating configurations in the infimum.

For the explicit prism, the three equatorial tangent halfspaces form an equilateral triangle with inradius \(1\), and the two polar inequalities give a slab of height \(2\), so the volume computation \(3\sqrt3\times2=6\sqrt3\) is direct. Substitution gives \(6\sqrt3/(2\pi)^{3/2}\approx0.6598452203723182\).

## Relationship to prior work
Mulgund's 2026 paper proves the unrestricted regular-simplex stochastic domination theorem and then poses the rank-constrained distribution-function problem: for \(d\ge3\), \(n\ge d+2\), and fixed \(t>0\), minimize \(F_G(t)\) over correlation matrices of rank at most \(d\). It states that the optimal geometry is unknown except for the listed elementary cases and the three-dimensional cases with \(n=6\) and \(n=12\). In particular, the paper does not resolve \(d=3,n=5\).

The classical Lindelöf isoperimetric problem is different: it minimizes surface area or volume among polyhedra with a fixed number of faces circumscribed about the unit sphere. Modern surveys report the five-face case as proven and identify the trigonal or triangular prism. That geometric theorem supplies \(V_{3,5}\), but it does not state the Gaussian rank-constrained small-threshold limit. Conversely, the Gaussian paper formulates the fixed-threshold probability problem but does not make the uniform small-threshold reduction to minimum circumscribed volume.

Focused searches for rank-constrained Gaussian maxima, the five-direction three-dimensional case, small thresholds, pentahedra, triangular prisms, and equivalent tangent-halfspace formulations found no statement implying the theorem above. The closest database records concerned unrelated Gaussian maxima, simplex sections, and polyhedral extremal problems rather than this rank-constrained small-threshold limit.

## Limitations
The result gives only the leading asymptotic as \(t\downarrow0\). It does not solve Mulgund's fixed-positive-threshold problem, prove a rate of convergence, or characterize all asymptotically minimizing configurations. The historical five-face geometric theorem was checked through modern literature that explicitly reports the solved case rather than by re-deriving Lindelöf's nineteenth-century proof. The motivating paper also notes unpublished partial results on its rank-constrained problem; inaccessible unpublished work cannot be compared statement-by-statement and remains an originality risk.

## References
Abhijeet Mulgund, *Stochastic Domination of Gaussian Maxima by the Regular Simplex*, arXiv:2609.28452v1, first public September 23, 2026; primary MSC 60E15. See Problem 7.2 in the September 27 revision for the rank-constrained distribution-function problem.

András Lengyel, Zsolt Gáspár, and Tibor Tarnai, *The Roundest Polyhedra with Symmetry Constraints*, Symmetry 9 (2017), 41, DOI:10.3390/sym9030041. The introduction reformulates the Lindelöf problem as minimum volume for polyhedra circumscribed about the unit sphere and records the five-face case as proven.

Tibor Tarnai, Zsolt Gáspár, and András Lengyel, *From spherical circle coverings to the roundest polyhedra*, Philosophical Magazine 93 (2013), 3970–3982, DOI:10.1080/14786435.2013.800652. It reports the proven five-face solution as the trigonal prism.
