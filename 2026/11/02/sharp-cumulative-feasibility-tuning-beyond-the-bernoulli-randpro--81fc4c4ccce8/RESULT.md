# Sharp cumulative feasibility tuning beyond the Bernoulli RandProx-LC step bound

## Finding
For the Bernoulli-skipped linearly constrained RandProx algorithm on a scalar strongly convex quadratic, the exact mean-square stability interval in the dual-step product \(a=\gamma\tau\) is \(0<a<2\), independent of the update probability \(p\in(0,1)\). The algorithm's published general-purpose sufficient restriction specializes to \(a\le p\). More significantly, the **unique dual step minimizing the accumulated expected squared constraint violation** is
\[
a_\star(p)=\frac{2p}{p+\sqrt{p(4-3p)}}=\frac{2\sqrt p}{\sqrt p+\sqrt{4-3p}},\qquad p<a_\star(p)<1.
\]
Thus the cumulatively optimal step lies outside the published sufficient parameter region whenever an update can be skipped. In the rare-update regime, its accumulated feasibility cost is of order \(p^{-3/2}\), compared with order \(p^{-2}\) at both the standard bound \(a=p\) and the fastest mean-square dual step \(a=1\). This is a source-specific exact risk-versus-rate law, not a generalization to arbitrary constrained problems.

## Assumptions and scope
Fix \(\mu>0\), \(0<p<1\), deterministic \(x^0\in\mathbb R\) and \(u^0\in\mathbb R\setminus\{0\}\), and independent \(I_t\sim\operatorname{Bernoulli}(p)\), \(t=0,1,\ldots\). Minimize \(f(x)=\mu x^2/2\) subject to \(Kx=b\), with \(K=1\), \(b=0\), and \(g=0\). The unique primal-dual solution is \((x^\star,u^\star)=(0,0)\). Use Algorithm 4 (RandProx-LC) of Condat–Richtárik, with exact full gradient, primal step \(\gamma=1/\mu\), dual step \(\tau>0\), and the Bernoulli unbiased operator \(\mathcal R_t(z)=I_tz/p\), for which \(\omega=(1-p)/p\). Write \(a=\gamma\tau\). The prescribed source-theorem sufficient condition is \(a\le p\); we analyze the actual algebraic iteration also for larger \(a\).

Define the accumulated squared feasibility loss **starting after the first update** by
\[
J_p(a)=\sum_{t=1}^{\infty}\mathbb E\bigl[|Kx^t-b|^2\bigr]
=\sum_{t=1}^{\infty}\mathbb E[(x^t)^2].
\]
The particular choice to start at \(t=1\) excludes the initial condition; including \(t=0\) adds an \(a\)-independent term and does not change the optimizer. This criterion measures cumulative constraint violation; the extended-value constrained objective itself is not used on infeasible iterates.

## Proof
**Exact recurrence.** In the stated specialization, \(\nabla f(x)=\mu x\) and the source algorithm gives
\[
\widehat x^t=x^t-\gamma\mu x^t-\gamma u^t=-\gamma u^t.
\]
Its dual update, using \(1+\omega=1/p\), and its final primal correction become
\[
u^{t+1}=u^t+\frac{\tau}{1+\omega}\mathcal R_t(\widehat x^t)
=(1-aI_t)u^t,
\qquad
x^{t+1}=-\gamma\left(1-\frac{aI_t}{p}\right)u^t.
\]
This holds for every initial \(x^0\), with no stationarity assumption. Set
\[
q(a,p)=\mathbb E(1-aI_t)^2=1-pa(2-a),
\quad c(a,p)=\mathbb E\left(1-\frac{aI_t}{p}\right)^2
=1-2a+\frac{a^2}{p}.
\]
Independence of \(I_t\) from preceding iterates, followed by induction, yields the exact identities for all integers \(t\ge0\):
\[
\mathbb E[(u^t)^2]=(u^0)^2q(a,p)^t,
\quad
\mathbb E[(x^{t+1})^2]=\gamma^2(u^0)^2c(a,p)q(a,p)^t.
\]
Since \(0<p<1\), we have \(q(a,p)>0\) and \(c(a,p)=(a-p)^2/p+(1-p)>0\). The two sequences converge in mean square to zero exactly when \(q<1\), which for \(a>0\) is exactly \(0<a<2\). In that interval, since \(|1-a|<1\) and the Bernoulli success count tends to infinity almost surely, the dual converges almost surely; the displayed primal recurrence gives almost-sure primal convergence as well. At \(a=2\), the dual magnitude stays constant; above \(2\), the dual magnitude diverges almost surely. The source's Theorem 4 requires
\[
\gamma\tau((1-\zeta)\|K\|^2+\omega_{\mathrm{ran}})\le1;
\]
for Bernoulli sampling on \(K=1\), \(\zeta=0\) and \(\omega_{\mathrm{ran}}=(1-p)/p\), so this reduces to \(a\le p\), a sufficient but not necessary condition in this family.

