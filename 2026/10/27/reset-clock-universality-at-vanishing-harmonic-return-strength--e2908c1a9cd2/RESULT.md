# Reset-clock universality at vanishing harmonic-return strength

## Finding
Fix a diffusion coefficient \(D>0\) and target position \(L>0\). A particle repeatedly searches from the origin as a free Brownian motion and, if its independent search clock rings before it finds the target, returns stochastically under a harmonic restoring force. Crucially, the target remains absorbing during return. For **every** independent identically distributed reset-clock law with \(0<\mathbb E R<\infty\), the total target-hitting time \(T_k\), for return stiffness \(k>0\), obeys

\[
\boxed{\lim_{k\downarrow0}\sqrt{k}\,\mathbb E[T_k]
=L\sqrt{\frac{\pi}{2D}}.}
\]

The limit is independent of the entire reset-clock distribution, including its mean. It applies to exponential, deterministic, Erlang, and other integrable clocks. At exactly \(k=0\), the mean target-hitting time is infinite. The critical inverse-square-root divergence is therefore singular, not a small regular correction to instantaneous restarting.

## Assumptions and scope
Let \(B_t=\sqrt{2D}\,W_t\) start at zero, and define the positive-target search hitting time \(\tau_L=\inf\{t\ge0:B_t=L\}\). At the beginning of each independent cycle, sample a nonnegative clock \(R\), independent of the Brownian path, with \(0<\mathbb E R<\infty\). The clock may have atoms, including an atom at zero; it is independent and resampled afresh in every new search cycle. If \(\tau_L\le R\), absorption completes the cycle. If \(R<\tau_L\), search stops at \(X=B_R<L\), and a fresh independent Brownian noise drives a return diffusion

\[
dY_t=-kY_t\,dt+\sqrt{2D}\,dW'_t,\qquad Y_0=X.
\]

Return ends at the first hit of \(0\) or \(L\). Reaching \(L\) absorbs the particle, while reaching \(0\) starts the next independent search cycle. If \(X\le0\), the return must hit \(0\) first. No additional reset clock acts during the return. Define \(T_k\) as the full physical elapsed time, including both search and return durations. These rules specify a renewal process and permit absorption during either phase.

The parameter \(k\) has units of inverse time; the normalization \(\sqrt{k}\,\mathbb E T_k\) has units of square-root time, consistent with \(L/\sqrt D\). The singular limit varies \(k\) while holding \(D,L\), and the complete clock law fixed.

## Proof
**1. Renewal reduction.** Put \(\sigma=R\wedge\tau_L\). Let \(q_s=\Pr(\tau_L\le R)\). For a return starting at \(x<L\), write \(h_k(x)=\Pr_x(\tau_L^{\rm ret}<\tau_0^{\rm ret})\) and \(m_k(x)=\mathbb E_x[\tau_0^{\rm ret}\wedge\tau_L^{\rm ret}]\). If \(x\le0\), set \(h_k(x)=0\) and interpret \(m_k(x)\) as the mean first time the return reaches zero. Renewal conditioning gives the exact identity

\[
\mathbb E T_k=
\frac{\mathbb E\sigma+\mathbb E[m_k(B_R)\,;\,R<\tau_L]}
{q_s+\mathbb E[h_k(B_R)\,;\,R<\tau_L]}.
\tag{1}
\]

The denominator is strictly positive because \(q_s>0\) under the hypotheses. All numerator expectations are finite for each fixed \(k>0\), as shown below, so this identity also establishes finite mean absorption for positive stiffness.

