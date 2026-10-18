# Exact Gaussian improvement probabilities and quartic-root thresholds for a one-probe Nyström spectral preconditioner

## Finding

Let \(m\ge1\), \(\lambda>\mu>0\), and \(A=\operatorname{diag}(\lambda,\mu I_m)\). Form \(H=I_{m+1}+A\). Given any nonzero \(\omega\in\mathbb R^{m+1}\), use the rank-one Nyström approximation
\[
N=A\omega(\omega^{\mathsf T}A\omega)^{-1}\omega^{\mathsf T}A,
\qquad P=(I_{m+1}+N)^{-1}.
\]
Write \(h_1=1+\lambda\), \(h_2=1+\mu\) and \(t=\omega_1^2/\sum_{j=2}^{m+1}\omega_j^2\). When both numerator and denominator are positive, the entire spectrum of \(P^{1/2}HP^{1/2}\) consists of one eigenvalue \(1\), one eigenvalue
\[
K(t)=\frac{h_1h_2(\lambda t+\mu)}{\lambda h_1t+\mu h_2},
\]
and \(m-1\) copies of \(h_2\). In particular the spectral condition number is \(K(t)\), a strictly decreasing function of \(t>0\), with \(h_2<K(t)<h_1\). The exceptional Gaussian-zero events have probability zero; the formula extends continuously to the two endpoints.

The unpreconditioned condition number is \(\kappa_0=h_1/h_2\). If \(h_1\le h_2^2\), **no** nondegenerate one-probe sketch improves \(\kappa_0\). If \(h_1>h_2^2\), strict improvement occurs **exactly** when
\[
t>t_*=\frac{\mu^2h_2}{\lambda(h_1-h_2^2)}.
\]
Suppose the coordinates of \(\omega\) are independent centered Gaussians with a positive top-to-bulk variance ratio \(r=v_1/v_2\), meaning covariance \(\operatorname{diag}(v_1,v_2I_m)\). Then, for \(h_1>h_2^2\), the exact improvement probability at every finite \(m\) is
\[
p_m(r)=1-I_{t_*/(t_*+r)}\left(\frac12,\frac m2\right),
\]
where \(I_z(a,b)\) is the regularized incomplete beta function; it is zero if \(h_1\le h_2^2\). In the improvement-possible regime it increases strictly with \(r\). Thus isotropic Gaussian, covariance-informed Gaussian (covariance \(A+A^2\)), and one-power Gaussian (\(\omega=Ag\) with \(g\sim\mathcal N(0,I)\)) have respective ratios
\[
r_0=1,\qquad r_{\mathrm{EDA}}=\frac{\lambda(1+\lambda)}{\mu(1+\mu)},\qquad r_{\mathrm{pow}}=\left(\frac\lambda\mu\right)^2
\]
and strictly ordered improvement probabilities
\[
p_m(r_0)<p_m(r_{\mathrm{EDA}})<p_m(r_{\mathrm{pow}}).
\]

A dimension-dependent sharp transition separates these options. Fix \(\mu>0\), take \(m\to\infty\) and \(\lambda_m\to\infty\), and denote the standard normal cumulative distribution function by \(\Phi\). At \(\lambda_m=c m^{1/4}\) for any fixed \(c>0\),
\[
p_m(r_{\mathrm{EDA}})\longrightarrow
2\Phi\!\left(-\frac{\mu^{3/2}(1+\mu)}{c^2}\right),\qquad
p_m(r_{\mathrm{pow}})\longrightarrow
2\Phi\!\left(-\frac{\mu^2\sqrt{1+\mu}}{c^2}\right),
\]
whereas \(p_m(r_0)\to0\). At \(\lambda_m=c m^{1/2}\),
\[
p_m(r_0)\longrightarrow
2\Phi\!\left(-\frac{\mu\sqrt{1+\mu}}c\right),\qquad
p_m(r_{\mathrm{EDA}}),p_m(r_{\mathrm{pow}})\longrightarrow1.
\]
More generally, for either covariance-informed or one-power sketch the probability tends to zero when \(\lambda_m=o(m^{1/4})\) and to one when \(\lambda_m/m^{1/4}\to\infty\); for the isotropic sketch the corresponding scale is \(m^{1/2}\). These statements assume \(\lambda_m\to\infty\) and fixed \(\mu\).

