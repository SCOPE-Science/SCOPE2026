# Early–late reversal of the middle arrival under simultaneous stochastic resetting

## Finding

**Theorem (protocol reversal at the first interior arrival rank).** Fix a target distance \(d>0\), diffusivity \(D>0\), and reset rate \(r>0\). Three labeled particles, initially at \(d\), move as independent Brownian motions with generator \(D\partial_x^2\) until their individual first hits of the target \(0\). Compare two protocols at the *same per-particle reset rate*: (I) independent rate-\(r\) Poisson clocks reset the three positions to \(d\); (G) one rate-\(r\) Poisson clock resets all three positions simultaneously to \(d\). The clocks are independent of all Brownian noises. Previously recorded first-hit events remain recorded after any reset. Write \(T_{(1)}\le T_{(2)}\le T_{(3)}\) for the ordered **first** hits and use superscripts \(\mathrm I\) and \(\mathrm G\) for the protocols.

The two middle-arrival distributions cannot be stochastically ordered. In fact, for every \(0<t<d^2/(6D)\),
\[
 \Pr(T^{\mathrm G}_{(2)}\le t)>\Pr(T^{\mathrm I}_{(2)}\le t).
\]
For all sufficiently large \(t\), the inequality is **reversed**. More precisely, let
\[
 q_0(t)=\operatorname{erf}\!\left(\frac d{\sqrt{4Dt}}\right),\qquad t>0,
\]
and, for \(j=1,2\), let \(\theta_j\in(0,r)\) be the unique solution of
\[
 r\int_0^\infty e^{-(r-\theta_j)u}q_0(u)^j\,du=1.
\]
Define
\[
 c_j=\left[r^2\int_0^\infty u e^{-(r-\theta_j)u}q_0(u)^j\,du\right]^{-1}.
\]
Then \(c_1,c_2>0\), \(\theta_1<\theta_2<\min\{r,2\theta_1\}\), and
\[
 \Pr(T^{\mathrm G}_{(2)}>t)\sim3c_2e^{-\theta_2t},\qquad
 \Pr(T^{\mathrm I}_{(2)}>t)\sim3c_1^2e^{-2\theta_1t}.
\]
In particular,
\[
 \frac{\Pr(T^{\mathrm G}_{(2)}>t)}{\Pr(T^{\mathrm I}_{(2)}>t)}
 \sim \frac{c_2}{c_1^2}e^{(2\theta_1-\theta_2)t}\longrightarrow\infty.
\]
At the two extreme ranks, there is instead a **strict all-time comparison**:
\[
 \Pr(T^{\mathrm G}_{(1)}>t)>\Pr(T^{\mathrm I}_{(1)}>t),\qquad
 \Pr(T^{\mathrm G}_{(3)}\le t)>\Pr(T^{\mathrm I}_{(3)}\le t),\quad t>0.
\]
Thus a shared reset clock delays the earliest arrival and accelerates the final arrival, yet the second arrival is accelerated at short horizons and delayed in the late tail. The theorem concerns distributions, **not** a comparison of their medians (the \(50\%\) quantiles).

## Assumptions and scope

The three Brownian noises are mutually independent; in (G) only the reset clock is common. The first-hitting time of each label is the first visit to zero, even when other labels have already hit. The external reset clock continues regardless of earlier hits. In (I), each label has its own independent, rate-\(r\) clock; in (G), the one common clock is also rate \(r\), so each individual has the same marginal first-hit law in both protocols. Instantaneous perfect reset and a perfectly absorbing **recorded target event** are assumed. No interactions or physical exclusion occur. \(D,d,r\) remain fixed when \(t\to\infty\). The theorem makes no statement about correlated Brownian noises, geometric/reset travel overhead, or target-triggered reset clocks.

## Proof

**1. Conditional binomial law.** For an observation horizon \(t\), expose the common Poisson reset times, whose successive gap lengths partition \([0,t]\) into \(\ell_1,\ldots,\ell_m\). For one particle, the conditional no-hit probability is
\[
 U_t=\prod_{i=1}^m q_0(\ell_i),\quad 0<U_t<1.
\]
For fixed reset times, Brownian paths of different particles are independent, so in (G) the count of labels that have reached the target is conditionally \(\operatorname{Binomial}(3,1-U_t)\). Its unconditional one-label hit probability is \(p_t=1-\mathbb E U_t\). In (I) the hit indicators are independent \(\operatorname{Bernoulli}(p_t)\) because each label sees an independent clock and Brownian path. This also verifies equality of the one-label marginal distributions.

