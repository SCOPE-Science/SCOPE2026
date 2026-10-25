# Exact lost-delegation law and square-root direct-voter transition on bipartite networks

## Finding
Let the two parts of a complete bipartite delegation network contain \(m\) and \(n\) voters, where \(m,n\ge 2\). Every voter independently casts a direct ballot with probability \(q\in(0,1)\); otherwise they choose one uniformly random vertex in the other part and delegate to it. Delegations are fixed once chosen, are transitive, and all votes ending in a delegation cycle are lost.

For integers \(a\ge0\), put \((a)_0=1\) and \((a)_j=a(a-1)\cdots(a-j+1)\) for \(1\le j\le a\), with \((a)_j=0\) when \(j>a\). Write \(r=1-q\) and set
\[
A_{2j}=\frac{(n)_j(m-1)_j}{n^j m^j},\qquad
A_{2j+1}=\frac{(n)_{j+1}(m-1)_j}{n^{j+1}m^j}.
\]
The exact probability that a specified voter in the \(m\)-vertex part retains effective voting weight is
\[
H_{m,n}(q)=q\sum_{j\ge0}\left(r^{2j}A_{2j}+r^{2j+1}A_{2j+1}\right).
\]
All sums terminate automatically when their falling factorials vanish. The expected number of represented voter-weights is \(R_{m,n}(q)=mH_{m,n}(q)+nH_{n,m}(q)\), and the expected lost voter-weights are \(L_{m,n}(q)=m+n-R_{m,n}(q)\).

There are two distinct asymptotic conclusions.

**Critical direct-voter density.** For each integer \(N\), let \(m_N/N\to\alpha>0\), \(n_N/N\to\beta>0\) and \(q_N\sqrt N\to c\in[0,\infty]\). Put \(\kappa=(1/\alpha+1/\beta)/8\). Then
\[
\frac{R_{m_N,n_N}(q_N)}{m_N+n_N}\longrightarrow
F_{\alpha,\beta}(c),
\]
where \(F(0)=0\), \(F(\infty)=1\), and for \(0<c<\infty\),
\[
F_{\alpha,\beta}(c)=c\int_0^\infty e^{-ct-\kappa t^2}\,dt
=\frac{c\sqrt\pi}{2\sqrt\kappa}
\exp\!\left(\frac{c^2}{4\kappa}\right)
\operatorname{erfc}\!\left(\frac{c}{2\sqrt\kappa}\right).
\]
In particular, on balanced networks \(m_N=n_N=N\), the limit is \(c\sqrt\pi e^{c^2}\operatorname{erfc}(c)\) for \(0<c<\infty\). Thus the scale \(q_N\asymp N^{-1/2}\) separates asymptotically vanishing representation from asymptotically complete representation.

**Fixed direct-voter density.** Along any sequence with \(m,n\to\infty\), if \(q\in(0,1)\) is fixed and \(m/n\to\rho\in(0,\infty)\), then
\[
L_{m,n}(q)\longrightarrow
\frac{r^2\left[2+r(\rho+\rho^{-1})\right]}{q^2(1+r)^2}.
\]
For balanced parts and \(q=1/2\), the limiting *total* expected number of lost voter-weights is \(4/3\), although the network size diverges.

## Assumptions and scope
Each voter chooses independently exactly once between direct voting and a single outgoing delegation; there is no revoting or adaptive cycle breaking. Every edge between the parts is available as a delegation edge in both directions, but edges within either part are unavailable. A voter is represented if their unique outgoing path reaches a direct ballot. If that path enters a directed cycle before reaching a direct ballot, the original voter's unit of weight is lost. We count represented *original voter-weights*, not the number of direct ballots and not correctness of a collective voting outcome. The underlying graph is fixed; only independent ballot/delegation choices are random. All asymptotic statements assume both parts grow proportionally to the common index \(N\).

## Proof
**Exact formula.** Fix a starting vertex in the \(m\)-part and reveal its unique delegation chain sequentially. Conditional on the previously visited distinct vertices, previously unseen vertices have independent, unexposed choices distributed as in the model. If the chain has visited \(j+1\) distinct \(m\)-part vertices (including the start) and \(j\) distinct \(n\)-part vertices, the next hop from the \(m\)-part avoids a repeated vertex with probability \((n-j)/n\). Conversely, from the \(n\)-part when \(j+1\) distinct \(m\)-part vertices have already appeared, avoiding a repeat has probability \((m-j-1)/m\). Therefore the probability of surviving \(2j\) delegation hops with no repeated vertex, conditional on all those voters delegating, is exactly \(A_{2j}\), and the analogous probability after \(2j+1\) hops is \(A_{2j+1}\). Reaching a direct voter after exactly \(t\) delegation hops has probability \(q r^t A_t\). These events are disjoint and exhaust all successful paths; the alternative is an eventual repeated vertex and hence a cycle. Summation proves \(H_{m,n}\); symmetry proves the expression for \(R\) and \(L\).

