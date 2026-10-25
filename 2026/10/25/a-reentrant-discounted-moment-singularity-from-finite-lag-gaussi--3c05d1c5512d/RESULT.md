# A reentrant discounted-moment singularity from finite-lag Gaussian dynamics reconstruction

## Finding

Let a continuously observed Ornstein–Uhlenbeck (OU) process have parameters \(a>0\) and \(\sigma>0\):
\[
 dX_t=-aX_t\,dt+\sigma\,dW_t,\qquad X_0=0.
\]
For a lag \(h>0\), form a continuous-time surrogate using the *uncentered* conditional first and second increments divided by \(h\). Let \(Z^{(h)}\) denote the resulting diffusion, started at zero, and for any \(\beta>0\) define its nonnegative discounted quartic evaluation
\[
 V_{\beta,h}=\mathbb E_0\int_0^\infty e^{-\beta t}(Z_t^{(h)})^4\,dt\in[0,+\infty].
\]
Set \(s=ah\) and
\[
 F(s)=\frac{2(1-4e^{-s}+3e^{-2s})}{s},\quad
 H(s)=s(4e^{-s}-6e^{-2s})-(1-4e^{-s}+3e^{-2s}).
\]
There is exactly one \(s_*\in(\log3,+\infty)\) solving \(H(s_*)=0\), and \(F_*=F(s_*)=0.553698915832467\ldots\), \(s_*=2.545394354952303\ldots\). The exact discounted-value finiteness classification is
\[
 V_{\beta,h}=+\infty\quad\Longleftrightarrow\quad \beta\le aF(ah).
\]
If \(0<\beta<aF_*\), there are exactly two lags \(h_-(\beta)<s_*/a<h_+(\beta)\), satisfying \(aF(ah_\pm)=\beta\), and the value is infinite **precisely** on \([h_-(\beta),h_+(\beta)]\); at the two endpoints it is also infinite. At \(\beta=aF_*\), precisely one lag is singular, while for \(\beta>aF_*\), all lags have finite value. As a concrete example, for \(a=\sigma=1\) and \(\beta=0.4\), the singular lag band is approximately \([1.614693483787,4.843313713699]\), bounded on both sides by finite-value regimes.

The surrogate has a unique invariant distribution of Student type; its variance is exactly that of the original Gaussian OU invariant measure, but its fourth moment is finite if and only if \(ah<\log3\). Therefore preservation of the invariant second moment does not ensure control of a fourth-order objective. The original OU objective remains finite and equals
\[
 V^{\mathrm{OU}}_\beta(0)=\frac{6\sigma^4}{\beta(\beta+2a)(\beta+4a)}
\]
for every \(\beta>0\).

## Assumptions and scope

The quantifiers are: arbitrary \(a,\sigma,h,\beta>0\), one spatial dimension, exact OU transition moments (no sampling or numerical-estimation error), no control action and no population interaction, initial condition zero, the uncentered second increment \(\mathbb E[(X_h-X_0)^2\mid X_0=x]\) rather than the centered conditional variance, and nonnegative reward \(x\mapsto x^4\). This is a specialization of one-step-coefficient continuous-time generator surrogates, not a claim about every discretization or policy-optimization algorithm. A finite discounted value means the expectation of the nonnegative integral is finite; it is not merely a formal polynomial solution of a PDE.

## Proof

**1. Exactly reconstructed generator.** Write \(q=e^{-ah}\), \(r=1-q\), and \(v=\sigma^2(1-q^2)/(2a)\). The OU transition is \(X_h=qx+\eta\) conditional on \(X_0=x\), where \(\mathbb E\eta=0\) and \(\mathbb E\eta^2=v\). Thus the conditional increment mean and uncentered squared increment are \(-rx\) and \(r^2x^2+v\). The surrogate generator is exactly
\[
 (\widehat L_h f)(x)=-\frac rh x f'(x)+\frac{v+r^2x^2}{2h}f''(x).
\]
Equivalently \(dZ_t=-(r/h)Z_t\,dt+\sqrt{(v+r^2Z_t^2)/h}\,dB_t\). Its coefficients are globally Lipschitz (the diffusion coefficient has derivative bounded by \(r/\sqrt h\)); since \(v>0\), the model is uniformly elliptic in the sense that its squared diffusion is bounded below by \(v/h>0\). Thus a nonexplosive unique strong solution exists.

