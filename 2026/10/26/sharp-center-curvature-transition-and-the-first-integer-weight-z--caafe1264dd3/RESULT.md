# Sharp center-curvature transition and the first integer-weight zero-curvature circle for Euclidean-distance Bergman disks

## Finding
On the unit disk, equip the holomorphic Bergman space with the actual Euclidean boundary-distance weight \((1-|z|)^t\), where \(t>-1\). Denote its diagonal reproducing kernel by \(K_t(z,z)\), its Kähler coefficient by \(g_t(z)=\partial_z\partial_{\bar z}\log K_t(z,z)\), and the normalized complex-one-dimensional curvature by
\[
H_t(z)=-\frac{1}{g_t(z)}\partial_z\partial_{\bar z}\log g_t(z).
\]
The center curvature and its boundary limit are, for **every** real \(t>-1\),
\[
\boxed{H_t(0)=\frac{4(t^2+t-15)}{5(t+3)(t+4)},\qquad
\lim_{|z|\uparrow1}H_t(z)=-\frac{2}{t+2}.}
\]
In particular, center curvature is strictly increasing in \(t\) and becomes positive precisely when
\[
\boxed{t>t_c:=\frac{\sqrt{61}-1}{2}.}
\]
For all such parameters the curvature changes sign at least once between the center and the boundary. The metric is of constant curvature within this entire family **only at** \(t=0\), when \(H_0\equiv-1\).

At the **first nonnegative integer weight with positive center curvature**, \(t=4\), the zero-curvature set consists of exactly one Euclidean circle \(\{|z|=r_*\}\), with positive curvature inside and negative curvature outside. Its squared radius \(s_*=r_*^2\) is the unique zero in \((0,1)\) of
\[
\begin{aligned}
P(s)={}&147s^{12}-7308s^{11}-55818s^{10}-195804s^9-455427s^8\\
&-850584s^7-1064716s^6-850584s^5-455427s^4\\
&-195804s^3-55818s^2-7308s+147.
\end{aligned}
\]
An exact rational enclosure is \(1759/100000<s_*<1760/100000\); hence \(r_*\approx0.1326555817\). This is a classification of radial curvature signs, not a classification of off-diagonal kernel zeros.

## Assumptions and scope
Set \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and use **unnormalized** planar area measure \(dA\). The Hilbert norm is
\[
\|f\|_t^2=\int_{\mathbb D}|f(z)|^2(1-|z|)^t\,dA(z),\qquad t>-1.
\]
The metric coefficient \(g_t>0\) uses the \(\partial\bar\partial\log K_t\) convention. With the curvature convention above, the ordinary unweighted disk Bergman metric has constant curvature \(-1\); changing to the Riemannian Gaussian-curvature convention can multiply the displayed values by a fixed positive factor and does not affect any signs or thresholds. Let \(s=|z|^2\) in radial computations.

## Proof
**1. Reproducing kernel and positive metric.** Angular orthogonality and the beta integral give
\[
\|z^n\|_t^2=2\pi\mathrm B(2n+2,t+1),\qquad
K_t(z,w)=\sum_{n\ge0}\frac{\Gamma(2n+t+3)}{2\pi\Gamma(2n+2)\Gamma(t+1)}(z\overline w)^n.
\]
Completeness of monomials follows by angular Parseval and Tonelli. Positivity of \(g_t\) follows from the fact that the first two coefficient functions \(1,z\) are nonzero and orthogonal: differentiating the log of the sum of squared normalized monomials gives the positive variance of their degrees at every \(s\in[0,1)\).

