# Minimum resolving-set mobility separates two cospectral strongly regular graphs

## Finding

Let \(R=K_4\square K_4\) be the sixteen-vertex rook graph. Let \(S\) be the Shrikhande graph on \(\mathbb Z_4^2\), adjacent at differences in \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\). Both graphs are strongly regular with parameters \((16,6,2,2)\), and both have metric dimension four. A **metric basis** is a four-vertex set whose distance vectors distinguish all sixteen vertices.

For a graph \(G\), write \(J(G)\) for the graph of metric bases joined when one landmark is replaced by another, and \(T(G)\) for the subgraph of such moves in which the removed and inserted landmarks are adjacent in \(G\). Write \(J_2(G)\) for the graph of metric bases joined when exactly two landmarks are replaced, that is, when the bases have intersection of size two. Then

\[
J(R)=T(R)\cong\bigsqcup_{16} H(2,3),\qquad J(S)=T(S)\cong48K_1.
\]

Here \(H(2,3)=K_3\square K_3\). Thus the rook graph has exactly \(144\) metric bases and its one-replacement graph consists of sixteen connected nine-vertex components, whereas the Shrikhande graph has exactly \(48\) metric bases and every basis is frozen under any single landmark replacement.

In contrast, \(J_2(R)\) is connected, \(26\)-regular on \(144\) vertices with diameter three, and \(J_2(S)\) is connected, \(10\)-regular on \(48\) vertices with diameter three. Therefore **six is the least capacity** that allows every pair of minimum resolving sets to be connected by additions and deletions of one landmark while every intermediate set remains resolving: capacity five is insufficient for either graph. In the capacity-six system, any two bases can be connected in at most twelve elementary add/delete operations. The two graphs share the same strongly regular parameters and metric dimension, but their minimum-basis mobility is radically different.

## Assumptions and scope

All graphs are finite, undirected, and simple. Vertices of both graphs are identified with pairs \((x,y)\) whose coordinates belong to \(\{0,1,2,3\}\); the Shrikhande adjacency uses arithmetic modulo four. Distances are ordinary shortest-path distances. A set \(B\) resolves \(G\) exactly when the tuples \((d_G(v,b))_{b\in B}\) are distinct for distinct vertices \(v\). A one-landmark replacement retains the cardinality four and is allowed only when its result also resolves \(G\).

For capacity \(c\), the add/delete graph has as states all resolving subsets of at most \(c\) vertices, joined by addition or deletion of exactly one vertex. The connectivity assertion concerns **all metric bases within that graph**. It does not assert that the graph of all feasible configurations is connected at capacity five; in fact, it is not. The claim concerns precisely these two labeled graph isomorphism types; it is not an assertion about every strongly regular graph.

## Proof

**1. Minimum cardinalities.** The dimension-four values are established in the cited literature: Cáceres et al. prove \(\beta(K_4\square K_4)=4\), and Bailey tabulates \(\beta(S)=4\). For independent verification, both included programs enumerate all sets of one, two, and three landmarks and verify that none resolves either graph. They also exhibit the four-landmark families described below. These are complete finite checks, not extrapolations.

**2. Rook-graph bases and one-replacement components.** Cáceres et al., Lemma 6.2, characterize resolving sets in products of complete graphs by empty rows/columns and lonely selected cells. Applying its three conditions to a four-cell set in the four-by-four board forces exactly three occupied rows and three occupied columns, each with occupancy pattern \((2,1,1)\), with the double row and double column not intersecting at a selected cell. Conversely every such configuration resolves the graph by that lemma.

More explicitly, for any row \(r\), column \(c\), excluded row \(u\ne r\), and excluded column \(v\ne c\), define

\[
B_{r,c;u,v}=\{(r,y):y\notin\{c,v\}\}\ \cup\ \{(x,c):x\notin\{r,u\}\}.
\]

Every rook-graph basis is uniquely of this form. There are \(4\cdot4\cdot3\cdot3=144\) choices. Each such basis consists of two sites in row \(r\) and two sites in column \(c\), with their intersection \((r,c)\) unselected. A one-element replacement cannot change the unique double row or double column: removing a site in one pair leaves the other pair intact, while making one of its occupied rows/columns into a new double would create a forbidden occupied intersection. Hence every replacement keeps \((r,c)\) fixed and changes only \(u\) or \(v\). Conversely every change of either excluded coordinate yields another basis. The nine choices of \((u,v)\) with fixed \((r,c)\) therefore induce \(K_3\square K_3\). Each such move changes a selected site to another site on the same row or column, so it is also a token slide in \(R\). No edges join different \((r,c)\), giving exactly sixteen components and \(16\cdot18=288\) exchange edges.

**3. Shrikhande bases and one-replacement isolation.** In the coordinate model, three representative four-sets are

\[
\begin{aligned}
U_1&=\{(0,0),(0,1),(2,0),(2,3)\},\\
U_2&=\{(0,0),(0,2),(1,0),(3,2)\},\\
U_3&=\{(0,0),(0,2),(1,1),(3,1)\}.
\end{aligned}
\]

