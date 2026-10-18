# Universal critical aging limit and covariance transition in persistent walks

## Finding

**Functional critical-limit theorem.** Let \(c>0\), and let \((\xi_k)_{k\ge1}\) be independent Bernoulli random variables with deterministic probabilities \(0\le p_k\le1\) satisfying
\[
\lim_{k\to\infty}k p_k=c.
\]
Let the initial velocity \(V_0\in\{-1,+1\}\) be arbitrary and independent of these variables. Set \(V_k=V_{k-1}(-1)^{\xi_k}\), \(X_0=0\), and \(X_n=\sum_{k=1}^n V_k\). For each integer \(N\ge1\), let \(Y_N(t)\) be the piecewise-linear interpolation of \(X_{\lfloor Nt\rfloor}/N\) on \([0,\infty)\).

Let \((S(v))_{v\in\mathbb R}\) be a stationary symmetric two-state continuous-time Markov chain with states \(\{-1,+1\}\) and transition rate \(c\) in both directions. Define the continuous, 1-Lipschitz random function
\[
Y(t)=\int_0^t S(\log u)\,du,\qquad t\ge0,
\]
where the value at \(u=0\) is irrelevant. Then, **for every finite \(T>0\)**,
\[
Y_N\ \Longrightarrow\ Y\quad\text{in }C([0,T])
\]
with the uniform topology. In particular, the limit does not depend on any finite number of early reversal probabilities or on the initial-velocity distribution.

For every \(t>0\), \(Y(t)/t\) has density
\[
f_c(y)=\frac{\Gamma(c+\tfrac12)}{\sqrt\pi\,\Gamma(c)}(1-y^2)^{c-1}\,\mathbf 1_{(-1,1)}(y).
\]
Equivalently \((Y(t)/t+1)/2\) is \(\operatorname{Beta}(c,c)\). The density on \((-1,1)\), including its endpoint singularities for \(0<c<1\), is already known for the **continuous** Euler–Poisson–Darboux random flight [2]; the asserted new result is its **universal functional emergence from the discrete calendar-time reversal walk**, together with the exact two-time aging classification below. It must not be interpreted as a new formula for that continuous random flight.

For \(0<s\le t\), the limiting centered two-time displacement covariance is exactly
\[
C_c(s,t):=\operatorname{Cov}(Y(s),Y(t))=\frac{s^2}{2c+1}+\frac{s^{2c+1}}{2c+1}\int_s^t v^{-2c}\,dv.
\]
In particular, at the **distinct critical reversal coefficient** \(c=\tfrac12\),
\[
C_{1/2}(s,t)=\frac{s^2}{2}\left(1+\log(t/s)\right).
\]
For fixed \(s>0\) and \(t\to\infty\), the exact limiting-process covariance has the sharp trichotomy
\[
C_c(s,t)\sim\frac{s^{2c+1}}{(2c+1)(1-2c)}t^{1-2c}\quad(0<c<\tfrac12),
\]
\[
C_{1/2}(s,t)\sim\frac{s^2}{2}\log(t/s),\qquad
C_c(s,t)\longrightarrow\frac{2c\,s^2}{(2c-1)(2c+1)}\quad(c>\tfrac12).
\]
Here the long-lag limit is taken **after** the discrete-to-continuous scaling limit; no simultaneous-growing-lag error estimate is asserted for the original walk.

As an explicit finite-walk prediction, convergence of bounded moments yields
\[
\lim_{N\to\infty}\frac{\mathbb E[X_N^2]}{N^2}=\frac1{2c+1},\qquad
\lim_{N\to\infty}\frac{\mathbb E[X_N^4]}{N^4}=\frac3{(2c+1)(2c+3)},
\]
and hence the exact limiting Binder cumulant, in the normalization of [1],
\[
\lim_{N\to\infty}\left(1-\frac{\mathbb E[X_N^4]}{3(\mathbb E[X_N^2])^2}\right)=\frac2{2c+3}.
\]
Unlike the numerical crossing in [1], this fixes the full coefficient dependence under all independent protocols satisfying \(k p_k\to c\).

## Assumptions and scope

The increments \(\xi_k\) are *independent across calendar times*, with probabilities depending on the absolute step index and not on the duration of the current run. This is not the run-age-dependent persistent walk of [4]. The only large-index regularity is \(k p_k\to c\in(0,\infty)\); no summable error, monotonicity, or exact \(p_k=c/k\) identity is needed. Initial velocity is independent of future flips; it can be deterministic. Both states have speeds exactly one. The result concerns the one-dimensional model and the limits just specified.

