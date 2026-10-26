# Exact moment-loss wedge and Pareto-exponent reversal under frequent partial resetting

## Finding

A linear particle subject to *expanding* drift, Brownian noise and frequent partial contractions has an exact stationary Pareto tail. The second-order diffusion approximation has another Pareto exponent. Their orders reverse **exactly at the common stationary variance threshold**, despite both models having identical finite stationary variances wherever those variances exist. More strongly, a nonempty open parameter wedge has finite stationary fourth moment for the original model but infinite fourth moment for the diffusion approximation.

Take \(D>0\), \(\lambda>0\), \(0<\gamma<\lambda\), and \(0<s<1\). Let \(X\) be the stationary version of the process
\[
 dX_t=\gamma X_t\,dt+\sqrt{2D}\,dW_t\quad\text{between jumps},
 \qquad X_t=(1-s)X_{t-}\quad\text{at Poisson rate }\lambda/s.
\]
Let \(Y\) be the stationary Itô diffusion approximation
\[
 dY_t=(\gamma-\lambda)Y_t\,dt+\sqrt{2D}\,dW_t+\sqrt{\lambda s}\,Y_t\,dB_t,
\]
where \(W\) and \(B\) are independent Brownian motions. Define \(p_s\) as the unique strictly positive root of
\[
 \gamma p+\frac{\lambda}{s}\big((1-s)^p-1\big)=0,
\]
and put \(q_s=1+2(\lambda-\gamma)/(\lambda s)\). Then there exist finite strictly positive constants \(C_X,C_Y\) (dependent on the parameters) such that
\[
 \mathbb P(X>x)\sim C_X x^{-p_s},\qquad
 \mathbb P(Y>x)\sim C_Y x^{-q_s}\qquad (x\to\infty).
\]
Both stationary distributions are symmetric. With \(b=\gamma/\lambda\) and \(s_c=2(1-b)\), the comparison is exact:
\[
 p_s>q_s\ \text{if }s<s_c,\qquad
 p_s=q_s=2\ \text{if }s=s_c<1,\qquad
 1<p_s<q_s<2\ \text{if }s>s_c.
\]
In particular, when \(b\le 1/2\), the first inequality holds for every \(s\in(0,1)\). For \(b>1/2\), both inequalities and the equality occur in the permitted parameter range. Away from equality, the ratio of the two positive tails tends to zero or infinity according to the indicated exponent order.

The two stationary variances agree **exactly**, not just asymptotically, whenever \(s<s_c\):
\[
 \mathbb E[X^2]=\mathbb E[Y^2]=
 \frac{2D}{2(\lambda-\gamma)-\lambda s}.
\]
Both variances diverge when \(s\ge s_c\) (if that range intersects \((0,1)\)). Nevertheless their higher moment regimes differ. For every \(0<s<2/3\), define
\[
 b_{4,\mathrm{DA}}=1-\frac32s,\qquad
 b_{4,\mathrm{true}}=1-\frac32s+s^2-\frac14s^3.
\]
On the nonempty **open** wedge \(b_{4,\mathrm{DA}}<\gamma/\lambda<b_{4,\mathrm{true}}\), the true fourth stationary moment is finite but the approximate fourth moment is infinite, while both stationary variances are finite. For example, \(s=1/5\) and \(\gamma/\lambda=18/25\) give \(p_s\approx4.2608254345>4\) but \(q_s=19/5<4\). If both fourth moments exist, they satisfy the exact strict inequality \(\mathbb E[X^4]<\mathbb E[Y^4]\).

For fixed \(b\in(0,1)\) the weak-reset limit is singular in the far tail. Let \(c_b>0\) uniquely solve \(bc_b=1-e^{-c_b}\). Then
\[
 p_s=\frac{c_b}{s}+\frac{c_be^{-c_b}}{2(b-e^{-c_b})}+O(s),\qquad
 \frac{p_s}{q_s}\longrightarrow\frac{c_b}{2(1-b)}>1
 \quad(s\downarrow0).
\]
Thus the ratio of the exact and Gaussian-approximation tail indices stays separated from one even though the approximation is valid for ordinary fixed-scale observables as \(s\downarrow0\).

## Assumptions and scope

All statements quantify over the specified \(D,\lambda,\gamma,s\). The Poisson clock is homogeneous and independent of the Brownian motion; each jump contracts the current position, rather than resetting to an independently drawn position. The drift is expanding (\(\gamma>0\)), but its mean contraction due to jumps is stronger (\(\gamma<\lambda\)). Stationarity refers to the invariant law at arbitrary deterministic observation times, not only at reset epochs. The two Brownian drivers of the approximate Itô SDE are independent. The survival index is the exponent of the right-tail *probability*, not the exponent of its density. No simultaneous spatial-threshold/weak-reset scaling is claimed.

