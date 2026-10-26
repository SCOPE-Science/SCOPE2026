# Four-cycle signatures in three-layer shuffled regular-graph occupancy

## Finding

Let \(G\) be any simple undirected \(2\)-regular graph on \(d\ge 7\) labeled vertices. Independently and uniformly relabel all vertex piles before each layer, then send every path along both graph edges. Start with one path at any fixed vertex. Write \(N_\ell(j)\) for the number of length-\(\ell\) paths ending at vertex \(j\), and \(Z_\ell=\#\{j:N_\ell(j)=0\}\). Let \(q(G)\) denote the number of connected components of \(G\) isomorphic to the four-cycle.

Put \(H=\binom d2\), \(\mu=(d-2)(d-3)/(d-1)\), and \(A=H\binom{d-4}{2}+d(d-4)\). The exact finite-layer identities are
\[
\mathbb E Z_2=\mu,\qquad
\operatorname{Var}(Z_2)=\frac{2(A+2q(G))}{H}+\mu-\mu^2,
\qquad
\mathbb E\left[\frac{Z_3}{d}\right]=\frac{A+2q(G)}{H^2}.
\]

Thus the second-layer mean is graph-independent, while its variance and the third-layer mean see **only** the number of four-cycle components. Among all such graphs of order \(d\), both quantities increase strictly with \(q(G)\). Their minima occur exactly for graphs with no four-cycle component; their maxima occur exactly when \(q(G)=q_{\max}(d)\), where \(q_{\max}(d)=\lfloor d/4\rfloor\) for \(d\equiv0,3\pmod4\) and \(q_{\max}(d)=\lfloor d/4\rfloor-1\) for \(d\equiv1,2\pmod4\).

The smallest graph order at which two such graphs can have different expected third-layer vacant fractions is \(d=7\). Indeed, the only two isomorphism types then are \(C_7\) and \(C_3\sqcup C_4\), for which
\[
\begin{array}{c|cc}
G & \operatorname{Var}(Z_2)&\mathbb E[Z_3/d]\\\hline
C_7 & 2/9 & 4/21\\
C_3\sqcup C_4 &26/63&86/441
\end{array}
\]
so the exact gaps are \(4/21\) in variance and \(2/441\) in the expected vacant fraction.

## Assumptions and scope

Every undirected edge is viewed as a pair of directed edges; there are no self-loops or multiple edges. Since \(G\) is simple, undirected, and two-regular, it is a disjoint union of cycles of lengths at least three. Before every path step, an **independent uniform permutation of all \(d\) labels** is applied globally to the entire pile vector (not independently to individual paths). Each outgoing graph edge then receives a copy of every path in its source pile. All expectations are over those independent permutations. The starting vertex is arbitrary. The quantity \(Z_3/d\) is the empirical mass at zero after exactly three layers, not a stationary quantity. The theorem holds for every integer \(d\ge7\), with no asymptotic assumption.

## Proof

After the first independent uniform relabeling, the initial path has exactly two distinct descendants. Therefore, immediately before the second graph layer, the two occupied unit piles lie at a uniformly chosen two-element subset \(S\subseteq[d]\). If \(N(v)\) is the two-element neighbor set of vertex \(v\), then
\[
N_2(v)=|S\cap N(v)|,\qquad Z_2=\sum_{v=1}^d\mathbf1\{S\cap N(v)=\varnothing\}.
\]
Each summand has expectation \(\binom{d-2}{2}/H\), hence \(\mathbb EZ_2=d\binom{d-2}{2}/H=\mu\).

For distinct target vertices \(a,b\), set \(k_{ab}=|N(a)\cap N(b)|\in\{0,1,2\}\). Their neighbor-set union has size \(4-k_{ab}\), so both are empty after layer two with probability
\[
\mathbb P(N_2(a)=N_2(b)=0)
=\frac{\binom{d-4+k_{ab}}2}{H}.
\]
Consequently,
\[
\mathbb E\binom{Z_2}{2}
=\frac1H\sum_{a<b}\binom{d-4+k_{ab}}2.
\]
Using \(\binom{u+k}{2}=\binom u2+uk+\binom k2\) and counting pairs of neighbors of each vertex gives \(\sum_{a<b} k_{ab}=d\). In a disjoint union of simple cycles, \(k_{ab}=2\) exactly for opposite vertices in a four-cycle component. Each such component gives two unordered pairs, hence \(\sum_{a<b}\binom{k_{ab}}2=2q(G)\). It follows that
\[
\sum_{a<b}\binom{d-4+k_{ab}}2=A+2q(G).
\]
The standard identity \(Z_2^2=2\binom{Z_2}{2}+Z_2\) now yields the stated variance.

Before layer three, a fresh uniform permutation relocates the second-layer piles. Conditional on the number \(Z_2\) of zero piles, the two prescribed incoming positions of any particular target both contain zero piles with probability \(\binom{Z_2}{2}/H\). By averaging over target vertices and then the second-layer process,
\[
\mathbb E[Z_3/d]
=\mathbb E\binom{Z_2}{2}/H
=\frac{A+2q(G)}{H^2}.
\]
There is no assumption that the positive piles are independent; only their global uniform permutation is used.

Every graph in the class is a partition of \(d\) into cycle lengths at least three. The minimum \(q=0\) is attained by the single cycle \(C_d\). The largest allowable number of four-cycle components is the greatest nonnegative integer \(q\) for which \(d-4q\) is zero or at least three. This gives the displayed formula for \(q_{\max}(d)\) and all equality cases (the remaining cycle lengths can be any partition of the residual into integers at least three). The coefficient of \(q\) is positive in each graph-sensitive identity.

For \(d\le6\), there are no two isomorphism types with different four-cycle counts: a four-cycle may occur only at \(d=4\), when the graph is uniquely \(C_4\). At \(d=7\), the partitions \(7\) and \(4+3\) have different counts, proving the claimed sharp onset. Substitution establishes the stated rational values.

## Verification

The standalone file `verify.py` independently enumerates all two-element subsets representing the second-layer occupied support, reconstructs all zero indicators, and enumerates all possible incoming two-element subsets for the third layer. It uses `fractions.Fraction` throughout. For every cycle partition of each \(d\in\{7,\ldots,17\}\), it checks the exact mean, variance, third-layer empty fraction, four-cycle count, and extremal range. It separately checks the two seven-vertex examples and both gaps. The recorded run in `verify_output.txt` reports 579 exact rational assertions passing. Run with `python verify.py` in the same directory. These finite tests are corroboration; the proof above establishes the formula for unbounded \(d\).

## Relationship to prior work

Chiclana, *Poisson occupancy of paths on permuted regular graphs* (arXiv:2610.14724, first public 2026-10-10), studies exactly the independent-layer-permutation path model, proving geometry-independent Poisson limits and exact quadratic contraction identities for doubly stochastic products. Those results are the starting point here. The present finite-depth calculation identifies the first structural cycle motif that survives random relabeling in vacant-site fluctuations and, one layer later, in the expected vacant fraction. The graph-sensitive \(d=7\) comparison shows why a geometry-independent quadratic norm identity does not itself prescribe the empirical mass at zero. This calculation neither strengthens nor disputes the paper's asymptotic Poisson theorem.

## Limitations

The classification concerns undirected simple two-regular graphs, a single initial path, independent full uniform permutations, and exactly two or three layers. It does not classify other graph degrees, higher-order occupancy statistics, or long-time distributions. The exact graph effect on \(\mathbb E[Z_3/d]\) is small for large \(d\), and no universal finite-size error lower bound for general regular graphs is claimed. The result is not externally or independently certified; a specialized earlier finite-layer identity may exist.

## References

1. Rafael Chiclana, *Poisson occupancy of paths on permuted regular graphs*, arXiv:2610.14724 (2026), first public 2026-10-10, https://arxiv.org/abs/2610.14724.
2. Luca Avena, Remco van der Hofstad, Frank den Hollander, and Oliver Nagy, *Mixing of fast random walks on dynamic random permutations* (2024), for context on dynamic-permutation models; the random-transposition dynamics differ from independent full-permutation path products.
