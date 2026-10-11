# Haar-random planar projection perimeter moments of all orthotopes

## Finding
For each integer \(d\ge3\), let
\[
Q(a)=\prod_{i=1}^{d}[-a_i/2,a_i/2]\subset\mathbb R^d,
\qquad a_i>0.
\]
Let \(S\) be a Haar-uniform two-dimensional linear subspace and let \(P_a(S)\) be the Euclidean perimeter of the orthogonal projection \(\operatorname{proj}_S Q(a)\). Define the convergent generalized hypergeometric value
\[
H_d={}_3F_2\!\left(\begin{matrix}
-\frac12,\frac12,\frac32\\
1,\frac{d+1}{2}
\end{matrix};1\right)
=\sum_{k=0}^\infty\frac{(-1/2)_k(1/2)_k(3/2)_k}{(1)_k((d+1)/2)_k\,k!}.
\tag{1}
\]
Here \((z)_k\) is the rising factorial. The **exact first and second perimeter moments** are
\[
\boxed{\mathbb E[P_a(S)]=
\sqrt\pi\frac{\Gamma(d/2)}{\Gamma((d+1)/2)}\sum_{i=1}^d a_i,}
\tag{2}
\]
\[
\boxed{\mathbb E[P_a(S)^2]=
\frac8d\sum_{i=1}^d a_i^2+
\frac{4\pi H_d}{d-1}\sum_{1\le i<j\le d}a_i a_j.}
\tag{3}
\]
Subtracting the square of (2) gives the exact variance for every orthotope.

For the unit cube \(Q_d=Q(1,\ldots,1)\),
\[
\mathbb E[P_d^2]=8+2\pi dH_d,
\qquad
\operatorname{Var}(P_d)=8+2\pi dH_d-
\pi d^2\left(\frac{\Gamma(d/2)}{\Gamma((d+1)/2)}\right)^2.
\tag{4}
\]
In dimension four,
\[
\mathbb E[P_4^2]=8+8\pi\,{}_3F_2\!\left(
\begin{matrix}-\frac12,\frac12,\frac32\\1,\frac52\end{matrix};1\right)
=28.495793565063314\ldots,
\tag{5}
\]
\[
\operatorname{Var}(P_4)=0.051349120618869645\ldots.
\]
The variance for unit cubes has the finite nonzero limit
\[
\boxed{\lim_{d\to\infty}\operatorname{Var}(P_d)
=8-\frac{5\pi}{2}=0.1460183660255\ldots.}
\tag{6}
\]

## Assumptions and scope
All projections are orthogonal and all randomness is Haar probability on \(G(d,2)\). Euclidean perimeter is measured in the projected two-plane, not ambient surface area or the planar shadow's area. The stated orthotopes are nondegenerate (all lengths positive); the same polynomial formulas extend continuously to degenerate limiting side lengths when a two-dimensional projection remains meaningful.

The theorem is a **second-moment evaluation** for the entire family \(d\ge3\), not merely an asymptotic limit. A result already known for the three-dimensional unit cube appears at \(d=3\) and is credited rather than claimed as a new special case. The first-moment part follows from classical intrinsic-volume identities; its role here is to normalize the genuinely new second moment and variance.

## Proof
Write \(e_1,\ldots,e_d\) for the standard orthonormal basis, and for each plane \(S\) set
\[
\ell_i(S)=\|\operatorname{proj}_S e_i\|_2.
\]
The projection of \(Q(a)\) is a planar zonotope: the Minkowski sum of \(d\) centered segments whose lengths are \(a_i\ell_i(S)\). The planar Cauchy perimeter integral makes perimeter additive under Minkowski sums. A line segment of length \(L\) has limiting perimeter \(2L\), hence the exact identity
\[
P_a(S)=2\sum_{i=1}^d a_i\ell_i(S).
\tag{7}
\]
By orthogonal invariance, the marginal squared projection length
\[
T=\ell_1(S)^2
\]
has a beta law
\[
T\sim\operatorname{Beta}\left(1,\frac{d-2}{2}\right).
\tag{8}
\]
In particular,
\[
\mathbb E\ell_1^2=\frac2d,
\qquad
\mathbb E\ell_1=\frac{\Gamma(3/2)\Gamma(d/2)}{\Gamma((d+1)/2)}.
\tag{9}
\]

