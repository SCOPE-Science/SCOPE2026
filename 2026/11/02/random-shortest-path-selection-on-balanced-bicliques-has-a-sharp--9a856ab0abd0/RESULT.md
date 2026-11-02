# Random shortest-path selection on balanced bicliques has a sharp coupon-coverage threshold

## Finding

**Theorem (random strong-geodetic routing).** Fix an integer \(N\ge2\) and the complete bipartite graph \(K_{N,N}\), with parts \(L\) and \(R\). Fix any \(a\) vertices in \(L\) and any \(b\) vertices in \(R\), with \(0\le a,b\le N\). Between every unordered pair of fixed terminals choose, independently and uniformly, one of its shortest paths; paths between opposite parts are the unique edges. Let \(\mathcal C_{N;a,b}\) be the event that the union of all chosen paths and all terminals covers all vertices. Put
\[
Q_N(h,t)=\sum_{j=0}^{h}(-1)^j\binom hj\left(1-\frac jN\right)^t,
\]
with the usual convention \(0^0=1\). Then the exact finite-size reliability is
\[
\boxed{\Pr(\mathcal C_{N;a,b})=Q_N\!\left(N-b,\binom a2\right)\,Q_N\!\left(N-a,\binom b2\right).}
\]

Fix \(c\in\mathbb R\). For every sufficiently large \(N\), take the same terminal count in each part,
\[
a_N(c)=\left\lfloor\sqrt{2N(\log N+c)}\right\rfloor.
\]
Then the numbers of uncovered nonterminals in the two parts converge jointly to independent Poisson random variables of mean \(e^{-c}\). In particular,
\[
\boxed{\lim_{N\to\infty}\Pr(\mathcal C_{N;a_N(c),a_N(c)})=\exp(-2e^{-c}).}
\]
More generally, for a fixed \(\lambda>0\) and \(a_N=\lfloor\lambda\sqrt{2N\log N}\rfloor\),
\[
\lim_{N\to\infty}\Pr(\mathcal C_{N;a_N,a_N})=
\begin{cases}0,&0<\lambda<1,\\1,&\lambda>1.\end{cases}
\]

The smallest balanced terminal count allowing **some deliberately chosen geodesics** to cover the graph, by contrast, is
\[
\boxed{a_N^{\mathrm{exist}}=\left\lceil\frac{\sqrt{8N+1}-1}{2}\right\rceil.}
\]
Therefore asymptotically reliable **independent uniform geodesic assignment** has a terminal budget a factor \(\sqrt{\log N}\) larger than optimized geodesic assignment. This separation concerns random routing for *fixed terminals*; it does not assert a new value for the conventional strong geodetic number.

## Assumptions and scope

Graphs are finite, simple, undirected. Every path selected for an unordered terminal pair is shortest in the original graph. Choices are mutually independent and uniform among shortest paths for that pair, not conditioned on previous choices; terminals are fixed in advance. Paths for pairs of terminals in opposite parts have no internal vertices. For terminals in the same part there are exactly \(N\) shortest two-edge paths, each indexed by its distinct middle vertex in the other part. All logarithms are natural. The limit holds along integers \(N\to\infty\), with stated fixed real parameters; no claim of uniformity in moving \(c\) or \(\lambda\) is made.

## Proof

**Path-to-occupancy bijection.** A pair of terminals in \(L\) is distance two and has precisely the \(N\) vertices of \(R\) as possible middle vertices; terminal pairs in \(R\) behave symmetrically. Independent shortest-path choices thus generate \(\binom a2\) independent uniform draws from the \(N\) vertices of \(R\), and independently \(\binom b2\) draws from \(L\). A terminal is covered regardless of the route choices. Hence covering \(R\) is equivalent to the first sample hitting all \(N-b\) nonterminal vertices, while covering \(L\) is equivalent to the independent second sample hitting all \(N-a\) nonterminal vertices. Inclusion–exclusion over the omitted nonterminals in each part gives the two factors \(Q_N\), including all degenerate endpoints \(a,b\in\{0,1,N\}\).

**Poisson window.** Put \(a=a_N(c)\) and \(m=\binom a2\). The floor and quadratic expansion imply \(m=N(\log N+c)+o(N)\) and \(a=o(N)\). Let \(U_R\) count the nonterminal vertices of \(R\) missed by all \(m\) independent midpoint draws from \(L\). For each fixed nonnegative integer \(r\), falling-factorial moments are exactly
\[
\mathbb E[(U_R)_r]=(N-a)_r\left(1-\frac rN\right)^m\longrightarrow e^{-cr}.
\]
Indeed \((N-a)_r/N^r\to1\) and \(m\log(1-r/N)=-r\log N-rc+o(1)\). These are the factorial moments of \(\mathrm{Poisson}(e^{-c})\); the standard factorial-moment convergence theorem for nonnegative integer-valued random variables yields \(U_R\Rightarrow\mathrm{Poisson}(e^{-c})\). The same calculation holds for \(U_L\), which is independent of \(U_R\) for every \(N\), because it uses a disjoint family of path choices. Joint convergence therefore gives \(\Pr(U_L=U_R=0)\to\exp(-2e^{-c})\).

