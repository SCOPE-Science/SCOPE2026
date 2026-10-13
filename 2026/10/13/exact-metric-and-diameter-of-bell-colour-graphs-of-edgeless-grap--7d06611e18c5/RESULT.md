# Exact metric and diameter of Bell colour graphs of edgeless graphs
## Finding
For integers \(n\ge 1\) and \(1\le k\le n\), consider the Bell \(k\)-colour graph
\[
\mathcal B_k(\overline{K_n}),
\]
whose vertices are the partitions of an \(n\)-element set into at most \(k\) nonempty blocks. Two partitions are adjacent when one can be obtained from the other by changing the block of exactly one element, with a new singleton block permitted when the block bound is respected.

For partitions \(P\) and \(Q\), form the weighted bipartite graph whose two vertex classes are the blocks of \(P\) and \(Q\), and give a block pair \((A,B)\) weight \(|A\cap B|\). Define
\[
\mu(P,Q)=\max_M\sum_{(A,B)\in M}|A\cap B|,
\]
where \(M\) ranges over matchings between the two block families. Then the exact shortest-path metric is
\[
d_{\mathcal B_k(\overline{K_n})}(P,Q)=n-\mu(P,Q).
\]
In particular, the restriction to at most \(k\) blocks does not lengthen any shortest path: \(\mathcal B_k(\overline{K_n})\) is an isometric induced subgraph of the full Bell colour graph. Its diameter is
\[
\operatorname{diam}\mathcal B_k(\overline{K_n})
=n-\left\lceil\frac{n}{k}\right\rceil.
\]

## Assumptions and scope
All sets and graphs are finite. The graph \(\overline{K_n}\) is the edgeless graph on \(n\) vertices, so every set partition is a proper partition into independent sets. The parameter range is \(1\le k\le n\); for \(k\ge n\) the Bell colour graph is already the full graph and the same metric formula applies.

The result concerns the reconfiguration metric of Bell colour graphs, not the Hasse-diagram metric of the partition lattice. The maximum-matching quantity \(n-\mu(P,Q)\) is classical in clustering comparison under names including transfer distance, partition distance, and maximum matching distance. The new statement identified here is that this classical partition distance is exactly the graph distance in every truncated Bell graph \(\mathcal B_k(\overline{K_n})\), together with the isometry and exact diameter formula.

## Proof
Let a walk from \(P\) to \(Q\) have length \(t\). At most \(t\) distinct elements are moved, so at least \(n-t\) elements are never moved. Two never-moved elements that begin in the same block remain together, while two never-moved elements that begin in distinct blocks cannot end in the same block: merging their blocks would require moving an element from one of those blocks. Hence the never-moved elements induce a matching between blocks of \(P\) and blocks of \(Q\). Its total intersection weight is at least \(n-t\). Therefore
\[
n-t\le \mu(P,Q),
\qquad
t\ge n-\mu(P,Q).
\]

For the reverse inequality, pad the block families of \(P\) and \(Q\) with empty blocks until each has exactly \(k\) slots. Extend a maximum-weight matching realizing \(\mu(P,Q)\) to a bijection between these \(k\) slots. Use the paired slots as common temporary labels. Exactly \(\mu(P,Q)\) elements already have the same initial and target label; recolor every other element once to its target label. At every intermediate step there are at most \(k\) nonempty labels. After labels are forgotten, each recoloring either leaves the unlabeled partition unchanged or traverses one edge of \(\mathcal B_k(\overline{K_n})\). Removing repeated consecutive partitions gives a path of length at most \(n-\mu(P,Q)\). Combined with the lower bound, its length is exactly \(n-\mu(P,Q)\). This also proves the isometry assertion.

It remains to maximize this distance. Pad the two block families to \(k\) slots and view their intersection sizes as a \(k\)-by-\(k\) nonnegative integer matrix of total sum \(n\). If a uniformly random permutation of the columns is chosen, the expected weight of the corresponding perfect matching is \(n/k\). Hence
\[
\mu(P,Q)\ge \left\lceil\frac{n}{k}\right\rceil,
\]
so every distance is at most \(n-\lceil n/k\rceil\).

For equality, take \(Q\) to be the one-block partition and take \(P\) to have \(k\) blocks whose sizes differ by at most one. A matching can pair the sole block of \(Q\) with only one block of \(P\), so
\[
\mu(P,Q)=\max_{A\in P}|A|
=\left\lceil\frac{n}{k}\right\rceil.
\]
Thus the upper bound is attained and the diameter formula follows.

## Verification
The accompanying `verify.py` constructs every set partition for \(1\le n\le 6\), constructs Bell adjacency directly from one-element block changes, and for every \(1\le k\le n\) performs breadth-first search from every vertex of \(\mathcal B_k(\overline{K_n})\). It independently computes \(\mu(P,Q)\) by a dynamic-programming maximum-weight matching routine and checks every ordered pair against the formula above. It also checks the predicted diameter.

The replay output is recorded as:

`ALL CHECKS PASSED; n_max=6; bell_vertices_full=278; parameter_graphs=21; ordered_pair_checks=140668; diameter_checks=21`

The finite computation is a stress test only. The proof above establishes the statement for all \(n\) and \(k\) in the stated range.

## Relationship to prior work
Finbow and MacGillivray define the Bell \(k\)-colour graph using partitions into at most \(k\) independent sets and study its connectivity and Hamiltonicity. Their full text also proves a Cartesian-product rule for Bell graphs of graph joins. Their paper does not state a shortest-path metric or diameter formula.

Hearn studies reconstruction from Bell colouring graphs and gives structural results that recover the underlying graph from the reconfiguration graph in broad regimes. The inspected full preprint contains no theorem giving the metric above or the edgeless-graph diameter.

The matching expression itself is not claimed to be new. In the partition-comparison literature, the transfer or maximum matching distance is the minimum number of ground elements that must be moved between clusters, and it is computed by a maximum-weight matching on block intersections. The result here identifies that metric with Bell-graph shortest-path distance even after imposing the \(k\)-block cap, and derives the exact diameter of every truncated edgeless Bell graph.

## Limitations
The theorem treats the edgeless underlying graph. For a general graph, feasibility constraints on independent blocks can prevent the temporary labeled recolorings used in the proof, so neither the matching formula nor isometry is asserted beyond this family.

The originality comparison found the classical transfer-distance formula and treats it as prior coverage rather than novelty. The remaining originality risk is an older or differently indexed reconfiguration paper that may already identify the transfer metric with the at-most-\(k\)-block partition graph. No such statement was located in the Bell-colour, isomorphic-colour, partition-reconfiguration, or maximum-matching-distance searches performed here.

## References
1. S. Finbow and G. MacGillivray, *Hamiltonicity of Bell and Stirling Colour Graphs*, arXiv:2512.13864v1, first public version 15 December 2025; Utilitas Mathematica 127 (2026), 239--258.
2. B. Hearn, *Reconstructing a graph from its Bell colouring graph*, arXiv:2604.13005v1, first public version 14 April 2026.
3. G. Rossi, *Hamming distance between partitions, clustering comparison and information*, Proceedings of PMAMCM 2015, pp. 101--107, DOI:10.13140/RG.2.1.1654.8328.
