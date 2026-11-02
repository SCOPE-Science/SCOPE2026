# An effective logarithmic rate for the critical probabilities of stopping near a random-walk maximum

## Finding

For the Bernoulli semi-best selection problem, let \(p_n\) be the critical up-step probability for stopping immediately from drawdown one with \(n\) steps remaining. For every integer \(n\ge32\),
\[
0<\frac12-p_n\le\sqrt{\frac{3\log n}{2n}}.
\]
Equivalently, immediate stopping is optimal whenever
\[
0<p\le\frac12-\sqrt{\frac{3\log n}{2n}},\qquad n\ge32.
\]
In particular, \(\limsup_{n\to\infty}(\frac12-p_n)\sqrt{n/\log n}\le\sqrt{3/2}\). This is a quantitative rate, not a sharp asymptotic equivalent.

## Assumptions and scope

Let \(X_1,X_2,\ldots\) be independent with \(\Pr(X_i=1)=p\), \(\Pr(X_i=-1)=q=1-p\). Write \(S_k=\sum_{i=1}^kX_i\) and \(M_k=\max_{0\le j\le k}S_j\), with \(S_0=0\). A decision state \((n,j)\) means \(n\) future steps remain and the present running maximum is \(j\) above the present position. The reward of stopping at a time \(\tau\le n\) is the probability that the present position lies within one unit of the maximum of the entire walk through the horizon. The underlying optimal-stopping threshold theorem of Allaart [1] asserts that, in state \((n,1)\), stopping is optimal exactly when \(p\le p_n\); moreover \(p_n<1/2\) for \(n\ge4\).

Set \(U_k=\Pr_p(M_k\le1)\), \(\pi_{k,j}\) to be the maximum reward in state \((k,j)\), and \(W_n=p\pi_{n-1,0}+q\pi_{n-1,2}\), the optimal value subject to taking at least one more step from state \((n,1)\). The rule stops immediately iff \(U_n\ge W_n\). All logarithms are natural.

## Proof

**Step 1: a finite-horizon comparison.** Fix \(0<p<1/2\), write \(\delta=q-p=1-2p>0\), \(\rho=p/q\), and \(\nu=1-\rho^2\). The usual first-passage computation gives \(U_k\downarrow\nu\). More precisely, for the first hitting time \(T_2=\inf\{m\ge0:S_m=2\}\),
\[
U_L-\nu=\Pr_p(T_2>L,\ T_2<\infty)=\rho^2\Pr_q(T_2>L),
\]
where the subscript \(q\) means that the up-step probability is \(q\). The second identity is exact: for each path ending at level two for the first time, the likelihood ratio of its probability under parameters \(p\) and \(q\) is \((p/q)^2\). Under the upward-drifting law \(\Pr_q\), \(T_2<\infty\) almost surely.

