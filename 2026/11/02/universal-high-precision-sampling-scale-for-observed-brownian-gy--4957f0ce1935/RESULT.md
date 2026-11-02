# Universal high-precision sampling scale for observed Brownian-gyrator irreversibility

## Finding
For a stationary overdamped Brownian gyrator with two unequal bath temperatures, consider the relative entropy between the two-time joint law and its time-reversed joint law, divided by the observation lag. Add independent Gaussian readout errors at both endpoints, with covariance proportional to the two bath diffusivities. For every positive readout-noise level, this pairwise irreversibility rate has at least one strictly positive maximizing lag. As the readout noise vanishes, **every** maximizing lag obeys the universal square-root law
\[
\boxed{\frac{t_h}{\sqrt{h/\kappa}}\longrightarrow1},
\]
where \(\kappa\) is the mean restoring rate and \(h\) has units of time. The leading optimal rate is
\[
\boxed{\max_{t>0}J_h(t)=\sigma\bigl[1-2\sqrt{\kappa h}+o(\sqrt h)\bigr]},
\qquad
\sigma=\frac{u^2(T_x-T_y)^2}{2\kappa T_xT_y}.
\]
The coefficients of the optimal *time scale* and relative loss are independent of both coupling strength and temperature contrast, provided these remain fixed, nonzero, and nondegenerate. These are pairwise time-reversal distinguishability statements, not claims about finite-sample estimation error or the entropy production of the complete noisy observation sequence.

## Assumptions and scope
Fix \(\kappa>0\), \(0<|u|<\kappa\), distinct temperatures \(T_x,T_y>0\), and a stationary two-dimensional diffusion
\[
 dX_t=-\begin{pmatrix}\kappa&-u\\-u&\kappa\end{pmatrix}X_t\,dt+
 \sqrt{2\operatorname{diag}(T_x,T_y)}\,dB_t.
\]
For each \(t>0\) observe \(Y_0=X_0+\xi_0\), \(Y_t=X_t+\xi_t\), where \(\xi_0,\xi_t\) are independent centered Gaussians, independent of the diffusion, each with covariance \(h\operatorname{diag}(T_x,T_y)\), for \(h\ge0\). Write \(P_{t,h}\) for the joint law of \((Y_0,Y_t)\) and \(P_{t,h}^{\leftarrow}\) for the law of \((Y_t,Y_0)\), and set
\[
 J_h(t)=t^{-1}D_{\mathrm{KL}}(P_{t,h}\Vert P_{t,h}^{\leftarrow}).
\]
In the stationary normal-mode basis set
\[
 a=\kappa-u,\quad b=\kappa+u,\quad d=(T_x+T_y)/2,\quad e=(T_x-T_y)/2,
\]
\[
 D=\begin{pmatrix}d&e\\e&d\end{pmatrix},\quad
 C=\begin{pmatrix}d/a&2e/(a+b)\\2e/(a+b)&d/b\end{pmatrix},\quad
 F(t)=\operatorname{diag}(e^{-at},e^{-bt}).
\]
Here \(C\) is the stationary covariance, \(D\) the diffusion tensor in normal coordinates, and \(a,b>0\), \(D,C\succ0\). All limits as \(h\downarrow0\) keep the model parameters fixed.

## Proof
**1. Exact two-time Gaussian divergence.** Put \(V=C+hD\), \(K=CF\) and
\[
 P=V+\tfrac12(K+K^{\mathsf T}),\qquad
 Q=V-\tfrac12(K+K^{\mathsf T}),\qquad
 H=\tfrac12(K-K^{\mathsf T}).
\]
The orthogonal transformation from \((Y_0,Y_t)\) to their normalized sum and difference gives the covariance block matrix \(\begin{psmallmatrix}P&H\\H^{\mathsf T}&Q\end{psmallmatrix}\). Swapping the endpoints changes \(H\) into \(-H\) while preserving \(P,Q\). Conditionally on the sum, the two Gaussian laws of the difference have opposite means \(\pm H^{\mathsf T}P^{-1}\) times the sum and the same covariance \(Q-H^{\mathsf T}P^{-1}H\). The conditional Gaussian KL formula therefore yields the **exact** identity
\[
 \boxed{D_{\mathrm{KL}}(P_{t,h}\Vert P_{t,h}^{\leftarrow})
 =2\operatorname{tr}\!\left[(Q-H^{\mathsf T}P^{-1}H)^{-1}
 H^{\mathsf T}P^{-1}H\right]}.\tag{1}
\]
All matrices inverted here are positive definite for \(t>0\). Since \(C_{12}=2e/(a+b)\ne0\) and \(a\ne b\), the off-diagonal matrix \(H\) is nonzero at every finite positive lag; hence (1) is strictly positive.

