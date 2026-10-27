# Protocol-dependent prefactor for strongly reset active Ornstein–Uhlenbeck search

## Finding

Consider an active Ornstein–Uhlenbeck particle on a fixed interval with absorption at the left endpoint and reflection at the right endpoint. With **complete Poisson resetting** of both position and propulsion velocity, the logarithmically leading high-resetting search cost is Brownian, but its exact multiplicative prefactor retains the *entire exponential moment of the velocity-reset distribution*. In the model defined below, writing \(\tau\) for the absorption time without resetting, \(r>0\) for the complete-resetting rate, and \(p_r=\mathbb E[e^{-r\tau}]\),

\[
\lim_{r\to\infty}e^{x_0\sqrt{r/D}}p_r=\mathbb E_\rho[e^{-x_0 V_0/(2D)}]=:A_\rho.
\]

Consequently the exact mean completion time \(\mathcal T_r\) under resetting satisfies

\[
\lim_{r\to\infty}r e^{-x_0\sqrt{r/D}}\mathbb E[\mathcal T_r]=A_\rho^{-1}.
\]

For a prescribed reset velocity \(V_0=v\), \(A_\rho=e^{-x_0v/(2D)}\). If instead \(V_0\) is redrawn at every reset from the stationary OU distribution \(\mathcal N(0,D_v/\tau_p)\), then

\[
A_\rho=\exp\!\left(\frac{x_0^2D_v}{8D^2\tau_p}\right).
\]

Thus the limiting ratio of the Gaussian-redraw to zero-velocity-redraw mean completion times is \(\exp[-x_0^2D_v/(8D^2\tau_p)]\), even though the two protocols share the same leading divergent factor \(e^{x_0\sqrt{r/D}}/r\). No weak-activity assumption is made.

## Assumptions and scope

Fix \(L>0\), \(x_0\in(0,L)\), spatial diffusivity \(D>0\), persistence time \(\tau_p>0\), and active-noise parameter \(D_v>0\). Between resets, let \(B,W\) be independent standard Brownian motions and solve

\[
 dX_t=V_t\,dt+\sqrt{2D}\,dB_t-dK_t,\qquad
 dV_t=-\tau_p^{-1}V_t\,dt+\frac{\sqrt{2D_v}}{\tau_p}\,dW_t.
\]

Here \(K\) is the minimal continuous nondecreasing upper Skorokhod regulator: it increases only at \(X_t=L\), maintaining \(X_t\le L\). The evolution is stopped when \(X_t=0\). The starting state is \(X_0=x_0\), with \(V_0\sim\rho\), independent of \(B,W\). We permit (i) a deterministic finite \(V_0\), or (ii) a nondegenerate centered Gaussian \(V_0\) of any fixed finite variance (the stationary choice has variance \(D_v/\tau_p\)).

For the reset process, independent Poisson times of rate \(r\) replace \((X,V)\) with an independent fresh \((x_0,V_0)\) and restart both driving Brownian motions. The stopping time \(\mathcal T_r\) ends the process at the first absorption. The limit is \(r\to\infty\) with all spatial and OU parameters fixed; it is not uniform when \(D\downarrow0\), \(x_0\downarrow0\), or \(L-x_0\downarrow0\).

## Proof

**1. An exact constant-drift comparison.** For constant drift \(a\in\mathbb R\), denote by \(\tau^a\) the absorption time for Brownian motion with generator \(D\partial_{xx}+a\partial_x\) reflected at \(L\), starting at \(x_0\). Its Laplace transform \(u_r^a(x)=\mathbb E_x[e^{-r\tau^a}]\) solves

\[
Du''+au'-ru=0,\qquad u(0)=1,\quad u'(L)=0.
\]

Writing \(s=\sqrt{a^2+4Dr}\), \(\alpha=(s+a)/(2D)\), and \(\beta=(s-a)/(2D)\), the exact solution is

\[
u_r^a(x)=\frac{e^{-\alpha x}+(\alpha/\beta)e^{-(\alpha+\beta)L+\beta x}}{1+(\alpha/\beta)e^{-(\alpha+\beta)L}}.
\]

For fixed \(a\), \(e^{x_0\sqrt{r/D}}u_r^a(x_0)\to e^{-ax_0/(2D)}\). Moreover, uniformly for \(r\ge1\) and all real \(a\),

\[
e^{x_0\sqrt{r/D}}u_r^a(x_0)\le2\exp(C|a|),\qquad C=x_0/(2D)+1/\sqrt D.
\]

Indeed \(s\ge2\sqrt{Dr}\), \(\alpha/\beta=\exp[2\operatorname{arsinh}(a/(2\sqrt{Dr}))]\le\exp(|a|/\sqrt D)\), and the two numerator terms obey the displayed bound separately.

**2. Pathwise comparison for a time-dependent velocity.** For a continuous input path \(y\) starting below \(L\), upper reflection is \(\Gamma_L(y)_t=y_t-\sup_{s\le t}(y_s-L)_+\). If \(y_2-y_1\) is nonnegative and nondecreasing, then \(\Gamma_L(y_2)_t\ge\Gamma_L(y_1)_t\), since the two regulators differ by at most \(y_2(t)-y_1(t)\). On \([0,T]\), put

