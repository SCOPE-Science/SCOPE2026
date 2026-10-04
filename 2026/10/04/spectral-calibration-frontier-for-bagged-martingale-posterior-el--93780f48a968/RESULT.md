# Spectral calibration frontier for bagged martingale posterior ellipsoids
## Finding
Assume the Gaussian limit established for the bagged martingale posterior (bMGP): a centering estimator \(\widehat\vartheta_n\) satisfies
\[
\sqrt n\,(\widehat\vartheta_n-\vartheta_\star)\Rightarrow N(0,\Sigma_0),
\]
and, conditionally on the observed data, the centered bMGP satisfies
\[
\sqrt n\,(\vartheta^\dagger-\widehat\vartheta_n)\Rightarrow N(0,\Sigma_0+\Sigma_\star),
\]
with \(\Sigma_0\) positive definite and \(\Sigma_\star\) positive semidefinite. These are the covariance objects appearing in the bMGP calibration theorem of Wang, Fong, and Frazier.

Let \(\lambda_1\le\cdots\le\lambda_d\) be the eigenvalues of
\[
A=\Sigma_0^{-1/2}\Sigma_\star\Sigma_0^{-1/2},
\]
and set \(a_i=(1+\lambda_i)^{-1}\). For independent \(Z_i\sim N(0,1)\), define
\[
Q=\sum_{i=1}^d a_i Z_i^2.
\]
For a scalar radial rescaling of the centered draws,
\[
\vartheta^\dagger_\tau=\widehat\vartheta_n+\sqrt\tau\,(\vartheta^\dagger-\widehat\vartheta_n),
\]
the nominal \((1-\alpha)\) Gaussian-limit credible ellipsoid has asymptotic frequentist coverage
\[
F_Q\!\left(\tau\,\chi^2_{d,1-\alpha}\right).
\]
Therefore the unique scalar that gives exact joint coverage at the chosen level is
\[
\tau_{\mathrm E}(\alpha)=\frac{q_Q(1-\alpha)}{\chi^2_{d,1-\alpha}},
\]
where \(q_Q(1-\alpha)\) is the \((1-\alpha)\)-quantile of \(Q\).

If \(\lambda_1<\lambda_d\), then for every \(\alpha\in(0,1)\),
\[
\frac1{1+\lambda_d}<\tau_{\mathrm E}(\alpha)<\frac1{1+\lambda_1}.
\]
By contrast, every equal-tailed linear-contrast interval is asymptotically non-undercovering if and only if
\[
\tau\ge\tau_{\mathrm L}:=\frac1{1+\lambda_1}.
\]
Thus anisotropy creates a strict frontier: exact calibration of one joint ellipsoid permits more contraction than a scalar rule that protects every linear contrast. In the extreme-confidence limit,
\[
\tau_{\mathrm E}(\alpha)\longrightarrow\tau_{\mathrm L}
\qquad\text{as }\alpha\downarrow0.
\]

## Assumptions and scope
The result is asymptotic and inherits the bMGP Gaussian-limit assumptions. The centering estimator must have the stated \(N(0,\Sigma_0)\) sampling limit, the centered bMGP must have the stated \(N(0,\Sigma_0+\Sigma_\star)\) conditional limit, and covariance estimators used to construct the ellipsoid must converge to their population limits. The theorem concerns a single scalar radial post-processing of bMGP draws. It does not claim that scalar rescaling is the most general covariance calibration; matrix-valued sandwich adjustments can be strictly richer.

The first public version of the motivating bMGP paper is dated 2026-09-24. Its main calibration result is conservative because its limiting posterior covariance adds \(\Sigma_0\) to \(\Sigma_\star\). The present result asks how much of that conservatism can be removed without changing the draw directions or rerunning predictive simulations.

## Proof
Write \(C=\Sigma_0+\Sigma_\star\). After rescaling, the limiting posterior covariance is \(\tau C\). The Gaussian-limit ellipsoid is therefore
\[
\mathcal E_\tau(\alpha)=\left\{\vartheta:n(\vartheta-\widehat\vartheta_n)^\top(\tau C)^{-1}(\vartheta-\widehat\vartheta_n)\le\chi^2_{d,1-\alpha}\right\}.
\]
Under repeated sampling, \(Y=\sqrt n(\widehat\vartheta_n-\vartheta_\star)\Rightarrow N(0,\Sigma_0)\). Hence the limiting coverage event is
\[
Y^\top C^{-1}Y\le\tau\,\chi^2_{d,1-\alpha}.
\]
The generalized eigenvalues of the pair \((\Sigma_0,C)\) are \(a_i=(1+\lambda_i)^{-1}\). Orthogonal diagonalization after whitening therefore gives
\[
Y^\top C^{-1}Y\ \overset d=\ \sum_{i=1}^d a_iZ_i^2=Q.
\]
Because \(Q\) has a continuous strictly increasing distribution on \((0,\infty)\), exact coverage \(1-\alpha\) holds for exactly one positive scalar, namely \(\tau_{\mathrm E}(\alpha)=q_Q(1-\alpha)/\chi^2_{d,1-\alpha}\).

Let \(a_\max=(1+\lambda_1)^{-1}\) and \(a_\min=(1+\lambda_d)^{-1}\). Pathwise,
\[
a_\min\sum_i Z_i^2\le Q\le a_\max\sum_i Z_i^2.
\]
If \(a_\min<a_\max\), both inequalities are strict with positive probability on every nontrivial radial shell, so the corresponding positive quantiles are strictly ordered. This proves
\[
a_\min<\tau_{\mathrm E}(\alpha)<a_\max.
\]

