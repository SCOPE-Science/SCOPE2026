# Sharp Hausdorff regularity exponents of planar radial weighted perimeters

## Finding
Let \(K,L\) be arbitrary nonempty compact convex subsets of \(\mathbb R^2\), including segments and points. For every real \(p>-1\), define the multiplicity-corrected radial weighted perimeter
\[
\mathcal E_p(K)=\eta_K\int_{\partial K}|x|^p\,d\mathcal H^1(x),\qquad
\eta_K=\begin{cases}1,&\dim K=2,\\2,&\dim K\le1.\end{cases}
\]
For \(p=0\), the integrand is \(1\) even at the origin; a singleton has energy zero. Put \(\delta=d_H(K,L)\). The sharp global regularity-exponent phase diagram is:

1. **Singular weights.** If \(-1<p<0\), then, independently of the locations and diameters of \(K,L\),
   \[
   |\mathcal E_p(K)-\mathcal E_p(L)|\le C_p\delta^{p+1},\qquad
   C_p=2\pi(2-p)+\frac{4\pi(-p)}{p+1}.
   \]
   The exponent \(p+1\) cannot be increased even when both sets lie inside any prescribed ball about the origin.
2. **Unweighted endpoint.** If \(p=0\), then \(|\mathcal E_0(K)-\mathcal E_0(L)|\le2\pi\delta\), with optimal coefficient \(2\pi\).
3. **Nonsingular weights.** If \(p>0\) and \(K,L\subset R B_2\), where \(R>0\) and \(B_2\) is the closed Euclidean unit disk, then
   \[
   |\mathcal E_p(K)-\mathcal E_p(L)|\le 2\pi(1+\max\{1,p\})R^p\delta.
   \]
   The Lipschitz exponent \(1\) is optimal. The displayed constants for \(p\ne0\) are explicit *admissible* constants, not claimed sharp.

## Assumptions and scope
The Hausdorff metric is Euclidean, the radial weight is centered at the fixed origin, and \(p>-1\) is essential for integrability through the origin on one-dimensional convex boundaries. A segment is counted twice, the geometric limit of boundaries of thinning convex bodies. The first bound is global on all compact convex planar sets, without any circumradius bound. For \(p>0\), the fixed containing ball is essential for the stated uniform constant. No assertion concerns nonconvex boundaries, ambient dimensions other than two, or optimal values of the nonzero-power prefactors.

## Proof
**1. A local boundary-growth lemma.** For Borel sets \(A\), write \(\mu_K(A)=\eta_K\mathcal H^1(A\cap\partial K)\) and \(M_K(r)=\mu_K(B(0,r))\). For every compact convex \(K\) and \(r>0\),
\[
0\le M_K(r)\le2\pi r.\tag{1}
\]
If \(K\) is two-dimensional, the boundary arc inside the open disk belongs to the boundary of the convex intersection \(K\cap\overline B(0,r)\), up to a null set. Planar perimeter is inclusion-monotone for convex bodies, so this intersection has perimeter at most that of the disk, \(2\pi r\). If \(K\) is a segment, its length inside the disk is at most \(2r\), and the multiplicity-two measure is at most \(4r<2\pi r\); for a point it is zero. Consequently, when \(K\subset RB_2\),
\[\mu_K(\mathbb R^2)\le2\pi R.\tag{2}\]

