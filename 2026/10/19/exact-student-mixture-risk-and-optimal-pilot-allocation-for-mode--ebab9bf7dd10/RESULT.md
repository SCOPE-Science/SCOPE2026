# Exact Student-mixture risk and optimal pilot allocation for model-assisted gradients

## Finding

**Theorem (finite-population Gaussian pilot law).** Let \(p\ge 1\), \(N>B\ge p+3\) be integers. Independently generate \(X_i\sim N_p(0,I_p)\), \(\varepsilon_i\sim N(0,\sigma^2)\), for \(1\le i\le N\), where \(\sigma>0\). Fix \(\beta\in\mathbb R^p\) and define scalar per-example gradients \(g_i=\beta^{\mathsf T}X_i+\varepsilon_i\). All covariates \(X_i\) are available cheaply; the true finite-population gradient is \(G=N^{-1}\sum_i g_i\).

Draw a uniform pilot of \(a\) distinct examples, \(p\le a\le B-1\), fit a **no-intercept, unregularized** ordinary least-squares model \(\widehat\beta\) to the pilot gradients, and independently sample \(b=B-a\) distinct examples uniformly without replacement from the complement. Use the corresponding model-assisted difference estimator defined below. Put
\[
\nu=a-p+1,\qquad
\gamma=\frac{(N-a)(N-B)}{N^2(B-a)}.
\]
The estimator is conditionally design-unbiased given the entire finite population and the pilot. Under the joint Gaussian data law and the sampling design, its error has the **exact** representation
\[
\boxed{\widehat G-G\ \stackrel{d}{=}\ \sigma\sqrt\gamma\,Z\sqrt{1+V/U},}
\]
where \(Z\sim N(0,1)\), \(V\sim\chi^2_p\), and \(U\sim\chi^2_\nu\) are mutually independent.

For every real \(q>0\), the absolute \(q\)-th error moment is finite **if and only if** \(q<\nu\), and in this range it equals
\[
\boxed{
(\sigma\sqrt\gamma)^q
\frac{2^{q/2}\Gamma((q+1)/2)}{\sqrt\pi}
\frac{\Gamma((\nu-q)/2)\Gamma((\nu+p)/2)}
{\Gamma(\nu/2)\Gamma((\nu+p-q)/2)}.}
\]
In particular, the second moment is infinite for \(a=p\) or \(a=p+1\), even though the OLS fit and individual estimator are finite almost surely. For \(a\ge p+2\),
\[
\boxed{\mathbb E(\widehat G-G)^2
=\sigma^2\frac{(N-a)(N-B)}{N^2(B-a)}
\frac{a-1}{a-p-1}.}
\]

For comparison, a simple random sample of \(B\) gradients, with the same number of gradient evaluations, has unconditional mean-square error
\[
R_{\mathrm{plain}}=\frac{N-B}{NB}(\|\beta\|^2+\sigma^2).
\]
Writing \(s=\|\beta\|^2/\sigma^2\) and
\[
C_N(a)=\frac{B(N-a)(a-1)}{N(B-a)(a-p-1)},
\]
this pilot-and-correction estimator beats the plain mini-batch **if and only if** \(s>C_N(a)-1\). A finite-risk pilot allocation exists which beats plain sampling **if and only if**
\[
\boxed{s>\min_{a\in\{p+2,\ldots,B-1\}}C_N(a)-1.}
\]
This is a strict comparison of unconditional gradient-estimation risk, not of optimizer trajectory or runtime.