**2. Explicit noiseless law and its infinitesimal rate.** Write \(c_1=d/a\), \(c_2=d/b\), \(w=2e/(a+b)\), \(p=e^{-at}\), \(q=e^{-bt}\). The same Gaussian formula at \(h=0\) simplifies to
\[
 \boxed{D_{\mathrm{KL}}(P_{t,0}\Vert P_{t,0}^{\leftarrow})=
 \frac{w^2(p-q)^2(1-pq)}{c_1c_2(1-p^2)(1-q^2)-w^2(1-pq)^2}}.\tag{2}
\]
Its denominator is positive, as it is the determinant of the nondegenerate transition covariance \(C-FCF\). Taylor expansion of (2) at zero gives
\[
 J_0(t)=\sigma[1-\kappa t+O(t^2)],\qquad
 \sigma=\frac{e^2(b-a)^2}{(a+b)(d^2-e^2)}
 =\frac{u^2(T_x-T_y)^2}{2\kappa T_xT_y}>0.\tag{3}
\]
In particular \(J_0(t)\to\sigma\). Moreover \(J_0(t)<\sigma\) for every \(t>0\): the full stationary pathwise time-reversal KL on an interval of length \(t\) equals \(\sigma t\), whereas retaining only endpoints is a strict data-processing contraction. To see strictness, the path log-likelihood ratio contains a nonzero Stratonovich signed-area term because the antisymmetric part of \(D^{-1}\operatorname{diag}(a,b)\) is nonzero when \(e(a-b)\ne0\). Conditioned on two endpoints, an elliptic diffusion bridge has nondegenerate signed-area fluctuations, so the path log ratio is not endpoint-measurable; equality in data processing is impossible. Formula (2) also gives \(J_0(t)\to0\) as \(t\to\infty\).

**3. Exact small-parameter comparison.** For \(h>0\), (1) implies \(J_h(t)\to0\) as \(t\downarrow0\), because \(H=O(t)\) while \(Q\to hD\); it also tends to zero as \(t\to\infty\), because \(H\) decays exponentially. Thus a positive interior global maximum exists. Addition of independent observation noise is a Markov kernel that commutes with endpoint swapping, so data processing gives \(0<J_h(t)\le J_0(t)\).

For precise joint scaling, put \(z=h/t\) and regard (1) as a function of \((t,z)\) near \((0,0)\). With \(A=\operatorname{diag}(a,b)\), the stationary Lyapunov identity \(AC+CA=2D\) gives
\[
 P=2C+O(t+zt),\quad Q=t(1+z)D+O(t^2),\quad
 H=\tfrac t2(AC-CA)+O(t^2).
\]
After factoring \(t\) out of the conditional covariance in (1), the quotient \(J_{zt}(t)\) extends analytically to a neighborhood of \((t,z)=(0,0)\). Its value at \(t=0\) is \(\sigma/(1+z)\), since the coefficient
\[
 \tfrac14\operatorname{tr}\!\big[D^{-1}(AC-CA)^{\mathsf T}C^{-1}(AC-CA)\big]=\sigma.
\]
Its derivative along \(z=0\) follows from (3). Hence the **uniform two-variable expansion** is
\[
 \boxed{\frac{J_h(t)}{\sigma}=1-\kappa t-\frac ht+
 O\!\left((t+h/t)^2\right)}\tag{4}
\]
when \(t\downarrow0\) and \(h/t\downarrow0\). This is a Taylor statement for the exact matrix expression, not a heuristic approximation.

