# A logarithmic two-boundary crossover for Brownian exit races and collective resetting

## Finding

Fix \(d,D>0\) and \(\theta\in\mathbb R\). For every sufficiently large integer \(N\), consider \(N\) independent Brownian motions of diffusion coefficient \(D\), each started at \(d\) in \((0,L_N)\), where
\[
L_N=d\left(2+\frac{\theta}{\log N}\right),\qquad b=\frac{d^2}{4D},\qquad c_N=\log N-\frac12\log\log N-\frac12\log\pi.
\]
Let \(T_N\) be the earliest time at which any walker reaches either boundary, and let \(J_N\in\{0,1\}\) indicate whether its exit was through the left target (\(0\)) or the right reset threshold (\(1\)). Write \(C_\theta=1+e^{-2\theta}\) and \(p_\theta=C_\theta^{-1}\).

**Theorem (joint exit-time/endpoint and restarted completion laws).** As \(N\to\infty\):

1. The pair \((b/T_N-c_N,J_N)\) converges jointly in distribution to an independent pair \((Y,J)\), where
\[
\Pr(Y\le y)=\exp\bigl[-C_\theta e^{-y}\bigr],\quad
\Pr(J=0)=p_\theta=\frac{1}{1+e^{-2\theta}},\quad
\Pr(J=1)=1-p_\theta.
\]
The unnormalized limiting joint densities with respect to \(y\) are respectively \(e^{-y}\exp[-C_\theta e^{-y}]\) and \(e^{-2\theta}e^{-y}\exp[-C_\theta e^{-y}]\).
2. If each right exit instantaneously returns all walkers to \(d\), with independent fresh increments, and the experiment stops on the first left exit, the number \(K_N\) of search episodes is exactly geometric with parameter \(\Pr(J_N=0)\). The total search time \(S_N\) obeys
\[
\frac{\log N}{b}S_N\ \xrightarrow{\mathcal D}\ K_\theta,
\qquad \Pr(K_\theta=k)=p_\theta(1-p_\theta)^{k-1},\quad k=1,2,\ldots.
\]
3. The convergence of normalized single-episode durations holds in every fixed positive integer moment. In particular,
\[
\lim_{N\to\infty}\frac{\log N}{b}\,\mathbb E[S_N]=C_\theta=1+e^{-2\theta}.
\]

The finite-size location of the nontrivial competition window is \(L_N-2d=\theta d/\log N\). At fixed \(\theta\), a continuous one-episode exit-time fluctuation has a Gumbel limit, but the rescaled *total restarted* completion time has a discrete geometric limit.

## Assumptions and scope

All logarithms are natural. Brownian motion with diffusion coefficient \(D\) means generator \(D\partial_{xx}\) and variance \(2Dt\). The two endpoints are absorbing *within an episode*. Between episodes resetting is instantaneous, with no refractory time, and the new Brownian motions are independent of preceding ones. All walkers have the same deterministic initial position \(d\). The double limit keeps \(d,D,\theta\) fixed while \(N\) varies; \(L_N>d\) holds for all sufficiently large \(N\). There are no simultaneous boundary hits almost surely. No claim is made for interacting walkers, correlated resetting noise, finite-time reset delays, or distances outside this specified window.

## Proof

**Step 1: exact first-exit representations.** For a single walker, let \(F_{0,N}(t)\) and \(F_{1,N}(t)\) be the probabilities of exit through the left and right boundary, respectively, by time \(t\), *as the first exit*. Their time derivatives \(j_{0,N}\), \(j_{1,N}\) are positive flux densities. Define
\[
f_a(t)=\frac{a}{\sqrt{4\pi D t^3}}\exp\left(-\frac{a^2}{4Dt}\right),\qquad a>0.
\]
The Dirichlet heat-kernel reflection expansion, or equivalently the power-series expansion of the Laplace transforms \(\sinh((L_N-d)\sqrt{s/D})/\sinh(L_N\sqrt{s/D})\) and \(\sinh(d\sqrt{s/D})/\sinh(L_N\sqrt{s/D})\), gives for every \(t>0\)
\[
 j_{0,N}(t)=\sum_{k=0}^{\infty}\bigl[f_{d+2kL_N}(t)-f_{2L_N-d+2kL_N}(t)\bigr],
\]
\[
 j_{1,N}(t)=\sum_{k=0}^{\infty}\bigl[f_{L_N-d+2kL_N}(t)-f_{L_N+d+2kL_N}(t)\bigr].
\]
These series and their integrated versions converge absolutely for each \(t>0\), and the integrated leading terms are \(\operatorname{erfc}(d/\sqrt{4Dt})\) and \(\operatorname{erfc}((L_N-d)/\sqrt{4Dt})\).