The complete family of metric bases consists exactly of their \(\mathbb Z_4^2\)-translates. Each translation family has sixteen members and the families are disjoint, giving \(48\) bases. Moreover any two distinct members of their union intersect in at most two vertices; thus no one-replacement move exists. These assertions have a finite, explicit certificate: for each of the \(\binom{16}{4}=1820\) four-sets, and each of the \(\binom{16}{2}=120\) pairs of vertices, the independent checker tests whether at least one chosen landmark distinguishes that pair. It asserts equality of the complete set of successful masks with the three translation families and directly checks all pairwise overlaps. A separate checker uses all sixteen full distance signatures rather than pair-separation masks. Both source files are supplied and terminate successfully.

**4. Exactly two replacements restore connectivity.** The graph \(J_2(G)\) has an edge precisely when two four-sets share two vertices. The two included independent verifiers build these graphs directly from the complete basis families: for \(R\), every vertex has degree \(26\), the graph has \(1872\) edges, and every vertex has eccentricity three; for \(S\), every vertex has degree \(10\), the graph has \(240\) edges, and every vertex has eccentricity three. Breadth-first traversal from every basis verifies the absence of disconnected states and checks both diameter claims. These are finite exhaustive calculations over \(144\) and \(48\) vertices respectively.

The resolving-set property is monotone under addition. If bases \(B,C\) share two vertices, add the two vertices of \(C\setminus B\) to \(B\), then delete the two vertices of \(B\setminus C\). Every intermediate set contains \(B\) or \(C\) and is resolving, and its size never exceeds six. A path of at most three edges in \(J_2\) therefore gives at most twelve add/delete steps.

At capacity five, any path between two cardinality-four states alternates between cardinalities four and five; two consecutive distinct cardinality-four states must share three vertices. Hence its paths among metric bases lie entirely within components of \(J(G)\). Since \(J(R)\) has sixteen components and \(J(S)\) has forty-eight, capacity five does not connect all bases. Since no resolving set has fewer than four vertices, the same is true at every lower capacity. This proves the sharp capacity-six threshold.

## Verification

The standalone standard-library Python files `verify_direct.py` and `verify_characterization.py` are complete; neither reads any external data. Run them respectively with `python3 verify_direct.py` and `python3 verify_characterization.py`. Their expected outputs are embedded as `verify_direct.out` and `verify_characterization.out`.

The direct verifier constructs the two distance matrices from their adjacency definitions; checks all vertex degrees and every common-neighbor count; enumerates \(\sum_{k=1}^{4}\binom{16}{k}\) candidate sets per graph; constructs the single-jump and single-slide graphs; checks their exact degree and component profiles; and calculates all eccentricities in the two-replacement graphs by complete breadth-first searches.

The independent verifier constructs graph edges differently, computes shortest-path distances by breadth-first search, and encodes resolution as a covering condition on the \(120\) unordered vertex-pair tests. It checks the explicit rook-graph formula and the complete three-orbit Shrikhande classification by enumerating all four-subsets, then recomputes the two-replacement statistics using bitmasks. These bound and exhaust the search spaces; no heuristic, random sample, or time-limited search is used. Both terminate with success markers. Those markers are reproducibility evidence only, not an independent external audit.

## Relationship to prior work

Cáceres et al. (2005 preprint; 2007 journal) determine metric dimension of \(K_n\square K_m\) and give the general empty-row/column and lonely-vertex resolving-set characterization. In particular the four-by-four rook metric dimension, its shape-of-basis classification, and hence the count \(144\) already follow from their Lemma 6.2. Those facts alone are **not** presented as new. Bailey (2013 preprint) tabulates the metric dimension four for both the Shrikhande and rook graphs, without providing the paired one-replacement and two-replacement reconfiguration classification established here.

The distinctive contribution is the explicit **contrast** \(16H(2,3)\) versus \(48K_1\) under minimum-basis exchanges and the sharp common capacity-six restoration proved by the two-replacement graphs. The calculations separate a set-exchange property from metric dimension and from the shared strongly regular parameter set. Related work on reconfigurations of metric bases exists, including the project/thesis by Morentin; its complete text could not be inspected, and exact overlap with unindexed material remains a residual originality risk. No implication of novelty is drawn merely from a failed search.

## Limitations

This is an exact finite-graph result, not an infinite-family theorem. The Shrikhande classification and both two-exchange diameters rely on transparent exhaustive finite verification, with two differently formulated checkers, rather than a complete human-only classification argument. The ordinary rook-graph metric dimension and resolving-set criterion are existing results and are not novelty claims. Search and accessible-text checks do not rule out unpublished or unindexed equivalent computations. Independent external scientific audit has not been performed.

## References

1. J. Cáceres, C. Hernando, M. Mora, I. M. Pelayo, M. L. Puertas, C. Seara, D. R. Wood, *On the Metric Dimension of Cartesian Products of Graphs*, arXiv:math/0507527, first posted 2005-07-26; SIAM J. Discrete Math. 21 (2007), 423–441. See Lemma 6.2 and Theorem 6.1. https://arxiv.org/abs/math/0507527
2. R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, arXiv:1312.4973, first posted 2013-12-17. See Section 3 and Table 1. https://arxiv.org/abs/1312.4973
3. J. Morentin, *Reconfigurations of Metric Bases*, thesis/project metadata, California State University institutional repository; complete text not available in the inspected access route. https://scholarworks.calstate.edu/concern/projects/pv63g4914
