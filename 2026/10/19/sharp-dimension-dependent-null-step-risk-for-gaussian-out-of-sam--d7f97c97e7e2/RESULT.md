# Sharp dimension-dependent null-step risk for Gaussian out-of-sample hypergradient scaling

## Finding

Consider the out-of-sample hypergradient feedback and null-step acceptance rule for a scalar preconditioner. At the minimizer of an isotropic quadratic, independent Gaussian training and validation gradients produce a Student-ratio hypergradient whose law **does not improve with minibatch size**, even though the resulting primal risk decreases inversely with batch size. The exact two-update risk has three distinct small-learning-rate regimes, separated by gradient dimension one and two.

**Theorem.** Fix integers \(d\ge 1\), \(b\ge 1\), positive \(\sigma,M,\eta\), and the stochastic convex objectives
\[
 f_{\omega}(x)=\frac12\|x\|_2^2+\langle\omega,x\rangle,
 \qquad \omega\sim N(0,\sigma^2 I_d/b).
\]
The expected objective is \(f(x)=\tfrac12\|x\|_2^2\), uniquely minimized at \(x_*=0\). The Gaussian oracle represents a minibatch average of \(b\) independent isotropic Gaussian linear perturbations. At each call, training and validation perturbations are independent, and fresh calls are mutually independent.

Initialize the scalar scaled-gradient procedure at \(x_0=0\), \(\alpha_0=0\), with candidate stepsizes \([0,M]\). Use the normalized independent-validation hypergradient
\[
 h_{\omega,\nu}(\alpha;x)
 =\frac{f_{\nu}(x-\alpha\nabla f_{\omega}(x))-f_{\nu}(x)}
 {\|\nabla f_{\omega}(x)\|_2^2}
\]
for projected online scaling with learning rate \(\eta\). At each primal update, accept the proposed point only if its **validation-sample** objective is no larger than that at the current point. (Ties are harmless.) The first primal step is zero. Let \(\alpha_1\) be the learned stepsize and \(x_2\) the accepted second primal iterate.

Define \(R_d=N/\sqrt{U_d}\), where \(N\sim N(0,1)\), \(U_d\sim\chi_d^2\) are independent. Write \(p_\eta(r)=\min\{M,\max\{0,\eta r\}\}\) and
\[
 A_d(p)=\Pr\left\{\frac{N}{\sqrt{U_{d+2}}}\ge\frac p2\right\},\qquad p\ge0.
\]
Then the following **exact, finite-sample** formulas hold:
\[
 \boxed{\alpha_1\ \stackrel{\mathrm d}=\ p_\eta(R_d),\quad
 \mathbb E f(x_2)=\frac{d\sigma^2}{2b}
 \mathbb E\big[p_\eta(R_d)^2 A_d(p_\eta(R_d))\big].}
\]
In particular, the distribution of \(\alpha_1\) is independent of \(b\); its atom at zero has probability \(1/2\), and its atom at \(M\) has positive probability \(\Pr\{R_d\ge M/\eta\}\). The trial iterate before the second null step has true expected objective \(\frac{d\sigma^2}{2b}\mathbb E p_\eta(R_d)^2\).

For fixed \(d,b,\sigma,M\) and \(\eta\downarrow0\), put
\[
 C_1(M)=\frac M\pi\left[1-\frac2\pi\arctan\!\left(\frac M2\right)
 -\frac{M/2}{\pi(1+M^2/4)}\right]>0.
\]
The **accepted** error has the following *sharp equivalent*, with positive coefficients:
\[
 \boxed{\mathbb E f(x_2)=\frac{d\sigma^2}{2b}\begin{cases}
 C_1(M)\eta+o(\eta),&d=1,\\
 \frac14\eta^2\log(1/\eta)+o\big(\eta^2\log(1/\eta)\big),&d=2,\\
 \frac{\eta^2}{4(d-2)}+o(\eta^2),&d\ge3.
 \end{cases}}
\]
The corresponding factors **before** the null step are \(2M\eta/\pi+o(\eta)\), \(\frac12\eta^2\log(1/\eta)+o(\eta^2\log(1/\eta))\), and \(\eta^2/[2(d-2)]+o(\eta^2)\), respectively, inside the common multiplier \(d\sigma^2/(2b)\).

## Assumptions and scope

All finite parameters and quantifiers are as stated above. Gaussian perturbations are added linearly to strongly convex quadratic sample objectives. The scalar preconditioner is exactly projected onto \([0,M]\); gradients, feedback derivatives, and validation comparisons are exact. The two validation batches used for feedback and the subsequent null-step decision are separate and independent. The first decision evaluates a zero proposal because \(\alpha_0=0\). The result concerns two primal updates, not the invariant distribution or convergence of an indefinitely continued algorithm. The asymptotic statements vary only the **online hypergradient learning rate** \(\eta\); the minibatch size \(b\), cap \(M\), and dimension \(d\) remain fixed.

