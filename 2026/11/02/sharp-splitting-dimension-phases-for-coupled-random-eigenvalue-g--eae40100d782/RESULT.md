# Sharp splitting-dimension phases for coupled random eigenvalue gaps

## Finding

Fix an integer \(d\geq1\), a coupling ratio \(0<\theta<1\), and an \(\mathbb R^d\)-valued random vector \(X\) with bounded, compactly supported probability density \(f\) continuous at the origin, where \(f(0)>0\). Write \(R=\|X\|_2\), \(a=1-\theta^2\), \(c=a/2\), and \(S_d=2\pi^{d/2}/\Gamma(d/2)\). Consider the coupled positive spectral branches
\[
\lambda_h(X)=\sqrt{R^2+h^2},\qquad
\Delta_h(X)=\lambda_h(X)-\lambda_{\theta h}(X),\qquad h>0.
\]
For \(p>d\), let
\[
J_{p,d}(\theta)=\int_0^\infty
\bigl(\sqrt{1+t^2}-\sqrt{\theta^2+t^2}\bigr)^p t^{d-1}\,dt.
\]
This integral is finite and strictly positive. The complete moment trichotomy, valid for every fixed real \(p>0\) as \(h\downarrow0\), is
\[
\mathbb E\Delta_h^p\sim
\begin{cases}
S_df(0)J_{p,d}(\theta)h^{p+d},&p>d,\\
S_df(0)c^p h^{2p}\log(1/h),&p=d,\\
c^ph^{2p}\mathbb E R^{-p},&p<d.
\end{cases}
\tag{1}
\]
In particular, the coupled correction has the **sharp variance phase transition**
\[
\operatorname{Var}(\Delta_h)\sim
\begin{cases}
S_1f(0)J_{2,1}(\theta)h^3,&d=1,\\
S_2f(0)c^2h^4\log(1/h),&d=2,\\
c^2v h^4,&d\geq3,
\end{cases}
\qquad v=\operatorname{Var}(R^{-1})>0\quad(d\geq3).
\tag{2}
\]
The mean correction is \(S_1f(0)c h^2\log(1/h)(1+o(1))\) for \(d=1\), and \(c h^2\mathbb E R^{-1}(1+o(1))\) for \(d\geq2\).

The standardized **central fourth moment**, \(\kappa_h=\mathbb E[(\Delta_h-\mathbb E\Delta_h)^4]/\operatorname{Var}(\Delta_h)^2\), has five regimes:
\[
\kappa_h\sim
\begin{cases}
\displaystyle \frac{J_{4,1}(\theta)}{S_1f(0)J_{2,1}(\theta)^2}\,h^{-1},&d=1,\\[5pt]
\displaystyle \frac{J_{4,2}(\theta)}{S_2f(0)c^4}\,\frac{h^{-2}}{\log(1/h)^2},&d=2,\\[5pt]
\displaystyle \frac{S_3f(0)J_{4,3}(\theta)}{c^4v^2}\,h^{-1},&d=3,\\[5pt]
\displaystyle \frac{S_4f(0)}{v^2}\log(1/h),&d=4,\\[5pt]
\displaystyle \frac{\mathbb E[(R^{-1}-\mathbb E R^{-1})^4]}{v^2},&d\geq5.
\end{cases}
\tag{3}
\]
For \(N\geq2\) independent copies of \(\Delta_h\), let \(\widehat V_{N,h}\) be their unbiased sample variance. The exact identity
\[
\mathbb E\left[\left(\frac{\widehat V_{N,h}}{\operatorname{Var}(\Delta_h)}-1\right)^2\right]
=\frac1N\left(\kappa_h-\frac{N-3}{N-1}\right)
\tag{4}
\]
makes the **necessary and sufficient** sampling budgets for relative mean-square consistency explicit: along any \(h\downarrow0\) and integer \(N_h\geq2\), the expression in (4) tends to zero exactly when
\[
\begin{array}{c|c}
\text{splitting dimension}&\text{condition}\\\hline
1,3&N_hh\to\infty\\
2&N_hh^2\log(1/h)^2\to\infty\\
4&N_h/\log(1/h)\to\infty\\
\geq5&N_h\to\infty.
\end{array}
\tag{5}
\]
Thus the two-dimensional splitting case has a particularly severe relative-variance sampling barrier even though its absolute level variance decays almost quartically.

## Assumptions and scope