**2. A normal-variation inequality.** First let \(K,L\) have positive smooth curvature and let \(f\) be smooth and radial, nonnegative, with \(\nabla f\) integrable over their boundaries and Minkowski interpolants. Let \(h_t=(1-t)h_K+th_L\) be the support function; write \(n=(\cos\theta,\sin\theta)\), \(\tau=(-\sin\theta,\cos\theta)\), \(x_t=h_tn+h_t'\tau\), and \(\rho_t=h_t+h_t''>0\). Then
\[
F_f(K_t)=\int_0^{2\pi}f(x_t)\rho_t\,d\theta,
\qquad\|h_L-h_K\|_{L^\infty}=\delta.
\]
Differentiating with \(v=h_L-h_K\), using \(x_t'=\rho_t\tau\), and integrating once by parts cancels the two terms containing \(v'\). This yields the exact formula
\[
\frac d{dt}F_f(K_t)=\int_0^{2\pi}v(\theta)
\bigl[f(x_t)+\rho_t\nabla f(x_t)\cdot n\bigr]d\theta.
\]
Therefore
\[
|F_f(K)-F_f(L)|\le\delta\left(2\pi\sup_{t,\theta} f(x_t)+
\sup_{0\le t\le1}\int_{\partial K_t}|\nabla f|\,ds\right).\tag{3}
\]
The same inequality follows for Lipschitz radial truncations by smooth approximation.

**3. Singular powers.** For \(-1<p<0\) and \(\varepsilon>0\), let \(f_\varepsilon(x)=\min\{|x|^p,\varepsilon^p\}\), constant on the radius-\(\varepsilon\) disk. It has supremum \(\varepsilon^p\), and \(|\nabla f_\varepsilon|=(-p)|x|^{p-1}\mathbf1_{\{|x|>\varepsilon\}}\) almost everywhere. Integration by parts against the cumulative function \(M_K\) and (1) gives
\[
\int_{\partial K}|\nabla f_\varepsilon|ds
\le 2\pi(1-p)\varepsilon^p.\tag{4}
\]
The exact truncation-error identity and (1) give
\[
0\le\mathcal E_p(K)-F_{f_\varepsilon}(K)
=(-p)\int_0^\varepsilon r^{p-1}M_K(r)\,dr
\le\frac{2\pi(-p)}{p+1}\varepsilon^{p+1}.\tag{5}
\]
Use (3)--(5) on both sets and their Minkowski interpolants. For \(\delta>0\), take \(\varepsilon=\delta\); then
\[
|\mathcal E_p(K)-\mathcal E_p(L)|
\le2\pi(2-p)\delta^{p+1}+\frac{4\pi(-p)}{p+1}\delta^{p+1}.
\]
For \(\delta=0\) the sets coincide.

**4. Nonsingular powers.** For \(p=0\), put \(f\equiv1\) in (3). For \(p>0\) and \(K\subset RB_2\), (1)--(2) and integration by parts yield
\[
\int_{\partial K}p|x|^{p-1}ds
\le\begin{cases}2\pi R^p,&0<p\le1,\\2\pi pR^p,&p\ge1.\end{cases}\tag{6}
\]
Indeed, for \(0<p<1\), integrate \(r^{p-1}\) against \(dM_K(r)\) and bound \(M_K(r)\le2\pi r\); for \(p\ge1\), use \(p|x|^{p-1}\le pR^{p-1}\) and (2). The support interpolation remains in \(RB_2\); (3) with \(\sup_{t,\theta} f(x_t)\le R^p\) proves the claimed coefficient. For \(p=0\) the same argument gives exactly \(2\pi\delta\).

**5. General convex sets and sharp exponents.** Approximate arbitrary compact convex sets by smooth strictly convex outer approximants; the support functions converge uniformly, and the multiplicity-corrected boundary measures converge weakly. For \(-1<p<0\), (5) controls the singular remainder uniformly, establishing convergence of the actual weighted energies; for \(p\ge0\), this follows from continuity of the weight on a common compact ball. Thus (1)--(6) and the asserted estimates pass to all limits, including segments and points. For sharpness, take \(K=\{0\}\) and \(L=\delta B_2\). Then \(d_H(K,L)=\delta\) and \(\mathcal E_p(L)=2\pi\delta^{p+1}\), establishing optimality of the exponent \(p+1\) for negative \(p\), and optimality of the \(p=0\) constant. To avoid degenerate sets, replace \(K\) by a disk of radius \(\delta^2\) and \(L\) by a disk of radius \(\delta\). For positive \(p\), compare disks of radii \(r\) and \(r+\delta\) for fixed \(r>0\); their energy difference is asymptotic to \(2\pi(p+1)r^p\delta\), so the exponent cannot exceed \(1\).

## Verification
The standalone standard-library program `CHECKS.py` numerically tests all three claimed regimes against exact disk formulas, verifies the degeneration normalization using the exact segment formula \(\mathcal E_p([-a,a]\times\{0\})=4a^{p+1}/(p+1)\), and compares independent mesh resolutions on a nonsingular triangular boundary. Execution returned `RADIAL_WEIGHTED_PERIMETER_FINITE_CHECKS_OK`. None of these finite tests proves the universal inequalities: the proof is steps 1--5 above. The local-growth estimate, support variation identity, singular remainder bounds and sharpness examples are independently specified and can be checked directly.

## Relationship to prior work
Csató--Giovagnoli--Roy (arXiv:2608.19851v1, first public 2026-08-20) formulate weighted perimeters with a factor two on degenerate convex bodies and announce a qualitative Hausdorff-continuity theorem. Their stated conclusions concern continuity and optimization of weights, not explicit global moduli or sharp Hölder exponents. Csató--Giovagnoli (arXiv:2610.11677v1, first public 2026-10-08) subsequently provide a qualitative continuity proof; this later paper is used only for comparison and does not set the initiating date. Hug--Schneider (arXiv:1310.1514) establish a half-Hölder result for support measures tested in a bounded-Lipschitz metric, which does not directly handle the unbounded singular weight and does not imply the phase diagram above. Saracco--Stefani (arXiv:2306.07770v1) study inclusion monotonicity of weighted perimeters, not the requested two-body Hausdorff upper modulus. The novelty assessment is conditional on the inspected literature: unindexed equivalents are possible.

## Limitations
No optimal prefactor is asserted when \(p\ne0\). No reverse estimate, geometric rigidity theorem, higher-dimensional analogue, or pointwise modulus for nonconvex curves is established. A generic bounded-Lipschitz continuity theorem alone is insufficient for the singular exponent. The result is an analytic theorem, not an independent certification; no independent scientific audit has been performed.

## References
1. G. Csató, D. Giovagnoli, P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1, 2026-08-20, https://arxiv.org/html/2608.19851v1 .
2. G. Csató, D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1, 2026-10-08, https://arxiv.org/html/2610.11677v1 .
3. D. Hug, R. Schneider, *Hölder continuity of normal cycles and of support measures of convex bodies*, arXiv:1310.1514v1, 2013-10-05, https://arxiv.org/html/1310.1514v1 .
4. G. Saracco, G. Stefani, *On the monotonicity of weighted perimeters of convex bodies*, 2024, relevant inclusion-monotonicity results, https://arxiv.org/abs/2306.07770 .