The minimum over integer pilot sizes is exactly determined by two neighbors of a real threshold. With \(L=N-1\), \(c=B-1\), define
\[
t_* = \frac{pcL}{pc+\sqrt{pc(L-c)(L-p)}},\qquad a_*=1+t_*.
\]
The minimizing integer pilot sizes belong to the feasible values obtained by clipping \(\lfloor a_*\rfloor\) and \(\lceil a_*\rceil\) to \([p+2,B-1]\) and retaining those attaining the smaller \(C_N\) (possibly a tie). In the large-population real-valued relaxation \(N\to\infty\) with \(p,B\) fixed, the optimum and risk-ratio lower envelope are
\[
\boxed{a_*\longrightarrow1+\sqrt{p(B-1)},\qquad
\inf_{p+1<a<B}\lim_{N\to\infty}C_N(a)
=\frac{B}{(\sqrt{B-1}-\sqrt p)^2}.}
\]
For fixed \(p\) and \(B\to\infty\) with \(N/B\to\infty\), the optimal integer pilot size is asymptotic to \(\sqrt{pB}\), and the signal-to-noise threshold is asymptotic to \(2\sqrt{p/B}\).

## Assumptions and scope

The theorem is a fixed-iterate, scalar-gradient test model for the two-stage model-assisted estimator; it is not a claim about the original paper's regularized kernel implementation. There is no intercept and no regularization in this specialization. The pilot and the correction sample are disjoint, uniformly chosen without replacement, and use a total of exactly \(B\) gradient evaluations. The target \(G\) is the **realized finite-population mean**, not the superpopulation expectation. Design-unbiasedness is conditional on the finite population and the randomly selected pilot; the displayed moment and risk identities further average over the Gaussian superpopulation. When \(a<p\) the specified unregularized full-column-rank OLS fit is not defined and is outside the theorem. The data model permits arbitrary fixed \(\beta\) and any \(\sigma>0\). The Gaussian covariates are assumed observed without expensive gradient evaluations.

With pilot index set \(I_1\), remaining set \(J\) of size \(M=N-a\), and correction set \(I_2\subset J\) of size \(b=B-a\), let \(\widehat g_i=\widehat\beta^{\mathsf T}X_i\). The estimator is explicitly
\[
\widehat G=\frac1N\left(
\sum_{i\in I_1}g_i+
\sum_{i\in J}\widehat g_i+
\frac{M}{b}\sum_{i\in I_2}(g_i-\widehat g_i)
\right).
\]

## Proof

**1. Conditional design identity.** Once the pilot and the entire finite population are fixed, put \(e_i=g_i-\widehat g_i\) for \(i\in J\), \(\overline e_J=M^{-1}\sum_{i\in J}e_i\). Direct subtraction gives
\[
\widehat G-G=\frac{M}{N}
\left(\frac1b\sum_{i\in I_2}e_i-\overline e_J\right).
\]
Simple random sampling of \(b\) elements of \(J\) has zero-centered error and conditional design variance
\[
\operatorname{Var}_{I_2}(\widehat G-G\mid I_1,X,g)
=\frac{M(M-b)}{N^2b}\,S_J^2,
\qquad S_J^2=\frac1{M-1}\sum_{i\in J}(e_i-\overline e_J)^2.
\]
Here \(M\ge b+1\ge2\) because \(N>B\). This proves conditional unbiasedness and the finite-population correction.

**2. Gaussian reduction.** Put \(\delta=\widehat\beta-\beta\). Conditional on the pilot, the nonpilot residuals \(e_i=\varepsilon_i-\delta^{\mathsf T}X_i\), \(i\in J\), are independent centered Gaussians of variance \(\sigma^2+\|\delta\|^2\). The signed sampling-difference coefficients of these residuals have squared sum \(M(M-b)/(N^2b)=\gamma\), for every correction set \(I_2\). Therefore, conditional on the pilot, \(\widehat G-G\) is exactly \(N(0,\gamma(\sigma^2+\|\delta\|^2))\), yielding an independent standardized Gaussian factor \(Z\).

