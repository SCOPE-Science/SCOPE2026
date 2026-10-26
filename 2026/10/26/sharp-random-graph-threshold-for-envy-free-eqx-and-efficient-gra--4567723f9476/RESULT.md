# Sharp random-graph threshold for envy-free, EQX and efficient graphical goods allocations

## Finding
Let \(G_n\sim G(n,c\log n/n)\) for a fixed real \(c>0\). Each vertex is an agent, and each edge is a distinct indivisible good worth one to either endpoint and zero to every other agent; utilities are additive and **not normalized across agents**. Write \(P_n\) for the existence of a complete allocation that is simultaneously envy-free (EF), equitable up to any positively valued good (EQX), and fractionally Pareto optimal (fPO). With
\[
c_*=\frac{2}{1-\log 2},
\]
the sharp off-critical law is
\[
\lim_{n\to\infty}\Pr(P_n)=\begin{cases}0&0<c<c_*,\\1&c>c_* .\end{cases}
\]
In fact, in the upper regime, with probability tending to one there is a welfare-maximizing orientation whose recipients' utilities differ by at most one. The assertion does not specify the law at \(c=c_*\).

## Assumptions and scope
A simple graph \(G=(V,E)\) has \(n\ge2\) vertices, \(m=|E|\), and \(q=\lfloor m/n\rfloor\). Each edge-good may be allocated to exactly one agent. An allocation is EF if \(u_i(A_i)\ge u_i(A_j)\) for every ordered pair \(i,j\). It is EQX if \(u_i(A_i\setminus\{g\})\le u_j(A_j)\) for every \(i,j\) and every \(g\in A_i\) positively valued by \(i\). Fractional Pareto optimality rules out a feasible fractional reassignment weakly improving every agent's expected additive utility and strictly improving one. Logarithms are natural. The random graph is a simple, independent-edge Erdős–Rényi graph, and \(c\) is fixed while \(n\) tends to infinity.

## Proof
**1. Deterministic orientation criterion.** Total attainable welfare is \(m\), since each edge has unit value for its endpoints. Every fPO complete allocation must achieve this value: an edge given to an unapproving agent can be transferred to an approving endpoint without harming its current recipient. Conversely, an endpoint allocation maximizes welfare and is fPO. Therefore fPO allocations correspond exactly to orientations with recipient indegrees \(t_v\) and \(\sum_v t_v=m\).

For a simple graph, an agent values at most one good in any *other* agent's bundle. Thus an orientation is EF exactly when every vertex incident to an edge has \(t_v\ge1\). All goods held in an orientation have positive value to their recipients, so EQX says \(t_i-1\le t_j\) for every pair of agents with \(t_i>0\). If \(m>0\), this is equivalent to \(\max_v t_v-\min_v t_v\le1\); hence every \(t_v\) is either \(q\) or \(q+1\).

Write \(e(S)\) for the number of edges with both endpoints in \(S\), and \(b(S)\) for the number with at least one endpoint in \(S\). A standard integral feasible-circulation argument, or the max-flow/min-cut theorem applied to edge supply vertices and agent demand intervals, gives the exact characterization
\[
\exists\text{ edge orientation with }q\le t_v\le q+1\quad\Longleftrightarrow\quad
 e(S)\le(q+1)|S|\text{ and }b(S)\ge q|S|\ \text{for every }S\subseteq V.\tag{1}
\]
Indeed both inequalities are necessary. For sufficiency, connect a source to each edge-node with a unit arc, connect that node to its two endpoint agents with unit-capacity arcs, and connect each agent to the sink with a lower bound \(q\) and upper bound \(q+1\); standard lower-bound flow feasibility or the generalized Hall criterion yields precisely the two subset inequalities. Integrality supplies an actual orientation.

**2. Random cut expansion above the threshold.** Put \(\lambda=(n-1)p_n\), so \(\lambda\sim c\log n\). Chernoff concentration of \(m\) implies \(q/\lambda\to1/2\) in probability. Define \(I(a)=1-a+a\log a\) for \(a>0\). Since \(I(1/2)=(1-\log2)/2\), the assumption \(c>c_*\) is exactly \(cI(1/2)>1\). We show that with probability tending to one, simultaneously for all \(S\) of size \(1\le s\le n/2\),
\[
e(S)\le qs,\qquad b(S)\ge(q+1)s.\tag{2}
\]
Fix small \(\delta,\eta>0\) chosen below and work on the high-probability event \((1/2-\delta)\lambda\le q\le(1/2+\delta)\lambda\). If \(s\le\eta n\), the random variable \(b(S)\) is binomial with mean
\[
\mu_s=p_n\left(s(n-s)+\binom{s}{2}\right)=\lambda s\left(1-\frac{s-1}{2(n-1)}\right)\ge(1-\eta)\lambda s
\]
for large \(n\). Applying the exponential binomial lower-tail inequality and continuity of its rate yields
\[
\Pr\bigl[b(S)<(1/2+2\delta)\lambda s\bigr]\le\exp\left[-(1-\eta)\lambda s I\!\left(\frac{1/2+2\delta}{1-\eta}\right)\right].
\]
Choose \(\eta,\delta\) small enough that \(c(1-\eta)I((1/2+2\delta)/(1-\eta))>1+\varepsilon\) for some \(\varepsilon>0\). This upper bound is \(n^{-(1+\varepsilon/2)s}\) for large \(n\); summing over at most \(n^s\) sets works. For \(\eta n<s\le n/2\), the mean of \(b(S)\) is at least \((3/4-o(1))\lambda s\), so for \(\delta<1/8\) its lower tail below \((1/2+2\delta)\lambda s\) has probability \(\exp[-\Omega(s\log n)]\). This dominates the \(2^n\) possible subsets.

