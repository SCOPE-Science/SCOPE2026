# Exact equilibrium-selection and fixation-time laws for asynchronous best-shot play on complete bipartite networks

## Finding

**Theorem (extinction lottery and sharp random-update clock).** Let \(a,b\ge 1\), set \(N=a+b\), and let \(0\le i\le a\), \(0\le j\le b\) be the initial numbers of producers in the two parts of \(K_{a,b}\). At each tick an independently uniform vertex replaces its action with its unique best response: produce if and only if none of its neighbors produces. Then almost surely play reaches one of two pure Nash equilibria, \(P_A\) (everyone in the first part produces) or \(P_B\) (everyone in the second part produces).

If \(i,j>0\), the exact selection probabilities are
\[
\Pr(P_A)=\frac{i}{i+j},\qquad \Pr(P_B)=\frac{j}{i+j}.
\]
For \(1\le k\le i\), the joint probability that \(P_A\) is selected and exactly \(k\) original first-part producers remain at the moment the second part loses its last producer is
\[
 w^A_k=\frac{\binom{i+j-k-1}{j-1}}{\binom{i+j}{j}}.
\]
Similarly, for \(1\le\ell\le j\), the joint probability of \(P_B\) and \(\ell\) surviving original second-part producers is
\[
 w^B_\ell=\frac{\binom{i+j-\ell-1}{i-1}}{\binom{i+j}{i}}.
\]
Let \(H_0=0\) and \(H_m=\sum_{r=1}^m 1/r\) for positive integers \(m\). If \(S\) is the number of scheduled vertex selections until a pure Nash equilibrium is first attained (including selections that leave the action unchanged), then for \(i,j>0\),
\[
\boxed{\mathbb E[S]=(a+b)\left[H_i+H_j-H_{i+j}+\sum_{k=1}^i w^A_k H_{a-k}+\sum_{\ell=1}^j w^B_\ell H_{b-\ell}\right].}
\]
The exact boundary cases are
\[
\begin{aligned}
\mathbb E[S\mid i>0,j=0]&=(a+b)H_{a-i},\\
\mathbb E[S\mid i=0,j>0]&=(a+b)H_{b-j},\\
\mathbb E[S\mid i=j=0]&=1+aH_{a-1}+bH_{b-1}.
\end{aligned}
\]
The selected equilibrium is certain on the already occupied side when just one side has initial producers; for the all-zero start, \(\Pr(P_A)=a/(a+b)\).

More explicitly, in the equivalent system with independent rate-one Poisson update clocks, let \(\tau\) be the first time one of two initially occupied parts has no producers. For \(i,j>0\),
\[
\Pr(\tau>t)=[1-(1-e^{-t})^i][1-(1-e^{-t})^j]\quad(t\ge0),\qquad \mathbb E\tau=H_i+H_j-H_{i+j}.
\]
For balanced all-producing initial profiles \(a=b=i=j=m\), the discrete-time expected fixation time satisfies the sharp asymptotic
\[
\boxed{\mathbb E[S]=4m\log m+(4\gamma-2\log 2)m+o(m),}
\]
where \(\gamma\) is Euler's constant.

## Assumptions and scope

The graph is a labeled, simple, undirected complete bipartite graph with nonempty parts. Actions are binary. Every vertex has the **strict, homogeneous best-shot response** \(T(0)=1\) and \(T(q)=0\) for each integer \(q\ge1\), based on the number of producing **neighbors, excluding itself**. A tick chooses one of all \(N\) vertices uniformly and independently, *with replacement*. The step count includes null updates; the first time a pure equilibrium is reached is the stopping time. Initial profiles are deterministic but arbitrary within the stated counts. There are no independent action mistakes, strategic experimentation, or simultaneous revisions.

## Proof

**Equilibria.** If both parts contain producers then no such producer is currently best responding; if neither part contains a producer then all vertices want to produce. If exactly one part contains producers, all its other vertices want to produce and every vertex of the other part wants to stay inactive. Therefore the only equilibria are \(P_A\) and \(P_B\).

**Extinction lottery.** While both parts contain at least one producer, every inactive vertex stays inactive when selected, while each producing vertex turns inactive upon its **first** selection. Hence the only state-changing selections before a part empties are the first selections of the \(i+j\) initially producing vertices. Their first-selection order is a uniform random permutation, because all vertices have identical selection probabilities. One side empties when its final original producer is selected; the other side retains the producers in the terminal, uninterrupted suffix of the permutation. The probability that this suffix consists of exactly \(k\) first-part producers (preceded by a last second-part producer) is the number \(\binom{i+j-k-1}{j-1}\) of feasible placements of the remaining second-part producers among the preceding positions divided by all \(\binom{i+j}{j}\) part-label permutations. This gives \(w^A_k\); the other expression follows by symmetry. The last member of a random permutation is equally likely to be any initially producing player, proving \(\Pr(P_A)=i/(i+j)\). Notice that \(\sum_k w^A_k=i/(i+j)\), and likewise for the other side.

**Clock until commitment.** Equip each vertex with an independent rate-one Poisson clock. Their union has rate \(N\), and its independent uniform vertex marks reproduce exactly the discrete process. Each original producer's first update time is independent exponential of rate one. For a set of \(r\) such times, the maximum has cumulative distribution \((1-e^{-t})^r\) and expectation \(H_r\). Commitment occurs at the **minimum** of the maximum first-update times from the two sides. Independence gives the displayed survival function. Because the minimum of two numbers is their sum minus their maximum, and the maximum over both groups has expectation \(H_{i+j}\), the exact mean is \(H_i+H_j-H_{i+j}\).

