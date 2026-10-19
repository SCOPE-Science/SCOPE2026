# Universal successful-excursion marks and an exponentially accurate ring-to-line approximation

## Finding

For a Brownian search on a circle with a point target and independent Poisson relocation to a spatial density whose two target-side limits have a common power exponent, the starting distance and travel time of the *eventual successful excursion* possess a joint, universal high-rate law. Both its marginals are Gamma, but they are correlated: the limiting correlation between the rescaled reset-to-target distance and successful-excursion duration equals \(1/\sqrt{2}\), for **every** admissible local density exponent. The sign of the reset side is asymptotically independent of both, with probabilities fixed by the two local density coefficients. For a natural symmetric power-density family, convergence of the *entire joint marked law* is exponentially fast in total variation, with an explicit nonasymptotic bound. A target-density power threshold separates vanishing, finite and diverging mean search time under arbitrarily rapid resetting.

**The asserted contribution is the joint asymptotic marked law and the quantitative total-variation bound, not the already-known general renewal formula, final-reset-point weighting, or unmarked exponential search-time limit.**

Let \(\beta>0\) and write \(q=\sqrt{r/D}\). Denote the distance and duration of the terminal successful excursion by \(d_*\) and \(H_*\), and its starting side by \(S_*\in\{+,-\}\). As \(r\to\infty\),
\[
(qd_*,rH_*,S_*)\ \Longrightarrow\ (Z,U,S),
\qquad
\mathbb E[e^{-tZ-sU}]=(t+\sqrt{1+s})^{-\beta}\quad(t,s\geq0).
\]
Here \(Z\sim\operatorname{Gamma}(\beta,1)\), \(U\sim\operatorname{Gamma}(\beta/2,1)\), and \(\operatorname{Corr}(Z,U)=1/\sqrt2\). The joint density is
\[
 f_\beta(z,u)=\frac{z^{\beta}}{\Gamma(\beta)\sqrt{4\pi}\,u^{3/2}}
 \exp\!\left(-u-\frac{z^2}{4u}\right),\qquad z,u>0.
\]
The variable \(S\) is independent of \((Z,U)\).

## Assumptions and scope

Fix a circle of circumference \(C=2a>0\), a single perfectly absorbing target at arclength \(0\equiv 2a\), and a diffusion coefficient \(D>0\). Between resets the motion has generator \(D\partial_{yy}\) on \((0,2a)\). At time zero and at each subsequent point of an independent rate-\(r\) Poisson process, select a fresh independent location with normalized Lebesgue density \(\rho\) on \((0,2a)\). Brownian trajectories in successive segments are independent. Let \(\delta(y)=\min(y,2a-y)\). The side \(+\) refers to \(y<a\), and \(-\) to \(y>a\). The terminal successful excursion is the first segment to hit the target before its next resetting clock; its starting distance, duration and side are \((d_*,H_*,S_*)\). The initial segment counts as a renewal segment, whether or not any physical reset has yet occurred.

Assume there exist a common \(\beta>0\) and constants \(c_+,c_-\geq0\), \(c=c_++c_->0\), such that, in the density sense as \(y\downarrow0\),
\[
 \rho(y)=c_+y^{\beta-1}+o(y^{\beta-1}),\qquad
 \rho(2a-y)=c_-y^{\beta-1}+o(y^{\beta-1}).
\]
No condition beyond nonnegativity, measurability and integrability is needed away from the target. In particular, \(\beta<1\) permits an integrable density cusp, and a zero side coefficient is permitted. There is no atom at the target. Throughout, \(\operatorname{Gamma}(k,1)\) denotes shape \(k\), rate \(1\).

Write \(\tau_y\) for the target-hitting time in an excursion without resetting, and let \(p_r=\int_0^{2a}\rho(y)\,\mathbb E_y[e^{-r\tau_y}]\,dy\). Then
\[
 p_r\sim c\Gamma(\beta)\left(\frac Dr\right)^{\beta/2},\quad
 \mathbb E[T_r]=\frac{1-p_r}{rp_r}
 \sim\frac{r^{\beta/2-1}}{c\Gamma(\beta)D^{\beta/2}}.
\]
Hence the high-reset mean tends to zero for \(\beta<2\), to \(1/(cD)\) for \(\beta=2\), and to infinity for \(\beta>2\). These mean-asymptotic implications are included to interpret the marked theorem; the elementary renewal identity is prior art. The high-rate law for \(rp_rT_r\) is also known in general resetting theory; the additional joint statement here identifies its independence from the successful marks:
\[
 (rp_rT_r,qd_*,rH_*,S_*)\Longrightarrow(E,Z,U,S),
 \qquad E\sim\operatorname{Exp}(1),\quad E\perp(Z,U,S).
\]

