# Joint bilateral excursion extremes and logistic spatial imbalance under sluggish diffusion with resetting

## Finding

For the nonsticky symmetric sluggish diffusion with generator \(Lf(x)=|x|^{-\alpha}f''(x)\), \(\alpha\geq0\), independently reset to zero at Poisson rate \(r>0\), write \(P_T=\sup_{0\leq t\leq T}X_t\) and \(N_T=-\inf_{0\leq t\leq T}X_t\). Both are nonnegative. The following is a single joint-extremes theorem: an exact two-sided survival transform at finite time, followed by independent Gumbel limits and explicit range/imbalance laws at long time.

Let \(\mu=(\alpha+2)^{-1}\), and for \(u>0\), \(z\geq0\), define
\[
E_u(z)={}_0F_1\!\left(;1-\mu;\mu^2uz^{1/\mu}\right),\qquad
O_u(z)=z\,{}_0F_1\!\left(;1+\mu;\mu^2uz^{1/\mu}\right).
\]
For \(a,b,s>0\), put
\[
H_u(a,b)=\frac{O_u(a)+O_u(b)}{E_u(a)O_u(b)+E_u(b)O_u(a)}.
\]
Then
\[
\boxed{\int_0^\infty e^{-sT}\Pr(P_T<a,\ N_T<b)\,dT
=\frac{1-H_{s+r}(a,b)}{s+rH_{s+r}(a,b)}.}
\]

For the joint long-time limit, set
\[
A_\mu=\frac{2^\mu\sqrt{\pi/2}}{\Gamma(1-\mu)},\quad
\beta=\tfrac12-\mu,\quad
c_T=\log(A_\mu rT)+\beta\log\log(A_\mu rT),
\]
where \(T\) is large enough that the iterated logarithm is defined. Then, as \(T\to\infty\) with \(\alpha,r\) fixed,
\[
\boxed{\left(2\mu\sqrt r\,P_T^{1/(2\mu)}-c_T,\quad
2\mu\sqrt r\,N_T^{1/(2\mu)}-c_T\right)
\Longrightarrow (G_+,G_-),}
\]
with \(G_+,G_-\) **independent standard Gumbel** random variables, each with CDF \(\exp(-e^{-x})\).

Write \(m_T=(c_T/(2\mu\sqrt r))^{2\mu}\) and \(w_T=2\mu m_T/c_T\), both for sufficiently large \(T\). Consequently,
\[
\boxed{\left(\frac{P_T+N_T-2m_T}{w_T},\quad
\frac{P_T-N_T}{w_T}\right)
\Longrightarrow (G_++G_-,G_+-G_-).}
\]
The second marginal is standard logistic:
\[
\Pr(G_+-G_-\leq d)=\frac1{1+e^{-d}},
\]
while the first marginal has the non-Gumbel CDF
\[
\Pr(G_++G_-\leq z)=2e^{-z/2}K_1(2e^{-z/2}),
\]
where \(K_1\) denotes the modified Bessel function of the second kind.

## Assumptions and scope

Fix any finite real \(\alpha\geq0\), resetting rate \(r>0\) and observation horizon \(T>0\). Between resets, \(X\) is the recurrent continuous symmetric diffusion on the real line in natural scale, with speed density proportional to \(|x|^\alpha\), specified away from zero by \(Lf=|x|^{-\alpha}f''\), and by continuity of the function and its first spatial derivative at the regular, nonsticky origin. Equivalently its forward equation is \(\partial_t p=\partial_x^2(|x|^{-\alpha}p)\). Each independent exponential resetting event instantly returns \(X\) to zero, and the process starts at zero at time zero. The generator convention has Brownian variance rate \(2\) when \(\alpha=0\); other normalizations require rescaling \(r\) and time. Boundary events \(<\) and \(\leq\) have equal probability for strictly positive levels. The long-time results have **fixed** \(r\) and \(\alpha\), and are not uniform in either parameter or lattice spacing.

## Proof

