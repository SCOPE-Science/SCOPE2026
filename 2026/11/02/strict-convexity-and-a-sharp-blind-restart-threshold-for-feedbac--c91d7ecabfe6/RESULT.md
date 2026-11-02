# Strict convexity and a sharp blind-restart threshold for feedback-reset Brownian search

## Finding

A Brownian searcher with an absorbing target may be reset to its initial position by two independent mechanisms: a *feedback* clock of rate \(r>0\), acting only when its position is negative, and a *blind* clock of rate \(\rho\geq0\), acting regardless of position. For any fixed feedback rate, the mean completion time is a **strictly convex function of the blind-resetting rate**. Consequently, blind resetting has a unique strictly positive global optimum precisely below a sharp feedback-strength threshold. It is globally detrimental at or above the threshold; no disconnected, first-order optimum can survive.

Put \(t_0=L^2/D\), \(w=L\sqrt{r/D}>0\), \(s=\rho L^2/D\geq0\) and \(\mathcal T(s,w)=\mathbb E\tau_{\rho,r}/t_0\). Then
\[
\mathcal T(s,w)=\frac{\cosh\sqrt{s}-1}{s}+\frac{\sinh\sqrt{s}}{\sqrt{s}\sqrt{s+w^2}},
\qquad \mathcal T(0,w)=\frac12+\frac1w,
\]
with continuous interpretation at \(s=0\). For every \(w>0\), \(\partial_s^2\mathcal T(s,w)>0\) for all \(s\geq0\).

Let \(w_c\) be the unique positive root of \(w^3+4w^2-12=0\), numerically \(w_c=1.479815748755\ldots\), and put \(r_c=w_c^2D/L^2=2.189854650264\ldots D/L^2\). If \(0<r<r_c\), exactly one \(\rho_*(r)>0\) globally minimizes the mean, and this strictly improves upon \(\rho=0\). If \(r\geq r_c\), the unique optimum is \(\rho_*=0\), and every positive blind-reset rate strictly increases the mean.