For a nonzero contrast \(c\), the rescaled posterior-to-sampling variance ratio is
\[
r_\tau(c)=\tau\,\frac{c^\top Cc}{c^\top\Sigma_0c}.
\]
An equal-tailed Gaussian interval is asymptotically non-undercovering exactly when \(r_\tau(c)\ge1\). The Rayleigh quotient satisfies
\[
\inf_{c\ne0}\frac{c^\top Cc}{c^\top\Sigma_0c}=1+\lambda_1,
\]
so all contrasts are protected exactly when \(\tau\ge(1+\lambda_1)^{-1}=a_\max\). For anisotropic mismatch, the strict inequality \(\tau_{\mathrm E}(\alpha)<a_\max\) means that exact calibration of the joint ellipsoid necessarily sacrifices non-undercoverage in at least one generalized-eigen direction.

For the high-confidence limit, \(Q\le a_\max\chi_d^2\) gives \(q_Q(1-\alpha)\le a_\max\chi^2_{d,1-\alpha}\). Conversely, one term with coefficient \(a_\max\) gives \(Q\ge a_\max Z^2\), hence
\[
\frac{q_Q(1-\alpha)}{\chi^2_{d,1-\alpha}}\ge a_\max\frac{\chi^2_{1,1-\alpha}}{\chi^2_{d,1-\alpha}}.
\]
The ratio of the two chi-square upper quantiles tends to \(1\) as \(\alpha\downarrow0\), proving \(\tau_{\mathrm E}(\alpha)\to a_\max\).

## Verification
The accompanying `verify.py` independently evaluates a two-dimensional anisotropic example using deterministic quadrature and bisection. For \(\Sigma_0=I_2\), \(\Sigma_\star=\operatorname{diag}(0,3)\), and \(\alpha=0.05\), it obtains
\[
\tau_{\mathrm E}(0.05)\approx0.6917708845,
\]
while \(\tau_{\mathrm L}=1\). Thus no scalar contraction is safe for every linear contrast in this example, yet the nominal 95 percent joint ellipsoid can be contracted by about 30.8 percent in covariance scale and remain exactly calibrated asymptotically. The script also checks the proportional case, in which the ellipsoid and contrast scalars coincide.

The numerical check is illustrative only. The theorem is proved analytically above; numerical quadrature is not used to justify the general statement.

## Relationship to prior work
Wang, Fong, and Frazier derive the bMGP Gaussian limit with covariance \(\Sigma_0+\Sigma_\star\) and emphasize conservative calibration. Their result supplies the covariance decomposition used here, but the inspected theorem, corollary, Gaussian example, and discussion do not state the scalar joint-ellipsoid calibration quantile, the strict ellipsoid-versus-all-contrast frontier, or its high-confidence limit.

Tanaka studies scalar learning-rate calibration of generalized posterior credible sets. That work already establishes two relevant facts: calibration is level-specific in general, and one scalar can calibrate all Gaussian-limit nominal levels only when posterior and sampling covariance are proportional. Those facts are treated here as prior art, not as part of the originality claim. In the accessible full-text material inspected, Tanaka analyzes scalar contrasts and generic scalar containment calibration but does not state the bMGP-specific strict frontier between the exact joint-ellipsoid scalar and the scalar threshold required to avoid undercoverage for every linear contrast, nor the high-confidence coalescence of those two thresholds.

Huggins and Miller develop bagged posteriors and study how bootstrap sample size changes asymptotic covariance and reproducibility. That mechanism changes the bagging procedure itself; it does not imply the level-specific weighted-chi-square scalar for post-processing an already-computed bMGP.

Shaby's open-faced sandwich adjustment and later location-scale calibration work use matrix-valued transformations to match a target covariance. Those methods are broader than scalar radial contraction and can remove anisotropy when the required matrices are estimated. They therefore do not make the scalar-constrained frontier vacuous: the present statement characterizes exactly what is possible when directions and correlations are intentionally left unchanged and only one radial scale is adjusted.

Weighted chi-square limits under covariance misspecification are classical. The distributional identity for \(Q\) is not claimed as new by itself; the finding is the sharp bMGP-specific scalar calibration frontier and the strict separation between one joint ellipsoid and all linear contrasts.

## Limitations
The result is asymptotic, not a finite-sample coverage guarantee. Estimation error in \(\Sigma_0\), \(\Sigma_\star\), or the weighted-chi-square quantile is not analyzed here. A data-dependent plug-in implementation would require conditions ensuring consistent covariance and quantile estimation. Matrix-valued calibration can dominate scalar calibration when stable matrix estimation is available. The result does not alter the bMGP predictive engine and does not claim improved point estimation.

## References
1. H. Wang, E. Fong, and D. T. Frazier, “Bagged Martingale Posteriors: Calibrated Uncertainty Quantification for Predictive Resampling,” arXiv:2609.30622v1, 2026.
2. M. Tanaka, “A Theory of Bootstrap Coverage Calibration for Generalized Posterior Credible Sets,” arXiv:2606.25729v1, 2026.
3. J. H. Huggins and J. W. Miller, “Reproducible Parameter Inference Using Bagged Posteriors,” arXiv:2311.02019v1; Electronic Journal of Statistics 18, 2024.
4. S. Tamano and Y. Tomo, “Location--Scale Calibration for Generalized Posterior,” arXiv:2511.15320v1, 2025.
5. B. A. Shaby, “The Open-Faced Sandwich Adjustment for MCMC Using Estimating Functions,” Journal of Computational and Graphical Statistics 23, 2014, doi:10.1080/10618600.2013.842174.
6. B. E. Hansen, “Criterion-Based Inference Without the Information Equality: The Weighted Chi-Square Distribution,” 2021.