The nontrivial step is the **pairwise correlation of projected perpendicular edges**. We establish the exact identity
\[
\boxed{\mathbb E[\ell_1\ell_2]=\frac{\pi}{2(d-1)}H_d.}
\tag{10}
\]
Conditional on \(T=t\), choose an orthonormal frame \(u,v\) of \(S\) so that
\[
u_1=\sqrt t,\qquad v_1=0.
\]
The vectors
\[
\frac{u-\sqrt t\,e_1}{\sqrt{1-t}}
\quad\text{and}\quad v
\]
form a Haar-uniform orthonormal two-frame inside \(e_1^\perp\cong\mathbb R^{d-1}\), independent of \(t\). Their \(e_2\)-coordinates have the same joint distribution as the first two coordinates \((X,Y)\) of a uniformly distributed point of the sphere in \(\mathbb R^{d-1}\). Thus, conditionally on \(T=t\),
\[
\ell_2=\sqrt{(1-t)X^2+Y^2}.
\tag{11}
\]
In polar coordinates, write \((X,Y)=R(\cos\theta,\sin\theta)\) with \(\theta\) uniform on \([0,2\pi)\) and independent of \(R\). For \(d>3\),
\[
R^2\sim\operatorname{Beta}\left(1,\frac{d-3}{2}\right);
\]
when \(d=3\) the same distributional statement holds in the limiting sense \(R=1\). In both cases,
\[
\mathbb E R=\frac{\Gamma(3/2)\Gamma((d-1)/2)}{\Gamma(d/2)}.
\tag{12}
\]
The angular average in (11) is
\[
\frac1{2\pi}\int_0^{2\pi}\sqrt{1-t\cos^2\theta}\,d\theta
={}_2F_1\!\left(-\frac12,\frac12;1;t\right).
\tag{13}
\]
Combining (8), (11)--(13), we obtain the exact beta integral
\[
\mathbb E[\ell_1\ell_2]
=\frac{\Gamma(3/2)\Gamma((d-1)/2)}{\Gamma(d/2)}
\frac{d-2}{2}
\int_0^1 t^{1/2}(1-t)^{(d-4)/2}
{}_2F_1\!\left(-\frac12,\frac12;1;t\right)\,dt.
\tag{14}
\]
Expand the Gauss hypergeometric series in (14) and integrate each term. The series is absolutely integrable for every integer \(d\ge3\): the beta weight is integrable at both endpoints, and the Gauss series is absolutely convergent at \(t=1\). Euler's beta integral gives
\[
\frac{d-2}{2}\int_0^1
 t^{1/2}(1-t)^{(d-4)/2}
{}_2F_1\!\left(-\frac12,\frac12;1;t\right)\,dt
=
\frac{\Gamma(3/2)\Gamma(d/2)}{\Gamma((d+1)/2)} H_d.
\tag{15}
\]
Multiplying by the prefactor in (14) and using
\[
\Gamma\left(\frac{d+1}{2}\right)
=\frac{d-1}{2}\Gamma\left(\frac{d-1}{2}\right),
\]
yields (10) without numerical approximation.

Expand (7), use (9) on diagonal terms and (10) on distinct indices. This gives (2) and (3), hence (4)--(5).

For (6), the defining series (1) gives
\[
H_d=1-\frac{3}{4(d+1)}+O(d^{-2}).
\tag{16}
\]
To make the error rigorous, observe that (1) can be viewed as the expectation of the analytic angular factor in (13) with \(t\) having the \(\operatorname{Beta}(3/2,(d-2)/2)\) law. In the expansion of the angular factor, the constant and linear terms are \(1-t/4\), and the sum of the absolute values of all coefficients of degree at least two is finite. This bounds the remainder in absolute value by a constant times the beta-law second moment, which is
\[
\frac{15}{(d+1)(d+3)}=O(d^{-2}).
\]
Stirling's ratio expansion also gives
\[
\left[\frac{\Gamma(d/2)}{\Gamma((d+1)/2)}\right]^2
=\frac2d\left(1+\frac1{2d}+O(d^{-2})\right).
\tag{17}
\]
Substitution into (4) yields
\[
\mathbb E[P_d^2]=2\pi d+8-\frac{3\pi}{2}+O(d^{-1}),
\qquad
\big(\mathbb E[P_d]\big)^2=2\pi d+\pi+O(d^{-1}).
\]
Their difference gives (6).