The transition from the interior-optimum side is continuous and has the explicit first-order law
\[
\frac{L^2}{D}\rho_*(r)
=C\bigl(w_c-L\sqrt{r/D}\bigr)
+O\!\left(\bigl(w_c-L\sqrt{r/D}\bigr)^2\right),\qquad
C=3.465571330427\ldots,
\]
where \(C=a_1'(w_c)/(2a_2(w_c))\), \(a_1(w)=1/24+1/(6w)-1/(2w^3)\), and \(a_2(w)=1/720+1/(120w)-1/(12w^3)+3/(8w^5)\). In particular, the optimized dimensionless mean improves over its no-blind-reset value by \(0.410127978679\ldots(w_c-w)^2+O((w_c-w)^3)\) near the threshold from below.

## Assumptions and scope

Fix \(D>0\), \(L>0\) and feedback rate \(r>0\). Starting at \(X_0=0\), the position follows \(dX_t=\sqrt{2D}\,dB_t\) between jumps. A rate-\(r\) independent Poisson clock instantaneously sends \(X_t\) to \(0\) only if \(X_{t-}<0\) (events at nonnegative positions are ignored). A second independent rate-\(\rho\) Poisson clock always sends \(X_t\) to \(0\). The experiment ends at \(\tau_{\rho,r}=\inf\{t\geq0:X_t=L\}\), with the target absorbing. Reset times take no physical time; the Brownian and Poisson drivers are mutually independent. At \(\rho=0\) the second clock is absent. There is no drift, refractory time, energy cost, or dependence on unobserved history.

All inequalities and uniqueness statements are for every real \(D,L,r\) in the stated domain, not a parameter grid. The critical rate is for *fixed* feedback strength, optimizing only the second, unconditional clock.

## Proof

**1. The one-clock first-passage transform.** Let \(H_r=\tau_{0,r}\), and \(u_\lambda(x)=\mathbb E_x[e^{-\lambda H_r}]\), \(\lambda>0\). On the negative half-line the backward equation is
\[
D u_\lambda''-(r+\lambda)u_\lambda+r u_\lambda(0)=0.
\]
Boundedness as \(x\to-\infty\) yields
\[
u_\lambda(x)=u_\lambda(0)\left[\frac r{r+\lambda}+\frac\lambda{r+\lambda}
 e^{x\sqrt{(r+\lambda)/D}}\right],\qquad x<0,
\]
and hence \(u_\lambda'(0-)=\lambda u_\lambda(0)/\sqrt{D(r+\lambda)}\). On \((0,L)\), \(Du_\lambda''=\lambda u_\lambda\), with continuous derivative at zero and \(u_\lambda(L)=1\). Thus
\[
\phi_r(\lambda)=u_\lambda(0)=
\left[\cosh\!\left(L\sqrt{\lambda/D}\right)
+\sqrt{\frac\lambda{\lambda+r}}\sinh\!\left(L\sqrt{\lambda/D}\right)\right]^{-1}.
\]
This agrees with the first-passage transform implied by the known smart-reset propagator. The bounded solution of these elliptic equations is the hitting-time Laplace transform by the stopped-process Feynman–Kac/backward argument.

**2. Addition of the blind clock.** Before each independent outer reset, the feedback process restarts afresh from zero. With \(E_\rho\sim\operatorname{Exp}(\rho)\) independent of \(H_r\), the success probability of an attempt is \(\phi_r(\rho)\), and its mean duration is \((1-\phi_r(\rho))/\rho\). The renewal identity gives
\[
\mathbb E\tau_{\rho,r}=\frac{1-\phi_r(\rho)}{\rho\phi_r(\rho)}
\quad(\rho>0),
\]
which simplifies exactly to the displayed \(\mathcal T(s,w)\). The continuous \(\rho\downarrow0\) limit gives \(\mathcal T(0,w)=1/2+1/w\). An independent check comes from the combined backward mean equation: on \(x<0\), \(D m''-(r+\rho)(m-m(0))=-1\), and on \(0<x<L\), \(D m''-\rho(m-m(0))=-1\), with \(m(L)=0\), \(m\) and \(m'\) continuous at zero. Solving gives the same formula.

**3. Strict convexity.** Define the entire functions
\[
A(s)=\frac{\cosh\sqrt{s}-1}{s}=
\sum_{n=0}^\infty\frac{s^n}{(2n+2)!},\qquad
G(s)=\frac{\sinh\sqrt{s}}{\sqrt{s}}=
\sum_{n=0}^\infty\frac{s^n}{(2n+1)!}.
\]
Then \(\mathcal T(s,w)=A(s)+G(s)(s+w^2)^{-1/2}\), and \(A''(s)>0\) for \(s\geq0\). The canonical product of the hyperbolic sine is
\[
G(s)=\prod_{n=1}^\infty\left(1+\frac{s}{\pi^2n^2}\right).
\]
For \(k=1,2,3\), set \(Q_k(s)=\sum_{n=1}^\infty(s+\pi^2n^2)^{-k}\). The series are absolutely convergent on \(s\geq0\). Logarithmic differentiation gives \(G'/G=Q_1\), \(G''/G=Q_1^2-Q_2>0\). Cauchy–Schwarz implies \(Q_2^2\leq Q_1Q_3\), whence
\[
\frac{d}{ds}\frac{Q_2}{Q_1^2}=
\frac{2(Q_2^2-Q_1Q_3)}{Q_1^3}\leq0.
\]
The classical sums \(Q_1(0)=1/6\) and \(Q_2(0)=1/90\) therefore imply \(Q_2/Q_1^2\leq2/5\), or, equivalently,
\[
\frac{(G')^2}{GG''}\leq\frac53.
\]
With \(v=s+w^2>0\), differentiation twice yields
\[
\frac{d^2}{ds^2}\!\left(G(s)v^{-1/2}\right)
=\frac{v^2G''-vG'+3G/4}{v^{5/2}}.
\]
Completing the square and using the last inequality gives
\[
 v^2G''-vG'+\frac34G
=G''\left(v-\frac{G'}{2G''}\right)^2
+\frac34G-\frac{(G')^2}{4G''}
\geq\frac13G>0.
\]
Consequently both summands of \(\mathcal T\) are strictly convex, and so is \(\mathcal T(\cdot,w)\) on all \([0,\infty)\).

**4. The unique optimum and threshold.** Expansion at zero gives
\[
\mathcal T(s,w)=\frac12+\frac1w+a_1(w)s+a_2(w)s^2+O_w(s^3),
\qquad a_1(w)=\frac{w^3+4w^2-12}{24w^3}.
\]
The cubic \(w^3+4w^2-12\) is strictly increasing on \((0,\infty)\), negative at zero and positive at two; it therefore has exactly one positive root \(w_c\). If \(w\ge w_c\), strict convexity and \(\partial_s\mathcal T(0,w)\ge0\) show that \(s=0\) is the unique minimizer. If \(0<w<w_c\), the initial derivative is negative. Meanwhile \(\mathcal T(s,w)\ge A(s)\to\infty\) as \(s\to\infty\), so strict convexity gives exactly one global minimizer \(s_*(w)>0\). The strict improvement follows from the negative initial slope.

**5. Critical scaling.** At \((s,w)=(0,w_c)\), the second derivative is \(2a_2(w_c)>0\), and \(a_1'(w_c)=(9-w_c^2)/(6w_c^4)>0\). Apply the implicit-function theorem to \(\partial_s\mathcal T(s,w)=0\), using the analytic extension near \(s=0\) (valid for \(|s|<w_c^2\)). This yields
\[
s_*(w)=\frac{a_1'(w_c)}{2a_2(w_c)}(w_c-w)+O((w_c-w)^2)
\]
as \(w\uparrow w_c\). Substitution into the Taylor series gives the quadratic optimal-gain expansion with coefficient \((a_1'(w_c))^2/[4a_2(w_c)]\).

## Verification

The standalone program `check_hybrid.py` checks the two independent backward/renewal formulations against each other, numerical positivity of the derived curvature expression, the derivative threshold, strict sample comparisons, and the critical scaling for several dimensionless parameter choices. Run `python3 check_hybrid.py` with standard Python 3; no third-party libraries are required. Its finite tests are diagnostics only. The global statement is proved by the infinite-product inequality and convexity argument above.

## Relationship to prior work

Tal-Friedman, Keidar, Reuveni and Roichman [1] derive the one-sided feedback model, its first-passage transform and its mean at a single feedback rate. Those facts are input, not claimed as new. Plata, Gupta and Azaele [2] study a closely related asymmetric threshold-reset diffusion and provide general one-clock first-passage methods. Pal and Reuveni [3] give general renewal-restart identities and local restart criteria. The new statement concerns an *independent second reset mechanism* added to the smart-feedback process: exact strict convexity in its rate, a global (not merely infinitesimal) uniqueness classification, and the critical optimum/gain asymptotics. Neither the one-clock Laplace transform alone nor the generic local coefficient-of-variation test states this global classification.

Searches did not identify a directly encompassing published theorem, but non-indexed or inaccessible sources can affect publication priority. In particular, complete text of [2] and [3] was not available for full comparison; the accessible abstract and record were compared, and this limitation should be checked independently before asserting publication priority.

## Limitations

The result assumes zero-duration, complete position resets to the same start, independent exponential clocks, constant diffusion coefficient, zero drift and one absorbing target. It does not optimize energetic cost, trajectories under feedback delay, or arbitrary resetting-time laws. Strict convexity in the blind-reset rate is special to this model and is not asserted for every completion-time distribution. The first derivative of the mean at zero blind-reset rate gives only a *local* criterion in general; the product argument is essential for the global conclusion here.

## References

1. O. Tal-Friedman, T. D. Keidar, S. Reuveni and Y. Roichman, *Smart Resetting: An Energy-Efficient Strategy for Stochastic Search Processes*, arXiv:2409.10108v1, 16 September 2024, https://arxiv.org/html/2409.10108v1.
2. C. A. Plata, D. Gupta and S. Azaele, *Asymmetric Stochastic Resetting: Modeling Catastrophic Events*, arXiv:2007.12417, 24 July 2020, https://arxiv.org/abs/2007.12417.
3. A. Pal and S. Reuveni, *First Passage Under Restart*, arXiv:1607.06048, 20 July 2016, https://arxiv.org/abs/1607.06048.
