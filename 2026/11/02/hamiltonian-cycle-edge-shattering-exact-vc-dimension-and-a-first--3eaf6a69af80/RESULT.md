# Hamiltonian-cycle edge shattering: exact VC dimension and a first adaptive gap

## Finding

For every integer \(n\ge3\), let \(\mathcal H_n\) be the Boolean concept class of undirected Hamiltonian cycles of the labeled complete graph \(K_n\), with one binary edge-membership query for each unordered vertex pair. Then
\[
\operatorname{VCdim}(\mathcal H_n)=
\begin{cases}
0,&n=3,\\
1,&n=4,\\
n-2,&n\ge5.
\end{cases}
\]
The Littlestone dimensions for \(n=3,4,5,6\) are respectively \(0,1,3,5\). Thus \(n=6\) is the first order at which the two dimensions differ: \(\operatorname{VCdim}(\mathcal H_6)=4\) and \(\operatorname{Ldim}(\mathcal H_6)=5\).

For each integer \(s\ge1\), fix \(s\) labeled, mutually disjoint six-vertex groups, and let \(\mathcal P_s\) consist of the unions of one chosen Hamiltonian cycle within every group. The query universe is the union of the within-group edge sets (edges between groups are not queries). Then
\[
\operatorname{VCdim}(\mathcal P_s)=4s,\qquad
\operatorname{Ldim}(\mathcal P_s)=5s.
\]
This provides an unbounded separation for a natural componentwise Hamiltonian-cycle selection model. No assertion is made that the disjoint union is itself one Hamiltonian cycle on all vertices.

## Assumptions and scope

All graphs are finite, labeled, simple and undirected. A hypothesis is the edge set of an undirected spanning cycle, with reversal identified. A query asks whether one specified edge occurs in the hypothesis. VC dimension is the maximum size of a fixed edge-query support realizing every Boolean labeling. Littlestone dimension is the maximum depth of a complete, realizable adaptive query tree (with distinct queried edges along each root-to-leaf path automatically permitted; queries may vary between branches). Dimension zero means that no query admits both answers.

## Proof

**Lemma: prescribed adjacencies of a spanning path.** Let \(m\ge4\) and let \(S=\{\{1,2\},\{2,3\},\ldots,\{m-1,m\}\}\). Every assignment of positive and negative labels to these \(m-1\) edges is realized by a Hamiltonian path in \(K_m\).

Indeed, a prescribed set of positive edges divides the ordered vertices into \(k\) nonempty, consecutive path-blocks. Each block must be traversed contiguously, in either direction. Only the edges between originally adjacent blocks are prohibited, and only their original endpoints can form the forbidden edge. If \(k=1\), the original spanning path works. If \(k\ge4\), order the blocks by even indices in ascending order, followed by odd indices in ascending order. Neighboring block indices then never differ by one, so all inter-block edges avoid the prohibited set. If \(k=2\), at least one block has size at least two (since \(m\ge4\)); orient it so that the sole inter-block edge is different from the prohibited original boundary edge. If \(k=3\), at least one block has size at least two. Choose an ordering with exactly one originally neighboring pair, incident to such a nonsingleton block: for a nonsingleton first block use order \(2,1,3\); otherwise use \(1,3,2\) if the third block is nonsingleton, and \(1,3,2\) also if the middle block is nonsingleton. Orient the nonsingleton member to avoid that one prohibited boundary edge; the other inter-block adjacency is between originally non-neighboring blocks. Concatenation proves the lemma.

**Static dimension.** For \(n\ge5\), take the \(n-2\) consecutive edges of a spanning path on vertices \(1,\ldots,n-1\), leaving vertex \(n\) outside the queried support. By the lemma with \(m=n-1\), every labeling is realized by a Hamiltonian path on the first \(n-1\) vertices. Joining vertex \(n\) to both endpoints closes this path into a Hamiltonian cycle without changing its trace on the queried edges. Thus the VC dimension is at least \(n-2\).

Conversely, if \(n-1\) queried edges were shattered, their all-positive labeling would be contained in a Hamiltonian cycle. Such a set of \(n-1\) cycle edges is a spanning path. Choose an endpoint edge \(e\) of this path. Requiring all the remaining \(n-2\) queried edges to be positive leaves a fixed spanning path on \(n-1\) vertices and one isolated vertex. Any Hamiltonian cycle containing that fixed path must join the isolated vertex to both its endpoints, forcing \(e\) positive. Hence the labeling with only \(e\) negative is impossible, a contradiction. Larger shattered supports would contain a shattered \((n-1)\)-subset. For \(n=3\), the sole undirected Hamiltonian cycle gives dimension zero. For \(n=4\), there are three cycles: one edge can be positive or negative, while two queries cannot be shattered because that would require four hypotheses.