## Assumptions and scope

All matrices are finite-dimensional, real, and positive definite; \(m\) is any positive integer and \(\lambda>\mu>0\). The preconditioner is the **unscaled inverse of \(I+N\)**, equivalent to the spectral limited-memory choice \(\theta=1\) for the approximate Nyström eigenspace. It is not an optimization over the preconditioner's scaling \(\theta\). The Gaussian sketch is independent of the matrix and is not subsequently selected or rejected using data. The metric is the exact spectral \(2\)-condition number of the symmetrically preconditioned Hessian, not a fixed-step or finite-time iterative convergence bound. The bulk eigenvalue is strictly positive, unlike idealized low-rank-only residuals.

## Proof

**Block reduction and spectral identity.** Let \(x=\omega_1\) and \(y=\|\omega_{2:m+1}\|_2\). For \(x,y>0\), an orthogonal rotation of the bulk coordinates reduces the nontrivial matrix pair to the plane spanned by the top coordinate and the normalized bulk component. On its orthogonal complement, \(N=0\) and \(H=h_2I\). In the plane, the Nyström matrix is rank one and satisfies \(0\preceq N\preceq A\), because \(N=A^{1/2}qq^{\mathsf T}A^{1/2}\) with \(q=A^{1/2}\omega/\|A^{1/2}\omega\|_2\). The residual \(A-N\) has rank one in the plane. Thus
\[
(I+N)^{-1/2}H(I+N)^{-1/2}
=I+(I+N)^{-1/2}(A-N)(I+N)^{-1/2}
\]
has eigenvalue \(1\); its other eigenvalue equals \(\det(H)/\det(I+N)\) on this plane. The determinant lemma gives
\[
\det(I+N)=1+\operatorname{tr}N
=\frac{\lambda h_1x^2+\mu h_2y^2}{\lambda x^2+\mu y^2}.
\]
This yields the stated \(K(t)\) and the remaining \(h_2\) eigenvalues. Direct differentiation gives
\[
K'(t)=\frac{h_1h_2\lambda\mu(h_2-h_1)}{(\lambda h_1t+\mu h_2)^2}<0.
\]
Its endpoint limits are \(h_1\) at \(t=0\) and \(h_2\) as \(t\to\infty\), proving the condition-number assertion and the unavoidable floor. The formula holds when \(m=1\) with no bulk-complement eigenvalues.

**Exact improvement event.** Compare \(K(t)\) with \(h_1/h_2\) and cross-multiply strictly positive denominators. The inequality is equivalent to
\[
\lambda(h_1-h_2^2)t>\mu^2h_2.
\]
If \(h_1\le h_2^2\), this is impossible; if \(h_1>h_2^2\), it is precisely \(t>t_*\).

**Gaussian law and comparisons.** Write \(\omega_1=\sqrt{v_1}X\) and the bulk entries as \(\sqrt{v_2}Y_j\) with independent standard normals. Then \(X^2\sim\chi_1^2\), \(Z=\sum_jY_j^2\sim\chi_m^2\), and \(t=rX^2/Z\). The beta-gamma identity says \(X^2/(X^2+Z)\sim\mathrm{Beta}(1/2,m/2)\); hence \(t>t_*\) if and only if that beta variable exceeds \(t_*/(t_*+r)\), proving the exact CDF. Since the beta density is strictly positive, \(p_m(r)\) increases strictly with \(r\). For \(\lambda>\mu>0\), direct positive-ratio comparisons yield \(1<r_{\mathrm{EDA}}<r_{\mathrm{pow}}\), so probability ordering follows.

**Sharp asymptotic windows.** By the strong law for independent normal-square coordinates, \(Z/m\to1\) in probability, independently of \(X\). In the improvement-possible regime the event is \(X^2>t_*Z/r\). As \(\lambda\to\infty\),
\[
t_*\sim\frac{\mu^2(1+\mu)}{\lambda^2},\qquad
r_{\mathrm{EDA}}\sim\frac{\lambda^2}{\mu(1+\mu)},\qquad
r_{\mathrm{pow}}=\frac{\lambda^2}{\mu^2}.
\]
Thus the event thresholds for \(X^2\) are asymptotic to, respectively,
\[
\frac{\mu^2(1+\mu)m}{\lambda^2},\quad
\frac{\mu^3(1+\mu)^2m}{\lambda^4},\quad
\frac{\mu^4(1+\mu)m}{\lambda^4}.
\]
At each critical scale the threshold converges in probability to the displayed positive constant; continuity of the \(\chi_1^2\) distribution gives \(\Pr\{X^2>a^2\}=2\Phi(-a)\). Below critical scales the threshold tends to infinity and the probability tends to zero; above them it tends to zero and the probability tends to one. This proves every stated limit, without replacing finite samples by a deterministic orthogonal projection.

