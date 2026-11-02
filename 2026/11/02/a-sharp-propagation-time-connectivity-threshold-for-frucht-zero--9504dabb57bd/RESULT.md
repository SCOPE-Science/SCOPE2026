# A sharp propagation-time connectivity threshold for Frucht zero-forcing exchanges

## Finding

Let \(F\) be the twelve-vertex Frucht graph, with the labeled edge set in the next section. An *efficient* minimum zero-forcing set means one attaining the smallest parallel propagation time among all minimum zero-forcing sets. For each integer \(t\), let \(\mathcal Z_{\le t}(F)\) have as vertices the minimum zero-forcing sets whose parallel propagation time is at most \(t\). Join two vertices when their underlying four-element sets differ by exactly one vertex (unrestricted token jumping).

**Theorem.** The zero-forcing number of \(F\) is \(4\), and its \(89\) minimum zero-forcing sets have propagation-time distribution
\[
(\#\{B:\operatorname{pt}(F,B)=j\})_{j=3}^{6}=(8,32,43,6),
\]
respectively. There are no minimum zero-forcing sets with any other propagation time. For \(t<3\), the filtered graph is empty. The complete connectivity and metric filtration is:

| Allowed time \(t\) | Vertices | Edges | Component orders | Diameter if connected |
| --- | ---: | ---: | --- | ---: |
| \(3\) | 8 | 10 | \(6,2\) | not defined |
| \(4\) | 40 | 100 | \(40\) | 8 |
| \(5\) | 83 | 322 | \(83\) | 6 |
| \(t\ge6\) | 89 | 366 | \(89\) | 6 |

More precisely, the efficient-set graph is
\[
\mathcal Z_{\le3}(F)\cong(C_3\square K_2)\sqcup K_2.
\]
In particular, the unrestricted zero-forcing exchange graph is connected, but its efficient-set induced subgraph is disconnected; allowing **one** extra forcing round is necessary and sufficient for connectedness. The four-round connected graph has diameter \(8\), larger than the unrestricted diameter \(6\). The minimum exchange distance between the two efficient-set components, when intermediate configurations of at most four rounds are allowed, is exactly \(4\).

## Assumptions and scope

All graphs are finite, simple and undirected. Use the following labeling of the Frucht graph \(F\) on \(\{0,1,\ldots,11\}\):

```text
(0,1) (0,6) (0,7) (1,2) (1,7) (2,3) (2,8) (3,4) (3,9)
(4,5) (4,9) (5,6) (5,10) (6,10) (7,11) (8,9) (8,11) (10,11)
```

This is isomorphic to the Hamiltonian-cycle LCF representation

```text
[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]
```

(the explicit relabeling is checked in the independent verifier). Initially the vertices of \(B\) are colored blue. At each *parallel* round, every currently blue vertex with exactly one currently white neighbor forces that neighbor blue; all permitted forces use the coloring at the start of the round. Let \(\operatorname{pt}(F,B)\) be the least number of rounds before every vertex becomes blue, and infinity if the process stalls. A minimum zero-forcing set has smallest cardinality among all forcing sets. The induced exchange graphs allow one selected vertex to be replaced by **any** unselected vertex, not necessarily an adjacent graph vertex. No assertion here concerns positive-semidefinite or skew zero forcing, and the theorem is specific to this Frucht graph.

## Proof

**1. Zero forcing is equivalent to meeting every fort.** A nonempty vertex set \(U\) is a *fort* when each vertex outside \(U\) has either zero or at least two neighbors in \(U\). If a forcing process stops with nonempty white set \(U\), this set is a fort. Conversely, if the initial blue set is disjoint from a fort, no vertex of that fort can ever be forced: take the first hypothetically forced vertex and use the fact that the force's source has either zero or at least two neighbors in the still-white fort. Thus a set is zero forcing exactly when it intersects every inclusion-minimal fort.

The standalone program `verify_forts.py` enumerates all \(2^{12}-1=4095\) nonempty subsets in a distinct LCF labeling, finds precisely \(851\) forts and \(66\) inclusion-minimal forts, and checks every candidate of cardinality at most four against them. No set of cardinality below four hits all minimal forts; exactly \(89\) four-sets do. This establishes \(Z(F)=4\), with exhaustive rather than sampled coverage.

**2. Exact propagation times.** For a blue set \(S\), define \(\Phi(S)\) to add simultaneously every white vertex that is the unique white neighbor of a blue vertex in \(S\). Since no eligible force can prevent another eligible force from becoming blue, iterating \(\Phi\) gives the minimum possible parallel propagation time under the stated rule. The direct verifier enumerates the \(299\) candidates of sizes below four and the \(495\) four-element candidates, and applies this recurrence. It finds precisely \(89\) forcing four-sets, with round counts \(3:8\), \(4:32\), \(5:43\), \(6:6\). The independent fort verifier builds the same invariant distributions from its different graph labeling and set-based recurrence. After applying the independently checked LCF-to-edge-list isomorphism, it also reproduces the exact roster of all \(89\) four-sets, with SHA-256 `ced4bd0df213493a9ce37d11a5d15d181998edcdc493efe0d439870c99d57d1b` for their sorted integer-mask representation.

**3. Every legal exchange and the connectivity cutoff.** Because all minimum sets have cardinality four, two distinct sets are adjacent exactly when their intersection has cardinality three. The direct verifier checks all \(\binom{89}{2}=3916\) unordered pairs. It obtains \(366\) edges, then restricts this exact edge relation to propagation-time sublevel sets. Exhaustive connected-component searches give precisely the orders in the table. The six-vertex efficient component has nine edges, is cubic, and consists of two vertex-disjoint triangles joined by three cross-edges, hence is \(C_3\square K_2\). The other two efficient sets form one edge. At time four, the complete induced 40-vertex graph is connected, establishing the sharp one-round threshold.

**4. Metric calculations and explicit bridge.** Breadth-first search from every allowed configuration yields diameters \(8\), \(6\), \(6\) for thresholds four, five, and six. At threshold four, the least distance between the two formerly disconnected efficient components is \(4\). An explicit valid bridge, listed as selected vertex labels, is

```text
{3,4,5,6} -> {3,5,6,10} -> {1,5,6,10} ->
{0,1,6,10} -> {0,1,7,10}.
```

Its propagation times are \(3,4,4,4,3\) in order; the global minimum crossing distance of four is independently certified by the complete breadth-first-search comparison. The scripts contain all boundary conditions and numerical assertions needed to reproduce the certificate without external libraries.

## Verification

Execute the two complete standalone programs using ordinary Python 3:

```text
python verify_direct.py
python verify_forts.py
```

Their successful outputs are:

```text
DIRECT_ALL_794_CANDIDATES_OF_SIZE_AT_MOST_FOUR_PASS
FRUCHT_89_SETS_366_EXCHANGES_FAST_PRISM_PLUS_EDGE_PASS
LCF_FORT_HYPERGRAPH_AND_PARALLEL_TIMES_PASS
MINIMAL_FORTS 66 ALL_FORTS 851
INDEPENDENT_FOUR_SPEED_LEVELS_PASS
```

The programs use different vertex constructions, different forcing-set recognition (direct propagation versus independent minimal-fort hitting), and separate exchange-graph algorithms. The explicit mapping between their labeled graphs is checked. This is a finite exhaustive certificate: it proves this graph's exact counts and distances, not a theorem about arbitrary asymmetric cubic graphs.

## Relationship to prior work

The standard zero-forcing rule originates in the 2008 minimum-rank literature. Hogben, Huynh, Kingsley, Meyer, Walker and Young formalized parallel propagation time and efficient minimum zero-forcing sets, proving in particular that connected nontrivial graphs possess at least two efficient sets (arXiv:1410.4191v1, Sections 1–2). Geneson, Haas and Hogben subsequently defined the single-vertex-replacement zero-forcing reconfiguration graph and studied its connectivity on general families (arXiv:2009.00220v1). Neither inspected work supplies the Frucht speed-filtered exchange graph, its triangular-prism-plus-edge optimum, or the one-round connectivity cutoff. The established definitions and general results are not claimed as new.

The Frucht graph is a classical twelve-vertex cubic graph with trivial automorphism group; its lack of graph symmetry makes an exact speed-versus-exchange analysis especially informative. The novelty claim is strictly the combined finite filtration and its structural threshold, not the individual definitions or a general theory of graph reconfiguration.

## Limitations

The proof is specific to the stated graph and the synchronous standard forcing rule. It uses an exhaustive finite certificate and does not establish a family-wide bound, a minimal-counterexample theorem among all graphs, or any independent formal verification. A possible unindexed historical tabulation of Frucht zero-forcing sets or a speed-filtered reconfiguration study under other terminology remains an originality risk. Scientific completeness of the finite search does not establish historical uniqueness.

## References

1. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648, DOI 10.1016/j.laa.2007.10.009.
2. L. Hogben, M. Huynh, N. Kingsley, S. Meyer, S. Walker, M. Young, *Propagation time for zero forcing on a graph*, arXiv:1410.4191v1, first posted 2014-10-15; https://arxiv.org/abs/1410.4191.
3. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1, first posted 2020-09-01; https://arxiv.org/abs/2009.00220.
4. E. W. Weisstein, *Frucht Graph*, MathWorld; https://mathworld.wolfram.com/FruchtGraph.html (graph description and LCF notation).
