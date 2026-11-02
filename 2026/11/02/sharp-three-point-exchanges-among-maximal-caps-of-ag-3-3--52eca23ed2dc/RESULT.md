# Sharp three-point exchanges among maximal caps of \(AG(3,3)\)

## Finding

Let \(V=\mathbb F_3^3\), and let \(\mathcal C\) be the collection of its largest subsets containing no three distinct collinear points (maximum *caps*). For positive \(r\), put two distinct caps \(C,C'\) adjacent in the \(r\)-exchange graph when \(|C\setminus C'|=|C'\setminus C|=r\). The following is one exact classification theorem for the first mobile exchange graph.

Every cap in \(\mathcal C\) has size \(9\), and \(|\mathcal C|=2106\). The \(1\)- and \(2\)-exchange graphs have no edges. The \(3\)-exchange graph \(X\) is connected, is regular of degree \(72\), has \(75816\) edges, and has diameter and radius exactly \(4\).

For **every** \(C\in\mathcal C\), the numbers of caps \(C'\) at distance \(d_X(C,C')=j\), subdivided by their intersection sizes \(t=|C\cap C'|\), are exactly:

| Exchange distance \(j\) | Intersection size \(t\) | Number of caps |
| --- | --- | ---: |
| 0 | 9 | 1 |
| 1 | 6 | 72 |
| 2 | 3, 4, 5 | 576, 522, 108 |
| 3 | 1, 2, 3 | 153, 648, 24 |
| 4 | 0 | 2 |

In particular, **distance four is equivalent to disjointness**. The two caps at distance four from \(C\) are precisely its two disjoint partners in the unique partition of \(V\) into three maximum caps. Both the existence and uniqueness of this partition were previously known; the new assertion is its exact relationship to the exchange metric. Also, the \(24\) caps meeting \(C\) in three points yet lying at distance three show that set-intersection size alone does not determine exchange distance.

The established facts that the maximum size is \(9\), that maximal caps are affinely equivalent, and that each lies in a unique three-cap partition are not claimed as new. The contribution is the sharp first-mobile move size and complete \(3\)-exchange metric profile.

## Assumptions and scope

Coordinates are ternary and labels are literal integers \(0\le v<27\), with \(v\) corresponding to \((v\bmod3,\lfloor v/3\rfloor\bmod3,\lfloor v/9\rfloor\bmod3)\in V\). For distinct \(a,b\), the unique third point on their line is \(c=-a-b\), with operations in \(\mathbb F_3^3\). A nine-element subset is a cap exactly when it contains none of the \(117\) three-point affine lines. Exchange size counts removed vertices, not the total symmetric-difference cardinality (which is twice the exchange size). There is no claim for higher dimensions or nonmaximum caps.

## Proof

**Exhaustive universe and optimum.** The following two bounded exact certificates each enumerate the full \(27\)-point affine geometry directly. The Python certificate recursively builds every line-free subset in increasing label order through cardinality \(10\). Its internal forbidden-point mask is extended after selecting \(x\) by all third points \(-x-y\) for previously selected \(y\). A branch is retained exactly when it has no forbidden chosen point. It reaches exactly \(2106\) line-free subsets of size nine and none of size ten. Any cap of more than ten points would contain a ten-cap, so nine is the maximum size. The C++ certificate independently visits all \(\binom{27}{9}=4686825\) nine-element subsets using fixed-popcount bitmasks; it tests them against the \(117\) affine-line masks, finds the same \(2106\) caps, then checks that none extends to ten points. Thus both the search space and the maximality test are exhaustive, with no symmetry reduction.

**Exchange edges.** Two nine-caps have exchange size \(r\) precisely when their intersection size is \(9-r\). Directly comparing all \(\binom{2106}{2}\) unordered cap pairs gives the following exact pair-intersection census: for intersection size \(t=0,1,2,3,4,5,6\), respectively, the numbers of unordered pairs are \(2106,161109,682344,631800,549666,113724,75816\). There are no intersections of size seven or eight. Therefore no one- or two-point exchange is possible and the three-point exchange graph has exactly \(75816\) edges. Each cap meets exactly \(72\) others in six points, establishing regularity. The other certificate constructs all neighbors instead by removing three selected points and inserting three unselected points, retaining precisely replacements that appear in the independently enumerated cap dictionary; it reproduces the edge count and degree.

**Metric.** Both certificates generate the entire exact adjacency graph and run breadth-first search from *each* of its \(2106\) vertices. For every start vertex, the joint histogram of BFS distance and intersection size is exactly the displayed table. Its entries sum to \(2106\), so each search reaches every vertex; hence the graph is connected. The maximum distance in each search is four, establishing both diameter and radius four. The distance-four bin contains exactly two caps, both disjoint from the root; the intersection census supplies exactly two disjoint caps per root. Follett et al., Proposition 2.2, independently establishes that the two disjoint partners and the root partition the affine space, so the claimed geometric interpretation is justified. All assertions are finite, exact, and reproducible using the standalone artifacts `verify.py` and `verify_alt.cpp`.

## Verification

Run `python3 verify.py`, or compile and execute `g++ -O3 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt`. The first program uses backtracking and pairwise intersection to construct exchanges; the second uses all fixed-size subsets and direct three-for-three replacements. Both check every start vertex in breadth-first search rather than extrapolating from a sample. Their expected final markers are `ALL_VERIFY_OK` and `INDEPENDENT_VERIFY_OK`. The complete joint distance/intersection profile, not only its marginal diameter, is asserted inside both programs.

## Relationship to prior work

Follett, Kalail, McMahon, Pelland and Won established the size-nine bound, affine equivalence, and the unique three-cap partition for \(AG(3,3)\) in Proposition 2.2 of their 2013 preprint (published in *Discrete Mathematics* 337, 2014). That result does not state an exchange operation, a minimal exchange size, a three-swap adjacency graph, or its shortest-path distances. In the same paper, the rest of the analysis concerns the 20-point caps and partitions of \(AG(4,3)\). Awan, Frechette, Li and McMahon study the dimension-four demicap and partition structure; their Proposition 3.1 and Table 1 include the known fact that each outside point completes two secants to an \(AG(3,3)\) maximal cap, but no maximum-nine-cap three-exchange metric. These facts have been separated from the novel metric classification, rather than counted as new. The alternative viewpoint of maximum independent sets in the 27-point affine Steiner triple system was also considered for possible implication coverage; no covering theorem was found in the inspected sources.

## Limitations

The theorem is a finite exact classification of \(AG(3,3)\), not a general reconfiguration theorem for \(AG(n,3)\). The proof is computer-assisted by exhaustive deterministic enumeration; the two complete programs supply the critical finite certificates, and neither an unchecked numerical sampling nor an asymptotic inference is used. The literature check cannot rule out equivalent statements under an unindexed association-scheme or finite-geometric-graph name; no independent scholarly priority assessment has been performed.

## References

1. Michael Follett, Kyle Kalail, Elizabeth McMahon, Catherine Pelland, and Robert Won, *Partitions of \(AG(4,3)\) into Maximal Caps*, first public arXiv version 2013-02-19, arXiv:1302.4703, DOI:10.1016/j.disc.2014.08.002. Particularly Section 2, Proposition 2.2. https://arxiv.org/html/1302.4703v1
2. Jordan Awan, Claire Frechette, Yumi Li, and Elizabeth McMahon, *Demicaps in \(AG(4,3)\) and Their Relation to Maximal Cap Partitions*, arXiv:2106.14141, 2021. Particularly Sections 1–3, Proposition 3.1 and Table 1. https://arxiv.org/pdf/2106.14141