## Verification

The companion `verify.py` independently constructs dense \(P^{1/2}HP^{1/2}\) matrices and compares their measured condition numbers with the scalar formula for randomly sampled small-dimensional inputs. It also checks finite incomplete-beta probabilities, the zero-improvement boundary, Gaussian simulation against the exact CDF, and quantitative critical-window approximations. Execution passed 1,108 finite numerical/distribution checks in a standard NumPy/SciPy environment. These are reproducibility checks, not substitutes for the analytical proof.

An illustrative instance is \(\mu=1\), \(\lambda=20\), \(m=10^4\): the finite exact beta law gives probabilities approximately \(1.89\times10^{-14}\) (isotropic), \(0.597\) (covariance-informed) and \(0.701\) (one-power). No claim is made about wall-clock cost or end-to-end EDA acceleration from this example.

## Relationship to prior work

The 2026 EDA preconditioning paper defines the spectral limited-memory framework, the Gaussian power-sketch comparator and, under stated modeling approximations, the novel right-hand-side-difference covariance \(A+A^2\). It reports algorithmic experiments and sketch quality, but its inspected Sections 3.1–3.2, numerical results, and conclusions do not state the finite beta-law for **strict condition-number improvement**, its obstruction when \(1+\lambda\le(1+\mu)^2\), or the quartic-root versus square-root success windows. Those are the claims assessed here, not the covariance construction or Nyström formula itself.

Frangella, Tropp and Udell study randomized Nyström PCG with a **different scaled preconditioner**, and prove expected condition-number guarantees at sketch ranks comparable to effective dimension. Carson and Daužickaitė analyze mixed-precision Nyström error and condition-number bounds; Giraud and Gratton study deterministic spectral-preconditioner sensitivity. None of the inspected accessible material supplies the present one-probe, two-plateau **Gaussian improvement probability** for the unscaled EDA spectral LMP. The common beta-gamma identity, rank-one determinant formula and power-sketch idea are established tools, not claimed as new separately. An equivalent result under another preconditioner parameterization remains a residual bibliographic risk.

## Limitations

This is an exact low-dimensional spectral-model benchmark with a full-rank positive bulk, not a theorem for arbitrary spectra or actual EDA Hessians. It depends on independent Gaussian coordinates and the fixed scaling \(\theta=1\). Replacing it with the paper's recommended adaptive \(\theta\), increasing sketch rank, or using a genuinely singular \(A\) changes the claim. For this two-level spectrum, exact CG solves the original and preconditioned systems in at most two distinct-eigenvalue steps in exact arithmetic, so the spectral-condition-number effect is **not** evidence for delayed or accelerated CG on this toy family. Finite experiments do not certify novelty, arbitrary-dimensional generality, floating-point stability, or real-world performance.

## References

1. Daužickaitė et al., *Accelerating an ensemble of variational data assimilations with randomized preconditioning*, arXiv:2605.23571v1, first public May 22, 2026. https://arxiv.org/abs/2605.23571
2. Frangella, Tropp, Udell, *Randomized Nyström Preconditioning*, arXiv:2110.02820, and SIAM J. Matrix Anal. Appl., DOI:10.1137/21M1466244. https://arxiv.org/abs/2110.02820
3. Carson and Daužickaitė, *Single-Pass Nyström Approximation in Mixed Precision*, SIAM J. Matrix Anal. Appl., DOI:10.1137/22M154079X. https://doi.org/10.1137/22M154079X
4. Giraud and Gratton, *On the Sensitivity of Some Spectral Preconditioners*, SIAM J. Matrix Anal. Appl., DOI:10.1137/040617546. https://doi.org/10.1137/040617546
5. Persson, Boullé and Kressner, *Randomized Nyström approximation of nonnegative self-adjoint operators*, arXiv:2404.00960. https://arxiv.org/abs/2404.00960
