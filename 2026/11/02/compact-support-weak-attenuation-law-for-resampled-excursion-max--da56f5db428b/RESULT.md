# Compact-support weak-attenuation law for resampled-excursion maxima

## Finding
For the excursion-height model of Yoshida [1], take spatial attenuation \(r=e^{-\varepsilon}\) and let \(\varepsilon\downarrow0\). A new uniform parameter \(P\in(0,1)\) is sampled for the excursion. The rescaled excursion maximum \(\varepsilon M_\varepsilon\), jointly with \(P\), converges in distribution to a nontrivial two-point mixture conditional on the parameter: for \(p\le1/2\) the limiting height is zero; for \(p>1/2\) it equals \(t_c(p)\) with probability \(2p-1\) and zero otherwise. The deterministic cutoff \(t_c(p)\) is defined below.

Write
\[
F(p,t)=\int_0^t\log\frac{e^u-p}{p}\,du
=\frac{t^2}{2}-t\log p+\operatorname{Li}_2(pe^{-t})-\operatorname{Li}_2(p).
\]
For \(p>1/2\), \(t_c(p)\) is the unique strictly positive root of \(F(p,t)=0\). Let \(t_*=t_c(1)\), numerically \(t_*=1.70542815480031\ldots\), and for every \(0<t<t_*\) let \(p_t\in(1/2,1)\) solve \(F(p_t,t)=0\). Then the limiting height \(Y\) satisfies
\[
\Pr(Y=0)=\frac34,\qquad
\Pr(Y\ge t)=p_t(1-p_t)\quad(0<t<t_*),\qquad
\Pr(Y\ge t)=0\quad(t\ge t_*).
\]
The positive-height distribution has a logarithmically thin upper edge:
\[
\Pr(Y\ge t)\sim
\frac{\log(e^{t_*}-1)(t_*-t)}{\log[1/(t_*-t)]}
\qquad(t\uparrow t_*).
\]
Furthermore, for fixed \(0<t<t_*\), conditional on the event \(\{M_\varepsilon\ge\lfloor t/\varepsilon\rfloor\}\), the parameter converges to a law with density
\[
\frac{(2p-1)\mathbf 1_{[p_t,1]}(p)}{p_t(1-p_t)}\quad(0<p<1).
\]

## Assumptions and scope
Consider one excursion of a nearest-neighbor chain starting at zero. At time zero sample \(P\) uniformly on \((0,1)\); it is held fixed for that excursion. From zero the first step is to one with probability \(P\), otherwise the excursion ends at zero with maximum zero. At positive state \(k\), the right-step probability is \(P e^{-\varepsilon k}\), and the left-step probability is \(1-P e^{-\varepsilon k}\). The excursion ends upon the first return to zero and \(M_\varepsilon\) is its maximum. These rules make the excursion finite almost surely for every \(\varepsilon>0\). The theorem concerns exactly this geometric spatial attenuation, uniform independent parameter sampling, a single excursion and the singular joint limit \(\varepsilon\downarrow0\). The auxiliary parameter \(p=1\) appears only to define the endpoint cutoff; it is not charged by the uniform environment law.

The conditional limiting law can be expressed by \(Y=t_c(P)I\), where, conditional on \(P=p\), \(I\) is Bernoulli with success probability \((2p-1)_+\). Define \(t_c(p)=0\) for \(p\le1/2\) for this representation. Joint convergence is convergence of probability measures on \((0,1)\times[0,\infty)\) in the usual weak topology; the event-limit statements are for the indicated fixed thresholds, not finite-size error bounds.

## Proof
**Exact scale function.** The finite-height formula in Yoshida [1, Theorem 1] yields for every integer \(N\ge2\) and \(p\in(0,1)\)
\[
H_\varepsilon(N,p):=\Pr(M_\varepsilon\ge N\mid P=p)
=\frac{p}{S_\varepsilon(N,p)},\qquad
S_\varepsilon(N,p)=\sum_{i=0}^{N-1}T_{\varepsilon,i}(p),
\]
where \(T_{\varepsilon,0}=1\) and \(T_{\varepsilon,i}(p)=\prod_{j=1}^i(1-pe^{-\varepsilon j})/(pe^{-\varepsilon j})\). This follows alternatively by solving the two-boundary gambler's-ruin recurrence and multiplying the hitting probability from one by the probability \(p\) of making the initial excursion step.

**The action and phase boundary.** For fixed \(p\in(0,1)\) and \(u\ge0\), elementary Riemann sums give
\[
\varepsilon\log T_{\varepsilon,\lfloor u/\varepsilon\rfloor}(p)
\longrightarrow F(p,u),
\]
uniformly over compact \(u\)-intervals. Indeed the summand is the continuous function \(\phi_p(v)=\log[(e^v-p)/p]\). Its derivative in \(v\) is strictly positive, so \(F(p,\cdot)\) is strictly convex; its initial derivative is \(\log[(1-p)/p]\). For \(p\le1/2\), \(F(p,t)>0\) for all \(t>0\). For \(p>1/2\), it first decreases below zero, then crosses zero once and tends to infinity. This proves existence and uniqueness of \(t_c(p)\). The same argument works at \(p=1\) for strictly positive times, since \(\log(e^u-1)\) is integrable at zero.