For the internal-edge condition, \(e(S)\) is binomial with mean \(\nu_s=p_n\binom{s}{2}\). If \(s\le\eta n\), for \(T=(1/2-\delta)\lambda s\), the standard bound \(\Pr[e(S)\ge T]\le(e\nu_s/T)^T\) is at most \((C s/n)^{(1/2-\delta)\lambda s}\) for an absolute constant \(C\) depending only on \(\delta\). Taking \(\eta\) small enough and summing \(\binom ns\le(en/s)^s\) makes this \(o(1)\) uniformly over these sizes. If \(\eta n<s\le n/2\), then \(\nu_s\le(1/4+o(1))\lambda s\), while \(T\ge(1/2-\delta)\lambda s\); a binomial upper-tail bound is \(\exp[-\Omega(s\log n)]\), so a union bound also succeeds. This proves (2).

For \(|S|>n/2\), put \(T=V\setminus S\). As \(|T|\le n/2\), equation (2) gives
\[
e(S)=m-b(T)\le m-(q+1)|T|\le(q+1)|S|,
\]
where the final inequality uses \(m<(q+1)n\), and
\[
b(S)=m-e(T)\ge m-q|T|\ge q|S|.
\]
Thus (1) holds for all subsets and a balanced orientation exists. Since \(q\to\infty\), this orientation is EF, EQX and fPO.

**3. A low-degree obstruction below the threshold.** Fix \(0<c<c_*\). Choose sufficiently small \(\delta>0\) such that \(cI((1-\delta)/2)<1\). With high probability \(q\ge(1-\delta/2)\lambda/2\). Put \(k_n=\lfloor(1-\delta)\lambda/2\rfloor\). For a fixed vertex, the binomial lower-tail local asymptotics at \(k_n\) yield
\[
\Pr\bigl(\deg(v)<k_n\bigr)=n^{-cI((1-\delta)/2)+o(1)}.
\]
The expected number \(Z\) of such vertices consequently diverges polynomially. For two distinct vertices, expose their common edge separately and their remaining independent incident edges. Since \(p_n=o(1)\), the joint low-degree probability is at most \((1+O(p_n))\) times the product of marginal probabilities (a direct conditioning calculation), and \(\mathrm{Var}(Z)/\mathbb E[Z]^2\to0\). Therefore \(Z>0\) with probability tending to one. Such a vertex has \(\deg(v)<q\) and cannot receive \(q\) edges in any orientation, contradicting the necessary EQX+fPO condition. This finishes both limits.

## Verification
The included independent finite checker `verify.py` tests the exact cut criterion against direct dynamic-programming edge orientations for every labeled simple graph on two through five vertices (\(2+8+64+1024=1098\) graphs) and reproducible additional six- and seven-vertex samples. These checks passed, but are not an infinite probabilistic proof. The upper and lower asymptotic assertions rely on the analytic concentration and tail arguments above. The checker also confirms the numerical value of \(c_*\) and rate identity.

## Relationship to prior work
Hosseini, Pathak, Xia and Zhang (2026, arXiv:2608.26410) investigate simultaneous envy and equitability, predominantly EF1+EQ1 under different valuation assumptions; this result concerns exact EF plus EQX plus fPO in a sparse, unnormalized graphical binary-goods model. Misra and Sethia (2024, arXiv:2410.14272) relate EF graphical allocations to orientations, but do not derive this joint random-graph phase transition. Peled and Peleg (2024, arXiv:2412.13127) already identify the **same numeric constant** in a different random-graph rigidity problem because it marks the minimum-degree-versus-half-average-degree crossover: neither the constant nor its random-degree asymptotic is claimed new. The new statement is the precise joint fair-allocation transition, including its sufficient global orientation inequalities.

## Limitations
The theorem is off-critical and does not determine behavior at \(c=c_*\), a scaling window, algorithms beyond feasible flows, multigraphs, heterogeneous weights, or agent-normalized utilities. The unnormalized valuation assumption is essential to the stated EQX equivalence. The motivating 2026 article's abstract was accessible, but its complete primary text could not be inspected; an implicit related theorem there or in the wider orientation literature remains a publication-priority risk. Numeric equality of the threshold with an earlier rigidity threshold is acknowledged rather than claimed as new. No independent audit has occurred.

## References
1. H. Hosseini, S. Pathak, L. Xia, and C. Zhang, *Simultaneous Envy and Equitability Guarantees*, arXiv:2608.26410 (first public 2026-08-26), https://arxiv.org/abs/2608.26410.
2. N. Misra and A. Sethia, *Envy-Free and Efficient Allocations for Graphical Valuations*, arXiv:2410.14272 (2024), https://arxiv.org/abs/2410.14272.
3. Y. Peled and N. Peleg, *On the Rigidity of Random Graphs in high-dimensional spaces*, arXiv:2412.13127 (2024), https://arxiv.org/html/2412.13127v2.
