# Critical delegation produces non-self-averaging lost voting weight

## Finding

Consider uniform transitive delegation on a complete directed social network without self-arcs. Each of \(n\ge2\) voters independently votes directly with probability \(q_n\), or delegates uniformly to one of the other \(n-1\) voters. A voter is **represented** when their delegation chain terminates at a direct voter; every voter whose chain enters a directed delegation cycle without a direct voter loses their voting weight. Let \(Z_n\) be the number represented and \(X_n=Z_n/n\).

There is a **sharp square-root transition**. If \(q_n\sqrt n\to0\), then \(X_n\to0\) in probability; if \(q_n\sqrt n\to\infty\), then \(X_n\to1\) in probability. In the critical regime \(q_n\sqrt n\to c\in(0,\infty)\), define

\[
I(a)=\int_0^\infty e^{-au-u^2/2}\,du,\quad P(c)=cI(c),\quad H_c(t)=(c+t)I(c+t).
\]

The limiting mean and variance are exactly

\[
\lim_{n\to\infty}\mathbb E X_n=P(c),\qquad
\lim_{n\to\infty}\operatorname{Var}(X_n)
=V(c)=\int_0^\infty ce^{-ct-t^2/2}[H_c(t)-P(c)]\,dt>0.
\]

Thus the represented fraction **does not converge in probability to any deterministic constant** at the critical scale. In particular, \(P(1)\approx0.6556795424\) and \(V(1)\approx0.07008433765\), so the standard deviation remains approximately \(0.26473447\). The persistent sample-to-sample spread matters when forecasting how much voting weight actually survives delegation cycles.

For each finite \(n\) and \(q\in[0,1]\), the exact expected represented fraction also has the positive finite sum

\[
\mathbb E X_n = q\sum_{k=0}^{n-1}(1-q)^k\prod_{r=1}^{k}\frac{n-r}{n-1},
\]

where an empty product equals one. An exact two-point recursion for the finite variance appears below and in the standalone checker. The finite sum alone is not presented as a new complete probability law; the new claim is the critical non-concentration theorem and its strictly positive explicit variance.

## Assumptions and scope

Each voter independently chooses exactly one action, direct voting or delegation, before any tallies are computed. Direct voters are sinks; non-direct voters point to another uniformly random vertex, with no self-delegation. Delegation is frozen and transitive. In a cycle with no direct voter, neither cycle members nor any upstream voters are counted. Every voter starts with unit weight. The theorem counts represented weight, not the accuracy of a two-candidate decision. There is no tie-breaking convention to specify.

The finite formulas hold for all integers \(n\ge2\) and probabilities \(q\in[0,1]\). All asymptotic limits are as \(n\to\infty\) through integers, with the indicated sequence of probabilities. The non-concentration conclusion requires \(c\in(0,\infty)\), not its endpoints.

## Proof

**One ancestral path.** Fix vertex \(1\), and reveal its actions sequentially along its directed chain. If the first \(k\) distinct vertices are non-direct and the next is a fresh direct voter, the event has probability

\[
a_{n,k}(q)=q(1-q)^k\prod_{r=1}^{k}\frac{n-r}{n-1},\qquad 0\le k\le n-1.
\]

Indeed, a non-direct vertex picks among the other \(n-1\) vertices, and the \(r\)-th attempted step along a self-avoiding chain has \(n-r\) unvisited choices. The disjoint events indexed by \(k\) exhaust successful paths. Exchangeability then yields \(\mathbb E X_n=\sum_k a_{n,k}\).

**Exact finite two-point law.** Let \(A_i\) mean that voter \(i\) is represented, and write \(J_n(q)=\Pr(A_1\cap A_2)\). Condition on a successful path from voter \(1\) containing \(s\) vertices, including one direct-voting endpoint. If voter \(2\) is on that path it succeeds. Otherwise, to compute its success probability, consider an exploration that has exposed \(\ell\) distinct non-direct vertices outside the known successful path. Denote its conditional success probability by \(h_{s,\ell}\). Success occurs by hitting any of the \(s\) known successful vertices; alternatively it may visit an unexposed vertex, which directly votes with probability \(q\) or continues exploration. Revisiting one of the previously exposed non-direct vertices fails. Thus

