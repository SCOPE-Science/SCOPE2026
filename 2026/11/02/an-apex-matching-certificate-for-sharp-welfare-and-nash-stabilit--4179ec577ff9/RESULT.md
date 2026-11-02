# An apex-matching certificate for sharp welfare and Nash stability in simple fractional hedonic games

## Finding

Let \(H\) be any finite simple graph on \(m\ge 2\) vertices, with maximum degree at most two and no cycles of lengths three or four. Its cycles, if any, therefore have length at least five. Form \(G=K_1\vee H\) by adjoining a new universal vertex \(h\). In the *simple symmetric fractional hedonic game*, every partition \(\Pi\) of \(V(G)\) assigns each vertex \(v\) in its coalition \(C_v\) utility
\[
u_v(\Pi)=\frac{|N_G(v)\cap C_v|}{|C_v|},\qquad
\operatorname{SW}(\Pi)=\sum_{v\in V(G)}u_v(\Pi).
\]

**Apex-matching theorem.** Every partition satisfies the sharp universal bound
\[
\operatorname{SW}(\Pi)\le\frac m2+1.
\]
Equality holds **if and only if** the hub's coalition is either \(\{h\}\cup V(Q)\), for an edge \(Q=K_2\) of \(H\), or \(\{h\}\cup V(Q)\), for a three-vertex induced path \(Q=P_3\) of \(H\), and every other coalition is a two-vertex edge. Equivalently, the vertices of \(H-V(Q)\) are paired by a perfect matching. **Every equality partition is a Nash equilibrium** against arbitrary individual moves to another existing coalition or to a new singleton.

Writing \(\operatorname{pm}(J)\) for the number of perfect matchings of a graph \(J\) (one for the empty graph), the exact number of partitions attaining the bound is
\[
N_{\mathrm{sharp}}(H)=\sum_{Q\in E(H)}\operatorname{pm}(H-V(Q))
+\sum_{Q\in\mathcal P_3(H)}\operatorname{pm}(H-V(Q)),
\]
where \(\mathcal P_3(H)\) is the set of distinct induced three-vertex paths. In particular, \(\max_\Pi\operatorname{SW}(\Pi)=m/2+1\) **exactly when** this integer is positive; in that case the price of Nash stability equals one. If it vanishes, the welfare optimum is strictly below the bound (no claim is made here about its exact lower value).

**Canonical consequences.** For a fan \(F_m=K_1\vee P_m\), \(m\ge2\), the maximum welfare is \(m/2+1\), every optimum is Nash stable, and the number of optima is \(\lfloor m/2\rfloor\). For a wheel \(W_m=K_1\vee C_m\), \(m\ge5\), the same maximum welfare and stability hold, with exactly \(m\) optimal partitions. At the excluded short wheels, \(W_3=K_4\) has a unique welfare-maximizing grand coalition with welfare \(3\), and \(W_4\) has a unique welfare-maximizing grand coalition with welfare \(16/5\); these too are Nash stable.

## Assumptions and scope

The underlying simple graph \(H\) can be disconnected, and isolated vertices are permitted. The hypothesis excludes triangles and four-cycles *inside \(H\)*, not inside \(G\), which may have many triangles via \(h\). All friendship edge values in \(G\) are exactly one, all nonedges zero, and individual utilities use coalition size—including the player—as denominator. No negative weights, directed valuations, non-unilateral stability notion, or restrictions on the number or connectedness of coalitions are imposed. An optimal partition is labeled by its actual vertex sets; rotations of a wheel count as different partitions.

A Nash deviation may move a single vertex from its coalition into any other existing coalition or a newly formed singleton; it must strictly improve that vertex's utility. Price of stability here means the ratio of maximum possible social welfare to the maximum social welfare of a Nash-stable partition.

## Proof

