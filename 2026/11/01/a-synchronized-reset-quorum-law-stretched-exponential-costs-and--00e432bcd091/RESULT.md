# A synchronized-reset quorum law: stretched-exponential costs and inverse-square optimal clock scaling

## Finding

Consider \(N\ge1\) independent Brownian searchers, each having generator \(D\partial_{xx}\), started at \(d>0\), with an absorbing target at zero. A *quorum* is achieved when **every** searcher has reached the target during a single attempt. At rate \(r>0\), one common Poisson clock aborts any unfinished attempt, resets all searchers to \(d\), and erases the attempt's completed hits. The clock is independent of Brownian trajectories and starts afresh after every abort. Let \(T_N(r)\) denote the total time until the first successful attempt and put \(c=d/\sqrt{\pi D}\).

For all finite \(N\) and \(r>0\), the exact mean is
\[
\mathbb E T_N(r)=\frac{1-q_N(r)}{r q_N(r)},\qquad
q_N(r)=r\int_0^\infty e^{-rt}\operatorname{erfc}\!\left(\frac{d}{\sqrt{4Dt}}\right)^Ndt.
\]
For each fixed \(r>0\),
\[
\boxed{\lim_{N\to\infty}\frac{\log\mathbb E T_N(r)}{N^{2/3}}
=3\left(\frac{rd^2}{4\pi D}\right)^{1/3}.}
\]

At the simultaneous scaling \(r_N=\lambda/(c^2N^2)\), \(\lambda>0\), set
\[
\Psi(\lambda)=\int_0^\infty\exp\left(-y-\frac{\lambda}{y^2}\right)dy,\qquad
H(\lambda)=\frac{1-\Psi(\lambda)}{\lambda\Psi(\lambda)}.
\]
Then the rescaled mean converges:
\[
\boxed{\lim_{N\to\infty}\frac{\mathbb E T_N(\lambda/(c^2N^2))}{c^2N^2}=H(\lambda).}
\]
The continuous function \(H\) diverges at both \(0\) and \(+\infty\), so \(h_*=\min_{\lambda>0}H(\lambda)\in(0,\infty)\) is attained. Moreover,
\[
\boxed{\lim_{N\to\infty}\frac{\min_{r>0}\mathbb E T_N(r)}{c^2N^2}=h_* .}
\]
Every exact finite-\(N\) minimizing rate exists; the set of scaled rates \(\{c^2N^2r_N^*\}\) is bounded away from both zero and infinity, and every subsequential limit lies in \(\operatorname{argmin}H\). No uniqueness of the limiting optimizer is asserted. Numerical quadrature suggests a minimizing \(\lambda\) near \(4.303684\) and \(h_*\) near \(1.924582\); these approximations are not part of the proof.

## Assumptions and scope

The Brownian motions are independent *within each attempt*. Hits during an attempt are retained until the next global reset, but **not** across attempts. Upon a reset all \(N\) paths restart independently from the identical initial position, with an independent Poisson clock. The target is a perfectly absorbing point, but an absorbed searcher stays counted as completed until the attempt ends. The model differs from protocols recording completed hits permanently, protocols resetting each searcher independently, and protocols resetting when the *first* particle arrives. There is no reset travel time, interparticle interaction, or target gating. The asserted limits hold for fixed \(D,d,r>0\), or fixed \(D,d,\lambda>0\) under the indicated \(N\)-dependent rate, and all integer \(N\to\infty\).

## Proof

**1. Bare completion time and exact renewal.** For one Brownian first-passage time \(\tau\), the reflection principle gives
\[
F(t)=\Pr(\tau\le t)=\operatorname{erfc}\!\left(\frac{d}{\sqrt{4Dt}}\right).
\]
For independent searchers within an attempt, the time needed for all successes is \(M_N=\max_{1\le j\le N}\tau_j\), so \(\Pr(M_N\le t)=F(t)^N\). If \(E_r\) is an independent exponential time of rate \(r\), the attempt succeeds precisely when \(M_N<E_r\). Integration by parts yields
\[
q_N(r)=\mathbb E e^{-rM_N}=r\int_0^\infty e^{-rt}F(t)^Ndt.
\]
The duration of one attempt is \(\min(M_N,E_r)\), whose mean is \((1-q_N(r))/r\). Renewal after each failed attempt gives \(\mathbb E T_N(r)=\mathbb E\min(M_N,E_r)/q_N(r)\), proving the exact formula. For fixed \(N\), this quantity is finite at each positive rate. As \(r\downarrow0\), it diverges because \(M_N\ge\tau_1\) and \(\mathbb E\tau_1=\infty\); as \(r\to\infty\), it diverges since \(q_N(r)\le\mathbb E e^{-r\tau_1}=e^{-d\sqrt{r/D}}\). Therefore a finite positive minimizing rate exists.

**2. Fixed-rate large-population asymptotic.** As \(t\to\infty\),
\[
F(t)=1-ct^{-1/2}+O(t^{-3/2}),\qquad
\log F(t)=-ct^{-1/2}+O(t^{-1}).
\]
Set \(t=N^{2/3}u\). Locally uniformly for \(u\in(0,\infty)\),
\[
\frac{1}{N^{2/3}}\log\big(e^{-rt}F(t)^N\big)
\longrightarrow -ru-cu^{-1/2}.
\]
For rigorously restricting the integral to a compact interval of positive \(u\), note that a universal \(b>0\) satisfies \(F(t)\le e^{-b/\sqrt t}\) for all \(t>0\): take \(b=(d/\sqrt{4D})\inf_{v>0}[-\log(\operatorname{erfc}v)]/v\), which is positive by continuity and the positive limits at zero and infinity. The contribution from \(0<t<\varepsilon N^{2/3}\) has an upper exponential rate no larger than \(-b/\sqrt\varepsilon\); the contribution from \(t>KN^{2/3}\) is bounded by \(e^{-rKN^{2/3}}\). Both become negligible by choosing \(\varepsilon\) small and \(K\) large. The elementary Laplace principle on the remaining compact interval now gives
\[
-\lim_{N\to\infty}N^{-2/3}\log q_N(r)
=\min_{u>0}(ru+cu^{-1/2})
=3(rc^2/4)^{1/3}.
\]
Since \(q_N(r)\to0\), the renewal expression has the same positive limit for \(N^{-2/3}\log\mathbb E T_N(r)\).