\[
h_{s,n-s}=\frac{s}{n-1},\qquad
h_{s,\ell}=\frac{s}{n-1}+\frac{n-s-\ell}{n-1}\bigl[q+(1-q)h_{s,\ell+1}\bigr]
\]

for \(1\le\ell<n-s\). For \(s<n\), put \(f_{n,s}=q+(1-q)h_{s,1}\), and set \(f_{n,n}=0\) solely to simplify the zero-coefficient endpoint. Conditional on the first path having \(k+1\) vertices, voter \(2\) lies on it with probability \(k/(n-1)\). Otherwise its success probability is \(f_{n,k+1}\). Therefore

\[
J_n(q)=\sum_{k=0}^{n-1}a_{n,k}(q)
\left[\frac{k}{n-1}+\frac{n-1-k}{n-1}f_{n,k+1}\right].
\]

Consequently the exact finite variance is

\[
\operatorname{Var}(X_n)=\frac{p_n(1-p_n)}n+
\frac{n-1}{n}\bigl[J_n(q)-p_n^2\bigr],\qquad p_n=\sum_k a_{n,k}.
\]

The recursion involves only probabilities of fresh vertices, hits to the known successful path, or self-intersections. It is valid also when \(q=0\) or \(q=1\).

**Critical single-path limit.** Suppose \(q_n\sqrt n\to c\in(0,\infty)\). For \(k/\sqrt n\to t\ge0\),

\[
(1-q_n)^k\prod_{r=1}^k\frac{n-r}{n-1}
\longrightarrow e^{-ct-t^2/2}.
\]

For bounded \(t\), this follows by logarithmic expansion. The upper bound \(\prod_{r=1}^k (n-r)/(n-1)\le\exp[-k(k-1)/(2(n-1))]\) provides a summable Gaussian tail uniformly in \(n\). A Riemann-sum argument therefore gives \(\sum_k a_{n,k}\to cI(c)\). More precisely, the successful-chain length divided by \(\sqrt n\) has a subprobability density limit \(ce^{-ct-t^2/2}\,dt\).

**Two paths and non-concentration.** Conditional on a successful first path of \(s\) vertices with \(s/\sqrt n\to t\ge0\), voter \(2\) is on the first path with probability \(O(s/n)=o(1)\). If it is outside, its successive non-direct vertices encounter a direct voter at asymptotic rate \(c/\sqrt n\), an already known successful vertex at rate \(t/\sqrt n\), and a previously visited vertex at rate \(u/\sqrt n\) after \(u\sqrt n\) distinct visits. More exactly, after \(\ell\) distinct non-direct vertices outside the known path, the survival probability before an absorption, hit or self-intersection is

\[
(1-q_n)^\ell\prod_{r=1}^{\ell-1}\frac{n-s-r}{n-1}.
\]

For \(\ell/\sqrt n\to u\ge0\), this tends to \(e^{-(c+t)u-u^2/2}\). At that step the success probability at the next action is \(s/(n-1)+q_n(n-s-\ell)/(n-1)\), asymptotic to \((c+t)/\sqrt n\). The same Gaussian tail argument justifies Riemann summation and yields \(f_{n,s}\to H_c(t)\), uniformly for \(t\) in compact intervals. Integrating over the first-path length gives

\[
\lim_{n\to\infty}J_n(q_n)=
\int_0^\infty ce^{-ct-t^2/2}H_c(t)\,dt.
\]

Since \(0\le X_n\le1\), the finite variance identity yields \(\operatorname{Var}(X_n)\to V(c)\). To see strict positivity, integrate by parts:

\[
H_c(t)=1-\int_0^\infty u e^{-(c+t)u-u^2/2}\,du.
\]

Hence \(H_c\) is strictly increasing on \([0,\infty)\), and \(H_c(0)=P(c)\). The positive integral defining \(V(c)\) is therefore strictly greater than zero for all \(c>0\). If \(X_n\) converged in probability to a constant, boundedness would force its variance to vanish, contradicting this limit.