The parameter \(h\) is a positive gap-opening or regularization scale, not necessarily a spatial meshwidth. The same random vector is used at both levels. The support of \(f\) is compact and \(f\) is bounded and continuous at \(0\), with \(f(0)>0\); continuity away from \(0\) is unnecessary. The law is absolutely continuous, so \(R>0\) almost surely and, for every \(p<d\), \(\mathbb E R^{-p}<\infty\). For \(d\geq3\), \(v\) is finite and strictly positive because the density is positive near the origin. For \(d\geq5\), the inverse-radius fourth moment is finite.

The positive branch is an actual Hermitian eigenvalue: choose Hermitian Clifford generators \(\Gamma_1,\ldots,\Gamma_{d+1}\) with \(\Gamma_i\Gamma_j+\Gamma_j\Gamma_i=2\delta_{ij}I\), and set \(B_h(X)=\sum_{j=1}^d X_j\Gamma_j+h\Gamma_{d+1}\). Then \(B_h^2=(R^2+h^2)I\), giving the upper eigenvalue \(\lambda_h\). In the one-parameter real-symmetric case, \(B_h(x)=\begin{pmatrix}x&h\\h&-x\end{pmatrix}\). In two parameters, a Hermitian two-by-two realization uses the three Pauli matrices. The dimension \(d\) counts independent random splitting coordinates of this local normal form; it is neither the finite-element spatial dimension nor the size of \(B_h\).

## Proof

**Moment kernel.** Rationalization gives the exact nonnegative identity
\[
\Delta_h(x)=\frac{(1-\theta^2)h^2}{\sqrt{R^2+h^2}+\sqrt{R^2+\theta^2h^2}}
=h\,g(R/h),\qquad
 g(t)=\sqrt{1+t^2}-\sqrt{\theta^2+t^2}.
\tag{6}
\]
In particular, \(g(t)>0\), \(g(t)\sim c/t\) as \(t\to\infty\), and \(0\leq\Delta_h/h^2\leq c/R\) for \(R>0\). Let \(p>0\).

If \(p>d\), substitute \(x=hy\) in \(\mathbb E\Delta_h^p\); the result divided by \(h^{p+d}\) is \(\int_{\mathbb R^d}g(\|y\|)^p f(hy)\,dy\). Boundedness of \(f\) and the \(t^{-p}\) decay yield an integrable dominator on \(\mathbb R^d\), and continuity at zero yields the first branch of (1) by dominated convergence and polar coordinates.

If \(p<d\), divide (6) by \(h^2\). It converges pointwise to \(c/R\) and is dominated by \(c/R\); the \(p\)-th power of the latter is integrable. Dominated convergence yields the last branch of (1).

If \(p=d\), fix a small \(\varepsilon>0\) and split the radial integral at radii \(h\) and \(\varepsilon\). In the annulus \(h\ll R\ll\varepsilon\), (6) equals \(ch^2/R\) up to a relative error tending to zero in the interior. Continuity of \(f\) at zero gives the logarithmic integral \(S_df(0)c^d h^{2d}\int_h^\varepsilon dR/R\). The inner ball and exterior region are \(O(h^{2d})\) at fixed \(\varepsilon\), and the angular-density discrepancy can be made an arbitrarily small multiple of \(h^{2d}\log(1/h)\). Taking \(h\to0\) and then \(\varepsilon\to0\) establishes the middle branch of (1), including the coefficient. This proves (1) for all \(p>0\).

**Variance.** Apply (1) at \(p=1,2\). When \(d=1\), the squared mean is \(O(h^4\log(1/h)^2)=o(h^3)\); when \(d=2\), it is \(O(h^4)=o(h^4\log(1/h))\). For \(d\geq3\), the domination in (6) yields \(L^2\) convergence \(\Delta_h/h^2\to c/R\), so its variance divided by \(h^4\) converges to \(c^2v\). This proves (2) and the stated means.

**Fourth moments.** Expand the fourth centered moment exactly as
\[
\mathbb E\Delta_h^4-4m_h\mathbb E\Delta_h^3
+6m_h^2\mathbb E\Delta_h^2-3m_h^4,
\qquad m_h=\mathbb E\Delta_h.
\tag{7}
\]
For \(d=1,2,3,4\), apply (1) with \(p=1,2,3,4\). In each case the last three terms of (7) are lower order than the first: respectively \(h^5\), \(h^6\), \(h^7\), and \(h^8\log(1/h)\) are the leading scales. Divide by the square of (2) to obtain the first four branches of (3). For \(d\geq5\), (6) converges to \(c/R\) in \(L^4\), so centered fourth moments and variances converge after rescaling; the last branch follows. All constants are positive and finite under the hypotheses.

