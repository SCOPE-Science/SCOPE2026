# A sharp collective-fluctuation crossover under Bernoulli-thinned common resetting

## Finding
Let \(N\ge1\) independent one-dimensional Brownian particles have generator \(D\partial_x^2\), with \(D>0\). At the epochs of an independent common rate-\(r\) Poisson clock (\(r>0\)), each particle is independently returned to the origin with probability \(q_N\in(0,1]\); the decisions are independent over particles and epochs. Consider the unique stationary regime and its dimensionless mean-square radius
\[
T_N=\frac{rq_N}{2DN}\sum_{i=1}^N X_i^2.
\]

**Exact finite-system result.** For all \(N\ge1\),
\[
\mathbb E T_N=1,\qquad
\operatorname{Var}(T_N)=\frac5N+\left(1-\frac1N\right)\frac{q_N}{2-q_N}.
\]
For distinct particles the stationary squared-position correlation coefficient is
\[
\operatorname{Corr}(X_i^2,X_j^2)=\frac{q_N}{5(2-q_N)}.
\]

**Fixed-fraction limit.** If \(q_N\to q\in(0,1]\), then
\[
T_N\Longrightarrow V_q=\sum_{k=1}^{\infty}q(1-q)^{k-1}E_k,
\quad E_k\overset{\mathrm{iid}}\sim\operatorname{Exp}(1),
\]
with independent \(E_k\), and
\[
\mathbb E e^{-sV_q}=\prod_{j=0}^{\infty}\frac1{1+sq(1-q)^j},\quad s\ge0;
\qquad \operatorname{Var}(V_q)=\frac q{2-q}>0.
\]
Here \(V_1\) is exponential of mean one. Thus the stationary mean-square radius does not self-average at fixed positive participation probability.

**Vanishing-fraction normal crossover.** If \(q_N\to0\) as \(N\to\infty\), then, without further restrictions on \(Nq_N\),
\[
\frac{T_N-1}{\sqrt{5/N+(1-1/N)q_N/(2-q_N)}}
\Longrightarrow\mathcal N(0,1).
\]
In particular, if \(Nq_N\to c\in[0,\infty)\), then
\[
\sqrt N(T_N-1)\Longrightarrow\mathcal N(0,5+c/2),
\]
while if \(Nq_N\to\infty\) and \(q_N\to0\), then
\[
\sqrt{2/q_N}(T_N-1)\Longrightarrow\mathcal N(0,1).
\]
The collective and individual fluctuation contributions exchange dominance at the natural scale \(Nq_N\asymp1\).

## Assumptions and scope
The Brownian noises are independent and independent of the Poisson clock and all Bernoulli reset marks. There is **one** shared Poisson clock of rate \(r\), not a separate clock for each particle. Each common event resets a *random Bernoulli subset* of the particles; the subset size has binomial distribution and is **not fixed**. The origin is the common reset position. The stationary law is unique for each finite \(N\) and \(q_N>0\), since every coordinate is reset infinitely often and coupled paths driven by the same randomness forget their finite initial positions almost surely.

## Proof
**1. Exact stationary construction.** Enumerate the common Poisson event ages before observation as \(S_j=R_1+\cdots+R_j\), where the independent backward inter-arrival times \(R_k\) are exponential of rate \(r\). Conditional on this shared sequence, the most recent event marking particle \(i\) has index \(J_i\) with \(\Pr(J_i=j)=q(1-q)^{j-1}\), independently across particles. Here \(q=q_N\). Independently let \(Z_i\) be standard Gaussian. The stationary position is distributed as
\[
X_i=\sqrt{2DS_{J_i}}\,Z_i.
\]
In particular, conditional on the full event-age sequence, all particle positions are iid Gaussian-variance mixtures. The marked Poisson process of an individual coordinate has rate \(rq\), so \(S_{J_i}\sim\operatorname{Exp}(rq)\) marginally; its Gaussian factor is independent.

**2. Exact finite-size variance.** Put \(Y_i=rqX_i^2/(2D)=rqS_{J_i}Z_i^2\). Since an exponential mean-one random variable multiplied by an independent \(Z_i^2\) has mean one and second moment six,
\[
\mathbb EY_i=1,\qquad \operatorname{Var}(Y_i)=5.
\]
Conditional on the event ages,
\[
\mathbb E[Y_i\mid(S_j)]
=rq\sum_{j\ge1}q(1-q)^{j-1}S_j
=q\sum_{k\ge1}(1-q)^{k-1}E_k=:V_q,
\quad E_k=rR_k.
\]
The last equality follows by exchanging two nonnegative sums. The independent mean-one exponentials give
\[
\operatorname{Var}(V_q)=q^2\sum_{k\ge1}(1-q)^{2(k-1)}=\frac{q}{2-q}=:v_q.
\]
For distinct particles, conditional independence yields \(\operatorname{Cov}(Y_i,Y_j)=v_q\). Consequently the variance of \(N^{-1}\sum_iY_i\) is \(5/N+(1-1/N)v_q\), and the squared-position correlation coefficient is \(v_q/5\). These equations are exact, including the endpoints \(N=1\) and \(q=1\).

**3. Fixed positive participation.** By conditional independence and subsequent averaging over the shared ages, \(\mathbb E[(T_N-V_{q_N})^2]=N^{-1}\mathbb E[\operatorname{Var}(Y_1\mid(S_j))]=(5-v_{q_N})/N\). Therefore \(T_N-V_{q_N}\to0\) in \(L^2\). The series for \(V_q\) converges in \(L^2\), and its weights vary continuously in \(q\) near any fixed \(q>0\) (including \(q=1\)); hence \(V_{q_N}\to V_q\) in \(L^2\) under a common exponential coupling. Independence of the summands yields the displayed convergent product for its Laplace transform, with the \(q=1\) case obtained by retaining the first summand.