**2. Exact center curvature.** Write the diagonal kernel near \(s=0\) as
\[
K_t(s)=K_t(0)[1+A_ts+B_ts^2+O(s^3)],
\qquad A_t=\frac{(t+3)(t+4)}6,\qquad
B_t=\frac{(t+3)(t+4)(t+5)(t+6)}{120}.
\]
For a radial scalar function \(h(s)\), \(\partial_z\partial_{\bar z}h(s)=(s h'(s))'\). Consequently,
\[
 g_t(s)=A_t+(4B_t-2A_t^2)s+O(s^2),\qquad
 H_t(0)=2-\frac{4B_t}{A_t^2}=\frac{4(t^2+t-15)}{5(t+3)(t+4)}.
\]
Direct differentiation gives
\[
\frac{d}{dt}H_t(0)=\frac{12(2t^2+18t+39)}{5(t+3)^2(t+4)^2}>0\qquad(t>-1).
\]
The quadratic numerator has the unique zero \(t_c=(\sqrt{61}-1)/2\) in \((-1,\infty)\).

**3. Curvature at the outer boundary and the nonconstant-curvature conclusion.** Let \(p=t+2>1\), and choose \(x\in(0,1)\) with \(x^2=s\). The binomial identity, or direct summation of the even gamma ratios, yields the already-known closed kernel formula
\[
K_t(s)=\frac{t+1}{4\pi x}[(1-x)^{-p}-(1+x)^{-p}].
\]
Near \(s=1\), the first term has a pole of order \(p\); the second is smooth. Differentiating this expression with respect to real \(s\) (including derivatives up to order four) gives
\[
 g_t(s)\sim\frac{p}{(1-s)^2},\qquad
 (s(\log g_t(s))')'\sim\frac{2}{(1-s)^2}.
\]
Indeed, the relative correction to the dominant singular term is a sum of a smooth Taylor correction and a term of size \((1-s)^p\), whose required differentiated errors are lower order because \(p>1\). Therefore \(\lim_{s\uparrow1}H_t(s)=-2/p\). For \(t>t_c\), the opposite center and boundary signs and radial continuity force at least one zero-curvature circle. Moreover the difference between center and boundary curvatures factors exactly:
\[
H_t(0)+\frac2{t+2}=\frac{2t(t+1)(2t+9)}{5(t+2)(t+3)(t+4)}.
\]
On \(t>-1\) this vanishes only at \(t=0\); hence every other family member has nonconstant curvature. At \(t=0\), \(K_0(s)\) is proportional to \((1-s)^{-2}\), so \(H_0\equiv-1\).

**4. The unique curvature-zero circle at the first integer transition.** The nonnegative integers \(0,1,2,3\) lie below \(t_c\), while \(4>t_c\). At \(t=4\), the diagonal kernel is a positive constant times \((3s^2+10s+3)/(1-s)^6\). Differentiation produces
\[
 g_4(s)=\frac{12R(s)}{(1-s)^2(s+3)^2(3s+1)^2},\quad
 R(s)=7s^4+28s^3+58s^2+28s+7,
\]
and, exactly,
\[
 H_4(s)=\frac{P(s)}{6R(s)^3}.
\]
The denominator is strictly positive for \(0\le s<1\), while \(P(0)=147>0\) and \(P(1)=-4194304<0\). Moreover, \(P'(s)<0\) for \(0<s<1\): every coefficient of \(P'\) is negative except the positive leading contribution \(1764s^{11}\), and this is strictly dominated by the contribution \(-80388s^{10}\) because \(s<1\). Thus \(P\) has precisely one zero in \((0,1)\), is positive before it, and is negative after it. Direct exact-rational substitution gives \(P(1759/100000)>0>P(1760/100000)\), proving the displayed enclosure and uniqueness without inference from numerics.

## Verification
The standalone script `curvature_phase_check.py` uses symbolic rational arithmetic to confirm the Taylor-coefficient identity, monotonicity and center/boundary difference, the exact rational weight-four metric and curvature expressions, the sign values and rational enclosure, and the derivative sign certificate. It reports `PASS` when these finite algebraic checks hold. The all-real-parameter statement and outer-boundary limit rely on the analytic proof, not on finite sampling.

## Relationship to prior work
Marinescu and Xing (2026) establish parameter analyticity for Euclidean boundary-distance weighted Bergman kernels on smooth pseudoconvex domains; the disk is a concrete specialization. A previously published disk computation gives the complete closed kernel formula above and the unrelated sharp **Lu Qi-Keng zero-freeness transition** at \(t=2\). The kernel formula is explicitly used here as prior input; neither that formula nor its off-diagonal zero classification is claimed as new. The present claim concerns the different invariant \(H_t\): its global-parameter center sign boundary \(t_c>2\), sharp boundary limit, constant-curvature rigidity, and a complete radial sign classification at the first integer parameter above \(t_c\). Yoo's 2024 and 2026 treatments provide curvature conventions and weighted Bergman metric context, but not this Euclidean-distance disk curvature phase analysis.

## Limitations
No radial sign classification is asserted for every real parameter \(t\); away from \(t=4\) the theorem only guarantees **existence** of a curvature-zero circle when \(t>t_c\). The curvature is the specified one-dimensional complex curvature, not a curvature statement for all smooth pseudoconvex domains. The already-known closed kernel formula permits differentiating to recover parts of the result, so priority for elementary consequences of that formula remains a substantive residual originality risk. The uniqueness of the \(t=4\) sign-changing circle additionally requires a strict polynomial sign argument. There has been no independent audit.

## References
1. G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258v1, first posted 2026-09-21. https://arxiv.org/abs/2609.24258.
2. *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels*, research record published 2026-10-11. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-lu-qi-keng-transitions-for-euclidean-boundary-distance-wei--b68d363f03d0.
3. S. Yoo, *Boundary Behavior of Bisectional Curvatures for Weighted Bergman Metrics*, arXiv:2605.17702, 2026. https://arxiv.org/abs/2605.17702.
4. S. Yoo, *Invariant Weighted Bergman Metrics on Domains*, arXiv:2406.19588, 2024. https://arxiv.org/abs/2406.19588.
