# A log-log extinction delay and a near-resonant Gumbel crossover in a directed epidemic

## Finding
Consider a continuous-time infection process on the directed complete bipartite network with \(m_n\) sources and \(n\) receivers. Sources initially are all infected and independently recover permanently at rate one; receivers initially are all susceptible, recover from infection at rate \(\mu_n\), and can be reinfected. Every infected source infects each susceptible receiver independently at rate \(\lambda/m_n\); no receiver infects any vertex, and sources cannot be reinfected. Let \(T_n\) be the first time at which no infected vertices remain. Fix \(\lambda>0\), \(\rho\in(0,\infty)\), and \(\theta\in\mathbb R\), and assume \(m_n/n\to\rho\) and
\[
\mu_n=1+\frac{\theta}{\log n}>0.
\]
Then, for every real \(x\),
\[
\lim_{n\to\infty}\Pr\{T_n\le\log n+\log\log n+x\}
=\exp\left[-\lambda\Phi(\theta)e^{-x}\right],\qquad
\Phi(\theta)=\begin{cases}(1-e^{-\theta})/\theta,&\theta\ne0,\\1,&\theta=0.\end{cases}
\]
Equivalently, \(T_n-\log n-\log\log n-\log(\lambda\Phi(\theta))\) converges in distribution to the standard Gumbel law. At the same observation times, the infected-receiver count converges to a Poisson random variable of mean \(\lambda\Phi(\theta)e^{-x}\), while the infected-source count converges in probability to zero. The limit is independent of \(\rho\) (provided its limit is positive and finite). The extra \(\log\log n\) delay is caused by the near-coincidence of source and receiver recovery rates; \(\Phi\) supplies the complete fixed-\(\theta\) crossover on the detuning scale \(1/\log n\).

## Assumptions and scope
For every sufficiently large integer \(n\), \(m_n\) is a positive integer; every initially infected source has a lifetime distributed as an independent rate-one exponential variable. Conditional on the sources' history, each receiver is an independent, time-inhomogeneous two-state Markov process with susceptible-to-infected intensity \(h_n(t)=\lambda A_n(t)/m_n\) and infected-to-susceptible intensity \(\mu_n\), where \(A_n(t)\) counts still-infected sources. All clocks are independent except for the common source history that modulates receiver infection rates. Once the process reaches zero infected vertices, it is absorbing. The theorem concerns fixed positive \(\lambda\), fixed real \(\theta\), and asymptotic \(n\to\infty\) with \(0<\rho<\infty\). It does not assert uniformity for unbounded \(\theta\) or for \(\rho\) approaching zero or infinity.

## Proof
**Conditional reduction.** Let \(L_1,\dots,L_{m_n}\) be independent \(\operatorname{Exp}(1)\) source lifetimes and \(A_n(t)=\sum_i\mathbf1_{\{L_i>t\}}\). Given all lifetimes, receiver states are independent with common infection probability \(q_n(t)\), satisfying
\[
q_n'(t)=h_n(t)(1-q_n(t))-\mu_nq_n(t),\qquad q_n(0)=0.
\]
Consequently,
\[
q_n(t)=\int_0^t h_n(s)e^{-\mu_n(t-s)}
\exp\left[-\int_s^t h_n(u)\,du\right]ds.
\]
Let \(q_{0,n}(t)=\int_0^t h_n(s)e^{-\mu_n(t-s)}ds\), the linearization obtained by omitting susceptible depletion. Since \(1-e^{-y}\le y\) for \(y\ge0\),
\[
0\le q_{0,n}(t)-q_n(t)\le\int_0^t\int_s^t h_n(s)h_n(u)e^{-\mu_n(t-s)}\,du\,ds.\tag{1}
\]

