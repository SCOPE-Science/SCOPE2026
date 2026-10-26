# First-excitation connectivity and Petersen bridges among dodecahedral bisections

## Finding

Let \(D=GP(10,2)\) be the dodecahedral graph. A **bisection** is an unordered partition \(\{S,V(D)\setminus S\}\) with \(|S|=10\). Its cost \(c(S)\) is the number of edges with one endpoint on each side. Two bisections are **swap-adjacent** if one representative side is obtained from the other by replacing exactly one selected vertex with one unselected vertex (up to complementation).

The exact minimum cost is \(6\), and precisely **ten** bisections attain it. These are exactly the radius-two vertex balls \(B_2(v)\), with \(B_2(v)\) and \(B_2(v')\) representing the same bisection precisely when \(v,v'\) are antipodal (distance \(5\)). No two minimum bisections are swap-adjacent.

The graph \(X\) of all bisections with cost at most \(8\), joined by swaps that remain within this cost bound, has exactly \(340\) vertices (ten of cost \(6\), 330 of cost \(8\)), \(2520\) edges, and is connected, with radius \(5\) and diameter \(6\). Its eccentricities are \(5\) at \(280\) states and \(6\) at \(60\) states.

Construct a graph \(J\) on the ten minimum bisections, joining two when they can be connected by **two swaps** through a cost-\(8\) bisection. Then \(J\) is the Petersen graph \(\operatorname{KG}(5,2)\). Each edge of \(J\) admits exactly four distinct cost-\(8\) intermediate bisections; no nonedge admits one. Within \(X\), the minimum-to-minimum distances are \(2\) for the fifteen edges of \(J\), and \(4\) for the other thirty pairs. Therefore \(2\) is the **minimum and sufficient additional cut budget** to connect all optima, and four swaps suffice between any pair of optima within that budget.

The scalar minimum cost \(6\) and the abstract antipodal Petersen quotient have precedents in the literature; the contribution is the full optimum classification and the sharp cost-constrained exchange geometry.

## Assumptions and scope

Use vertices \(u_i=i\) and \(v_i=10+i\) for \(i\in\{0,\ldots,9\}\), indices modulo \(10\), and exactly the \(30\) edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+2}\). The graph is simple and undirected. Distances in \(D\) are ordinary graph distances. Bisections are **unlabeled**: \(\{S,S^c\}\) is one state, and each state has the unique representative with \(u_0\in S\). Swap moves preserve side size \(10\), and the budget constraint applies to **every intermediate state**. The two-step graph \(J\) is different from the ordinary one-step graph of minimum bisections, which has no edges. All claims concern exactly \(D\), not arbitrary generalized Petersen graphs or other fullerene graphs.

## Proof