**Critical-window limit.** Let \(t=O(\sqrt N)\). For \(t=2j\), taking logarithms in the products above yields, uniformly for \(j/\sqrt N\) in compact intervals,
\[
\log A_{2j}=-\frac{j(j-1)}{2n_N}-\frac{j(j+1)}{2m_N}+o(1)
=-\kappa\frac{t^2}{N}+o(1).
\]
The same limit holds for odd \(t\). If \(0<c<\infty\), \(q_N\sqrt N\to c\) implies \(r_N^t\to e^{-ct/\sqrt N}\) on this scale. Consequently
\[
H_{m_N,n_N}(q_N)=q_N\sum_{t\ge0}r_N^t A_t
\longrightarrow c\int_0^\infty e^{-ct-\kappa t^2}\,dt.
\]
For the passage from bounded scaled ranges to the entire sum, use \(A_t\le\exp(-C t^2/N)\) for some \(C>0\) uniform for all relevant \(t\), since the falling-factorial collision hazards sum to at least a constant times \(t^2/N\). The tail is therefore uniformly dominated by a Gaussian integral. Interchanging the two part sizes gives the same limit because their only difference is an \(O(t/N)\) finite-size correction to the logarithm. Their weighted average establishes the limit for \(R/(m+n)\). Completing the square evaluates the displayed complementary-error-function expression.

For \(c=0\), the same Gaussian survival bound gives \(H_{m_N,n_N}\le C' q_N\sqrt N\to0\). For \(c=\infty\), the failure probability is bounded by the probability that a geometrically stopped path makes a repeated hop: a union bound gives \(1-H_{m_N,n_N}\le C''/(Nq_N^2)\to0\), because at step \(t\) at most \(t+1\) preceding vertices can be repeated, the opposite side has at least a fixed multiple of \(N\) vertices, and \(\sum_{t\ge0}(t+1)r_N^t=q_N^{-2}\). Thus both endpoint statements hold even if \(q_N\) does not tend to zero when \(c=\infty\).

**Fixed-density lost-vote limit.** Decompose the first failed hop according to its length; exactly
\[
1-H_{m,n}(q)=\sum_{j\ge0}\left[
  r^{2j+1}A_{2j}\frac{j}{n}
 +r^{2j+2}A_{2j+1}\frac{j+1}{m}
\right].
\]
The first term is a revisit on an attempted hop from the \(m\)-part to the \(n\)-part; the second is a revisit in the reverse direction. For fixed \(j\), both survival factors tend to one as \(m,n\to\infty\). Multiply by \(m\), apply dominated convergence using the geometric factor \(r^{2j}\), and use \(\sum_{j\ge0}j x^j=x/(1-x)^2\), \(\sum_{j\ge0}(j+1)x^j=(1-x)^{-2}\). This gives
\[
\lim m(1-H_{m,n})=
\frac{\rho r^3+r^2}{(1-r^2)^2}.
\]
The other side contributes \((\rho^{-1}r^3+r^2)/(1-r^2)^2\). Adding and using \(1-r^2=q(1+r)\) proves the announced expression.

## Verification
The standalone `verify.py` computes rational probabilities directly from the finite products, independently enumerates every direct/delegate choice profile for eight small bipartite networks, traces each chosen edge to a direct vote or a repeated vertex, and verifies both source-part survival probabilities and total mass. It checks both \(q=1/2\) and \(q=1/3\) at each network size. For \(m=n=3\) and \(q=1/2\), the exact survival probability of a specified voter is \(1123/1296\) and the expected total lost weight is \(173/216\). Its arithmetic checks do not replace the limiting arguments in the proof.

## Relationship to prior work
Transitive voting weights and the elimination of cycle-trapped delegations are pre-existing features of liquid-democracy models. Colley, Delemazure and Gilbert (2023) develop delegation-sensitive voting-power measures: their directed bipartite theorem assumes a one-way delegator-to-proxy graph (hence no alternating cycles), and their complete-digraph formulas concern a different underlying network and voter criticality. Berinsky and collaborators (2021) analyze stochastic delegation and weight concentration on more general models, but the inspected contributions do not give this two-way bipartite exact expected lost-weight distribution or the present direct-voter critical scaling. Utke and Schmidt-Kraepelin (2023) develop alternative, more robust delegation mechanisms, not the frozen-one-choice process solved here. The path-exposure/birthday-collision method itself is standard random-mapping probability theory. The specific claim is only the exact bipartite representation law, its square-root direct-voter transition, and the fixed-density loss constant; no priority claim is made for the general concepts.

## Limitations
The proof gives expectation, not concentration or the full distribution of lost weights. It does not address preferential or unequal-probability choices, ranked/deferred delegation, dynamic re-voting, multiple outgoing delegates, abstention policy, or non-bipartite graphs. General random mapping literature could contain equivalent statements under other terminology; the bibliographic comparison was not exhaustive. The model says nothing about voters' preference accuracy or majority outcomes. No independent validation has been performed.

## References
1. Colley, R., Delemazure, T., Gilbert, H., *Measuring a Priori Voting Power — Taking Delegations Seriously*, arXiv:2301.02462 (first publicly available January 6, 2023), https://arxiv.org/abs/2301.02462 .
2. Berinsky, A. J., Halpern, D., Halpern, J. Y., Jadbabaie, A., Mossel, E., Procaccia, A. D., Revel, M., *Tracking Truth with Liquid Democracy*, arXiv:2107.11868 (first publicly available July 25, 2021), https://arxiv.org/abs/2107.11868 .
3. Utke, J., Schmidt-Kraepelin, U., *Anonymous and Copy-Robust Delegations for Liquid Democracy*, arXiv:2307.01174 (first publicly available July 3, 2023), https://arxiv.org/abs/2307.01174 .
4. Brill, M. et al., *Liquid Democracy with Ranked Delegations*, AAAI 2022, https://ojs.aaai.org/index.php/AAAI/article/view/20428 .
5. Pitman, J., *Random mappings, forests, and subsets associated with Abel-Cayley-Hurwitz multinomial expansions*, Séminaire Lotharingien de Combinatoire 46 (2001), https://statistics.berkeley.edu/tech-reports/593 .