**4. Vanishing participation: thermal component.** For an integer \(a\ge1\) write
\[
H_{a,q}=(rq)^a\sum_{j\ge1}q(1-q)^{j-1}S_j^a
=\mathbb E[(rqS_J)^a\mid(S_j)].
\]
Almost surely, the strong law gives \(rS_j/j\to1\). The geometric Riemann sum satisfies
\[
q\sum_{j\ge1}(1-q)^{j-1}(qj)^a\longrightarrow a!.
\]
Splitting off a finite initial segment and bounding the tail by \((1\pm\epsilon)^a(qj)^a\) proves \(H_{a,q}\to a!\) almost surely as \(q\downarrow0\), for \(a=1,2,4\). The bound also shows that these conditional moments remain bounded along any sequence \(q\downarrow0\) for almost every environment. Therefore, since \(\mathbb E Z^{2a}=(2a-1)!!\),
\[
\operatorname{Var}(Y_i\mid(S_j))=3H_{2,q}-H_{1,q}^2\longrightarrow5,
\]
with bounded conditional fourth centered moments. Applying the conditional triangular-array Lyapunov theorem to the independent row \(Y_1,\ldots,Y_N\), with \(q=q_N\downarrow0\), gives
\[
\sqrt N(T_N-V_{q_N})\Longrightarrow\mathcal N(0,5)
\]
conditionally for almost every shared environment. Its conditional characteristic function tends to the deterministic Gaussian characteristic function.

**5. Vanishing participation: environmental component and synthesis.** Write
\[
V_q-1=\sum_{k\ge1}q(1-q)^{k-1}(E_k-1).
\]
Its variance is \(v_q=q/(2-q)\); the maximal coefficient divided by \(\sqrt{v_q}\) is \(\sqrt{q(2-q)}\to0\). Truncation followed by the Lindeberg theorem proves
\[
(V_q-1)/\sqrt{v_q}\Longrightarrow\mathcal N(0,1).
\]
Because the thermal component has a conditional characteristic function tending almost surely to a nonrandom limit, it is jointly asymptotically independent of the environmental component. Their deterministic variance weights in \(T_N-1=(T_N-V_q)+(V_q-1)\) are \(5/N\) and \(v_q\) to first order. On every subsequence one can take a further subsequence on which the normalized weights converge; each such limit is a sum of independent centered Gaussians whose total variance is one. The asserted unified standardized limit follows. If \(Nq_N\to c\), then \(Nv_{q_N}\to c/2\); if \(Nq_N\to\infty\), then \(5/(Nv_{q_N})\to0\). These establish the two displayed regimes. The exact finite-size variance differs from \(5/N+v_{q_N}\) by \(v_{q_N}/N\), negligible in this final normalization.

## Verification
A standalone Python 3 program, `verify.py`, checks stationary one-particle second/fourth generator equations and two-particle mixed-moment equations with exact rational arithmetic; it also checks the corresponding pair characteristic-function equation, finite-size variance identities, perpetuity cumulants, and the geometric-weight identity. A seeded Monte Carlo sample checks the mean and variance of the exponential perpetuity. Executing `python verify.py` returned `PASS 99 exact and numerical checks; Monte Carlo mean=1.0020, variance=0.1457`. These finite computations corroborate, but do not replace, the proof of the infinite-population and vanishing-participation limits.

## Relationship to prior work
Evans and Majumdar (arXiv:1102.2704) establish the one-particle Poisson-reset stationary diffusion paradigm. Vilk, Assaf, and Meerson (arXiv:2205.10273) analyze independent per-particle resetting and a separate farthest-particle reset rule. Biroli, Larralde, Majumdar, and Schehr (arXiv:2211.00563), and de Mauro, Biroli, Majumdar, and Schehr (arXiv:2509.06658), analyze *complete simultaneous* resets and their induced correlations; the latter paper explicitly raises partial-subset resets as a further question (conclusion, p. 28). Bressloff (arXiv:2401.03501, p. 4) distinguishes local independent resets from global all-particle resets. Neither endpoint is the Bernoulli-thinned *common-clock* rule with \(0<q<1\) considered here. The present theorem gives its stationary squared-radius law and sharp \(Nq\) fluctuation crossover. It does not solve the distinct variant that resets an **exactly prescribed number** of particles at each event. Any broader general theory implying the displayed formulas would affect historical priority; no exhaustive novelty certification is claimed.

## Limitations
The model assumes noninteracting Brownian diffusion in one dimension, homogeneous shared Poisson-event times, independent Bernoulli inclusion marks, identical diffusivities, a common zero reset site, and stationary sampling. The theorem does not classify time-dependent fluctuations, interacting particles, non-Poisson common clocks, a fixed-size randomly selected reset subset, or extreme-value statistics. At \(q=1\) the limiting exponential law is consistent with the known fully simultaneous reset model and is not itself claimed to be new. Numerical simulations do not establish any infinite-system limit.

## References
1. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704 (first public version 2011-02-14), https://arxiv.org/abs/1102.2704.
2. O. Vilk, M. Assaf, and B. Meerson, *Fluctuations and first-passage properties of systems of Brownian particles with reset*, arXiv:2205.10273 (2022), https://arxiv.org/abs/2205.10273.
3. M. Biroli, H. Larralde, S. N. Majumdar, and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563 (2022), https://arxiv.org/abs/2211.00563.
4. P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization*, arXiv:2401.03501 (2024), https://arxiv.org/abs/2401.03501.
5. G. de Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (2025), https://arxiv.org/abs/2509.06658.
