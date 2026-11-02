# A sparse-reset first-order transition in optimal Brownian survival decay

## Finding

For one-dimensional Brownian search with two possible stochastic reset locations, an order-\(L^{-2}\) probability of resetting near the target creates a sharp competition between a slow reset rate that explores from far away and a fast reset rate that exploits the rare near-target resets. The objective is the infinite-time exponential *survival decay rate* rather than the mean first-passage time.

Let \(u_*\in(1,2)\) be the unique nonzero solution of
\[
u_*=2(1-e^{-u_*}),\qquad C=\frac{u_*^2}{e^{u_*}-1},\qquad A=2u_*,\qquad c_* =\frac{e^2 C}{4}.
\]
Numerically, \(u_*=1.593624260040\ldots\), \(C=0.647610237891\ldots\), \(A=3.187248520080\ldots\), and \(c_*=1.196307094506\ldots\).

For every fixed \(c>0\) distinct from \(c_*\), every global optimizer \(r^*_L\) of the exponential survival decay rate obeys
\[
\begin{array}{c|c|c}
 & \lim_{L\to\infty}L^2r^*_L/D & \lim_{L\to\infty}L^2\max_{r>0}\lambda_L(r)/D\\
 c<c_* & A & C\\
 c>c_* & \text{not finite; }\lim_{L\to\infty}r^*_L/D=4 & 4c/e^2
\end{array}.
\]
There is a fixed neighborhood of \(c_*\) in which, for all sufficiently large \(L\), exactly one \(c_L\) gives two separated **global** maximizers. At this coexistence weight,
\[
 c_L=c_*+\frac{K}{L^2}+O(L^{-3}),\qquad
 K=\frac{e^2}{4}c_*A-\frac{c_*^2}{e^2}=6.8497995733\ldots>0.
\]
On one side the unique globally winning branch has \(r\sim DA/L^2\); on the other it has \(r\sim4D\). Here uniqueness means uniqueness of the *coexistence weight in the stated neighborhood*, not a classification of every possible finite-distance transition outside it.

## Assumptions and scope

Fix \(D>0\). A particle begins at any \(x>0\), moves with generator \(D\partial_{xx}\) on \((0,\infty)\), and is absorbed upon hitting \(0\). At independent Poisson times with total rate \(r>0\), it instantaneously jumps to \(1\) with probability \(p_L=c/L^2\) or to \(L\) with probability \(1-p_L\). These choices are independent of the past. For each \(c>0\), take \(L>\max\{1,\sqrt c\}\). Define
\[
 S_{x,L,r}(t)=\Pr_x(T>t),\qquad
 \lambda_L(r)=-\lim_{t\to\infty}\frac1t\log S_{x,L,r}(t).
\]
The proof below establishes existence and strict positivity of this limit, independently of \(x\). The order of limits matters: first \(t\to\infty\) for each fixed \(L,r\); then optimize over \(r\), then send \(L\to\infty\). No finite-time optimization is claimed.

## Proof