The Gaussian oracle has persistent, noninterpolating gradient noise even at \(x_*\), and therefore does **not** satisfy the relative-gradient-noise assumption used for convergence in the motivating source. The theorem is a model-specific boundary calculation and does not refute that convergence theorem.

## Proof

**1. Feedback and its exact law.** At \(x_0=0\), the sampled training gradient equals \(g=\omega\), and for independent validation perturbation \(v=\nu\) the feedback is
\[
 h_{g,v}(\alpha;0)=\frac{\|\alpha g\|^2/2-\alpha\langle v,g\rangle}{\|g\|^2}
 =\frac{\alpha^2}{2}-\alpha\frac{\langle v,g\rangle}{\|g\|^2}.
\]
The training gradient is nonzero almost surely. Thus \(\partial_\alpha h(0)=-R\), where \(R=\langle v,g\rangle/\|g\|^2\). Projected online descent gives \(\alpha_1=p_\eta(R)\); the first trial and accepted primal points both equal zero. Put \(g=(\sigma/\sqrt b)Z\), \(v=(\sigma/\sqrt b)E\) with independent standard Gaussian \(d\)-vectors. Conditional on \(Z\), the scalar \(\langle E,Z\rangle/\|Z\|\) is standard normal, and its conditional law does not depend on \(Z\); it is therefore independent of \(\|Z\|^2\sim\chi_d^2\). Consequently \(R\stackrel{\mathrm d}=R_d\). This yields the minibatch invariance and both atoms. Its density is
\[
 \rho_d(r)=c_d(1+r^2)^{-(d+1)/2},\qquad
 c_d=\frac{\Gamma((d+1)/2)}{\sqrt\pi\,\Gamma(d/2)}.
\]
The Student-ratio law, not its derivation as a probability identity, is not claimed to be new.