**Quantitative power-density specialization.** Let \(\rho(y)=\beta\delta(y)^{\beta-1}/(2a^\beta)\), so each side is equally likely. Put \(x=a\sqrt{r/D}\), and let \(P_r\) be the joint law of \((qd_*,rH_*,S_*)\), while \(P_\infty\) is the limiting joint law above with an independent fair side sign. For every \(x\geq2\beta+2\),
\[
\boxed{\ 
\|P_r-P_\infty\|_{\mathrm{TV}}\ \leq\
4\left[\frac{x^{\beta}e^{-x}}{\Gamma(\beta+1)(1-e^{-4x})}
+\frac{\Gamma(\beta,x)}{\Gamma(\beta)}\right].\ }
\]
Here \(\Gamma(\beta,x)=\int_x^\infty u^{\beta-1}e^{-u}\,du\). Total variation is \(\sup_A|P_r(A)-P_\infty(A)|\). In particular, the error is \(O_\beta(x^\beta e^{-x})\) as \(x\to\infty\); the bound applies simultaneously to location, duration and side, not just their marginals.

## Proof

**1. The single-segment transform.** Unwrap the circle at the target to the absorbing interval \((0,2a)\). The solution of \(D h''=s h\), with \(h(0)=h(2a)=1\), is
\[
 h_s(y)=\mathbb E_y[e^{-s\tau_y}]
 =\frac{\cosh(\sqrt{s/D}(a-\delta(y)))}{\cosh(a\sqrt{s/D})}
 =\frac{e^{-q_s\delta(y)}+e^{-q_s(2a-\delta(y))}}{1+e^{-2aq_s}},
 \quad q_s=\sqrt{s/D}.
\]
For each positive \(r\), independently sample \(Y\sim\rho\), its Brownian hitting time \(\tau_Y\), and its exponential resetting clock \(R\sim\operatorname{Exp}(r)\). Success \(\{\tau_Y<R\}\) has probability \(p_r\). Conditioning a geometric sequence of independently repeated trials on its first success shows that the terminal segment has the exact marked transform
\[
 \mathbb E[e^{-tqd_*-srH_*}\mathbf 1_{\{S_*=+\}}]
 =\frac{1}{p_r}\int_0^a \rho(y)e^{-tqy}h_{r(1+s)}(y)\,dy.
\]
For the other side, replace \(\rho(y)\) by \(\rho(2a-y)\). This is a conditional-success formula; the successful duration is \(\tau_Y\), not the whole process's first-arrival time.

**2. Local Laplace asymptotics.** For fixed \(t,s\geq0\), the integral on side \(+\) is asymptotic, after \(z=qy\), to
\[
 c_+q^{-\beta}\int_0^\infty z^{\beta-1}
 e^{-(t+\sqrt{1+s})z}\,dz
 =c_+q^{-\beta}\Gamma(\beta)(t+\sqrt{1+s})^{-\beta}.
\]
The same calculation holds on side \(-\). To justify domination, choose a fixed small \(\epsilon>0\); the density on \((0,\epsilon)\) is bounded by a constant times \(y^{\beta-1}\) on each side, whereas the contribution of \(\delta\geq\epsilon\) is bounded by an exponentially small multiple of \(\int\rho=1\). The second image term in \(h_s\) is likewise exponentially small. At \(t=s=0\) this gives \(p_r\sim c\Gamma(\beta)q^{-\beta}\). After division by \(p_r\), the limiting joint Laplace transform including the side sign equals \((c_\pm/c)(t+\sqrt{1+s})^{-\beta}\). Continuity of Laplace transforms implies joint weak convergence and asymptotic independence of the side sign.

