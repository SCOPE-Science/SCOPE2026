# A marked clock-fluctuation law for frequently reset stable flights

## Finding

A frequently reset symmetric stable flight exits a bounded interval after a macroscopic exponential waiting time, but its final successful attempt lasts only on the inverse-reset-rate scale. Its exit side and normalized overshoot have an explicit marked law. More subtly, the error incurred by estimating first-exit time by the number of resets divided by the reset rate is not asymptotically Gaussian: it is a Gaussian scale mixture with an exactly Laplace marginal.

Let \(E,Z,H,S,U\) be independent variables with \(E\sim\operatorname{Exp}(A)\), \(Z\sim N(0,1)\), \(H\sim\operatorname{Exp}(1)\), \(\Pr(S=\pm)=A_\pm/A\), and \(\Pr(U>u)=(1+u)^{-\alpha}\) for \(u\ge0\). The single joint assertion is

\[
\boxed{(N_r/r,T_r,\sqrt r(T_r-N_r/r),rH_r,S_r,U_r)\Longrightarrow(E,E,\sqrt E Z,H,S,U).}
\]

In particular, the unconditioned clock-error limit \(Y=\sqrt E Z\) has characteristic function \(A/(A+\xi^2/2)\) and density \(\sqrt{A/2}\exp(-\sqrt{2A}|y|)\). The limit variables \(E\) and \(Y\) are dependent: \(Y\mid E=t\sim N(0,t)\). The final-attempt mark \((H,S,U)\) is independent of both.

## Assumptions and scope

Fix \(0<\alpha<2\), \(\sigma>0\), \(L>0\), and \(x\in(-L,L)\). The free process \(X\) starts at \(x\) and is normalized by

\[
\mathbb E[e^{i\xi(X_t-x)}]=e^{-t\sigma^\alpha|\xi|^\alpha}.
\]

Write \(\tau=\inf\{t\ge0:X_t\notin(-L,L)\}\). Its Levy jump density is \(\nu(dz)=c_\alpha\sigma^\alpha|z|^{-1-\alpha}\,dz\), where \(c_\alpha=\Gamma(1+\alpha)\sin(\pi\alpha/2)/\pi\). The positive and negative one-jump exit rates are

\[
A_+=\frac{c_\alpha\sigma^\alpha}{\alpha(L-x)^\alpha},\qquad
A_-=\frac{c_\alpha\sigma^\alpha}{\alpha(L+x)^\alpha},\qquad A=A_++A_->0.
\]

For each \(r>0\), make independent copies of the free process and independent exponential reset clocks of rate \(r\). If a reset clock rings before that copy exits, discard the copy and restart at \(x\); otherwise stop at its free exit. Let \(N_r\in\{0,1,\ldots\}\) count failed attempts, \(T_r\) be total physical duration, and \(H_r\) the free exit duration on the successful attempt. Define \(S_r=+\) on exit to the right and \(S_r=-\) on exit to the left. If the final exit position is \(Y_r^{\mathrm{exit}}\), let

\[
U_r=\begin{cases}(Y_r^{\mathrm{exit}}-L)/(L-x),&S_r=+,\\
(-L-Y_r^{\mathrm{exit}})/(L+x),&S_r=-.
\end{cases}
\]

The process is stopped at the first point *outside* the open interval; any exact-boundary exit contributes no positive mass in the limiting mark measure. The theorem concerns fixed \(L,x,\sigma,\alpha\) and \(r\to\infty\); it does not assert a uniform limit as \(\alpha\to2\) or as \(x\) approaches the boundary.

## Proof

**1. Small-time marked exit.** For any bounded continuous test function \(f\) on exit location whose discontinuities have zero Levy-measure mass, the standard single-large-jump small-time limit gives

\[
\lim_{t\downarrow0}\frac{1}{t}\mathbb E[f(X_\tau)\mathbf1_{\{\tau\le t\}}]
=\int_{\mathbb R\setminus(-L,L)}f(y)c_\alpha\sigma^\alpha|y-x|^{-1-\alpha}\,dy.\tag{1}
\]