Writing \(h(p)=3p^2-2p^3\), the middle-arrival CDFs are
\[
 F_{\mathrm G}(t)=\mathbb E h(1-U_t),\qquad F_{\mathrm I}(t)=h(1-\mathbb E U_t).
\]
The same conditional structure and strict Jensen inequality applied to \(u^3\) and \((1-u)^3\) give the extreme-rank inequalities, provided \(U_t\) is nonconstant. This is true at every \(t>0\): no reset occurs with positive probability; with positive probability a single reset falls near an \(s>0\) for which \(q_0(s)q_0(t-s)\ne q_0(t)\). Indeed, as \(s\downarrow0\), \(q_0(s)=1-o(s)\), whereas \(q_0(t-s)=q_0(t)-s q_0'(t)+o(s)\), and \(q_0'(t)<0\).

**2. Exact short-time comparison.** The no-reset first-hit CDF is
\[
 f_0(t)=1-q_0(t)=\operatorname{erfc}\!\left(\frac d{\sqrt{4Dt}}\right).
\]
Direct differentiation shows \(f_0''(t)>0\) for \(0<t<d^2/(6D)\), since its derivative has logarithmic derivative \(d^2/(4Dt^2)-3/(2t)\). A convex function with \(f_0(0)=0\) is superadditive on intervals within this range. Therefore, for any reset-time partition,
\[
 0\le1-U_t\le\sum_i f_0(\ell_i)\le f_0(t)
 <\operatorname{erfc}(\sqrt{3/2})<\tfrac12.
\]
Since \(h''(p)=6-12p>0\) on \([0,1/2)\) and \(1-U_t\) is nondegenerate, strict Jensen gives \(F_{\mathrm G}(t)>F_{\mathrm I}(t)\) for the claimed range.

**3. Two tilted renewal poles.** Let \(S_j(t)=\mathbb E U_t^j\), the probability that \(j\) specified particles under (G) have all avoided the target by time \(t\). Conditioning on the first reset gives the exact renewal identity
\[
 S_j(t)=e^{-rt}q_0(t)^j+r\int_0^t e^{-ru}q_0(u)^jS_j(t-u)\,du.
\]
With \(K_j(z)=\int_0^\infty e^{-zu}q_0(u)^j\,du\), this yields
\[
 \widetilde S_j(s)=\frac{K_j(s+r)}{1-rK_j(s+r)}.
\]
For \(j=1,2\), \(rK_j(r)<1\), while \(K_j(z)\uparrow\infty\) as \(z\downarrow0\), because \(q_0(u)\sim d/(\sqrt{\pi D u})\). Strict monotonicity gives the unique \(\theta_j\in(0,r)\). Also \(q_0(u)^2<q_0(u)\) for \(u>0\), hence \(\theta_2>\theta_1\).

Tilting the renewal identity by \(e^{\theta_j t}\) makes its convolution kernel a nonlattice probability density \(r e^{-(r-\theta_j)u}q_0(u)^j\) of finite positive mean. Its forcing term is directly Riemann integrable. The key renewal theorem, with the normalizations displayed above, gives
\[
 S_j(t)\sim c_j e^{-\theta_jt},\qquad j=1,2.
\]
There is a *strict* gap between the doubled one-label exponent and the two-label exponent. If \(2\theta_1\ge r\), then \(\theta_2<r\le2\theta_1\). Otherwise, for an independent \(E\sim\operatorname{Exp}(r)\), put \(Z=e^{\theta_1 E}q_0(E)\). The first-pole equation says \(\mathbb EZ=1\), while strict Cauchy–Schwarz says \(\mathbb EZ^2>1\). As \(\theta\mapsto rK_2(r-\theta)\) is strictly increasing, its unit-crossing point obeys \(\theta_2<2\theta_1\). This argument is genuinely strict because \(Z\) is not almost surely constant.