**Variance estimation and sharpness.** The classical fourth-moment expansion of the unbiased sample variance gives (4) exactly for every \(N\geq2\); no Gaussian approximation is used. Substituting (3) into (4) gives each necessary-and-sufficient condition in (5). Since (1)-(3) have positive finite leading coefficients, these powers and logarithms cannot be improved for the stated density class. Uniform probability in the unit ball is an explicit admissible example in every dimension. Finally, for a Clifford normal form \(B_h\) of matrix size \(m\), \(\operatorname{tr}(B_h^2)=m(R^2+h^2)\), so the corresponding trace-square level difference is the deterministic value \(m(1-\theta^2)h^2\), with zero sampling variance; this isolates the effect of selecting an individual eigenvalue branch rather than a smooth spectral invariant.

## Verification

The accompanying `verify.py` uses only the Python standard library. Execute `python3 verify.py`. It checks 175 exact-rational characteristic-polynomial identities for the one- and two-parameter Hermitian normal forms and 24 independent radial quadrature comparisons across dimensions \(1\) through \(6\) and moment orders \(1\) through \(4\). It also checks three exact-rational sample-variance identities and the one-dimensional variance and standardized fourth-moment constants. With \(\theta=1/2\), the one-dimensional integrals are \(J_{2,1}\approx0.290374807140498\) and \(J_{4,1}\approx0.0357744018751967\). For \(X\) uniform on \([-1,1]\), (3) specializes to \(\kappa_h\sim0.424281907450412/h\). These finite checks corroborate constants and normalizations; the asymptotic assertions are proved above, not inferred from numerical samples.

## Relationship to prior work

Sun and Khandelwal (first public 27 March 2026) analyze multiplicity and symmetry-adapted block diagonalization in structural eigenfrequency computations; their article motivates quantifying how a small symmetry-breaking gap affects random eigenvalue sampling, but does not study coupled moments, fourth-moment intermittency, or sample-variance budgets. Cui et al. (2024) give multilevel Monte Carlo methods for stochastic convection-diffusion eigenvalues with general bias/variance assumptions, without analyzing a local avoided-crossing normal form and its splitting-dimension transitions. Grubišić, Saarikangas and Hakula (2022) study stochastic collocation for isolated eigenspaces and exhibit deterioration for individual modes at crossings; their results do not specify the rates or the sampling-budget phase diagram (1)-(5). Dölz and Ebert (2022/2024) characterize stochastic perturbations of multiple eigenpairs, eigenspace alignment, and Monte Carlo estimates of means/covariances; their full-text perturbation and sampling analysis does not provide the coupled gap-scale moment or relative sample-variance budget. Standard regular-variation/dominated-convergence arguments are used, not claimed as novel. The contribution is the joint sharp spectral-gap, variance, fourth-moment and necessary/sufficient sample-size classification in this explicit coupling model.

## Limitations

The theorem concerns the precise Clifford avoided-crossing model with an additive gap scale and *common-random-number* level coupling; it is not a general claim about finite-element mesh errors, arbitrary matrix perturbations, non-Hermitian exceptional points, or nonlinear eigenvalue tracking. A density vanishing or singular at the degeneracy, noncompact/heavy-tailed sampling, a scale-dependent coupling ratio, or a nonidentical level coupling can change the exponents. The fourth-moment conclusion controls relative mean-square accuracy of the sample variance, not a central limit theorem or computational wall-clock complexity. The literature comparison cannot rule out older equivalent formulations of the radial moment lemma or special normal forms; independent verification of historical priority remains outstanding.

## References

1. Shiyao Sun and Kapil Khandelwal, "Application of Group-Theoretical Approaches in Structural Natural Frequency Analyses," *International Journal for Numerical Methods in Engineering* 127 (2026), e70308. First published 27 March 2026. https://doi.org/10.1002/nme.70308
2. Tiangang Cui, Hans De Sterck, Alexander D. Gilbert, Stanislav Polishchuk, and Robert Scheichl, "Multilevel Monte Carlo Methods for Stochastic Convection–Diffusion Eigenvalue Problems," *Journal of Scientific Computing* 99 (2024), article 77, published 3 May 2024. https://doi.org/10.1007/s10915-024-02539-9
3. Luka Grubišić, Mikael Saarikangas, and Harri Hakula, "Stochastic collocation method for computing eigenspaces of parameter-dependent operators," *Numerische Mathematik* 153 (2023), 85–110, first published 22 December 2022. https://doi.org/10.1007/s00211-022-01339-3
4. Jürgen Dölz and David Ebert, "On Uncertainty Quantification of Eigenvalues and Eigenspaces with Higher Multiplicity," *SIAM Journal on Numerical Analysis* 62 (2024), 422–451; arXiv first posted 17 October 2022. https://arxiv.org/abs/2210.09089; https://doi.org/10.1137/22M1529324