A justification uses a fixed threshold below the distance from \(x\) to both endpoints, separates the compound-Poisson jumps above that threshold from the bounded-jump remainder, and excludes two significant jumps with \(O(t^2)\) probability. The bounded-jump process cannot move a fixed positive distance with probability of order \(t\), by exponential-martingale bounds. First restrict exit locations away from either boundary; the probability of a one-jump exit within a boundary strip of width \(\varepsilon\) is \(O(\varepsilon t)\), so the strip can then shrink. This establishes the vague marked statement, its total-mass counterpart (use tightness of exit marks), and the claimed side and excess distributions. The underlying exit and overshoot small-time techniques are developed in Figueroa-Lopez and Tankov [3]; the unmarked total-mass asymptotic is also explicitly used by Zbik and Palmowski [1]. In particular,

\[
\Pr(\tau\le t)=At+o(t),\quad
p_r:=\mathbb E e^{-r\tau}=A/r+o(1/r).\tag{2}
\]

For a marked exit set \(B\), set \(Q_B(a)=\mathbb E[e^{-a\tau}\mathbf1_{\{X_\tau\in B\}}]\). Equation (1), with integration by parts and exponential kernels, yields \(aQ_B(a)\to\nu(B-x)\), for boundary-null sets; here \(\nu(B-x)\) means the integral on the right of (1) restricted to \(B\). Set \(Q=Q_{\mathbb R\setminus(-L,L)}\).

**2. Exact regeneration identity.** An attempted flight succeeds with probability \(p_r=Q(r)\). Thus \(N_r\) is geometric on \(\{0,1,\ldots\}\), \(\Pr(N_r=n)=(1-p_r)^np_r\). Conditional on failure, the reset interval \(D_r\) has density

\[
\frac{re^{-rt}\Pr(\tau>t)}{1-p_r},\qquad t>0.\tag{3}
\]

The failed durations are independent and independent of the terminal successful flight and its exit mark. If \(s,v,u\ge0\), geometric summation gives the following exact marked Laplace transform:

\[
\mathbb E[e^{-sT_r-vN_r-urH_r}\mathbf1_{\{Y_r^{\mathrm{exit}}\in B\}}]
=\frac{Q_B(r+s+ur)}{1-e^{-v}\frac r{r+s}[1-Q(r+s)]}.\tag{4}
\]

Indeed, a failed trial contributes \(e^{-v}\mathbb E[e^{-sE_r}\mathbf1_{E_r<\tau}]=e^{-v}r[1-Q(r+s)]/(r+s)\), and the successful trial contributes \(Q_B(r+s+ur)\). This is a marked refinement of the classical renewal transform, not a claim that the unmarked transform itself is new [4].

**3. Macro time, micro time, and marks.** Equation (2) and the geometric law imply \(N_r/r\Rightarrow E\sim\operatorname{Exp}(A)\). For every \(u\ge0\) and marked continuity set \(B\), independence of the successful trial gives

\[
\mathbb E[e^{-urH_r}\mathbf1_{\{Y_r^{\mathrm{exit}}\in B\}}\mid\text{success}]
=\frac{Q_B((1+u)r)}{Q(r)}\longrightarrow
\frac{\nu(B-x)/A}{1+u}.\tag{5}
\]

Therefore the success duration converges to a unit exponential and is independent of the limiting exit mark. The exact independence between success and the previous failures makes these marks independent of \(N_r/r\), too. The stable Levy density yields \(\Pr(S=\pm)=A_\pm/A\) and, conditional on either side,

\[
\Pr(U>u\mid S=\pm)=\frac{\int_{(1+u)d_\pm}^\infty z^{-1-\alpha}\,dz}{\int_{d_\pm}^\infty z^{-1-\alpha}\,dz}=(1+u)^{-\alpha}.\tag{6}
\]

Thus \(S\) and \(U\) are independent even when the starting point is off-center.

**4. The non-Gaussian fluctuation mechanism.** Since \(\Pr(\tau\le t)\le Ct\) for some finite \(C\) and every \(t\ge0\), equation (3) yields

\[
\mathbb E(rD_r)=1+O(r^{-1}),\qquad
\operatorname{Var}(rD_r)\to1,\qquad
\sup_{r\ge r_0}\mathbb E e^{\theta rD_r}<\infty\quad(\theta<1).\tag{7}
\]

For the first bound, subtract the truncated integrand from the mean of a unit exponential, use \(\Pr(\tau\le t)\le Ct\), and divide by \(1-p_r\); analogous dominated convergence proves the second. The exponential domination supplies uniform third moments. With independent failed durations \(D_{r,j}\) define

\[
W_r=\sqrt r\Big(\sum_{j=1}^{N_r}D_{r,j}-N_r/r\Big)=\frac1{\sqrt r}\sum_{j=1}^{N_r}(rD_{r,j}-1).
\]

