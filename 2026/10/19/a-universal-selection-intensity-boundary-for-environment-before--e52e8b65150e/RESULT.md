# A universal selection-intensity boundary for environment-before-Fermi public-goods dynamics

## Finding
For a three-player stochastic nonlinear public-goods interaction at unit marginal multiplier (group size and enhancement multiplier both equal three), drawing the synergy/discounting environment **before** applying a nonlinear Fermi comparison leads to a selection-intensity-dependent threshold absent from the corresponding averaged-payoff update. The central conclusions are an exact global threshold for the existence of positive cooperative drift, strict monotonicity of that threshold in selection strength, and a universal inverse-strength asymptotic.

Let \(0<\delta<1\), \(s>0\), and \(p\in[0,1]\). Write \(t=\delta x\), where \(x\in(0,1)\) denotes the cooperator frequency, and put
\[
 a(t)=2t+t^2,\qquad b(t)=2t-t^2,\qquad
 H_{s,p}(t)=p\tanh\!\left(\frac{sa(t)}2\right)
 -(1-p)\tanh\!\left(\frac{sb(t)}2\right).
\]
The precisely specified population dynamics are \(\dot x=x(1-x)H_{s,p}(\delta x)\). Define
\[
 q_s(t)=\frac{\tanh(sb(t)/2)}{\tanh(sa(t)/2)+\tanh(sb(t)/2)},\qquad
 p_{\min}(s,\delta)=\min_{0<t\le\delta}q_s(t),
\]
where \(q_s(0)=1/2\) by continuous extension.

**Theorem.** For every fixed \(0<\delta<1\), \(s\mapsto p_{\min}(s,\delta)\) is continuous and strictly increasing, with
\[
 \lim_{s\downarrow0}p_{\min}(s,\delta)=\frac12-\frac\delta4,
 \qquad
 p_{\min}(s,\delta)=\frac12-\frac{C}{s}+o(s^{-1})\quad(s\to\infty).
\]
The constant is independent of \(\delta\):
\[
 C=\max_{z>0}\frac{z^2}{2\sinh(2z)}
 =\frac{z_*^2}{2\sinh(2z_*)}
 =0.13808161171941437949\ldots,
\]
where \(z_*=0.95750402407726874068\ldots\) is the unique positive solution of \(\tanh(2z)=z\). Every minimizing frequency \(t_s\) satisfies \(s t_s\to z_*\).

In particular, for each \(p\) with \(1/2-\delta/4<p<1/2\), there is a **unique finite** selection strength \(s_c(p,\delta)>0\) such that: if \(0<s<s_c\), some interior cooperator frequencies have strictly positive drift; if \(s>s_c\), every interior frequency has strictly negative drift, and every interior solution decreases to all-defection. As \(p\uparrow1/2\) with \(\delta\) fixed, \(s_c(p,\delta)\sim C/(1/2-p)\). For \(p\ge1/2\), drift is strictly positive at every interior state for every \(s>0\).

A rational-parameter local witness is \(p=2/5\), \(\delta=4/5\), \(x=5/6\), so \(t=2/3\). At this fixed state, the stochastic-before-Fermi drift is strictly positive exactly when
\[
 s<\frac94\operatorname{artanh}(1/\sqrt3)
 =1.4815776340404187972\ldots,
\]
and negative exactly when the reverse inequality holds. In contrast, Fermi comparison **after** averaging the environmental payoffs has a strictly positive payoff gap \(8/45\) at the same state for *every* \(s>0\). This is a comparison of two different, explicitly defined update protocols, not a correction of the earlier model.

## Assumptions and scope
The motivating payoff construction assigns equal probabilities for randomly drawn partner strategies conditional on the population cooperator fraction \(x\), with independent partner sampling in the infinite-population limit. For the triple game with group multiplier three, the expected conditional payoff difference of cooperating rather than defecting in a **shared synergy environment** is \(a(\delta x)\), and in a **shared discounting environment** is \(-b(\delta x)\). At each strategy-comparison event, one common environmental label is sampled (synergy with probability \(p\)); the relevant composition-averaged conditional payoff gap is used in a Fermi comparison; and only then is the environmental randomness averaged. This **environment-before-Fermi** protocol produces the above drift (with a choice of time unit). The protocol does *not* resample individual co-player compositions inside each Fermi comparison, does *not* use independent environmental labels for the two compared players, and is not a finite-population fixation model.

