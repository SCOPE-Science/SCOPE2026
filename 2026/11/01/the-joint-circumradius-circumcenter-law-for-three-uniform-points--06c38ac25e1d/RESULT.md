# The joint circumradius–circumcenter law for three uniform points in a disk

## Finding
Let \(X_1,X_2,X_3\) be independent, area-uniform points in the closed Euclidean unit disk \(B\subset\mathbb R^2\). Almost surely they are noncollinear. Write \(R>0\) for their circumradius and \(S\ge0\) for the distance of their circumcenter from the disk center. Define, for \(0\le a\le\pi\),
\[
\Phi(a)=24\left[a^2+\frac{a}{2}\sin(2a)+\cos(2a)-1\right].
\]
For \(r>0\) and \(s>0\), define the accessible half-angle
\[
\alpha(r,s)=\begin{cases}
\pi,&r+s\le1,\\
\arccos\left(\frac{r^2+s^2-1}{2rs}\right),&|r-s|<1<r+s,\\
0,&\text{otherwise}.
\end{cases}
\]
The **joint density** of \((R,S)\) with respect to \(dr\,ds\), on the entire positive quadrant, is exactly
\[
\boxed{j(r,s)=\frac{2r^3s}{\pi^2}\,\Phi\bigl(\alpha(r,s)\bigr).}
\]
In particular, the full marginal circumradius density is the one-dimensional, nonoscillatory quadrature
\[
\boxed{f_R(r)=24r^3(1-r)_+^2+\frac{2r^3}{\pi^2}
\int_{|1-r|}^{1+r}s\,\Phi\!\left(\arccos\frac{r^2+s^2-1}{2rs}\right)ds,\qquad r>0,}
\]
where \((z)_+=\max\{z,0\}\). This gives the previously unresolved contribution of triangles whose circumcircle *crosses* the boundary of the sampling disk, including the case \(0<R<1\). It does not impose containment of the full circumcircle.

## Assumptions and scope
The points are independent with the normalized two-dimensional Lebesgue probability measure on \(B=\{x\in\mathbb R^2:\|x\|_2\le1\}\). Degenerate collinear triples have probability zero. The joint density is asserted for Lebesgue-almost-every \((r,s)\in(0,\infty)^2\); the values assigned on curve boundaries and on the coordinate axes do not affect the probability law. The circumcenter is the Euclidean center of the unique circle through all three sampled points, and may be arbitrarily far outside \(B\).

## Proof
**1. Circumcircle coordinates.** Except for a null set, every ordered triple has a unique representation
\[
x_i=c+r u(\theta_i),\quad i=1,2,3,\quad c\in\mathbb R^2,\quad r>0,\quad u(\theta)=(\cos\theta,\sin\theta).
\]
The absolute six-dimensional Jacobian is
\[
\left|\frac{\partial(x_1,x_2,x_3)}{\partial(c_1,c_2,r,\theta_1,\theta_2,\theta_3)}\right|
=r^3\left|\det\bigl(u(\theta_2)-u(\theta_1),u(\theta_3)-u(\theta_1)\bigr)\right|.
\]
For a fixed circumcenter \(c\) with \(s=\|c\|\), the requirement \(x_i\in B\) restricts each angle to a common arc. If \(r+s\le1\), the entire circle is allowed. If \(|r-s|<1<r+s\), the allowed arc has half-angle \(\alpha(r,s)\) as displayed: solving \(\|c+ru\|^2\le1\) gives \(\cos\angle(-c,u)\ge(r^2+s^2-1)/(2rs)\). Outside these cases the feasible arc has zero length. Boundary tangencies are null events.

**2. Exact triple-angle integral.** Let \(\mathcal J(a)\) denote the integral of the absolute determinant over three *labeled* angles on any arc of length \(2a\), \(0\le a\le\pi\). Translation of the angular interval does not alter its value. Sorting the three angles contributes six permutations. Put \(u=(\theta_2-\theta_1)/2\), \(v=(\theta_3-\theta_2)/2\) within a sorted chamber, so \(u,v>0\), \(u+v<a\), and \(\theta_1\) ranges over an interval of length \(2(a-u-v)\). The Jacobian of the two gaps is \(4\), and the determinant equals \(4\sin u\sin v\sin(u+v)\). Consequently
\[
\mathcal J(a)=192\int_{u,v>0,\,u+v<a}(a-u-v)\sin u\sin v\sin(u+v)\,du\,dv.
\]
Using \(w=u+v\) and
\[
\int_0^w\sin u\sin(w-u)\,du=\frac12(\sin w-w\cos w),
\]
one obtains
\[
\mathcal J(a)=96\int_0^a(a-w)\sin w(\sin w-w\cos w)\,dw
=24\left[a^2+\frac a2\sin(2a)+\cos(2a)-1\right]=\Phi(a).
\]
This is a genuinely restricted-arc evaluation; replacing the arc by the full circle would incorrectly discard boundary-crossing circumcircles.