**3. Scaling limit and full optimal-rate scaling.** Let \(Z_N=M_N/N^2\). At each \(z>0\),
\[
\Pr(Z_N\le z)=F(N^2z)^N\longrightarrow\exp(-c/\sqrt z).
\]
Thus \(Z_N\Rightarrow Z\), with \(Z\) having this Fréchet distribution. If \(Y\) is standard exponential, then \(Z\stackrel d=c^2/Y^2\). For \(u>0\), set \(Q_N(u)=\mathbb E e^{-uZ_N}\). Bounded weak convergence implies
\[
Q_N(u)\to \Psi(c^2u),\qquad
\Psi(\lambda)=\mathbb E e^{-\lambda/Y^2}.
\]
Substitution into the exact renewal formula proves the asserted scaled-rate limit.

For the global optimization, write
\[
\frac{\mathbb E T_N(u/N^2)}{N^2}
=\frac{1-Q_N(u)}{uQ_N(u)}=:G_N(u).
\]
On compact subsets of \(u>0\), \(Q_N\) and hence \(G_N\) converge uniformly: \(|Q_N'(u)|\le1/(eu)\). To rule out escaping minimizers, first suppose \(u_N\downarrow0\). For every \(M>0\), concavity of \(1-e^{-u x}\) yields
\[
G_N(u_N)\ge\frac{1-Q_N(u_N)}{u_N}
\ge\frac{1-e^{-u_NM}}{u_NM}\,\mathbb E\min(Z_N,M).
\]
The right-hand side converges to \(\mathbb E\min(Z,M)\), and \(\mathbb EZ=\infty\) by its \(z^{-1/2}\) tail. Sending \(M\to\infty\) forces \(G_N(u_N)\to\infty\).

Conversely, suppose \(u_N\to\infty\). The same bound \(F(t)\le e^{-b/\sqrt t}\) implies \(\Pr(Z_N\le z)\le e^{-b/\sqrt z}\) for every \(z>0\) and \(N\). Splitting \(\mathbb E e^{-u_NZ_N}\) at \(Z_N=u_N^{-2/3}\) yields
\[
Q_N(u_N)\le e^{-b u_N^{1/3}}+e^{-u_N^{1/3}},
\]
so \(u_NQ_N(u_N)\to0\) and \(G_N(u_N)\to\infty\). Therefore minimizing \(u=N^2r\) stay in a common compact interval, and compact-uniform convergence implies convergence of the minima and the described limit-point property. Finally, the same small/large parameter arguments applied to \(Z\) show that the limiting objective \(H\) diverges at both endpoints (it is a positive multiple of the limit for \(G_N\)).

## Verification

A self-contained Python 3 script, `verify.py`, uses only the Python standard library to evaluate independent representations of the Laplace transforms and verify finite-population convergence numerically. It checks the single-particle closed form, the two Fréchet-transform representations, finite-population scaling, and the fixed-rate stretched-exponential exponent. Run with `python3 verify.py` from the extracted package directory. Finite quadrature is supplementary to the proofs above; it does not establish an infinite-population assertion by enumeration.

## Relationship to prior work

Biroli, Majumdar and Schehr (2023, arXiv:2303.18012) studied the *first* searcher to arrive under common versus individual resets, finding a different finite-walker optimal-resetting threshold. Vatash et al. (2026, arXiv:2609.23542) investigated optimal arrival rank with completed hits retained in the rank sequence with the cumulative arrivals measured across the search process. Those are not the present *all-in-one-epoch*, progress-erasing quorum. The Brownian first-passage law, the renewal restart identity and basic extreme-value convergence are standard inputs, not claims of novelty. The assessed contribution is the explicit combined fixed-clock stretched-exponential population law and exact optimal inverse-square clock scaling for this quorum model, including global minimizer compactness and the universal rescaling integral. Related generalized restart/maxima results could imply parts of the asymptotic mechanism; see limitations.

## Limitations

This theorem concerns a strict quorum (every member completes within one uninterrupted global-reset epoch), not permanent absorption, cumulative rank completion, or independent resets. It assumes identical starting distances, independent free Brownian motion within epochs and zero reset overhead. It does not prove uniqueness of the limiting optimal rate, rates of convergence, or a full probability law for the total completion time. Prior literature coverage is qualified because a directly relevant 2026 rank-dependent manuscript was only available in abstract/metadata form here; no independent publication-priority audit has been performed. A general theorem on restarting maxima of heavy-tailed tasks may imply portions of these results.

## References

1. M. Biroli, S. N. Majumdar and G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, Phys. Rev. E 107, 064141 (2023), arXiv:2303.18012, https://arxiv.org/abs/2303.18012.
2. R. Vatash, E. Goldfarb, V. Yu. Rudyak and Y. Roichman, *Rank-dependent optimal resetting in multiparticle search* (2026), first submitted 2026-09-20, arXiv:2609.23542, https://arxiv.org/abs/2609.23542.
3. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Phys. Rev. Lett. 106, 160601 (2011), arXiv:1102.2704, https://arxiv.org/abs/1102.2704.