**Clock after commitment.** If the first part wins with \(k\) surviving original producers, every one of its other \(a-k\) vertices is inactive and has no producing neighbor. It activates at its first update after commitment, stays active thereafter, and every vertex in the losing part stays inactive. By the independent-increments and memorylessness properties of Poisson processes, the remaining activation waiting times are independent rate-one exponentials, with expected maximum \(H_{a-k}\). This depends only on \(k\), even when some vertices were selected previously. The corresponding mean for the second part is \(H_{b-\ell}\). Average over the joint suffix probabilities and add the commitment expectation. Since the rate-\(N\) inter-event spacings are independent of uniform vertex marks, the mean number of discrete steps to an absorbing state equals \(N\) times the mean continuous time, proving the principal formula. If one side initially has no producers, its other side can only gain producers and the additional expected continuous time is the maximum of the \(a-i\) or \(b-j\) required rate-one first updates. If both sides are initially empty, the first selected vertex activates and decides the eventual winning side; conditioning on that first choice proves all boundary formulas.

**Balanced large-network law.** For \(a=b=i=j=m\), symmetry gives \(\mathbb E[S]/(2m)=2H_m-H_{2m}+\mathbb E[H_{m-K}\mid P_A]\), where \(K\) is the number of surviving first-part producers on the event \(P_A\). The conditional tail obeys
\[
\Pr(K\ge k\mid P_A)=2\frac{(m)_k}{(2m)_k}\le 2^{1-k}\quad(1\le k\le m),
\]
where \((r)_k=r(r-1)\cdots(r-k+1)\). In particular, \(\mathbb E[K\mid P_A]=O(1)\), and, splitting at \(K=m/2\), \(H_m-\mathbb E[H_{m-K}\mid P_A]=o(1)\) (the low tail costs at most \(2K/m\); the high tail is exponentially small times \(H_m\)). Therefore the continuous-time mean equals \(3H_m-H_{2m}+o(1)\). Using \(H_m=\log m+\gamma+o(1)\) and \(H_{2m}=\log(2m)+\gamma+o(1)\) yields \(2\log m+2\gamma-\log2+o(1)\). Multiplication by \(2m\) proves the asymptotic.

## Verification

The standalone standard-library script `verify.py` independently constructs (1) the proposed closed formulas for probabilities and expected scheduled steps and (2) the two absorbing Markov first-step recurrences. It checks equality with exact rational arithmetic for every \(1\le a,b\le8\) and every \(0\le i\le a\), \(0\le j\le b\), a total of \(1936\) state configurations, and checks that the suffix weights sum to the corresponding win probabilities. Run `python3 verify.py` from the same directory; the expected line begins `PASS: 1936 exact rational states`. These are finite corroborations, **not** proofs of the arbitrary-size statements. The combinatorial and probabilistic arguments above supply the infinite proof.

## Relationship to prior work

Klimm and Stahlberg (arXiv:2301.11849, public January 27, 2023) establish general existence and convergence of best responses for decreasing binary public-goods patterns, including the present strict pattern. Dall'Asta, Pin and Ramezanpour (arXiv:1002.3572) define the best-shot game, identify its equilibria as maximal independent sets and study a different socially steered simulated-annealing procedure. Ramazi, Riehl and Cao (2016) analyze convergence of asynchronous coordination and anti-coordination games more broadly. The present claim concerns the **random, with-replacement scheduler from any fixed initial action profile** on complete bipartite graphs, giving its exact absorbing-state law, survivor-count distribution, mean hitting time and balanced asymptotics. A published exact random-order greedy maximal-independent-set law on chain graphs already covers the **empty-start equilibrium-selection distribution** on complete bipartite graphs. Its random single-pass acceptance mechanism does not analyze arbitrary nonempty producer configurations or the number of repeated random updates required for all producers to stabilize. The empty-start selection probability is not asserted to be new. No priority or exhaustive literature-uniqueness claim is made.

## Limitations

Exact formulas do not automatically carry to nonuniform update rates, stochastic mistakes, other graph classes, simultaneous play, different best-response thresholds, or rules selecting only currently dissatisfied agents. Existing general convergence results already imply qualitative convergence here. The mathematical contribution is quantitative, and specialist precedence is possible. Independent external validation has not been performed.

## References

1. M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, arXiv:2301.11849 (initial public posting January 27, 2023), https://arxiv.org/abs/2301.11849.
2. L. Dall'Asta, P. Pin and A. Ramezanpour, *Optimal equilibria of the best shot game*, arXiv:1002.3572 (2010), https://arxiv.org/abs/1002.3572.
3. P. Ramazi, J. R. Riehl and M. Cao, *Networks of conforming or nonconforming individuals tend to reach satisfactory decisions*, Proceedings of the National Academy of Sciences (2016), https://pmc.ncbi.nlm.nih.gov/articles/PMC5135341/.
4. M. I. Jones, S. D. Pauls and F. Fu, *The dual problems of coordination and anti-coordination on random bipartite graphs*, (2021), https://pmc.ncbi.nlm.nih.gov/articles/PMC9165663/.
5. *Exact random-greedy maximal-independent-set law on chain graphs*, publicly available mathematical study, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-random-greedy-maximal-independent-set-law-on-chain-graphs--36fe61ce32de.
