# Algebraic spatial clustering from global Pareto resetting in the one-dimensional Glauber chain

## Finding
Consider the nearest-neighbor kinetic Ising chain on \(\mathbb Z\), reset **globally** to one fixed initial spin configuration at independent intervals with survival law \(\Pr(W>t)=1\) for \(0\leq t<\tau_0\), and \(\Pr(W>t)=(\tau_0/t)^\alpha\) for \(t\geq\tau_0\), where \(\alpha>1\), \(\tau_0>0\). Draw that initial configuration once from independent spins of mean \(m_0\in(-1,1)\), and average the following correlations over the initial configuration, the spin dynamics, and the stationary renewal age. Write \(G_\ell(T)=\mathbb E[\sigma_0\sigma_\ell]-\mathbb E[\sigma_0]\mathbb E[\sigma_\ell]\) for integer \(\ell\geq1\).

At zero temperature, the stationary connected two-point function has the exact spatial tail
\[
\boxed{\lim_{\ell\to\infty}\ell^{2(\alpha-1)}G_\ell(0)
=(1-m_0^2)\frac{(4\tau_0)^{\alpha-1}}{\alpha\sqrt\pi}\Gamma\!\left(\alpha-\tfrac12\right)>0.}
\]
For \(p=\alpha-1\), define the exact gamma-ratio comparison
\[
B_{\ell,p}=\frac{2\ell\,\Gamma(2p)\Gamma(\ell-p)}{\Gamma(p)(\ell+p)\Gamma(\ell+p)},\qquad \ell>p.
\]
For integer \(\ell>\max\{p,2\tau_0\}\), the quantitative finite-distance statement is
\[
0\le \frac{(1-m_0^2)\tau_0^p}{\alpha}B_{\ell,p}-G_\ell(0)
\le\frac{1-m_0^2}{\alpha}\left(\frac{2e\tau_0}{\ell}\right)^\ell\!\left(1+\frac p{\ell-p}\right).
\]
Thus algebraic spatial clustering persists for every finite Pareto exponent \(\alpha>1\), with an exponent continuously controlled by the renewal tail.

For comparison, at every strictly positive finite temperature let \(\gamma=\tanh(2\beta J)\in(0,1)\), \(\kappa=1-\gamma\), \(q=(1-\sqrt{1-\gamma^2})/\gamma<1\) and \(L(s)=\mathbb E[e^{-sA}]\) for stationary renewal age \(A\). Then
\[
G_\ell(T)=m_0^2\bigl[L(2\kappa)-L(\kappa)^2\bigr]+R_\ell,
\qquad 0\le R_\ell\le q^\ell.
\]
In particular, when \(m_0=0\), positive-temperature spatial correlations are exponentially bounded rather than algebraic. For \(m_0\neq0\), the positive-temperature connected function approaches the positive, spatially constant covariance induced by the common renewal age; the spatially varying remainder is exponentially bounded. The age-induced plateau alone is not claimed to be new.

## Assumptions and scope
The infinite-volume Glauber spin-flip rate is
\[
w_i(\sigma)=\tfrac12\bigl[1-\tfrac\gamma2\sigma_i(\sigma_{i-1}+\sigma_{i+1})\bigr],\qquad
\gamma=\tanh(2\beta J),\quad J>0.
\]
Time is normalized so each site has unit-rate Poisson update opportunities. The zero-temperature case means \(\gamma=1\), with voter-model coalescing duality. At every reset time the entire system returns to the **same** initially sampled independent Bernoulli spin field; it is *not* reset sitewise, nor is a new spin field drawn at every reset. All displayed stationary moments are annealed. The initial reset field is independent of the renewal intervals and the dynamical randomness. \(\mathbb E W=\alpha\tau_0/(\alpha-1)<\infty\), so the equilibrium age distribution exists. No assertion is made here for \(\alpha\le1\), quenched correlations conditional on a particular reset field, or non-nearest-neighbor dynamics.

The stationary age density and survival are, respectively,
\[
g_A(t)=\frac{\alpha-1}{\alpha\tau_0}\begin{cases}1,&0\le t\le\tau_0,\\ (\tau_0/t)^\alpha,&t>\tau_0,\end{cases}
\quad
H_A(t)=\Pr(A\ge t)=\begin{cases}1-\frac{(\alpha-1)t}{\alpha\tau_0},&0\le t\le\tau_0,\\\frac1\alpha(\tau_0/t)^{\alpha-1},&t>\tau_0.\end{cases}
\]
The density is continuous at \(\tau_0\) and integrates to one; the survival formula likewise agrees at \(\tau_0\).