**Step 2: the two rare-exit intensities.** Set \(t_N(y)=b/(c_N+y)\) for any fixed real \(y\) and all sufficiently large \(N\). Since \(L_N/d\to2\), the distances of all reflection images other than the leading one are bounded strictly above \(d\). Their exponential factors are therefore negligible compared with the leading terms at \(t_N(y)\), uniformly for \(y\) in compact intervals. Thus
\[
F_{0,N}(t_N(y))=\operatorname{erfc}(\sqrt{c_N+y})\,[1+o(1)],
\]
\[
F_{1,N}(t_N(y))=\operatorname{erfc}\!\left[\left(1+\frac\theta{\log N}\right)\sqrt{c_N+y}\right][1+o(1)].
\]
Using \(\operatorname{erfc}(\sqrt z)=e^{-z}/\sqrt{\pi z}\,[1+O(z^{-1})]\) and the specified centering, one obtains
\[
NF_{0,N}(t_N(y))\longrightarrow e^{-y},\qquad
NF_{1,N}(t_N(y))\longrightarrow e^{-2\theta}e^{-y},
\]
because \(\bigl[(1+\theta/\log N)^2-1\bigr](c_N+y)\to2\theta\). The convergence is locally uniform in \(y\).

**Step 3: time and mark limit.** Independence of the \(N\) walkers yields
\[
\Pr(T_N>t)=\bigl[1-F_{0,N}(t)-F_{1,N}(t)\bigr]^N.
\]
The event \(b/T_N-c_N\le y\) is equivalent to \(T_N\ge t_N(y)\); Step 2 therefore proves the Gumbel distribution function in the theorem. More precisely, the joint density in the decreasing variable \(y=b/t-c_N\) for the left-exit mark is
\[
N j_{0,N}(t_N(y))\,\bigl[1-F_{0,N}(t_N(y))-F_{1,N}(t_N(y))\bigr]^{N-1}\left|\frac{dt_N}{dy}\right|.
\]
The leading image term and \(|dt_N/dy|=b/(c_N+y)^2\) imply that the first and last factors have product tending to \(e^{-y}\). For the right endpoint the same product tends to \(e^{-2\theta}e^{-y}\). Consequently the two joint densities converge locally uniformly to the displayed limits. Their total integrals are \(p_\theta\) and \(1-p_\theta\), respectively, and sum to one. Convergence on compact sets together with the already established tightness of \(b/T_N-c_N\) thus proves weak joint convergence without loss of endpoint mass; the factorization establishes independence of the limiting time and mark.

**Step 4: renewal and the geometric law.** Let \(p_N=\Pr(J_N=0)\), so Step 3 gives \(p_N\to p_\theta\in(0,1)\). Independent renewal after each unsuccessful episode makes \(K_N\) exactly geometric with parameter \(p_N\). Moreover, the first part of the theorem implies \((\log N/b)T_N\to1\) in probability: \(b/T_N=c_N+O_{\Pr}(1)\) and \(c_N/\log N\to1\). For any fixed number of episodes their normalized durations converge jointly in probability to one each. Since \(\sup_{N\ge N_0}\Pr(K_N>k)\le(1-p_\theta/2)^k\), truncation at a large fixed \(k\) gives
\[
\frac{\log N}{b}S_N- K_N\longrightarrow0\qquad\text{in probability}.
\]
Combining this with \(K_N\Rightarrow K_\theta\) proves the full completion-time law. This step does not assume that a finite-\(N\) episode's duration is independent of its endpoint: the joint limit and tight geometric episode count suffice.