**1. Nonreset interval exit.** For \(\tau_{a,b}=\inf\{t\geq0:X_t\notin(-b,a)\}\) without resetting, its Laplace transform \(h(x)=\mathbb E_xe^{-u\tau_{a,b}}\) satisfies \(h''=u|x|^\alpha h\) off zero and \(h(-b)=h(a)=1\). The two positive-half-line solutions \(E_u,O_u\), obtained by the displayed \({}_0F_1\) series, obey \(E_u(0)=1\), \(E'_u(0)=0\), \(O_u(0)=0\) and \(O'_u(0)=1\), and solve the ODE. Matching \(h,h'\) at zero writes \(h(x)=cE_u(x)+dO_u(x)\) for positive \(x\), and \(h(-x)=cE_u(x)-dO_u(x)\) for positive \(x\). The two boundary equations give \(h(0)=H_u(a,b)\). Their denominator is positive since all series terms of \(E,O\) are positive for positive arguments. Hence \(H_u=\mathbb E_0e^{-u\tau_{a,b}}\), and the nonreset survival transform is \((1-H_u)/u\).

**2. Reset renewal identity.** Conditioning on the first reset, the two-sided survival probability \(S_r(T)=\Pr(P_T<a,N_T<b)\) obeys \(S_r(T)=e^{-rT}S_0(T)+r\int_0^T e^{-rt}S_0(t)S_r(T-t)\,dt\). Taking the Laplace transform and inserting \(\widetilde S_0(u)=(1-H_u)/u\) yields exactly the displayed finite-time transform. This is a two-sided absorbing-boundary calculation; a one-sided maximum formula alone does not fix the joint distribution.

**3. Rare positive and negative excursions.** For a *complete* independent reset interval of duration \(E\sim\operatorname{Exp}(r)\), let \(p_a\) and \(p_b\) be the probabilities of reaching \(a\) and \(-b\) before \(E\), respectively. Solving the decaying half-line boundary-value problem with the same two fundamental solutions gives
\[
p_a=G_r(a):=\left(E_r(a)+k_{\mu,r}O_r(a)\right)^{-1},\qquad
k_{\mu,r}=\frac{\Gamma(1-\mu)}{\Gamma(1+\mu)}(\mu\sqrt r)^{2\mu},
\]
and \(p_b=G_r(b)\) by reflection symmetry. The coefficient is fixed by choosing the solution decaying at negative infinity, expressible with the modified Bessel \(K_\mu\), and matching the constant and linear terms at the origin. Its large-level asymptotic, obtained from \(I_{\pm\mu}\), is
\[
G_r(a)\sim A_\mu\zeta_a^\beta e^{-\zeta_a},\qquad
\zeta_a=2\mu\sqrt r\,a^{1/(2\mu)}.
\]
If one complete excursion reaches **both** thresholds, it must hit one first, then cross zero before reaching the opposite one. Strong Markov at the first threshold, independence and memorylessness of the exponential reset time, and a second strong-Markov application at zero give
\[
0\leq p_{ab}:=\Pr(\text{both signs reached before }E)\leq2p_ap_b.
\]
The probability of touching either boundary in one complete interval is therefore \(q_{a,b}=p_a+p_b-p_{ab}=H_r(a,b)\).

**4. Joint Gumbel law.** For fixed \(\xi,\eta\in\mathbb R\) set \(a_T=[(c_T+\xi)/(2\mu\sqrt r)]^{2\mu}\) and \(b_T=[(c_T+\eta)/(2\mu\sqrt r)]^{2\mu}\), defined for large \(T\). Step 3 gives \(rTp_{a_T}\to e^{-\xi}\), \(rTp_{b_T}\to e^{-\eta}\), and \(rTp_{a_Tb_T}\leq 2rTp_{a_T}p_{b_T}\to0\). Thus \(rTq_{a_T,b_T}\to e^{-\xi}+e^{-\eta}\). For a fixed \(0<\varepsilon<1\), let \(n_-=\lfloor(1-\varepsilon)rT\rfloor\) and \(n_+=\lceil(1+\varepsilon)rT\rceil\). Let \(C_T\sim\operatorname{Poisson}(rT)\) be the number of completed reset intervals before \(T\). Compare the actual path with the first \(n_-\) or \(n_++1\) **whole** i.i.d. intervals in an infinite extension. This gives the rigorous sandwich
\[
(1-q)^{n_++1}-\Pr(C_T>n_+)
\ \leq S_r(T;a_T,b_T)\leq\
(1-q)^{n_-}+\Pr(C_T<n_-).
\]
The Poisson tails vanish. Taking \(T\to\infty\), then \(\varepsilon\downarrow0\), proves \(S_r(T;a_T,b_T)\to\exp(-e^{-\xi}-e^{-\eta})\), the CDF of two independent standard Gumbels. This argument explicitly handles the incomplete last interval and never assumes the reset count is independent of excursion maxima.

**5. Physical range and imbalance.** Taylor's formula for \(a=[\zeta/(2\mu\sqrt r)]^{2\mu}\) at \(\zeta=c_T\) gives \((P_T-m_T)/w_T\Rightarrow G_+\) and \((N_T-m_T)/w_T\Rightarrow G_-\) jointly. Summing and subtracting proves the last vector limit. If \(U,V\) are independent unit exponential random variables, then \(G_+=-\log U\), \(G_-=-\log V\). Consequently \(G_+-G_-=\log(V/U)\) has the stated logistic CDF and \(G_++G_-=-\log(UV)\), whose CDF is \(\int_0^\infty e^{-u-e^{-z}/u}\,du=2e^{-z/2}K_1(2e^{-z/2})\).

## Verification

A standalone, standard-library-only numerical checker (`verify.py`) reproduces the exact \(\alpha=0\) hyperbolic-function formula, checks the positive/negative overlap bounds, compares the special-function two-sided exit formula against independently discretized killed generators, evaluates differential-equation residuals, and tests rare-interval intensity scaling and the logistic identity. It contains \(142\) assertions. Its finite checks are supplements to, not replacements for, the full proof above. Run with `python3 verify.py`.

## Relationship to prior work

Frimpong, *Extremal and global-time statistics of sluggish random walks with stochastic resetting* (arXiv:2610.34568, first public October 25, 2026), establishes the diffusion convention, one-sided maximum transform and its Gumbel normalization; these are input facts and not claimed as new. The related Frimpong–Bresque–Roldán study (arXiv:2610.21962) develops resetting, first passage and occupation statistics. Singh–Pal (2021) treats renewal theory for the maximum and its attainment time; Godrèche–Luck (2022) treats maxima and records in resetting random walks. Dębicki–Hashorva–Michna (2026) treats one-sided supremum, infimum tails and temporal two-point distributions for reset Brownian motion. Méndez–Masó-Puigdellosas–Campos (2022) treats exit from absorbing intervals with Markovian resetting; the general renewal mechanism is already known. The present **joint** theorem is the explicit bilateral special-function transform for the singular sluggish diffusion together with the rare opposite-excursion estimate, asymptotic independence, and the two-sided range/imbalance laws; it does not repackage the one-sided Gumbel theorem as novel. Claim-level coverage beyond inspected sources remains a publication-priority risk.

## Limitations

No uniformity in \(\alpha\), \(r\), lattice mesh or observation threshold is asserted. The process is the symmetric, nonsticky natural-scale extension, not an arbitrary weak extension at the singular origin. Only convergence in law of the extreme vector and of the range/imbalance vector is proved; convergence of moments or finite-time independent extremes is not asserted. The exact finite-time expression is a Laplace transform in observation time, not a claimed elementary inverse. Physical range and signed imbalance have a common random limiting pair and are **not** asserted independent. The proof assumes memoryless independent Poisson resets, zero reset point, and a continuous symmetric diffusion. Independent mathematical and publication-priority validation has not been performed.

## References

1. T. D. Frimpong, *Extremal and global-time statistics of sluggish random walks with stochastic resetting*, arXiv:2610.34568 (first public 2026-10-25), https://arxiv.org/abs/2610.34568.
2. T. D. Frimpong, L. Bresque and É. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962 (2026), https://arxiv.org/abs/2610.21962.
3. P. Singh and A. Pal, *Extremal statistics for stochastic resetting systems*, arXiv:2102.07111 (2021), https://arxiv.org/abs/2102.07111.
4. C. Godrèche and J.-M. Luck, *Maximum and records of random walks with stochastic resetting*, arXiv:2203.01102 (2022), https://arxiv.org/abs/2203.01102.
5. K. Dębicki, E. Hashorva and Z. Michna, *Distributional and Extremal Behaviour of Brownian Motion with Exponential Resetting*, Methodology and Computing in Applied Probability 28, 79 (2026), https://doi.org/10.1007/s11009-026-10316-4.
6. V. Méndez, A. Masó-Puigdellosas and D. Campos, *Non-standard diffusion under Markovian resetting in bounded domains*, arXiv:2201.12043 (2022), https://arxiv.org/abs/2201.12043.