**4. Third-label remainder.** At \(\theta_2\),
\[
 rK_3(r-\theta_2)<rK_2(r-\theta_2)=1.
\]
By continuity choose \(\varepsilon>0\) with \(\theta_2+\varepsilon<r\) and \(rK_3(r-\theta_2-\varepsilon)<1\). The renewal transform implies
\[
 \int_0^\infty e^{(\theta_2+\varepsilon)t} S_3(t)\,dt<\infty.
\]
Since \(S_3\) is nonincreasing, integration over \([t-1,t]\) shows \(S_3(t)=O(e^{-(\theta_2+\varepsilon)t})\), in particular \(S_3(t)=o(S_2(t))\).

**5. Middle-rank tail and crossing.** Conditional binomial counting gives
\[
 \Pr(T^{\mathrm G}_{(2)}>t)=3S_2(t)-2S_3(t),
\]
whereas under independent clocks,
\[
 \Pr(T^{\mathrm I}_{(2)}>t)=3S_1(t)^2-2S_1(t)^3.
\]
Substituting steps 3–4 gives the stated sharp asymptotics and diverging ratio. The distributions are continuous, so the strict early and late inequalities force at least one CDF crossing. No uniqueness of the crossing is asserted. \(\square\)

## Verification

The accompanying standalone `verify.py` checks the one-body Laplace transform independently against the exact formula \(K_1(z)=[1-e^{-d\sqrt{z/D}}]/z\), finite binomial identities, Jensen-sign examples, strictly separated renewal poles for several distance values, the convex early bound, and discretized Volterra renewal solutions. Run in this directory with `OPENBLAS_NUM_THREADS=1 python verify.py` after installing `requirements.txt`. It prints 154 passed numerical/finite-algebra tests; at \(D=d=r=1\), it finds \(\theta_1\simeq0.489409173023\), \(\theta_2\simeq0.874957794252\), and \(2\theta_1-\theta_2\simeq0.103860551795\). The Volterra discretization shows an early negative and late positive difference of survival probabilities, with signs consistent with the proved inequalities. These finite calculations do not certify infinite-time asymptotics; the proof above supplies those steps.

## Relationship to prior work

Vatash, Goldfarb, Rudyak, and Roichman (arXiv:2609.23542, originally public 2026-09-20) derive ordered-arrival baselines for independently reset searchers and compare protocols, including numerical global resetting. The evaluated theorem addresses a different question: a rigorous **sign reversal in calendar-time probability** for the first interior arrival rank, including a strict early window, explicit spectral long-tail constants, and separation of joint-survival exponents. The primary result sections available for examination did not state this reversal; coverage in inaccessible portions remains a priority risk. Biroli, Majumdar, and Schehr (arXiv:2303.18012) analyze the *first* arrival for two protocols, not this three-label middle arrival. Belan (arXiv:1906.05619) investigates the median (quantile) of a *single* restarted completion time, which differs from the second ordered arrival of three searchers. Conditional Bernoulli mixtures, Jensen, and scalar renewal theory are standard methods and are not themselves claimed as discoveries. The claim is the application-specific **early-to-late inversion and sharp pole separation**.

## Limitations

Only three initially identical independent Brownian searchers in one spatial dimension, independent exponentially distributed reset intervals, complete zero-travel-time resetting and an absorbing first-hit record are covered. The early bound \(d^2/(6D)\) is a sufficient explicit interval, not a sharp crossing time. The proof gives at least one crossing, not uniqueness or its exact location. No comparison of the *mean* middle-arrival times is established, and there is no non-Poisson, interacting, finite-return or heterogeneous-distance extension here. No independent scientific audit or literature-wide priority certification has occurred.

## References

1. R. Vatash, E. Goldfarb, V. Yu. Rudyak, and Y. Roichman, *Rank-dependent optimal resetting in multiparticle search*, arXiv:2609.23542 (first submitted 2026-09-20), https://arxiv.org/abs/2609.23542.
2. M. Biroli, S. N. Majumdar, and G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012 (2023), https://arxiv.org/abs/2303.18012.
3. S. Belan, *Median and mode in first passage under restart*, arXiv:1906.05619; Physical Review Research **2**, 013243 (2020), https://arxiv.org/abs/1906.05619.
4. The nonarithmetic key renewal theorem and elementary convexity/Jensen inequalities (standard analytic tools; no originality is claimed for them).