By contrast, the reference averaged-payoff-before-Fermi protocol has gap
\[
 \overline{\Delta}(t)=p a(t)-(1-p)b(t)
 =2t(2p-1)+t^2,
\]
and drift proportional to \(\tanh(s\overline\Delta(t)/2)\). The distinction is the order of a nonlinear map and an environmental average. All quantified bounds below concern the stated three-player, shared-environment, conditionally averaged-payoff dynamical model with \(0<\delta<1\).

## Proof
**1. Exact drift threshold.** Set \(A=\tanh(sa(t)/2)\), \(B=\tanh(sb(t)/2)\). For \(0<t\le\delta<1\), \(0<B<A<1\). Therefore
\[
 H_{s,p}(t)=p(A+B)-B,
 \qquad H_{s,p}(t)>0\iff p>q_s(t)=\frac{B}{A+B}.
\]
In particular \(0<q_s(t)<1/2\). The limits as \(t\downarrow0\) give \(q_s(0)=1/2\), so its minimum on \([0,\delta]\) is attained away from zero. This yields the exact equivalence between a positive-drift frequency and \(p>p_{\min}(s,\delta)\). If \(p<p_{\min}\), all interior drift is strictly negative. For \(p>p_{\min}\), even a minimizer at \(t=\delta\) yields an *interior* positive-drift interval by continuity and strictness.

**2. Strict selection-strength monotonicity.** For fixed \(t>0\), put \(R_s=A/B\). Direct logarithmic differentiation gives
\[
 \frac{\partial}{\partial s}\log R_s
 =\frac{a(t)}{\sinh(sa(t))}-\frac{b(t)}{\sinh(sb(t))}<0,
\]
because for any fixed \(s>0\), the function \(u\mapsto u/\sinh(su)\) strictly decreases on positive \(u\), and \(a(t)>b(t)\). Since \(q_s=1/(1+R_s)\), every positive-\(t\) threshold strictly increases with \(s\). Choosing a minimizing point at the larger of two strengths proves strict increase of the minima. Joint continuity and compactness, together with the extension at zero, give continuity of \(p_{\min}\).

**3. Weak-strength boundary.** Uniformly for \(0\le t\le\delta\), the expansion \(\tanh(y)=y+O(y^3)\), with the common vanishing factor \(t\) canceled, gives
\[
 q_s(t)=\frac{b(t)}{a(t)+b(t)}+O(s^2)
 =\frac{2-t}{4}+O(s^2).
\]
Taking the minimum on the compact interval yields \(p_{\min}(s,\delta)\to1/2-\delta/4\) as \(s\downarrow0\).

**4. Sharp strong-strength boundary.** Writing \(z=st\), direct expansion at fixed \(z>0\) gives
\[
 s\left(\frac12-q_s(z/s)\right)
 \longrightarrow g(z)=\frac{z^2}{2\sinh(2z)},
\]
uniformly on every compact \(z\)-interval bounded away from zero. Indeed, the two Fermi arguments become \(z\pm z^2/(2s)\), whose hyperbolic tangents differ by \(z^2s^{-1}\operatorname{sech}^2z+O(s^{-2})\).

To justify optimization rather than incorrectly interchanging a pointwise limit and minimum, observe that for \(0<t\le\delta<1\), \(b(t)\ge t\). The mean-value theorem and monotonicity of \(\operatorname{sech}^2\) on the positive half-line imply
\[
 \tanh(sa/2)-\tanh(sb/2)
 \le s t^2\operatorname{sech}^2(sb/2).
\]
Since the sum of these two hyperbolic tangents is at least \(2\tanh(sb/2)\), it follows that
\[
 0<s\left(\frac12-q_s(t)\right)
 \le\frac{s^2t^2}{2\sinh(sb(t))}
 \le\frac{z^2}{2\sinh z}.
\]
The right side tends to zero both as \(z\downarrow0\) and as \(z\to\infty\). Thus every maximizing sequence in the rescaled variable is confined to a fixed compact subinterval of \((0,\infty)\), so the compact-uniform limit can be maximized and gives \(s(1/2-p_{\min})\to\max g=C\).

For uniqueness, \(g'(z)=0\) is equivalent to \(\tanh(2z)=z\). The function \(h(z)=\tanh(2z)-z\) has \(h(0)=0\), \(h'(0)=1\), \(h''(z)<0\) for \(z>0\), and \(h(1)<0\). It therefore has exactly one positive root \(z_*\), giving the unique positive maximizer of \(g\). Compactness of maximizing sequences then proves \(st_s\to z_*\) for every minimizing \(t_s\).