**Source fluctuations.** For \(t\ge0\), write \(W_i(t)=\int_0^{L_i\wedge t}e^{\mu_n s}ds\). Then
\[
q_{0,n}(t)=\frac{\lambda e^{-\mu_n t}}{m_n}\sum_{i=1}^{m_n}W_i(t),\quad
\mathbb EW_i(t)=\int_0^t e^{(\mu_n-1)s}ds.
\]
Fix \(x\in\mathbb R\) and set \(t_n=\log n+\log\log n+x\). For all sufficiently large \(n\), \(\mu_n\) belongs to a fixed compact subset of \((1/2,3/2)\). Using
\[
\mathbb E e^{2\mu_n(L_i\wedge t)}
=1+2\mu_n\int_0^t e^{(2\mu_n-1)s}ds,
\]
one obtains \(\mathbb EW_i(t_n)^2\le C_\theta e^{(2\mu_n-1)t_n}\). Independence gives
\[
\operatorname{Var}[nq_{0,n}(t_n)]
\le C_{\lambda,\theta}\frac{n^2e^{-t_n}}{m_n}
=O\big((\log n)^{-1}\big).\tag{2}
\]
The expectation is explicit:
\[
\mathbb E[nq_{0,n}(t_n)]
=\lambda n e^{-\mu_nt_n}\int_0^{t_n}e^{(\mu_n-1)s}ds
\longrightarrow\lambda e^{-x}\Phi(\theta).\tag{3}
\]
For \(\theta=0\), interpret the integral as \(t_n\). For nonzero fixed \(\theta\), substitute \(\mu_n-1=\theta/\log n\) and \(t_n/\log n\to1\). Equations (2)–(3) show convergence of \(nq_{0,n}(t_n)\) in probability to the displayed constant.

**Control of receiver reinfections and exclusion.** For \(0\le s\le u\), independence of source lifetimes yields
\[
\mathbb E[h_n(s)h_n(u)]
=\lambda^2\left[(1-m_n^{-1})e^{-(s+u)}+m_n^{-1}e^{-u}\right].
\]
Taking expectations in (1) and integrating first in \(u\) gives
\[
\mathbb E\left[e^{\mu_nt}(q_{0,n}(t)-q_n(t))\right]
\le\lambda^2\int_0^t e^{\mu_ns}\left[(1-m_n^{-1})e^{-s}(e^{-s}-e^{-t})
+m_n^{-1}(e^{-s}-e^{-t})\right]ds.
\]
At \(t=t_n\), the integral is bounded by \(C_{\lambda,\theta}(1+t_n/m_n)\): the first term is bounded using \(\mu_n<3/2\), and the second using \(\int_0^{t_n}e^{(\mu_n-1)s}ds=O_\theta(t_n)\). Thus
\[
\mathbb E[n(q_{0,n}(t_n)-q_n(t_n))]
\le C_{\lambda,\theta}ne^{-\mu_nt_n}(1+t_n/m_n)
=O((\log n)^{-1}).\tag{4}
\]
By (2)–(4) and Markov's inequality,
\[
nq_n(t_n)\xrightarrow{\mathbb P}\lambda e^{-x}\Phi(\theta).\tag{5}
\]

**Poisson law and absorption.** Conditional on the source lifetimes, the number \(B_n(t_n)\) of infected receivers has law \(\operatorname{Binomial}(n,q_n(t_n))\). Formula (5), together with \(nq_n(t_n)^2\to0\) in probability, implies its probability generating function converges to \(\exp[\lambda\Phi(\theta)e^{-x}(z-1)]\) for every \(0\le z\le1\); bounded convergence establishes the unconditional Poisson limit. Also,
\[
\Pr\{A_n(t_n)>0\}\le m_n e^{-t_n}=O((\log n)^{-1}).
\]
As the all-susceptible state is absorbing, \(\{T_n\le t_n\}=\{A_n(t_n)=0,\ B_n(t_n)=0\}\). Their probabilities differ from \(\Pr\{B_n(t_n)=0\}\) by at most \(m_ne^{-t_n}\). The Poisson zero-atom therefore yields the stated Gumbel distribution. This completes the proof.