**2. Invariant law and fourth-moment boundary.** The zero-current stationary density solves \((Dp)'=2bp\), where \(D(x)=(v+r^2x^2)/h\) and \(b(x)=-rx/h\). Direct integration gives
\[
 p_h(x)=\frac{(r/\sqrt v)\,\Gamma(1+1/r)}{\sqrt\pi\,\Gamma(1/2+1/r)}
 \left(1+\frac{r^2x^2}{v}\right)^{-(1+1/r)}.
\]
This is a scaled Student law with \(\nu_h=1+2/r>3\) degrees of freedom; the stated normalization follows from the beta integral. The density is integrable, strictly positive, and decays as \(|x|^{-2-2/r}\). Its stationary fourth moment is finite if and only if \(4<\nu_h\), namely \(r<2/3\), equivalently \(e^{-ah}>1/3\) or \(ah<\log3\). At equality the fourth-moment integral has logarithmic divergence. The identity
\[
 \widehat L_h(x^2)=-\frac{2r-r^2}{h}x^2+\frac vh
\]
shows that its stationary variance is \(v/(2r-r^2)=\sigma^2/(2a)\). For completeness, applying this quadratic Lyapunov drift gives tightness/positive recurrence; strict positivity and smoothness of transition densities on the connected real line give irreducibility and uniqueness of the invariant probability. This also establishes uniqueness independently of the explicit density normalization.

**3. Exact discounted fourth moment.** Starting at \(Z_0=0\), denote \(m_j(t)=\mathbb E[Z_t^j]\). The generator identities for \(x^2\) and \(x^4\) yield, with \(c=v/h>0\),
\[
 m_2'=\lambda_2m_2+c,\qquad m_4'=\lambda_4m_4+6c m_2,
\]
where \(m_2(0)=m_4(0)=0\) and
\[
 \lambda_2=-\frac{1-q^2}{h}<0,\quad
 \lambda_4=\frac{-4r+6r^2}{h}=\frac{2(1-4q+3q^2)}{h}=aF(ah).
\]
These are valid finite-time polynomial moments: the SDE coefficients have linear growth, so standard localized Itô estimates give moments of every finite order on finite horizons. Since \(m_2(t)=c(1-e^{\lambda_2t})/(-\lambda_2)>0\) for \(t>0\), the variation-of-constants formula
\[
 m_4(t)=6c\int_0^t e^{\lambda_4(t-u)}m_2(u)\,du
\]
is strictly positive. If \(\beta\le\lambda_4\), the contribution from \(u\in[0,1]\) makes \(m_4(t)\ge C e^{\lambda_4t}\) for all \(t\ge1\), where \(C=6c\int_0^1e^{-\lambda_4u}m_2(u)\,du>0\); hence its discounted time integral diverges, including at equality. If \(\beta>\lambda_4\), Tonelli's theorem and direct Laplace transformation of these nonnegative moment equations give
\[
 V_{\beta,h}=\frac{6(v/h)^2}{\beta(\beta-\lambda_2)(\beta-\lambda_4)}
 =\frac{6(v/h)^2}{\beta\,[\beta+(1-q^2)/h]\,[\beta-aF(ah)]}<\infty.
\]
The OU comparison follows similarly from \(m_2'=-2am_2+\sigma^2\) and \(m_4'=-4am_4+6\sigma^2m_2\).

**4. Exactly one reentrant divergence band.** The numerator of \(F\) factors as \(N(s)=1-4e^{-s}+3e^{-2s}=(1-e^{-s})(1-3e^{-s})\); it is nonpositive up to \(s_0=\log3\), strictly positive afterwards, and tends to one as \(s\to+\infty\). For \(s>s_0\),
\[
 F'(s)=\frac{2H(s)}{s^2},\qquad
 H'(s)=sN''(s)=4se^{-s}(3e^{-s}-1)<0.
\]
Further, \(H(s_0)=s_0N'(s_0)>0\) and \(H(s)\to-1\) as \(s\to\infty\). Consequently \(H\) has exactly one zero \(s_*\) on that interval, and \(F\) strictly rises from zero to \(F_*\) and then strictly falls to zero. Continuity, strict monotonicity on the two sides, and the condition \(\beta\le aF(ah)\) give the exact zero/one/two critical-lag trichotomy, with no other excluded cases. Numerical values are reproducible using the included bisection program; the analytic classification does not depend on floating-point numerics.

## Verification

Run `python3 checks/verify.py` with the Python 3 standard library. It checks the exact rational variance identity for 1,045 pairs of rational one-step factors, brackets the unique critical point, finds the two critical lags for five discounts, and compares closed-form discounted values against independent RK4 integrations of the coupled moment-and-cost ODE for five parameter choices; every relative error is below \(10^{-4}\). Its recorded reproducible output is `checks/output.txt`. These finite diagnostics do not prove the all-parameter inequalities, which are established by the analytic steps above.

## Relationship to prior work

The uncentered first-two-increment substitution is directly motivated by Bayraktar, Hernandez, Yan, and Zhu (2026), Section 4.1, whose estimators use conditional increments divided by the observation lag. Lade (2009), Section 3, already derives exactly the finite-lag linear drift and state-quadratic second Kramers–Moyal coefficient of an OU process. Thus these coefficients are **not** claimed as new. The Student invariant family and its moment recursion are also established generically in Pearson diffusion work, including Forman and Sørensen (2008) and Monthus (2023), so those general properties are not separately claimed as novel.

The claim distinguished here is the **joint sharp phase diagram in observation lag and discount**: the unique interior maximum of the fourth-moment growth exponent, the resulting closed reentrant interval of infinite discounted quartic evaluation at fixed positive discount, and its coexistence with the exact variance match and always-finite true OU benchmark. The inspected earlier analyses do not state this lag/discount classification. It is a consequence of combining the exact lag coefficients with an additional global parameter optimization, not a claimed new class of Pearson diffusions.

## Limitations

This is an uncontrolled, one-dimensional model with exact infinite-data conditional increment statistics; it does not quantify errors in finite-sample inference, alternative centered-covariance estimators, higher-order moment corrections, numerical PDE solvers, or policy optimality. It is not a contradiction of convergence theorems that assume globally bounded coefficients, restricted reward growth, or sufficiently small observation lag. In particular, the motivating mean-field theory treats such unbounded-growth situations separately. The critical result is for a nonnegative quartic reward and the first-order **uncentered** second-increment generator only. Independent mathematical review and exhaustive literature priority verification have not been performed.

## References

1. Erhan Bayraktar, Martin Hernandez, Qinxin Yan, Yuhua Zhu (2026), *Mean-Field PhiBE: Continuous-Time Mean-Field Reinforcement Learning from Discrete-Time Data*, arXiv:2606.26498v1, first public 2026-06-25, Section 4.1 and Section 5.
2. Steven J. Lade (2009), *Finite sampling interval effects in Kramers-Moyal analysis*, arXiv:0905.4324, Section 3, equations (7)–(8).
3. Cécile Monthus (2023), *Large deviations for the Pearson family of ergodic diffusion processes involving a quadratic diffusion coefficient and a linear force*, arXiv:2303.09348v3, Sections III and XIII.
4. Julie Lyng Forman and Michael Sørensen (2008), *The Pearson Diffusions: A Class of Statistically Tractable Diffusion Processes*, Scandinavian Journal of Statistics 35, 438–465, DOI:10.1111/j.1467-9469.2007.00592.x.
5. Predrag Pilipović, Adeline Samson, Susanne Ditlevsen (2026), *Strang splitting estimator for nonlinear multivariate stochastic differential equations with Pearson-type multiplicative noise*, arXiv:2604.16645v2, supplemental classification of Pearson diffusion invariant laws.