For a new continuation walk \(S'_m\), its drawdown from initial drawdown \(i\) is \(D_m=\max\{i,\max_{0\le k\le m}S'_k\}-S'_m\ge i-S'_m\). Therefore \(D_m\le1\) implies \(S'_m\ge i-1\). If \(1\le L\le k\), split any stopping rule into stopping with at least \(L\) steps remaining and stopping during the final \(L\) steps. In the first part the conditional win probability is at most \(U_L\). For \(i=2\), a winning stop must first reach drawdown one, an event with probability at most \(\rho\) by gambler's ruin. A union bound for the last \(L\) times gives
\[
\pi_{k,0}\le U_L+\sum_{m=k-L+1}^{k}\Pr_p(S_m\ge-1),
\]
\[
\pi_{k,2}\le\rho U_L+\sum_{m=k-L+1}^{k}\Pr_p(S_m\ge1).
\]
These inequalities hold for arbitrary adapted stopping rules, not just threshold rules.

**Step 2: concentration with explicit dependence on the drift.** Hoeffding's inequality for sums of independent steps in \([-1,1]\) gives, whenever \(\delta m\ge1\),
\[
\Pr_p(S_m\ge-1)\le\exp\!\left[-\frac{(\delta m-1)^2}{2m}\right]\le e^{\delta-\delta^2m/2},\quad
\Pr_p(S_m\ge1)\le e^{\delta-\delta^2m/2}.
\]
Similarly, if \(\delta L\ge1\),
\[
0\le U_L-\nu\le\rho^2\Pr_q(S_L\le1)
\le\rho^2e^{\delta-\delta^2L/2}.
\]
Take \(k=n-1\), \(L=\lfloor n/3\rfloor\), and assume \(\delta L\ge1\). Since all times in the last-window sums are at least \(n-L\), the preceding bounds give
\[
W_n\le 2pU_L+Le^{\delta-\delta^2(n-L)/2}.
\]
Using \(U_n\ge\nu\) and the exact identity
\[\delta\nu=(q-p)\left(1-\frac{p^2}{q^2}\right)=\frac{\delta^2}{q^2},\]
we obtain the fully explicit certificate
\[
\boxed{U_n-W_n\ge\frac{\delta^2}{q^2}
-e^\delta\left(2p\rho^2e^{-\delta^2L/2}+Le^{-\delta^2(n-L)/2}\right).}\tag{1}
\]
No long-horizon approximation enters (1).

**Step 3: the logarithmic window.** For every integer \(n\ge32\), set
\[\delta=\sqrt{\frac{6\log n}{n}},\qquad p=\frac{1-\delta}{2}.\]
The function \(6\log n/n\) is decreasing for \(n>e\); at \(n=32\) it is less than one, so \(0<\delta<1\). As \(L=\lfloor n/3\rfloor\ge n/4\), we have \(\delta L\ge\sqrt{6n\log n}/4>1\). Moreover, \(L\ge n/3-1\) and \(n-L\ge2n/3\). Since \(2p\rho^2\le1\), the error term in (1) is bounded above by
\[
e^\delta\left(e^{-\delta^2L/2}+Le^{-\delta^2(n-L)/2}\right)
\le\frac{e^{\delta+\delta^2/2}}{n}+\frac{e^\delta}{3n}
\le\frac{e^{3/2}+e/3}{n}<\frac6n.
\]
But \(\delta^2/q^2\ge\delta^2=6\log n/n>6/n\). Therefore \(U_n>W_n\). By Allaart's exact threshold property, \(p\le p_n\). Combining this with \(p_n<1/2\) and rearranging proves the finite bound. Multiplying by \(\sqrt{n/\log n}\) gives the stated limsup bound.

## Verification

The accompanying standalone Python checker `verification/check.py` computes independent exact-rational Bellman recursions at small horizons, checks the finite probability formula, evaluates the analytic certificate over many horizons, and compares the certificate against the actual optimal Bellman continuation on several finite instances. Its recorded output is in `verification/output.txt`. These finite checks do not prove the bound for all \(n\); that conclusion follows from Steps 1–3.

## Relationship to prior work

Allaart [1] introduced the critical probabilities, proved the threshold property and the upper bound \(p_n<1/2\), and studied their oscillation. Islas [2] established further finite-index oscillation inequalities. Islas [3] proved \(p_n\to1/2\) and explicitly noted that the argument did not supply a rate. The present result derives an effective near-diffusive upper bound on the threshold deficit by combining a finite-horizon split with exact first-passage duality and concentration. It does not improve the structural threshold characterization or determine its true asymptotic order.

## Limitations

The logarithmic factor and the coefficient \(\sqrt{3/2}\) are not claimed to be optimal. The finite bound is conservative at modest horizons; sharper critical-window analysis might yield a smaller or logarithm-free error. The result is restricted to independent \(\pm1\) increments, the one-unit semi-best payoff and the decision at drawdown one. Historical-priority assessment is provisional; broader results from optimal-stopping theory could provide other quantitative bounds.

## References

[1] P. C. Allaart, *How to stop near the top in a random walk?*, RIMS Kôkyûroku **1682** (2010), 33–40. https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1682-05.pdf

[2] J. A. Islas, *Oscillation criteria for stopping near the top of a random walk*, arXiv:1711.08857, first posted 24 November 2017; subsequently *Bol. Soc. Mat. Mex.* **30** (2024), Article 43. https://arxiv.org/pdf/1711.08857

[3] J. A. Islas, *Convergence of the critical probabilities for stopping near the top of a random walk*, arXiv:2610.26670v1, first posted 19 October 2026. https://arxiv.org/html/2610.26670v2

[4] W. Hoeffding, *Probability inequalities for sums of bounded random variables*, *Journal of the American Statistical Association* **58** (1963), 13–30.