**3. Marginals, density and correlation.** The half-line Brownian first-passage density from rescaled distance \(z>0\), written in rescaled time \(u>0\), is
\[
 \frac{z}{\sqrt{4\pi}\,u^{3/2}}\exp\!\left(-\frac{z^2}{4u}\right).
\]
Under the independent rate-one exponential kill, multiply by \(e^{-u}\), then weight starting sites by \(z^{\beta-1}/\Gamma(\beta)\). This produces exactly \(f_\beta\), normalized by the well-known hitting-time transform \(\int_0^\infty e^{-su}f_{\mathrm{hit}}(u\mid z)du=e^{-z\sqrt{s}}\). Setting \(s=0\) gives the Gamma density \(z^{\beta-1}e^{-z}/\Gamma(\beta)\) for \(Z\); setting \(t=0\) gives \((1+s)^{-\beta/2}\), the Laplace transform of \(\operatorname{Gamma}(\beta/2,1)\) for \(U\). Conditional on \(Z=z\), \(U\) has transform \(\exp[-z(\sqrt{1+s}-1)]\); therefore
\[
 \mathbb E[U\mid Z=z]=z/2,\quad
 \operatorname{Var}(U\mid Z=z)=z/4,\quad
 \operatorname{Cov}(Z,U)=\beta/2.
\]
Since \(\operatorname{Var}(Z)=\beta\) and \(\operatorname{Var}(U)=\beta/2\), the correlation is \(1/\sqrt2\). All these are properties of the limiting law; a finite-rate convergence-of-correlations assertion is not needed.

**4. Independence from the total search clock.** Let \(A_r\) denote the sum of the durations of *failed* segments before the terminal successful segment. Independence of renewal trials gives independence of \(A_r\) and the terminal successful marks already at finite \(r\). For \(h\geq0\), a failed segment has exponential-duration Laplace contribution \(r(1-p_{r+h})/(r+h)\), and a geometric sum yields
\[
 \mathbb E[e^{-h A_r}]
 =\frac{p_r}{1-\frac{r}{r+h}(1-p_{r+h})}.
\]
For \(h=\theta rp_r\), \(\theta\geq0\), the established regular variation \(p_r\sim\mathrm{constant}\,r^{-\beta/2}\) implies \(p_{r(1+\theta p_r)}/p_r\to1\) and \(p_r\to0\). Therefore \(\mathbb E[e^{-\theta rp_rA_r}]\to(1+\theta)^{-1}\). Since \(T_r=A_r+H_*\) and \(rp_rH_*=p_r(rH_*)\to0\) in probability by tightness, the claimed joint limit and independence follow. The unmarked exponential limit is consistent with the more general frequent-resetting results of Linn and Lawley.

**5. Explicit total-variation inequality.** Consider the specialized symmetric density. On each sampled side, couple circle Brownian motion started at distance \(d\in(0,a)\) to Brownian motion on the half-line starting at the same distance from the *near* target endpoint, using the identical Brownian path and the identical exponential resetting clock. Their successful-excursion outcome and duration agree unless the circle path hits the *opposite* endpoint of the unwrapped interval before its near endpoint and before reset. The probability of that exceptional event, conditional on \(d\), is
\[
 b_q(d)=\mathbb E_d[e^{-r\tau_{2a}};\tau_{2a}<\tau_0]
 =\frac{\sinh(qd)}{\sinh(2aq)}\leq\frac{e^{-x}}{1-e^{-4x}}
 \quad(0<d<a,\ x=aq).
\]
Let \(\mu_r\) be the unnormalized finite-circle successful marked measure, \(\nu_{<a}\) its coupled half-line measure with starting distances truncated at \(a\), and \(\nu_\infty\) the half-line measure with the same power intensity continued to \((0,\infty)\). The half-line mass is \(m_\infty=\Gamma(\beta+1)x^{-\beta}\), and its omitted fraction from \(d>a\) is \(Q(\beta,x)=\Gamma(\beta,x)/\Gamma(\beta)\). The coupling and triangle inequality give
\[
 \sup_A|\mu_r(A)-\nu_\infty(A)|
 \leq \frac{e^{-x}}{1-e^{-4x}}+m_\infty Q(\beta,x).
\]
Furthermore \(h_r(y)\geq e^{-q\delta(y)}\) for \(0<\delta(y)<a\), so the ring successful mass satisfies \(p_r\geq m_\infty[1-Q(\beta,x)]\). If \(x\ge2\beta+2\), Markov's inequality for \(\operatorname{Gamma}(\beta,1)\) yields \(Q(\beta,x)\leq\beta/x<1/2\), hence \(p_r\geq m_\infty/2\). Normalizing both finite measures increases total variation by at most twice the unnormalized discrepancy divided by \(p_r\). Combining these bounds gives exactly the displayed factor-four inequality. For fixed \(\beta>0\), the upper-Gamma tail is \(O_\beta(x^{\beta-1}e^{-x})\), proving the asserted exponential accuracy.

