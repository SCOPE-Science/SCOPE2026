# Near-critical first-return crossover for the Pelikan random interval map

## Finding
For a uniform initial point in the upper dyadic interval, the Pelikan random interval map has the following sharp first-return transition. Let \(\Phi\) be the standard normal distribution function. For fixed \(u\in\mathbb R\), define the parameter \(p_n=\tfrac12+u/(2\sqrt n)\). Then
\[
\lim_{n\to\infty}\sqrt n\,\Pr_{p_n}(\tau>n)
=\mathcal F(u),\qquad
\mathcal F(u)=\sqrt{\frac2\pi}e^{-u^2/2}-2u\Phi(-u).
\]
The event on the left includes the possibility of never returning. In particular \(\mathcal F(0)=\sqrt{2/\pi}\), the function is strictly decreasing, and \(\mathcal F'(u)=-2\Phi(-u)\). The negative-parameter limit includes a positive escape contribution absent on the positive side. The claim concerns an explicit near-critical scaling, not a new general ballot theorem or the already studied fixed-parameter recurrence dichotomy.

## Assumptions and scope
At each integer time an independent coin chooses the expanding map \(T_+(x)=2x\bmod1\) with probability \(p\), and the contracting map \(T_-(x)=x/2\) with probability \(q=1-p\). Fix \(I=[1/2,1)\), choose \(X_0\) with normalized Lebesgue law on \(I\), and let \(\tau=\inf\{k\ge1:X_k\in I\}\), taking \(\tau=\infty\) when no such time exists. Endpoint conventions affect only a null initial set. For each horizon \(n\) the parameter is constant throughout the entire \(n\)-step trajectory and equals \(p_n\); the parameter is not changed dynamically from step to step. The theorem applies to every fixed real \(u\) and sufficiently large integers \(n\) with \(p_n\in(0,1)\). It does not assert uniformity for \(u\) growing with \(n\), nor a quenched (fixed coin-sequence) limit.

Write the dyadic bands as \(I_j=[2^{-j-1},2^{-j})\), for integers \(j\ge0\), and write \(J_k=j\) when \(X_k\in I_j\). An interval-uniform point remains interval-uniform under every branch restricted to a single band. From level \(j\ge1\) the level decreases by one with probability \(p\) and increases by one with probability \(q\). From \(J_0=0\), the first step has level distribution
\[
\Pr(J_1=j)=q\mathbf1_{\{j=1\}}+p2^{-j-1},\qquad j\ge0.
\]
In particular, the first-step height \(J=J_1\) has \(\mathbb E J=1\), independently of \(p\). A step to \(J=0\) is an immediate return; otherwise subsequent return is the first downward hit of zero from height \(J\).

## Proof
Let \(H_j\) denote the hitting time of zero by a nearest-neighbor random walk on nonnegative levels, started at integer \(j\ge0\), with down-step probability \(p\) and up-step probability \(q\). Put \(H_0=0\), allowing \(H_j=\infty\) when appropriate. The elementary ballot/reflection formula gives, for integers \(m\ge j\ge1\) with \(m\equiv j\pmod 2\),
\[
\Pr_p(H_j=m)=\frac jm\binom{m}{(m+j)/2}
 p^{(m+j)/2}q^{(m-j)/2};
\]
the probability is zero for all other finite \(m\). For \(p<q\), its total mass is \((p/q)^j\), so \(\Pr_p(H_j=\infty)=1-(p/q)^j\); for \(p\ge q\), this nonreturn probability is zero. Because \(\tau=1+H_J\), with the convention \(1+\infty=\infty\),
\[
\Pr_p(\tau>n)=\sum_{j\ge0}
 \big(q\mathbf1_{\{j=1\}}+p2^{-j-1}\big)
 \Pr_p(H_j>n-1).
\tag{1}
\]

Fix \(u\in\mathbb R\) and use \(p=p_n\). For fixed \(j\ge1\), Stirling's formula applied to the displayed ballot mass, on the lattice of parity \(m\equiv j\pmod2\), gives the tail limit
\[
\lim_{n\to\infty}\sqrt n\sum_{m>n-1}\Pr_{p_n}(H_j=m)
=\frac{j}{\sqrt{2\pi}}\int_1^\infty
 t^{-3/2}e^{-u^2t/2}\,dt.
\tag{2}
\]
Indeed \(4p_nq_n=1-u^2/n\) and \((p_n/q_n)^{j/2}\to1\). The factor of two from parity lattice spacing is included in the coefficient. The bound \(\Pr_{p_n}(H_j=m)\le C_jm^{-3/2}\), valid for large \(n\) and all allowed \(m\), justifies extending the Riemann sum to infinite time. If \(u<0\), the defective mass obeys
\[
\lim_{n\to\infty}\sqrt n\Pr_{p_n}(H_j=\infty)=-2uj,
\]
while for \(u\ge0\) it vanishes. Integration by parts and a Gaussian change of variables identify the integral in (2) as
\[
\frac1{\sqrt{2\pi}}\int_1^\infty t^{-3/2}e^{-u^2t/2}\,dt
=\sqrt{\frac2\pi}e^{-u^2/2}-2|u|\Phi(-|u|).
\]
Thus in every sign regime,
\[
\lim_{n\to\infty}\sqrt n\,\Pr_{p_n}(H_j>n-1)
=j\left[\sqrt{\frac2\pi}e^{-u^2/2}-2u\Phi(-u)\right].
\tag{3}
\]

It remains to justify averaging over the unbounded but geometrically decaying initial level \(J\). The unit-height ballot formula and \(4p_nq_n\le1\) give
\[
\Pr_{p_n}(H_1>m)\le C_u m^{-1/2}
\quad(1\le m\le n),
\]
including the possible infinite-hitting mass of order \(n^{-1/2}\). By the strong Markov property \(H_j\) is a sum of \(j\) independent copies of \(H_1\), possibly infinite. For \(1\le j\le n-1\), if the sum exceeds \(n-1\), at least one summand exceeds \(\lfloor(n-1)/j\rfloor\). A union bound yields \(\sqrt n\,\Pr_{p_n}(H_j>n-1)\le C'_u j^{3/2}\). The same estimate after increasing the constant is trivial for \(j\ge n\). The first-step distribution is bounded by a constant multiple of a geometric law, whose \(3/2\)-moment is finite, uniformly in \(n\). Dominated convergence in (1), followed by \(\mathbb E J=1\), gives the announced limit exactly. No finite computation substitutes for the infinite-time estimates.

As a supporting identity, the unit-height hitting-time probability generating function satisfies \(h(z)=z(p+qh(z)^2)\), so
\[
h(z)=\frac{1-\sqrt{1-4pqz^2}}{2qz},\qquad
\mathbb E_p[z^\tau;\tau<\infty]
=z\left(qh(z)+\frac{p}{2-h(z)}\right),\quad 0<z<1.
\]
These exact generating functions are supplied to make the first-return law reproducible; the claim of originality concerns the explicit finite-horizon *double-scaling limit* proved above, not the underlying classical hitting-time identity.

## Verification
The accompanying standalone \(\texttt{verify.py}\) reproduces exact finite-time first-return probabilities in two independent ways: the ballot formula and forward dyadic-level Markov dynamics with rational probabilities. It also compares independently propagated survival tails for increasing horizons against the analytical crossover function at several fixed positive, negative, and zero values of \(u\). The checker uses optional numerical arrays for these limit illustrations; the proof of (2), (3), and the dominated-convergence step remains analytical. Run with \(\texttt{python verify.py}\) in an environment with Python 3 and NumPy.

## Relationship to prior work
Hata and Yano (first arXiv version 2021-08-03) proved critical infinite-ergodic laws for the Pelikan map and wrote down the dyadic transition kernel; their results do not assert the present varying-parameter return-tail profile. Yan et al. (first arXiv version 2023-08-18) investigated the critical transition, invariant densities and correlations. Monthus (first arXiv version 2024-09-30) gave explicit fixed-parameter absorption/first-passage transforms for the associated nearest-neighbor model, its resetting-time laws, and their fixed-parameter asymptotics, notably Appendix B, equations B35–B47. Those formulas and the classical ballot law provide much of the structure; the present distinction is the *joint* limit where the probability bias tends to criticality at exactly the inverse square-root horizon scale for return to the upper dyadic band. Monthus's fixed-parameter asymptotics cannot simply be substituted at \(p=p_n\), since their error estimates are not uniform in the bias. This work does not claim novelty of Brownian first-passage techniques, the underlying Markov reduction, or the fixed-parameter recurrence dichotomy.

## Limitations
The result is annealed and for the specified absolutely continuous initial distribution on the upper dyadic interval. It does not address arbitrary singular initial data, common-noise conditioning, functional limit processes or a uniform-in-\(u\) error bound. Exact reset-event waiting times studied by Monthus are not identical to first returns of the level-zero band. Classical random-walk techniques are essential ingredients; the historical-priority risk that a general unpublished uniform first-passage theorem subsumes this particular parameter-window formula remains. All correctness and novelty assessments reported elsewhere are internal reviews, not independent validation.

## References
- G. Hata and K. Yano, “Arcsine and Darling–Kac laws for piecewise linear random interval maps,” arXiv:2108.01332, first posted 2021-08-03, especially §5 and its dyadic Markov kernel. https://arxiv.org/abs/2108.01332
- J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck and R. Klages, “Transition to anomalous dynamics in a simple random map,” arXiv:2308.09269, first posted 2023-08-18. https://arxiv.org/abs/2308.09269
- C. Monthus, “Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region,” arXiv:2409.19999, first posted 2024-09-30, especially §V and Appendix B. https://arxiv.org/abs/2409.19999
