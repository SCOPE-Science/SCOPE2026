# Minimum zero-forcing sets of the Heawood graph: a Fano-incidence classification

## Finding
Let \(H\) be the point–line incidence graph of the Fano plane \(\mathrm{PG}(2,2)\). Its zero-forcing number is \(Z(H)=6\). A six-vertex set \(B\) is a minimum zero-forcing set **if and only if** all three conditions hold:

1. \(B\) contains three point vertices and three line vertices;
2. its three points are noncollinear and its three lines are nonconcurrent;
3. at least three of the nine possible selected point–line pairs are incident.

There are exactly \(700\) such sets. Under the full \(336\)-element automorphism group of \(H\), they constitute five orbits, classified by their induced subgraphs, as follows.

| Induced graph on \(B\) | Number of sets | Incidences | Parallel propagation time | Degree in the exchange graph |
|:--|--:|--:|--:|--:|
| \(C_6\) | 28 | 6 | 2 | 18 |
| \(P_6\) | 168 | 5 | 2 | 18 |
| \(P_5\sqcup K_1\) | 168 | 4 | 3 | 17 |
| \(2P_3\) | 168 | 4 | 3 | 16 |
| \(P_4\sqcup 2K_1\) | 168 | 3 | 3 | 14 |

Here \(P_j\) denotes a path on \(j\) vertices, \(C_j\) a cycle, and \(K_1\) an isolated vertex. Thus the \(700\) optimum sets split into \(196\) with propagation time \(2\) and \(504\) with propagation time \(3\). Exactly \(84\) balanced noncollinear/nonconcurrent pairs fail: their induced subgraph is \(2K_2\sqcup 2K_1\), with only two incidences.

Connect two minimum sets when one selected vertex can be exchanged for one unselected vertex. This minimum-basis exchange graph is connected, has \(700\) vertices and \(5712\) edges, and has diameter \(6\). The numbers of unordered distinct pairs at exchange distances \(1,2,3,4,5,6\) are respectively \(5712,34524,86184,87192,28056,2982\).

## Assumptions and scope
All graphs are finite, undirected, and simple. Represent the seven Fano points by nonzero vectors of \(\mathbb F_2^3\), labeled \(1,\ldots,7\). A Fano line is a three-point set \(\{a,b,c\}\) satisfying \(a\oplus b\oplus c=0\), where \(\oplus\) is bitwise addition. The graph \(H\) is bipartite, with a point adjacent to each of its three incident lines; it has \(14\) vertices, \(21\) edges, is cubic, and has girth \(6\).

A black vertex with exactly one white neighbor may force it black. A set is *zero forcing* if successive legal forces turn all vertices black. Its *parallel propagation time* is the number of synchronous rounds when every currently available force is performed in each round. The exchange graph refers only to minimum (cardinality-six) zero-forcing sets, not to all zero-forcing sets.

## Proof
**Finite reduction.** Each of the \(7\) Fano lines is a triple of distinct nonzero vectors whose bitwise sum is zero. The verifier constructs these seven lines, their \(14\)-vertex incidence graph, and the exact integer neighbor masks. A parallel step adds to the current black mask every unique white neighbor of a black vertex. If the step adds no vertex, the process has reached its terminal fixed point. All updates are monotone; every legal sequential force is eventually included by this closure, and conversely every parallel addition is a legal force at the start of its round. Hence this algorithm decides the zero-forcing property exactly for every subset.

**Minimum and geometric criterion.** The checker tests every subset of size at most five (\(3473\) subsets in all) and finds that none forces \(H\). It then tests every one of the \(\binom{14}{6}=3003\) six-subsets, finding exactly \(700\) that force all vertices. As an independent formulation, there are \(\binom73-7=28\) noncollinear triples of points and \(28\) nonconcurrent triples of lines. The checker examines all \(28\cdot28=784\) combinations. Precisely \(700\) have at least three selected incidences and \(84\) have exactly two. The former \(700\) are exactly the \(700\) forcing six-subsets; the latter \(84\) all fail. This proves all three conditions in both directions, as well as \(Z(H)=6\). An independent one-force-at-a-time implementation agrees on all \(3003\) six-subsets.