## Proof

**1. Macroscopic reversal-point convergence.** Fix \(0<\varepsilon<T<\infty\). For disjoint intervals \((a_i,b_i]\subset[\varepsilon,T]\), the reversal counts
\[
N_{N,i}=\sum_{a_iN<k\le b_iN}\xi_k
\]
are independent. Their generating functions are products of the form \(\prod_k(1+p_k(z-1))\). From \(k p_k\to c\),
\[
\sum_{aN<k\le bN}p_k\longrightarrow c\log(b/a),\qquad
\sum_{aN<k\le bN}p_k^2\longrightarrow0.
\]
Therefore the finite-dimensional counting laws and, equivalently, the finite point processes on \([\varepsilon,T]\) converge to an inhomogeneous Poisson process of intensity \(c\,du/u\). This does not assert convergence on any neighborhood of zero, where the limiting process has infinitely many switches.

**2. Forgotten initial orientation.** Independence gives
\[
\mathbb E[V_{\lfloor\varepsilon N\rfloor}\mid V_0]
=V_0\prod_{k=1}^{\lfloor\varepsilon N\rfloor}(1-2p_k).
\]
For all sufficiently large indices, \(0<p_k<1/2\), and \(\sum_k p_k=\infty\). Consequently this product tends to zero. Since each velocity is \(\pm1\), \(V_{\lfloor\varepsilon N\rfloor}\) becomes asymptotically fair, independently of the future reversal counts. Thus on \([\varepsilon,T]\) the rescaled velocity field converges, in its finite-jump representation, to \(S(\log u)\): time-change \(u=e^v\) turns the intensity \(c\,du/u\) into constant rate \(c\,dv\), and the chain starts in its invariant fair sign law. The resulting laws agree for different choices of \(\varepsilon\), giving a two-sided stationary sign process \(S\).

**3. Tightness and removal of zero.** For fixed \(\varepsilon>0\), the finite-jump mapping to the time integral is continuous almost surely because a Poisson process places no jump at prescribed integration endpoints. For every \(t\in[0,T]\), the contribution from \([0,\varepsilon]\) to either scaled walk or limiting integral is bounded by \(\varepsilon+N^{-1}\). Accordingly the truncated integrals converge jointly at any finite collection of times as \(N\to\infty\), followed by \(\varepsilon\downarrow0\). Each interpolated \(Y_N\) is 1-Lipschitz and \(Y_N(0)=0\); its laws are tight in \(C([0,T])\) by Arzelà–Ascoli. The limiting \(Y\) is continuous. Finite-dimensional identification plus tightness proves the claimed functional convergence.

**4. Continuous-limit marginal without an unproved density assumption.** Let
\[
Z_v=\int_{-\infty}^{v}e^{-(v-w)}S(w)\,dw.
\]
The stationary process \((Z_v,S(v))\) has generator
\[
\mathcal L\varphi(z,\sigma)=(\sigma-z)\partial_z\varphi(z,\sigma)+c\bigl[\varphi(z,-\sigma)-\varphi(z,\sigma)\bigr].
\]
Consider the proposed joint invariant densities
\[
q_\sigma(z)=\frac{1+\sigma z}{2}\,f_c(z),\quad \sigma\in\{-1,1\},\quad-1<z<1.
\]
They are nonnegative and integrate to total mass one. Their probability fluxes at the boundaries vanish because \((1-z^2)f_c(z)\) is a constant multiple of \((1-z^2)^c\to0\). Direct integration by parts shows \(\sum_\sigma\int q_\sigma\mathcal L\varphi=0\), since
\[
\frac d{dz}\bigl[(1-z^2)f_c(z)\bigr]=-2czf_c(z).
\]
This supplies an invariant probability without supposing in advance that the stationary law has a density. Uniqueness follows by coupling two two-state chains after their finite meeting time and then applying the exponential contraction of \(\dot Z=S-Z\). Since the explicit pullback process is stationary, its marginal is \(f_c\). The substitution \(u=e^w\) shows \(Y(1)=Z_0\); stationarity of \(S\) under logarithmic translations gives \(Y(t)/t\stackrel d=Y(1)\). This proves the beta law and excludes boundary atoms.