**Sharp first-order threshold.** For \(a=\lfloor\lambda\sqrt{2N\log N}\rfloor\), we have \(m/N=\lambda^2\log N+o(1)\). Thus \(\mathbb E U_R=(N-a)(1-1/N)^m=N^{1-\lambda^2+o(1)}\). When \(\lambda>1\), Markov's inequality yields \(\Pr(U_R>0)\to0\), and likewise for \(U_L\). When \(0<\lambda<1\), the expectation diverges and the exact factorial second-moment identity
\[
\mathbb E[(U_R)_2]=(N-a)(N-a-1)(1-2/N)^m
\]
gives \(\operatorname{Var}(U_R)/(\mathbb E U_R)^2\to0\). Chebyshev's inequality yields \(\Pr(U_R=0)\to0\), hence full coverage fails with probability tending to one.

**Optimal-vs-random comparison.** Deliberate choices cover the \(N-a\) nonterminal vertices on one side exactly when the \(\binom a2\) available geodesics through that side can be assigned so each nonterminal occurs as a midpoint at least once, equivalently \(\binom a2\ge N-a\). The choices on opposite sides are independent, so for balanced counts this condition is necessary and sufficient. Solving \(a(a+1)\ge2N\) gives the displayed least integer. Its asymptotic value \(\sqrt{2N}(1+o(1))\), compared with \(\sqrt{2N\log N}(1+o(1))\) at random-routing success, proves the factor \(\sqrt{\log N}\).

## Verification

A standalone Python standard-library checker `verify_random_routes.py` independently reconstructs the graph adjacency and verifies the complete list of shortest paths. It enumerates all independent midpoint assignments for 47 finite parameter triples with \(2\le N\le4\), checking the exact formula against brute-force vertex coverage, including asymmetric terminal counts and degenerate cases. It also checks the exact probabilities \(1/9\) for \((N,a,b)=(3,2,2)\) and \(1369/4096\) for \((4,3,3)\). The limit law is proved by factorial moments and inequalities above; finite checks alone cannot establish it.

## Relationship to prior work

Iršič's 2017 analysis of the strong geodetic problem on complete bipartite graphs already gives the deterministic midpoint-capacity criterion and extremal terminal selection (arXiv:1708.02416v1). Iršič and Konvalinka (arXiv:1806.00302v1) and Gledel and Iršič (arXiv:1810.04004v1) further analyze deterministic complete-bipartite and crown-graph strong geodetic parameters. The present result does not re-claim those results; its object is the coverage reliability when *each terminal pair independently draws a random shortest path*, including a sharp two-sided Poisson window and quantitative price of this randomness. The probabilistic proof uses standard coupon-collector methods, credited as such; the contribution is the exact graph-routing correspondence and its mathematical implication for random versus optimized geodesic coverage. A 2022 strong geodetic recognition complexity article (arXiv:2208.01796v1) treats a different question. Literature-priority searches did not locate the exact randomized path assignment theorem; failure to find it is not proof of global novelty.

## Limitations

The model assumes independent uniform route choices and fixed equal-sized parts; it does not address optimal randomized routing, correlated geodesics, random terminal locations, or arbitrary graphs. The asymptotic Poisson limit is proved for fixed \(c\) only, and the zero–one threshold for fixed \(\lambda\ne1\). The probability estimate is exact for every finite \(N,a,b\), while claims of publication priority remain subject to specialized earlier routing/coupon-collector literature. No external independent mathematical audit is claimed.

## References

1. V. Iršič, *Strong geodetic number of complete bipartite graphs and of graphs with specified diameter*, arXiv:1708.02416v1 (first public 2017-08-08), https://arxiv.org/abs/1708.02416.
2. V. Iršič and M. Konvalinka, *Strong geodetic problem on complete multipartite graphs*, arXiv:1806.00302v1 (2018-06-01), https://arxiv.org/abs/1806.00302.
3. V. Gledel and V. Iršič, *Strong geodetic number of complete bipartite graphs, crown graphs and hypercubes*, arXiv:1810.04004v1 (2018-10-09), https://arxiv.org/abs/1810.04004.
4. C. V. G. C. Lima et al., *On the Computational Complexity of the Strong Geodetic Recognition Problem*, arXiv:2208.01796v1 (2022-08-03), https://arxiv.org/abs/2208.01796.
5. A. Boneh and M. Hofri, *The coupon-collector problem revisited: a survey of engineering problems and computational methods*, Stochastic Models 13 (1997), 39–66, doi:10.1080/15326349708807412 (standard occupancy background, not asserted priority evidence for graph routing).