**1. Coalition inequalities.** For any coalition \(C\), the total payoff contributed by its members is exactly \(2e_G(C)/|C|\), by counting each internal edge twice. Fix a partition. If \(R\subseteq V(H)\) is a coalition of size \(r\) not containing \(h\), then for \(r=1,2,3,4\) it contains at most \(0,1,2,3\) edges, respectively, since \(H\) has no triangles or four-cycles. For \(r\ge5\), the degree bound gives \(e_H(R)\le r\). In each case,
\[
\frac{2e_H(R)}r\le\frac r2,
\]
with equality only for \(r=2\) when the vertices are adjacent. Indeed, for \(r\ge5\) the left side is at most \(2<r/2\).

Let the unique coalition containing \(h\) be \(C=\{h\}\cup S\), with \(s=|S|\). Because \(h\) has exactly \(s\) incident edges inside \(C\), this coalition contributes
\[
\frac{2(s+e_H(S))}{s+1}.
\]
For \(s=0,1,2,3,4\), the respective upper bounds are \(0,1,2,5/2,14/5\). Each is at most \(1+s/2\), with equality precisely when \(s=2\) and \(H[S]\) is one edge, or \(s=3\) and \(H[S]\) is a path with two edges. For \(s\ge5\), using \(e_H(S)\le s\),
\[
\frac{2(s+e_H(S))}{s+1}\le\frac{4s}{s+1}
<1+\frac s2,
\]
since \(s^2-5s+2>0\) at every integer \(s\ge5\). Summing the inequalities for disjoint coalitions proves \(\operatorname{SW}(\Pi)\le(m-s)/2+(1+s/2)=m/2+1\).

Equality in this sum requires equality in every component inequality: the hub coalition is a hub-plus-edge or a hub-plus-induced-path, and all other coalitions are edges forming a perfect matching of the remaining vertices. Conversely, every such partition attains equality, since the hub coalition yields \(2\) when \(s=2\), or \(5/2\) when \(s=3\), and every outside pair yields \(1\). The two types of hub coalition and the accompanying matching uniquely determine the partition. This gives the displayed exact count and matching-certificate equivalence.

**2. Stability.** First suppose \(s=2\). The hub and the two rim vertices each earn \(2/3\), while all other vertices earn \(1/2\) in their matched pairs. The hub, moving to any pair, would earn \(2/3\), not a strict gain. A selected rim vertex has at most one neighbor outside the selected edge because \(\Delta(H)\le2\), so entering any outside pair yields at most \(1/3\). An outside matched vertex has at most one neighbor among the two selected endpoints because \(H\) is triangle-free. It would earn at most \(2/4=1/2\) after moving to the hub coalition (one contribution from the hub and at most one from \(H\)). It can earn at most \(1/3\) when entering any other pair, since a common neighbor of the pair would form a triangle in \(H\).

Now suppose \(s=3\). The hub and the middle vertex of the chosen path earn \(3/4\), its endpoints each earn \(1/2\), and outside matched vertices earn \(1/2\). Any selected path vertex has at most one neighbor outside that path, so joining another pair yields at most \(1/3\). The hub could receive only \(2/3\) by joining a pair. An outside vertex is adjacent to at most one of the three path vertices, for two such adjacencies would create a triangle or four-cycle within \(H\); hence entering the hub coalition gives at most \(2/5\). Joining another pair yields at most \(1/3\). A move to a singleton always gives zero, which improves none of these positive utilities. Therefore **every** equality partition is Nash stable.

**3. Fans and wheels.** On \(P_m\), parity forces the chosen hub motif to be an edge when \(m\) is even or a three-vertex path when \(m\) is odd. The remaining path segments have perfect matchings precisely when the motif starts at an odd-numbered vertex along the path, and these matchings are unique. There are \(m/2\) such edges in the even case and \((m-1)/2\) such three-vertex paths in the odd case. On \(C_m\), \(m\ge5\), deleting any edge if \(m\) is even, or any consecutive three-vertex path if \(m\) is odd, leaves a single even-order path with one perfect matching, producing exactly \(m\) distinct optima.