## Verification
The standalone `verify.py` implements two independent evaluations of the nontrivial pairwise moment: the generalized hypergeometric expression (10) and a high-precision numerical beta/elliptic-angle integration of (14). It checks the existing three-cube exact value, the four-cube numeric benchmark, the asymptotic trend, and the arbitrary-length quadratic-form identity for selected boxes. Separate Haar two-frame sampling checks both the second moment and the cross-edge term.

For additional geometric independence, the checker constructs the convex hull of all projected vertices in dimensions three and four and compares the hull perimeter with the zonotope identity (7). Exact symbolic equalities in the proof, not finite checks or Monte Carlo, establish the theorem for every dimension and orthotope.

## Relationship to prior work
Kabluchko, Litvak, and Zaporozhets (arXiv:1511.08479, first publicly available 26 November 2015; primary MSC 52A23) derive every moment of **one-dimensional projection length** of a cube and its high-dimensional limiting law. In their Example 3.3, the second width moment is \(1+2(d-1)/\pi\). Their Theorem 3.1 concerns random **line** widths; neither it nor the example states the second perimeter moment of a random **two-plane** projection. A one-directional width moment does not specify covariance across two distinct directions in the random plane, which is the integral explicitly evaluated in (10).

Finch's full primary text on planar projections (arXiv:1203.2464, sections 2.2, 3, and 4.2) gives the exact hypergeometric second perimeter moment for the three-cube, and explicitly records only \(28.4\ldots\) for the four-cube. It also states that general higher-moment expressions for the periwidth family were unavailable at that time. The \(d=3\) case of (4) is therefore **prior-covered**; the extension to all higher dimensions and arbitrary orthotope side lengths is the subject of the finding.

Paouris, Pivovarov, and Zinn (arXiv:1210.7012) study **two-dimensional projected area** and its large-dimensional limit via Gaussian zonotopes. Their invariant is not the boundary perimeter, and their projected-area variance does not determine the perimeter variance. They are credited for relevant Grassmannian and zonotope machinery, not used as originality evidence for our specific evaluated perimeter kernel.

Published integral-geometric and Gaussian-moment representations can reduce projected perimeter questions to expectations, but the claim here is the evaluated beta-hypergeometric correlation (10) and its exact full-family second-moment and asymptotic consequences. Searches compared this statement against periwidth, shadow perimeter, intrinsic volume, random zonotope, Gaussian projection, orthotope, and the characteristic special-function parameters.

## Limitations
The theorem is for orthotopes (rectangular boxes) with orthogonal edge directions, not arbitrary parallelotopes or arbitrary convex bodies. It evaluates the first two moments; it does not determine the full distribution or higher cumulants. The limit (6) is only a variance limit; it does not assert convergence in distribution.

The three-cube formula and one-dimensional width formulas are prior results. General moment-representation identities are also prior results. No independent historical audit is claimed. Unindexed work on random zonotopes or high-dimensional perimeter may contain equivalent special-function reductions; this is a residual originality risk, not a proof of uniqueness.

## References
1. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1 (2015), later published in Journal of Mathematical Sciences 225 (2017), 770--787. https://arxiv.org/abs/1511.08479
2. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1 (2012). https://arxiv.org/abs/1203.2464
3. G. Paouris, P. Pivovarov, and J. Zinn, *A central limit theorem for projections of the cube*, arXiv:1210.7012v2 (2012); Probability Theory and Related Fields 159 (2014), 701--719. https://arxiv.org/abs/1210.7012
4. G. Paouris and P. Pivovarov, *Small-Ball Probabilities for the Volume of Random Convex Sets*, Discrete & Computational Geometry 49 (2013), 601--646, DOI: 10.1007/s00454-013-9492-2. Only the accessible abstract and mathematical-reference description were inspected here; no assertion of noncoverage of the inaccessible full text is made.