**3. Pilot distribution.** The \(a\)-by-\(p\) Gaussian pilot design matrix \(X_1\) has full column rank almost surely since \(a\ge p\). Conditional on \(X_1\),
\[
\delta\sim N_p(0,\sigma^2(X_1^{\mathsf T}X_1)^{-1}).
\]
For any unit vector \(u\), orthogonally rotate the design columns so that \(u\) is the first coordinate. The Schur complement gives
\[
[u^{\mathsf T}(X_1^{\mathsf T}X_1)^{-1}u]^{-1}
=x^{\mathsf T}(I-P_{X_{-}})x\sim\chi^2_{a-p+1},
\]
where \(x\) is independent of the remaining \(p-1\) columns and the orthogonal complement has rank \(a-p+1\). Consequently every unit projection of \(\delta\) has the law \(\sigma Z_1/\sqrt U\), where \(Z_1\sim N(0,1)\) and \(U\sim\chi^2_\nu\) are independent. By the Cramér–Wold theorem, the **whole vector** has the representation
\[
\delta\stackrel d=\sigma W/\sqrt U,
\quad W\sim N_p(0,I_p),\quad U\sim\chi^2_\nu\text{ independent}.
\]
This derivation also establishes the critical low-degree-of-freedom behavior without treating fitted and correction samples as dependent.

**4. Error law and every moment.** Substitute \(\|\delta\|^2/\sigma^2\stackrel d=V/U\), with \(V=\|W\|^2\sim\chi^2_p\), into step 2. Since \(U/(U+V)\sim\operatorname{Beta}(\nu/2,p/2)\), the required absolute moment equals the product of the usual absolute normal moment and an inverse beta moment. Integrating the beta density gives the displayed gamma-function formula for \(q<\nu\). For \(q\ge\nu\), the beta density near zero is a positive multiple of \(v^{\nu/2-1}\), while the integrand is \(v^{-q/2}\); the integral diverges. In particular, the second moment reduces to the stated expression when \(\nu>2\), and is infinite otherwise.

**5. Comparison and optimal budget split.** A uniform size-\(B\) simple random sample has conditional design variance \((1-B/N)S_g^2/B\), where \(S_g^2\) is the realized unbiased sample variance of all \(g_i\). Averaging over the Gaussian law gives \(\mathbb ES_g^2=\sigma^2+\|\beta\|^2\). Division of the two finite mean-square errors yields \(R_{\mathrm{assisted}}/R_{\mathrm{plain}}=C_N(a)/(1+s)\), proving the exact strict improvement criterion.