**2. Exact risk of the validation null step.** At the second update, the proposal is \(y=-p g'\) with \(p=\alpha_1\) and independent \(g',v'\sim N(0,\sigma^2 I_d/b)\). It is accepted exactly when
\[
 \frac{p^2}{2}\|g'\|^2-p\langle v',g'\rangle\le0.
\]
For \(p>0\), conditional on \(g'=(\sigma/\sqrt b)Z'\), acceptance has probability \(\overline\Phi(p\|Z'\|/2)\); for \(p=0\) there is no displacement regardless of the tie convention. Therefore
\[
 \mathbb E[f(x_2)\mid p]
 =\frac{\sigma^2p^2}{2b}\mathbb E[\|Z'\|^2\overline\Phi(p\|Z'\|/2)].
\]
If \(U_d=\|Z'\|^2\), then for all measurable bounded \(q\),
\(\mathbb E[U_dq(U_d)]=d\,\mathbb E[q(U_{d+2})]\), by the explicit chi-square densities. It follows that the conditional expected objective is exactly
\(\frac{d\sigma^2}{2b}p^2 A_d(p)\). Averaging over the independent random \(p\) proves the boxed identity. Dropping the null-step indicator proves the trial-risk formula.

**3. Dimension \(d=1\): a clipped Cauchy boundary layer.** Here \(\rho_1(r)=1/[\pi(1+r^2)]\). With \(y=\eta r\), the accepted risk factor (without \(d\sigma^2/(2b)\)) is
\[
 I_1(\eta)=\frac\eta\pi\int_0^\infty
 \frac{\min(y,M)^2A_1(\min(y,M))}{y^2+\eta^2}\,dy.
\]
The integrand after division by \(\eta\) is dominated by a constant for \(0<y\le M\) and by \(M^2/y^2\) for \(y>M\); dominated convergence gives
\[
 \lim_{\eta\downarrow0}\frac{I_1(\eta)}\eta
 =\frac1\pi\left(\int_0^M A_1(y)\,dy+M A_1(M)\right).
\]
For \(u=p/2\), direct integration of the density \(\rho_3(r)=\frac2\pi(1+r^2)^{-2}\) gives
\[
 A_1(p)=\frac12-\frac1\pi\left(\arctan u+\frac u{1+u^2}\right).
\]
Since \(\frac d{dp}[p\arctan(p/2)]=\arctan u+u/(1+u^2)\), the limit equals the stated \(C_1(M)\). It is strictly positive because its unevaluated integral comprises positive tail probabilities. The same substitution with \(A_1\) replaced by one yields \(\mathbb E p_\eta(R_1)^2\sim2M\eta/\pi\).

**4. Dimension \(d=2\): logarithmic boundary layer.** Now \(\rho_2(r)=\frac12(1+r^2)^{-3/2}\), so \(r^2\rho_2(r)\sim1/(2r)\). For every fixed \(0<\delta<M\), the part \(1\le r\le\delta/\eta\) contributes
\[
 \eta^2\int_1^{\delta/\eta}r^2 A_2(\eta r)\rho_2(r)\,dr.
\]
The function \(A_2\) is continuous and \(A_2(0)=1/2\), so upper and lower comparison with \(1/2\pm\sup_{0\le p\le\delta}|A_2(p)-1/2|\) yields the sharp logarithmic coefficient \(1/4\) after \(\eta\downarrow0\), then \(\delta\downarrow0\). The portion \(r<1\) is \(O(\eta^2)\), while the portion \(r>\delta/\eta\) is \(O_\delta(\eta^2)\) since the squared projected step is bounded and \(\Pr\{R_2>t\}=O(t^{-2})\). Replacing \(A_2\) by one gives coefficient \(1/2\) for the trial step.

**5. Dimension \(d\ge3\): finite second moment.** Since \(R_d=N/\sqrt{U_d}\), independence and the chi-square inverse moment yield \(\mathbb E R_d^2=1/(d-2)\). The symmetry implies \(\mathbb E(R_d)_+^2=1/[2(d-2)]\). Pointwise, \(p_\eta(R_d)/\eta\to(R_d)_+\), and \(p_\eta(R_d)/\eta\le(R_d)_+\); also \(A_d(p_\eta(R_d))\to1/2\). Dominated convergence therefore gives
\[
 \lim_{\eta\downarrow0}\frac{I_d(\eta)}{\eta^2}
 =\frac12\mathbb E(R_d)_+^2=\frac1{4(d-2)}.
\]
The same argument without acceptance gives \(1/[2(d-2)]\) for the trial step. All cases are proved.

## Verification

The standalone `check.py` uses only the Python standard library. Running `python check.py` evaluates the exact Student-ratio survival function via a cosine-power recurrence, independently integrates the null-step and proposal risks, checks closed Cauchy/dimension-two proposal formulas, checks small-learning-rate limits, and replays the two stochastic updates with seeded independent Gaussian draws for dimensions one through three and two minibatch sizes. The program reported **70 passing check families** in this package. The analytical proof supplies the infinite-domain result; numerical checks are not an exhaustive proof.

## Relationship to prior work

Zhang, Gao, Ye, and Udell (2026) introduce stochastic online-scaled gradient methods, independent-sample ratio and hypergradient feedback, a projection safeguard, and a validation-based null step. Their convergence theorems require a relative gradient-noise condition. The present statement analyzes the specific *noninterpolating Gaussian* oracle at the population optimum, derives the exact accepted second-update risk, and identifies its dimension-dependent small-learning-rate constants. No new optimizer or general convergence claim is made.

Gao, Chu, Ye, and Udell (2025) develop deterministic online scaling and the hypergradient feedback mechanism. The Student distribution is a classical Gaussian-ratio identity. Work on heavy-tailed SGD (Gürbüzbalaban, Şimşekli, and Zhu, 2021) studies multiplicative-noise-induced tail behavior in stationary gradient iterations; it does not directly give this projected two-update null-step risk formula. A distinct contemporary specialization of stochastic online scaling on *random-curvature* quadratics studies population feedback targets and curvature stability; this statement instead concerns additive Gaussian noninterpolation, Student-ratio fluctuations, and dimension-dependent accepted risk. Bibliographic completeness is not guaranteed.

## Limitations

This is an exact-arithmetic, isotropic, independently resampled Gaussian **expectation-oracle** model, not a conditional-on-fixed-finite-dataset guarantee. It covers only the first two steps initialized at the true minimizer and zero scaling. The null-step uses a noisy validation objective, not exact population loss. The result neither contradicts convergence theorems requiring vanishing relative gradient noise nor claims stability, nonconvergence, or stationary error for the full trajectory. The probability identities from Student distributions are classical; the assessed contribution is the coupling to the projected hypergradient and validation null step, with its sharp three-regime accepted-risk law.

## References

1. W. Zhang, W. Gao, Y. Ye, M. Udell, *Stochastic Gradient Methods with Online Scaling*, arXiv:2609.11751v2 (first publicly posted 2026-09-10), especially Sections 2–3, 5.1, and Appendix A. https://arxiv.org/html/2609.11751v2
2. W. Gao, Y.-C. Chu, Y. Ye, M. Udell, *Gradient Methods with Online Scaling Part I: Theoretical Foundations*, arXiv:2505.23081v2 (first publicly posted 2025-05-29), Sections 3 and 7. https://arxiv.org/html/2505.23081v2
3. M. Gürbüzbalaban, U. Şimşekli, L. Zhu, *The Heavy-Tail Phenomenon in SGD*, Proceedings of ICML 2021; arXiv:2006.04740. https://arxiv.org/abs/2006.04740
4. Standard Student-ratio identity: if independent \(N\sim N(0,1)\) and \(U\sim\chi_d^2\), then \(\sqrt d\,N/\sqrt U\) has Student's \(t\) law with \(d\) degrees of freedom.