## Proof

**1. Existence and the Gaussian mixture.** For a two-sided stationary Poisson clock, let \(N_u\) count jumps in the preceding time interval of length \(u\). The stochastic convolution from the infinite past is conditionally centered Gaussian, with random variance
\[
 V=2D\int_0^\infty e^{2\gamma u}(1-s)^{2N_u}\,du.
\]
Almost surely, \(N_u/u\to\lambda/s\), so the exponential rate of the integrand is \(2\gamma+2(\lambda/s)\log(1-s)<2(\gamma-\lambda)<0\). Consequently \(0<V<\infty\) almost surely and \(X\overset d=\sqrt V Z\), where \(Z\sim N(0,1)\) is independent of \(V\). Standard contraction of the backwards fundamental solution gives a unique stationary solution.

**2. Perpetuity tail.** Let \(T\sim\operatorname{Exp}(\lambda/s)\) be the first backward jump. Poisson independence and a split of the integral at \(T\) yield
\[
 V\overset d=A V'+B,\quad
 A=(1-s)^2e^{2\gamma T},\quad
 B=\frac{D}{\gamma}(e^{2\gamma T}-1),
\]
with \(V'\) an independent copy of \(V\), independent of the pair \((A,B)\). The pair itself need not have independent components. Its logarithmic mean is \(\mathbb E\log A=2\log(1-s)+2\gamma s/\lambda<0\). Also \(B>0\), the law of \(\log A\) is nonarithmetic, \(\mathbb P(A>1)>0\), and \(\mathbb P(Av+B=v)<1\) for any deterministic \(v\). For \(\rho>0\) with \(2\gamma\rho<\lambda/s\),
\[
 \mathbb E A^\rho=(1-s)^{2\rho}\frac{\lambda/s}{\lambda/s-2\gamma\rho}.
\]
Strict convexity and the negative logarithmic mean give a unique \(\rho>0\) with \(\mathbb E A^\rho=1\). This equation is precisely the displayed equation for \(p_s=2\rho\). At that root, \(\lambda/s-2\gamma\rho=(\lambda/s)(1-s)^{2\rho}>0\), which leaves a positive margin in the moment condition \(\mathbb E B^{\rho+\epsilon}<\infty\) for some \(\epsilon>0\); also \(\mathbb E[A^\rho\log^+A]<\infty\). Goldie's nonarithmetic implicit renewal theorem for positive affine perpetuities applies and gives \(\mathbb P(V>v)\sim C_Vv^{-\rho}\) with \(0<C_V<\infty\). Positivity follows from positive \(B\), nondegeneracy and positive probability of \(A>1\). Breiman's product-tail lemma, using Gaussian moments, then gives
\[
 \mathbb P(X>x)\sim C_V\,\mathbb E[(Z_+)^{p_s}]\,x^{-p_s},
\]
where \(Z_+=\max(Z,0)\). Symmetry supplies the negative tail. These standard heavy-tail theorems are credited as prior mathematical methods; the power-index equation in isolation is not presented as a new general theorem.

**3. Approximate tail and exact comparison.** The stationary zero-flux Fokker–Planck equation for \(Y\) gives
\[
 f_Y(y)=K(2D+\lambda s y^2)^{-1-(\lambda-\gamma)/(\lambda s)}.
\]
Its survival-tail index is \(q_s\). Define
\[
 \psi_s(u)=\gamma u+\frac\lambda s((1-s)^u-1),\qquad
 \psi_{\mathrm{DA}}(u)=(\gamma-\lambda)u+\frac{\lambda s}{2}u(u-1).
\]
Their positive zeros are \(p_s\) and \(q_s\), respectively; \(\psi_s(1)=\gamma-\lambda<0\). Taylor's theorem about \(s=0\), with the third derivative of \((1-s)^u\), shows at any \(u>1\): \(\psi_s(u)<\psi_{\mathrm{DA}}(u)\) for \(u>2\), the reverse for \(1<u<2\), and equality for \(u=2\). Both functions are negative between 1 and their unique zero above 1. Evaluate at \(u=q_s\) to obtain the asserted root ordering. Moreover \(q_s=2\) if and only if \(s=2(1-\gamma/\lambda)\).

**4. Exact moment agreements and failures.** Applying the exact jump generator to \(x^2\), and the approximate diffusion generator to \(x^2\), gives in both cases
\[
 \mathcal L x^2=2D+[2(\gamma-\lambda)+\lambda s]x^2.
\]
Finite second moments occur exactly when the corresponding survival exponent is greater than two; stationarity then proves the common formula. For fourth moments, both generators have source term \(12Dx^2\), while their coefficients multiplying \(x^4\) are
\[
 \psi_s(4)=4(\gamma-\lambda)+6\lambda s-4\lambda s^2+\lambda s^3,
 \quad \psi_{\mathrm{DA}}(4)=4(\gamma-\lambda)+6\lambda s.
\]
Therefore \(p_s>4\) iff \(\gamma/\lambda<b_{4,\mathrm{true}}\), while \(q_s>4\) iff \(\gamma/\lambda<b_{4,\mathrm{DA}}\). The strict gap between those boundaries is \(s^2-s^3/4>0\), establishing the moment-loss wedge. When both fourth moments exist,
\[
 \mathbb E[X^4]=\frac{12D\mathbb E[X^2]}{-\psi_s(4)},\qquad
 \mathbb E[Y^4]=\frac{12D\mathbb E[Y^2]}{-\psi_{\mathrm{DA}}(4)},
\]
and \(\psi_s(4)<\psi_{\mathrm{DA}}(4)<0\) gives the strict ordering. Exponent equality \(p_s=q_s=2\) coincides with the shared variance-divergence boundary.

**5. Weak-reset singularity.** Set \(b=\gamma/\lambda\), \(z_s=sp_s\). The root equation becomes \(bz_s=1-(1-s)^{z_s/s}\). Since \(\log(1-s)/s=-1-s/2+O(s^2)\), strict monotonicity of \((1-e^{-z})/z\) proves \(z_s\to c_b>0\). Implicit differentiation yields
\[
 z_s=c_b+s\frac{c_be^{-c_b}}{2(b-e^{-c_b})}+O(s^2).
\]
The denominator is positive at the nonzero crossing. Finally, \((1-e^{-u})/u>1-u/2\) for every \(u>0\), so at \(u=2(1-b)\) the decreasing left side is greater than \(b\); consequently \(c_b>2(1-b)\), proving the strict limiting ratio.

## Verification

The accompanying standalone `verify.py` uses deterministic bisection (rather than the analytical theorem) to cross-check the unique positive tail root, sign changes across the second-moment boundary, exact second moments from the perpetuity and the two generators, the nonempty fourth-moment wedge, finite fourth-moment inequalities, and weak-reset expansions over a grid of parameters. It prints a count of successful assertions. The exact comparison, affine-renewal tail law, and infinite-moment assertions rest on the preceding mathematical proof and Goldie's theorem, **not** on finite tests.

## Relationship to prior work

Galla (2026), arXiv:2602.21635v1, derives the weak-reset diffusion approximation and its affine-model stationary density (main-text Eq. (5), supplementary Eqs. (S1)–(S8)); those are prior results, not claimed new. Goldie's (1991) renewal theorem and the later generalized Ornstein–Uhlenbeck literature supply the general perpetuity heavy-tail mechanism; the existence of heavy tails and the affine tail-index root are not independently novel. Tal-Friedman, Roichman and Reuveni (2022) study partial resetting of drift diffusion with *constant* drift; Zanette and Manrubia (2020/2021) study multiplicative growth with full reinjection; neither inspected model derives the stated comparison against a second-order approximation. The contribution assessed here is the complete **finite-\(s\) tail-index reversal at the shared variance boundary**, its **nonempty fourth-moment-loss wedge**, and the **nonvanishing weak-reset exponent ratio** in this physically motivated linear model. The possibility of an equivalent comparison hidden in broader heavy-tail work is a residual originality risk.

## Limitations

This is a single-variable linear expanding-drift model with fixed proportional contractions, positive additive Brownian diffusivity, and homogeneous Poisson jumps. The tail coefficients are proved positive and finite but not evaluated in elementary closed form. Convergence of the stationary distribution at fixed spatial scales as \(s\to0\) is not quantified here. Limits in \(x\to\infty\) and \(s\to0\) need not commute; no uniform crossover-distance theorem is claimed. The Goldie theorem is a cited external theorem, not reproved here. The weak-reset diffusion approximation is used exactly as published, without asserting it accurately describes all rare events.

## References

1. T. Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1 (first posted 2026-02-25), especially Eq. (5), Sections A and S1.
2. C. M. Goldie, *Implicit renewal theory and tails of solutions of random equations*, Ann. Appl. Probab. **1** (1991), 126–166, doi:10.1214/aoap/1177005985.
3. G. Alsmeyer and A. Behme, *Tail behavior of Markov-modulated generalized Ornstein–Uhlenbeck processes*, arXiv:2601.09314v1 (2026).
4. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with partial resetting*, Phys. Rev. E **106** (2022), 054116; arXiv:2205.03363.
5. D. H. Zanette and S. Manrubia, *Fat tails and black swans: Exact results for multiplicative processes with resets*, Chaos **30** (2020), 033104; arXiv:2105.11679.
