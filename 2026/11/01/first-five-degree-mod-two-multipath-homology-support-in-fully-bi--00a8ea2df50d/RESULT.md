# First five-degree mod-two multipath homology support in fully bidirected wheel graphs

## Finding

The multipath complexes of completely bidirected wheel graphs exhibit five distinct nonvanishing reduced mod-two homology degrees for the first time at the wheel with ten rim vertices. In the notation below, the complete result is
\[
\widetilde H_j(X_{10};\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^{49}, & j=5,\\
\mathbb F_2^{40}, & j=6,\\
\mathbb F_2^{40}, & j=7,\\
\mathbb F_2^{42}, & j=8,\\
\mathbb F_2^{20}, & j=9,\\
0, & \text{otherwise}.
\end{cases}
\]
No wheel with between three and nine rim vertices has nonzero reduced mod-two homology in five distinct degrees. The complete finite census is:

| Rim length | Number of faces, including empty | Nonzero reduced \(\mathbb F_2\)-Betti numbers \(j\mapsto\widetilde\beta_j\) |
|---:|---:|---|
| 3 | 73 | \(1\mapsto7,\ 2\mapsto6\) |
| 4 | 261 | \(2\mapsto19,\ 3\mapsto8\) |
| 5 | 871 | \(2\mapsto2,\ 3\mapsto23,\ 4\mapsto10\) |
| 6 | 2,783 | \(3\mapsto29,\ 4\mapsto26,\ 5\mapsto12\) |
| 7 | 8,597 | \(4\mapsto43,\ 5\mapsto30,\ 6\mapsto14\) |
| 8 | 25,865 | \(4\mapsto37,\ 5\mapsto32,\ 6\mapsto34,\ 7\mapsto16\) |
| 9 | 76,171 | \(5\mapsto71,\ 6\mapsto36,\ 7\mapsto38,\ 8\mapsto18\) |
| 10 | 220,395 | \(5\mapsto49,\ 6\mapsto40,\ 7\mapsto40,\ 8\mapsto42,\ 9\mapsto20\) |

## Assumptions and scope

Fix an integer \(3\le r\le10\). Let \(C_r\) be the simple undirected cycle with rim vertices \(0,\ldots,r-1\), including the triangle when \(r=3\); adjoining a hub \(h=r\), joined to every rim vertex, gives \(W_{r+1}=C_r*K_1\). Replace each undirected edge by both directed arcs, with no loops and no multiple copies. The resulting digraph \(D_r\) has \(r+1\) vertices and \(4r\) arcs. The standard multipath complex \(X_r=X(D_r)\) is a simplicial complex on these arcs. A face is an arc set for which each connected nontrivial component is a simple directed path, including paths of length one; equivalently every vertex has selected indegree and outdegree at most one, and no directed cycle is selected. An isolated vertex of the original digraph does not contribute a vertex to the complex. Chains and Betti numbers below are over the field \(\mathbb F_2\), and \(\widetilde H_0\) means reduced homology.

## Proof

**Finite face characterization.** First, the indegree/outdegree and directed-cycle conditions in the definition are necessary and sufficient for a selected arc set to be a vertex-disjoint union of directed paths. They are hereditary under arc deletion. For a recursion through the \(4r\) labeled arcs, store for each graph vertex its selected indegree and outdegree, and a bitset of its current directed reachability. For an arc \(a\to b\), the include branch is permitted precisely when \(a\) has no outgoing selected arc, \(b\) has no incoming selected arc, and no path already runs from \(b\) to \(a\). In that case, update reachability from each predecessor of \(a\) to each successor of \(b\). Branching on both inclusion and exclusion for every arc enumerates every face exactly once. The script `verify_bidirected_wheels.py` implements this algorithm in `directed_faces`.

**Independent characterization.** In a selected multipath, forgetting arrowheads produces an undirected forest of paths: degree at most two, and no cycle. Conversely, orient each nontrivial connected path in one of its two consistent directions. This is a bijection between directed multipaths and oriented undirected path forests. The routine `undirected_path_faces` enumerates **all** undirected edge subsets with degree at most two and no union-find cycle, and then both orientations of each path component. It does not invoke the directed-arc reachability algorithm. Equality of the two complete face sets, including the empty face, is asserted for each \(r=3,\ldots,10\).

**Exact homology calculation.** For every nonempty face \(\sigma\) containing \(d+1\) arcs, form its degree-\(d\) simplicial chain basis vector. Over \(\mathbb F_2\), its boundary is the sum of the \(d+1\) faces obtained by deleting one arc. For each \(d\ge1\), perform complete integer-bitset XOR Gaussian elimination on **all** columns of the boundary \(\partial_d\), taking the highest nonzero bit as the pivot until the column is zero or a new pivot is found. Every pivot represents a linearly independent vector in \(\mathbb F_2\); conversely a zero column is dependent on earlier ones. Thus the final pivot count is exactly \(\operatorname{rank}\partial_d\). The chain identity \(\partial_{d-1}\partial_d=0\) holds because every codimension-two face appears twice in a simplicial boundary. Therefore
\[
\beta_d=\dim C_d-\operatorname{rank}(\partial_d)-\operatorname{rank}(\partial_{d+1}).
\]
The degrees are finite and every face of the original complex is included; consequently the calculation is exhaustive, not extrapolative.

For \(r=10\), the chain-group dimensions in degrees \(0,\ldots,9\) are
\[
(40,610,4660,19720,47964,67160,52900,22360,4620,360).
\]
The corresponding boundary ranks for \(\partial_1,\ldots,\partial_9\) are
\[
(39,571,4089,15631,32333,34778,18082,4238,340).
\]
Substitution yields ordinary \(\beta_0=1\), and exactly the positive reduced Betti ranks claimed. The analogous exhaustive counts for the seven preceding rims are included in the checker output. In particular, their numbers of nonzero positive degrees are respectively \(2,2,3,3,3,4,4\), while for \(r=10\) it is \(5\). The assertions follow.

## Verification

Run `python3 verify_bidirected_wheels.py` in the directory containing the accompanying script (standard library only). Each case constructs the full face set twice by mathematically different algorithms, compares those sets for exact equality, computes every binary boundary rank, checks Euler–Poincaré equality and connectedness, and checks the complete stated Betti dictionary. The script's observed output is reproduced in `verification_output.txt`; the final line is `BIDIRECTED_WHEEL_FIRST_FIVE_DEGREES_EXACT_GF2_VERIFIED`. At the largest case the direct and independent enumerators agree on all \(220395\) faces, including the empty face. The complete exact boundary ranks, not sampled columns or numerical approximations, are checked.

## Relationship to prior work

Caputi, Collari, Di Trani and Smith introduced systematic homotopy classifications for multipath complexes of oriented paths, polygons, small grids and transitive tournaments [1]. Caputi, Collari and Smith later calculated the homology of **bidirectional polygons without a hub** [2]. Their Theorem 2.10 has a different source digraph, and adjoining a spoke from a new hub to every rim vertex changes the permitted arc faces; the polygon theorem does not yield the displayed wheel table. Other existing same-underlying-wheel calculations for **discrete Morse complexes** concern a different simplicial complex and do not determine multipath homology. An earlier universal top-homology theorem implies the highest-degree rank \(2r\) for these wheels, including \(20\) at \(r=10\); the new information here lies in the four lower nonzero degrees and the exact finite cutoff in support width. The classification is for a precisely specified eight-member family and not a theorem for all wheels.

## Limitations

All homology coefficients are \(\mathbb F_2\). This study does not determine torsion in integral homology, homotopy type, or wheel sizes beyond ten rim vertices. The asserted word *first* means first **within the exact ordered wheel family** starting at the smallest simple wheel; the computations do not establish a general formula or monotonicity for larger rims. The complete finite scripts provide checkable computational proofs, but the conclusions have not undergone independent mathematical auditing. Unindexed equivalent literature remains possible.

## References

[1] L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, initial public preprint 9 August 2022, arXiv:2208.04656, https://arxiv.org/abs/2208.04656.

[2] L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, initial public preprint 9 January 2026, arXiv:2601.05670, https://arxiv.org/abs/2601.05670.
