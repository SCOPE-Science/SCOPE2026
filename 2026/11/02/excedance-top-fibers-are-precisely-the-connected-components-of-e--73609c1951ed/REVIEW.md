# Scientific review of excedance-top fiber connectivity

## Correctness — PASS

The local swap rule is an exact indicator identity at positions \(i,i+1\): the excedance number is unchanged if and only if neither exchanged value equals \(i+1\). It separately preserves each moved value's excedance status. Every proposed top-value subset has an explicit feasible canonical representative, and every adjacent inversion in the ordering defined by this representative is a legal swap. Bubble sort therefore proves connectivity of every fiber and the component formula. The characterization of isolated representatives is checked at each boundary. The edge identity follows from a degree count and two deletion bijections. Exhaustive independent permutation-graph implementations test \(n\le9\). Their success corroborates but is not the infinite proof.

## Originality — PASS, subject to literature risk

The inspected 2000 paper of Ehrenborg and Steingrímsson treats sets of excedance *indices* and their enumeration; it does not supply the top-value reconfiguration graph. Steingrímsson and Williams' 2005 tableaux paper develops refined weak-excedance bijections, not connectivity under statistic-preserving neighboring transpositions. The 2014 paper of Baril–Mansour–Petrossian specifies individual excedance positions and values; that equivalence is finer, so its counting statements do not establish the present connectivity of coarser top-value fibers. The 2011 adjacent-transformations paper studies pattern rules that do not depend on the absolute boundary value. Actual searches of the research-record index for excedance-top fibers, Eulerian strata, adjacent-transposition connectivity, and corresponding aliases returned no stronger covering theorem. Residual risk remains for an unindexed reconfiguration treatment or an equivalent constrained-permutation theorem.

## Value — PASS

The result gives a complete structural classification for the natural Eulerian-number layers of the permutahedron, which fragment into exponentially many components under the classical permutation statistic. The constructive canonical-path argument resolves reachability; the isolation result finds a unique frozen state at each cardinality; the explicit edge formula quantifies permitted local dynamics. These go beyond recomputation of Eulerian coefficients or an isolated example.

## Limits

No exact internal diameter or individual component-size formula is claimed. Some fibers are not geodesically convex in the full permutahedron. Independent scholarly validation has not been performed, and alternative-literature novelty remains a risk.

Self-review: passed. Independent audit: not yet performed.
