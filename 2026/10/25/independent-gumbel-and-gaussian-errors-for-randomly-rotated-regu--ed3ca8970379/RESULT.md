# Independent Gumbel and Gaussian errors for randomly rotated regular polygons

## Finding
Fix an integer \(n\ge3\). Let \(P_n\) be the regular Euclidean \(n\)-gon circumscribed about the unit disk, centered at the origin, so its inradius is exactly \(1\). Independently choose \(m\ge2\) uniform planar rotations of \(P_n\), and let \(K_m\) be their intersection. Write \(A_m\) for its area and \(H_m=d_H(K_m,B_2)\) for its Euclidean Hausdorff distance from the unit disk \(B_2\). Then as \(m\to\infty\), with \(n\) fixed,
\[
\left(m^{5/2}(A_m-\mathbb EA_m),\ \frac{nm}{2\pi}\sqrt{8H_m}-\log m\right)
\ \xrightarrow{\mathrm d}\ (Z,G),
\]
where \(Z\) and \(G\) are **independent**, \(Z\sim N(0,40\pi^6/n^4)\), and \(\Pr(G\le t)=\exp(-e^{-t})\) is the standard Gumbel law. In addition,
\[
\mathbb EA_m-\pi\sim\frac{2\pi^3}{n^2m^2},\qquad
m^5\operatorname{Var}(A_m)\longrightarrow\frac{40\pi^6}{n^4}.
\]
Consequently, the random approximation has a typical worst-direction radial discrepancy of order \((\log m)^2/m^2\) but an integrated area discrepancy of order \(m^{-2}\). Their first nondegenerate centered fluctuations are independent in the joint limit.

## Assumptions and scope
All rotations are independent and Haar-uniform on \([0,2\pi)\); copies have identical centers and incircles and **are not translated**. The integer \(n\) is fixed when \(m\) tends to infinity. Areas are planar Lebesgue areas; \(d_H\) is Euclidean Hausdorff distance between compact sets. Every copied polygon contains \(B_2\), hence \(H_m=\max_{x\in K_m}(|x|-1)\). Ties among random rotation phases occur with probability zero; the exact geometric identities also hold with ties. The mean in the centered area statistic is the actual finite-\(m\) expectation, not an asymptotic approximation.

## Proof
**Circular-gap representation.** Set \(L=2\pi/n\). Each rotated polygon has outward side-normal directions \(\Theta_j+kL\), for \(0\le k<n\), where independent phases \(\Theta_j\) are uniform modulo \(L\). Sort the \(m\) phases on the circle of circumference \(L\), and denote their cyclic gaps by \(g_1,\ldots,g_m\), including any zero gaps. They sum to \(L\). Along a radial unit direction, the most restrictive supporting half-plane is the one whose normal is closest in angle; the radial support is the secant of this shortest angular distance, which does not exceed \(L/2\le\pi/3\). Integrating its square over the circular Voronoi arcs gives the **exact identities**
\[
 A_m=n\sum_{j=1}^m\tan(g_j/2),\qquad
 H_m=\sec\left(\frac12\max_jg_j\right)-1.
\tag{1}
\]
In particular, the first identity follows because each half of a circular gap contributes \(\frac12\int\sec^2t\,dt\) to the polar area integral and there are \(n\) periodic normal configurations.

**Normalized exponential gaps.** Uniform circular spacings have the exact Dirichlet representation
\[
(g_1,\ldots,g_m)\ \stackrel{\rm d}=\ \frac{L}{S_m}(E_1,\ldots,E_m),
\qquad S_m=\sum_{j=1}^mE_j,
\tag{2}
\]
where \(E_j\) are independent unit-mean exponential variables. This remains true if the cyclic indexing is anchored at one sampled phase rather than at a fixed origin. Write \(\bar E_m=S_m/m\), \(\overline{E^3}_m=m^{-1}\sum E_j^3\), and \(M_m=\max_j E_j\).

**Bulk-area fluctuations.** Taylor's theorem on the compact interval \([0,L/2]\), with \(L\le2\pi/3\), gives a universal fixed-\(n\) constant \(C\) with \(|\tan(x)-x-x^3/3|\le Cx^5\). Inserting (2) into (1), and using \(n\sum_jg_j/2=\pi\), yields
\[
 A_m-\pi=\frac{\pi^3}{3n^2m^2}\frac{\overline{E^3}_m}{\bar E_m^3}+R_m,
\qquad |R_m|\le C_n\sum_jg_j^5.
\tag{3}
\]
The Dirichlet moment formula gives \(\mathbb E(\sum_jg_j^5)^2=O_n(m^{-8})\), since its terms involve \(\mathbb E U_i^{10}=10!/(m)_{10}\) and \(\mathbb E U_i^5U_j^5=(5!)^2/(m)_{10}\), for Dirichlet coordinates \(U_j=g_j/L\). Therefore \(m^{5/2}R_m\to0\) in \(L^2\), even after centering. The law of large numbers yields \(\bar E_m\to1\) and \(\overline{E^3}_m\to6\), establishing the mean asymptotic; convergence of expectations follows from the exact Dirichlet moments. The bivariate central limit theorem for \((\bar E_m,\overline{E^3}_m)\) and the delta method for \(f(u,v)=v/u^3\) yield influence function
\[
\psi(E)=E^3-18E+12,\qquad
\mathbb E\psi(E)=0,\quad \mathbb E\psi(E)^2=360.
\]
Thus the centered area converges to \(N(0,40\pi^6/n^4)\) at rate \(m^{5/2}\). The same moment bounds and a fourth-moment bound on the bivariate averages give uniform integrability of the squared normalized area fluctuations; alternatively one may expand exact mixed Dirichlet moments of the cubic term. This proves the asserted variance limit.