**Cumulative-risk minimization.** For \(0<a<2\), summing the absolutely convergent geometric series gives
\[
\frac{J_p(a)}{\gamma^2(u^0)^2}
=S_p(a)=\frac{1-2a+a^2/p}{pa(2-a)}.
\]
Differentiating this explicit rational function yields
\[
S_p'(a)=\frac{2((1-p)a^2+pa-p)}{p^2a^2(2-a)^2}.
\]
The numerator \(G_p(a)=(1-p)a^2+pa-p\) is strictly increasing for \(a>0\), negative at \(a=0\), and positive at \(a=2\), so there is exactly one critical point. Since \(S_p\) diverges at both endpoints \(0\) and \(2\), that point is the unique global minimizer. Solving \(G_p(a)=0\), rationalizing the positive root, gives the formula for \(a_\star(p)\). Moreover
\[
G_p(p)=-p(1-p)^2<0,\quad G_p(1)=1-p>0,
\]
so \(p<a_\star(p)<1\). Consequently, the cumulative optimum is neither the largest step certified by Theorem 4 nor the step that minimizes \(q(a,p)\): the latter is uniquely \(a=1\) because \(q=1-p+p(a-1)^2\).

**Rare-update scale and separation.** The exact expressions at the two comparison steps are
\[
S_p(p)=\frac{1-p}{p^2(2-p)},
\qquad S_p(1)=\frac{1-p}{p^2}.
\]
As \(p\downarrow0\), direct expansion of the radical gives \(a_\star(p)\sim\sqrt p\), \(S_p(a_\star(p))\sim p^{-3/2}\), and hence
\[
\frac{S_p(p)}{S_p(a_\star(p))}\sim\frac{1}{2\sqrt p},
\qquad
\frac{S_p(1)}{S_p(a_\star(p))}\sim\frac{1}{\sqrt p}.
\]
The improvement in cumulative feasibility error is unbounded as skipping becomes rare. For the special rate-optimal choice \(a=1\), the dual is annihilated at the first Bernoulli success, and the primal is annihilated on the following update; thus a finite-termination interpretation is consistent with the fast asymptotic mean-square factor but does not minimize cumulative primal excursions.

## Verification
The accompanying standalone `verify.py` checks the symbolic recurrence, the derivative and minimizer identities, all endpoint comparisons, and 96 sets of exact rational Bernoulli-tree moment equalities (each involving complete enumeration of every sample path up to six steps). The exhaustive finite trees are crosschecks for the closed-form laws, not infinite-horizon proofs; those rest on the independent-product identity and geometric-series argument above. Run `python verify.py` after installing packages in `requirements.txt`.

## Relationship to prior work
Condat and Richtárik, *RandProx: Primal–Dual Optimization Algorithms with Randomized Proximal Updates*, arXiv:2207.12891, first posted 2022-07-26, provide Algorithm 4, the Bernoulli operator (6), Algorithm 5, and Theorem 4 with its sufficient \(a\le p\) specialization. These algorithmic and convergence ingredients are prior work. Their bound concerns a general class of problems, so a larger admissible range in this particular scalar case does not contradict it. The present result supplies the exact scalar mean-square domain and unique optimum of a separately motivated *cumulative squared feasibility* objective; neither is stated in the inspected source passages. Mishchenko and coauthors' *ProxSkip*, arXiv:2202.09357, Theorem 3.6, concerns a fixed parameter relationship and expected Lyapunov rates and does not provide the variable dual-step cumulative feasibility optimizer. A step beyond the source bound is a statement about this specialization, not a generally valid RandProx parameter recommendation.

## Limitations
The calculation is exact for one scalar linearly constrained quadratic, a particular exact-gradient primal step, iid Bernoulli skips, and deterministic nonzero initial dual. No stability claim is made for arbitrary smooth objectives, other constraint matrices, inexact gradients, correlated randomizations, or implementation floating-point effects. The risk criterion is \(\sum_t\mathbb E[(x^t)^2]\), not terminal objective error or communication cost, and selecting \(a_\star\) requires knowledge of the sampling probability. The proof does not establish historical priority relative to every possible earlier stochastic-splitting analysis.

## References
1. L. Condat and P. Richtárik, *RandProx: Primal–Dual Optimization Algorithms with Randomized Proximal Updates*, arXiv:2207.12891, first version 2022-07-26; inspected public HTML version 3 (Algorithms 2, 4, 5, Theorem 4, Appendix A.1): https://arxiv.org/html/2207.12891v3 .
2. K. Mishchenko, G. Malinovsky, S. Stich, and P. Richtárik, *ProxSkip: Yes! Local Gradient Steps Provably Lead to Communication Acceleration! Finally!*, arXiv:2202.09357, first version 2022-02-18; inspected public HTML version 2 (Algorithm 1, Theorem 3.6, Section 3.5): https://arxiv.org/html/2202.09357v2 .