For the real pilot relaxation write \(t=a-1\), \(L=N-1\), \(c=B-1\). Apart from a positive constant, minimizing \(C_N\) is minimizing
\[
f(t)=\frac{(L-t)t}{(c-t)(t-p)},\qquad p<t<c.
\]
The sign of \(f'(t)\) equals that of
\[
P(t)=(L-c-p)t^2+2pc\,t-pcL.
\]
Now \(P(p)=p(p-c)(L-p)<0\) and \(P(c)=c(c-p)(L-c)>0\). On \((p,c)\) the derivative \(P'(t)=2(L-c-p)t+2pc\) is positive: if \(L-c-p\ge0\) this is immediate; otherwise it is at least \(2(L-c-p)c+2pc=2c(L-c)>0\). Thus the unique root in \((p,c)\) is the unique continuous minimum. Solving its quadratic equation and rationalizing gives \(t_*\). The integer minimizer therefore lies among the feasible neighbors of \(a_*\). Finally let \(N\to\infty\): \(t_*\to\sqrt{pc}\). At this value the limiting risk ratio is \(B/(\sqrt c-\sqrt p)^2\). If \(p\) is fixed while \(B\to\infty\), rounding affects only smaller-order terms, giving the stated asymptotic pilot size and signal threshold. This completes the proof.

## Verification

The included `verify.py` independently enumerates finite-population correction subsamples with rational arithmetic, checks design unbiasedness and exact conditional variance, tests the closed-form integer minimizer against exhaustive candidate enumeration, checks gamma-function moment reductions, and simulates Gaussian pilots with their actual OLS fits and correction samples. It passed **4,675 checks** on Python with NumPy installed. These tests supplement rather than replace the proof; the infinite-moment boundary is established analytically, not experimentally.

To reproduce, place `verify.py` next to this file and run `python verify.py`; Python standard library suffices for rational checks, and NumPy activates the Gaussian simulations. No network calls or additional datasets are required.

## Relationship to prior work

Pohjankukka and Heikkonen (2026) introduce the pilot-trained, model-assisted difference-gradient architecture and its design-unbiasedness, using kernel ridge regression in their experiments. The exact Gaussian OLS pilot distribution, all-moment transition, finite-population risk and risk-optimal split derived here are not claims made in their accessible manuscript. Classical inverse-Wishart, Student and Horvitz–Thompson identities are proof ingredients, not claimed inventions. Blanchet, Chen, Lu, and Ying (2023) study nonparametric regression-adjusted control variates for Sobolev moment estimation and minimax rates; their setting and conclusions do not contain this finite-population Gaussian OLS law. Stanley et al. (2026) study pilot-covariance uncertainty in multifidelity Monte Carlo, not this pilot-trained regression difference estimator. Sanguiao Sande and Zhang (2020 preprint; 2021 journal) already prove the exactly design-unbiased single-split estimator in their Eq. (1), including pilot-trained weighted OLS; Riaño (2026) explicitly identifies that estimator and distinguishes it from a differently weighted partition-trained model-assisted estimator, whose variance is decomposed for arbitrary algorithms. Neither inspected treatment supplies the stated Gaussian OLS radial law, its moment threshold or the sharp budget split. Earlier survey regression and model-assisted sampling literature creates a residual possibility that an equivalent finite-sample specialization has previously appeared; no unconditional novelty guarantee is asserted.

## Limitations

The distribution law relies on independent isotropic Gaussian covariates, homoscedastic Gaussian residuals, scalar fixed-iterate gradients, a disjoint uniform two-stage design and unregularized no-intercept OLS. The actual 2026 experiments employ kernel ridge regression, for which these divergence thresholds cannot be transferred without a separate argument. If features are not available cheaply, evaluating every \(\widehat g_i\) may impose extra cost not represented by the count of gradient observations. No algorithm-wide optimization rate, generalization benefit, wall-clock advantage or non-Gaussian tail guarantee is proved. All reported risk comparisons are **unconditional superpopulation averages** against a **realized finite-population target**, not conditional guarantees for every dataset.

## References

1. J. Pohjankukka and J. Heikkonen, *Stochastic Gradient Optimization with Model-Assisted Sampling*, arXiv:2606.27171, first submitted 2026-06-25. https://arxiv.org/abs/2606.27171
2. J. Blanchet, H. Chen, Y. Lu, and L. Ying, *When can Regression-Adjusted Control Variates Help? Rare Events, Sobolev Embedding and Minimax Optimality*, arXiv:2305.16527, 2023. https://arxiv.org/abs/2305.16527
3. M. Stanley, T. Coons, G. Bomarito, P. Leser, J. Pribe, and J. Warner, *Sample correlation adjustments for robust Multi-fidelity Monte Carlo under limited pilot sampling*, arXiv:2605.23016, 2026. https://arxiv.org/abs/2605.23016
4. L. Sanguiao Sande and L.-C. Zhang, *Design-Unbiased Statistical Learning in Survey Sampling*, Sankhyā A 83 (2021), 714–744, arXiv:2003.11423. https://arxiv.org/abs/2003.11423 (general single-split estimator; earlier work).
5. M. E. Riaño, *Model-assisted estimation with a training subsample: a two-phase sampling approach with design-based variance estimation*, arXiv:2609.04082, 2026. https://arxiv.org/abs/2609.04082 (full HTML reviewed, distinct variance-design target).
6. R. R. Sitter, *Variance Estimation for the Regression Estimator in Two-Phase Sampling*, Journal of the American Statistical Association 92 (1997), 780–787. https://doi.org/10.1080/01621459.1997.10474031 (abstract inspected; full text not confirmed).
