# Rare-excursion history selection in a Brownian-diffusivity reset bath

## Finding

Consider a stationary one-dimensional particle whose position and signed diffusivity amplitude are jointly reset to zero at independent Poisson times of rate \(r>0\). Between resets,
\[
 dY_t=\sqrt{2}\,\Lambda\,dB_t,\qquad dX_t=\sqrt{2}\,Y_t\,dW_t,
\]
where \(\Lambda>0\) and \(B,W\) are independent standard Brownian motions. The physical instantaneous diffusivity is \(D_t=Y_t^2\). At a stationary observation time \(0\), let \(A\) be the backward age of the current reset excursion and define its complete diffusivity-amplitude history \(H_x(u)=Y_{-A+uA}\), \(0\le u\le1\), on the event \(X_0>x\).

For \(x\to\infty\), put
\[
 s_x=\sqrt{\frac{\pi x}{4\Lambda r}},\qquad
 h_x=\sqrt{\frac{s_x}{2r}},\qquad
 g(u)=2\sqrt{\frac{\Lambda}{\pi}}\sin\!\left(\frac{\pi u}{2}\right).
\]
Then the following **single conditional-history theorem** holds:
\[
 \left.\frac{A-s_x}{h_x}\ \right|\ X_0>x\ \Longrightarrow\ N(0,1),
\qquad
 \left.\frac{H_x(\cdot)}{\sqrt{x}}\ \right|\ X_0>x\ \Longrightarrow\ \tfrac12\delta_g+\tfrac12\delta_{-g}
 \quad\hbox{in }C([0,1]).
\]
In particular, uniformly over the fractional age \(u\in[0,1]\), the entire **physical diffusivity profile** becomes deterministic:
\[
 \left.\sup_{0\le u\le1}\left|
 \frac{D_{-A+uA}}{x}-\frac{4\Lambda}{\pi}
 \sin^2\!\left(\frac{\pi u}{2}\right)
 \right|\ \right|\ X_0>x\ \xrightarrow{\mathbb P}0.
\]
The Gaussian age scale and the sine-squared profile hold for every fixed \(r,\Lambda>0\). The rescaled diffusivity profile is independent of the reset rate, although the selected age is not. The corresponding results for \(X_0<-x\) follow by symmetry. These are statements about *conditional histories*, not an additional claim of originality for the stationary position tail.

## Assumptions and scope

The process is in its unique regenerative stationary law. Every Poisson event resets both coordinates \((X,Y)\) to \((0,0)\); the Brownian drivers are independent across and within renewal intervals; no additive thermal position noise or drift is included. The model is equivalent in joint law \((X,Y)\) to writing \(dX_t=\sqrt{2}|Y_t|d\widetilde W_t\), because \(\int\operatorname{sgn}(Y_t)\,dW_t\) is a Brownian motion independent of the entire \(Y\) path. The theorem concerns one spatial coordinate, a fixed pair of positive parameters, and thresholds \(x\to+\infty\). The rescaling of the past path begins at the most recent reset and ends at the present observation.

## Proof

**1. Renewal and Brownian scaling.** The stationary backward age \(A\) has density \(r e^{-rs}\,ds\), independently of freshly initiated Brownian trajectories. For independent unit-time Brownian motions \(B,W\), set \(J=\int_0^1 B_t\,dW_t\). Brownian scaling gives, jointly with the rescaled past path,
\[
 X_0\overset{d}{=}2\Lambda A J,
 \qquad H_x(u)\overset{d}{=}\sqrt{2}\Lambda\sqrt A\,B_u.
\]
Thus the conditional age density under \(X_0>x\) is exactly
\[
 p_x(s)=\frac{r e^{-rs}\,\mathbb P(J>x/(2\Lambda s))}{\mathbb P(X_0>x)},\qquad s>0.
\]