The conditional characteristic function of one centered summand is \(1-\xi^2/(2r)+o(1/r)\), uniformly on compact \(\xi\)-sets. Since \(N_r/r\) is tight and converges to \(E\), for real \(\xi,\eta\)

\[
\mathbb E e^{i\eta N_r/r+i\xi W_r}
\longrightarrow \mathbb E e^{(i\eta-\xi^2/2)E}
=\frac{A}{A-i\eta+\xi^2/2}.\tag{8}
\]

The right side is the joint transform of \((E,\sqrt E Z)\), where \(Z\sim N(0,1)\) is independent of \(E\). Joint convergence with the successful-trial variables follows from their exact independence from all failed attempts. Finally,

\[
T_r=\sum_{j=1}^{N_r}D_{r,j}+H_r,
\]

and \(rH_r=O_{\mathbb P}(1)\), so \(T_r-N_r/r=o_{\mathbb P}(1)\) while \(\sqrt r H_r=o_{\mathbb P}(1)\). Slutsky's theorem completes the asserted six-dimensional joint limit. Integrating the Gaussian characteristic function over \(E\sim\operatorname{Exp}(A)\) gives \(A/(A+\xi^2/2)\), the symmetric Laplace density shown in the finding.

## Verification

The included standalone `verify.py` replays the exact renewal-transform algebra against the solvable exponential-hazard competing-clock model, validates the positive and negative jump-intensity integrals, checks that the side-conditioned excess law normalizes to one for several stable indices and asymmetries, and checks numerical Fourier/Laplace identities and moments of the Gaussian-exponential mixture. Assertions count and tolerances are reported by the script. These finite checks independently stress-test the displayed constants and transformations; they do not certify the infinite-process limit in place of the proof.

## Relationship to prior work

[1] Zbik and Palmowski (2026) study this symmetric stable-flight setting and derive mean first-exit asymptotics at rapid Poisson resetting. Their cited small-time exit rate \(A\) is used here, rather than rediscovered. They do not develop reset-count fluctuations or a joint exit-side/excess law.

[2] Linn and Lawley (2023), Theorem 1, prove the general exponential first-passage limit under frequent resetting; the marginal limit \(T_r\Rightarrow\operatorname{Exp}(A)\) is already covered by their theorem and is not claimed as original.

[3] Figueroa-Lopez and Tankov (2014), especially Proposition 2.1 and its small-time analysis, give the precursor Levy exit/overshoot asymptotics; neither the one-jump limit nor the conditional Pareto calculation alone is a new claim.

[4] Sunil et al. (2023), equation (10), derive a general joint reset-count/time renewal transform. The unmarked specialization of (4) is therefore known. The statement assessed here is the **combined six-dimensional two-scale limit**, particularly the mixed-normal / Laplace discrepancy between time and normalized reset count together with its asymptotically independent marked final excursion. Deriving this requires the random-index fluctuation argument (7)–(8), not just the previously established first-order exponential limit.

## Limitations

No rate of convergence or uniformity near the Gaussian endpoint \(\alpha=2\) is claimed. The limiting signed excess density is not a statement about free-flight overshoots at long time. The clock-error limit is not independent of the limiting completion time. Prior general renewal formulas could make parts of the assertion a derivable corollary; its priority as a *joint* second-order theorem remains subject to further literature comparison and independent review. Numerical and exact finite checks cannot replace the probabilistic limit arguments.

## References

1. B. Zbik and Z. Palmowski, *Asymptotic behaviour for escaping an interval by Levy flights under stochastic resetting*, arXiv:2610.20410v1 (first public October 14, 2026), https://arxiv.org/abs/2610.20410.
2. S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, Physical Review E 108, 024114 (2023), arXiv:2302.05409, https://arxiv.org/abs/2302.05409.
3. J. E. Figueroa-Lopez and P. Tankov, *Small-time asymptotics of stopped Levy bridges and simulation schemes with controlled bias*, Bernoulli 20 (2014), 1126–1164, arXiv:1203.2355, https://arxiv.org/abs/1203.2355.
4. J. C. Sunil, R. A. Blythe, M. R. Evans, and S. N. Majumdar, *The cost of stochastic resetting*, Journal of Physics A 56 (2023), 395001, arXiv:2304.09348, https://arxiv.org/abs/2304.09348.