**Away from the critical window.** Fix independent random variables determining each voter's potential target and a uniform random variable determining whether the voter casts a direct ballot. Increasing \(q\) converts delegators into direct voters without destroying any represented paths, so \(X_n\) is nondecreasing under this coupling. For any \(M>0\), compare with \(q=M/\sqrt n\). Since \(P(M)\to1\) as \(M\to\infty\) and \(P(M)\to0\) as \(M\downarrow0\), the critical-window mean limit and monotonicity imply the claimed off-critical limits. Because \(X_n\in[0,1]\), the corresponding mean limits imply convergence in probability via Markov's inequality.

## Verification

The bundled Python program `verify.py` is independent of the asymptotic limit argument. It exhaustively enumerates every vector of direct-voting or out-neighbor choices for \(2\le n\le6\), at both \(q=1/3\) and \(q=2/5\). It uses exact integer probability weights for every action profile and exact rational arithmetic for both \(\mathbb EX_n\) and \(\Pr(A_1\cap A_2)\), comparing brute-force enumeration with the separate path formulas above. There are \(100136\) complete delegation profiles over the ten checks. Running `python3 verify.py` prints `EXACT_CHECKS_OK 10 ASSIGNMENTS 100136` if all assertions pass.

The limiting integrals at \(c=1\) are numerical evaluations, not finite-sample certification. The analytic estimates and dominated Riemann sums, not the finite enumeration, prove the infinite conclusions.

## Relationship to prior work

Christoff and Grossi, arXiv:1612.08048, introduced the guru/cycle-abstention framework and calculated the limiting probability of **no direct voters** under an impartial profile model, a different event from the fraction of votes ultimately represented. Berinsky et al., arXiv:2107.11868, studied concentration and truth tracking for fixed positive direct-voting probabilities, including consequences of delegation cycles, rather than a vanishing direct-voter probability at the critical square-root scale. Colley, Delemazure and Gilbert, arXiv:2301.02462, gave a general **finite** delegation-partition recursion on a complete digraph. Their recursion is stronger for finite-law enumeration and could in principle be used to obtain finite moments; those finite distributional implications are not asserted as new here. The distinct contribution is an explicit nonzero asymptotic variance and non-self-averaging theorem in the singular \(q_n\sqrt n\to c\) regime. The proof uses a second growing ancestral path and its collision hazard to quantify correlation.

Related finite exact expected-participation formulas on bipartite delegation graphs also yield the same first-moment crossover constant in the balanced case; this finding is not premised on treating that mean limit as new. The independent strictly positive *variance* limit, proved here for uniform complete-digraph delegation, is the substantive mathematical distinction.

## Limitations

The result does not characterize the complete weak limit law of \(X_n\); it gives its limiting first two moments and proves that no deterministic limit exists in the critical window. It does not quantify voting accuracy, power of individual gurus, or strategic delegation. The theorem assumes that every delegator samples uniformly from all other voters and that the initial delegation choices are independent. Cycles are treated as lost voting weight; procedural cycle-resolution rules would alter the model. Related classical random-mapping asymptotics could contain equivalent formulations under different terminology. In particular, existing complete-graph finite partition recursions must not be misrepresented as absent or uninformative.

## References

- Zoé Christoff and Davide Grossi, *Liquid Democracy: An Analysis in Binary Aggregation and Diffusion*, arXiv:1612.08048, first submitted 2016-12-23, Section 3.2.1. https://arxiv.org/abs/1612.08048
- Adam J. Berinsky et al., *Tracking Truth with Liquid Democracy*, arXiv:2107.11868, first submitted 2021-07-25, Sections 2–5 and appendices. https://arxiv.org/abs/2107.11868
- Rachael Colley, Théo Delemazure and Hugo Gilbert, *Measuring a Priori Voting Power—Taking Delegations Seriously*, arXiv:2301.02462, first submitted 2023-01-06, Section 5 and Proposition 3. https://arxiv.org/abs/2301.02462