## Proof
**1. Coalescing-walk reduction at zero temperature.** The standard graphical dual of the zero-temperature Glauber/voter model sends two spins at distance \(\ell\) backwards along nearest-neighbor continuous-time random walks until they coalesce. Each ancestral line jumps left and right with rate \(1/2\). Their separation before coalescence therefore has a symmetric nearest-neighbor birth/death walk whose up and down rates are each one. Let \(T_\ell\) be its first hitting time of zero from \(\ell\). Conditional on a coalescence, the two spins have the same initial ancestor; without one they come from independent initial Bernoulli spins. Consequently, for each fixed elapsed time \(t\),
\[
\mathbb E[\sigma_0(t)\sigma_\ell(t)]=m_0^2+(1-m_0^2)\Pr(T_\ell\le t),\qquad
\mathbb E[\sigma_i(t)]=m_0.
\]
Averaging over the independent stationary age \(A\) gives the exact identity
\[
G_\ell(0)=(1-m_0^2)\mathbb E[H_A(T_\ell)].
\]
This is an annealed statement: the fixed reset configuration is averaged only after the equal-time pair product is formed.

**2. Exact inverse hitting-time moment.** The generator of the separation walk is \(\Delta f(n)=f(n+1)+f(n-1)-2f(n)\). Solving \(\Delta u=su\) for the bounded solution with \(u(0)=1\) yields
\[
\mathbb E[e^{-sT_\ell}]=\left(\frac{s+2-\sqrt{s(s+4)}}2\right)^\ell,\qquad s>0.
\]
Since \(p>0\), the Mellin–Laplace formula gives
\[
\mathbb E[T_\ell^{-p}]=\frac1{\Gamma(p)}\int_0^\infty s^{p-1}\mathbb E[e^{-sT_\ell}]\,ds.
\]
Put \(s=2(\cosh\theta-1)\) and then \(v=e^{-\theta}\). The integral becomes
\[
\frac1{\Gamma(p)}\int_0^1 v^{\ell-p-1}(1-v)^{2p-1}(1+v)\,dv
=\frac{\mathrm B(\ell-p,2p)+\mathrm B(\ell-p+1,2p)}{\Gamma(p)}=B_{\ell,p}
\]
provided \(\ell>p\). These substitutions establish, rather than assume, the exact gamma-ratio identity.

**3. Quantitative cutoff correction.** By the displayed age survival formula, the difference between \((\tau_0^p/\alpha)\mathbb E[T_\ell^{-p}]\) and \(\mathbb E[H_A(T_\ell)]\) is nonnegative and supported on \(T_\ell\le\tau_0\). The pointwise inequality follows by putting \(u=t/\tau_0\in(0,1]\) and applying the convex tangent bound \(u^{-p}\ge (p+1)-pu\). Thus
\[
0\le\frac{\tau_0^p}{\alpha}\mathbb E[T_\ell^{-p}]-\mathbb E[H_A(T_\ell)]
\le\frac{\tau_0^p}{\alpha}\mathbb E[T_\ell^{-p};T_\ell\le\tau_0].
\]
For the separation walk to hit zero it must make at least \(\ell\) jumps. Its total jump rate is two until absorption; domination by a rate-two Poisson process and the elementary Poisson Chernoff bound imply
\[
F_\ell(t):=\Pr(T_\ell\le t)\le\left(\frac{2et}{\ell}\right)^\ell,\qquad 0<t\le\tau_0,\quad \ell>2\tau_0.
\]
Integration by parts yields
\[
\mathbb E[T_\ell^{-p};T_\ell\le\tau_0]
=\tau_0^{-p}F_\ell(\tau_0)+p\int_0^{\tau_0}t^{-p-1}F_\ell(t)\,dt
\le\tau_0^{-p}\left(\frac{2e\tau_0}{\ell}\right)^\ell\!\left(1+\frac p{\ell-p}\right).
\]
This proves the claimed finite-distance error after multiplying by \(1-m_0^2\). Finally, the gamma-ratio limit \(\Gamma(\ell-p)/\Gamma(\ell+p)\sim\ell^{-2p}\), together with the gamma duplication identity \(2\Gamma(2p)/\Gamma(p)=4^p\Gamma(p+1/2)/\sqrt\pi\), proves the sharp asymptotic amplitude.