**Symmetry and shape classification.** Every invertible linear map on \(\mathbb F_2^3\) induces a point/line preserving incidence automorphism; there are \((2^3-1)(2^3-2)(2^3-4)=168\) of them. Orthogonality under the nondegenerate standard dot product induces an incidence-preserving point–line duality. These generate \(336\) distinct automorphisms, each of whose fourteen neighbor sets is checked. Since the connected bipartite graph has a unique bipartition up to interchange and every incidence-preserving point permutation is a Fano collineation, these are all automorphisms. Orbit generation partitions the \(700\) successful sets into the five rows above and the \(84\) failed candidate pairs into one additional orbit. Explicit induced degree sequences distinguish the two four-incidence rows. Running the synchronous forcing closure for one representative of each orbit gives the propagation column; orbit invariance extends it to every member.

**Exchange metric.** Generate all six-subsets differing from a successful set by one deletion and one addition; retain precisely those among the \(700\) successful sets. These are exactly the exchange graph edges, by definition. Their enumerated undirected degree sum is \(11424\), proving \(5712\) edges. Breadth-first search from each of its \(700\) vertices reaches every other vertex and yields the exact six-entry distance distribution in the finding. Its histogram sums to \(\binom{700}{2}=244650\), proving connectedness and diameter \(6\).

All loops are over finite, explicitly bounded sets and use integer or set arithmetic. The included verifier carries out every stated enumeration and assertion; the claims concern this graph, not a conjectured infinite pattern.

## Verification
Run `python3 verify.py` with Python 3.8 or later; it needs only the standard library. A successful run prints `VERIFY_OK` after checking the cardinality-six forcing census and lower sizes, the point–line characterization, the independent sequential forcing rule, the full symmetry action, the five successful induced-shape classes, the propagation-time split, and all exchange-graph distances. The checker constructs the graph internally from the Fano incidence axiom; no external data files or previously computed tables are necessary.

## Relationship to prior work
Hogben, Huynh, Kingsley, Meyer, Walker, and Young formalize zero-forcing propagation time and its extrema over minimum sets (arXiv:1410.4191, first publicly available 2014-10-15). Their inspected manuscript supplies the definition and general principles, not the five-orbit Heawood classification. Gentner and Rautenbach give a general girth-six lower bound, \(Z(G)\ge (g-2)(\delta-2)+2\) for \(g=6\), which gives \(Z(H)\ge6\) for this cubic graph (arXiv:1608.00747). That bound does not imply the \(700\)-set enumeration, geometric forcing criterion, propagation split, or exchange distances. Deaett and Hall (arXiv:1708.07741, Section 2) already use ordinary zero forcing in the determination of the Heawood minimum rank, and the value \(Z(H)=6\) is not claimed as new here. Their inspected manuscript treats semidefinite representations and the positive-semidefinite variant \(Z_+(H)=5\), not the exact ordinary-forcing basis family, its five orbits, its propagation split, or its exchange geometry. The finite-projective-plane, zero-forcing, and reconfiguration terminologies were also searched for equivalent numerical classifications.

## Limitations
This is an exact, finite graph result. It does not classify zero-forcing sets larger than six or prove an analogous characterization for higher-order projective planes. Exhaustive checks establish the stated finite classifications but do not exclude an unindexed earlier enumeration; that remains an originality risk.

## References
1. L. Hogben, M. Huynh, N. Kingsley, S. Meyer, S. Walker, and M. Young, *Propagation time for zero forcing on a graph*, arXiv:1410.4191, v1 2014-10-15, https://arxiv.org/abs/1410.4191.
2. M. Gentner and D. Rautenbach, *Some Bounds on the Zero Forcing Number of a Graph*, arXiv:1608.00747, v1 2016-08-02, https://arxiv.org/abs/1608.00747.
3. L. Deaett and H. T. Hall, *Orthogonal representations of Steiner triple system incidence graphs*, arXiv:1708.07741, v1 2017-08-25, https://arxiv.org/abs/1708.07741.