**1. Renewal pole and genuine exponential tail.** The unreset Brownian survival function is \(S_x^0(t)=\operatorname{erf}(x/\sqrt{4Dt})\). For \(\Re s>-r\), define
\[
 H_x(s)=\int_0^\infty e^{-(r+s)t}S_x^0(t)\,dt
 =\frac{1-e^{-x\sqrt{(r+s)/D}}}{r+s},
\]
and \(H_\nu(s)=p_LH_1(s)+(1-p_L)H_L(s)\). Conditioning on the first reset gives the exact transform
\[
\widehat S_x(s)=\frac{H_x(s)}{1-rH_\nu(s)}.
\]
The function \(rH_\nu(-\lambda)\) strictly increases from \(rH_\nu(0)<1\) to infinity as \(\lambda\uparrow r\) (the no-reset Brownian first-passage mean is infinite). Therefore exactly one \(\lambda\in(0,r)\) solves \(rH_\nu(-\lambda)=1\), and the pole is simple. For rigor beyond merely locating a Laplace pole, set \(g_x(t)=e^{-rt}S_x^0(t)\) and \(k(t)=r g_\nu(t)\). The tilted renewal kernel \(e^{\lambda t}k(t)\) is a nonarithmetic probability density with finite strictly positive mean \(\mu=-rH_\nu'(-\lambda)\), because \(\lambda<r\). The tilted forcing \(e^{\lambda t}g_x(t)\) is directly Riemann integrable. The key renewal theorem applied to \(S_x=g_x+r g_x*S_\nu\) yields
\[
 S_x(t)\sim C_x e^{-\lambda t},\qquad
 C_x=\frac{H_x(-\lambda)}{-r H_\nu'(-\lambda)}>0.
\]
Thus \(\lambda\) is the actual exponential survival rate, for each initial site \(x>0\).

**2. Exact parametrization of the objective.** Put \(\theta=\sqrt{(r-\lambda)/D}\) and
\[
 q_L(\theta)=p_L e^{-\theta}+(1-p_L)e^{-L\theta}.
\]
The pole equation becomes \(\lambda=rq_L(\theta)\) and \(r-\lambda=D\theta^2\); equivalently
\[
 r(\theta)=\frac{D\theta^2}{1-q_L(\theta)},\qquad
 \lambda(\theta)=\frac{D\theta^2q_L(\theta)}{1-q_L(\theta)}.
\]
The derivative \(r'(\theta)\) has the sign of \(2(1-q_L)+\theta q_L'\), which is a positive weighted mean of \(2(1-e^{-z})-ze^{-z}>0\) for \(z>0\). Hence \(r(\theta)\) increases bijectively from \(0\) to infinity and optimization over \(r\) equals optimization over \(\theta\). The positive objective \(\lambda(\theta)\) vanishes at both endpoints \(\theta\downarrow0\), \(\theta\uparrow\infty\), so it attains a global maximum.

**3. Two asymptotically separated competition charts.** Write \(F_L(\theta;c)=L^2\lambda(\theta)/D\). In the far-reset chart \(\theta=u/L\), uniformly with two derivatives on each fixed compact \(u\)-interval inside \((0,\infty)\),
\[
 F_L(u/L;c)=f(u)+\frac{c u^2}{L^2(1-e^{-u})}+O(L^{-3}),
 \qquad f(u)=\frac{u^2}{e^u-1}.
\]
The derivative of \(f\) has the sign of \(2(1-e^{-u})-u\), which has exactly one positive zero \(u_*\), and \(f''(u_*)<0\). Thus the far branch has a unique local maximizer near \(u_*\), with peak height and reset rate
\[
 M_{\rm far}(c,L)=C+\frac{cA}{L^2}+O(L^{-3}),\qquad
 r_{\rm far}=\frac{DA}{L^2}+o(L^{-2}).
\]
In the near-reset chart \(\theta=v\), uniformly with two derivatives on each fixed compact \(v\)-interval inside \((0,\infty)\),
\[
 F_L(v;c)=c v^2e^{-v}+\frac{c^2v^2e^{-2v}}{L^2}+O(L^{-4})+O(L^4e^{-Lv}).
\]
The limiting function has a unique nondegenerate maximum at \(v=2\). Consequently
\[
 M_{\rm near}(c,L)=\frac{4c}{e^2}+\frac{4c^2}{e^4L^2}+O(L^{-4})+O(L^4e^{-L}),\qquad
 r_{\rm near}=4D+o(1).
\]
All estimates here are locally uniform in \(c\) in any fixed compact subset of \((0,\infty)\).

**4. No hidden third global branch.** The basic estimate
\[
 F_L(\theta;c)\le
 \frac{(L\theta)^2e^{-L\theta}}{(1-p_L)(1-e^{-L\theta})}
 +\frac{c\theta^2 e^{-\theta}}{(1-p_L)(1-e^{-L\theta})}
\]
follows by lower-bounding \(1-q_L\). For any sequence of parameters with \(L\to\infty\), if \(\theta\to0\), \(L\theta\to u\in(0,\infty)\), the objective tends to \(f(u)\). If \(\theta\to v\in(0,\infty)\), it tends to \(cv^2 e^{-v}\). If \(L\theta\to0\), or \(\theta\to0\) with \(L\theta\to\infty\), or \(\theta\to\infty\), the displayed bound tends to zero. Since both candidate peak limits are positive and each has a unique strict maximizer, every global optimizer lies, for large \(L\), in one of the two above neighborhoods. Their nondegenerate curvatures and the uniform two-derivative expansions guarantee one local maximum in each neighborhood; neither a third scale nor a second optimum on a branch can compete.

**5. Global phase selection and coexistence shift.** Comparing the heights shows that, for each fixed \(c<c_*\), only the far branch wins when \(L\) is large, while for fixed \(c>c_*\), only the near branch wins. For a fixed sufficiently small neighborhood of \(c_*\), the optimized height difference \(M_{\rm far}-M_{\rm near}\) is continuous in \(c\), positive at its left endpoint, negative at its right endpoint, and has derivative \(-4/e^2+O(L^{-2})<0\). The derivative assertion follows from the envelope theorem and \(\partial_cF_L(\theta;c)=\theta^2(e^{-\theta}-e^{-L\theta})/(1-q_L)^2\): its far-chart value is \(O(L^{-2})\), while the near-chart value tends to \(4/e^2\). There is therefore exactly one coexistence weight \(c_L\) in this neighborhood, with two distinct global maximizers. Substituting \(c_L=c_*+K/L^2+O(L^{-3})\) into the two peak expansions and solving their equality yields
\[
 K=\frac{e^2}{4}c_* A-\frac{c_*^2}{e^2}>0.
\]
The stated scale limits, objective limits, and jump of the optimal reset rate follow.

## Verification

The standalone Python 3 program `verify_tail_crossover.py` uses only the standard library. Execute `python3 verify_tail_crossover.py` from the extracted package. It cross-checks the pole equation and monotonic parameter mapping, far/near branch heights, the two-scale global objective on broad grids, the coexistence roots, and the first correction constant. In its delivered version, it reports 30,524 passing finite diagnostic assertions. The analytic estimates and renewal theorem above, rather than finite grids, justify all infinite-limit and uniqueness statements.

## Relationship to prior work

Julián-Salgado, Dagdug and Boyer derive the two-reset-site renewal survival transform (their equation (3)) and analyze discontinuities in the **mean-first-passage-time minimizing rate**, with other parameter controls. The renewal formula is an input here, not a new contribution. Méndez, Flaquer-Galmés and Campos further analyze random reset positions, equivalent resetting points, mean first-passage times and fluctuations. The present theorem instead maximizes the dominant **survival exponential rate** and isolates a sparse, distance-dependent reset probability with exact global phase boundary, two optimizer scales, and a finite-distance coexistence correction. The original survival-transform identity does not on its own state or establish that global optimizing phase diagram. Related general restart and renewal results justify the framework but are not claimed to be new.

## Limitations

The conclusions concern absorbing half-line Brownian motion, memoryless reset clocks, two positive reset points, the particular rare-near-site scaling \(p_L=c/L^2\), and the order of limits specified above. The exponentially decaying prefactor may depend on the initial site, although the rate does not. The finite-\(L\) coexistence weight is proved unique only in a fixed neighborhood of the asymptotic critical weight; no global classification of all finite-\(L\) secondary local extrema is asserted. Neither the mean-first-passage-time optimum nor finite-horizon survival optimization is derived. The calculation does not establish experimentally measurable switching under finite observation windows.

## References

- P. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (first publicly posted 2023-11-20), https://arxiv.org/abs/2311.11897. Relevant exact renewal transform: equation (3); mean-time optimization: sections III–V.
- V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125 (2024-01-02), https://arxiv.org/abs/2401.01125. Relevant random-reset and two-point MFPT sections.
- M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic resetting and applications*, arXiv:1910.07993, https://arxiv.org/abs/1910.07993. General resetting and renewal background.