\[
Z_T=\sup_{0\le s\le T}|V_s-V_0|,\qquad a_-=V_0-Z_T,\quad a_+=V_0+Z_T.
\]

Using the same spatial Brownian motion, monotonicity implies \(\tau^{a_-}\le\tau\le\tau^{a_+}\) up to the observation horizon \(T\), because the integrated drift differences are nondecreasing. With \(F_T(t)=e^{-rt}\mathbf1_{\{t\le T\}}\), a decreasing function of \(t\), and conditioning on the independent velocity path, one obtains

\[
\mathbb E[u_r^{a_+}(x_0)]-e^{-rT}\le p_r\le\mathbb E[u_r^{a_-}(x_0)]+e^{-rT}.
\]

The error bound follows since \(0\le e^{-r\tau}-F_T(\tau)\le e^{-rT}\), also when \(\tau=\infty\).

**3. Limit and integrability.** Choose \(T=r^{-1/3}\). Then \(e^{x_0\sqrt{r/D}-rT}\to0\). OU paths are continuous, so \(Z_T\to0\) almost surely, and hence \(a_\pm\to V_0\). The OU representation and Gaussian maximal estimates imply \(\mathbb E\exp[c\sup_{0\le t\le1}|V_t|]<\infty\) for every finite \(c>0\), for either allowed initial law. The exponential bound from Step 1 and dominated convergence therefore imply

\[
\mathbb E[e^{x_0\sqrt{r/D}}u_r^{a_\pm}(x_0)]\longrightarrow \mathbb E[e^{-x_0V_0/(2D)}].
\]

The sandwich in Step 2 yields the first assertion. The argument requires neither small active variance nor rapid OU decorrelation: persistence influences the limiting prefactor only through the chosen initial-velocity law.

**4. Renewal identity and protocols.** Complete resetting gives independent search cycles. With \(p_r=\Pr(\tau<E_r)=\mathbb E[e^{-r\tau}]\), where \(E_r\) is independent exponential of rate \(r\), the exact renewal equation yields

\[
\mathbb E[\mathcal T_r]=\frac{1-p_r}{r p_r}.
\]

Since \(x_0>0\) and paths are continuous, \(p_r\to0\). Inserting Step 3 gives the stated mean-time asymptotic. For Gaussian \(V_0\sim\mathcal N(0,\sigma^2)\), its exponential moment equals \(\exp[x_0^2\sigma^2/(8D^2)]\); stationarity means \(\sigma^2=D_v/\tau_p\).

## Verification

The independent numerical script `artifacts/check.py` checks the constant-drift boundary-value solution against the differential equation and boundary data, evaluates its large-\(r\) prefactor for several drift directions, tests the normalized Gaussian-redraw limit by deterministic Gauss–Hermite quadrature, and verifies the deterministic upper-reflection comparison on sampled continuously interpolated input paths. These are finite tests of exact intermediate formulas, not substitutes for the limiting argument in Steps 2–3. Run with `python artifacts/check.py` with NumPy and SciPy installed.

## Relationship to prior work

Georgiou, Bressloff, and Bertrand (2026), arXiv:2609.21124v1, investigate first-passage statistics for the same confined AOUP model and analyze fixed-velocity versus Gaussian velocity reinitialization numerically. Their published perturbation theory is in weak activity; the exact high-reset-rate velocity-distribution prefactor above is not among their stated formulas. Linn and Lawley (2023), arXiv:2302.05409v1, give broad, rigorous frequent-resetting renewal asymptotics **conditional on short-time first-passage estimates** (including their Theorem 3) and treat diffusive and run-and-tumble examples. This finding supplies the corresponding coefficient for a confined particle driven by continuous OU propulsion; their general renewal theorem does not by itself compute that coefficient. The renewal identity itself is not new (Pal and Reuveni, 2017). Shankari and Sahoo (2025), arXiv:2509.18515v1, treat stationary displacement statistics under resetting, not absorption-time prefactors for the confined overdamped process.

## Limitations

The finding is an asymptotic, not a finite-rate closed form. The limit fixes strictly positive translational diffusivity; it does not apply to purely active motion with \(D=0\), a velocity that persists across resetting events, or an initial reset velocity whose distribution changes with \(r\). The result is a refinement of the known frequent-restart universality framework; a broader previously published short-time theorem might implicitly imply the same coefficient, so the priority comparison is not exhaustive. Independent verification has not been performed.

## References

1. D. K. Georgiou, P. C. Bressloff, and T. Bertrand, *Persistence, resetting, and first-passage times of an active Ornstein–Uhlenbeck particle*, arXiv:2609.21124v1 (first posted 2026-09-17), https://arxiv.org/abs/2609.21124.
2. S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, Physical Review E 108, 024114 (2023), arXiv:2302.05409, https://arxiv.org/abs/2302.05409.
3. A. Pal and S. Reuveni, *First Passage under Restart*, Physical Review Letters 118, 030603 (2017), arXiv:1607.06048, https://arxiv.org/abs/1607.06048.
4. U. Shankari and M. Sahoo, *Active Ornstein–Uhlenbeck particle under stochastic resetting*, arXiv:2509.18515v1 (2025), https://arxiv.org/abs/2509.18515.