**5. Aging covariance.** For \(u,v>0\), the two-state chain correlation is
\[
\mathbb E[S(\log u)S(\log v)]
=e^{-2c|\log u-\log v|}
=\left(\frac{\min(u,v)}{\max(u,v)}\right)^{2c}.
\]
The means vanish and all integrands are bounded, justifying Fubini. In particular,
\[
\mathbb E[Y(s)^2]
=2\int_0^s\int_0^v(u/v)^{2c}\,du\,dv=\frac{s^2}{2c+1}.
\]
For \(v\ge s\), the additional increment has cross-covariance
\[
\mathbb E[Y(s)S(\log v)]
=\int_0^s (u/v)^{2c}\,du
=\frac{s^{2c+1}}{(2c+1)v^{2c}}.
\]
Integration from \(s\) to \(t\) proves the exact covariance formula. Evaluating the elementary power integral (or logarithm at \(2c=1\)) gives the stated long-lag trichotomy. No claim of independent increments or convergence to an ordinary stationary displacement process is made.

**6. Moments and Binder coefficient.** The beta integral gives \(\mathbb E[Y(1)^2]=1/(2c+1)\) and \(\mathbb E[Y(1)^4]=3/((2c+1)(2c+3))\). Since \(|Y_N(1)|\le1\), functional weak convergence implies convergence of each fixed moment. Substitution gives the stated Binder limit.

## Verification

The accompanying pure-Python program `verify_limit.py` reproduces **53 deterministic finite-step and integral assertions**. It evolves the exact joint moment recursions through order four for five values of \(c\), uses a smooth legal protocol \(p_k=c/(k+2c)\), and independently evaluates selected finite-step unequal-time covariances by propagating the velocity correlation product. It compares these with the beta moment formulas and the explicit aging covariance; a separate numerical integral checks the covariance expression and density normalization for selected parameters. In the current environment, it completed with output `PASS: 53 deterministic finite-step and integral checks`. These are finite consistency tests, not a replacement for Steps 1–6. Run with `python3 verify_limit.py`; only the Python standard library is needed.

## Relationship to prior work

Pradhan, Roy, and Ray [1] introduce precisely the calendar-time dependent independent reversal model, identify the change at the critical power, and establish the asymptotic second moment \(\mathbb E[X_N^2]/N^2\to1/(2c+1)\). Their treatment of the broad critical displacement distribution and Binder crossing is numerical. Neither that established variance nor the power-law transition is claimed as new here. The new discrete statement is a functional convergence theorem under the sharp universality assumption \(k p_k\to c\), with exact higher-moment and aging consequences.

Garra and Orsingher [2, Eq. (1.5), (2.7)] already obtain the identical beta-shaped one-time density **exactly** for the continuous finite-velocity random flight whose switching intensity is \(c/t\); they also identify the familiar arcsine, uniform, and bell-shaped regimes. The matching density, its shape transition, and those continuous equations are **prior results**. They do not in the examined sections prove convergence of independent Bernoulli calendar-time walks under \(k p_k\to c\), or state the above two-time covariance threshold for that discrete scaling limit. The proof here makes the discrete-to-continuous connection and its multitime consequences explicit. Angelani and Garra [3] analyze general time-dependent telegraph-rate equations and different solvable protocols, rather than a discrete universal functional limit. The run-age dependent model of Cénac and coauthors [4] has a different clock and addresses recurrence classification.

## Limitations

The claim requires independence of reversal indicators and a fixed limiting positive coefficient \(c\); it does not cover correlated flips, random environments, state-dependent hazards, or multidimensional orientation rules. The beta density is established prior theory for a related continuous model; the originality claim deliberately excludes that known formula in isolation. A broader published functional invariance principle for rare inhomogeneous switches could subsume the present discrete theorem; such implicit coverage is a residual literature risk. The critical aging crossover concerns the **limiting process first**, not an unproved simultaneous long-lag limit for finite \(N\). No independent scientific audit or experimental validation has been performed.

## References

[1] A. Pradhan, R. Roy, P. Ray, *Diffusive-to-Ballistic transition in a Persistent Random Walk*, arXiv:2605.20116v1, first public 2026-05-19, https://arxiv.org/abs/2605.20116 .

[2] R. Garra and E. Orsingher, *Random flights related to the Euler-Poisson-Darboux equation*, arXiv:1411.0648; *Markov Processes and Related Fields* 22 (2016), 87–110, https://arxiv.org/abs/1411.0648 .

[3] L. Angelani and R. Garra, *Probability distributions for the run-and-tumble models with variable speed and tumbling rate*, *Modern Stochastics: Theory and Applications* 6 (2019), 3–12, DOI:10.15559/18-VMSTA127, https://www.vmsta.org/journal/VMSTA/article/141/read .

[4] P. Cénac, B. de Loynes, A. Le Ny and Y. Offret, *Persistent random walks*, arXiv:1509.03882, https://arxiv.org/abs/1509.03882 .