For the exceptional wheels, \(W_3=K_4\) has welfare \(3\) in the grand coalition and every proper partition has smaller welfare. In \(W_4\) the five-vertex grand coalition has eight edges and welfare \(16/5\). Every proper partition has largest block of size at most four: a \(2+3\) split contributes at most \(1+2=3\); a \(4+1\) split contributes at most \(2\cdot5/4=5/2\); all further splits contribute at most \(3\). Hence the grand coalition is uniquely optimal. Any grand coalition in a nonnegative-valuation game is Nash stable, since departing alone yields zero.

## Verification

The exact executable checks `verify.py` enumerate every set partition and every unilateral move for fan bases of orders \(2\) through \(9\) and wheel bases of orders \(3\) through \(9\), verifying the claimed welfare, exact count, and Nash stability of *all* optima. The second checker, `verify_general.py`, tests all \(50\) eligible non-isomorphic base graphs of orders \(2\) through \(7\) from the NetworkX graph atlas, including disconnected cases. It independently counts edge- and path-deletion perfect matchings and checks both directions of the sharpness criterion as well as stability for all sharp partitions. Both programs use exact rational arithmetic and finite exhaustive enumeration. Run `python verify.py` and `python verify_general.py` after installing dependencies from `requirements.txt`. These finite tests are corroboration, **not** a replacement for the proof for arbitrary \(m\).

## Relationship to prior work

Hanaka, Ikeyama and Ono (arXiv:2310.05139v1) introduce algorithms for maximum utilitarian welfare of fractional hedonic games on tree-like graphs, including a bounded-treewidth approach; their results establish computability for the present graph families but do not state the matching-certificate equality characterization, the exact fan/wheel counting, or stability of every welfare optimum. Bilò and coauthors (JAIR 62, 2018) establish that every optimal outcome on a **tree** is Nash stable; the apex graphs here contain triangles whenever \(H\) has an edge, so this theorem does not subsume the present claim. Bazgan, Casel and Cazals (arXiv:2107.13282) show the equivalent dense-graph-partition objective and results for degree-at-most-two input graphs and very dense input graphs; \(K_1\vee H\) is generally neither a degree-at-most-two graph nor covered by their minimum-degree bound.

## Limitations

This theorem characterizes *attainment of the sharp upper bound*, not the exact optimum for arbitrary bases lacking a matching certificate. Cycles of length three or four in the base invalidate critical induced-edge bounds; the only short wheels treated separately are \(W_3\) and \(W_4\). The result does not extend automatically to signed, weighted, asymmetric or directed games, to strong Nash/core stability, or to dynamics converging to the optimal partition. Published and indexed literature comparisons are not a proof of absolute priority; an unindexed or differently phrased classification remains possible.

## References

1. T. Hanaka, A. Ikeyama, H. Ono, *Maximizing Utilitarian and Egalitarian Welfare of Fractional Hedonic Games on Tree-like Graphs*, earliest arXiv version 2023-10-08, https://arxiv.org/abs/2310.05139.
2. V. Bilò, A. Fanelli, M. Flammini, G. Monaco, L. Moscardelli, *Nash Stable Outcomes in Fractional Hedonic Games: Existence, Efficiency and Computation*, Journal of Artificial Intelligence Research 62 (2018), 315–371, https://doi.org/10.1613/jair.1.11211.
3. C. Bazgan, K. Casel, P. Cazals, *Dense Graph Partitioning on Sparse and Dense Graphs*, arXiv:2107.13282 (2021), https://arxiv.org/abs/2107.13282; SWAT 2022, https://doi.org/10.4230/LIPIcs.SWAT.2022.13.
4. H. Aziz, S. Gaspers, J. Gudmundsson, J. Mestre, H. Täubig, *Welfare Maximization in Fractional Hedonic Games*, IJCAI 2015, https://ijcai.org/proceedings/2015/71.