For any fixed \(t>0\) and \(p\in(0,1)\) with \(F(p,t)>0\), the final summand in \(S_\varepsilon(\lfloor t/\varepsilon\rfloor,p)\) diverges exponentially, and hence \(H_\varepsilon\to0\). If \(F(p,t)<0\), necessarily \(p>1/2\). Choose \(u_0>0\) sufficiently small that \(\phi_p(u)\le-a<0\) on \([0,u_0]\). The terms up to \(u_0/\varepsilon\) are bounded by \(e^{-ai}\). Uniform negativity of \(F(p,u)\) on \([u_0,t]\) makes the sum of the remaining \(O(1/\varepsilon)\) terms vanish exponentially. Dominated convergence for the early terms therefore gives
\[
S_\varepsilon(\lfloor t/\varepsilon\rfloor,p)
\longrightarrow\sum_{i=0}^\infty\left(\frac{1-p}{p}\right)^i
=\frac{p}{2p-1},
\]
so \(H_\varepsilon\to2p-1\). The value on the equation \(F(p,t)=0\) is unnecessary for the joint weak limit because for fixed \(t\) it occurs at at most one interior value of \(p\), which has zero uniform probability.

**Limit and its distribution.** For each fixed \(t>0\), the preceding calculation yields
\[
\lim_{\varepsilon\downarrow0}H_\varepsilon(\lfloor t/\varepsilon\rfloor,p)
=(2p-1)\mathbf1_{\{p>1/2,\ t<t_c(p)\}}
\]
for Lebesgue-almost every \(p\). The convergence holds with a bounded continuous weight of \(p\) under integration, by domination since \(0\le H_\varepsilon\le1\). The function \(F(p,t)\) is strictly decreasing in \(p\), as follows by differentiating its integral, and therefore \(t_c\) is strictly increasing. The root \(p_t\) increases from \(1/2\) to \(1\) as \(t\) runs from zero to \(t_*\). Integration over \(p\in[p_t,1]\) gives
\[
\int_{p_t}^1(2p-1)\,dp=p_t(1-p_t).
\]
These weighted tail probabilities at all positive continuity thresholds establish the asserted joint weak convergence (the limiting conditional tails specify a probability kernel); they also give the marked-parameter conditional density by normalization. The positive mass is \(\int_{1/2}^1(2p-1)dp=1/4\), leaving an atom \(3/4\) at zero. The monotone endpoint is \(t_*\), characterized by \(F(1,t_*)=0\).

**Logarithmic upper edge.** Put \(h=t_*-t\) and \(\delta=1-p_t\). As \(h\downarrow0\), one has \(\delta\downarrow0\), and
\[
F(1-\delta,t)-F(1,t)
=\int_0^t\log\left(1+\frac{\delta}{e^u-1}\right)du-t\log(1-\delta)
=\delta\log(1/\delta)+O(\delta),
\]
with an error uniform for \(t\) in a fixed compact neighborhood of \(t_*\). To justify the last estimate, split the integral at a fixed small positive number: near zero, \(e^u-1\sim u\), reducing its singular contribution to \(\int_0^c\log(1+\delta/u)du=\delta\log(1/\delta)+O(\delta)\); away from zero it is \(O(\delta)\). Since \(F(1,t_*)=0\) and \(\partial_tF(1,t_*)=a:=\log(e^{t_*}-1)>0\), we have \(F(1,t)=-ah+O(h^2)\). The defining identity \(F(1-\delta,t)=0\) therefore gives \(\delta\log(1/\delta)\sim ah\), whence \(\delta\sim ah/\log(1/h)\). Finally \(p_t(1-p_t)=\delta(1-\delta)\sim\delta\), proving the stated edge law.

## Verification
The accompanying `verify_weak_decay.py` checks the finite hitting-probability scale identity against independently solved rational two-boundary recurrences for several rational parameters and heights. It also numerically checks the phase roots, finite-attenuation probabilities and the asymptotic approach to the limiting tail; recorded console output is in `verification_output.txt`. The exact-rational tests have 684 successful assertions. No finite computation is treated as proof of weak convergence or of the logarithmic edge; those follow from the arguments above.

## Relationship to prior work
Yoshida [1] defines this exact excursion model and derives the finite-attenuation hitting law, maximum-depth distribution and expectations. The formula for \(H_\varepsilon\) is therefore **prior work**, not a newly claimed result. The finding here concerns the singular joint scaling \(\varepsilon\downarrow0\), the random two-point macroscopic excursion-height law, its explicit uniformly mixed cutoff profile and its nonanalytic endpoint. These statements are not explicitly contained in the inspected results of [1], which do supply the starting exact formula. Barrera, Bertoncini and Fernández [2] study escape and convergence of birth-and-death chains under different parameter scalings; their general results do not directly state the mixed-environment cutoff and logarithmic endpoint for [1]. General asymptotic scale-function methods may provide other routes to this law and are a residual historical-priority risk.

## Limitations
This is a one-excursion weak-attenuation theorem, not a limit for the maximum across many excursions or for physical-time maxima. The environment is uniform on \((0,1)\) and resampled per excursion. The limiting atom, cutoff and logarithmic edge need not hold for other parameter laws or nongeometric spatial decay. The endpoint asymptotic is nonuniform near \(t_*\) and offers no explicit finite-\(\varepsilon\) uniform error estimate. Scientific evaluation is a self-review; no independent audit has been performed.

## References
[1] Naohiro Yoshida, *Analysis of an Inhomogeneous Random Walk with Spatial Decay of Transition Probabilities and Parameter Renewal per Excursion*, arXiv:2604.22644v1, first posted 24 April 2026. https://arxiv.org/html/2604.22644v1

[2] J. Barrera, W. Bertoncini, and R. Fernández, *Abrupt Convergence and Escape Behavior for Birth and Death Chains*, arXiv:0903.1832 (2009). https://arxiv.org/abs/0903.1832