**3. Joint density.** The joint law of the three ordered sample points has constant density \(\pi^{-3}\) on \(B^3\). Integrating the Jacobian over the allowed angles yields density \(\pi^{-3}r^3\Phi(\alpha(r,s))\) with respect to \(dc\,dr\). Polar coordinates for the circumcenter contribute \(dc=s\,ds\,d\varphi\), and rotational symmetry integrates \(d\varphi\) over \(2\pi\). Therefore
\[
 j(r,s)=\frac{2r^3s}{\pi^2}\Phi(\alpha(r,s)).
\]
The transformation is one-to-one up to null degeneracies, hence the density integrates to one; no unknown normalizing constant is inserted.

**4. Circumradius marginal.** For \(0<r<1\) and \(0<s<1-r\), \(\alpha=\pi\) and \(\Phi(\pi)=24\pi^2\), so \(j(r,s)=48r^3s\). Its integral over that fully contained region is \(24r^3(1-r)^2\). For every \(r>0\), the partially intersecting region of circumcenters is \(|1-r|<s<1+r\), with \(\alpha\in(0,\pi)\). Integrating \(j\) over these two disjoint regions gives the displayed formula for \(f_R\). There is no missing circumcenter regime.

The contained-circle density integrates exactly to \(\int_0^1 24r^3(1-r)^2dr=2/5\), agreeing with the known contained-circle calculation. Integrating the full density over \(0<r<1\) gives the independently established value \(\Pr(R<1)=4-32/\pi^2\); thus the crossing-circle contribution to this event is \(18/5-32/\pi^2\), strictly positive.

## Verification
The standalone file `circumradius_geometry_verify.py` independently evaluates the restricted-arc triple integral, checks the elementary kernel at several angles, integrates the new density, compares against established exact probabilities, and uses direct quasi-Monte Carlo sampling of random triples as a separate numerical stress test. It passed 26 deterministic comparisons in the recorded execution, including \(\Pr(R<1)\approx0.757722123445\), fully contained probability \(0.4\), and noncontained subunit-radius probability \(\approx0.357722123445\). The sampling calculation does not prove the identity; Steps 1–4 supply the analytic proof. To reproduce, execute `python circumradius_geometry_verify.py` with NumPy and SciPy installed.

## Relationship to prior work
Bakó-Szabó, Besau, and Fodor [1, Section 5.2 and Remark 5.4] obtain the known part of the distribution at larger circumradii, determine \(\Pr(R<1)\), and explicitly single out the law for subunit-radius circumcircles protruding outside the disk as unresolved. The present elementary joint density and its one-dimensional marginal integral resolve this geometric gap, without claiming that all resulting antiderivatives are elementary.

Le Caër [2] obtains distributions when the entire circumsphere is contained inside the sampling ball, and investigates other cases numerically; his conditional contained-circle law does not contain the complementary boundary-crossing contribution.

A previously published analysis [3] derives the first two small-radius asymptotic coefficients for general smooth convex sampling regions from a universal circumcircle change-of-variables identity. Such a representation is compatible with the present result, but the cited finding does not evaluate the restricted-arc angular integral or state the exact joint law and full subunit-radius density. No originality is claimed for its small-radius coefficients, the classical Jacobian, or the known probability \(\Pr(R<1)\).

## Limitations
The exact joint density is elementary; the marginal is supplied as a one-dimensional definite integral rather than a completely elementary antiderivative. Historical priority is not established against inaccessible or unindexed work, including classical random-triangle literature and unpublished derivations of the same angular integral. The statement is restricted to three independent uniform planar sample points in a Euclidean disk. The numerical verification is finite and is not an independent mathematical audit.

## References
[1] A. Bakó-Szabó, F. Besau, F. Fodor, *Sylvester's four point problem for ball-convex bodies*, arXiv:2608.29975 (first public 2026-08-30), Section 5.2 and Remark 5.4. https://arxiv.org/html/2608.29975v1

[2] G. Le Caër, *Circumspheres of sets of n+1 random points in the d-dimensional Euclidean unit ball (0<n<d+1)*, Journal of Mathematical Physics 58 (2017), 053301; arXiv:1803.08484. https://arxiv.org/pdf/1803.08484

[3] *The area–perimeter signature in the small-circumradius law of a random triangle*, published mathematical research record, 2026-10-11. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-area-perimeter-signature-in-the-small-circumradius-law-of-a--1252d4f1e8f4
