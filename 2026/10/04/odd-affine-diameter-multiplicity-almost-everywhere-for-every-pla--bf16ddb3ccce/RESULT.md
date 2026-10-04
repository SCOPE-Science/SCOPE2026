# Odd affine-diameter multiplicity almost everywhere for every planar body of constant width
## Finding
Let \(K\subset\mathbb R^2\) be a convex body of constant width \(w>0\). For Lebesgue-almost every \(z\in\operatorname{int}K\), the number \(N_a(K,z)\) of affine diameters of \(K\) containing \(z\) is finite and odd. Equivalently, for
\[
Q(K)=\{z\in\operatorname{int}K:N_a(K,z)<\infty\text{ and }N_a(K,z)\text{ is even}\},
\]
one has
\[
\lambda_2(Q(K))=0.
\]
The statement includes nonsmooth constant-width bodies such as Reuleaux polygons.

## Assumptions and scope
An affine diameter is a chord joining two boundary points that lie on parallel supporting lines of \(K\). The count \(N_a(K,z)\) counts geometric affine-diameter segments, not normal parameters. The theorem is planar and assumes only convexity and constant width. It does not settle the corresponding measure-zero question for arbitrary planar convex bodies.

## Proof
Write \(u(\theta)=(\cos\theta,\sin\theta)\), and let \(x(\theta)\) be the unique support point of \(K\) with outer normal \(u(\theta)\).

First, a constant-width body is strictly convex. Indeed,
\[
K-K=wB_2.
\]
For each direction \(u\), the exposed face satisfies
\[
F(K-K,u)=F(K,u)-F(K,-u).
\]
The left side is a singleton because the Euclidean disk is strictly convex. Hence \(F(K,u)\) is a singleton for every \(u\).

Let \(h\) be the support function. Constant width gives, distributionally,
\[
h(\theta)+h(\theta+\pi)=w.
\]
The curvature measures satisfy
\[
\mu+\tau_\pi\mu=w\,d\theta.
\]
Since \(\mu\) is positive, it follows that \(\mu=\rho(\theta)\,d\theta\) with \(0\le \rho\le w\) almost everywhere. Consequently \(h\in W^{2,\infty}\), the support-point parametrization \(x\) is Lipschitz, and
\[
x(\theta+\pi)=x(\theta)-w\,u(\theta).
\]

Parameterize unoriented affine diameters by the Möbius strip
\[
M=([0,\pi]\times[0,1])/\bigl((0,t)\sim(\pi,1-t)\bigr)
\]
and define
\[
\Phi([\theta,t])
=t\,x(\theta)+(1-t)x(\theta+\pi)
=x(\theta)-(1-t)w\,u(\theta).
\]
The map \(\Phi:M\to K\) is Lipschitz. Its boundary is the single loop obtained by following \(x(\theta)\) from \(\theta=0\) to \(2\pi\); therefore \(\Phi|_{\partial M}\) has winding number one around every point of \(\operatorname{int}K\). Thus the mod-\(2\) degree satisfies
\[
\deg_2(\Phi,z)=1
\qquad(z\in\operatorname{int}K).
\]

Use the standard degree-count fact for Lipschitz maps between two-dimensional manifolds: outside a null set consisting of the image of the nondifferentiability set and the image of the zero-Jacobian set, every finite fiber has cardinality congruent modulo \(2\) to the mod-\(2\) degree. Rademacher's theorem and the Lipschitz null-set property handle the first set; the area formula handles the zero-Jacobian set. At a differentiability point with nonzero determinant, differentiability gives a small-ball homotopy to the invertible derivative, so the isolated local mod-\(2\) degree is one. Summing local degrees over a finite fiber gives the global degree.

It remains to know that the fiber is finite almost everywhere. Bárány, Hug, and Schneider prove that for planar convex bodies in general relative position with their reflection, affine-diameter multiplicity is integrable. Here every exposed face of \(K\) and of \(-K\) is a singleton, so the required relative-position condition holds. Therefore \(N_a(K,z)<\infty\) for almost every \(z\in K\).

For every such nonexceptional interior point,
\[
N_a(K,z)=\#\Phi^{-1}(z)\equiv\deg_2(\Phi,z)\equiv1\pmod2.
\]
Hence \(N_a(K,z)\) is odd almost everywhere, and \(\lambda_2(Q(K))=0\).

## Verification
The proof uses no finite experiment. The critical checks are: constant width implies singleton support faces; the curvature measure is absolutely continuous with density in \([0,w]\); the diameter sweep is a Lipschitz map from a Möbius strip whose boundary winds once; the Lipschitz area formula makes the nondifferentiable and zero-Jacobian images null; and the published mean-multiplicity theorem gives finite fibers almost everywhere. These steps prove an almost-everywhere statement and do not assert pointwise finiteness at exceptional points.

## Relationship to prior work
Soltan's survey formulates the question whether the set of points lying on a finite even number of affine diameters has full-dimensional measure zero, and records smooth and polyhedral partial results. Makeev's kinematic work proves the parity conclusion under \(C^2\) smoothness and positive curvature, while his earlier constant-width work treats a piecewise-\(C^2\) setting. The present argument removes all boundary regularity assumptions within the full planar constant-width class by using the constant-width curvature-measure identity and mod-\(2\) degree on the Lipschitz diameter sweep.

Bárány, Hug, and Schneider provide the general mean-multiplicity theorem used only to guarantee finiteness almost everywhere. Their paper does not state the constant-width parity conclusion.

## Limitations
This result does not solve Soltan's measure-zero problem for arbitrary planar convex bodies. It also does not classify the exceptional null set, does not bound the odd multiplicity pointwise, and does not claim that every interior point has finitely many affine diameters. A historically relevant 2000 constant-width paper of Makeev was available only through its abstract during the comparison; the abstract specifies a piecewise-\(C^2\) class, so an unindexed formulation in its inaccessible full text remains a residual originality risk.

## References
1. I. Bárány, D. Hug, and R. Schneider, “Affine diameters of convex bodies,” arXiv:1403.7158, first version 27 March 2014.
2. V. Soltan, “Affine diameters of convex bodies—a survey,” *Expositiones Mathematicae* 23 (2005), 47–63, doi:10.1016/j.exmath.2005.01.019.
3. V. V. Makeev, “A kinematic formula for affine diameters and affine medians of a convex set,” *Zapiski Nauchnykh Seminarov POMI* 280 (2001), 264–275.
4. V. V. Makeev, “An extremal property of the Reuleaux triangle,” *Zapiski Nauchnykh Seminarov POMI* 267 (2000).
