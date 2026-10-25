# Erlang resetting creates a clock-order logarithmic correction in first-passage spatial extremes

## Finding

For a Brownian searcher repeatedly reset on a multi-stage renewal clock, the maximum attained before its first hit of an absorbing target has **different exponential tails according to the completed reset count**, a universal size-biased geometric law for that count conditional on an extreme excursion, and a Gumbel limit whose centering contains a clock-order dependent \(\log\log k\) term.

Fix an integer \(\ell\ge2\). The reset waiting time is Erlang with \(\ell\) exponential stages, each of rate \(r\). With notation from the next section, let

\[
K=\frac{C}{(\ell-1)!}\left(\frac r\omega\right)^{\ell-1},\qquad
K_0=\frac{C}{(\ell-1)!}\left(\frac {2r}\omega\right)^{\ell-1}.
\]

For every fixed integer \(k\ge1\), as the barrier \(m\to\infty\),

\[
\Pr(M>m\mid N=0)\sim\frac{K_0}{p}m^{\ell-1}e^{-\kappa m},\qquad
\Pr(M>m\mid N=k)\sim\frac{kK}{q}m^{\ell-1}e^{-\alpha m}.
\]

The unconditional tail is \(\Pr(M>m)\sim (K/p)m^{\ell-1}e^{-\alpha m}\), and the extreme-event-conditioned count has the limit

\[
\Pr(N=k\mid M>m)\longrightarrow
\begin{cases}0,&k=0,\\p^2 kq^{k-1},&k\ge1.\end{cases}
\]

The limiting probabilities sum to one. For \(k\to\infty\), put

\[
b_k=\log k+(\ell-1)\log\log k+\log\frac{K}{q\alpha^{\ell-1}}.
\]

For every real \(s\),

\[
\lim_{k\to\infty}\Pr\bigl(\alpha M-b_k\le s\mid N=k\bigr)=e^{-e^{-s}}.
\]

The extra \((\ell-1)\log\log k\) correction is absent with a single exponential reset stage.

## Assumptions and scope

Let \(x>0,D>0,r>0,v\in\mathbb R\), and let \(\ell\ge2\) be an integer. Each excursion is governed until its next reset or absorption by

\[
dX_t=v\,dt+\sqrt{2D}\,dW_t,
\]

starting at \(x\). Reset intervals are independent and identically distributed Erlang(\(\ell,r\)) random variables independent of Brownian motion. At each reset the position returns instantaneously to \(x\), with a completely new clock and Brownian motion; the process stops upon its first encounter with the absorbing endpoint \(0\). Let \(N\in\{0,1,\ldots\}\) be the number of completed resets before absorption and \(M=\sup_{0\le t\le\tau}X_t\). Set

\[
\omega=\sqrt{v^2+4Dr},\quad\alpha=\frac{\omega-v}{2D},\quad
\beta=\frac{\omega+v}{2D},\quad\kappa=\frac\omega D=\alpha+\beta,\quad
C=e^{\alpha x}-e^{-\beta x}.
\]

All these quantities are finite and \(\alpha,\beta,\kappa,C\) are strictly positive. Here \(\tau\) denotes total absorption time and exists almost surely. The quantities \(p,q\), defined below, belong to \((0,1)\).

## Proof