**Exhaustive bisection principle.** Fixing \(u_0\in S\), all unordered bisections are represented once by the \(\binom{19}{9}=92378\) subsets obtained by selecting nine further vertices. For each subset, calculate the exact integer
\[
c(S)=\sum_{\{a,b\}\in E(D)}|\mathbf1_S(a)-\mathbf1_S(b)|=30-2|E(D[S])|.
\]
The second equality follows because \(D\) is cubic and \(|S|=10\). In particular all possible costs are even. The complete histogram \(c\mapsto\#\{S:c(S)=c\}\), calculated by a fully specified enumeration, is
\[
\begin{array}{c|rrrrrrrrrr}
c&6&8&10&12&14&16&18&20&22&24\\\hline
\#&10&330&2232&10560&22680&27330&18760&8166&2190&120.
\end{array}
\]
There are no entries of lower cost. The supplied verifier recomputes this table twice: once by examining all \(30\) edges for each canonical subset, and independently by examining the induced degrees in all \(\binom{20}{10}=184756\) oriented subsets. Thus the exact bound and ten optimal states follow without assuming an optimizer or extrapolating a sample.

**Geometric classification.** In \(D\) the distance-layer sizes from every vertex are \((1,3,6,6,3,1)\). Consequently every radius-two ball has ten vertices. The exhaustive verification calculates its boundary, equal to \(6\), and shows that the twenty balls yield ten distinct unordered bisections, the equality of two canonical representatives occurring exactly for their two antipodal centers. Since the previous count established exactly ten optima, this lists all of them.

**Cost-eight exchange graph.** Generate all \(340\) states with \(c\le8\). For each canonical state, enumerate its \(10\cdot10=100\) selected-to-unselected swaps and retain precisely those whose destination cost remains at most \(8\). The verifier reconstructs the adjacency **independently** by testing every pair of the \(340\) states for symmetric-difference size \(2\) or \(18\) (complement-equivalent size \(2\)); the two adjacency sets agree. This gives \(2520\) undirected edges, of which \(300\) join levels \(6\) and \(8\), and \(2220\) join two level-\(8\) states. No edge joins two minima. Breadth-first search from **every** state establishes connectedness and the eccentricity counts, hence radius \(5\) and diameter \(6\). These are exhaustive searches on a graph whose every state and transition was already constructed.

**Petersen bridge certificate.** Index the ten optimal bitmasks in increasing order. The numbers of common cost-eight neighbors are either \(4\) (exactly fifteen pairs) or \(0\) (thirty pairs). The verifier provides the following explicit bijection, in that increasing-mask order, to the two-subsets of \(\{0,1,2,3,4\}\):
\[
01,\ 23,\ 04,\ 12,\ 24,\ 03,\ 14,\ 13,\ 02,\ 34.
\]
Here \(ab\) denotes the two-element subset \(\{a,b\}\), **not** a two-digit integer. Every one of the fifteen pairs with four intermediate configurations maps to disjoint two-subsets, and every other pair maps to intersecting two-subsets. This is a complete, directly checked adjacency certificate for \(J\cong\operatorname{KG}(5,2)\). All-pairs breadth-first search in \(X\) gives distances \(2\) and \(4\) in exactly the stated multiplicities. Finally, since no one-step move preserves cost \(6\), a budget below \(8\) cannot connect distinct minima; since \(X\) is connected, budget \(8\) suffices. Thus the budget excess \(2\) is sharp.

## Verification

From this package run `python3 verify.py` with Python 3.9 or later; only the standard library is needed. The script constructs the graph by the three modular edge rules, enumerates every balanced partition in two independent ways, constructs both versions of the swap graph, checks all radius-two balls and the explicit Petersen labeling, and performs complete shortest-path calculations. It exits with `VERIFY_OK` if and only if all its assertions pass. The bounded enumeration is the finite proof component; no numerical approximation, random search, optimization timeout, or inference from test samples is used.

## Relationship to prior work

Bollobás and Scott explain balanced partitioning as a classical extremal graph problem. Cygan, Lokshtanov, Pilipczuk, Pilipczuk and Saurabh provide a general parameterized algorithm for Minimum Bisection, without the particular optimum set or low-cost swap geometry of this graph. Abiad and collaborators report the dodecahedral isoperimetric number \(i(D)=0.6\); their value implies that a size-ten side has at least six crossing edges, so **the scalar optimum is not asserted to be new**. Waller describes the known antipodal two-cover from the dodecahedral graph to the Petersen graph; thus **the abstract quotient and its ten vertices are not asserted to be new**. The new comparison concerns which balanced partitions are optimal, which states become reachable after the smallest cost increase, exact reconfiguration distances, and four-fold two-step passages realizing the known abstract quotient. None of the inspected relevant primary material determines this complete constrained exchange landscape.

## Limitations

This is a complete finite classification for one twenty-vertex graph, **not** a general theorem about all Platonic or generalized Petersen graphs, nor a fast algorithm for arbitrary Minimum Bisection. The result uses an exhaustive computer-checkable finite proof; the complete Python code is part of the result. No independent audit or globally exhaustive novelty certification has been performed. An unindexed earlier computation of the dodecahedral cut landscape remains possible. The already published scalar isoperimetric value and antipodal quotient must not be cited as independent new contributions.

## References

1. B. Bollobás and A. D. Scott, *Problems and results on judicious partitions*, Random Structures & Algorithms 21 (2002), 414–430, https://people.maths.ox.ac.uk/scott/Papers/judprob.pdf .
2. M. Cygan, D. Lokshtanov, M. Pilipczuk, M. Pilipczuk and S. Saurabh, *Minimum Bisection is Fixed Parameter Tractable*, arXiv:1311.2563 (2013), https://arxiv.org/abs/1311.2563 .
3. A. Abiad et al., *The edge-isoperimetric number of graphs and their powers*, arXiv:2601.17519 (2026), especially Appendix Table A4, https://arxiv.org/abs/2601.17519 .
4. D. A. Waller, *Double covers of graphs*, Bulletin of the Australian Mathematical Society, https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/double-covers-of-graphs/4C6C74E71345E1C2C1048853BF638F4D .
5. E. Weisstein, *Dodecahedral Graph*, MathWorld, https://mathworld.wolfram.com/DodecahedralGraph.html .