**4. Global maximizers and the sharp universal scale.** Taking \(t=\sqrt{h/\kappa}\) in (4) gives
\[
 \sup_{t>0}J_h(t)\ge \sigma[1-2\sqrt{\kappa h}+O(h)].\tag{5}
\]
Let \(t_h\) be any global maximizer. Strict \(J_0(t)<\sigma\), decay at infinity, and the data-processing upper bound force \(t_h\to0\). Also \(h/t_h\to0\): otherwise, from the leading \(J_h(t)/\sigma\sim t/(t+h)\) as \(t,h\to0\) (and the corresponding upper bound if \(h/t\to\infty\)), a subsequence would remain bounded away from \(\sigma\), contrary to (5). With both small, (4) and (5) force \(\kappa t_h+h/t_h=O(\sqrt h)\), so \(s_h=t_h/\sqrt h\) stays in a compact subset of \((0,\infty)\). Uniformly on such subsets,
\[
 \frac{1-J_h(s\sqrt h)/\sigma}{\sqrt h}\longrightarrow
 \kappa s+\frac1s.
\]
The function on the right has the unique global minimum \(2\sqrt\kappa\) at \(s=1/\sqrt\kappa\). Consequently every maximizing sequence satisfies \(t_h/\sqrt{h/\kappa}\to1\), and matching the upper and lower bounds in (4)–(5) gives the stated optimal-rate asymptotic.

## Verification
`CHECKER.py` is a complete Python 3 standard-library reproducibility script. For four distinct parameter sets it independently constructs the four-dimensional forward and reverse Gaussian covariance matrices and checks the KL formula against the two-dimensional conditional representation and the evaluated noiseless rational formula. It also tests positive-noise and noiseless inequalities, the infinitesimal decay coefficient, and the square-root optimum and leading rate-loss asymptotic numerically. Run `python CHECKER.py`; the packaged run reported 64 passed checks. The finite numerical checks corroborate, but do not establish, the global analytic proof.

## Relationship to prior work
Viot et al., *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248 (first submitted 2023-07-11), study the same Gaussian two-bath gyrator and finite-step fluctuations of angular momentum and angular velocity; they do not evaluate the noisy pairwise forward/reverse KL optimum in the inspected main text and supplementary material. Lucente et al., arXiv:2306.14558, develop scale-dependent empirical entropy-production diagnostics, including a Poisson-driven gyrator; their finite-resolution objects and results are different. Otsubo et al., Communications Physics 5, 11 (2022), show empirically that increasing the interval may mitigate measurement-noise bias in entropy-production inference, but do not give this exact model-specific universal optimum. Mazzolo and Monthus, arXiv:2210.05353, treat continuous-path entropy-production large deviations, not independent-noise two-frame sampling. Generic Gaussian relative-entropy and data-processing identities are established tools and are not claimed as new. The assessed contribution is the exact two-time-noise optimization and its sharp \(\sqrt h\) scaling with model-independent leading coefficient within this gyrator family.

## Limitations
The result concerns *two-time marginal* KL divergence per lag, not entropy production for the full observed process, not finite-sample estimator variance, and not a thermodynamic efficiency optimum. Gaussian white readout errors are independent across frames and have covariance exactly \(h\operatorname{diag}(T_x,T_y)\), a physically motivated but restrictive proportional-noise assumption; arbitrary readout anisotropy can change the leading coefficient. The square-root asymptotic is pointwise in fixed nonzero coupling and temperature contrast, not uniform as the process approaches equilibrium. The proof does not establish uniqueness of the optimizer for each finite \(h\); only the universal limiting behavior of all optimizers. A broader pre-existing Gaussian channel theorem might imply portions of this specialization, and publication priority has not been independently certified.

## References
1. P. Viot, A. Argun, G. Volpe, A. Imparato, L. Rondoni, and G. Oshanin, *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248, 2023; Soft Matter 20, 3154–3160 (2024). https://arxiv.org/abs/2307.05248
2. D. Lucente, A. Puglisi, M. Viale, and A. Vulpiani, *Statistical features of systems driven by non-Gaussian processes: theory & practice*, arXiv:2306.14558 (2023). https://arxiv.org/html/2306.14558v2
3. S. Otsubo, S. K. Manikandan, T. Sagawa, and S. Krishnamurthy, *Estimating time-dependent entropy production from non-equilibrium trajectories*, Communications Physics 5, 11 (2022). https://doi.org/10.1038/s42005-021-00787-x
4. A. Mazzolo and C. Monthus, *Nonequilibrium diffusion processes via non-Hermitian electromagnetic quantum mechanics with application to the statistics of entropy production in the Brownian gyrator*, arXiv:2210.05353 (2022). https://arxiv.org/abs/2210.05353