**2. Singular-mode factorization.** For \(n\ge1\), put \(\omega_n=(n-\tfrac12)\pi\), \(\sigma_n=1/\omega_n\), \(e_n(t)=\sqrt2\cos(\omega_nt)\), and \(f_n(t)=\sqrt2\sin(\omega_nt)\). These are the singular functions and singular values of the Volterra kernel \(\mathbf1_{\{s<t\}}\), because
\[
 \int_0^t e_n(u)\,du=\sigma_n f_n(t),\qquad
 \int_t^1 f_n(u)\,du=\sigma_n e_n(t).
\]
With independent standard-normal arrays \((\xi_n)\), \((\eta_n)\), the isonormal expansion gives
\[
 J=\sum_{n\ge1}\sigma_n\xi_n\eta_n\quad\hbox{in }L^2,
 \qquad B_t=\sum_{n\ge1}\sigma_n f_n(t)\xi_n\quad\hbox{in }C([0,1]).
\]
The singular values satisfy \(\sigma_1=2/\pi>\sigma_2=2/(3\pi)\). Let \(L=\sigma_1\xi_1\eta_1\), \(R=\sum_{n\ge2}\sigma_n\xi_n\eta_n\); \(L\) and \(R\) are independent. For \(|\theta|<\pi/2\),
\[
 \mathbb E e^{\theta J}=\prod_{n\ge1}(1-\theta^2\sigma_n^2)^{-1/2}=(\cos\theta)^{-1/2}.
\]
For some \(\varepsilon>0\), \(\mathbb E e^{(\pi/2+\varepsilon)|R|}<\infty\), using \(\sigma_2<\sigma_1\) and \(\sum\sigma_n^2<\infty\).

**3. One-big-mode conditional lemma.** The independent-normal product has
\[
 \mathbb P(L>z)\sim\sqrt{\frac{\sigma_1}{2\pi z}}e^{-z/\sigma_1}.
\]
Conditioning on \(J>z\), the law of the entire off-principal-mode array converges in total variation to its exponential tilt with density proportional to \(e^{R/\sigma_1}\). Indeed, conditioning first on the off-mode array, divide \(\mathbb P(L>z-R)\) by \(\mathbb P(L>z)\), use pointwise convergence to \(e^{R/\sigma_1}\), and split \(|R|\le z/2\) from the complement. The product-tail bound together with the exponential moment beyond \(1/\sigma_1\) controls the complement and permits dominated convergence. Under this tilt the off-mode Brownian path remains a tight continuous Gaussian process: each two-normal block has covariance bounded by \((1-\sigma_2^2/\sigma_1^2)^{-1}\), so its partial-sum covariance is bounded by a fixed multiple of Brownian covariance. Consequently the off-mode path divided by \(\sqrt z\) vanishes uniformly in conditional probability.

Conditional on a bounded off-mode remainder, \(\xi_1\eta_1>(z-R)/\sigma_1\). Writing \(S=(\xi_1+\eta_1)/\sqrt2\) and \(T=(\xi_1-\eta_1)/\sqrt2\), the event is \(S^2-T^2>2(z-R)/\sigma_1\); Gaussian tail bounds show \(T/\sqrt z\to0\) and \(|S|/\sqrt z\to\sqrt{2/\sigma_1}\). Its two signs have equal probability by symmetry. This proves the path-level limit
\[
 \left.\frac{B_\cdot}{\sqrt z}\ \right|\ J>z
 \ \Longrightarrow\ \tfrac12\delta_{b}+\tfrac12\delta_{-b}
 \quad\hbox{in }C([0,1]),\qquad
 b(u)=\frac{\sigma_1f_1(u)}{\sqrt{\sigma_1}}=\frac{2}{\sqrt\pi}\sin\!\left(\frac{\pi u}{2}\right).
\]
The normal-product tail and the off-mode tilt also yield the exact logarithmic and polynomial tail:
\[
 \mathbb P(J>z)\sim \frac{2}{\pi^{3/2}}z^{-1/2}e^{-\pi z/2}.
\]
Here \(\prod_{n\ge2}(1-\sigma_n^2/\sigma_1^2)=\pi/4\), obtained from the cosine product at its first zero.