**5. Unique critical intensity and global decline.** Strict continuous increase from \(1/2-\delta/4\) to \(1/2\) gives a unique solution \(p_{\min}(s_c,\delta)=p\) for every \(p\) in that open interval. The sign conclusions follow from Step 1. In the strictly negative regime, a trajectory with \(0<x(0)<1\) decreases and has a limit. If that limit were in \((0,1)\), continuity would keep its derivative bounded strictly below zero near the limit; this is impossible. Thus \(x(t)\downarrow0\). Inverting the strong-strength asymptotic gives \(s_c\sim C/(1/2-p)\) as \(p\uparrow1/2\).

**6. Exact rational witness.** At \(t=2/3\), \(a=16/9\) and \(b=8/9\). With \(u=\tanh(4s/9)\in(0,1)\), the double-angle identity gives
\[
 H_{s,2/5}(2/3)=\frac{u}{5}
 \left(\frac4{1+u^2}-3\right),
\]
so its sign is the sign of \(1-3u^2\). Solving \(u=1/\sqrt3\) yields the stated critical value. The averaged gap is \((2/5)(16/9)-(3/5)(8/9)=8/45>0\). This completes the proof.

## Verification
The standalone file `verify.py` uses independent symbolic and arbitrary-precision calculations. It checks the payoff identities, verifies the pointwise threshold monotonicity on a representative grid, reproduces the rational witness and its exact critical strength, computes the unique universal constant to high precision, verifies its predicted scaling at strengths \(100,1000,10000\), and checks the global tail inequality at \(995\) parameter points. The numerical sample is not a proof of an all-parameter statement: the proof above supplies that statement independently. Run `python verify.py` with Python 3 and packages `sympy` and `mpmath`.

## Relationship to prior work
Zhu et al. (2024), Eqs. (4)–(7) and the corresponding supplementary derivation, average the synergy/discounting payoffs before applying the Fermi function in their infinite-population mean-field evolution. Their framework supplies the nonlinear public-goods payoff family and motivates studying the alternative ordering; it does not provide the present exact \(s\)-dependent threshold and universal high-strength optimization law. Earlier stochastic-payoff Fermi work (Traulsen, Nowak and Pacheco, 2007) establishes the importance of noisy realized payoffs and discusses effective selection temperature in finite populations; it is highly relevant conceptually, and no claim is made that noncommutation of payoff averaging and nonlinear imitation is itself new. Zhang et al. (2026) analyze stochastic changing games on networks principally via weak-selection fixation criteria, not this three-player strong-selection mean-field bifurcation. Thus the claimed contribution is **the exact nonlinear-public-goods threshold and its universal asymptotic**, not the elementary identity between expected Fermi rates and Fermi rates of expected payoffs.

## Limitations
The conclusions are for an exactly specified shared-environment, composition-averaged three-player Fermi dynamics, not for all stochastic payoff models, independently realized group shocks, individual sampled-group payoff fluctuations, finite-population fixation, or heterogeneous contact networks. Positive drift somewhere below the critical intensity does not by itself imply universal fixation of cooperation. No assertion of an equilibrium's stability at the critical intensity is needed. Earlier stochastic-payoff literature may contain less visible equivalent specializations; independent priority assessment remains outstanding.

## References
1. W. Zhu et al., *Evolutionary dynamics in stochastic nonlinear public goods games*, arXiv:2408.02042v1 (first submitted 4 August 2024), https://arxiv.org/html/2408.02042v1 ; *Communications Physics* **7**, 377 (2024), https://doi.org/10.1038/s42005-024-01865-6.
2. A. Traulsen, M. A. Nowak and J. M. Pacheco, *Stochastic payoff evaluation increases the temperature of selection*, *Journal of Theoretical Biology* **244** (2007), 349–356, https://doi.org/10.1016/j.jtbi.2006.08.008.
3. Y. Zhang et al., *Effects of stochastic games on evolutionary dynamics in structured populations*, *Communications Physics* **9**, 101 (2026), https://doi.org/10.1038/s42005-026-02536-4.
4. C. Hauert and A. McAvoy, *Frequency-dependent returns in nonlinear public goods games*, arXiv:2404.13728 (first submitted 21 April 2024), https://arxiv.org/abs/2404.13728.