**1. Killed-excursion Laplace transforms.** For a barrier \(m>x\), let \(\tau_0,\tau_m\) be the two free-diffusion hitting times. Solving the backward boundary-value equation \(D f''+vf'=rf\) on \((0,m)\), with endpoint values \((1,0)\) or \((0,1)\), gives

\[
F_0(r,m)=\mathbb E_x[e^{-r\tau_0};\tau_0<\tau_m]
=\frac{e^{-\beta x}-e^{-\kappa m}e^{\alpha x}}{1-e^{-\kappa m}},
\]
\[
F_m(r,m)=\mathbb E_x[e^{-r\tau_m};\tau_m<\tau_0]
=\frac{e^{\alpha x}-e^{-\beta x}}{e^{\alpha m}-e^{-\beta m}}.
\]

On the half-line, \(F_0(r,\infty)=\phi(r)=e^{-\beta x}\). These formulas also follow directly by solving a two-by-two linear system for the exponential eigenfunctions.

**2. Erlang survival transform and exact joint law.** An Erlang waiting time \(R\) has survival function

\[
\Pr(R>t)=e^{-rt}\sum_{j=0}^{\ell-1}\frac{(rt)^j}{j!}.
\]

For any exit event with Laplace transform \(F(r)=\mathbb E[e^{-rT};\mathrm{exit\ event}]\), define

\[
\mathcal T_{\ell,r}F=\sum_{j=0}^{\ell-1}\frac{(-r)^j}{j!}\,\partial_r^jF.
\]

Differentiation under the Laplace transform identifies \(\mathcal T_{\ell,r}F=\Pr(T<R,\mathrm{exit\ event})\); there is no appeal to memorylessness of the Erlang duration. Put

\[
p=\mathcal T_{\ell,r}\phi,\quad q=1-p,\quad
p_m=\mathcal T_{\ell,r}F_0(r,m),\quad
q_m=1-\mathcal T_{\ell,r}[F_0(r,m)+F_m(r,m)].
\]

Then \(p_m\) is the chance of hitting zero before either the next reset or the barrier, and \(q_m\) is the chance of resetting before either boundary. Renewal independence of consecutive excursions yields, for every integer \(k\ge0\),

\[
\boxed{\Pr(M<m,N=k)=p_m q_m^k.}
\]

Removing the upper boundary gives \(\Pr(N=k)=p q^k\), and summation yields \(\Pr(M<m)=p_m/(1-q_m)\). Because \(p>0\), the number of resets is finite almost surely.

**3. Exact tail-difference identities.** Elementary simplification of the two exit transforms gives

\[
\phi-F_0=\frac{C e^{-\kappa m}}{1-e^{-\kappa m}},\qquad
F_0+F_m-\phi=\frac{C(e^{-\alpha m}-e^{-\kappa m})}{1-e^{-\kappa m}}.
\]

Therefore

\[
p-p_m=\mathcal T_{\ell,r}\!\left(\frac{C e^{-\kappa m}}{1-e^{-\kappa m}}\right),\qquad
q-q_m=\mathcal T_{\ell,r}\!\left(\frac{C(e^{-\alpha m}-e^{-\kappa m})}{1-e^{-\kappa m}}\right).
\]

For fixed parameters, differentiation of \(e^{-m f(r)}\) exactly \(j\) times has highest power \((-mf'(r))^j e^{-mf(r)}\) and smaller powers of \(m\). As \(\alpha'(r)=1/\omega\) and \(\kappa'(r)=2/\omega\), the \(j=\ell-1\) term dominates, yielding the **two distinct sharp scales**

\[
p-p_m\sim K_0 m^{\ell-1}e^{-\kappa m},\qquad
q-q_m\sim K m^{\ell-1}e^{-\alpha m}.
\]

Terms containing \(e^{-\kappa m}\) are exponentially smaller than the \(\alpha\) term in the second expression; derivative remainders are smaller by powers of \(m\). No finite truncated series is used as an infinite proof.

**4. Fixed-count tails and extreme-event count distribution.** From the exact law,

\[
\Pr(M>m,N=k)=p q^k-p_m q_m^k.
\]

For \(k=0\) it equals \(p-p_m\). For fixed \(k\ge1\) its leading contribution is \(kpq^{k-1}(q-q_m)\), since \(\kappa>\alpha\). Division by \(pq^k\) gives the stated conditional tails. Summing over all reset counts first gives \(\Pr(M>m)=1-p_m/(1-q_m)\sim(q-q_m)/p\). Dividing the fixed-\(k\) joint tail by this unconditional tail yields \(p^2 kq^{k-1}\). Its sum over positive integers equals \(p^2/(1-q)^2=1\), hence no probability mass escapes to diverging counts.

**5. High-count Gumbel law.** For \(k\to\infty\), define \(m_k(s)=(b_k+s)/\alpha\), which tends to infinity. Substitution into the sharp tail formula gives

\[
\frac{k(q-q_{m_k(s)})}{q}\longrightarrow e^{-s}.
\]

The precise conditional distribution is

\[
\Pr(M<m_k(s)\mid N=k)=\frac{p_{m_k(s)}}p\left(\frac{q_{m_k(s)}}q\right)^k.
\]

The first factor tends to one, while the second tends to \(e^{-e^{-s}}\) because \(k[(q-q_m)/q]^2\to0\). Continuity of the spatial maximum distribution removes any ambiguity between strict and weak inequalities.

## Verification

The included file `verify_extreme.py` independently reconstructs both absorbing-boundary exit probabilities through the killed Brownian transition-kernel sine series (80,000 modes), for nine distinct parameter combinations including positive and negative drift and clock orders one, two, and three. Each compared exit probability agrees with the derivative formulas within \(2\times10^{-5}\). It also directly compares large-barrier exact differences to both predicted sharp constants and evaluates Gumbel centering against the limiting cumulative distribution, with high-precision arithmetic and a very large conditional count. Run `python verify_extreme.py` with Python 3, NumPy, SciPy, and mpmath. These numerical tests support, but do not replace, the analytic argument.

## Relationship to prior work

Guo, Yan, and Chen (arXiv:2311.14714, first public November 17, 2023) derive drifted Brownian first-passage maximum statistics for **exponential (Poisson) resetting**, including an unconditioned spatial maximum and its attainment time. Their preceding arXiv:2306.15929 covers the drift-free Poisson case. Singh and Pal (arXiv:2102.07111) study extremes of resetting trajectories observed for a **fixed time**, likewise with constant-rate resets. The exact stopped-excursion renewal law is built from standard killed-diffusion transforms; neither these transforms nor classical Gumbel convergence is claimed as novel. The contribution asserted here is their joint consequence for **multi-stage Erlang clocks before absorption**, including the finite-versus-positive reset-count exponent separation, size-biased limiting count, and nonzero order-specific \(\log\log k\) centering. Related generalized-resetting literature treats first-passage times, but may contain an equivalent rare-excursion argument not identified in the inspected sources.

## Limitations

The result requires independent fresh renewal clocks, identical reset locations, integer Erlang shape, one-dimensional constant-coefficient drift and diffusion, and absorption at a single target. The high-count theorem concerns an increasingly rare conditional event, not ordinary unconditioned large-time Gumbel behavior. The \(\ell=1\) Poisson comparison follows by the same formulas but is not put forward as new. The result does not establish analogous constants for noninteger Gamma renewal clocks, state-dependent clocks, or moving targets. No claim of complete literature uniqueness or independent validation is made.

## References

1. W. Guo, H. Yan, H. Chen, *Extremal statistics for first-passage trajectories of drifted Brownian motion under stochastic resetting*, arXiv:2311.14714 (first made public 2023-11-17), J. Stat. Mech. (2024) 013203. https://arxiv.org/abs/2311.14714
2. W. Guo, H. Yan, H. Chen, *Extremal statistics for a resetting Brownian motion before its first-passage time*, arXiv:2306.15929 (2023), Phys. Rev. E 108, 044115. https://arxiv.org/abs/2306.15929
3. P. Singh, A. Pal, *Extremal statistics for stochastic resetting systems*, arXiv:2102.07111 (2021), Phys. Rev. E 103, 052119. https://arxiv.org/abs/2102.07111
4. S. Linn, S. D. Lawley, *First-passage times under frequent stochastic resetting*, Phys. Rev. E 108, 024114 (2023). https://doi.org/10.1103/PhysRevE.108.024114