**Adaptive dimension through six vertices.** The number of Hamiltonian cycles in \(K_n\) is \((n-1)!/2\). Every complete adaptive tree of depth \(d\) has at least \(2^d\) distinct hypotheses, so \(\operatorname{Ldim}(\mathcal H_4)\le1\) and \(\operatorname{Ldim}(\mathcal H_5)\le3\). Their VC lower bounds give equality, and \(\operatorname{Ldim}(\mathcal H_3)=0\).

For \(n=6\), the standalone file `cycle_depth5_certificate.json` contains a complete binary decision tree of depth five: all 31 internal nodes specify an edge query, and all 32 leaves specify explicit six-vertex cyclic orders. For each leaf, its cycle realizes exactly the binary answers recorded along the root-to-leaf path. These 32 exact witnesses prove \(\operatorname{Ldim}(\mathcal H_6)\ge5\). Since \(|\mathcal H_6|=60<64\), a depth-six tree cannot exist, establishing equality.

**Componentwise amplification.** For concept classes on disjoint query domains, VC dimensions add: a shattered support splits into shattered supports in each domain, and independent choices realize every product labeling. Littlestone dimensions also add. The lower bound follows by concatenating adaptive witness trees. For the upper bound, on each component run an optimal deterministic realizable online learner; its number of mistakes is at most that component's Littlestone dimension. On interleaved queries, the total number of mistakes is therefore bounded by the sum. The minimax characterization of Littlestone dimension by optimal realizable mistake bound proves the upper bound. Applying these facts to \(s\) copies of \(\mathcal H_6\) gives the displayed formulas.

## Verification

`check_hamiltonian_cycle_gap.py` independently enumerates Hamiltonian cycles as permutations with the initial vertex fixed and reversals identified, generates every edge-label trace on supports for \(3\le n\le6\), and computes Littlestone dimension by the exact recursion
\[
L(C)=\max_{e\text{ splitting }C}\bigl(1+\min\{L(C_{e=0}),L(C_{e=1})\}\bigr),
\]
with \(L(C)=0\) for an unsplittable version space. The program separately validates the explicit depth-five certificate, checking the edges and every root-to-leaf binary constraint instead of relying on recorded dimension values. Running `python check_hamiltonian_cycle_gap.py cycle_depth5_certificate.json` reproduces `verification_output.txt` and ends with `ALL_HAMILTONIAN_CYCLE_GAP_CHECKS_PASS`. These computations confirm small orders; the all-order VC formula and product additivity are proved mathematically, not extrapolated from enumeration.

## Relationship to prior work

Manurangsi (arXiv:2211.01443, first publicly submitted November 2, 2022) develops general hardness of approximating VC and Littlestone dimensions of explicitly given concept classes; its inspected introduction and principal theorems concern reductions from biclique problems, not Hamiltonian-cycle edge-membership classes. Coudert, Csikós, Ducoffe and Viennot (SEA 2024) explicitly work with *closed vertex-neighborhood* set systems, not edge sets of Hamiltonian cycles. Kranakis, Krizanc, Ruf, Urrutia and Woeginger (1997) investigate graph-defined VC set systems including some path and cycle families. Its abstract does not settle whether the present complete-graph Hamiltonian-cycle model is covered; full-text comparison was unavailable and remains a substantive historical-priority risk.

Related existing mathematical records include general matroid-basis shattering, Hamiltonian-*path* edge-incidence shattering, and the edge-incidence class of all spanning two-factors of \(K_6\). The last has 70 hypotheses and the same pair of dimensions \((4,5)\), but it includes disconnected two-factors; this finding supplies a depth-five tree using only the 60 connected Hamiltonian cycles, and an all-order VC formula for this more constrained class. Neither the numerical coincidence nor the earlier theorem proves the connected-cycle lower bound without the certificate.

## Limitations

The exact Littlestone formula is established only for orders three through six. No claim is made about higher-order adaptive dimensions, all shattered supports, or full historical priority. The infinite-family assertion concerns independently chosen cycles in prescribed components, not all Hamiltonian cycles of a connected graph. The possibly relevant 1997 graph-set-system study was not inspected in full. Independent scientific review is not claimed here.

## References

1. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443 (first submitted 2022-11-02), https://arxiv.org/abs/2211.01443.
2. D. Coudert, M. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, SEA 2024, DOI 10.4230/LIPIcs.SEA.2024.8, https://doi.org/10.4230/LIPIcs.SEA.2024.8.
3. E. Kranakis, D. Krizanc, B. Ruf, J. Urrutia and G. J. Woeginger, *The VC-dimension of set systems defined by graphs*, Discrete Applied Mathematics 77 (1997), 237–257, DOI 10.1016/S0166-218X(96)00137-0. Full-text priority comparison remains unresolved.