## Verification
A standalone finite-state checker, `verify.py`, constructs the exact generator on \(\{0,\dots,m\}\times\{0,\dots,n\}\), with transitions \((a,b)\to(a-1,b)\) at rate \(a\), \((a,b)\to(a,b-1)\) at rate \(\mu b\), and \((a,b)\to(a,b+1)\) at rate \(\lambda a(n-b)/m\). It calculates transient probabilities by an independent matrix exponential, checks the exact source-survival identity, and verifies the upper bound \(0\le n\mathbb Eq_{0,n}-\mathbb EB_n\le n\mathbb E(q_{0,n}-q_n)\) using deterministic quadrature. Across several part sizes, observation times, and rates it passed 144 finite-generator test cases. The script additionally samples actual source lifetimes and solves the conditional receiver equation exactly between recovery jumps, comparing finite-size extinction probabilities with the three predicted crossover constants. These numerical checks are finite experiments and are not used as an infinite-system proof; the preceding bounds supply that proof.

## Relationship to prior work
Heinzmann (J. Appl. Probab. 46, 296–307, 2009) proves multitype branching extinction-time approximations assuming an irreducible linearized offspring matrix with a simple dominant eigenvalue (Theorem 2.1 and the subsequent subcritical estimates). Its full article, including that hypothesis, was inspected. This condition is inapplicable to the present one-way process, whose two decay rates coincide at resonance and whose source-to-receiver transmission matrix is reducible. Heinzmann (J. Appl. Probab. 46, 296–307, 2009) proves multitype branching extinction-time approximations assuming an irreducible linearized offspring matrix with a simple dominant eigenvalue (Theorem 2.1 and the subsequent subcritical estimates). Its full article, including that hypothesis, was inspected. This condition is inapplicable to the present one-way process, whose two decay rates coincide at resonance and whose source-to-receiver transmission matrix is reducible. Windridge (arXiv:1408.4768, first public 20 August 2014) proves Gumbel extinction asymptotics for a particular subcritical multitype branching epidemic through a *purely exponential* survival-tail estimate. The present process is not a branching process because receivers are finite-state susceptible/infected particles subject to repeated infection, and its repeated recovery eigenvalue produces a polynomial factor in the transient tail, hence a \(\log\log n\) centering correction. Ménard and Singh (arXiv:1502.06982, 24 February 2015) study nontrivial infinite-graph contact-process thresholds by cumulative merging, rather than a finite directed two-population extinction distribution. Van de Bovenkamp and Van Mieghem (Phys. Rev. E 92, 032806, 2015) investigate general finite-network SIS survival times and evaluate mean survival times on complete and star graphs; the available abstract does not specify this directed two-layer joint near-resonant distribution. Their full article was not accessible for inspection and remains a historical-coverage risk. No absolute priority or independence from every possible general theorem is claimed. The exact logarithmic detuning profile and the conditional Poisson argument are supplied here in full.

## Limitations
The model deliberately forbids receiver-to-source and receiver-to-receiver transmission. Sources recover permanently; only receivers exhibit SIS-type reinfection. The asymptotic assumes initial infection of every source, initial susceptibility of every receiver, and positive finite asymptotic population ratio. The result provides weak convergence, not a quantitative total-variation rate for the extinction time or convergence of its moments. The same laws need not apply to bidirectional, sparse, spatially heterogeneous, or nearly-empty-source networks. General branching-process Gumbel theory supplies conceptual context but does not establish the specific asserted critical detuning formula without an additional comparison argument. Full historical priority remains subject to further literature review.

## References
1. D. Heinzmann, “Extinction times in multitype Markov branching processes,” Journal of Applied Probability 46 (2009), 296–307, https://doi.org/10.1239/jap/1238592131 (journal issue dated March 2009; earliest day of public availability not independently verified).
2. P. Windridge, “The extinction time of a subcritical branching process related to the SIR epidemic on a random graph,” arXiv:1408.4768 (first public 2014-08-20), https://arxiv.org/abs/1408.4768.
3. L. Ménard and A. Singh, “Percolation by cumulative merging and phase transition for the contact process on random graphs,” arXiv:1502.06982 (first public 2015-02-24), https://arxiv.org/abs/1502.06982.
4. R. van de Bovenkamp and P. Van Mieghem, “Survival time of the susceptible-infected-susceptible infection process on a graph,” Phys. Rev. E 92, 032806 (2015), https://doi.org/10.1103/PhysRevE.92.032806. The full article was inaccessible; comparison is based on its publication abstract.