**2. Return-side splitting and mean durations.** The backward generator is \(D\partial_x^2-kx\partial_x\). Its splitting probability solves \(Dh''-kxh'=0\), with boundary values \(h(0)=0\) and \(h(L)=1\). Thus

\[
h_k(x)=\begin{cases}
0,&x\le0,\\
\displaystyle\frac{\int_0^x\exp(ku^2/(2D))\,du}{\int_0^L\exp(ku^2/(2D))\,du},&0<x<L.
\end{cases}
\tag{2}
\]

In particular \(h_k(x)\to x/L\) for \(0<x<L\). On the negative side, put \(a=-x>0\). Solving the OU mean-hitting-time equation with \(m_k(0)=0\), and choosing the solution whose derivative does not grow as \(\exp(ka^2/(2D))\) at infinity, yields

\[
m_k(-a)=\sqrt{\frac{\pi}{2Dk}}\int_0^a
\operatorname{erfcx}\!\left(\sqrt{\frac{k}{2D}}\,u\right)du,
\quad \operatorname{erfcx}(z)=e^{z^2}\operatorname{erfc}(z).
\tag{3}
\]

For \(z\ge0\), the integral representation of \(\operatorname{erfcx}\) implies \(0<\operatorname{erfcx}(z)\le1\). Consequently, for every fixed \(a\ge0\),

\[
\sqrt{k}\,m_k(-a)\longrightarrow a\sqrt{\frac{\pi}{2D}},
\qquad 0\le\sqrt{k}\,m_k(-a)\le a\sqrt{\frac{\pi}{2D}}.
\tag{4}
\]

For \(0\le x\le L\), the mean return time solves \(Dm_k''-kxm_k'=-1\) with both endpoint values zero. Its Green-kernel representation is continuous jointly in \((k,x)\) on \([0,k_0]\times[0,L]\), for every finite \(k_0\). Hence these positive-side means are uniformly bounded as \(k\downarrow0\).

**3. Dominated limits.** By independence and \(\mathbb E R<\infty\),

\[
\mathbb E[\lvert B_R\rvert\,;\,R<\tau_L]
\le\mathbb E\lvert B_R\rvert
\le\sqrt{2D\,\mathbb E R}<\infty.
\]

Define the positive and finite negative-excursion weight

\[
A=\mathbb E[(-B_R)_+\,;\,R<\tau_L]>0.
\tag{5}
\]

Strict positivity follows because on any positive-duration search there is a positive chance to lie below zero without touching \(L\). Equations (2)–(4), dominated convergence, uniform boundedness on \([0,L]\), and \(\mathbb E\sigma\le\mathbb E R\) give

\[
\sqrt{k}\,\mathbb E[m_k(B_R);R<\tau_L]
\longrightarrow \sqrt{\frac{\pi}{2D}}A,
\qquad
q_s+\mathbb E[h_k(B_R);R<\tau_L]
\longrightarrow q_0,
\]

where \(q_0=q_s+L^{-1}\mathbb E[(B_R)_+;R<\tau_L]\).

**4. Conservation at the search stopping time.** The stopped Brownian martingale \(B_{t\wedge\sigma}\) is uniformly integrable: the stopped second moment is bounded by \(2D\mathbb E\sigma\), using Itô isometry and \(\mathbb E\sigma<\infty\). Optional stopping therefore implies

\[
0=\mathbb E[B_\sigma]
=Lq_s+\mathbb E[B_R;R<\tau_L].
\]

Splitting the last term into positive and negative contributions gives the **exact cancellation**

\[
A=Lq_s+\mathbb E[(B_R)_+;R<\tau_L]=Lq_0.
\tag{6}
\]

Substitute the two limits and (6) into (1):

\[
\lim_{k\downarrow0}\sqrt{k}\,\mathbb E T_k
=\frac{\sqrt{\pi/(2D)}A}{q_0}
=L\sqrt{\frac{\pi}{2D}}.
\]

Finally, when \(k=0\), a Brownian motion started at any negative point has infinite mean first-passage time to zero. Since the event of negative reset has positive probability, the total mean absorption time at \(k=0\) is infinite. This completes the proof.

## Verification
The standalone script `verify_weak_return.py` evaluates the independent killed-Brownian reset-position density and the OU boundary-value problem, then compares finite-stiffness means with the proven limit. Its five reset laws are exponential clocks with three distinct rates and deterministic clocks with two distinct durations. For all twenty combinations of clock and stiffness it checks the exact optional-stopping cancellation numerically; it also verifies monotone approach of the scaled means, positive-side boundary conditions, and an independent closed expression for the exponential-clock success probability. Executing `python verify_weak_return.py` with Python, NumPy and SciPy produced **59 passing deterministic assertions**. Numerical agreement corroborates but does not replace the proof.

## Relationship to prior work
Dubey and Pal (2026), arXiv:2610.18814v1, derive general stochastic-return renewal equations (their equations (5)–(8)) and analyze a switching harmonic trap at exponential reset times. The free-search/OU-return model is a specialization of their physical setting. Frydel (2025), arXiv:2511.14646v1, analyzes the target-visible return protocol (SR-B), including its exact mean renewal formula (equations (46)–(47)) and the return splitting probability (equation (48)). These foundational equations and the splitting ODE are **not** claimed as new. Biswas, Kundu, and Pal (2024), and Biswas, Dubey, Kundu, and Pal (2025), develop the broader stochastic-return search framework.

The contribution asserted here is the joint weak-return-stiffness asymptotic, its **exact clock-law-independent leading amplitude across all integrable iid renewal reset laws**, and the martingale cancellation proving that universality. The examined works provide building blocks but do not explicitly give this invariant coefficient with this clock-law quantifier. Generic stopped-martingale and one-dimensional OU hitting-time facts are likewise standard; the model-specific cancellation is the substantive content.

## Limitations
Only the mean completion time is classified, not the complete distribution, next asymptotic order, or uniform behavior if the clock law varies with \(k\). The proof requires an independent clock of finite positive mean; heavy-tailed clocks of infinite mean are outside scope. Resetting is disabled during return, search has zero drift, the return potential is harmonic, and the target is visible during return. The same coefficient is not asserted for search drift, spatially dependent diffusion, nonlinear return forces, or blind returns. The leading-order universality may be implicit in more general first-passage or renewal theorems not identified by the literature comparison; independent priority assessment remains necessary.

## References
1. A. Dubey and A. Pal, “Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols,” arXiv:2610.18814v1 (first public 2026-10-13), https://arxiv.org/html/2610.18814v1 .
2. D. Frydel, “Search by Return: Stochastic Resetting in Fluctuating Harmonic Potentials,” arXiv:2511.14646v1 (2025), https://arxiv.org/html/2511.14646v1 .
3. A. Biswas, A. Kundu, and A. Pal, “Search with stochastic home returns can expedite classical first passage under resetting,” Physical Review E **110**, L042101 (2024).
4. A. Biswas, A. Dubey, A. Kundu, and A. Pal, “Drift-diffusive resetting search process with stochastic returns: speedup beyond optimal instantaneous return,” Physical Review E **111**, 014142 (2025).