**4. Positive-temperature comparison.** The unreset pair function \(C_\ell(t)\) satisfies the closed Glauber equations
\[
\partial_tC_\ell=-2C_\ell+\gamma(C_{\ell-1}+C_{\ell+1}),\quad \ell\ge1,\qquad C_0(t)=1,\quad C_\ell(0)=m_0^2\ (\ell\ge1).
\]
The mean is \(m(t)=m_0e^{-\kappa t}\). Set \(u_\ell(t)=C_\ell(t)-m_0^2e^{-2\kappa t}\). It obeys the same homogeneous interior linear equation, initial data \(u_\ell(0)=0\), and boundary \(u_0(t)=1-m_0^2e^{-2\kappa t}\in[0,1]\). The time-independent comparison functions zero and \(q^\ell\) are lower and upper solutions because \(\gamma(q+q^{-1})=2\). Positivity/comparison for the killed birth/death semigroup gives \(0\le u_\ell(t)\le q^\ell\), uniformly in \(t\ge0\). Averaging in stationary age and subtracting the square of \(\mathbb E[m(A)]\) yields the asserted plateau decomposition. For \(\alpha>1\), the age law has positive continuous support, so \(\operatorname{Var}(e^{-\kappa A})=L(2\kappa)-L(\kappa)^2>0\) whenever \(\kappa>0\).

## Verification
A standalone Python checker in `verify.py` evaluates the **independent** zero-temperature hitting-time density \(f_\ell(t)=\ell e^{-2t}I_\ell(2t)/t\) against the equilibrium-age survival, without using the Mellin beta integral in its numerical integration. It independently evaluates the exact gamma ratio and leading amplitude, testing \(\alpha\in\{1.2,1.5,2,3\}\), \(\ell\in\{20,50,100\}\), and \(\tau_0=1\). All twelve comparisons passed; finite cutoff discrepancies obey the proved Poisson error bound to numerical precision, and the rescaled correlations approach the claimed amplitudes. The script requires Python, NumPy and SciPy and prints `Numerical checks completed` when all assertions pass. These finite checks illustrate but do not replace the full analytical argument.

## Relationship to prior work
V K and Nagar (2026, arXiv:2602.15495v1) introduce this global power-law-reset Glauber model and study the **distribution of spatially averaged magnetization**. Their conclusion explicitly identifies spatial correlations and domain growth under power-law resets as a further direction. Magoni, Majumdar and Schehr (2020, arXiv:2002.04867v1) study global **Poisson** resetting and magnetization distributions and likewise mention two-point functions as an extension. Grange (2022/2023, arXiv:2207.08590v6) analyzes voter-model two-point functions with **independent, sitewise Poisson** resets to the initial opinion, not simultaneous global Pareto resetting. The graphical dual and renewal-age distribution are classical ingredients; their use here is not claimed as new. The combined sharp stationary spatial exponent, amplitude, explicit gamma-ratio bound, and temperature contrast have not been identified in those inspected sources.

## Limitations
This is an exact **annealed**, infinite one-dimensional lattice statement. It does not assert spatial clustering conditional on the single fixed reset field. It requires finite-mean renewal intervals \(\alpha>1\) and independent Bernoulli initial spins, and excludes additional correlations present in non-product reset templates. At positive temperature the common-age plateau can be nonzero; exponential decay applies to the spatial remainder, and to the entire connected correlation only for \(m_0=0\). The parameter \(\gamma=0\) limit is not included in the comparison statement as written, but can be treated separately. The code checks finitely many cases; the theorem's full quantifiers are established analytically. As with any literature comparison, possible implicit or unindexed coverage by general renewal/coalescence theory is a remaining originality risk.

## References
1. Anagha V K and Apoorva Nagar, *Ising Model with Power Law Resetting*, arXiv:2602.15495v1, publicly posted 17 February 2026. https://arxiv.org/html/2602.15495v1
2. Matteo Magoni, Satya N. Majumdar, and Grégory Schehr, *Ising model with stochastic resetting*, arXiv:2002.04867v1 (2020). https://arxiv.org/html/2002.04867v1
3. Pascal Grange, *Voter model under stochastic resetting*, arXiv:2207.08590v6 (2023; first posted 2022). https://arxiv.org/html/2207.08590v6
4. Roy J. Glauber, *Time-Dependent Statistics of the Ising Model*, Journal of Mathematical Physics 4 (1963), 294–307. https://doi.org/10.1063/1.1703954