**Extreme radial error.** From (1)--(2), \(H_m=\sec(LM_m/(2S_m))-1\). Since \(M_m=O_p(\log m)\), \(\bar E_m=1+O_p(m^{-1/2})\), and \(\sqrt{8(\sec(t/2)-1)}=t+O(t^3)\) as \(t\to0\),
\[
 \frac mL\sqrt{8H_m}-\log m
 =M_m-\log m+o_p(1).
\tag{4}
\]
Independence of exponentials gives \(\Pr(M_m-\log m\le t)=(1-e^{-t}/m)^m\to\exp(-e^{-t})\).

**Joint independence, not merely separate marginal limits.** Put \(F(E)=(E-1,E^3-6)\). For every fixed \(u\in\mathbb R^2\) and \(t\in\mathbb R\), let \(b_m=\log m+t\). Independence gives
\[
\mathbb E\left[e^{i\langle u,m^{-1/2}\sum_j F(E_j)\rangle}\,\mathbf1_{\{M_m\le b_m\}}\right]
=\left[\mathbb E\left(e^{i\langle u,F(E)\rangle/\sqrt m}\mathbf1_{\{E\le b_m\}}\right)\right]^m.
\tag{5}
\]
The ordinary centered characteristic-function expansion is \(1-\tfrac1{2m}u^T\Sigma u+o(m^{-1})\), where \(\Sigma\) is the covariance matrix of \((E,E^3)\). Truncating at \(b_m\) subtracts \(e^{-t}/m+o(m^{-1})\): the difference between the truncated tail expectation and the tail probability is at most \(\|u\|m^{-1/2}\mathbb E(\|F(E)\|;E>b_m)=O_t((\log m)^3m^{-3/2})=o(m^{-1})\). Consequently (5) tends to
\[
 e^{-\frac12u^T\Sigma u}\exp(-e^{-t}).
\]
The conditional characteristic-function criterion establishes joint convergence of the centered bivariate sample means and the centered maximum to **independent** multivariate normal and Gumbel limits. Applying the smooth map \(f(u,v)=v/u^3\) to the normal component, then (3)--(4), proves the claimed independent joint limit.

## Verification
Run `python verify.py` with Python 3 and only its standard library. The checker constructs rotations independently, samples the actual supporting-halfplane radial function and compares its numerical polar area to the exact circular-gap tangent sum for twelve combinations of polygon order and rotation count; it also checks first-order area and Gumbel mean scalings by simulation at several sample sizes, and verifies the exponential influence-function variance exactly from factorial moments. This run returned `VERIFY_OK 21 analytic geometric/numerical checks; influence variance 360`. These computations are supplementary, not an infinite proof; Steps 1--5 supply the analytic argument.

## Relationship to prior work
Kiss--Vidnyánszky (2014) studied unions of concentric regular polygons, including the equally spaced basic constructions. The old circle-spacing representation and univariate Gaussian or Gumbel limit mechanisms are not claimed as new. Xu (2015) studied random circumscribing polygons generated by individually random tangent directions, a different sampling mechanism from a complete regular polygon with one random shared rotation per copy; only its abstract was available. An existing result on independently rotated tangential polygons gives the exact expected intersection area and an exponential shape-memory correction, but not the joint fluctuation law. Another existing result on intersections of congruent disks centered at random points on a circle proves a related cubic-gap Gaussian area fluctuation, but its radial boundary is not a secant of angular gap and it does not state this Gaussian/Gumbel joint independence. A published Hausdorff Gumbel limit for randomly inscribed regular polygons concerns an arclength-sampled **convex hull inside** a polygon and a different, sequential, two-parameter limit. The geometric combination and independence assertion here is not a corollary of those stated conclusions without establishing a simultaneous bulk/extreme limit for one common set of random angles.

## Limitations
The result requires fixed polygon order, exact concentric equal-inradius copies, and independent uniform rotations. It is a joint asymptotic in the number of copies, not an exact finite-sample independence assertion. Central-limit and extreme-value ingredients are standard probability facts; the claim of additional content is their sharp joint geometric instantiation and independence. No Berry--Esseen rate or arbitrary convex body generalization is claimed. Earlier equivalent results about random circular spacings, even without explicit geometric wording, remain a genuine originality risk; some historical publisher full texts could not be inspected. No independent scientific audit has been performed.

## References
1. Viktor Kiss and Zoltán Vidnyánszky, “Unions of regular polygons with large perimeter-to-area ratio,” arXiv:1402.5452v1, first public 2014-02-21, *Discrete & Computational Geometry* 53 (2015), 878--889. https://arxiv.org/abs/1402.5452 ; https://arxiv.org/html/1402.5452v2
2. E. V. Koroleva and Ya. Yu. Nikitin, “U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons,” arXiv:1301.1360, first posted 2013-01-07. https://arxiv.org/abs/1301.1360
3. Wen-Qing Xu, “Random circumscribing polygons and approximations of π,” *Statistics & Probability Letters* 106 (2015), 52--57, doi:10.1016/j.spl.2015.06.026.
4. Claude Bélisle, “On the polygon generated by n random points on a circle,” *Statistics & Probability Letters* 81 (2011), 236--242.
5. “Sharp random-rotation area order and exponential shape memory for tangential polygons,” publicly accessible research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-random-rotation-area-order-and-exponential-shape-memory-fo--9cc93a56f053
6. “Exact circular-gap area laws and Gaussian fluctuations for intersecting congruent disks,” publicly accessible research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-circular-gap-area-laws-and-gaussian-fluctuations-for-inter--1c25b18e16e8
7. “Gumbel transition and second-order Hausdorff error for randomly inscribed regular polygons,” publicly accessible research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-gumbel-transition-and-second-order-hausdorff-error-for-randomly--3fe000dbc9a1