**4. Conditional reset-age saddle and central limit.** Uniformly for \(s\) in fixed compact multiples of \(\sqrt x\), the preceding tail gives
\[
 r e^{-rs}\mathbb P\!\left(J>\frac{x}{2\Lambda s}\right)
 \sim r\frac{2}{\pi^{3/2}}\sqrt{\frac{2\Lambda s}{x}}
 \exp\!\left(-rs-\frac{\pi x}{4\Lambda s}\right).
\]
The exponent \(\Phi_x(s)=rs+\pi x/(4\Lambda s)\) has the unique minimizer \(s=s_x\), with \(\Phi_x''(s_x)=2r/s_x\) and width \(h_x=1/\sqrt{\Phi_x''(s_x)}\). Since \(\Phi_x(s)/\sqrt x\) has a strictly larger value outside each neighborhood of \(s_x/\sqrt x\), Chernoff bounds for \(J\) at any parameter below \(\pi/2\), followed by a sharp bound on the principal-mode contribution, show that conditional mass outside \(s/s_x\in[1-\delta,1+\delta]\) is exponentially negligible relative to the full integral. Taylor expansion of \(\Phi_x(s_x+h_x z)\) gives \(\Phi_x(s_x)+z^2/2+o(1)\), uniformly on compact \(z\)-sets; the prefactor \(s^{1/2}\) varies negligibly on the \(h_x\) scale. Gaussian Laplace asymptotics with the same tail bounds control the complements. This proves the stated conditional central limit theorem and \(A/s_x\to1\) in conditional probability.

**5. Entire history and diffusivity.** On the selected age scale, \(z=x/(2\Lambda A)\to\infty\) in conditional probability; the conditional principal-mode lemma applies uniformly for \(A/s_x\) in a compact neighborhood of one. Since \(\sqrt{2}\Lambda\sqrt A\sqrt z/\sqrt x=\sqrt\Lambda\), the rescaled path converges to the symmetric two-point law supported on \(\pm\sqrt\Lambda b=\pm g\). Applying the continuous mapping \(h\mapsto h^2\) in the uniform topology yields the deterministic squared-path limit. This completes the proof.

## Verification

The included standalone script `check.py` recomputes Volterra singular-function integrals, the hyperbolic-cosine determinant, the off-mode determinant, the exact gamma-function density of \(J\), principal-mode conditional Gaussian quadratures, the saddle curvature, the universal profile coefficient, the inverse-Gaussian age proxy, and the consistency of the pre-existing marginal tail prefactor. It executes without access to external services. Analytical normal-product asymptotics, exponential tilting, and Laplace localization—not a finite cutoff or numerical simulation—establish the infinite-limit statements.

## Relationship to prior work

Santra, Basu, and Sabhapandit (2022) define the resetting stochastic-diffusivity particle and derive its stationary position law, including the stretched-exponential far tail and a saddle in the *unconditioned* position density. Those results are prerequisites, not claimed as novel. Masó-Puigdellosas, Campos, and Méndez (2022) give a general renewal identity for backward reset times conditioned on the observed position, specializing their calculations to ordinary diffusion. De Marco and Friz (2013/2018) establish large-strike conditional terminal-volatility laws for Stein–Stein diffusions. The present statement concerns a different regenerative model's **full backward diffusivity path conditioned on an extreme stationary displacement together with the nontrivial central-limit scale of its reset age**. In particular its universal sine-squared history is not a restatement of a stationary marginal tail or a fixed-time terminal-variance theorem. General Gaussian-mode and renewal techniques are acknowledged as mathematical antecedents.

## Limitations

Only one-dimensional independent Brownian drivers, joint Poisson resetting, and strictly positive fixed parameters are covered. This is asymptotic conditioning on an arbitrarily large positive stationary position, not a finite-threshold confidence interval, a first-passage trajectory, or a statement uniform in \(r\) or \(\Lambda\). The source literature provides the stationary far-tail mechanism; the specific conditional path theorem has not undergone independent scholarly validation. An unlocated general conditional Gaussian-chaos theorem could imply part of it. The sign of the auxiliary amplitude remains unobservable through its square and is asymptotically equiprobable.

## References

1. I. Santra, U. Basu, S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient*, arXiv:2205.00549v1 (public 2022-05-01), especially Sections 2, 4–6 and Appendix C. https://arxiv.org/abs/2205.00549
2. A. Masó-Puigdellosas, D. Campos, V. Méndez, *Conditioned backward and forward times of diffusion with stochastic resetting: a renewal theory approach*, arXiv:2205.01613v1 (2022-05-03), especially Section IV. https://arxiv.org/abs/2205.01613
3. S. De Marco, P. K. Friz, *Varadhan's formula, conditioned diffusions, and local volatilities*, arXiv:1311.1545 (2013), subsequently *SIAM Journal on Financial Mathematics* 9 (2018), especially Section 4.3. https://arxiv.org/abs/1311.1545