**Step 5: moment control and the mean.** Fix any \(A>1\), and put \(t_A=Ab/\log N\). By the leading short-time left-exit probability, \(N F_{0,N}(t_A)\ge N^{1-1/A+o(1)}\). Hence
\[
\Pr(T_N>t_A)\le\exp[-N^{1-1/A+o(1)}].
\]
For each fixed \(t_*>0\), \(L_N\) remains in a fixed compact positive length range, so a single interval-exit time has uniformly positive probability of being at most \(t_*\). Applying the Markov property on consecutive intervals of length \(t_*\) gives a uniform exponential tail after \(t_*\); for \(N\) independent walkers this bound is raised to the \(N\)-th power. Split the standard tail integral \(r\int_0^\infty t^{r-1}\Pr(T_N>t)\,dt\) at \(t_A\) and \(t_*\). For every fixed \(r\ge1\), the two remaining integrals are \(o((\log N)^{-r})\), while \(\Pr(T_N<(1-\varepsilon)b/\log N)\to0\) for each \(0<\varepsilon<1\), by Step 2 with the same short-time estimate. Letting \(A\downarrow1\) proves
\[
\mathbb E\left[\left(\frac{\log N}{b}T_N\right)^r\right]\longrightarrow1.
\]
The renewal identity \(\mathbb E S_N=\mathbb E T_N/p_N\), obtained by conditioning on the first episode and using the fresh continuation after a right exit, then gives the asserted mean scaling.

## Verification

The standalone standard-library program `verify.py` computes truncated image-series exit probabilities and first-exit fluxes, integrates the finite-population left-win density, and evaluates finite-population centered exit-time distribution functions. Run `python verify.py` from this directory. It first checks three numerical Laplace-transform identities for the image expansion, then tests \(\theta=-1,0,1\) and \(N=10^3,10^4,10^5,10^6\), checks the symmetry identity \(p_N=1/2\) when \(\theta=0\), validates probability bounds, and prints comparisons with the analytic limiting distributions. These finite calculations are corroborating checks only: the convergence and renewal results follow from Steps 1–5, not from numerical extrapolation.

## Relationship to prior work

Biswas, Majumdar and Pal (2026, arXiv:2603.25338) specify the same many-searcher threshold-reset protocol and derive an exact finite-\(N\) renewal formula, including \(\mathbb E S_N=\mathbb E T_N/p_N\). Their large-population analysis treats fixed threshold ratios and endpoint regimes; their examined results do not state the \(1/\log N\) *moving-threshold* crossover, the limiting independent Gumbel exit mark, or the normalized geometric completion-time distribution. Their 2025 precursor (arXiv:2504.13501) provides a general renewal framework but not this asymptotic classification. Linn and Lawley (arXiv:2110.11277) obtain extreme hitting probabilities for separated target sets with a fixed distance ratio; those fixed-ratio results do not directly give a two-endpoint ratio tending to one at the rate \(1/\log N\). Krapivsky, Majumdar and Rosso (arXiv:1004.5042) derive exact exit probabilities in the many-walker box and extreme-distance statistics, but the inspected formulation does not give the joint rare-time/exit-mark crossover or the restarted completion law. The short-time Brownian reflection principle, the renewal decomposition, and basic Gumbel asymptotics are standard background; novelty is claimed only for their complete sharp joint critical-window classification in this model.

## Limitations

The theorem concerns one-dimensional independent Brownian motions with instantaneous full resets and a threshold tuned within the stated critical window. It does not establish optimal threshold placement or a new formula for arbitrary finite-\(N\) exit probability. The finite-\(N\) convergence can be slow, especially away from \(\theta=0\); asymptotic constants should not be construed as precise small-system predictions. Although direct comparisons identified no explicitly covering result in the examined sources, implicit derivability from broader extreme-exit or renewal theory remains a literature risk. No independent scientific audit has been performed.

## References

1. A. Biswas, S. N. Majumdar and A. Pal, *Optimal threshold resetting in collective diffusive search*, first publicly submitted 2026-03-26, https://arxiv.org/abs/2603.25338.
2. A. Biswas, S. N. Majumdar and A. Pal, *Target search optimization by threshold resetting*, first publicly submitted 2025-04-18, https://arxiv.org/abs/2504.13501.
3. S. Linn and S. D. Lawley, *Extreme hitting probabilities for diffusion*, first publicly submitted 2021-10-21, https://arxiv.org/abs/2110.11277.
4. P. L. Krapivsky, S. N. Majumdar and A. Rosso, *Maximum of N Independent Brownian Walkers till the First Exit From the Half Space*, first publicly submitted 2010-04-28, https://arxiv.org/abs/1004.5042.