**6. The mean-time threshold.** The expected elapsed time in one renewal trial is \(\mathbb E\min(\tau_Y,R)=(1-p_r)/r\); geometric renewal then gives \(\mathbb E T_r=(1-p_r)/(rp_r)\). Substitution of the result of Step 2 proves the three regimes with threshold \(\beta=2\), equivalently density exponent \(\beta-1=1\). For \(\beta>2\), the finite mean at zero resetting (bounded circle) and divergence for large resetting imply existence of a global minimum over finite rates, potentially at rate zero; uniqueness or strict positivity of that minimizer is **not** asserted.

## Verification

`CHECK.py` is standalone Python 3 code requiring only its standard library. It computes finite-circle success transforms by independent composite-Simpson quadrature, tests the exact uniform-reset transform against \(\tanh(aq)/(aq)\), checks the predicted power-law and joint Laplace transforms across seven density powers, verifies moment identities, and compares exact ring success masses with the coupling/upper-Gamma bounds in four integer-power cases. Executing `python CHECK.py` in the delivered package produced `PASS: 219 deterministic tests; no analytical limit inferred from these checks.` The analytical argument above, rather than finite numerical evidence, proves the claims for all stated parameters.

## Relationship to prior work

Julián-Salgado, Castro-Villarreal, Dagdug and Boyer (2026), arXiv:2605.08414v1, derive general distributed-resetting survival and averaged first-passage formulas on a ring and study optimal rates for two discrete resetting sites. Those exact renewal formulas are **prior work**. Julián-Salgado, Dagdug and Boyer (2025), arXiv:2507.14483, Section V, explicitly derive a general finite-rate distribution of the **last resetting position**, including its product weighting by the underlying first-passage Laplace transform; they also print the Brownian Lévy–Smirnov hitting density. Their last-position formula implies the finite-rate starting-position marginal used here, and no independent novelty is claimed for it. The 2025 article focuses on resetting distributions *with support away from the target*, and neither the full joint fast-reset duration/location limit with its universal correlation nor the explicit exponentially accurate ring-to-line total-variation bound was identified in its results. Méndez, Flaquer-Galmés and Campos (2024) and Toledo-Marín and Boyer (2022) derive distributed-resetting first-passage renewal frameworks. Linn and Lawley (2023) already prove a general unmarked frequent-reset exponential limiting arrival time. The new conclusion is the *marked terminal segment* law, an explicit joint quantitative error bound for the natural power family, and their local-density threshold interpretation.

## Limitations

The theorem requires independent Brownian segments, memoryless Poisson resets, a single absorbing point on a fixed circle, a common density exponent on the two target sides, and constant diffusion coefficient. For the general near-target density assumption the joint law is weak, not a claimed total-variation convergence rate; the quantitative error bound holds only for the displayed symmetric pure-power family. The bound is for the successful *segment's marks*, not for the whole spatial trajectory. The exact finite-reset last-reset position weighting and the unmarked search-time limit are established by prior literature. The result does not establish stability to a noisy or time-dependent reset distribution, interacting particles, finite-measurement estimation error, or the uniqueness of an optimal finite rate. Some general renewal/first-passage transforms could subsume parts of the joint law implicitly; an independent novelty audit remains to be performed.

## References

1. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug and D. Boyer, *Mirror transitions in diffusion with stochastic resetting confined on a ring*, arXiv:2605.08414v1, first public 2026-05-08. https://arxiv.org/abs/2605.08414
2. P. Julián-Salgado, L. Dagdug and D. Boyer, *Abrupt transitions in the optimization of diffusion with distributed resetting*, arXiv:2507.14483 (2025), particularly Section V and Eqs. (26)–(29). https://arxiv.org/abs/2507.14483
3. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125 (2024). https://arxiv.org/abs/2401.01125
4. J. Q. Toledo-Marín and D. Boyer, *First passage time and information of a one-dimensional Brownian particle with stochastic resetting to random positions*, arXiv:2206.14387 (2022). https://arxiv.org/abs/2206.14387
5. S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, arXiv:2302.05409 (2023). https://arxiv.org/abs/2302.05409
6. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225 (2011). https://arxiv.org/abs/1107.4225
